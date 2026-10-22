"""Atino's own site for tools/gen_legal_apps.py (slug 'atino'): the home page (key 'index') and the privacy, terms
and support pages, in one design system that shares no template, class name or stylesheet with another app.
Everything is prefixed `at-`.

Identity. "Horizon": Atino is a dark, dawn-lit app (AtinoTheme.swift), so the site is a paper page (warm white in
light, deep teal ink in dark) that opens onto dark plate windows: the app's own textless sunrise plates, its real
screenshots in CSS device frames, sunrise amber and coral used as light, teal for "you". Seize blue appears only in
the icon. Fonts are system only: ui-rounded / SF Pro Rounded / Avenir Next Rounded for display, Avenir Next for
text, Iowan Old Style / Charter / Georgia for the legal reading text.

Isolation (App Store guideline 4.3): pages link only to their own pages and media (relative, so they work from file:// and from any host),
mailto:hello@seizeapps.com, and the vendors / regulators / Apple legal pages that the legal text already names.
No apps.apple.com, no seizeapps.com home, no studio, no other app, no CDN, no script. check_isolation() enforces it
and audit() fails the build on any offender.

Colour. Every foreground/background pair of the stylesheet is measured from the generated CSS by audit(), in light
and dark; gen_legal_apps.py refuses to write if one is under 4.5:1. Text over a plate is measured against the
worst case: the brightest pixel of any plate (--peak) under the scrim alpha the text actually sits on (--sc for
copy over a plate, --pc for glass cards and pills).
"""
import re, html as _html

MIN = 4.5
SLUG = 'atino'
BASE = './'      # set per page in page(): './' beside the app folder's files, '../' in a dir copy (privacy/index.html)
MEDIA = BASE + 'media/'

LIGHT = dict(bg='#FFFDF8', lift='#FAF5EA', cream='#F8F1E4', card='#FFFFFF', ink='#1B2426', muted='#56625F',
             line='#E8E2D4', amber_text='#8A5200', teal_text='#0E6B62', focus='#8A5200')
DARK = dict(bg='#0B1416', lift='#101C1F', cream='#101C1F', card='#132124', ink='#EAF0EE', muted='#A2B0AD',
            line='#22343A', amber_text='#FFC870', teal_text='#5CD6C9', focus='#FFC870')
# the same in both site themes: the app's own dark world
ART = dict(art_ink='#F4F1EA', art_lead='#D3DDDA', art_soft='#C5D2CF', art_eyebrow='#FFC870', art_teal='#5CD6C9',
           canvas='#0B1416', chip='#1B2D31', chip_text='#A9B8B6', amber='#FFB547', on_amber='#1F1404',
           coral='#FF7A59', sun_a='#FF8F6B', sun_b='#FFC070', peak='#FFD562')
SC, PC = '.84', '.72'   # scrim alpha under copy on a plate / under glass cards and pills

# text pairs measured by audit(): (label, foreground var, background var), plain colours
PAIRS_PLAIN = [
    ('body text on page', 'ink', 'bg'), ('body text on lifted band', 'ink', 'lift'), ('body text on cream band', 'ink', 'cream'),
    ('body text on card', 'ink', 'card'),
    ('muted text on page', 'muted', 'bg'), ('muted text on lifted band', 'muted', 'lift'),
    ('muted text on cream band', 'muted', 'cream'), ('muted text on card', 'muted', 'card'),
    ('amber text / links on page', 'amber_text', 'bg'), ('amber text / links on lifted band', 'amber_text', 'lift'),
    ('amber text / links on cream band', 'amber_text', 'cream'), ('amber text / links on card', 'amber_text', 'card'),
    ('teal icons on page', 'teal_text', 'bg'), ('teal icons on lifted band', 'teal_text', 'lift'),
    ('teal icons on cream band', 'teal_text', 'cream'),
    ('focus ring on page', 'focus', 'bg'), ('focus ring on lifted band', 'focus', 'lift'),
    ('focus ring on cream band', 'focus', 'cream'), ('focus ring on card', 'focus', 'card'),
    ('focus ring on plates', 'art_eyebrow', 'canvas'),
    ('button label on amber', 'on_amber', 'amber'),
    ('plate text on canvas', 'art_ink', 'canvas'), ('plate muted text on canvas', 'art_soft', 'canvas'),
    ('plate eyebrow on canvas', 'art_eyebrow', 'canvas'), ('plate teal on canvas', 'art_teal', 'canvas'),
    ('removed-data chip text on chip', 'chip_text', 'chip'),
    ('gradient word, start, on canvas', 'sun_a', 'canvas'), ('gradient word, end, on canvas', 'sun_b', 'canvas'),
]
# over a plate: (label, foreground var, alpha var); background = brightest plate pixel under that scrim
PAIRS_PLATE = [
    ('headline over plate', 'art_ink', 'sc'), ('lead over plate', 'art_lead', 'sc'), ('muted text over plate', 'art_soft', 'sc'),
    ('eyebrow over plate', 'art_eyebrow', 'sc'), ('gradient word, start, over plate', 'sun_a', 'sc'),
    ('gradient word, end, over plate', 'sun_b', 'sc'), ('teal icon over plate', 'art_teal', 'sc'),
    ('text in a glass card or pill', 'art_ink', 'pc'), ('muted text in a glass card', 'art_soft', 'pc'),
    ('eyebrow in a glass card', 'art_eyebrow', 'pc'), ('teal in a glass card', 'art_teal', 'pc'),
]


def _rgb(h):
    h = h.lstrip('#'); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _lum(h):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = _rgb(h); return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def _ratio(a, b):
    la, lb = _lum(a), _lum(b)
    if la < lb: la, lb = lb, la
    return (la + 0.05) / (lb + 0.05)


def _blend(under, over, alpha):
    u, o = _rgb(under), _rgb(over)
    return '#%02X%02X%02X' % tuple(round(o[i] * alpha + u[i] * (1 - alpha)) for i in range(3))


def _decl(d):
    return ';'.join('--%s:%s' % (k.replace('_', '-'), v) for k, v in d.items())


def root_css():
    return (':root{' + _decl(LIGHT) + ';' + _decl(ART) + ';--sc:%s;--pc:%s;color-scheme:light dark}\n' % (SC, PC) +
            '@media (prefers-color-scheme:dark){:root{' + _decl(DARK) + '}}\n')


def _vars(block):
    return {k.replace('-', '_'): v.strip() for k, v in re.findall(r'--([a-z-]+):([^;}]+)', block)}


def audit(html):
    """Every pair of PAIRS_PLAIN and PAIRS_PLATE, read from the <style> of a generated page, in light and dark,
    plus the isolation check. -> (rows, ok); a row is (mode, label, fg, bg, ratio)."""
    style = re.search(r'<style>(.*?)</style>', html, re.S).group(1)
    light = _vars(re.search(r':root\{([^}]*)\}', style).group(1))
    dark = dict(light, **_vars(re.search(r'prefers-color-scheme:dark\)\{:root\{([^}]*)\}', style).group(1)))
    rows = []
    for mode, v in (('light', light), ('dark', dark)):
        for label, fg, bg in PAIRS_PLAIN:
            rows.append((mode, label, v[fg], v[bg], _ratio(v[fg], v[bg])))
        for label, fg, a in PAIRS_PLATE:
            bg = _blend(v['peak'], v['canvas'], float(v[a]))
            rows.append((mode, label, v[fg], bg, _ratio(v[fg], bg)))
    bad = check_isolation(html)
    if bad: print('atino isolation:', bad)
    return rows, all(r[4] >= MIN for r in rows) and not bad


ALLOWED_EXTERNAL = ('mailto:hello@seizeapps.com', 'https://www.revenuecat.com/privacy', 'https://www.aepd.es',
                    'https://reportaproblem.apple.com', 'https://www.apple.com/legal/')


def check_isolation(html):
    """Links and sources a page may not carry; -> list of offenders."""
    bad = []
    for attr, v in re.findall(r'(href|src)="([^"]+)"', html):
        if v.startswith(('#', './', '../', 'https://seizeapps.com/atino/')): continue
        if v.startswith(ALLOWED_EXTERNAL): continue
        bad.append(v)
    if re.search(r'<script|stylesheet|@import|url\((?!#)|apps\.apple\.com', html): bad.append('script/stylesheet/import/url()/apps.apple.com')
    return bad


# ------------------------------------------------------------------------------------------------ stylesheet
CSS_BASE = r'''
:root{--display:ui-rounded,"SF Pro Rounded","Avenir Next Rounded","Avenir Next",system-ui,sans-serif;
--body:"Avenir Next",ui-sans-serif,system-ui,"Segoe UI",sans-serif;
--read:"Iowan Old Style","Charter","Palatino Linotype",Georgia,serif;
--spring:cubic-bezier(.34,1.4,.5,1)}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{animation:none!important;transition:none!important}}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--body);font-size:17px;line-height:1.55;-webkit-font-smoothing:antialiased;overflow-x:hidden}
img{display:block;max-width:100%;height:auto}
a{color:inherit}
:focus-visible{outline:3px solid var(--focus);outline-offset:3px;border-radius:6px}
.at-art :focus-visible{outline-color:var(--art-eyebrow)}
.at-skip{position:absolute;left:12px;top:-80px;z-index:60;background:var(--amber);color:var(--on-amber);padding:11px 18px;border-radius:12px;font-weight:700;text-decoration:none}
.at-skip:focus{top:12px}
.at-wrap{width:min(1200px,100% - 48px);margin-inline:auto}
@media (max-width:560px){.at-wrap{width:calc(100% - 40px)}}

/* the app's dark world: every block that carries a plate, in both site themes */
.at-art{--ink:var(--art-ink);--muted:var(--art-soft);--eyebrow:var(--art-eyebrow);--card:rgba(11,20,22,.82);--line:rgba(255,255,255,.16);
  color:var(--art-ink);background:var(--canvas);color-scheme:dark;position:relative;isolation:isolate}
.at-eyebrow{font-family:var(--display);font-size:13px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--eyebrow,var(--amber-text));margin:0 0 14px}
.at-h2{font-family:var(--display);font-weight:700;font-size:clamp(32px,4.4vw,56px);line-height:1.04;letter-spacing:-.025em;margin:0 0 20px;text-wrap:balance}
.at-lead{font-size:clamp(17px,1.5vw,20px);line-height:1.55;color:var(--muted);margin:0 0 16px;max-width:34em}
.at-sun{background:linear-gradient(92deg,var(--sun-a) 0%,var(--sun-b) 100%);-webkit-background-clip:text;background-clip:text;color:transparent;-webkit-text-fill-color:transparent}
@media (forced-colors:active){.at-sun{background:none;-webkit-text-fill-color:currentColor;color:currentColor}}

/* header */
.at-head{padding:22px 0;position:relative;z-index:10}
.at-head--abs{position:absolute;inset:0 0 auto 0}
.at-head__in{display:flex;align-items:center;justify-content:space-between;gap:14px}
.at-brand{display:inline-flex;align-items:center;gap:12px;text-decoration:none;font-family:var(--display);font-weight:700;font-size:21px;letter-spacing:-.01em;color:var(--art-ink)}
.at-brand img{width:38px;height:38px;border-radius:10px;box-shadow:0 6px 18px rgba(0,119,255,.28),0 0 0 1px rgba(255,255,255,.14)}
.at-nav{display:flex;align-items:center;gap:4px;font-family:var(--display);font-weight:600;font-size:15px}
.at-nav a{padding:9px 13px;border-radius:99px;text-decoration:none;color:var(--art-soft);transition:background .25s,color .25s}
.at-nav a:hover{background:rgba(255,255,255,.1);color:var(--art-ink)}
.at-nav a[aria-current="page"]{color:var(--art-ink);background:rgba(255,255,255,.12)}
.at-soon{display:inline-flex;align-items:center;gap:8px;margin-left:8px;padding:9px 14px;border-radius:99px;border:1px solid rgba(255,255,255,.28);background:rgba(11,20,22,var(--pc));color:var(--art-ink);font-size:13.5px;font-weight:700;white-space:nowrap}
.at-soon i{width:8px;height:8px;border-radius:50%;background:radial-gradient(circle,#FFE2A8,#FFB547 60%,#FF7A59);box-shadow:0 0 0 3px rgba(255,181,71,.22)}
@media (max-width:640px){.at-nav a.at-hide{display:none}.at-brand{font-size:19px}.at-brand img{width:34px;height:34px}.at-nav a{padding:8px 9px;font-size:14px}.at-soon{margin-left:2px;padding:8px 11px;font-size:13px}}
@media (max-width:560px){.at-nav a.at-hide{display:inline-block}.at-soon{display:none}.at-nav{gap:0}.at-nav a{padding:8px 8px;font-size:13.5px}.at-head__in{gap:8px}.at-brand{font-size:18px;gap:8px}}
@media (max-width:340px){.at-brand{font-size:0;gap:0}.at-nav a{padding:8px 6px;font-size:13px}}

/* page art: a plate inside a max-width window that fades into the canvas, so it is never stretched past its 1024 px source */
.at-stage{position:absolute;inset:0;z-index:-2;margin-inline:auto;max-width:1280px;overflow:hidden;
  -webkit-mask-image:linear-gradient(90deg,transparent 0,#000 11%,#000 89%,transparent 100%);mask-image:linear-gradient(90deg,transparent 0,#000 11%,#000 89%,transparent 100%)}
.at-stage img{width:100%;height:100%;object-fit:cover}
.at-scrim{position:absolute;inset:0;z-index:-1}

/* device frame; everything scales from --w */
.at-dev{--w:290px;width:var(--w);padding:calc(var(--w)*.03);border-radius:calc(var(--w)*.17);position:relative;margin:0;
  background:linear-gradient(145deg,#4a5557 0%,#1d2628 38%,#0c1213 70%,#364143 100%);
  box-shadow:0 0 0 calc(var(--w)*.004) rgba(255,255,255,.1) inset,0 calc(var(--w)*.1) calc(var(--w)*.2) rgba(0,0,0,.5),0 calc(var(--w)*.02) calc(var(--w)*.05) rgba(0,0,0,.4)}
.at-dev::before{content:"";position:absolute;inset:calc(var(--w)*.012);border-radius:calc(var(--w)*.158);background:#04080a;z-index:0}
.at-dev img{position:relative;z-index:1;width:100%;height:auto;border-radius:calc(var(--w)*.14);background:#0B1416}
.at-dev::after{content:"";position:absolute;z-index:2;top:calc(var(--w)*.058);left:50%;width:calc(var(--w)*.255);height:calc(var(--w)*.074);transform:translateX(-50%);border-radius:99px;background:#020405}
.at-stack{container-type:inline-size;position:relative;width:100%}
.at-stack .at-dev{position:absolute}
.at-cap{display:block;margin:14px auto 0;width:max-content;max-width:100%;padding:8px 16px;border-radius:99px;background:rgba(11,20,22,var(--pc));color:var(--art-soft);font-family:var(--display);font-size:14px;font-weight:600;text-align:center}

/* buttons */
.at-btn{display:inline-flex;align-items:center;gap:10px;padding:14px 24px;border-radius:99px;font-family:var(--display);font-weight:700;font-size:16px;text-decoration:none;
  background:var(--amber);color:var(--on-amber);box-shadow:0 10px 26px -8px rgba(255,150,40,.6);transition:transform .35s var(--spring),box-shadow .3s}
.at-btn:hover{transform:translateY(-2px) scale(1.02)}
.at-btn--ghost{background:transparent;color:var(--ink);box-shadow:none;border:1.5px solid var(--ink)}

/* footer */
.at-foot{border-top:1px solid var(--line);padding:56px 0 48px;color:var(--muted);font-size:15px;background:var(--bg)}
.at-foot__top{display:flex;flex-wrap:wrap;gap:28px 48px;justify-content:space-between;align-items:flex-start}
.at-foot__id{display:flex;gap:14px;align-items:center;color:var(--ink);font-family:var(--display)}
.at-foot__id img{width:48px;height:48px;border-radius:12px;box-shadow:0 8px 22px rgba(0,119,255,.25)}
.at-foot__id strong{display:block;font-size:19px;letter-spacing:-.01em}
.at-foot__id span{font-size:14.5px;color:var(--muted);font-family:var(--body)}
.at-foot ul{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:4px 26px;font-family:var(--display);font-weight:600}
.at-foot ul a{color:var(--ink);text-decoration:none;padding:8px 0;display:inline-block;border-bottom:1px solid transparent}
.at-foot ul a:hover{border-bottom-color:var(--amber-text)}
.at-foot small{display:block;margin-top:36px;padding-top:24px;border-top:1px solid var(--line);font-size:14px;line-height:1.6}
.at-foot a.mail{color:var(--amber-text);font-weight:700}
'''

CSS_HOME = r'''
@media (prefers-reduced-motion:no-preference){
  @keyframes at-rise{from{opacity:0;translate:0 26px;scale:.98}to{opacity:1;translate:0 0;scale:1}}
  @keyframes at-drift{from{transform:scale(1.02) translate3d(0,0,0)}to{transform:scale(1.07) translate3d(-1%,1.2%,0)}}
  @keyframes at-glow{0%,100%{opacity:.6}50%{opacity:1}}
}
/* hero */
.at-hero{padding:150px 0 100px;min-height:min(900px,100svh);display:flex;align-items:center;overflow:hidden}
.at-hero .at-stage img{object-position:center 31%}
@media (prefers-reduced-motion:no-preference){.at-hero .at-stage img{animation:at-drift 40s ease-in-out infinite alternate}}
.at-hero .at-scrim{background:
  linear-gradient(90deg,rgba(11,20,22,var(--sc)) 0%,rgba(11,20,22,var(--sc)) 46%,rgba(11,20,22,.25) 66%,rgba(11,20,22,0) 100%),
  linear-gradient(0deg,rgba(11,20,22,.9) 0%,rgba(11,20,22,0) 24%)}
.at-hero::after{content:"";position:absolute;left:0;right:0;bottom:0;height:3px;background:linear-gradient(90deg,transparent,#FF7A59 25%,#FFB547 60%,transparent)}
.at-hero__grid{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.2fr);gap:24px;align-items:center}
.at-hero h1{font-family:var(--display);font-weight:750;font-size:clamp(44px,5.6vw,84px);line-height:1;letter-spacing:-.035em;margin:0 0 24px;text-wrap:balance}
.at-hero .at-lead{font-size:clamp(18px,1.6vw,21px);color:var(--art-lead)}
.at-badge{display:inline-flex;align-items:center;gap:12px;margin:12px 0 0;padding:13px 22px 13px 18px;border-radius:99px;
  background:rgba(11,20,22,var(--pc));border:1px solid rgba(255,255,255,.26);font-family:var(--display);font-weight:700;font-size:16px;
  -webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);box-shadow:0 10px 30px rgba(0,0,0,.35)}
.at-badge::before{content:"";width:11px;height:11px;border-radius:50%;background:radial-gradient(circle,#FFE2A8,#FFB547 60%,#FF7A59);box-shadow:0 0 0 4px rgba(255,181,71,.2),0 0 18px rgba(255,181,71,.7)}
@media (prefers-reduced-motion:no-preference){.at-badge::before{animation:at-glow 3.2s ease-in-out infinite}}
.at-meta{display:flex;flex-wrap:wrap;gap:6px 22px;margin:22px 0 0;padding:0;list-style:none;font-family:var(--display);font-size:15px;font-weight:600;color:var(--art-soft)}
.at-meta li{display:flex;align-items:center;gap:8px}
.at-meta li+li::before{content:"";width:4px;height:4px;border-radius:50%;background:#FFB547;margin-right:6px;margin-left:-14px}
.at-hero__stack{aspect-ratio:1/1.06;margin-right:-40px;width:calc(100% + 40px)}
@media (prefers-reduced-motion:no-preference){.at-hero__stack .at-dev{animation:at-rise 1s var(--spring) both}}
.at-hero__stack .d1{--w:37cqw;left:-1cqw;top:20cqw;transform:rotate(-8deg);animation-delay:.25s;filter:brightness(.9)}
.at-hero__stack .d2{--w:37cqw;right:-1cqw;top:11cqw;transform:rotate(7deg);animation-delay:.4s;filter:brightness(.92)}
.at-hero__stack .d3{--w:47cqw;left:26.5cqw;top:2cqw;z-index:3;animation-delay:.1s}
.at-hero__stack::before{content:"";position:absolute;left:12%;right:12%;bottom:6%;height:20%;background:radial-gradient(closest-side,rgba(255,181,71,.38),transparent);filter:blur(10px)}
.at-hero__fig{margin:0;min-width:0}

/* stat strip */
.at-stats{background:var(--bg);padding:0}
.at-stats ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,1fr)}
.at-stats li{padding:34px 28px 32px;border-left:1px solid var(--line)}
.at-stats li:first-child{border-left:0;padding-left:0}
.at-stats b{display:block;font:700 clamp(26px,3vw,38px)/1.05 var(--display);letter-spacing:-.03em;font-variant-numeric:tabular-nums}
.at-stats span{display:block;margin-top:9px;font-size:15.5px;line-height:1.4;color:var(--muted)}
@media (max-width:760px){.at-stats ul{grid-template-columns:1fr 1fr}.at-stats li{padding:22px 16px 20px}.at-stats li:nth-child(odd){border-left:0;padding-left:0}.at-stats li:nth-child(n+3){border-top:1px solid var(--line)}}

/* bands */
.at-s{padding:clamp(72px,9vw,128px) 0;background:var(--bg)}
.at-s--lift{background:var(--lift)}
.at-s--cream{background:var(--cream)}
.at-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(40px,7vw,104px);align-items:center}
.at-ticks{list-style:none;margin:26px 0 0;padding:0;display:grid;gap:14px}
.at-ticks li{display:flex;gap:14px;align-items:flex-start;color:var(--ink);font-size:17px;line-height:1.5}
.at-ticks svg{flex:none;width:22px;height:22px;margin-top:2px}
.at-c{stroke:var(--teal-text)}
.at-art .at-c{stroke:var(--art-teal)}

/* how it works */
.at-how__head{max-width:40em;margin-bottom:56px}
.at-rail{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,1fr);gap:0;counter-reset:r;position:relative}
.at-rail li{position:relative;padding:0 28px 0 0;counter-increment:r}
.at-rail li::before{content:"0" counter(r);display:grid;place-items:center;width:52px;height:52px;border-radius:50%;background:var(--canvas);color:var(--art-teal);
  font:800 17px/1 var(--display);letter-spacing:.02em;box-shadow:0 0 0 1px rgba(92,214,201,.55);position:relative;z-index:1}
.at-rail li::after{content:"";position:absolute;left:52px;right:0;top:25.5px;height:1.5px;background:linear-gradient(90deg,var(--teal-text),transparent)}
.at-rail li:last-child::after{display:none}
.at-rail h3{font-family:var(--display);font-weight:700;font-size:20px;letter-spacing:-.01em;margin:22px 0 8px}
.at-rail p{margin:0;color:var(--muted);font-size:16px;line-height:1.5}
@media (max-width:900px){.at-rail{grid-template-columns:1fr;gap:6px}.at-rail li{padding:0 0 30px 74px}.at-rail li:last-child{padding-bottom:0}
  .at-rail li::before{position:absolute;left:0;top:0}.at-rail li::after{left:25.5px;right:auto;top:56px;bottom:4px;width:1.5px;height:auto;background:linear-gradient(var(--teal-text),transparent)}
  .at-rail h3{margin:10px 0 6px}}

/* art panel: a plate in a rounded window */
.at-panel{position:relative;isolation:isolate;overflow:hidden;border-radius:32px;aspect-ratio:5/6;background:var(--canvas);color:var(--art-ink);margin:0;
  box-shadow:0 40px 90px -30px rgba(7,28,30,.55),0 0 0 1px rgba(255,255,255,.08) inset}
.at-panel>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 22%;z-index:-1}
.at-panel::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(0deg,rgba(11,20,22,.75),rgba(11,20,22,0) 55%)}
.at-redact{position:absolute;left:20px;right:20px;bottom:20px;padding:22px 22px 20px;border-radius:24px;background:rgba(11,20,22,var(--pc));border:1px solid rgba(255,255,255,.14);
  -webkit-backdrop-filter:blur(16px);backdrop-filter:blur(16px)}
.at-redact .at-eyebrow{margin-bottom:12px}
.at-chips{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 16px;padding:0;list-style:none}
.at-chips li{font-family:var(--display);font-weight:600;font-size:14.5px;padding:7px 14px;border-radius:99px;background:var(--chip);color:var(--chip-text);
  text-decoration:line-through;text-decoration-color:var(--coral);text-decoration-thickness:2px}
.at-redact p.at-then{margin:0;display:flex;gap:10px;align-items:flex-start;font-size:15px;line-height:1.45;color:var(--art-ink);border-top:1px solid rgba(255,255,255,.12);padding-top:14px}
.at-redact svg{flex:none;width:20px;height:20px;margin-top:1px}
.at-fignote{margin:12px 0 0;font-size:14px;color:var(--muted);text-align:center}

/* plate windows: inset, hairline edge, rounded */
.at-pw{padding:clamp(14px,2vw,26px) clamp(12px,2vw,24px);background:var(--bg)}
.at-plate{max-width:1280px;margin-inline:auto;border-radius:22px;border:1px solid rgba(255,255,255,.08);overflow:hidden;box-shadow:0 40px 90px -50px rgba(7,28,30,.7)}
@supports (corner-shape:squircle){.at-plate,.at-panel,.at-sheet{corner-shape:squircle;border-radius:34px}.at-plate{border-radius:30px}}
.at-plate>.at-bg{position:absolute;inset:0;z-index:-2;width:100%;height:100%;object-fit:cover}

/* best fit first */
.at-glow{padding:clamp(72px,9vw,120px) 0 0}
.at-glow .at-scrim{background:
  radial-gradient(70% 55% at 30% 105%,rgba(255,122,89,.5),transparent 70%),
  radial-gradient(55% 50% at 55% 108%,rgba(255,181,71,.42),transparent 70%),
  radial-gradient(60% 50% at 20% 20%,rgba(92,214,201,.09),transparent 70%)}
.at-glow__stack{aspect-ratio:1/1.2;max-width:620px;margin-inline:auto}
.at-glow__stack .d1{--w:50cqw;left:0;top:4cqw;z-index:2}
.at-glow__stack .d2{--w:44cqw;right:0;top:20cqw;transform:rotate(5deg);filter:brightness(.88)}
.at-glow__hills{position:absolute;left:0;right:0;bottom:-1px;width:100%;height:150px;z-index:-1}
.at-glow .at-grid{padding-bottom:84px}
.at-glow .at-cap{margin-top:0}

/* estimate */
.at-panel--why{aspect-ratio:1/1.08}
.at-panel--why>img{object-position:center 40%}
.at-panel--why::after{background:linear-gradient(0deg,rgba(11,20,22,.5),rgba(11,20,22,.05) 60%)}
.at-sheet{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:min(76%,400px);border-radius:24px;overflow:hidden;
  box-shadow:0 30px 70px rgba(0,0,0,.6),0 0 0 1px rgba(255,255,255,.16);background:var(--canvas)}
.at-sheet>div{aspect-ratio:600/660;overflow:hidden}
.at-sheet img{width:100%;height:auto;margin-top:-107%}
.at-fit{display:flex;gap:26px;align-items:center;margin:30px 0 0;flex-wrap:wrap}
.at-arc{flex:none;position:relative;width:196px;height:176px;border-radius:26px;text-align:center;padding-top:16px;
  box-shadow:0 18px 40px -22px rgba(7,28,30,.6),0 0 0 1px rgba(255,255,255,.08) inset}
.at-arc svg{display:block;width:150px;height:150px;margin:0 auto;overflow:visible;filter:drop-shadow(0 0 12px rgba(255,181,71,.32))}
.at-arc__t{fill:none;stroke:#26393E;stroke-width:9;stroke-linecap:round;stroke-dasharray:66.67 100}
.at-arc__v{fill:none;stroke:url(#at-sunrise);stroke-width:9;stroke-linecap:round;stroke-dasharray:63.33 100}
@supports (animation-timeline:view()){@media (prefers-reduced-motion:no-preference){
  @keyframes at-sweep{from{stroke-dasharray:0 100}to{stroke-dasharray:63.33 100}}
  .at-arc__v{animation:at-sweep linear both;animation-timeline:view();animation-range:entry 20% cover 45%}}}
.at-arc b{position:absolute;left:0;right:0;top:66px;font:700 40px/1 var(--display);letter-spacing:-.02em}
.at-arc b small{font-size:17px;font-weight:700;margin-left:2px;vertical-align:top;position:relative;top:4px}
.at-arc em{position:absolute;left:0;right:0;top:128px;font:700 11.5px/1 var(--display);font-style:normal;letter-spacing:.14em;color:var(--art-soft)}
.at-quote{flex:1 1 260px;margin:0;padding:4px 0 4px 22px;border-left:3px solid #FFB547;font-family:var(--display);font-weight:600;font-size:clamp(19px,1.7vw,22px);line-height:1.4;letter-spacing:-.005em}
.at-quote cite{display:block;margin-top:8px;font-style:normal;font-size:14.5px;font-weight:500;color:var(--muted);font-family:var(--body)}

/* filters */
.at-filters{padding:clamp(72px,9vw,120px) 0 0}
.at-filters .at-scrim{background:linear-gradient(90deg,rgba(11,20,22,var(--sc)) 0%,rgba(11,20,22,var(--sc)) 46%,rgba(11,20,22,.1) 80%),linear-gradient(0deg,rgba(11,20,22,.7),rgba(11,20,22,0) 20%)}
.at-filters .at-bg{object-position:center 40%}
.at-filters .at-grid{align-items:end}
.at-filters .at-copy{padding-bottom:120px;align-self:center}
.at-filters .at-dev{--w:min(320px,70vw);margin-inline:auto;margin-bottom:-110px}

/* jobs */
.at-jobs__grid{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);gap:clamp(32px,6vw,88px);align-items:center}
.at-big{font:800 clamp(56px,8vw,112px)/.9 var(--display);letter-spacing:-.055em;font-variant-numeric:tabular-nums;margin:0 0 6px;color:var(--ink);white-space:nowrap}
.at-big em{font-style:normal;color:var(--amber-text)}
.at-jobs .at-h2{font-size:clamp(26px,3vw,38px);margin:14px 0 14px}
.at-src h3{font-family:var(--display);font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--amber-text);margin:0 0 12px;font-weight:700}
.at-src+.at-src{margin-top:26px}
.at-tags{display:flex;flex-wrap:wrap;gap:8px;list-style:none;margin:0;padding:0}
.at-tags li{padding:8px 15px;border-radius:99px;font-family:var(--display);font-weight:600;font-size:15px;background:var(--card);border:1px solid var(--muted);color:var(--ink)}
.at-fine{margin:28px 0 0;color:var(--muted);font-size:15.5px;max-width:38em}
@media (max-width:980px){.at-big{font-size:clamp(44px,15vw,120px)}}

/* pro */
.at-pro{padding:clamp(72px,9vw,120px) 0}
.at-pro .at-bg{object-position:center 28%}
.at-pro .at-scrim{background:linear-gradient(180deg,rgba(11,20,22,var(--sc)) 0%,rgba(11,20,22,var(--sc)) 30%,rgba(11,20,22,.3) 100%)}
.at-pro__head{max-width:40em;margin-bottom:44px}
.at-plans{display:grid;grid-template-columns:1fr 1fr;border-radius:26px;background:rgba(11,20,22,var(--pc));border:1px solid rgba(255,255,255,.16);
  -webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px);overflow:hidden}
.at-plan{padding:clamp(26px,3.4vw,44px)}
.at-plan--pro{border:2px solid #FFB547;border-radius:24px;margin:-1px;background:rgba(255,181,71,.06)}
.at-plan h3{font-family:var(--display);font-weight:700;font-size:24px;letter-spacing:-.015em;margin:0 0 4px;display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.at-plan h3 span{font-size:12.5px;letter-spacing:.12em;text-transform:uppercase;padding:4px 10px;border-radius:99px;background:var(--amber);color:var(--on-amber)}
.at-plan>p{margin:0 0 20px;color:var(--art-soft);font-size:15.5px}
.at-plan ul{list-style:none;margin:0;padding:0;display:grid;gap:14px}
.at-plan li{display:flex;gap:12px;align-items:flex-start;font-size:16.5px;line-height:1.45}
.at-plan li svg{flex:none;width:20px;height:20px;margin-top:2px}
.at-pro__fine{margin:22px 0 0;max-width:46em;font-size:15.5px;color:var(--art-lead)}
@media (max-width:760px){.at-plans{grid-template-columns:1fr}.at-plan--pro{margin:0 -1px -1px}}

/* privacy band */
.at-links{display:flex;flex-wrap:wrap;gap:12px;margin:30px 0 0}
.at-steps{list-style:none;margin:0;padding:0;counter-reset:s;position:relative}
.at-steps li{position:relative;padding:0 0 30px 64px;counter-increment:s}
.at-steps li:last-child{padding-bottom:0}
.at-steps li::before{content:counter(s);position:absolute;left:0;top:0;width:42px;height:42px;border-radius:50%;display:grid;place-items:center;
  font-family:var(--display);font-weight:800;font-size:17px;background:var(--canvas);color:var(--art-teal);box-shadow:0 0 0 1px rgba(92,214,201,.5)}
.at-steps li::after{content:"";position:absolute;left:20.5px;top:48px;bottom:6px;width:1.5px;background:linear-gradient(var(--teal-text),transparent)}
.at-steps li:last-child::after{display:none}
.at-steps h3{font-family:var(--display);font-weight:700;font-size:20px;margin:6px 0 6px;letter-spacing:-.01em}
.at-steps p{margin:0;color:var(--muted);font-size:16.5px}

@media (max-width:980px){
  .at-hero{padding:116px 0 64px;min-height:0;align-items:flex-start}
  .at-hero__grid,.at-grid,.at-jobs__grid{grid-template-columns:1fr}
  .at-hero .at-scrim{background:linear-gradient(180deg,rgba(11,20,22,var(--sc)) 0%,rgba(11,20,22,var(--sc)) 55%,rgba(11,20,22,.5) 100%)}
  .at-hero__stack{max-width:520px;margin:20px auto 0;width:100%}
  .at-panel{aspect-ratio:1/1.05;border-radius:28px}
  .at-glow .at-grid>figure{order:2}
  .at-filters .at-copy{padding-bottom:20px}
  .at-filters .at-dev{margin-bottom:-90px}
  .at-filters .at-scrim{background:linear-gradient(180deg,rgba(11,20,22,var(--sc)) 0%,rgba(11,20,22,var(--sc)) 34%,rgba(11,20,22,.3) 62%,rgba(11,20,22,.2) 100%)}
}
@media (max-width:560px){
  .at-panel{aspect-ratio:1/1.3}
  .at-panel>img{object-position:center 20%}
  .at-panel--why{aspect-ratio:1/1.2}
  .at-meta{flex-direction:column;gap:6px}.at-meta li+li::before{display:none}
  .at-hero h1{font-size:clamp(42px,12.5vw,56px)}
  .at-redact{left:12px;right:12px;bottom:12px;padding:18px 16px 16px}
  .at-chips li{font-size:13.5px;padding:6px 11px}
  .at-badge{font-size:15px}
  .at-arc{width:100%}
}
'''

CSS_LEGAL = r'''
.at-lhero{overflow:hidden;padding-bottom:clamp(40px,6vw,72px)}
.at-lhero .at-scrim{background:linear-gradient(90deg,rgba(11,20,22,var(--sc)) 0%,rgba(11,20,22,var(--sc)) 60%,rgba(11,20,22,.4) 100%)}
.at-lhero__in{padding-top:clamp(40px,7vw,88px)}
.at-lhero h1{font-family:var(--display);font-weight:800;font-size:clamp(38px,5.4vw,72px);line-height:1;letter-spacing:-.03em;margin:0 0 16px;text-wrap:balance}
.at-upd{margin:0;color:var(--art-lead);font-size:17px;max-width:40em}
.at-lang{margin:14px 0 0;font-family:var(--display);font-weight:700;font-size:15px}
.at-lang a{color:var(--art-eyebrow);text-underline-offset:4px}
.at-tabs{display:inline-flex;flex-wrap:wrap;gap:3px;padding:4px;border-radius:16px;background:rgba(11,20,22,var(--pc));border:1px solid rgba(255,255,255,.16);margin:28px 0 0;
  font-family:var(--display);font-weight:600;font-size:14.5px}
.at-tabs a{padding:10px 16px;border-radius:12px;color:var(--art-soft);text-decoration:none}
.at-tabs a:hover{color:var(--art-ink);background:rgba(255,255,255,.1)}
.at-tabs a[aria-current="page"]{background:var(--art-ink);color:var(--canvas)}
.at-lay{display:grid;grid-template-columns:240px minmax(0,1fr);gap:clamp(32px,6vw,96px);padding:72px 0 96px;align-items:start}
.at-lay--solo{grid-template-columns:minmax(0,1fr)}
.at-toc{position:sticky;top:28px;font-family:var(--display);font-size:15px}
.at-toc ol{list-style:none;margin:0;padding:0;border-left:1.5px solid var(--line)}
.at-toc li a{display:block;padding:8px 0 8px 18px;margin-left:-1.5px;border-left:1.5px solid transparent;color:var(--muted);text-decoration:none;font-weight:600;line-height:1.3}
.at-toc li a:hover{color:var(--ink);border-left-color:var(--amber-text)}
.at-tocm{display:none;border:1.5px solid var(--muted);border-radius:16px;background:var(--card);margin:0 0 30px;font-family:var(--display)}
.at-tocm summary{padding:14px 18px;font-weight:700;cursor:pointer;font-size:16px;color:var(--ink)}
.at-tocm ol{margin:0;padding:0 18px 12px;list-style:none}
.at-tocm a{display:block;padding:10px 0;color:var(--muted);text-decoration:none;border-top:1px solid var(--line);font-weight:600;font-size:15.5px}
.at-doc{font-family:var(--read);font-size:18px;line-height:1.65;max-width:68ch;min-width:0}
.at-doc h2{font-family:var(--display);font-weight:700;font-size:clamp(25px,2.5vw,31px);letter-spacing:-.02em;line-height:1.15;margin:2.4em 0 .6em;display:flex;gap:16px;align-items:baseline;scroll-margin-top:24px}
.at-doc>h2:first-child,.at-doc>.at-tocm+h2{margin-top:0}
.at-doc h2 span{font-size:.55em;letter-spacing:.06em;font-weight:800;color:var(--amber-text);min-width:1.6em}
.at-doc h3{font-family:var(--display);font-weight:700;font-size:20px;letter-spacing:-.01em;line-height:1.3;margin:2em 0 .5em}
.at-doc p{margin:0 0 1.1em}
.at-doc a{color:var(--amber-text);text-underline-offset:3px;text-decoration-thickness:1.5px}
.at-doc ul{margin:0 0 1.2em;padding:0 0 0 1.2em}
.at-doc li{margin:0 0 .7em;padding-left:.2em}
.at-doc li::marker{color:var(--amber-text)}
.at-doc h2.at-sum+ul{list-style:none;padding:30px 28px 26px;border-radius:24px;background:linear-gradient(var(--amber),var(--amber)) top/100% 4px no-repeat,var(--card);color:var(--ink);border:1px solid var(--line);
  box-shadow:0 18px 40px -26px rgba(7,28,30,.35)}
.at-doc h2.at-sum+ul li{padding-left:0;font-size:17.5px}
.at-doc h2.at-sum+ul li:last-child{margin-bottom:0}
.at-doc .contact{font-family:var(--display);font-size:clamp(22px,2.4vw,28px);font-weight:700;letter-spacing:-.01em}
.at-more{margin-top:2em;padding-top:1.6em;border-top:1px solid var(--line);font-family:var(--display);font-weight:700}
.at-sibs{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:2.8em 0 0;font-family:var(--display)}
.at-doc a.at-sib{text-decoration:none;color:var(--ink)}
.at-sib{display:block;padding:20px 22px;border-radius:20px;background:var(--card);border:1px solid var(--line);color:var(--ink);text-decoration:none;transition:transform .35s var(--spring),border-color .25s}
.at-sib:hover{transform:translateY(-3px);border-color:var(--amber-text)}
.at-sib strong{display:block;font-size:18px;letter-spacing:-.01em;margin-bottom:4px}
.at-sib span{font-family:var(--body);font-size:15px;line-height:1.4;color:var(--muted)}
@media (max-width:860px){.at-lay{grid-template-columns:1fr;padding-top:36px}.at-toc{display:none}.at-tocm{display:block}
  .at-doc h2{display:block}.at-doc h2 span{display:block;margin-bottom:4px}.at-doc h2.at-sum+ul{padding:20px 20px 20px 22px}.at-sibs{grid-template-columns:1fr}}
@media (max-width:560px){.at-doc{font-size:17.5px}.at-tabs{width:100%}.at-tabs a{flex:1 1 auto;text-align:center;padding:10px 10px}}
'''

# ------------------------------------------------------------------------------------------------ copy
UI = {
    'en': dict(lang='en', home='Atino, home', nav=[('privacy', 'Privacy'), ('terms', 'Terms'), ('support', 'Support')],
               soon='Coming soon', skip='Skip to content', contents='Contents', on_page='On this page', back='Back to Atino',
               tabs=[('privacy', 'Privacy'), ('terms', 'Terms'), ('support', 'Support')], other=('privacidad', 'Español', 'es'),
               tagline='Your CV against Europe&rsquo;s jobs.',
               foot='&copy; 2026 Izotz Cristobal Mota. Atino is coming soon to the App Store for iPhone. It is independent and not affiliated with the employers it lists. The jobs and names shown in the screenshots are sample data.',
               more='More in these pages', read_other='Leer en español', pagelabel='Atino pages'),
    'es': dict(lang='es', home='Atino, inicio', nav=[('privacidad', 'Privacidad'), ('terms', 'Terms'), ('support', 'Support')],
               soon='Próximamente', skip='Saltar al contenido', contents='Contenido', on_page='En esta página', back='Volver a Atino',
               tabs=[('privacidad', 'Privacidad'), ('terms', 'Terms · EN'), ('support', 'Support · EN')], other=('privacy', 'English', 'en'),
               tagline='Tu CV ante las ofertas de Europa.',
               foot='&copy; 2026 Izotz Cristobal Mota. Atino llegará pronto al App Store para iPhone. Es independiente y no tiene relación con las empresas cuyas ofertas muestra. Las ofertas y los nombres de las capturas son datos de ejemplo.',
               more='Más en estas páginas', read_other='Read in English', pagelabel='Páginas de Atino'),
}
SIB = {
    'privacy': ('Privacy', 'How Atino handles your CV and your data.', 'en'),
    'privacidad': ('Privacidad', 'Cómo trata Atino tu CV y tus datos.', 'es'),
    'terms': ('Terms of Use', 'The rules for using Atino, free and Pro.', 'en'),
    'support': ('Support', 'Contact, and answers to common questions.', 'en'),
}
SIB_ORDER = {'privacy': ['terms', 'support', 'privacidad'], 'privacidad': ['terms', 'support', 'privacy'],
             'terms': ['privacy', 'support', 'privacidad'], 'support': ['privacy', 'terms', 'privacidad']}
HERO_PLATE = {'privacy': ('plate-what-leaves.jpg', '46%'), 'privacidad': ('plate-what-leaves.jpg', '46%'),
              'terms': ('plate-why-it-fits.jpg', '40%'), 'support': ('plate-alerts.jpg', '34%')}

CHECK = ('<svg viewBox="0 0 22 22" aria-hidden="true"><circle class="at-c" cx="11" cy="11" r="10" fill="none" stroke-width="1.6"/>'
         '<path class="at-c" d="M6.5 11.3l3.1 3.1 6-6.4" fill="none" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>')
CHECK_AMB = CHECK.replace('class="at-c"', 'stroke="#FFB547"')


def dev(src, alt, cls, eager=False):
    ld = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return f'<div class="at-dev {cls}"><img src="{MEDIA}{src}" width="600" height="1303" alt="{alt}" {ld}></div>'


def _cur(k, cur): return ' aria-current="page"' if k == cur else ''


def head(title, desc, canon, alts, lang, host, css):
    alt_links = ''.join(f'<link rel="alternate" hreflang="{l}" href="{host}{SLUG}/{k}.html">\n' for l, k in alts.items())
    og = f'{host}{SLUG}/media/og.jpg'
    d = _html.escape(desc, quote=True)
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#0B1416">
<title>{title}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{canon}">
{alt_links}<link rel="icon" type="image/png" href="{MEDIA}icon-32.png">
<link rel="apple-touch-icon" href="{MEDIA}icon-180.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Atino">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<style>{css}</style>
</head>
'''


def header(u, cur, abs_=False):
    links = ''.join(f'<a href="{BASE}{k}.html"{_cur(k, cur)}{"" if k == cur or k.startswith("priv") else " class=at-hide"}>{label}</a>' for k, label in u['nav'])
    return (f'<header class="at-head{" at-head--abs" if abs_ else ""}"><div class="at-wrap at-head__in">'
            f'<a class="at-brand" href="{BASE}" aria-label="{u["home"]}"><img src="{MEDIA}icon-64.png" width="38" height="38" alt="">Atino</a>'
            f'<nav class="at-nav" aria-label="Atino">{links}<span class="at-soon"><i aria-hidden="true"></i>{u["soon"]}</span></nav></div></header>')


def footer(u):
    pages = [('privacy', 'Privacy'), ('terms', 'Terms'), ('support', 'Support')] if u['lang'] == 'en' else \
            [('privacidad', 'Privacidad'), ('terms', 'Terms (EN)'), ('support', 'Support (EN)')]
    links = ''.join(f'<li><a href="{BASE}{k}.html">{l}</a></li>' for k, l in pages)
    if u['lang'] == 'en':
        links += f'<li><a href="{BASE}privacidad.html" lang="es" hreflang="es">Pol&iacute;tica de privacidad</a></li>'
    else:
        links += f'<li><a href="{BASE}privacy.html" lang="en" hreflang="en">Privacy policy in English</a></li>'
    return (f'<footer class="at-foot"><div class="at-wrap"><div class="at-foot__top">'
            f'<div class="at-foot__id"><img src="{MEDIA}icon-180.png" width="48" height="48" alt="" loading="lazy"><div><strong>Atino</strong><span>{u["tagline"]}</span></div></div>'
            f'<nav aria-label="{u["pagelabel"]}"><ul>{links}<li><a class="mail" href="mailto:hello@seizeapps.com">hello@seizeapps.com</a></li></ul></nav></div>'
            f'<small>{u["foot"]}</small></div></footer>')


# ------------------------------------------------------------------------------------------------ home
HILLS = ('<svg class="at-glow__hills" viewBox="0 0 1440 150" preserveAspectRatio="none" aria-hidden="true"><defs>'
         '<linearGradient id="at-h1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#16312F"/><stop offset="1" stop-color="#0B1416"/></linearGradient></defs>'
         '<path d="M0 90 C 180 20 320 20 480 70 S 800 130 980 60 S 1300 10 1440 70 V150 H0Z" fill="url(#at-h1)" opacity=".9"/>'
         '<path d="M0 120 C 220 70 380 90 560 115 S 900 140 1100 100 S 1340 80 1440 110 V150 H0Z" fill="#0B1416"/></svg>')
ARC = ('<svg viewBox="0 0 150 150" aria-hidden="true"><defs><linearGradient id="at-sunrise" gradientUnits="userSpaceOnUse" x1="14" y1="0" x2="136" y2="0">'
       '<stop offset="0" stop-color="#FF7A59"/><stop offset="1" stop-color="#FFB547"/></linearGradient></defs>'
       '<g transform="rotate(150 75 75)"><circle class="at-arc__t" cx="75" cy="75" r="58" pathLength="100"/>'
       '<circle class="at-arc__v" cx="75" cy="75" r="58" pathLength="100"/></g></svg>')
SAMPLE = '<p class="at-cap">Screens show sample jobs, not real listings.</p>'


def home(u):
    ck = CHECK
    h = [f'<body>\n<a class="at-skip" href="#main">{u["skip"]}</a>\n{header(u, None, abs_=True)}\n<main id="main">']
    h.append(f'''<section class="at-art at-hero" aria-labelledby="top"><div class="at-stage"><img src="{MEDIA}plate-ranked.jpg" width="1024" height="1536" alt="" fetchpriority="high"></div><div class="at-scrim"></div>
<div class="at-wrap at-hero__grid"><div>
<h1 id="top">Your CV against <span class="at-sun">Europe&rsquo;s jobs.</span></h1>
<p class="at-lead">Import your CV and Atino ranks current job ads across Europe by fit, with a short reason for each. Your name and contact details are removed on your iPhone first.</p>
<p class="at-badge" role="note">Coming soon to the App Store</p>
<ul class="at-meta"><li>iPhone &middot; iOS 26 or later</li><li>More than 100,000 current job ads</li></ul></div>
<figure class="at-hero__fig"><div class="at-stack at-hero__stack">{dev('atino-03-filters.jpg', 'Atino&rsquo;s Filters sheet: where you want to work and how you would work, with the number of jobs that match.', 'd1', True)}{dev('atino-02-job.jpg', 'A sample job in Atino: Customer Success Manager, a 95 percent strong fit arc, four meters showing why it fits, and a button that opens the employer&rsquo;s own page.', 'd2', True)}{dev('atino-01-matches.jpg', 'Atino&rsquo;s Matches tab: sample jobs ranked best fit first, each with a fit percent.', 'd3', True)}</div>
<figcaption>{SAMPLE}</figcaption></figure>
</div></section>''')
    h.append('''<section class="at-stats" aria-label="Atino at a glance"><div class="at-wrap"><ul>
<li><b>100,000+</b><span>current job ads, updated every day</span></li>
<li><b>24</b><span>interface languages</span></li>
<li><b>iPhone</b><span>iOS 26 or later</span></li>
<li><b>No account</b><span>No advertising, no tracking</span></li>
</ul></div></section>''')
    h.append('''<section class="at-s at-s--lift" id="how" aria-labelledby="how-h"><div class="at-wrap">
<div class="at-how__head"><p class="at-eyebrow">How it works</p><h2 class="at-h2" id="how-h">One job per screen.</h2></div>
<ol class="at-rail">
<li><h3>Import your CV</h3><p>A PDF. Scans work too.</p></li>
<li><h3>See what it would send</h3><p>Atino removes your name, email, phone number, address, date of birth and ID number on the iPhone, then shows you the exact text. You can edit it.</p></li>
<li><h3>Choose, then search</h3><p>Pick where you want to work and how. The best fit comes first.</p></li>
<li><h3>Open a job to read it</h3><p>Apply takes you to the employer&rsquo;s own page.</p></li>
</ol></div></section>''')
    h.append(f'''<section class="at-s" aria-labelledby="f1"><div class="at-wrap at-grid"><div>
<p class="at-eyebrow">Your CV stays on your iPhone</p>
<h2 class="at-h2" id="f1">Redacted on the phone, before anything is sent.</h2>
<p class="at-lead">Import a PDF (scans work too). Atino removes your name, email, phone, address, date of birth and ID number on the phone, then shows you the exact text it would send. You can edit it.</p>
<ul class="at-ticks"><li>{ck}<span>Your CV text is not sent until you allow it.</span></li><li>{ck}<span>Withdraw in Settings and your CV, and everything Atino derived from it, is deleted from your iPhone.</span></li></ul>
</div>
<figure style="margin:0"><div class="at-panel at-art" aria-hidden="true"><img src="{MEDIA}plate-what-leaves.jpg" width="1024" height="1536" alt="" loading="lazy" decoding="async">
<div class="at-redact"><p class="at-eyebrow">Removed on your iPhone first</p><ul class="at-chips"><li>Name</li><li>Email</li><li>Phone</li><li>Address</li><li>Date of birth</li><li>ID number</li></ul>
<p class="at-then">{ck}<span>Then you see the exact text it would send, and you can edit it.</span></p></div></div>
<figcaption class="at-fignote">Illustration, not a screenshot.</figcaption></figure></div></section>''')
    h.append(f'''<div class="at-pw"><section class="at-plate at-art at-glow" aria-labelledby="f2"><div class="at-scrim"></div>{HILLS}
<div class="at-wrap at-grid"><figure style="margin:0"><div class="at-stack at-glow__stack">{dev('atino-02-job.jpg', 'A sample job opened in Atino, with its fit arc and the four meters.', 'd2')}{dev('atino-01-matches.jpg', 'The Matches tab with sample jobs ranked by fit.', 'd1')}</div><figcaption>{SAMPLE}</figcaption></figure>
<div><p class="at-eyebrow">Best fit first</p><h2 class="at-h2" id="f2">The result list is the product.</h2>
<p class="at-lead">Choose where you want to work and how, then search. Every result shows a fit percent and a short reason, and the best fit comes first.</p>
<ul class="at-ticks"><li>{ck}<span>Open a job to read it.</span></li><li>{ck}<span>Apply opens the employer&rsquo;s own page in Safari. Atino doesn&rsquo;t take applications.</span></li></ul></div></div></section></div>''')
    h.append(f'''<section class="at-s at-s--lift" aria-labelledby="f3"><div class="at-wrap at-grid"><div>
<p class="at-eyebrow">An estimate, said plainly</p><h2 class="at-h2" id="f3">The percent is an estimate, not a promise.</h2>
<p class="at-lead">Four meters show why a job fits: the work, skills, level and requirements. Use them to decide where to look first.</p>
<div class="at-fit"><div class="at-arc at-art" aria-hidden="true">{ARC}<b>95<small>%</small></b><em>STRONG FIT</em></div>
<blockquote class="at-quote">Fit is an estimate from your CV. Use it to decide where to look first, not as a promise.<cite>From the job screen in Atino</cite></blockquote></div></div>
<figure style="margin:0"><div class="at-panel at-panel--why at-art"><img src="{MEDIA}plate-why-it-fits.jpg" width="1024" height="1536" alt="" loading="lazy" decoding="async">
<div class="at-sheet"><div><img src="{MEDIA}atino-02-job.jpg" width="600" height="1303" alt="The lower half of a sample job screen in Atino: four teal meters (the work, skills, level, requirements) under &ldquo;Why it fits&rdquo;, and the button &ldquo;Apply on the employer&rsquo;s site&rdquo;." loading="lazy" decoding="async"></div></div></div>
<figcaption class="at-fignote">Sample job, not a real listing.</figcaption></figure></div></section>''')
    h.append(f'''<div class="at-pw at-pw--lift"><section class="at-plate at-art at-filters" aria-labelledby="f4"><img class="at-bg" src="{MEDIA}plate-filters.jpg" width="1024" height="1536" alt="" loading="lazy" decoding="async"><div class="at-scrim"></div>
<div class="at-wrap at-grid"><div class="at-copy"><p class="at-eyebrow">Narrow it your way</p><h2 class="at-h2" id="f4">Say where, and how you&rsquo;d work.</h2>
<p class="at-lead">Location from your CV, on-site, hybrid or remote, then refine by occupation and keywords. Atino counts the jobs that match before you search.</p></div>
<div>{dev('atino-03-filters.jpg', 'The Filters sheet in Atino: where you want to work, how you would work, and the number of jobs that match these filters.', '')}</div></div></section></div>''')
    h.append('''<section class="at-s at-s--cream at-jobs" aria-labelledby="f5"><div class="at-wrap at-jobs__grid"><div>
<p class="at-eyebrow">The jobs</p><p class="at-big" aria-hidden="true">100,000<em>+</em></p>
<h2 class="at-h2" id="f5">More than 100,000 current job ads.</h2>
<p class="at-lead">Downloaded the first time you open the app and updated every day. Sources and licences are listed in Settings.</p></div>
<div><div class="at-src"><h3>Company career pages</h3><ul class="at-tags"><li>Greenhouse</li><li>Lever</li><li>Ashby</li><li>Recruitee</li><li>Teamtailor</li></ul></div>
<div class="at-src"><h3>Official open data</h3><ul class="at-tags"><li>Sweden&rsquo;s JobTech</li><li>Norway&rsquo;s NAV</li><li>Spain&rsquo;s BOE</li><li>Lanbide</li><li>ECYL</li><li>SEF Murcia</li><li>Czechia&rsquo;s MPSV</li></ul></div>
<p class="at-fine">Atino is independent and not affiliated with the employers it lists. Apply opens the employer&rsquo;s own page.</p></div></div></section>''')
    ca = CHECK.replace('class="at-c"', 'stroke="#5CD6C9"')
    h.append(f'''<div class="at-pw"><section class="at-plate at-art at-pro" id="pro" aria-labelledby="f6"><img class="at-bg" src="{MEDIA}plate-alerts.jpg" width="1024" height="1536" alt="" loading="lazy" decoding="async"><div class="at-scrim"></div>
<div class="at-wrap"><div class="at-pro__head"><p class="at-eyebrow">Free, and Atino Pro</p><h2 class="at-h2" id="f6">Atino keeps watching.</h2>
<p class="at-lead">Save a search and Atino keeps watching it for you, with one alert a day when something new fits.</p></div>
<div class="at-plans">
<div class="at-plan"><h3>Free</h3><p>Everything you need to try it.</p><ul><li>{ca}<span>One search a day</span></li><li>{ca}<span>Your top 10 matches</span></li><li>{ca}<span>Location and workplace filters</span></li></ul></div>
<div class="at-plan at-plan--pro"><h3>Atino Pro <span>Optional</span></h3><p>Weekly or monthly.</p><ul>
<li>{CHECK_AMB}<span>Every match, and all the filters</span></li>
<li>{CHECK_AMB}<span>Saved searches, which Atino keeps watching for you</span></li>
<li>{CHECK_AMB}<span>As many searches as you need, within a fair-use limit of 60 a day</span></li>
<li>{CHECK_AMB}<span>A daily alert at the time you choose, when a saved search has something new</span></li></ul></div></div>
<p class="at-pro__fine">Atino Pro is an optional subscription, weekly or monthly auto-renewing; the App Store shows the price before you buy. iOS decides the exact moment the daily alert arrives.</p></div></section></div>''')
    h.append(f'''<section class="at-s at-s--lift at-priv" id="privacy" aria-labelledby="f7"><div class="at-wrap at-grid"><div>
<p class="at-eyebrow">Private, and clear about it</p><h2 class="at-h2" id="f7">No account. No advertising. No tracking.</h2>
<p class="at-lead">Your CV, your results and your saved searches stay on your iPhone. The only analytics are purchase analytics, which never see your CV.</p>
<div class="at-links"><a class="at-btn" href="{BASE}privacy.html">Read the privacy policy</a><a class="at-btn at-btn--ghost" href="{BASE}privacidad.html" lang="es" hreflang="es">Leer en espa&ntilde;ol</a></div></div>
<ol class="at-steps"><li><h3>On your iPhone</h3><p>Your name and contact details are removed first. The PDF itself never leaves.</p></li>
<li><h3>Only when you allow it</h3><p>The redacted text goes through a relay that keeps no copy of it, to Command Code and TypeSafe AI, who run the ranking model and may keep what they receive under their own terms.</p></li>
<li><h3>Yours to withdraw</h3><p>Withdraw in Settings and your CV and everything Atino derived from it is deleted from your iPhone. What those services already received stays under their terms.</p></li></ol></div></section>''')
    h.append(f'</main>\n{footer(u)}\n</body>\n</html>\n')
    return '\n'.join(h)


# ------------------------------------------------------------------------------------------------ legal pages
def _strip(s): return re.sub(r'<[^>]+>', '', s).strip()


def _prep(body):
    """-> h1, updated line, doc html, toc [(id, text)]. Links to sibling pages become root-relative."""
    body = re.sub(r'href="(?:\.\./)?(privacy|privacidad|terms|support)\.html"', rf'href="{BASE}\1.html"', body)
    body = re.sub(r'<!--at-depth:[^>]*-->', '', body)
    h1 = re.search(r'<h1>(.*?)</h1>', body, re.S).group(1).strip(); body = body.replace(f'<h1>{h1}</h1>', '', 1)
    m = re.search(r'<p class="updated">(.*?)</p>', body, re.S); upd = m.group(1).strip(); body = body.replace(m.group(0), '', 1)
    toc, n = [], [0]

    def sec(mo):
        n[0] += 1; i = n[0]; t = mo.group(1).strip()
        num = re.match(r'(\d+)\.\s*(.*)', t, re.S)
        label = num.group(2) if num else t
        toc.append((f's{i}', _strip(label)))
        cls = ' class="at-sum"' if re.search(r'short version|versión corta', label, re.I) else ''
        inner = f'<span>{num.group(1)}</span>{label}' if num else label
        return f'<h2 id="s{i}"{cls}>{inner}</h2>'
    body = re.sub(r'<h2>(.*?)</h2>', sec, body, flags=re.S)
    return h1, upd, body.strip(), toc


def legal(u, lang, key, title, desc, body, host, alts):
    h1, upd, doc, toc = _prep(body)
    plate, pos = HERO_PLATE[key]
    solo = key == 'support'
    tabs = ''.join(f'<a href="{BASE}{k}.html"{_cur(k, key)}{" lang=en" if lang == "es" and k != "privacidad" else ""}>{l}</a>' for k, l in u['tabs'])
    ok, ol, olang = u['other']
    if key in ('privacy', 'privacidad'):
        tabs += f'<a href="{BASE}{ok}.html" lang="{olang}" hreflang="{olang}">{ol}</a>'
        langline = f'<p class="at-lang"><a href="{BASE}{ok}.html" lang="{olang}" hreflang="{olang}">{u["read_other"]}</a></p>'
    else:
        tabs += f'<a href="{BASE}privacidad.html" lang="es" hreflang="es">Español</a>'
        langline = ''
    tocl = ''.join(f'<li><a href="#{a}">{t}</a></li>' for a, t in toc)
    aside = '' if solo else f'<aside class="at-toc" aria-label="{u["on_page"]}"><p class="at-eyebrow">{u["on_page"]}</p><ol>{tocl}</ol></aside>'
    tocm = '' if solo else f'<details class="at-tocm"><summary>{u["contents"]}</summary><ol>{tocl}</ol></details>'
    cards = ''.join(f'<a class="at-sib" href="{BASE}{k}.html"{"" if SIB[k][2] == lang else " lang=" + SIB[k][2]}><strong>{SIB[k][0]}</strong><span>{SIB[k][1]}</span></a>'
                    for k in SIB_ORDER[key])
    css = root_css() + CSS_BASE + CSS_LEGAL
    out = head(title, desc, f'{host}{SLUG}/{key}.html', alts, lang, host, css)
    out += f'''<body>
<a class="at-skip" href="#main">{u["skip"]}</a>
<div class="at-art at-lhero"><div class="at-stage"><img src="{MEDIA}{plate}" width="1024" height="1536" alt="" fetchpriority="high" style="object-position:center {pos}"></div><div class="at-scrim"></div>
{header(u, key)}
<div class="at-wrap at-lhero__in"><h1>{h1}</h1><p class="at-upd">{upd}</p>{langline}
<nav class="at-tabs" aria-label="{u["pagelabel"]}">{tabs}</nav></div></div>
<div class="at-wrap at-lay{" at-lay--solo" if solo else ""}">{aside}
<main id="main" class="at-doc">{tocm}
{doc}
<nav class="at-sibs" aria-label="{u["more"]}">{cards}</nav>
<p class="at-more"><a href="{BASE}">&larr; {u["back"]}</a></p></main></div>
{footer(u)}
</body>
</html>
'''
    return out


def page(app, lang, key, title, desc, body, host, alts):
    global BASE, MEDIA
    deep = bool(re.search(r'href="\.\./(?:privacy|privacidad|terms|support)\.html"|<!--at-depth:\.\./', body))
    BASE = '../' if deep else './'; MEDIA = BASE + 'media/'
    u = UI[lang]
    if key == 'index':
        css = root_css() + CSS_BASE + CSS_HOME
        return head(title, desc, f'{host}{SLUG}/', {}, lang, host, css) + home(u)
    return legal(u, lang, key, title, desc, body, host, alts)
