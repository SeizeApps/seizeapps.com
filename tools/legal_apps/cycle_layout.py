"""Cycle Timers' own page layout for tools/gen_legal_apps.py (slug 'cycle'). It shares no template, class name or
stylesheet with the other apps' pages (common page() in gen_legal_apps.py): everything here is prefixed `cy-`.

Identity: Cycle is a countdown ring, so every page opens on a ring (it fills 1/3, 2/3, 3/3 across Privacy, Terms,
Support), the sections are numbered cards on a grouped background (the first-party Settings look), the page
switcher is a pill bar pinned to the bottom of the screen, and the "last updated" line reads as a last-done stamp.

The text of each page lives in tools/legal_apps/cycle.py and is not touched here: page() only re-wraps it
(h1 / .updated / .summary go to the top, each <h2> becomes a card, each FAQ <h3> a question card).

Colours: accent #0E7C6B (light) / #3CC9AE (dark), nothing else in hue. audit(css) measures every foreground /
background pair the stylesheet uses, from the stylesheet itself, in both modes; gen_legal_apps.py refuses to write
a page if one is under 4.5:1 and tools/check_contrast.py prints the table from the generated files.
"""
import re

MIN = 4.5
LIGHT = dict(bg='#F4F6F5', card='#FFFFFF', soft='#EBF5F2', fg='#1C1C1E', muted='#5C5C61', line='#DDE3E1',
             track='#D3DEDB', accent='#0E7C6B', onaccent='#FFFFFF')
DARK = dict(bg='#101112', card='#1C1D1F', soft='#15302B', fg='#F2F2F7', muted='#AEAEB2', line='#303234',
            track='#2E3B38', accent='#3CC9AE', onaccent='#0A1F1B')

CSS = '''
:root{%(light)s;color-scheme:light dark}
@media (prefers-color-scheme:dark){:root{%(dark)s}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%%;scroll-padding-bottom:96px}
body.cy{margin:0;background:var(--bg);color:var(--fg);font:17px/1.55 -apple-system,BlinkMacSystemFont,"SF Pro Text","Helvetica Neue",Helvetica,Arial,sans-serif}
.cy-shell{max-width:640px;margin:0 auto;padding:28px 16px 24px}
.cy-top{text-align:center;padding:12px 0 22px}
.cy-ring{position:relative;width:132px;height:132px;margin:0 auto 14px}
.cy-ring svg{position:absolute;inset:0;width:100%%;height:100%%}
.cy-ring .cy-track{fill:none;stroke:var(--track);stroke-width:8}
.cy-ring .cy-arc{fill:none;stroke:var(--accent);stroke-width:8;stroke-linecap:round}
.cy-ring img{position:absolute;left:32px;top:32px;width:68px;height:68px;border-radius:16px}
.cy-kicker{margin:0 0 4px;font-size:15px;font-weight:600;letter-spacing:.02em}
.cy-top h1{font-size:30px;line-height:1.15;font-weight:700;letter-spacing:-.01em;margin:0 0 10px}
.cy-stamp,.cy-sub{margin:0 auto;color:var(--muted);font-size:15px;max-width:30em}
.cy-stamp::before{content:"";display:inline-block;width:.8em;height:.8em;border:2px solid var(--accent);border-radius:50%%;margin-right:.55em;vertical-align:-.05em}
.cy-short{background:var(--soft);border:1px solid var(--line);border-radius:20px;padding:16px 20px;margin:0 0 6px}
.cy-short p{margin:0}
.cy-main{counter-reset:cysec}
.cy-sec{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:18px 20px 8px;margin:14px 0}
.cy-sec h2{display:flex;align-items:center;gap:12px;font-size:19px;line-height:1.25;font-weight:650;margin:0 0 10px}
.cy-sec h2::before{counter-increment:cysec;content:counter(cysec);flex:none;display:grid;place-items:center;width:30px;height:30px;border:2px solid var(--accent);border-radius:50%%;font-size:14px;font-weight:600}
.cy-sec p,.cy-sec li{margin:0 0 12px}
.cy-sec ul{padding-left:22px}
.cy-contact{background:var(--soft)}
.cy-contact h2::before{content:"";counter-increment:none;width:30px;height:30px;border-radius:50%%;border-color:var(--accent);background:radial-gradient(circle,var(--accent) 0 28%%,transparent 31%%)}
.cy-contact .contact{font-size:20px;font-weight:600}
.cy-group{font-size:13px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:26px 8px 4px}
.cy-q{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:16px 20px 6px;margin:10px 0}
.cy-q h3{display:flex;align-items:flex-start;gap:10px;font-size:17px;line-height:1.3;font-weight:650;margin:0 0 8px}
.cy-q h3::before{content:"";flex:none;width:12px;height:12px;margin-top:.3em;border:2px solid var(--accent);border-radius:50%%}
.cy-q p{margin:0 0 12px}
a{color:var(--accent);text-underline-offset:3px}
.cy-tabs{position:sticky;bottom:14px;z-index:2;display:flex;gap:4px;width:max-content;max-width:100%%;margin:26px auto 22px;padding:5px;background:var(--card);border:1px solid var(--line);border-radius:999px;box-shadow:0 6px 24px rgba(0,0,0,.14)}
.cy-tabs a{display:block;min-width:92px;text-align:center;padding:9px 18px;border-radius:999px;color:var(--fg);text-decoration:none;font-size:15px;font-weight:600}
.cy-tabs a[aria-current=page]{background:var(--accent);color:var(--onaccent)}
.cy-tabs a:focus-visible,a:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.cy-end{text-align:center;color:var(--muted);font-size:14px;padding:0 8px}
.cy-end p{margin:0 0 8px}
.cy-end a{color:var(--muted)}
@media (max-width:420px){.cy-top h1{font-size:26px}.cy-tabs a{min-width:0;padding:9px 14px}}
'''

# (label, foreground var, background var): every text/background pair the stylesheet above can put on screen.
PAIRS = [
    ('body text on page', 'fg', 'bg'), ('body text on card', 'fg', 'card'), ('body text on tinted panel', 'fg', 'soft'),
    ('muted text on page', 'muted', 'bg'), ('muted text on card', 'muted', 'card'), ('muted text on tinted panel', 'muted', 'soft'),
    ('accent link on page', 'accent', 'bg'), ('accent link on card', 'accent', 'card'), ('accent link on tinted panel', 'accent', 'soft'),
    ('current page pill', 'onaccent', 'accent'),
]


def css():
    f = lambda d: ';'.join(f'--{k}:{v}' for k, v in d.items())
    return CSS % dict(light=f(LIGHT), dark=f(DARK))


def _vars(block):
    return dict(re.findall(r'--([a-z]+):(#[0-9A-Fa-f]{6})', block))


def audit(html):
    """Contrast of every PAIRS entry, read from the <style> of a generated page. -> (rows, ok); a row is
    (mode, label, fg, bg, ratio). Importing gen_legal_apps here (not at the top) avoids an import cycle."""
    from gen_legal_apps import ratio
    style = re.search(r'<style>(.*?)</style>', html, re.S).group(1)
    light = _vars(re.search(r':root\{([^}]*)\}', style).group(1))
    dark = dict(light, **_vars(re.search(r'prefers-color-scheme:dark\)\{:root\{([^}]*)\}', style).group(1)))
    rows = []
    for mode, v in (('light', light), ('dark', dark)):
        for label, fg, bg in PAIRS:
            rows.append((mode, label, v[fg], v[bg], ratio(v[fg], v[bg])))
    return rows, all(r[4] >= MIN for r in rows)


def _split(body):
    """h1, updated line, summary, then [(h2 html, [chunks])] where a chunk is body html between headings."""
    take = lambda pat: (lambda m: (m.group(1).strip(), body.replace(m.group(0), '', 1)) if m else ('', body))(re.search(pat, body, re.S))
    h1, body = take(r'<h1>(.*?)</h1>')
    upd, body = take(r'<p class="updated">(.*?)</p>')
    summ, body = take(r'<p class="summary">(.*?)</p>')
    parts = re.split(r'<h2>(.*?)</h2>', body)
    return h1, upd, summ, list(zip(parts[1::2], parts[2::2]))


def page(app, lang, key, title, desc, body, host, alts):
    root = '../'; slug = app['slug']
    icon = f'{root}assets/icons/{app["icon"]}'
    h1, upd, summ, secs = _split(body)
    order = ['privacy', 'terms', 'support']
    fill = (order.index(key) + 1) * 100 // len(order)
    pills = ''.join(f'<a href="{k}.html"{" aria-current=page" if k == key else ""}>{k.capitalize()}</a>' for k in order)
    stamp = (f'<p class="cy-stamp">{upd}</p>' if re.match(r'(Last updated|Effective)', upd) else f'<p class="cy-sub">{upd}</p>')
    out = []
    for i, (h, chunk) in enumerate(secs, 1):
        h = re.sub(r'^\d+\.\s+', '', h.strip()); chunk = chunk.strip()
        if '<h3>' in chunk:
            qs = re.split(r'<h3>(.*?)</h3>', chunk)
            out.append(f'<h2 class="cy-group">{h}</h2>')
            out += [f'<article class="cy-q"><h3>{q}</h3>\n{a.strip()}</article>' for q, a in zip(qs[1::2], qs[2::2])]
        else:
            cls = 'cy-sec cy-contact' if h == 'Contact' else 'cy-sec'
            out.append(f'<section class="{cls}" aria-labelledby="cy-s{i}"><h2 id="cy-s{i}">{h}</h2>\n{chunk}</section>')
    short = f'<aside class="cy-short">{"<p>" + summ + "</p>"}</aside>\n' if summ else ''
    mail = f'<a href="mailto:{app["email"]}">{app["email"]}</a>'
    by = f'{app["name"]} by {app["publisher"]} · Basque Country, Spain · {mail}'
    foot = ' · '.join(f'<a href="{k}.html">{l}</a>' for k, l in (('privacy', 'Privacy Policy'), ('terms', 'Terms of Use'), ('support', 'Support')))
    store = f' · <a href="{app["appStoreUrl"]}">{app["name"]} on the App Store</a>' if app.get('live') else ''
    kicker = f'<a href="{app["appStoreUrl"]}">{app["name"]}</a>' if app.get('live') else f'<a href="privacy.html">{app["name"]}</a>'
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{host}{slug}/{key}.html">
<meta name="theme-color" content="{LIGHT['bg']}" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="{DARK['bg']}" media="(prefers-color-scheme: dark)">
<link rel="icon" href="{icon}">
<link rel="apple-touch-icon" href="{icon}">
<style>{css()}</style>
</head>
<body class="cy">
<div class="cy-shell">
<main class="cy-main">
<header class="cy-top">
<div class="cy-ring" aria-hidden="true"><svg viewBox="0 0 120 120" focusable="false"><circle class="cy-track" cx="60" cy="60" r="52"/><circle class="cy-arc" cx="60" cy="60" r="52" pathLength="100" stroke-dasharray="{fill} 100" transform="rotate(-90 60 60)"/></svg><img src="{icon}" alt="" width="68" height="68"></div>
<p class="cy-kicker">{kicker}</p>
<h1>{h1}</h1>
{stamp}
</header>
{short}{chr(10).join(out)}
</main>
<nav class="cy-tabs" aria-label="{app['name']}">{pills}</nav>
<footer class="cy-end">
<p>{by}</p>
<p>{foot}{store}</p>
</footer>
</div>
</body>
</html>
'''
