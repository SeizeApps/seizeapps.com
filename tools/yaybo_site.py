"""Yaybo's own website: design system, page shells, the home page, support, legal layout, and the build audit.

Yaybo is a children's app, so its site is isolated on purpose (App Store guideline 4.3): its own CSS (inline, system fonts),
its own media under yaybo/media/, no link to the studio, to another app or to the App Store, no script, no CDN. The audit()
below enforces that and measures every text/background pair of the CSS in light and dark; build_pages() refuses to write
a single file when it fails.

gen_legal_yaybo.build_yaybo() calls build_pages(PRIVACY, TERMS, fill). The legal text is not touched here: it is wrapped
in <main>, the contents list is generated from its real headings and sits outside <main>.
"""
import os
import posixpath
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
YB = ROOT / 'yaybo'
SITE = 'https://seizeapps.com/yaybo/'
MAIL = 'hello@seizeapps.com'

# ---------------------------------------------------------------------------------------------------------------------
# Palette ("Sunny pond", from the app's KidTheme) -- the CSS custom properties AND the audit read these same dicts.
# ---------------------------------------------------------------------------------------------------------------------
LIGHT = {
    'page': '#FFF8EE', 'sunk': '#F4EEE4', 'surface': '#FFFFFF', 'ink': '#1E2640', 'ink2': '#5A6378', 'link': '#007285',
    'line': '#E9E2D6', 'lip': '#E2DACB', 'tint': '#DDF6F9', 'btn': '#007285', 'btnlip': '#005666', 'btnfg': '#FFFFFF',
    'focus': '#007285', 'band': '#14202B', 'bandink': '#F3F6F8', 'bandink2': '#AEBAC5', 'bandlink': '#4FD1E0',
    'chipbg': '#FFFFFF', 'restline': '#8A5A00', 'shadow': 'rgba(30,38,64,.20)', 'ring': 'rgba(0,0,0,0)',
    'plate-f': 'none', 'phone-f': 'none',
}
DARK = {
    'page': '#14202B', 'sunk': '#1A2833', 'surface': '#1E2C38', 'ink': '#F3F6F8', 'ink2': '#9AA6B2', 'link': '#4FD1E0',
    'line': '#2C3E4D', 'lip': '#0F1822', 'tint': '#1B3A44', 'btn': '#4FD1E0', 'btnlip': '#2A8E9C', 'btnfg': '#10202A',
    'focus': '#4FD1E0', 'band': '#0D1720', 'bandink': '#F3F6F8', 'bandink2': '#9AA6B2', 'bandlink': '#4FD1E0',
    'chipbg': '#1E2C38', 'restline': '#FFD45C', 'shadow': 'rgba(0,0,0,.42)', 'ring': '#2A3A48',
    'plate-f': 'brightness(.84) saturate(.95)', 'phone-f': 'brightness(.94)',
}
FIXED = {   # the same in both modes: islands that carry their own background
    'cream': '#FFF8EE', 'white': '#FFFFFF', 'navy': '#1E2640', 'sun': '#FFC107', 'sunlip': '#D99A00',
    'teal': '#06505E', 'tealtop': '#0A6475', 'cyan': '#9BEAF4', 'tealink': '#E6F7F9', 'chip': '#DDF6F9',
    'navypanel': '#1E2640', 'navyink': '#E3E7F0', 'foot': '#0E1B24', 'foot2': '#C5D0D9', 'scrimc': '#033440',
    'lband': '#06505E', 'lbandtop': '#04404D', 'sundot': '#FFC21A', 'iconink': '#1E2640',
}


def mode_colors(mode):
    d = dict(FIXED)
    d.update(LIGHT if mode == 'light' else DARK)
    return d


# Hero scrim, one source for the CSS and for the measurement over the composited picture.
SCRIM_H = [(0, .95), (.46, .90), (.60, .52), (1, .20)]          # left -> right, desktop
SCRIM_B = [(0, .62), (.30, .0)]                                  # nav strip at the top  (y fraction -> alpha)
SCRIM_F = [(.74, 0), (1, .55)]                                   # foot of the hero      (y fraction -> alpha)
SCRIM_M = [(0, .92), (.55, .90), (1, .66)]                       # top -> bottom, mobile (text above, phone below)
HERO_ZOOM = 1.45
HERO_ORIGIN = (1.0, .55)


def _stops(stops, c='3,52,64'):
    return ','.join(f'rgba({c},{a:g}) {p * 100:g}%' for p, a in stops)


# ---------------------------------------------------------------------------------------------------------------------
# Contrast
# ---------------------------------------------------------------------------------------------------------------------
def _lin(v):
    v /= 255
    return v / 12.92 if v <= .03928 else ((v + .055) / 1.055) ** 2.4


def lum(h):
    h = h.lstrip('#')
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return .2126 * _lin(r) + .7152 * _lin(g) + .0722 * _lin(b)


def ratio(a, b):
    la, lb = lum(a), lum(b)
    if la < lb:
        la, lb = lb, la
    return (la + .05) / (lb + .05)


# (label, foreground key, background key, minimum). Keys resolve per mode through mode_colors().
PAIRS = [
    # page surfaces
    ('body text on page', 'ink', 'page', 4.5), ('secondary text on page', 'ink2', 'page', 4.5), ('link on page', 'link', 'page', 4.5),
    ('body text on sunk', 'ink', 'sunk', 4.5), ('secondary text on sunk', 'ink2', 'sunk', 4.5), ('link on sunk', 'link', 'sunk', 4.5),
    ('body text on card', 'ink', 'surface', 4.5), ('secondary text on card', 'ink2', 'surface', 4.5), ('link on card', 'link', 'surface', 4.5),
    ('text on tint chip', 'ink', 'tint', 4.5), ('text on chip background', 'ink', 'chipbg', 4.5), ('secondary on chip background', 'ink2', 'chipbg', 4.5),
    ('button label (teal button)', 'btnfg', 'btn', 4.5), ('teal button against page (UI boundary)', 'btn', 'page', 3.0),
    ('focus ring on page', 'focus', 'page', 3.0), ('focus ring on card', 'focus', 'surface', 3.0), ('focus ring on sunk', 'focus', 'sunk', 3.0),
    ('rest-day outline on card', 'restline', 'surface', 3.0), ('rest-day outline on sunk', 'restline', 'sunk', 3.0),
    # fixed islands
    ('white on teal panel', 'white', 'teal', 4.5), ('cyan kicker on teal panel', 'cyan', 'teal', 4.5), ('lede on teal panel', 'tealink', 'teal', 4.5),
    ('white on teal panel (top of gradient)', 'white', 'tealtop', 4.5), ('cyan kicker on teal gradient top', 'cyan', 'tealtop', 4.5),
    ('ink on chip inside teal panel', 'navy', 'chip', 4.5), ('sun button label', 'navy', 'sun', 4.5),
    ('sun button against teal panel', 'sun', 'teal', 3.0), ('sun button against navy panel', 'sun', 'navypanel', 3.0),
    ('white on navy panel', 'white', 'navypanel', 4.5), ('lede on navy panel', 'navyink', 'navypanel', 4.5), ('sun kicker on navy panel', 'sun', 'navypanel', 4.5),
    ('badge text on cream', 'navy', 'cream', 4.5), ('Yay bubble', 'navy', 'white', 4.5),
    ('white on legal band', 'white', 'lband', 4.5), ('white on legal band (dark end)', 'white', 'lbandtop', 4.5), ('sun on legal band', 'sun', 'lband', 4.5),
    # the dark Parent Zone band
    ('text on the dark band', 'bandink', 'band', 4.5), ('secondary text on the dark band', 'bandink2', 'band', 4.5), ('kicker/link on the dark band', 'bandlink', 'band', 4.5),
    ('focus ring on the dark band', 'bandlink', 'band', 3.0),
    # footer panel
    ('white on footer panel', 'white', 'foot', 4.5), ('footer secondary text and disclaimer', 'foot2', 'foot', 4.5), ('sun focus on footer', 'sun', 'foot', 3.0),
    # icon tile on cards
    ('icon stroke on sun tile', 'iconink', 'sun', 4.5),
]


def contrast_rows():
    rows, ok = [], True
    for mode in ('light', 'dark'):
        c = mode_colors(mode)
        for label, fg, bg, mn in PAIRS:
            r = ratio(c[fg], c[bg])
            good = r >= mn
            ok &= good
            rows.append((f'{mode}: {label}', round(r, 2), mn, good))
    return rows, ok


def hero_rows():
    """White and sun-yellow text, and the focus ring, measured over the actual hero picture with the scrim composited.
    Desktop uses the page's own crop (cover + zoom); the numbers are the worst pixel (99.7th percentile) inside each box."""
    try:
        from PIL import Image
    except ImportError:
        return [('hero composite: skipped (Pillow missing)', 0, 0, True)], True
    src = Image.open(YB / 'media' / 'axolotl-reef.jpg').convert('RGB')
    rows, ok = [], True
    scr = tuple(int(FIXED['scrimc'].lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))

    def interp(stops, t):
        if t <= stops[0][0]:
            return stops[0][1]
        for (p0, a0), (p1, a1) in zip(stops, stops[1:]):
            if t <= p1:
                return a0 + (a1 - a0) * (t - p0) / (p1 - p0)
        return stops[-1][1]

    def composite(w, h, zoom, origin, scrim_fn):
        s = max(w / src.width, h / src.height)
        cover = src.resize((round(src.width * s), round(src.height * s)))
        ox, oy = (cover.width - w) / 2, (cover.height - h) / 2
        base = cover.crop((round(ox), round(oy), round(ox) + w, round(oy) + h))
        if zoom != 1:
            px, py = origin[0] * w, origin[1] * h
            base = base.transform((w, h), Image.AFFINE, (1 / zoom, 0, px - px / zoom, 0, 1 / zoom, py - py / zoom), Image.BICUBIC)
        px_ = base.load()
        out = Image.new('RGB', (w, h))
        o = out.load()
        for y in range(h):
            for x in range(w):
                r, g, b = px_[x, y]
                a = scrim_fn(x / w, y / h)
                o[x, y] = (round(r * (1 - a) + scr[0] * a), round(g * (1 - a) + scr[1] * a), round(b * (1 - a) + scr[2] * a))
        return out

    def worst(img, box):
        w, h = img.size
        x0, y0, x1, y1 = (round(box[0] * w), round(box[1] * h), round(box[2] * w), round(box[3] * h))
        vals = sorted(lum('#%02x%02x%02x' % img.getpixel((x, y))) for x in range(x0, x1, 3) for y in range(y0, y1, 3))
        return vals[int(len(vals) * .997) - 1]

    def over(layers):
        def f(x, y):
            keep = 1.0
            for a in layers:
                keep *= 1 - a(x, y)
            return 1 - keep
        return f

    desk = composite(480, 287, HERO_ZOOM, HERO_ORIGIN,
                     over([lambda x, y: interp(SCRIM_H, x), lambda x, y: interp(SCRIM_B, y), lambda x, y: interp(SCRIM_F, y)]))
    mob = composite(195, 480, 1.0, (.5, .5), over([lambda x, y: interp(SCRIM_M, y), lambda x, y: interp(SCRIM_B, y * 2)]))
    jobs = [
        ('hero headline and lede (desktop)', desk, (.07, .14, .50, .78), [('white', 4.5), ('sun', 4.5)]),
        ('hero nav (desktop)', desk, (.55, .0, .97, .09), [('white', 4.5)]),
        ('hero badge row fine print (desktop)', desk, (.07, .70, .50, .82), [('white', 4.5)]),
        ('hero text (mobile)', mob, (0, .10, 1, .62), [('white', 4.5), ('sun', 4.5)]),
    ]
    for label, img, box, checks in jobs:
        lw = worst(img, box)
        for fgk, mn in checks:
            r = (lum(FIXED[fgk]) + .05) / (lw + .05)
            ok &= r >= mn
            rows.append((f'composited {label}: {fgk} text', round(r, 2), mn, r >= mn))
    return rows, ok


# ---------------------------------------------------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------------------------------------------------
def _vars(d):
    return ''.join(f'--{k}:{v};' for k, v in d.items())


def build_css():
    dark = {k: v for k, v in DARK.items() if LIGHT.get(k) != v}
    scrim_desktop = (f'linear-gradient(90deg,{_stops(SCRIM_H)}),linear-gradient(180deg,{_stops(SCRIM_B)}),'
                     f'linear-gradient(180deg,{_stops(SCRIM_F)})')
    scrim_mobile = f'linear-gradient(180deg,{_stops(SCRIM_M)}),linear-gradient(180deg,{_stops([(0, SCRIM_B[0][1]), (SCRIM_B[1][0] / 2, 0)])})'
    css = CSS
    css = css.replace('@@LIGHT@@', _vars(LIGHT) + _vars(FIXED))
    css = css.replace('@@DARK@@', _vars(dark))
    css = css.replace('@@SCRIM_DESKTOP@@', scrim_desktop).replace('@@SCRIM_MOBILE@@', scrim_mobile)
    css = css.replace('@@ZOOM@@', f'{HERO_ZOOM:g}').replace('@@ORIGIN@@', f'{HERO_ORIGIN[0] * 100:g}% {HERO_ORIGIN[1] * 100:g}%')
    return re.sub(r'\n\s*', '\n', css).strip()


CSS = r'''
:root{color-scheme:light dark;@@LIGHT@@
--ffd:ui-rounded,"SF Pro Rounded","Arial Rounded MT Bold","Avenir Next",system-ui,sans-serif;
--ffb:ui-rounded,"SF Pro Rounded","Avenir Next","Segoe UI",system-ui,sans-serif}
@media (prefers-color-scheme:dark){:root{@@DARK@@}}
*{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{animation:none!important;transition:none!important}}
body{margin:0;background:var(--page);color:var(--ink);font:400 18px/1.6 var(--ffb);overflow-x:hidden}
.yb-sec{overflow-x:clip}
img{max-width:100%;height:auto}
a{color:var(--link);text-underline-offset:3px}
p{margin:0 0 1em}
h1,h2,h3{font-family:var(--ffd);margin:0;letter-spacing:-.01em;line-height:1.1;font-weight:800}
:focus-visible{outline:3px solid var(--focus);outline-offset:3px;border-radius:6px}
.yb-dark :focus-visible{outline-color:var(--bandlink)}
.yb-onhero :focus-visible,.yb-foot :focus-visible{outline-color:var(--white)}
.yb-skip{position:absolute;left:12px;top:-80px;background:var(--surface);color:var(--ink);padding:12px 18px;border-radius:12px;z-index:60;font-weight:700}
.yb-skip:focus{top:12px}
.yb-wrap{width:min(1180px,100% - 48px);margin-inline:auto}

/* header */
.yb-top{position:relative;z-index:10;padding:22px 0}
.yb-top.abs{position:absolute;inset:0 0 auto 0}
.yb-top .yb-wrap{display:flex;align-items:center;justify-content:space-between;gap:12px}
.yb-brand{display:flex;align-items:center;gap:12px;text-decoration:none;color:var(--white);font:800 24px/1 var(--ffd)}
.yb-brand img{width:44px;height:44px;border-radius:12px;box-shadow:0 2px 0 rgba(0,40,50,.4),0 8px 20px rgba(0,40,50,.35)}
.yb-nav{display:flex;gap:4px;flex-wrap:nowrap}
.yb-nav a{color:var(--white);text-decoration:none;font-weight:700;font-size:16px;padding:10px 14px;border-radius:999px;white-space:nowrap}
.yb-nav a:hover{background:rgba(255,255,255,.18)}
.yb-nav a[aria-current]{background:rgba(255,255,255,.22)}

/* buttons and badge */
.yb-btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:52px;font:800 18px/1.1 var(--ffd);text-decoration:none;padding:15px 26px;border-radius:20px;
cursor:pointer;border:0;transition:transform .2s cubic-bezier(.3,1.7,.5,1),box-shadow .2s;position:relative}
.yb-btn-sun{background:var(--sun);color:var(--navy);box-shadow:0 5px 0 var(--sunlip),0 14px 26px rgba(0,30,40,.3)}
.yb-btn-teal{background:var(--btn);color:var(--btnfg);box-shadow:0 5px 0 var(--btnlip),0 14px 26px var(--shadow)}
.yb-btn:hover{transform:translateY(-2px)}
.yb-btn:active{transform:translateY(4px);box-shadow:0 1px 0 rgba(0,0,0,.25)}
.yb-btn:focus-visible{outline:3px solid var(--bandlink);outline-offset:4px}
.yb-onhero .yb-btn:focus-visible,.yb-story .yb-btn:focus-visible,.yb-dark .yb-btn:focus-visible{outline:3px solid #9BEAF4;outline-offset:4px}
.yb-badge{display:inline-flex;align-items:center;gap:12px;background:var(--cream);color:var(--navy);padding:11px 22px 11px 16px;border-radius:20px;margin:0;
box-shadow:0 4px 0 #E2DACB,0 12px 24px rgba(0,30,40,.3);text-align:left}
.yb-badge svg{width:26px;height:26px;flex:none}
.yb-badge small{display:block;font:700 13.5px/1.1 var(--ffb);letter-spacing:.01em;margin-bottom:3px}
.yb-badge b{display:block;font:800 17px/1.1 var(--ffd)}

/* hero */
.yb-hero{position:relative;color:var(--white);overflow:hidden;isolation:isolate;padding:150px 0 150px;min-height:820px}
.yb-bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-3;transform:scale(@@ZOOM@@);transform-origin:@@ORIGIN@@;filter:var(--plate-f)}
.yb-hero .yb-scrim{position:absolute;inset:0;z-index:-2;background:@@SCRIM_DESKTOP@@}
.yb-hero-grid{display:grid;grid-template-columns:minmax(0,1.02fr) minmax(0,.98fr);gap:24px;align-items:center}
.yb-eyebrow{display:inline-block;font:800 15px/1 var(--ffd);color:var(--white);background:rgba(3,52,64,.55);border:2px solid rgba(255,255,255,.5);padding:9px 14px;border-radius:999px;margin:0 0 22px}
.yb-hero h1{font-size:clamp(40px,4.9vw,72px);line-height:1.04;margin-bottom:22px;text-wrap:balance}
.yb-hero h1 em{font-style:normal;color:var(--sun)}
.yb-lede{font-size:clamp(19px,1.6vw,22px);line-height:1.5;color:var(--white);max-width:33em}
.yb-cta{display:flex;flex-wrap:wrap;gap:18px 20px;align-items:center;margin:30px 0 20px}
.yb-fine{font-size:15.5px;color:var(--white);margin:0}
.yb-hero-art{container-type:inline-size;position:relative;width:100%;max-width:620px;margin-inline:auto;aspect-ratio:1/1.2}
.yb-hero-art .yb-float{position:absolute}
.yb-hero-art .c{left:25cqw;top:2cqw;width:50cqw;z-index:3;animation:yb-bob 7s ease-in-out infinite}
.yb-hero-art .l{left:-3cqw;top:20cqw;width:40cqw;z-index:2;transform:rotate(-9deg)}
.yb-hero-art .r{right:-3cqw;top:20cqw;width:40cqw;z-index:2;transform:rotate(9deg)}
.yb-hero-art .l .yb-ph,.yb-hero-art .r .yb-ph{animation:yb-bob 8s ease-in-out -3s infinite}
.yb-hero-art .y{right:-6cqw;bottom:-4cqw;width:32cqw;height:auto;z-index:4;filter:drop-shadow(0 12px 18px rgba(0,30,40,.4));animation:yb-wiggle 5s ease-in-out infinite;transform-origin:50% 90%}
@keyframes yb-bob{50%{translate:0 -10px}}
@keyframes yb-wiggle{0%,100%{rotate:-2deg}50%{rotate:3deg}}
.yb-bubbles span{position:absolute;border-radius:50%;background:radial-gradient(circle at 30% 30%,rgba(255,255,255,.7),rgba(255,255,255,.12) 60%);border:1.5px solid rgba(255,255,255,.35);animation:yb-rise linear infinite;z-index:-1;bottom:-40px}
@keyframes yb-rise{to{transform:translateY(-1000px)}}
.yb-wave{display:block;width:100%;height:auto;position:absolute;left:0;right:0;pointer-events:none}
.yb-wave.b{bottom:-1px}.yb-wave.t{top:-1px;transform:scaleY(-1)}
.yb-wave path{fill:var(--page)}

/* device frames */
.yb-ph{container-type:inline-size;width:var(--w,260px);flex:none}
.yb-ph-body{position:relative;padding:3.1cqw;border-radius:15.5cqw;background:linear-gradient(145deg,#38425A,#161D2C 55%,#232C42);
box-shadow:inset 0 0 0 .6cqw #4A5572,0 0 0 1px var(--ring),0 3cqw 7cqw var(--shadow),0 .8cqw 2cqw rgba(20,30,50,.18)}
.yb-ph-body img{display:block;width:100%;height:auto;border-radius:12.5cqw;background:var(--cream);filter:var(--phone-f)}
.yb-ph-body::before{content:"";position:absolute;right:-1cqw;top:26cqw;width:1.2cqw;height:16cqw;border-radius:1cqw;background:#2E3850}
.yb-pad{container-type:inline-size;width:var(--w,100%)}
.yb-pad-body{padding:2.4cqw;border-radius:4.6cqw;background:linear-gradient(145deg,#38425A,#161D2C 55%,#232C42);box-shadow:inset 0 0 0 .4cqw #4A5572,0 0 0 1px var(--ring),0 3cqw 7cqw var(--shadow)}
.yb-pad-body img{display:block;width:100%;height:auto;border-radius:2.6cqw;filter:var(--phone-f)}
.yb-cap{font:800 17px/1.25 var(--ffd);margin:22px 0 0;display:flex;align-items:center;gap:12px;color:var(--ink)}
.yb-cap b{flex:none;display:grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--btn);color:var(--btnfg);box-shadow:0 3px 0 var(--btnlip);font-size:17px}
.yb-sub{font-size:16.5px;color:var(--ink2);margin:6px 0 0}

/* sections */
.yb-sec{position:relative;padding:96px 0;isolation:isolate}
.yb-sec.sunk{background:var(--sunk)}
.yb-sec h2{font-size:clamp(32px,3.8vw,52px);margin-bottom:20px;text-wrap:balance}
.yb-kicker{font:800 15px/1.2 var(--ffd);color:var(--link);margin:0 0 16px;display:flex;align-items:center;gap:10px}
.yb-kicker i{width:30px;height:5px;border-radius:5px;background:var(--link);display:block;flex:none}
.yb-sec p.big{font-size:20px;line-height:1.55;color:var(--ink2)}
.yb-two{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:64px;align-items:center}
.yb-two.skills{grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr)}
.yb-steps{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;align-items:start;margin:0;padding:0}
.yb-steps li{list-style:none}
.yb-steps li:nth-child(2){margin-top:56px}
.yb-steps .yb-ph{--w:100%}
.yb-facts{margin:26px 0 0;padding:0;display:grid;gap:12px}
.yb-facts li{list-style:none;display:flex;gap:12px;align-items:flex-start;font-size:18px}
.yb-facts li::before{content:"";flex:none;width:22px;height:22px;margin-top:3px;border-radius:50%;background:var(--btn) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M6 12.5l4 4 8-9' fill='none' stroke='%23fff' stroke-width='3.4' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/70% no-repeat}
.yb-chips{display:flex;flex-wrap:wrap;gap:10px;margin:26px 0 0;padding:0}
.yb-chips li{list-style:none;display:inline-flex;align-items:center;gap:9px;font:800 16px/1.15 var(--ffd);padding:11px 15px 11px 12px;border-radius:14px;background:var(--chipbg);border:2px solid var(--line);box-shadow:0 3px 0 var(--lip);color:var(--ink)}
.yb-chips li i{width:14px;height:14px;border-radius:50%;flex:none}

/* skills: the plate is a banner, the phones climb out of it */
.yb-stage{position:relative;width:100%;max-width:660px;margin-inline:auto}
.yb-stage-plate{display:block;width:100%;aspect-ratio:2.35/1;object-fit:cover;object-position:50% 22%;border-radius:36px;box-shadow:0 6px 0 var(--lip),0 24px 50px var(--shadow);filter:var(--plate-f)}
.yb-fan{position:relative;container-type:inline-size;width:100%;aspect-ratio:1.5/1;margin-top:-17%}
.yb-fan .yb-ph{position:absolute;--w:35cqw}
.yb-fan .a{left:14cqw;top:3cqw;transform:rotate(-6deg);z-index:2;--w:37cqw}
.yb-fan .c{right:14cqw;top:9cqw;transform:rotate(6deg);z-index:1;--w:37cqw}

/* story cards: solid copy panel + illustrated plate */
.yb-story{position:relative;max-width:1180px;margin:0 auto;border-radius:44px;overflow:hidden;color:var(--white);isolation:isolate;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.05fr);min-height:520px;box-shadow:0 6px 0 rgba(0,0,0,.18),0 30px 60px var(--shadow)}
.yb-story.flip{grid-template-columns:minmax(0,1.05fr) minmax(0,1fr)}
.yb-story .copy{position:relative;z-index:1;padding:clamp(34px,5vw,72px);display:flex;flex-direction:column;justify-content:center}
.yb-story .art{position:relative;min-height:320px}
.yb-story .art img.plate{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:var(--plate-f)}
.yb-story.flip .art{order:-1}
.yb-story.teal{background:var(--teal)}
.yb-story.teal .copy{background:linear-gradient(180deg,var(--tealtop),var(--teal))}
.yb-story.navy{background:var(--navypanel)}
.yb-story h2{color:var(--white);margin-bottom:16px;font-size:clamp(32px,3.6vw,50px)}
.yb-story .yb-kicker{color:var(--cyan)}.yb-story .yb-kicker i{background:var(--cyan)}
.yb-story.navy .yb-kicker{color:var(--sun)}.yb-story.navy .yb-kicker i{background:var(--sun)}
.yb-story p.lede{font-size:19.5px;line-height:1.55;color:var(--tealink);margin:0 0 20px}
.yb-story.navy p.lede{color:var(--navyink)}
.yb-story .yb-btn{align-self:flex-start;margin-top:8px}
.yb-bub{position:absolute;left:46%;top:13%;z-index:2;background:var(--white);color:var(--navy);border-radius:26px 26px 26px 8px;padding:12px 26px 14px;font:800 clamp(24px,2.6vw,36px)/1.1 var(--ffd);box-shadow:0 14px 28px -12px rgba(0,40,50,.6)}
.yb-bub::after{content:"";position:absolute;left:18px;bottom:-12px;width:24px;height:24px;background:var(--white);clip-path:polygon(0 0,100% 0,0 100%);transform:skewX(-8deg)}
.yb-no{display:flex;flex-wrap:wrap;gap:10px;margin:4px 0 6px;padding:0}
.yb-no li{list-style:none;display:inline-flex;align-items:center;gap:9px;font:800 16px/1.1 var(--ffd);padding:10px 15px 10px 12px;border-radius:14px;background:var(--chip);color:var(--navy)}
.yb-no li svg{width:18px;height:18px;flex:none}
.yb-pair{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:28px;max-width:1180px;margin:40px auto 0}
.yb-tile{background:var(--surface);border:2px solid var(--line);border-radius:32px;padding:34px 36px 32px;box-shadow:0 6px 0 var(--lip),0 24px 48px var(--shadow)}
.yb-tile h3{font-size:26px;margin-bottom:10px}
.yb-tile p{color:var(--ink2);font-size:17.5px;margin:0}
.yb-streak{display:grid;grid-template-columns:minmax(0,1fr) 150px;gap:28px;align-items:end}
.yb-streak .yb-ph{--w:100%}
.yb-week{display:grid;grid-template-columns:repeat(7,1fr);gap:7px;margin:22px 0 14px;padding:22px 14px 16px;border-radius:22px;background:var(--sunk)}
.yb-week span{display:grid;gap:7px;justify-items:center;font:800 13.5px/1 var(--ffd);color:var(--ink2)}
.yb-week i{display:block;width:min(100%,40px);aspect-ratio:1;border-radius:50%}
.yb-week i.on{background:var(--sundot);box-shadow:inset 0 -4px 0 rgba(217,154,0,.65)}
.yb-week i.off{background:var(--surface);box-shadow:inset 0 0 0 2px var(--lip)}
.yb-week i.rest{border:2.5px dashed var(--restline)}
.yb-legend{display:flex;flex-wrap:wrap;gap:6px 20px;margin:0 0 20px;padding:0;font-size:14.5px;color:var(--ink2)}
.yb-legend li{list-style:none;display:flex;align-items:center;gap:8px}
.yb-legend i{display:block;width:14px;height:14px;border-radius:50%}
.yb-legend i.on{background:var(--sundot)}.yb-legend i.rest{border:2px dashed var(--restline)}
.yb-guides{display:flex;flex-direction:column}
.yb-meet{display:grid;grid-template-rows:1fr 1fr;flex:1;gap:14px;margin:18px 0 0;padding:0}
.yb-meet figure{margin:0;display:flex;align-items:center;gap:16px;background:var(--sunk);border-radius:22px;padding:12px 18px 12px 12px}
.yb-meet .m{width:min(124px,28%);aspect-ratio:1;border-radius:18px;background:var(--cream);display:grid;place-items:end center;overflow:hidden;flex:none}
.yb-meet .m img{width:100%;height:100%;object-fit:contain}
.yb-meet .m.tad{background:var(--white)}
.yb-meet figcaption{font-size:16.5px;line-height:1.35;color:var(--ink2)}
.yb-meet figcaption b{display:block;color:var(--ink);font:800 20px/1.2 var(--ffd);margin-bottom:2px}

/* progress */
.yb-road{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:56px;align-items:center;max-width:1180px;margin:64px auto 0}
.yb-device{position:relative;container-type:inline-size;width:100%;max-width:640px;margin-inline:auto;padding-bottom:12cqw}
.yb-device .yb-pad{--w:100%}
.yb-device .p1{position:absolute;right:-2cqw;bottom:0;--w:24cqw;z-index:3;transform:rotate(4deg)}
.yb-friends{display:flex;gap:10px;margin:20px 0 0;padding:0;flex-wrap:wrap}
.yb-friends li{list-style:none;width:64px;height:64px;border-radius:50%;background:var(--tint);border:3px solid var(--line);box-shadow:0 4px 0 var(--lip);display:grid;place-items:center;overflow:hidden}
.yb-friends img{width:76%;height:auto}
.yb-cards{display:flex;justify-content:flex-start;margin:34px 0 0;padding:0 0 0 10px}
.yb-cards li{list-style:none;width:23%;min-width:92px;aspect-ratio:3/2;background:#fff;padding:2.4%;border-radius:10px;box-shadow:0 14px 26px rgba(30,38,64,.30);margin-left:-3%}
.yb-cards li:nth-child(1){transform:rotate(-7deg) translateY(8px);margin-left:0}
.yb-cards li:nth-child(2){transform:rotate(3deg) translateY(-6px);z-index:2}
.yb-cards li:nth-child(3){transform:rotate(-2deg) translateY(6px);z-index:3}
.yb-cards li:nth-child(4){transform:rotate(7deg)}
.yb-cards img{width:100%;height:100%;object-fit:cover;border-radius:5px;display:block}

/* grown-ups: one deliberate dark moment */
.yb-band{background:var(--band);color:var(--bandink);padding:112px 0 100px}
.yb-band h2{color:var(--bandink);font-size:clamp(32px,3.8vw,52px);margin-bottom:20px;text-wrap:balance}
.yb-band .yb-kicker{color:var(--bandlink)}.yb-band .yb-kicker i{background:var(--bandlink)}
.yb-grow{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:72px;align-items:center}
.yb-grow-art{position:relative;display:grid;place-items:center;padding:10px 0}
.yb-grow-art::before{content:"";position:absolute;inset:6% 4%;border-radius:44px;background:radial-gradient(circle at 50% 40%,rgba(79,209,224,.22),rgba(79,209,224,0) 70%)}
.yb-grow-art .yb-ph{--w:min(100%,330px);position:relative}
.yb-band p.big{color:var(--bandink2)}
.yb-pts{display:grid;gap:22px;margin:34px 0 0;padding:0}
.yb-pts li{list-style:none;display:grid;grid-template-columns:46px minmax(0,1fr);gap:4px 18px;align-items:start}
.yb-pts .yb-ico{grid-row:1/3}
.yb-pts h3{font-size:20px;color:var(--bandink);align-self:end;margin:0}
.yb-pts p{font-size:16.5px;color:var(--bandink2);margin:0;line-height:1.5}
.yb-swipe{display:none;align-items:center;justify-content:center;gap:8px;margin:2px 0 0;font:700 15px/1.3 var(--ffd);color:var(--ink2)}
.yb-swipe svg{width:18px;height:18px;flex:none;animation:yb-nudge 1.8s ease-in-out 3}
.yb-band .yb-swipe{color:var(--bandink2)}
@keyframes yb-nudge{0%,100%{transform:translateX(0)}50%{transform:translateX(5px)}}
.yb-gate{display:flex;align-items:center;gap:14px;margin:38px 0 0;max-width:560px;padding:16px 22px;border-radius:20px;border:2px solid var(--bandink2);color:var(--bandink);font:700 17px/1.4 var(--ffd);text-align:left}
.yb-gate svg{width:26px;height:26px;flex:none;stroke:var(--bandlink);fill:none;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}

/* trust */
.yb-tgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;max-width:1180px;margin:40px auto 0;padding:0}
.yb-tgrid li{list-style:none;background:var(--surface);color:var(--ink);border:2px solid var(--line);box-shadow:0 5px 0 var(--lip),0 24px 40px var(--shadow);border-radius:24px;padding:26px 22px 24px}
.yb-tgrid h3{font-size:20px;margin:16px 0 8px;line-height:1.2}
.yb-tgrid p{font-size:16.5px;line-height:1.5;margin:0;color:var(--ink2)}
.yb-ico{width:46px;height:46px;border-radius:14px;background:var(--sun);display:grid;place-items:center;box-shadow:0 3px 0 var(--sunlip)}
.yb-ico svg{width:26px;height:26px;stroke:var(--iconink);fill:none;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}

/* spec strip + closing */
.yb-specs{max-width:1180px;margin:0 auto;padding:44px 0 0;border-top:2px solid var(--line);display:grid;grid-template-columns:repeat(4,1fr);gap:28px}
.yb-specs dt{font:800 14px/1.2 var(--ffd);color:var(--ink2);margin:0 0 6px}
.yb-specs dd{margin:0;font:700 17.5px/1.4 var(--ffd);color:var(--ink)}
.yb-specs dd small{display:block;font:400 15.5px/1.5 var(--ffb);color:var(--ink2);margin-top:4px}
.yb-close{max-width:1180px;margin:0 auto;border-radius:44px;background:linear-gradient(135deg,var(--tealtop),var(--teal) 60%);color:var(--white);display:grid;grid-template-columns:minmax(0,240px) minmax(0,1fr);gap:40px;align-items:center;padding:48px clamp(28px,5vw,72px);box-shadow:0 6px 0 rgba(0,0,0,.18),0 30px 60px var(--shadow)}
.yb-close img{width:100%;height:auto;filter:drop-shadow(0 12px 18px rgba(0,30,40,.35))}
.yb-close h2{color:var(--white);font-size:clamp(30px,3.4vw,46px);margin-bottom:10px}
.yb-close p{color:var(--tealink);font-size:19px;margin:0 0 22px}
.yb-close p.yb-badge{color:var(--navy);margin:0;font-size:inherit}

/* footer */
.yb-foot{position:relative;margin-top:96px}
.yb-foot-art{position:relative;height:230px;overflow:hidden;isolation:isolate}
.yb-foot-art img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 62%;z-index:-1;filter:var(--plate-f)}
.yb-foot-panel{background:var(--foot);color:var(--white);padding:46px 0 44px}
.yb-foot-grid{display:flex;justify-content:space-between;gap:30px 36px;flex-wrap:wrap;align-items:flex-start}
.yb-foot .yb-brand{font-size:28px}
.yb-foot .yb-brand img{width:56px;height:56px;border-radius:15px}
.yb-foot p{color:var(--foot2);margin:0}
.yb-foot a{color:var(--white);font-weight:700}
.yb-flinks{display:flex;flex-wrap:wrap;gap:8px 26px;font:700 18px/1.4 var(--ffd)}
.yb-foot .yb-legal-note{margin-top:34px;padding-top:24px;border-top:2px solid #2A3E4B;font-size:14px;line-height:1.6;color:var(--foot2)}

/* inner pages */
.yb-lband{background:linear-gradient(100deg,var(--lbandtop),var(--lband));color:var(--white);position:relative;overflow:hidden;padding-bottom:92px}
.yb-lband .yb-top{padding-bottom:10px}
.yb-crumb{font:700 16px/1.3 var(--ffd);margin:30px 0 0;color:var(--white);display:flex;flex-wrap:wrap;gap:8px 12px;align-items:center}
.yb-crumb a{color:var(--white)}
.yb-lband h1{font-size:clamp(38px,5vw,60px);margin-top:18px;color:var(--white)}
.yb-lband p.sub{font-size:20px;max-width:34em;margin:14px 0 0;color:var(--white)}
.yb-lband .yb-mascot{position:absolute;right:max(4%,calc(50% - 560px));bottom:-8px;width:130px;height:auto;filter:drop-shadow(0 10px 16px rgba(0,30,40,.4))}
.yb-lband.tall .yb-mascot{width:210px}
.yb-lgrid{display:grid;grid-template-columns:250px minmax(0,1fr);gap:48px;margin-top:-56px;padding-bottom:40px;align-items:start;position:relative;z-index:2}
.yb-toc{min-width:0;position:sticky;top:24px;background:var(--surface);border:2px solid var(--line);border-radius:24px;padding:22px 22px 20px;box-shadow:0 5px 0 var(--lip)}
.yb-toc h2{font-size:17px;margin:0 0 12px;color:var(--ink)}
.yb-toc ol{margin:0;padding:0;list-style:none;display:grid;gap:2px;font-size:15.5px;line-height:1.3;counter-reset:t}
.yb-toc li{counter-increment:t}
.yb-toc ol a{display:flex;gap:10px;padding:7px 10px;margin:0 -10px;border-radius:10px;text-decoration:none;color:var(--ink);font-weight:600}
.yb-toc.num ol a::before{content:counter(t,decimal-leading-zero);font:800 12.5px/1.6 var(--ffd);color:var(--ink2);flex:none;min-width:1.7em}
.yb-toc ol a:hover{background:var(--tint)}
.yb-toc .tools{margin-top:14px;padding-top:16px;border-top:2px solid var(--line);display:grid;gap:12px;justify-items:start}
.yb-toc .tools a{font-weight:800;font-size:15.5px}
.yb-toc .yb-btn{min-height:46px;font-size:16px;padding:11px 20px;border-radius:16px;color:var(--btnfg);text-decoration:none}
.yb-doc{background:var(--surface);border:2px solid var(--line);border-radius:32px;padding:56px clamp(24px,5vw,72px) 60px;box-shadow:0 6px 0 var(--lip),0 30px 60px var(--shadow);min-width:0}
.yb-doc>*{max-width:70ch}
.yb-doc h1{font-size:clamp(32px,3.6vw,46px);margin-bottom:10px}
.yb-doc .eyebrow{font:800 15px/1 var(--ffd);color:var(--link);margin:0 0 14px}
.yb-doc .effective{display:inline-block;background:var(--tint);color:var(--ink);font:700 15px/1.3 var(--ffd);padding:8px 14px;border-radius:999px;margin-bottom:24px}
.yb-doc h2{font-size:clamp(24px,2.4vw,31px);margin:2.1em 0 .6em;padding-top:1.1em;border-top:2px solid var(--line);scroll-margin-top:24px}
.yb-doc.num{counter-reset:s}
.yb-doc.num h2{counter-increment:s}
.yb-doc.num h2::before{content:counter(s,decimal-leading-zero);display:block;font:800 14px/1 var(--ffd);color:var(--link);margin-bottom:10px;letter-spacing:.02em}
.yb-doc .effective+p,.yb-doc h1+p{font-size:20px;line-height:1.55}
.yb-doc p,.yb-doc li{font-size:18px;line-height:1.7}
.yb-doc ul{padding-left:0;margin:0 0 1.2em;display:grid;gap:10px}
.yb-doc li{list-style:none;position:relative;padding-left:30px}
.yb-doc li::before{content:"";position:absolute;left:4px;top:.62em;width:12px;height:12px;border-radius:50%;background:var(--btn)}
.yb-doc strong{font-weight:700}
.yb-doc a{overflow-wrap:anywhere}
.yb-other{max-width:1180px;margin:0 auto;padding:0 0 10px;font:700 16px/1.4 var(--ffd);color:var(--ink2)}
.yb-sup{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;margin-top:-56px;padding-bottom:40px;position:relative;z-index:2}
.yb-sup>section{background:var(--surface);border:2px solid var(--line);border-radius:28px;padding:34px 34px 30px;box-shadow:0 6px 0 var(--lip),0 24px 48px var(--shadow)}
.yb-sup>section.wide{grid-column:1/-1;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:20px 40px;align-items:center}
.yb-sup h2{font-size:25px;margin-bottom:12px}
.yb-sup p{font-size:17.5px;color:var(--ink2);margin:0 0 12px}
.yb-sup p:last-child{margin-bottom:0}
.yb-sup strong{color:var(--ink)}
.yb-sup .path{display:inline-block;background:var(--tint);color:var(--ink);font:800 16px/1.3 var(--ffd);padding:8px 14px;border-radius:12px}

@media(max-width:1000px){
 .yb-two,.yb-two.skills,.yb-road{grid-template-columns:1fr;gap:44px}
 .yb-sec{padding:84px 0}
 .yb-grow{grid-template-columns:1fr;gap:48px}
 .yb-tgrid{grid-template-columns:repeat(2,1fr)}
 .yb-specs{grid-template-columns:repeat(2,1fr)}
 .yb-story,.yb-story.flip{grid-template-columns:1fr;min-height:0}
 .yb-story .art,.yb-story.flip .art{order:-1;min-height:300px}
 .yb-pair{grid-template-columns:1fr}
 .yb-streak{grid-template-columns:1fr}.yb-streak .yb-ph{display:none}
 .yb-lgrid{grid-template-columns:minmax(0,1fr);gap:24px;margin-top:-44px}
 .yb-toc{position:static}
}
@media(max-width:900px){
 .yb-hero{padding:112px 0 96px;min-height:0}
 .yb-hero-grid{grid-template-columns:1fr;gap:30px}
 .yb-hero .yb-scrim{background:@@SCRIM_MOBILE@@}
 .yb-hero-art{max-width:420px}
 .yb-bg{transform:none}
}
@media(max-width:640px){
 body{font-size:17px}
 .yb-wrap{width:min(1180px,100% - 36px)}
 .yb-top{padding:16px 0}
 .yb-brand{font-size:21px}.yb-brand img{width:38px;height:38px}
 .yb-top .yb-wrap{flex-wrap:wrap;row-gap:6px}
 .yb-nav{width:100%;justify-content:space-between;gap:0}
 .yb-nav a{padding:10px 8px;font-size:14.5px}
 .yb-hero{padding-top:148px}
 @media(max-width:380px){.yb-nav{flex-wrap:wrap;justify-content:center}.yb-nav a{padding:8px 6px;font-size:14px}}
 .yb-hero h1{font-size:clamp(36px,10.4vw,44px)}
 .yb-hero-art{aspect-ratio:1/1.18;max-width:340px}
 .yb-hero-art .l,.yb-hero-art .r{display:none}
 .yb-hero-art .c{left:11cqw;top:0;width:62cqw}
 .yb-hero-art .y{right:-2cqw;bottom:2cqw;width:40cqw}
 .yb-cta{flex-direction:column;align-items:stretch;gap:14px}
 .yb-cta .yb-btn,.yb-cta .yb-badge{width:100%;min-height:48px}
 .yb-cta .yb-badge{justify-content:center}
 .yb-bubbles{display:none}
 .yb-steps{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-inline:18px;gap:18px;padding:6px 18px 14px;margin:0 -18px}
 .yb-steps li{flex:0 0 60%;scroll-snap-align:start;margin-top:0!important}
 .yb-swipe{display:flex}
 .yb-sec{padding:56px 0}.yb-band{padding:72px 0 64px}.yb-grow{gap:36px}
 .yb-hero{padding-bottom:84px}.yb-road{margin-top:40px}
 .yb-tgrid{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-inline:18px;gap:14px;padding:6px 18px 14px;margin:32px -18px 0}
 .yb-tgrid li{flex:0 0 76%;scroll-snap-align:start}
 .yb-cards{display:none}
 .yb-tile.guides{display:none}
 .yb-specs{grid-template-columns:1fr 1fr;gap:18px 16px}.yb-specs dd{font-size:16px}.yb-specs dd small{font-size:14.5px}
 .yb-pair{margin-top:24px}
 .yb-stage-plate{border-radius:26px;aspect-ratio:2/1}
 .yb-story{border-radius:30px}
 .yb-story .art,.yb-story.flip .art{min-height:176px}
 .yb-story .copy{padding:30px 22px 34px}
 .yb-bub{left:auto;right:10%;top:12%}
 .yb-tile{padding:26px 22px 24px;border-radius:26px}
 .yb-week{gap:4px;padding:18px 8px 14px}
 .yb-close{grid-template-columns:1fr;gap:18px;text-align:center;border-radius:30px;padding:28px 20px}
 .yb-close img{max-width:104px;margin:0 auto}
 .yb-close .yb-badge{justify-content:center;width:100%}
 .yb-foot{margin-top:56px}.yb-foot-art{height:120px}.yb-foot-panel{padding:34px 0 32px}
 .yb-gate{margin-top:40px}
 .yb-lband{padding-bottom:70px}.yb-lband .yb-mascot,.yb-lband.tall .yb-mascot{width:96px;right:12px}
 .yb-doc{padding:34px 20px 40px;border-radius:26px}
 .yb-toc{padding:16px 16px 14px}
 .yb-toc ol{display:flex;overflow-x:auto;gap:8px;padding:2px 2px 10px;scroll-snap-type:x proximity}
 .yb-toc ol a{border:2px solid var(--line);white-space:nowrap;padding:8px 14px;margin:0;border-radius:999px;font-size:15px;scroll-snap-align:start}
 .yb-toc.num ol a::before{display:none}
 .yb-toc .tools{display:flex;flex-wrap:wrap;gap:10px 18px;align-items:center;margin-top:6px;padding-top:12px}
 .yb-sup{grid-template-columns:1fr}.yb-sup>section.wide{grid-template-columns:1fr}
 .yb-sup>section{padding:26px 22px 24px}
 .yb-cards li{min-width:0}
}
'''


# ---------------------------------------------------------------------------------------------------------------------
# Building blocks
# ---------------------------------------------------------------------------------------------------------------------
def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


STAR = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.6l2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.4l-5.9 3.2 1.2-6.5L2.5 9.5l6.6-.9z" '
        'fill="#FFC107" stroke="#D99A00" stroke-width="1.4" stroke-linejoin="round"/></svg>')
NO = ('<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.6" fill="none" stroke="#1E2640" stroke-width="2.6"/>'
      '<path d="M6 18L18 6" stroke="#1E2640" stroke-width="2.6" stroke-linecap="round"/></svg>')
ICONS = {
    'phone': '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="6" y="3" width="12" height="18" rx="3"/><path d="M10 18h4"/></svg>',
    'lock': '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="11" width="14" height="9" rx="2.5"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>',
    'mic': '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5.5 11a6.5 6.5 0 0 0 13 0M12 17.5V21"/></svg>',
    'report': '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="3" width="14" height="18" rx="3"/><path d="M9 8h6M9 12h6M9 16h3"/></svg>',
    'book': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5C7 4.5 10 4.8 12 6.5c2-1.7 5-2 8-1v13c-3-1-6-.7-8 1-2-1.7-5-2-8-1z"/><path d="M12 6.5V19.5"/></svg>',
    'heart': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 20s-7.5-4.4-7.5-10A4.3 4.3 0 0 1 12 7.6 4.3 4.3 0 0 1 19.5 10c0 5.6-7.5 10-7.5 10z"/></svg>',
    'people': '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="9" cy="8.5" r="3"/><path d="M3.5 19c.4-3.2 2.6-5 5.5-5s5.1 1.8 5.5 5"/><circle cx="17" cy="9.5" r="2.4"/><path d="M16.5 14.2c2.4-.2 3.9 1.2 4.3 3.8"/></svg>',
    'card': '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="6" width="18" height="12" rx="3"/><path d="M3 10.5h18"/></svg>',
}
WAVE = ('<svg class="yb-wave {c}" viewBox="0 0 1440 90" preserveAspectRatio="none" aria-hidden="true"><path d="M0 50 C 180 100 360 0 600 40 '
        'C 840 80 1020 10 1200 44 C 1320 66 1390 60 1440 48 L1440 90 L0 90 Z"/></svg>')


def phone(root, name, alt, w=None, cls='', lazy=True, dark=None, prio=False):
    style = f' style="--w:{w}"' if w else ''
    load = ' fetchpriority="high"' if prio else (' loading="lazy" decoding="async"' if lazy else '')
    img = f'<img src="{root}media/{name}" width="640" height="1387" alt="{esc(alt)}"{load}>'
    if dark:
        img = f'<picture><source media="(prefers-color-scheme: dark)" srcset="{root}media/{dark}">{img}</picture>'
    return f'<div class="yb-ph {cls}"{style}><div class="yb-ph-body">{img}</div></div>'


def pad(root, name, alt, cls='', lazy=True):
    load = ' loading="lazy" decoding="async"' if lazy else ''
    return (f'<div class="yb-pad {cls}"><div class="yb-pad-body"><img src="{root}media/{name}" width="1400" height="973" '
            f'alt="{esc(alt)}"{load}></div></div>')


def plate(root, name, cls='plate', eager=False):
    load = '' if eager else ' loading="lazy" decoding="async"'
    return f'<img class="{cls}" src="{root}media/{name}" width="1152" height="768" alt=""{load}>'


STR = {
    'en': dict(
        lang='en', home='Yaybo home', skip='Skip to content', privacy='Privacy', terms='Terms', support='Support', adults='For grown-ups',
        day='A day', skills='Skills', toc='On this page', write='Write to us', other='Read this in Spanish', otherlabel='Español',
        tag='A learning app for children, used with a grown-up.', where='For iPhone and iPad · iOS 26 or later · United States and Canada',
        legal='Legal', main='Main', foot='Footer'),
    'es': dict(
        lang='es', home='Inicio', skip='Saltar al contenido', privacy='Privacidad', terms='Condiciones', support='Soporte', adults='Para adultos',
        day='Un día', skills='Aprendizaje', toc='En esta página', write='Escríbenos', other='Read this in English', otherlabel='English',
        tag='Una app de aprendizaje para niños, que se usa con una persona adulta.',
        where='Para iPhone y iPad · iOS 26 o posterior · Estados Unidos y Canadá', legal='Legal', main='Principal', foot='Pie de página'),
}
# Directory (relative to yaybo/) of each page.
DIRS = {('en', 'home'): '', ('en', 'privacy'): 'privacy', ('en', 'terms'): 'terms', ('en', 'support'): 'support',
        ('es', 'privacy'): 'privacidad', ('es', 'terms'): 'condiciones', ('es', 'support'): 'soporte'}


def root_of(d):
    return '../' if d else ''


def link(frm, to, anchor=''):
    if frm == to:
        r = './'
    elif to == '':
        r = '../'
    elif frm == '':
        r = to + '/'
    else:
        r = '../' + to + '/'
    return r + anchor


def header(lang, here_dir, key, home=False, onband=True):
    s = STR[lang]
    root = root_of(here_dir)
    hl = lambda k: link(here_dir, DIRS[(lang, k)])
    cur = lambda k: ' aria-current="page"' if key == k else ''
    brand = f'<a class="yb-brand" href="{link(here_dir, "")}"><img src="{root}media/icon-512.png" width="44" height="44" alt="">Yaybo</a>'
    if home:
        items = (f'<a class="opt" href="#adventure">{s["day"]}</a><a class="opt" href="#skills">{s["skills"]}</a>'
                 f'<a class="opt" href="#grown-ups">{s["adults"]}</a><a href="{hl("privacy")}">{s["privacy"]}</a><a href="{hl("support")}">{s["support"]}</a>')
    else:
        items = (f'<a class="opt" href="{link(here_dir, "")}#grown-ups">{s["adults"]}</a><a href="{hl("privacy")}"{cur("privacy")}>{s["privacy"]}</a>'
                 f'<a class="opt" href="{hl("terms")}"{cur("terms")}>{s["terms"]}</a><a href="{hl("support")}"{cur("support")}>{s["support"]}</a>')
    return (f'<header class="yb-top{" abs" if home else ""}"><div class="yb-wrap">{brand}'
            f'<nav class="yb-nav" aria-label="{s["main"]}">{items}</nav></div></header>')


def footer(lang, here_dir, home=False):
    s = STR[lang]
    root = root_of(here_dir)
    hl = lambda k: link(here_dir, DIRS[(lang, k)])
    disclaimer = ''
    if home:
        disclaimer = ('<p class="yb-legal-note">Common Core State Standards: &copy; Copyright 2010. National Governors Association Center for Best Practices '
                      'and Council of Chief State School Officers. All rights reserved. TEKS belong to the Texas Education Agency and B.E.S.T. to the Florida '
                      'Department of Education. Yaybo is not endorsed by, or affiliated with, the NGA Center, CCSSO, TEA or FLDOE.</p>')
    return (f'<footer class="yb-foot"><div class="yb-foot-art">{plate(root, "turtles-moon.jpg", "", False)}{WAVE.format(c="t")}</div>'
            f'<div class="yb-foot-panel"><div class="yb-wrap"><div class="yb-foot-grid">'
            f'<div><a class="yb-brand" href="{link(here_dir, "")}"><img src="{root}media/icon-512.png" width="56" height="56" alt="">Yaybo</a>'
            f'<p style="margin:16px 0 0;max-width:26em">{s["tag"]}</p></div>'
            f'<div><nav class="yb-flinks" aria-label="{s["foot"]}"><a href="{hl("privacy")}">{s["privacy"]}</a><a href="{hl("terms")}">{s["terms"]}</a>'
            f'<a href="{hl("support")}">{s["support"]}</a><a href="mailto:{MAIL}">{MAIL}</a></nav>'
            f'<p style="margin:16px 0 0;font-size:15.5px">{s["where"]}</p></div></div>{disclaimer}</div></div></footer>')


def head(lang, here_dir, title, desc, alts=None, og_image='axolotl-smile.jpg'):
    root = root_of(here_dir)
    canon = SITE + (here_dir + '/' if here_dir else '')
    alt = ''
    for L, d in (alts or {}).items():
        alt += f'<link rel="alternate" hreflang="{L}" href="{SITE}{d}/">'
    return (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="color-scheme" content="light dark"><meta name="theme-color" content="#06505E">'
            f'<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">'
            f'<link rel="canonical" href="{canon}">{alt}'
            f'<meta property="og:type" content="website"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">'
            f'<meta property="og:url" content="{canon}"><meta property="og:image" content="{SITE}media/{og_image}">'
            f'<link rel="icon" type="image/png" sizes="32x32" href="{root}media/favicon-32.png"><link rel="apple-touch-icon" href="{root}media/apple-touch-icon.png">'
            f'<style>{build_css()}</style></head><body>')


def page_shell(lang, here_dir, key, title, desc, body, home=False, alts=None, disclaimer=False):
    s = STR[lang]
    return (head(lang, here_dir, title, desc, alts) + f'<a class="yb-skip" href="#main">{s["skip"]}</a>' + body + '</body></html>')


# ---------------------------------------------------------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------------------------------------------------------
def home_page():
    r = ''
    p = lambda *a, **k: phone(r, *a, **k)
    bubbles = ''.join(f'<span style="left:{x}%;width:{w}px;height:{w}px;animation-duration:{d}s;animation-delay:-{dl}s"></span>'
                      for x, w, d, dl in ((56, 18, 16, 2), (63, 30, 22, 9), (71, 14, 14, 5), (78, 24, 19, 12), (86, 16, 17, 3), (93, 34, 24, 15), (50, 20, 20, 7)))
    hero = f'''<section class="yb-hero yb-onhero" aria-labelledby="h1">
<img class="yb-bg" src="media/axolotl-reef.jpg" width="1152" height="768" alt="" fetchpriority="high">
<div class="yb-scrim"></div><div class="yb-bubbles" aria-hidden="true">{bubbles}</div>
{header('en', '', 'home', home=True)}
<div class="yb-wrap yb-hero-grid"><div class="yb-hero-copy">
<p class="yb-eyebrow">A learning app for ages 4 to 9</p>
<h1 id="h1">About ten minutes a day. Three stops. <em>Then it ends.</em></h1>
<p class="yb-lede">Reading and math first, with phonics, spelling, money, time and handwriting alongside: a daily plan for your family, Pre-K to 3rd grade, built on the grade-level expectations most U.S. states share. Yaybo the axolotl cheers every right answer.</p>
<div class="yb-cta"><p class="yb-badge">{STAR}<span><small>Not on sale yet</small><b>Coming soon to the App Store</b></span></p>
<a class="yb-btn yb-btn-sun" href="#adventure">See how a day works</a></div>
<p class="yb-fine">For iPhone and iPad &middot; iOS 26 or later &middot; United States and Canada</p></div>
<div class="yb-hero-art">
<div class="yb-float l">{p("ui-island.webp", "Yaybo's island seen from above: a green island in a pond with a bee, flowers and a bottom bar of Garden, Friends, Fridge and Wardrobe", w="100%", lazy=False)}</div>
<div class="yb-float r">{p("ui-book.webp", "Tad's book page: a picture of children and friends at the shore, the story text, and a Next page button", w="100%", lazy=False)}</div>
<div class="yb-float c">{p("ui-home.webp", "Yaybo's home screen: Hi, Maya! with Yaybo the axolotl and Tad the turtle, Today's Adventure with a Start Adventure button, and tiles for Road trip and My Island", w="100%", lazy=False, prio=True)}</div>
<img class="yb-float y" src="media/yaybo-wave.png" width="643" height="569" alt="Yaybo the axolotl, waving">
</div></div>{WAVE.format(c="b")}</section>'''

    adventure = f'''<section class="yb-sec" id="adventure" aria-labelledby="h-adv"><div class="yb-wrap yb-two">
<div><p class="yb-kicker"><i></i>How a day works</p><h2 id="h-adv">One Adventure a day, with a clear end</h2>
<p class="big">Your child gets one short Adventure a day: three short lessons that pick up where they left off. Three stops and about ten minutes, then a clear end.</p>
<ul class="yb-facts"><li>You set it up in about six minutes.</li><li>Instructions are spoken aloud, so early learners do not need to read.</li><li>You get a plain-English report each week.</li></ul></div>
<ol class="yb-steps" tabindex="0" aria-label="A day in Yaybo, in three steps">
<li>{p("ui-road.webp", "Today's Adventure: a path of three stops, Small letters, Count to 5 and You pick, with a Let's go! button", w="100%")}<p class="yb-cap"><b>1</b>See today's stops</p></li>
<li>{p("ui-counting.webp", "A counting lesson: Tap 2 apples, with five apples to tap, a Check button and Yaybo's voice", w="100%")}<p class="yb-cap"><b>2</b>Play a short lesson</p></li>
<li>{p("ui-celebration.webp", "Stop complete! Yay! Three stars, a handful of leaves and a Continue button, with Yaybo cheering under a sun", w="100%")}<p class="yb-cap"><b>3</b>A clear end</p></li>
</ol><p class="yb-swipe" aria-hidden="true"><span>Swipe to see more</span><svg viewBox="0 0 24 24"><path d="M5 12h13m-5-5.5 5.5 5.5-5.5 5.5" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></p></div></section>'''

    chips = ''.join(f'<li><i style="background:{c}"></i>{t}</li>' for c, t in (
        ('#2D7FF9', 'Math, Pre-K to 3rd grade'), ('#F23D7A', 'Phonics and reading'), ('#F23D7A', 'Spelling, 1st to 3rd grade'),
        ('#FFC107', 'Money and time'), ('#FF8A1F', 'Handwriting')))
    skills = f'''<section class="yb-sec" id="skills" aria-labelledby="h-skills" style="padding-top:40px"><div class="yb-wrap yb-two skills">
<div><p class="yb-kicker"><i></i>Reading and math, Pre-K to 3rd grade</p><h2 id="h-skills">Real school skills, step by step</h2>
<p class="big">Counting and number sense, stories read page by page, letters and sounds. Skills carry standards codes that line up with school in the United States and Canada: Common Core, plus Texas TEKS in Texas and Florida B.E.S.T. in Florida.</p>
<ul class="yb-chips">{chips}</ul>
<p class="yb-sub" style="margin-top:24px">Type this week's spelling list and your child practices it in the Adventure. Trace letters, numbers and your child's name with a finger or Apple Pencil, in print, slanted print or cursive.</p></div>
<div class="yb-stage">{plate(r, "story-time.jpg", "yb-stage-plate")}
<div class="yb-fan">{p("ui-counting.webp", "A counting lesson: Tap 2 apples, with five apples to tap and a Check button", cls="a")}{p("ui-book.webp", "Read the page: Tad's book with a picture of friends at the shore and the story in large type", cls="c")}</div></div>
</div></section>'''

    nos = ''.join(f'<li>{NO}{t}</li>' for t in ('No buzzers', 'No lost hearts', 'No leaderboards'))
    week = ''.join(f'<span><i class="{c}"></i>{d}</span>' for c, d in (('on', 'M'), ('on', 'T'), ('on', 'W'), ('rest', 'T'), ('on', 'F'), ('on', 'S'), ('off', 'S')))
    yay = f'''<section class="yb-sec" id="yay" aria-labelledby="h-yay" style="padding-top:40px"><div class="yb-wrap">
<div class="yb-story teal"><div class="copy"><p class="yb-kicker"><i></i>Gentle, never loud</p><h2 id="h-yay">Every right answer gets a Yay</h2>
<p class="lede">Yaybo the axolotl cheers every right answer and helps gently after a miss. Tad the turtle brings stories and silly skits.</p>
<ul class="yb-no">{nos}</ul></div>
<div class="art">{plate(r, "axolotl-smile.jpg")}<div class="yb-bub" aria-hidden="true">Yay!</div></div></div>
<div class="yb-pair"><div class="yb-tile"><div class="yb-streak"><div><h3>A forgiving Sunny Streak</h3>
<p>Rest days you choose. The stars, friends, clothes and postcards your child has earned are never taken away.</p>
<div class="yb-week" role="img" aria-label="An example week of the Sunny Streak: five sunny days and one rest day you chose">{week}</div>
<ul class="yb-legend" aria-hidden="true"><li><i class="on"></i>A sunny day</li><li><i class="rest"></i>A rest day you chose</li></ul></div>
{p("ui-celebration.webp", "Stop complete! Yay! Three stars, a handful of leaves and a Continue button, with Yaybo cheering under a sun", w="100%")}</div></div>
<div class="yb-tile guides yb-guides"><h3>Meet Yaybo and Tad</h3><div class="yb-meet">
<figure><div class="m"><img src="media/yaybo-idle.png" width="655" height="561" alt="" loading="lazy"></div><figcaption><b>Yaybo</b>the axolotl, cheering every right answer</figcaption></figure>
<figure><div class="m tad"><img src="media/tad.png" width="480" height="480" alt="" loading="lazy"></div><figcaption><b>Tad</b>the turtle, with stories and silly skits</figcaption></figure></div></div></div>
</div></section>'''

    friends = ''.join(f'<li><img src="media/critter-{n}.png" width="240" height="240" alt="" loading="lazy"></li>' for n in ('bee', 'fox', 'otter', 'penguin', 'koala'))
    cards = ''.join(f'<li><img src="media/{n}.jpg" width="560" height="373" alt="{esc(a)}" loading="lazy"></li>' for n, a in (
        ('pc-california', 'Postcard art: tall redwood trees'), ('pc-hawaii', 'Postcard art: a turtle swimming near a volcano'),
        ('pc-vermont', 'Postcard art: a maple syrup stand under an autumn tree'), ('pc-new-mexico', 'Postcard art: hot-air balloons over a mesa')))
    progress = f'''<section class="yb-sec sunk" id="progress" aria-labelledby="h-prog"><div class="yb-wrap">
<div class="yb-story navy flip"><div class="copy"><p class="yb-kicker"><i></i>Progress you can see</p><h2 id="h-prog">An island that grows, and a road trip across the U.S.</h2>
<p class="lede">Mastered skills fill an island with new friends. A road trip across the U.S. collects a postcard and a fun fact from each state.</p></div>
<div class="art">{plate(r, "yellow-van.jpg")}</div></div>
<div class="yb-road"><div class="yb-device"><div class="yb-pad"><div class="yb-pad-body"><img src="media/pad-home.webp" width="1400" height="973" alt="Yaybo's home on iPad, in landscape: Yaybo and Tad by the pond, Today's Adventure with a Start Adventure button, and tiles for Road trip, My Island, Quests, Wardrobe and Chest" loading="lazy" decoding="async"></div></div>
{p("ui-island.webp", "Yaybo's island from above: a green island in a pond with a bee, flowers and a bottom bar of Garden, Friends, Fridge and Wardrobe", cls="p1")}</div>
<div><h3 style="font-size:26px;margin-bottom:10px">Friends for the island, postcards for the road</h3><p class="yb-sub" style="margin:0">Works on iPhone and iPad.</p>
<ul class="yb-friends" aria-label="Some of the island friends">{friends}</ul><ul class="yb-cards" aria-label="Postcards from the road trip">{cards}</ul></div></div>
</div></section>'''

    pts = ''.join(f'<li><span class="yb-ico">{ICONS[i]}</span><h3>{h}</h3><p>{t}</p></li>' for i, h, t in (
        ('report', 'The weekly report', 'What is mastered, what is tricky, and a simple activity to do together.'),
        ('book', 'How they teach it', 'Short explainers for how school teaches each skill.'),
        ('heart', 'High-fives', 'Send your child a sticker and a note.'),
        ('people', 'Up to four children', 'On one subscription, with Family Sharing.')))
    grown = f'''<section class="yb-band yb-dark" id="grown-ups" aria-labelledby="h-grown"><div class="yb-wrap yb-grow">
<div><p class="yb-kicker"><i></i>For grown-ups</p><h2 id="h-grown">A weekly report in plain English</h2>
<p class="big">What is mastered, what is tricky, and one thing to try together. Optional Read-aloud lets your child read a word or a page out loud.</p>
<ul class="yb-pts" aria-label="What grown-ups get in the Parent Zone">{pts}</ul>
<p class="yb-gate">{ICONS["lock"]}<span>Everything for adults sits behind a parental gate, with an optional PIN.</span></p></div>
<div class="yb-grow-art">{p("ui-report.webp", "The weekly report in the Parent Zone: Maya's week with four checked days, 11 stops finished, 18 minutes and 4 days, then an At a glance list of what she is working on, what to try again and what comes next", w="100%")}</div>
</div></section>'''

    tcards = ''.join(f'<li><span class="yb-ico">{ICONS[i]}</span><h3>{h}</h3><p>{t}</p></li>' for i, h, t in (
        ('phone', 'It stays on your devices', "Your child's name and answers stay on your devices, and in your own iCloud if Sync is on."),
        ('lock', 'A parental gate', 'Everything for adults sits behind it, with an optional PIN.'),
        ('mic', 'Read-aloud is optional', 'Your device listens only while a button is held and never records, stores or sends the sound.'),
        ('card', 'Apple handles payments', "If a grown-up buys or restores a subscription, the purchase-analytics partner sees the purchase and your device's technical details, never anything about your child.")))
    trust = f'''<section class="yb-sec" id="privacy" aria-labelledby="h-trust"><div class="yb-wrap">
<div class="yb-story teal flip"><div class="copy"><p class="yb-kicker"><i></i>Privacy</p><h2 id="h-trust">No ads. No account. No tracking.</h2>
<p class="lede">Your child's name and answers stay on your devices, and in your own iCloud if Sync is on. Nothing else to buy.</p>
<a class="yb-btn yb-btn-sun" href="privacy/">Read the privacy policy</a></div><div class="art">{plate(r, "sunset-pond.jpg")}</div></div>
<ul class="yb-tgrid" tabindex="0" aria-label="How Yaybo protects your family">{tcards}</ul><p class="yb-swipe" aria-hidden="true"><span>Swipe to see more</span><svg viewBox="0 0 24 24"><path d="M5 12h13m-5-5.5 5.5 5.5-5.5 5.5" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></p>
<div style="max-width:1180px;margin:72px auto 0"><dl class="yb-specs">
<div><dt>Ages</dt><dd>4 to 9, Pre-K to 3rd grade</dd></div><div><dt>Devices</dt><dd>iPhone and iPad, iOS 26 or later</dd></div>
<div><dt>Available in</dt><dd>The United States and Canada</dd></div>
<div><dt>Yaybo Plus</dt><dd>A subscription<small>One plan covers up to four children and works with Family Sharing. Plans and the trial are shown in the app and on the App Store.</small></dd></div></dl></div>
<div style="margin-top:72px"><div class="yb-close"><img src="media/yaybo-wave.png" width="643" height="569" alt="Yaybo the axolotl, waving" loading="lazy">
<div><h2>Yaybo is coming soon.</h2><p>A daily plan your family can finish in about ten minutes, with a clear end.</p>
<p class="yb-badge">{STAR}<span><small>Not on sale yet</small><b>Coming soon to the App Store</b></span></p></div></div></div>
</div></section>'''

    body = f'<main id="main">{hero}{adventure}{skills}{yay}{progress}{grown}{trust}</main>' + footer('en', '', home=True)
    title = 'Yaybo: a daily learning plan for your family'
    desc = ('A daily learning plan for ages 4 to 9: phonics, reading, spelling, math, money, time and handwriting. About ten minutes a day, '
            'a plain-English report each week, no ads, no account, no tracking.')
    return page_shell('en', '', 'home', title, desc, body, home=True)


# ---------------------------------------------------------------------------------------------------------------------
# Support
# ---------------------------------------------------------------------------------------------------------------------
SUPPORT = {
    'en': dict(
        title='Yaybo support', desc='Contact Yaybo, manage or cancel a subscription, restore a purchase, or delete what Yaybo keeps.',
        h1='Yaybo support', sub='Questions about Yaybo, a subscription or your family’s data? Start here.',
        write=('Write to us', f'<p>Write to <a href="mailto:{MAIL}">{MAIL}</a>. Please leave your child’s name and details out of the email.</p>', 'Write to us'),
        manage=('Manage or cancel your subscription',
                '<p>Manage or cancel anytime in <span class="path">Settings › [your name] › Subscriptions</span> on your device.</p>'
                '<p>A subscription renews automatically unless you cancel at least 24 hours before the end of the current period. Cancelling stops the next renewal; you keep access until the end of the period you already paid for. Deleting the app does not cancel it.</p>'
                '<p>Apple handles payments and refunds, under the App Store’s refund policy: <a href="https://reportaproblem.apple.com/">reportaproblem.apple.com</a>.</p>'),
        restore=('Restore a purchase', '<p>“Restore” on the plan screen brings back a subscription you already own, on a new device or after reinstalling.</p>'
                 '<p>One Yaybo Plus subscription covers up to four children and works with Family Sharing.</p>'),
        delete=('Delete what Yaybo keeps', '<p>In the Parent Zone, behind the grown-up gate, you can review and delete everything Yaybo keeps: “Delete…” on a child, or “Delete all data”.</p>'
                '<p>Deleting your data does not cancel a subscription: that is in Settings › [your name] › Subscriptions.</p>'),
        read=('Read the details', '<p>How Yaybo handles your family’s information, and the terms of the Yaybo Plus subscription.</p>', 'Privacy policy', 'Terms of use')),
    'es': dict(
        title='Soporte de Yaybo', desc='Contacta con Yaybo, gestiona o cancela una suscripción, restaura una compra o borra lo que guarda Yaybo.',
        h1='Soporte de Yaybo', sub='¿Dudas sobre Yaybo, una suscripción o los datos de tu familia? Empieza aquí.',
        write=('Escríbenos', f'<p>Escribe a <a href="mailto:{MAIL}">{MAIL}</a>. Por favor, no pongas en el correo el nombre ni los datos de tu hijo o hija.</p>', 'Escríbenos'),
        manage=('Gestionar o cancelar la suscripción',
                '<p>Gestiónala o cancélala cuando quieras en <span class="path">Ajustes › [tu nombre] › Suscripciones</span> de tu dispositivo.</p>'
                '<p>La suscripción se renueva automáticamente salvo que la canceles al menos 24 horas antes de que termine el periodo en curso. Cancelar detiene la siguiente renovación; conservas el acceso hasta el final del periodo ya pagado. Borrar la app no la cancela.</p>'
                '<p>Apple gestiona los pagos y los reembolsos, según su política de reembolsos de la App Store: <a href="https://reportaproblem.apple.com/">reportaproblem.apple.com</a>.</p>'),
        restore=('Restaurar una compra', '<p>«Restaurar» en la pantalla del plan recupera una suscripción que ya tienes, en un dispositivo nuevo o tras reinstalar.</p>'
                 '<p>Una suscripción Yaybo Plus cubre hasta cuatro niños y funciona con Compartir en familia.</p>'),
        delete=('Borrar lo que guarda Yaybo', '<p>En la Zona para padres, tras la puerta para adultos, puedes revisar y borrar todo lo que guarda Yaybo: «Eliminar…» en un niño, o «Eliminar todos los datos».</p>'
                '<p>Borrar tus datos no cancela una suscripción: eso está en Ajustes › [tu nombre] › Suscripciones.</p>'),
        read=('Los detalles', '<p>Cómo trata Yaybo la información de tu familia, y las condiciones de la suscripción Yaybo Plus.</p>', 'Política de privacidad', 'Condiciones de uso')),
}


def band(lang, d, key, crumb, h1=None, sub=None):
    s = STR[lang]
    head1 = f'<h1>{h1}</h1><p class="sub">{sub}</p>' if h1 else ''
    return (f'<div class="yb-lband yb-onhero{" tall" if h1 else ""}">{header(lang, d, key)}<div class="yb-wrap">'
            f'<p class="yb-crumb"><a href="{link(d, "")}">\u2039 {s["home"]}</a><span aria-hidden="true">/</span><span>{crumb}</span></p>{head1}</div>'
            f'<img class="yb-mascot" src="{root_of(d)}media/yaybo-wave.png" width="643" height="569" alt=""></div>')


def support_page(lang):
    S = SUPPORT[lang]
    d = DIRS[(lang, 'support')]
    s = STR[lang]
    root = root_of(d)
    other = 'es' if lang == 'en' else 'en'
    cards = (f'<section class="wide"><div><h2>{S["write"][0]}</h2>{S["write"][1]}</div>'
             f'<a class="yb-btn yb-btn-teal" href="mailto:{MAIL}">{S["write"][2]}</a></section>'
             f'<section><h2>{S["manage"][0]}</h2>{S["manage"][1]}</section>'
             f'<section><h2>{S["restore"][0]}</h2>{S["restore"][1]}</section>'
             f'<section><h2>{S["delete"][0]}</h2>{S["delete"][1]}</section>'
             f'<section><h2>{S["read"][0]}</h2>{S["read"][1]}<p><a href="{link(d, DIRS[(lang, "privacy")])}">{S["read"][2]}</a> &middot; '
             f'<a href="{link(d, DIRS[(lang, "terms")])}">{S["read"][3]}</a></p></section>')
    body = (band(lang, d, 'support', STR[lang]['support'], S['h1'], S['sub']) + f'<div class="yb-wrap"><main id="main" class="yb-sup">{cards}</main></div>' + footer(lang, d))
    alts = {'en': DIRS[('en', 'support')], 'es': DIRS[('es', 'support')]}
    return page_shell(lang, d, 'support', S['title'], S['desc'], body, alts=alts)


# ---------------------------------------------------------------------------------------------------------------------
# Legal pages
# ---------------------------------------------------------------------------------------------------------------------
def legal_page(lang, kind, text, title, desc, alts):
    s = STR[lang]
    d = DIRS[(lang, kind)]
    heads = re.findall(r'<h2>(.*?)</h2>', text, flags=re.S)
    n = [0]

    def idify(m):
        n[0] += 1
        return f'<h2 id="s{n[0]}">'
    doc = re.sub(r'<h2>', idify, text)
    numbered = kind == 'privacy'
    toc = ''.join(f'<li><a href="#s{i + 1}">{h}</a></li>' for i, h in enumerate(heads))
    oth_lang = 'es' if lang == 'en' else 'en'
    oth_dir = DIRS[(oth_lang, kind)]
    nav = (f'<nav class="yb-toc{" num" if numbered else ""}" aria-label="{s["toc"]}"><h2>{s["toc"]}</h2><ol>{toc}</ol>'
           f'<div class="tools"><a class="back" href="{link(d, "")}">‹ {s["home"]}</a>'
           f'<a href="{link(d, oth_dir)}" hreflang="{oth_lang}" lang="{oth_lang}">{STR[lang]["otherlabel"]}</a>'
           f'<a class="yb-btn yb-btn-teal" href="mailto:{MAIL}">{s["write"]}</a></div></nav>')
    kindlabel = s['privacy'] if kind == 'privacy' else s['terms']
    body = (band(lang, d, kind, kindlabel) +
            f'<div class="yb-wrap yb-lgrid">{nav}<main id="main" class="yb-doc{" num" if numbered else ""}">{doc}</main></div>' + footer(lang, d))
    return page_shell(lang, d, kind, title, desc, body, alts=alts)


# ---------------------------------------------------------------------------------------------------------------------
# Audit and build
# ---------------------------------------------------------------------------------------------------------------------
ALLOWED_HTTPS = ('https://www.apple.com/legal/', 'https://reportaproblem.apple.com/', 'https://apps.apple.com/legal')
FORBIDDEN = [r'<script', r'<iframe', r'rel="stylesheet"', r'@import', r'fonts\.googleapis', r'fonts\.gstatic', r'cdn\.', r'apps\.apple\.com/(?!legal)',
             r'googletagmanager', r'<form', r'<embed', r'<object']


def isolation_rows(html, path, built=None):
    """Every link/src in the page stays inside yaybo/ (or is one of the allowed vendors); nothing external is loaded."""
    rows, ok = [], True
    here = posixpath.dirname(path)
    bad = []
    body = re.sub(r'<style>.*?</style>', '', html, flags=re.S)
    for m in re.finditer(r'(?:href|src|srcset|content)="([^"]*)"', body):
        v = m.group(1)
        if v.startswith(('#', 'mailto:' + MAIL)) or not v:
            continue
        if v.startswith(('http://', 'https://', '//')):
            if v.startswith(SITE) or v == SITE.rstrip('/'):
                if 'content=' in m.group(0)[:8]:
                    continue
                if m.group(0).startswith(('href', 'src')) and not re.search(r'rel="(canonical|alternate)"', html[max(0, m.start() - 120):m.start()]):
                    bad.append(v)
                continue
            if any(v.startswith(a) for a in ALLOWED_HTTPS):
                continue
            bad.append(v)
            continue
        if m.group(0).startswith('content=') or v.startswith(('mailto:', 'tel:')):
            if v.startswith(('mailto:', 'tel:')) and v != 'mailto:' + MAIL:
                bad.append(v)
            continue
        for part in v.split(','):
            u = part.strip().split(' ')[0].split('#')[0].split('?')[0]
            if not u:
                continue
            tgt = posixpath.normpath(posixpath.join(here, u))
            if not (tgt == '.' or tgt.startswith('yaybo') or tgt == 'yaybo') or tgt.startswith('..'):
                bad.append(v)
                continue
            f = ROOT / tgt
            if tgt in ('yaybo',) or u.endswith('/'):
                f = ROOT / tgt / 'index.html' if tgt != 'yaybo' else ROOT / 'yaybo' / 'index.html'
            exists = f.exists() or bool(built and ((tgt + '/index.html') in built or tgt in built))
            if not exists:
                bad.append(v + ' (missing)')
    rows.append((f'isolation {path}: only own pages, own media, mailto, Apple legal', len(bad), 0, not bad))
    for b in bad:
        rows.append((f'  offending reference: {b}', 0, 0, False))
    ok &= not bad
    hits = [pat for pat in FORBIDDEN if re.search(pat, body, flags=re.I)]
    rows.append((f'isolation {path}: no script, font CDN, iframe, form or store link', len(hits), 0, not hits))
    ok &= not hits
    if re.search(r'Kids Category', html, flags=re.I):
        rows.append((f'{path}: mentions the Kids Category', 1, 0, False))
        ok = False
    return rows, ok


def image_rows(html, path):
    bad = []
    for m in re.finditer(r'<img\b[^>]*>', html):
        t = m.group(0)
        if ' alt=' not in t:
            bad.append('no alt: ' + t[:80])
        if ' width=' not in t or ' height=' not in t:
            bad.append('no width/height: ' + t[:80])
    return [(f'images {path}: alt, width and height on every <img>', len(bad), 0, not bad)] + [(f'  {b}', 0, 0, False) for b in bad], not bad


KNOWN_DIRS = set(d for d in DIRS.values() if d) | {'yaybo'}
_CONTRAST_CACHE = []


def audit(html, path='yaybo/index.html', built=None):
    """(rows, ok): the contrast of every text/background pair of the CSS in light and dark (once per build), the composited hero,
    and this page's isolation and image attributes. A row is (label, value, minimum, passed)."""
    if not _CONTRAST_CACHE:
        r1, o1 = contrast_rows()
        r2, o2 = hero_rows()
        _CONTRAST_CACHE.append((r1 + r2, o1 and o2))
    rows, ok = list(_CONTRAST_CACHE[0][0]), _CONTRAST_CACHE[0][1]
    r, o = isolation_rows(html, path, built)
    rows, ok = rows + r, ok and o
    r, o = image_rows(html, path)
    rows, ok = rows + r, ok and o
    return rows, ok


def unused_media(pages):
    used = set()
    for h in pages.values():
        used |= set(re.findall(r'media/([\w.\-]+)', h))
    return sorted(p.name for p in (YB / 'media').iterdir() if p.is_file() and p.name not in used)


def build_pages(PRIVACY, TERMS, PAGES, fill, write=True, verbose=True):
    pages = {'yaybo/index.html': home_page(), 'yaybo/support/index.html': support_page('en'), 'yaybo/soporte/index.html': support_page('es')}
    texts = {'privacy': PRIVACY, 'terms': TERMS}
    for lang, kind, slug, title, desc in PAGES:
        alts = {L: DIRS[(L, kind)] for L in ('en', 'es')}
        clean = title.rsplit(' — ', 1)[0]
        pages[f'yaybo/{slug}/index.html'] = legal_page(lang, kind, fill(texts[kind][lang], lang), clean, desc, alts)
    failed, shown = False, set()
    built = set(pages)
    for path, html in pages.items():
        rows, ok = audit(html, path, built)
        if not ok:
            failed = True
            for label, val, mn, good in rows:
                if not good and (path, label) not in shown and not label.startswith(('light', 'dark', 'composited')) or (not good and label not in shown):
                    shown.add(label)
                    shown.add((path, label))
                    print(f'AUDIT FAIL {path}: {label} = {val} (min {mn})')
    rows0, ok0 = audit(pages['yaybo/index.html'], 'yaybo/index.html', built)
    if verbose:
        worst = min((r for r in rows0 if r[2] and r[0].startswith(('light', 'dark', 'composited'))), key=lambda r: r[1] / r[2])
        print(f'yaybo audit: {sum(1 for r in rows0 if r[2])} contrast checks, tightest {worst[0]} = {worst[1]} (min {worst[2]})')
    if failed:
        raise SystemExit('yaybo audit failed: nothing written')
    if write:
        for path, html in pages.items():
            out = ROOT / path
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(html, encoding='utf-8')
        un = unused_media(pages)
        if un and verbose:
            print('yaybo: media files not referenced by any page:', ', '.join(un))
    return pages
