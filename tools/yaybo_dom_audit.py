#!/usr/bin/env python3
"""Rendered-text contrast audit for the Yaybo pages (a check next to yaybo_site.audit(), which measures the declared CSS pairs).

For every visible text run it reads the computed colour and size from headless Chrome, then measures the real background behind it
in a second render of the same page with all text made transparent, so text over gradients, photos and scrims is measured on the
pixels that are actually drawn. Worst pixel (0.3th percentile) per text run; 4.5:1, or 3:1 for large text.

    python3 tools/yaybo_dom_audit.py [page ...] [--widths 1440,500] [--modes light,dark]

Pages are paths under the repo such as yaybo/index.html (default: all seven). Needs Google Chrome and Pillow. Exits 1 on any failure.
"""
import json, os, re, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
PAGES = ['yaybo/index.html'] + [f'yaybo/{d}/index.html' for d in ('privacy', 'terms', 'support', 'privacidad', 'condiciones', 'soporte')]

PROBE = r'''<script>
addEventListener('load',()=>{const out=[];const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);let n;
while(n=w.nextNode()){const t=n.nodeValue.trim();if(!t)continue;const el=n.parentElement;if(!el||/^(SCRIPT|STYLE|NOSCRIPT|TITLE)$/.test(el.tagName))continue;
const cs=getComputedStyle(el);if(cs.visibility!=='visible'||cs.display==='none')continue;
let op=1,p=el;while(p){op*=parseFloat(getComputedStyle(p).opacity);p=p.parentElement}if(op<.05)continue;
const r=document.createRange();r.selectNodeContents(n);const rs=[...r.getClientRects()].filter(b=>b.width>1&&b.height>1);if(!rs.length)continue;
const fs=parseFloat(cs.fontSize),fw=parseInt(cs.fontWeight)||400;
out.push({t:t.slice(0,40),c:cs.color,op:op,large:fs>=24||(fs>=18.66&&fw>=700),rects:rs.map(b=>[b.left+scrollX,b.top+scrollY,b.width,b.height])})}
const pre=document.createElement('pre');pre.id='yb-audit';pre.textContent=JSON.stringify({w:innerWidth,h:document.documentElement.scrollHeight,sw:document.documentElement.scrollWidth,items:out});document.body.appendChild(pre)});
</script>'''
HIDE = '<style>*{color:transparent!important;text-shadow:none!important;-webkit-text-fill-color:transparent!important;caret-color:transparent!important}</style>'


def chrome(args, mode):
    prof = tempfile.mkdtemp(prefix='yb-audit-')
    flags = [CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-first-run', f'--user-data-dir={prof}', '--virtual-time-budget=4000']
    flags += ['--blink-settings=preferredColorScheme=0', '--force-dark-mode'] if mode == 'dark' else ['--blink-settings=preferredColorScheme=1']
    r = subprocess.run(flags + args, capture_output=True, text=True)
    subprocess.run(['rm', '-r', prof])
    return r.stdout


def lin(v):
    v /= 255
    return v / 12.92 if v <= .03928 else ((v + .055) / 1.055) ** 2.4


def lum(c):
    return .2126 * lin(c[0]) + .7152 * lin(c[1]) + .0722 * lin(c[2])


def audit_page(rel, width, mode, tmp):
    from PIL import Image
    src = (ROOT / rel).read_text(encoding='utf-8').replace(' loading="lazy"', '')
    site = Path(tmp) / f'{mode}{width}'
    d = site / Path(rel).parent
    d.mkdir(parents=True, exist_ok=True)
    media = site / 'yaybo' / 'media'
    if not media.exists():
        media.parent.mkdir(parents=True, exist_ok=True)
        os.symlink(ROOT / 'yaybo' / 'media', media)
    probe, hide = d / 'probe.html', d / 'hide.html'
    probe.write_text(src.replace('</body>', PROBE + '</body>'), encoding='utf-8')
    dump = chrome([f'--window-size={width},1000', '--dump-dom', f'file://{probe}'], mode)
    m = re.search(r'<pre id="yb-audit">(.*?)</pre>', dump, re.S)
    if not m:
        return [('could not read the page', 0, 0, False)]
    import html as H
    data = json.loads(H.unescape(m.group(1)))
    shot = Path(tmp) / f'{mode}{width}-{Path(rel).parent.name}.png'
    hide.write_text(src.replace('</head>', HIDE + '</head>', 1), encoding='utf-8')
    height = data['h'] + 20
    chrome([f'--window-size={data["w"]},{height}', f'--screenshot={shot}', f'file://{hide}'], mode)
    im = Image.open(shot).convert('RGB')
    rows = []
    over = data['sw'] - data['w']
    rows.append((f'{rel} @{data["w"]} {mode}: no horizontal overflow', over, 0, over <= 0))
    for it in data['items']:
        mm = re.match(r'rgba?\(([\d.]+), ([\d.]+), ([\d.]+)(?:, ([\d.]+))?\)', it['c'])
        fg = tuple(float(mm.group(i)) for i in (1, 2, 3))
        alpha = float(mm.group(4) or 1) * it['op']
        mn = 3.0 if it['large'] else 4.5
        worst = 99.0
        for x, y, w, h in it['rects']:
            if x >= data['w'] or x + w <= 0:
                continue
            for py in range(max(0, int(y)), min(im.height, int(y + h) + 1), 2):
                for px in range(max(0, int(x)), min(im.width, int(x + w) + 1), 2):
                    bg = im.getpixel((px, py))
                    c = tuple(fg[i] * alpha + bg[i] * (1 - alpha) for i in range(3))
                    a, b = lum(c), lum(bg)
                    if a < b:
                        a, b = b, a
                    worst = min(worst, (a + .05) / (b + .05))
        if worst == 99.0:
            continue
        rows.append((f'{rel} @{data["w"]} {mode}: "{it["t"]}"', round(worst, 2), mn, worst >= mn - 0.005))
    return rows


def main():
    args = sys.argv[1:]
    widths, modes, pages = ['1440', '500'], ['light', 'dark'], []
    i = 0
    while i < len(args):
        if args[i] == '--widths':
            widths = args[i + 1].split(','); i += 2
        elif args[i] == '--modes':
            modes = args[i + 1].split(','); i += 2
        else:
            pages.append(args[i]); i += 1
    pages = pages or PAGES
    bad, total = 0, 0
    with tempfile.TemporaryDirectory(prefix='yb-site-') as tmp:
        for rel in pages:
            for w in widths:
                for mode in modes:
                    rows = audit_page(rel, w, mode, tmp)
                    fails = [r for r in rows if not r[3]]
                    total += len(rows)
                    bad += len(fails)
                    print(f'{rel} @{w} {mode}: {len(rows)} checks, {len(fails)} fail')
                    for r in fails[:12]:
                        print(f'   FAIL {r[0]} = {r[1]} (min {r[2]})')
    print(f'{total} checks, {bad} failures')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
