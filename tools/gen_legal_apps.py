"""Per-app legal pages: /<slug>/privacy, /<slug>/terms and /<slug>/support for seven apps.

One generator, one config module per app (tools/legal_apps/<slug>.py). Replaces gen_legal_cycle.py,
gen_legal_atino.py and gen_legal_roomy.py (22/10/2026). Every page is stand-alone on purpose: no studio
chrome, no shared site.css, no links to other apps. Each app gets its own small stylesheet built from its
own accent, in light and dark.

Files written per page:  <slug>/<page>.html  (GitHub Pages also serves it as /<slug>/<page>)
Shipped builds that link a directory URL (/atino/privacy/, /atino/privacidad/, /roomy/privacy/) also get a
full copy at <slug>/<page>/index.html, because Pages serves /foo from foo.html and /foo/ from foo/index.html
and neither covers the other. Both copies carry the same text and the same canonical (the .html one).

Colours. Each theme gives the app's declared accent as `mark` (borders, theme-color). Link and nav text uses
`accent`, which is the mark itself when it reaches 4.5:1 on the page and on the tinted summary panel, and
otherwise a darker (light mode) or lighter (dark mode) variant of the same hue, found here by walking HSL
lightness. build() refuses to write if any text/background pair is under 4.5:1; the table is printed by
`python3 tools/gen_legal_apps.py --contrast` (and by tools/check_contrast.py).

Adjusted text colours as of 22/10/2026 (declared accent -> text/link colour, light mode unless noted):
Tempo #007AFF -> #006BE0 (dark #1083FF), Atino #FFB547 -> #A36100, Roomy #C9E64A -> #687C11,
GamingHub #0077FF -> #006AE2, Overbit #6FC1DD -> #247B99. Readably, and the dark modes of Atino, Roomy,
GamingHub and Overbit use the declared accent unchanged.

Cycle does not use this template at all: its config says `renderer='cycle_layout'` and build_app() hands its pages to
legal_apps/cycle_layout.py (own HTML, own `cy-` classes, own stylesheet). Its colours are measured from the generated
CSS by cycle_layout.audit(), in build_apps() and in print_contrast().

`live`: True once the app is on sale (same moment as `appstore=` in gen_site.py's APPS: today Cycle Timers and Tempo).
Until then the page links to nothing on apps.apple.com, because that URL answers 404.

Run alone (`python3 tools/gen_legal_apps.py`) or through `python3 tools/gen_site.py`.
"""
import colorsys, importlib, os, sys

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
HOST = 'https://seizeapps.com/'
SLUGS = ['cycle', 'tempo', 'readably', 'atino', 'roomy', 'gaminghub', 'overbit']
MIN = 4.5

# ---------------------------------------------------------------- colour maths (WCAG 2.x)
def rgb(h):
    h = h.lstrip('#'); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
def hexs(c): return '#%02X%02X%02X' % tuple(max(0, min(255, round(v))) for v in c)
def lum(h):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = rgb(h); return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)
def ratio(a, b):
    la, lb = lum(a), lum(b)
    if la < lb: la, lb = lb, la
    return (la + 0.05) / (lb + 0.05)
def mix(base, top, t):
    a, b = rgb(base), rgb(top); return hexs([a[i] + (b[i] - a[i]) * t for i in range(3)])

def text_variant(mark, bg, soft, dark):
    """The mark itself if it passes on page and panel; else the same hue/saturation, lightness walked."""
    if min(ratio(mark, bg), ratio(mark, soft)) >= MIN: return mark
    r, g, b = [v / 255 for v in rgb(mark)]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    step = 0.004 if dark else -0.004
    while 0 < l < 1:
        l += step
        c = hexs([v * 255 for v in colorsys.hls_to_rgb(h, l, s)])
        if min(ratio(c, bg), ratio(c, soft)) >= MIN: return c
    raise SystemExit(f'no accessible variant of {mark} on {bg}')

def resolve(theme):
    """theme = {'light': {...}, 'dark': {...}} -> same, with soft and accent filled in."""
    out = {}
    for mode in ('light', 'dark'):
        t = dict(theme[mode]); dark = mode == 'dark'
        t.setdefault('soft', mix(t['bg'], t['mark'], 0.14 if dark else 0.08))
        t['accent'] = t.get('accent') or text_variant(t['mark'], t['bg'], t['soft'], dark)
        out[mode] = t
    return out

def pairs(t):
    return [('body text on page', t['fg'], t['bg']), ('body text on summary panel', t['fg'], t['soft']),
            ('muted text on page', t['muted'], t['bg']), ('muted text on summary panel', t['muted'], t['soft']),
            ('link / nav text on page', t['accent'], t['bg']), ('link / nav text on summary panel', t['accent'], t['soft'])]

def contrast_table(apps):
    rows, ok = [], True
    for a in apps:
        if a.get('renderer'): continue
        th = resolve(a['theme'])
        for mode in ('light', 'dark'):
            t = th[mode]
            rs = [(n, ratio(f, b)) for n, f, b in pairs(t)]
            ok &= all(r >= MIN for _, r in rs)
            rows.append((a['name'], mode, t['mark'], t['accent'], t['bg'], t['soft'], rs))
    return rows, ok

def print_contrast(apps):
    rows, ok = contrast_table(apps)
    print('| App | Mode | Declared accent | Text/link colour | Page bg | Panel | Body/page | Body/panel | Muted/page | Muted/panel | Link/page | Link/panel |')
    print('|---|---|---|---|---|---|---|---|---|---|---|---|')
    for name, mode, mark, acc, bg, soft, rs in rows:
        note = '' if mark == acc else ' (adjusted)'
        print(f'| {name} | {mode} | {mark} | {acc}{note} | {bg} | {soft} | ' + ' | '.join(f'{r:.2f}' for _, r in rs) + ' |')
    print('all pairs >= 4.5:1' if ok else 'FAIL: a pair is under 4.5:1')
    for a in apps:
        if a.get('renderer'): ok &= print_own_contrast(a)
    return ok


def renderer(app):
    return importlib.import_module(f'legal_apps.{app["renderer"]}')


def print_own_contrast(app):
    """Apps with their own renderer: measure the CSS of the pages as written to disk (all three, both modes)."""
    mod, ok = renderer(app), True
    print(f'\n{app["name"]} (own layout, measured from {app["slug"]}/*.html)\n')
    seen = {}  # the three pages share one stylesheet: print each distinct table once
    for key in sorted(k for _, k in app['pages']):
        path = os.path.join(SITE, app['slug'], f'{key}.html')
        if not os.path.isfile(path):
            print(f'MISSING {path}: run tools/gen_site.py'); return False
        rows, good = mod.audit(open(path, encoding='utf-8').read()); ok &= good
        seen.setdefault(tuple(rows), []).append(key)
    print('| Pages | Mode | Pair | Foreground | Background | Ratio |')
    print('|---|---|---|---|---|---|')
    for rows, keys in seen.items():
        for mode, label, fg, bg, r in rows:
            print(f'| {", ".join(keys)} | {mode} | {label} | {fg} | {bg} | {r:.2f}{"" if r >= MIN else " FAIL"} |')
    print('all pairs >= 4.5:1' if ok else 'FAIL: a pair is under 4.5:1')
    return ok

# ---------------------------------------------------------------- page chrome
CSS = '''
:root{--mark:%(l_mark)s;--accent:%(l_accent)s;--bg:%(l_bg)s;--fg:%(l_fg)s;--muted:%(l_muted)s;--line:%(l_line)s;--soft:%(l_soft)s;color-scheme:light dark}
@media (prefers-color-scheme:dark){:root{--mark:%(d_mark)s;--accent:%(d_accent)s;--bg:%(d_bg)s;--fg:%(d_fg)s;--muted:%(d_muted)s;--line:%(d_line)s;--soft:%(d_soft)s}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%%}
body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.6 -apple-system,BlinkMacSystemFont,"Helvetica Neue",Helvetica,Arial,sans-serif}
.wrap{max-width:720px;margin:0 auto;padding:0 20px}
header{border-bottom:1px solid var(--line)}
header .wrap{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:8px 16px;padding-top:14px;padding-bottom:14px}
.brand{display:flex;align-items:center;gap:10px;font-weight:700;font-size:18px;color:var(--fg);text-decoration:none}
.brand img{width:32px;height:32px;border-radius:8px}
nav a{color:var(--muted);text-decoration:none;margin-left:16px;font-size:15px}
nav a:first-child{margin-left:0}
nav a[aria-current=page]{color:var(--accent);font-weight:600}
main{padding:32px 0 48px}
h1{font-size:32px;line-height:1.2;margin:0 0 4px}
h2{font-size:20px;margin:32px 0 8px}
h3{font-size:17px;margin:20px 0 4px}
p,li{margin:0 0 12px}
ul{padding-left:22px}
a{color:var(--accent)}
.updated{color:var(--muted);font-size:15px;margin-bottom:24px}
.summary{background:var(--soft);border-left:4px solid var(--mark);border-radius:8px;padding:14px 16px;margin:0 0 8px}
.contact{font-size:20px;font-weight:600}
footer{border-top:1px solid var(--line);color:var(--muted);font-size:14px}
footer .wrap{padding-top:20px;padding-bottom:32px}
footer a{color:var(--muted)}
'''

UI = {
    'en': dict(lang='en', pages=[('privacy', 'Privacy'), ('terms', 'Terms'), ('support', 'Support')],
               foot=[('privacy', 'Privacy Policy'), ('terms', 'Terms of Use'), ('support', 'Support')],
               store='{name} on the App Store', by='{name} by {publisher} · Basque Country, Spain · {mail}'),
    'es': dict(lang='es', pages=[('privacidad', 'Privacidad'), ('terms', 'Terms'), ('support', 'Support')],
               foot=[('privacidad', 'Política de privacidad'), ('terms', 'Terms of Use'), ('support', 'Support')],
               store='{name} en el App Store', by='{name} de {publisher} · País Vasco, España · {mail}'),
}


def rel_base(depth):
    """Path from a page `depth` folders under the site root to its app folder."""
    return '' if depth == 1 else '../' * (depth - 1)


def page(app, th, lang, key, title, desc, body, depth, alts):
    u = UI[lang]; root = '../' * depth; base = rel_base(depth); slug = app['slug']
    icon = f'{root}assets/icons/{app["icon"]}'
    canon = f'{HOST}{slug}/{key}.html'
    mail = f'<a href="mailto:{app["email"]}">{app["email"]}</a>'
    nav_pages = list(u['pages'])
    nav = ''.join(f'<a href="{base}{s}.html"{" aria-current=page" if s == key else ""}>{label}</a>' for s, label in nav_pages)
    for l2, k2 in alts.items():
        if l2 != lang:
            nav += f'<a href="{base}{k2}.html" hreflang="{l2}" lang="{l2}">{"English" if l2 == "en" else "Español"}</a>'
    live = app.get('live', False)  # the App Store URL 404s until the app is on sale: no dead link on a legal page
    brand_href = app['appStoreUrl'] if live else f'{base}{nav_pages[0][0]}.html'
    store_link = f' · <a href="{app["appStoreUrl"]}">{u["store"].format(name=app["name"])}</a>' if live else ''
    foot_links = ' · '.join(f'<a href="{base}{s}.html">{label}</a>' for s, label in u['foot'])
    alt_links = ''.join(f'<link rel="alternate" hreflang="{l2}" href="{HOST}{slug}/{k2}.html">\n' for l2, k2 in alts.items())
    css = CSS % dict(l_mark=th['light']['mark'], l_accent=th['light']['accent'], l_bg=th['light']['bg'], l_fg=th['light']['fg'],
                     l_muted=th['light']['muted'], l_line=th['light']['line'], l_soft=th['light']['soft'],
                     d_mark=th['dark']['mark'], d_accent=th['dark']['accent'], d_bg=th['dark']['bg'], d_fg=th['dark']['fg'],
                     d_muted=th['dark']['muted'], d_line=th['dark']['line'], d_soft=th['dark']['soft'])
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
{alt_links}<meta name="theme-color" content="{th['light']['mark']}" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="{th['dark']['bg']}" media="(prefers-color-scheme: dark)">
<link rel="icon" href="{icon}">
<link rel="apple-touch-icon" href="{icon}">
<style>{css}</style>
</head>
<body>
<header><div class="wrap">
<a class="brand" href="{brand_href}"><img src="{icon}" alt="" width="32" height="32">{app['name']}</a>
<nav aria-label="{app['name']}">{nav}</nav>
</div></header>
<main><div class="wrap">
{body}
</div></main>
<footer><div class="wrap">
<p>{u['by'].format(name=app['name'], publisher=app.get('publisher_' + lang, app['publisher']), mail=mail)}</p>
<p>{foot_links}{store_link}</p>
</div></footer>
</body>
</html>
'''


def fill(app, text, base, lang):
    """Tokens in the bodies: @mail@ @email@ @updated@ and @<page>@ (relative link to a sibling page)."""
    text = (text.replace('@mail@', f'<a href="mailto:{app["email"]}">{app["email"]}</a>')
                .replace('@email@', app['email']).replace('@updated@', app['updated_' + lang]))
    for k in ('privacy', 'privacidad', 'terms', 'support'):
        text = text.replace(f'@{k}@', f'{base}{k}.html')
    return text


def load(slug):
    return importlib.import_module(f'legal_apps.{slug}').APP


def build_app(app):
    th = None if app.get('renderer') else resolve(app['theme'])
    slug = app['slug']
    out = os.path.join(SITE, app['slug']); os.makedirs(out, exist_ok=True)
    alts = {}  # lang -> page key, for the privacy twins
    for (lang, key), p in app['pages'].items():
        if key in ('privacy', 'privacidad'): alts[lang] = key
    if len(alts) < 2: alts = {}
    written = []
    for (lang, key), p in app['pages'].items():
        depths = [1] + ([2] if key in app.get('dir_copies', ()) else [])
        for depth in depths:
            body = fill(app, p['body'].strip(), rel_base(depth), lang)
            pair_alts = alts if key in ('privacy', 'privacidad') else {}
            if app.get('renderer'):
                mod = renderer(app)
                html = mod.page(app, lang, key, p['title'], p['desc'], body, HOST, pair_alts)
                if not mod.audit(html)[1]: raise SystemExit(f'{slug}/{key}: a colour pair is under 4.5:1')
            else:
                html = page(app, th, lang, key, p['title'], p['desc'], body, depth, pair_alts)
            path = f'{app["slug"]}/{key}.html' if depth == 1 else f'{app["slug"]}/{key}/index.html'
            full = os.path.join(SITE, path); os.makedirs(os.path.dirname(full), exist_ok=True)
            with open(full, 'w', encoding='utf-8') as f: f.write(html)
            written.append(path)
    return written


def all_apps():
    return [load(s) for s in SLUGS]


def build_apps():
    apps = all_apps()
    rows, ok = contrast_table(apps)
    if not ok:
        print_contrast(apps); raise SystemExit('legal pages: a colour pair is under 4.5:1')
    n = 0
    for a in apps: n += len(build_app(a))
    return n


if __name__ == '__main__':
    if '--contrast' in sys.argv:
        sys.exit(0 if print_contrast(all_apps()) else 1)
    print('legal app pages:', build_apps(), 'files')
