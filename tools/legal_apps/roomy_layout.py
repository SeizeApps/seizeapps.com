"""Roomy's own page layout for tools/gen_legal_apps.py (slug 'roomy'). It shares no template, class name or
stylesheet with the other apps' pages: everything here is prefixed `ry-`.

Identity: Roomy is a swipe cleaner whose icon is a sunset photo card on a citrus tile, so the pages are warm cream
(light) or warm charcoal (dark), with citrus-lime bands and night bands, sunset/hills art, and CSS-drawn iPhone
illustrations of the app with sample data (nothing here is a real screenshot: the only real ones are of the old
blue 0.0.3 build and would misrepresent the app).

Pages: home (key 'index'), privacy, terms, support, all in one shell. Isolation (App Store guideline 4.3): the pages link
only to each other, to roomy/media/, to mailto:hello@seizeapps.com and to the vendors and regulators the legal text names;
nothing on apps.apple.com (the app is not on sale), no Seize / studio / other-app link, no external font, script or image.

Colours: tokens at the top of the stylesheet; PAIRS lists every foreground/background pair they form, in both modes.
audit(html) measures them from the <style> of the generated page and refuses unknown `color:` declarations, so a new text
colour cannot ship unmeasured. gen_legal_apps.py refuses to write a page whose pair is under 4.5:1.

Depth: the directory copy roomy/privacy/index.html sits one level deeper; page() learns that from the marker
`<!--@terms@-->` at the top of every body (gen_legal_apps.fill() turns it into the relative path of terms.html).
"""

import re

MIN = 4.5
HOME_PAGES = ('privacy', 'terms', 'support')

# ------------------------------------------------------------------ colour tokens
# Every colour that carries text is a token here, and PAIRS below lists every foreground/background it sits on.
LIGHT = dict(
    bg='#FBF8EF', bg2='#F3EEDF', surface='#FFFFFF', surface2='#F6F2E5', text='#1E1C17', muted='#5A5748',
    line='#DDD6BF', line2='#6F6A55', olive='#4F6600', focus='#4F6600', sky_a='#FFF3CF', navbg='rgba(251,248,239,.86)',
    ink='#15190A', hl_a='#D6EE5E', hl_b='#AACD2F', glow_l='rgba(201,230,74,.5)', glow_o='rgba(255,184,92,.34)',
    glow_red='rgba(242,84,91,.2)', glow_worst='#FFDEA7', sun_o='.9', sun_b='1px', dot_halo='rgba(170,205,47,.35)',
    hill_far='#C3DA7E', hill_mid='#8FC15F', hill_near='#D3EC58', shadow='0 1px 0 rgba(255,255,255,.9) inset,0 18px 40px -22px rgba(60,50,20,.3)',
    lime_a='#D3EC58', lime_b='#AACD2F', lime_ink='#15190A', lime_muted='#2E3A0D', lime_eyebrow='#15190A', lime_focus='#15190A',
    lime_card='#F4FADA', lime_line='rgba(21,25,10,.2)', lime_line2='#3B4A0E', lime_glow='rgba(255,255,255,.4)',
    lime_chip='#15190A', lime_chipfg='#D6EE5E',
)
DARK = dict(
    bg='#16120E', bg2='#1B1610', surface='#211C16', surface2='#2D261E', text='#F4EFE3', muted='#B4AA9B',
    line='#352D23', line2='#9C917F', olive='#C9E64A', focus='#C9E64A', sky_a='#2A1D12', navbg='rgba(22,18,14,.84)',
    glow_l='rgba(201,230,74,.13)', glow_o='rgba(255,138,91,.17)', glow_red='rgba(242,84,91,.14)', glow_worst='#4E2F1F',
    sun_o='.5', sun_b='28px', dot_halo='rgba(201,230,74,.2)',
    hill_far='#1F2E1D', hill_mid='#27402A', hill_near='#2F4A27',
    shadow='0 1px 0 rgba(255,255,255,.045) inset,0 22px 44px -22px rgba(0,0,0,.7)',
    lime_a='#1E2A08', lime_b='#2A3A0C', lime_ink='#F1F5DC', lime_muted='#C6D2A0', lime_eyebrow='#D6EE5E', lime_focus='#D6EE5E',
    lime_card='#34470F', lime_line='rgba(214,238,94,.22)', lime_line2='#9DB63A', lime_glow='rgba(201,230,74,.1)',
    lime_chip='#D6EE5E', lime_chipfg='#15190A',
)
NIGHT = dict(  # the same in both modes
    night_a='#1B1610', night_b='#16120E', night_text='#F4EFE3', night_muted='#B4AA9B', night_surface='#211C16',
    night_surface2='#2D261E', night_line='#3B3328', night_line2='#9C917F', night_accent='#C9E64A', night_warm='#FF8A3D',
    orb='rgba(201,230,74,.3)',
)
LIGHT.update(NIGHT); DARK.update(NIGHT)
LIGHT.update(hillcap='#15190A'); DARK.update(hillcap='#F4EFE3')


def decl(d):
    return ';'.join(f'--ry-{k.replace("_", "-")}:{v}' for k, v in d.items())


# (label, foreground, [backgrounds]); names are tokens, '#hex' is a literal used in the CSS.
INK = '#15190A'
PAIRS = [
    ('text on page', 'text', ['bg', 'bg2', 'surface', 'surface2', 'sky_a']),
    ('muted text on page', 'muted', ['bg', 'bg2', 'surface', 'surface2', 'sky_a', 'glow_worst']),
    ('eyebrow / link olive', 'olive', ['bg', 'bg2', 'surface', 'surface2', 'sky_a']),
    ('focus ring', 'focus', ['bg', 'bg2', 'surface']),
    ('boundary (borders, step circles, badge)', 'line2', ['bg', 'bg2', 'surface', 'sky_a']),
    ('ink on citrus highlight / chips', INK, ['hl_a', 'hl_b', '#C9E64A', '#D6EE5E']),
    ('ink on pearl PRO pill', INK, ['#F4EBDD', '#D8C6A5']),
    ('ink on mint (stamp, keep)', INK, ['#3BD9A5', '#5CE5C0']),
    ('ink on coral (stamp, delete)', INK, ['#F2545B', '#F77A52']),
    ('caption on hills', 'hillcap', ['surface']),
    ('lime band: text', 'lime_ink', ['lime_a', 'lime_b', 'lime_card']),
    ('lime band: muted text', 'lime_muted', ['lime_a', 'lime_b', 'lime_card']),
    ('lime band: eyebrow', 'lime_eyebrow', ['lime_a', 'lime_b']),
    ('lime band: focus ring', 'lime_focus', ['lime_a', 'lime_b']),
    ('lime band: boundary', 'lime_line2', ['lime_a', 'lime_b']),
    ('lime band: icon chip', 'lime_chipfg', ['lime_chip']),
    ('night band: text', 'night_text', ['night_a', 'night_b', 'night_surface', 'night_surface2']),
    ('night band: muted text', 'night_muted', ['night_a', 'night_b', 'night_surface', 'night_surface2']),
    ('night band: citrus accent', 'night_accent', ['night_a', 'night_b', 'night_surface', 'night_surface2']),
    ('night band: warm accent', 'night_warm', ['night_surface', 'night_surface2']),
    ('night band: boundary', 'night_line2', ['night_a', 'night_b', 'night_surface']),
    # phone illustrations and floating chips (literal colours of the app, see Theme.swift)
    ('app: text', '#F4EFE3', ['#16120E', '#211C16', '#2D261E']),
    ('app: secondary text', '#B4AA9B', ['#16120E', '#211C16', '#2D261E']),
    ('app: citrus on dark', '#C9E64A', ['#16120E', '#211C16', '#15190A']),
    ('app: ink on start card', INK, ['#D6EE5E', '#AACD2F']),
    ('app: citrus on ink button', '#D6EE5E', [INK]),
    ('app: ink on coral button', INK, ['#F2545B', '#F77A52']),
    ('app: ink on citrus tag', INK, ['#C9E64A']),
    ('app: ink on mint chip', INK, ['#3BD9A5']),
    ('skip link', 'bg', ['text']),
    ('app: mint on dark', '#3BD9A5', ['#16120E', '#211C16']),
    ('app: coral on dark', '#F2545B', ['#16120E', '#211C16']),
]

TOKEN_NAMES = set('ry-' + k.replace('_', '-') for k in LIGHT)


def _vars(block):
    return dict(m.groups() for m in re.finditer(r'--(ry-[a-z0-9-]+):([^;]+)', block))


def _resolve(name, v):
    if name.startswith('#'):
        return name
    return v['ry-' + name.replace('_', '-')]


def audit(html):
    """Measure every PAIRS entry in light and dark, from the <style> of a generated page, and check that no `color:`
    declaration in that stylesheet uses a colour that PAIRS does not know. -> (rows, ok); a row is
    (mode, label, fg, bg, ratio). Imported here, not at the top, to avoid an import cycle with gen_legal_apps."""
    from gen_legal_apps import ratio
    style = re.search(r'<style>(.*?)</style>', html, re.S).group(1)
    light = _vars(re.search(r':root\{([^}]*)\}', style).group(1))
    dark = dict(light, **_vars(re.search(r'prefers-color-scheme:dark\)\{:root\{([^}]*)\}', style).group(1)))
    rows = []
    for mode, v in (('light', light), ('dark', dark)):
        for label, fg, bgs in PAIRS:
            f = _resolve(fg, v)
            for bg in bgs:
                b = _resolve(bg, v)
                rows.append((mode, label, f, b, ratio(f, b)))
    ok = all(r[4] >= MIN for r in rows)
    known = {_resolve(fg, light).upper() for _, fg, _ in PAIRS} | {_resolve(fg, dark).upper() for _, fg, _ in PAIRS}
    known_vars = {f'--ry-{fg.replace("_", "-")}' for _, fg, _ in PAIRS if not fg.startswith('#')}
    # text colours declared with `color:` must be a measured token or a measured literal (background-color etc. are not text)
    unknown = set()
    for m in re.finditer(r'(?<![\w-])color:\s*(#[0-9A-Fa-f]{6}|var\(--ry-[a-z0-9-]+\))', style):
        val = m.group(1)
        if val.startswith('#'):
            if val.upper() not in known: unknown.add(val)
        else:
            name = val[4:-1]
            if name not in known_vars and name not in INHERITED_TEXT_VARS: unknown.add(val)
    if unknown:
        raise SystemExit('roomy_layout.audit: text colours not covered by PAIRS: ' + ', '.join(sorted(unknown)))
    return rows, ok


# variables that only alias a measured token inside a band (--ry-text, --ry-muted ... are re-pointed in .ry-lime / .ry-night)
INHERITED_TEXT_VARS = {'--ry-text', '--ry-muted', '--ry-olive', '--ry-ink', '--ry-night-text', '--ry-lime-ink', '--ry-hillcap'}


CSS = r'''
@LIGHT_ROOT@
@media (prefers-color-scheme:dark){@DARK_ROOT@}
:root{--ry-display:ui-rounded,"SF Pro Rounded","Arial Rounded MT Bold",system-ui,sans-serif;--ry-body:"Avenir Next","Avenir","Segoe UI",ui-sans-serif,"Helvetica Neue",Arial,sans-serif;--ry-mono:ui-monospace,"SF Mono",Menlo,Consolas,"Liberation Mono",monospace;--ry-app:system-ui,-apple-system,"SF Pro Text","Segoe UI",Roboto,sans-serif;--ry-wrapw:1200px}
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
@media (forced-colors:active){.ry-badge,.ry-card,.ry-plan,.ry-chip,.ry-col{border:1px solid CanvasText}.ry-conf,.ry-hills,.ry-sun{display:none}a:focus-visible{outline:2px solid Highlight}}
body{margin:0;background:var(--ry-bg);color:var(--ry-text);font:400 17px/1.55 var(--ry-body);-webkit-font-smoothing:antialiased;overflow-x:clip}
@media (min-width:1100px){body{font-size:18px}}
img,svg{display:block;max-width:100%}
a{color:var(--ry-olive);text-underline-offset:.18em;text-decoration-thickness:1px}
a:hover{text-decoration-thickness:2px}
:focus-visible{outline:3px solid var(--ry-focus);outline-offset:3px;border-radius:6px}
.ry-skip{position:absolute;left:12px;top:-64px;background:var(--ry-text);color:var(--ry-bg);padding:10px 16px;border-radius:10px;z-index:100;font-weight:700;text-decoration:none}
.ry-skip:focus{top:12px}
.ry-wrap{width:100%;max-width:calc(var(--ry-wrapw) + 2*clamp(20px,4vw,40px));margin-inline:auto;padding-inline:clamp(20px,4vw,40px)}
.ry-ic{width:1em;height:1em;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;flex:none}
.ry-ic.f{fill:currentColor;stroke:none}
.ry-ic.b{stroke-width:2.8}
.ry-ph{width:100%;height:100%}
h1,h2,h3,h4{font-family:var(--ry-display);font-weight:800;margin:0;letter-spacing:-.02em;line-height:1.05;text-wrap:balance}
p{margin:0}

/* top bar */
.ry-top{position:sticky;top:0;z-index:50;background:var(--ry-navbg);-webkit-backdrop-filter:saturate(1.5) blur(16px);backdrop-filter:saturate(1.5) blur(16px);border-bottom:1px solid var(--ry-line)}
.ry-top-in{display:flex;align-items:center;gap:20px;height:64px}
.ry-brand{display:flex;align-items:center;gap:11px;color:var(--ry-text);text-decoration:none;font-family:var(--ry-display);font-weight:800;font-size:21px;letter-spacing:-.02em}
.ry-brand img{width:34px;height:34px;border-radius:9px;box-shadow:0 0 0 1px rgba(0,0,0,.1)}
.ry-nav{display:flex;gap:2px;margin-left:auto;align-items:center}
.ry-nav a{color:var(--ry-muted);text-decoration:none;font-size:15px;font-weight:600;padding:9px 13px;border-radius:999px}
.ry-nav a:hover{color:var(--ry-text);background:var(--ry-surface2)}
.ry-nav a[aria-current]{color:var(--ry-text);background:var(--ry-surface2)}

/* type bits */
.ry-k{font-family:var(--ry-mono);font-size:12.5px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--ry-olive);display:flex;align-items:center;gap:12px;margin:0 0 18px}
.ry-k::before{content:"";width:26px;height:3px;border-radius:3px;background:currentColor;flex:none}
.ry-lead{font-size:clamp(18px,1.5vw,21px);line-height:1.5;color:var(--ry-muted);max-width:34em;margin-top:22px;text-wrap:pretty}
h2.ry-h{font-size:clamp(36px,4.8vw,62px)}
.ry-mark{background:linear-gradient(135deg,var(--ry-hl-a),var(--ry-hl-b));color:var(--ry-ink);padding:0 .18em .03em;line-height:1.1;display:inline-block;border-radius:.24em;-webkit-box-decoration-break:clone;box-decoration-break:clone}

/* badge: a plain outlined label, not a link */
.ry-badge{display:inline-flex;align-items:center;gap:11px;border:1.5px solid var(--ry-line2);border-radius:999px;padding:12px 22px 12px 18px;font-family:var(--ry-display);font-weight:800;font-size:17px;letter-spacing:-.005em;color:var(--ry-text);background:var(--ry-surface);cursor:default;user-select:none}
.ry-badge i{width:10px;height:10px;border-radius:50%;background:linear-gradient(135deg,var(--ry-hl-a),var(--ry-hl-b));box-shadow:0 0 0 4px var(--ry-dot-halo);flex:none}

/* hero */
.ry-hero{position:relative;isolation:isolate;overflow:clip;padding:clamp(36px,5vw,76px) 0 0;background:linear-gradient(180deg,var(--ry-sky-a),var(--ry-bg) 88%)}
.ry-hero::before{content:"";position:absolute;z-index:-1;inset:0;background:radial-gradient(34% 46% at 80% 36%,var(--ry-glow-l),transparent 72%),radial-gradient(40% 40% at 72% 96%,var(--ry-glow-o),transparent 72%);pointer-events:none}
.ry-sun{position:absolute;z-index:-1;right:9%;top:14%;width:clamp(240px,30vw,460px);aspect-ratio:1;border-radius:50%;background:radial-gradient(circle at 40% 35%,#FFF6D6 0,#FFD66B 40%,#FF8A5B 100%);opacity:var(--ry-sun-o);filter:blur(var(--ry-sun-b))}
.ry-hero-in{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);align-items:center;gap:32px;padding-bottom:clamp(120px,13vw,200px)}
.ry-brandrow{display:flex;align-items:center;gap:14px;margin-bottom:26px}
.ry-brandrow img{width:60px;height:60px;border-radius:15px;box-shadow:0 12px 26px -10px rgba(60,80,0,.6),0 0 0 1px rgba(0,0,0,.08)}
.ry-brandrow span{font-family:var(--ry-mono);font-size:12.5px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--ry-olive);line-height:1.35}
.ry-hero h1{font-size:clamp(50px,7.2vw,98px);line-height:.98;letter-spacing:-.025em}
.ry-hero .ry-lead{margin-top:26px}
.ry-hero-row{display:flex;flex-wrap:wrap;align-items:center;gap:16px 24px;margin-top:34px}
.ry-fact{display:flex;align-items:center;gap:9px;font-weight:600;font-size:16px;color:var(--ry-muted)}
.ry-fact .ry-ic{font-size:19px;color:var(--ry-olive)}
.ry-stage{position:relative;height:calc(866px*var(--ry-s) + 74px*var(--ry-s)/.74);width:min(100%,640px);justify-self:end;--ry-s:.74}
.ry-stage .ry-fit{position:absolute;--s:var(--ry-s)}
.ry-stage .a{right:0;top:0;z-index:1}
.ry-stage .b{left:0;top:calc(74px*var(--ry-s)/.74);z-index:2}
figure.ry-fit{margin:0}
.ry-chip{position:absolute;z-index:3;display:flex;align-items:center;gap:12px;background:var(--ry-night-surface);color:var(--ry-night-text);border:1px solid var(--ry-night-line);border-radius:18px;padding:12px 16px;font-family:var(--ry-app);box-shadow:0 18px 36px -12px rgba(20,14,6,.55)}
.ry-chip .ic{width:36px;height:36px;border-radius:11px;display:grid;place-items:center;font-size:20px;flex:none}
.ry-chip b{display:block;font-family:var(--ry-display);font-size:21px;line-height:1.1;letter-spacing:-.01em}
.ry-chip span.s{display:block;font-size:12.5px;color:var(--ry-night-muted)}
.ry-chip.c1{right:-26px;top:46%}
.ry-chip.c2{left:30px;top:6px}
.ry-fine{font-size:14px;color:var(--ry-muted);margin-top:14px;text-align:center;position:relative;z-index:4}
.ry-hills{position:absolute;z-index:-1;left:0;right:0;bottom:-1px;width:100%;height:clamp(130px,16vw,250px)}
.ry-hills .far{fill:var(--ry-hill-far)}.ry-hills .mid{fill:var(--ry-hill-mid)}.ry-hills .near{fill:var(--ry-hill-near)}
.ry-heroholder{position:relative}
.ry-herocap{position:absolute;left:0;right:0;bottom:clamp(14px,2vw,26px);z-index:3;text-align:center;font-size:14px;color:var(--ry-hillcap)}

/* stats strip */
.ry-spec{border-block:1px solid var(--ry-line);background:var(--ry-bg2)}
.ry-spec ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,1fr)}
.ry-spec li{padding:28px 28px;border-left:1px solid var(--ry-line)}
.ry-spec li:first-child{border-left:0;padding-left:0}
.ry-spec .n{display:block;font-family:var(--ry-display);font-weight:800;font-size:clamp(32px,3.4vw,46px);letter-spacing:-.035em;line-height:1}
.ry-spec .n u{text-decoration:none;font-size:.5em;letter-spacing:-.01em;color:var(--ry-muted);margin-left:.2em}
.ry-spec .t{display:block;margin-top:10px;font-size:15.5px;color:var(--ry-muted);line-height:1.4;max-width:25ch}

/* bands */
.ry-band{position:relative;isolation:isolate;overflow:clip;padding:clamp(76px,9.5vw,136px) 0}
.ry-two{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(36px,6vw,96px);align-items:center}
.ry-two.flip>:first-child{order:2}
.ry-mid{position:relative;display:flex;justify-content:center}
.ry-mid .ry-fit{--s:.8;position:relative;z-index:2}
.ry-cap{font-size:14px;color:var(--ry-muted);text-align:center;margin-top:18px}
.ry-list{list-style:none;padding:0;margin:34px 0 0;display:grid;gap:12px}
.ry-list li{display:flex;gap:16px;align-items:flex-start;padding:16px 18px;border-radius:20px;background:var(--ry-surface);border:1px solid var(--ry-line)}
.ry-list .ic{flex:none;width:44px;height:44px;border-radius:13px;background:linear-gradient(135deg,var(--ry-hl-a),var(--ry-hl-b));color:var(--ry-ink);display:grid;place-items:center;font-size:23px}
.ry-list b{display:block;font:800 1.08rem/1.2 var(--ry-display);letter-spacing:-.01em}
.ry-list span.d{display:block;color:var(--ry-muted);font-size:16.5px;margin-top:3px;line-height:1.45}

/* lime band (deep olive in dark mode) */
.ry-lime{--ry-text:var(--ry-lime-ink);--ry-muted:var(--ry-lime-muted);--ry-olive:var(--ry-lime-eyebrow);--ry-focus:var(--ry-lime-focus);--ry-surface:var(--ry-lime-card);--ry-line:var(--ry-lime-line);--ry-line2:var(--ry-lime-line2);color:var(--ry-lime-ink);background:radial-gradient(42% 50% at 14% 36%,var(--ry-lime-glow),transparent 70%),linear-gradient(180deg,var(--ry-lime-a),var(--ry-lime-b))}
.ry-lime a{color:var(--ry-lime-ink)}
.ry-lime .ry-list .ic{background:var(--ry-lime-chip);color:var(--ry-lime-chipfg)}
.ry-fly{position:absolute;z-index:1;width:clamp(120px,13vw,190px);aspect-ratio:3/4;border-radius:22px;overflow:hidden;box-shadow:0 24px 40px -10px rgba(21,25,10,.45)}
.ry-fly.l{left:-4%;top:12%;transform:rotate(-16deg)}
.ry-fly.r{right:-4%;bottom:8%;transform:rotate(12deg)}
.ry-fly .ry-stamp{left:50%;top:14%;margin-left:-50%;width:100%;text-align:center}

/* swipe buttons */
.ry-rb{width:68px;height:68px;border-radius:50%;display:grid;place-items:center;font-size:30px;color:#15190A;box-shadow:0 10px 22px -8px rgba(0,0,0,.4)}
.ry-rb.x{background:linear-gradient(135deg,#F2545B,#F77A52)}
.ry-rb.k{background:linear-gradient(135deg,#3BD9A5,#5CE5C0)}
.ry-rb.u{background:#2D261E;color:#F4EFE3;box-shadow:none}
/* device */
.ry-fit{--s:.7;width:calc(412px*var(--s));height:calc(866px*var(--s));flex:none}
.ry-fit>.ry-dev{width:412px;height:866px;transform:scale(var(--s));transform-origin:0 0}
.ry-dev{position:relative;border-radius:68px;padding:4px;background:linear-gradient(150deg,#7B7060 0%,#2A241C 18%,#14110D 50%,#2A241C 82%,#6A5F50 100%);box-shadow:0 50px 90px -30px rgba(20,14,4,.65),0 18px 34px -14px rgba(20,14,4,.45)}
.ry-dev::before,.ry-dev::after{content:"";position:absolute;width:4px;border-radius:2px;background:linear-gradient(#5B5143,#2A241C)}
.ry-dev::before{left:-3px;top:150px;height:54px;box-shadow:0 74px 0 #3B3328}
.ry-dev::after{right:-3px;top:210px;height:96px}
.ry-bz{height:100%;border-radius:64px;background:#050403;padding:7px}
.ry-scr{position:relative;width:390px;height:844px;border-radius:57px;overflow:hidden;background:#16120E;color:#F4EFE3;font-family:var(--ry-app);font-size:15px;line-height:1.3;text-align:left}
.ry-isl{position:absolute;left:50%;top:11px;width:120px;height:35px;margin-left:-60px;border-radius:18px;background:#000;z-index:20}
.ry-hi{position:absolute;left:50%;bottom:8px;width:136px;height:5px;margin-left:-68px;border-radius:3px;background:rgba(244,239,227,.7);z-index:20}
.ry-sb{height:56px;display:flex;align-items:flex-end;justify-content:space-between;padding:0 34px 8px 40px;font-weight:600;font-size:16px}
.ry-sb svg{width:66px;height:13px}
.ry-pad{padding:6px 16px 0}
.ry-sec-c{color:#B4AA9B}
/* home screen */
.ry-hh{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;padding-top:2px}
.ry-hh .t{font-family:var(--ry-display);font-weight:700;font-size:34px;letter-spacing:-.01em;line-height:1.1}
.ry-hh .g{font-size:15px;color:#B4AA9B}
.ry-hb{display:flex;gap:12px;align-items:center}
.ry-prob{font-weight:800;font-size:13px;letter-spacing:.05em;padding:7px 13px;border-radius:999px;background:linear-gradient(135deg,#F4EBDD,#D8C6A5);color:#15190A}
.ry-gear{width:38px;height:38px;border-radius:50%;background:#211C16;display:grid;place-items:center;font-size:19px;color:#F4EFE3}
.ry-card2{background:#211C16;border-radius:22px;padding:16px;margin-bottom:12px}
.ry-stor{display:flex;gap:16px;align-items:center}
.ry-ring{position:relative;width:92px;height:92px;flex:none}
.ry-ring svg{width:92px;height:92px;transform:rotate(-90deg)}
.ry-ring .c{position:absolute;inset:0;display:grid;place-content:center;text-align:center}
.ry-ring b{font-family:var(--ry-display);font-size:20px;line-height:1}
.ry-ring small{font-size:11px;color:#B4AA9B}
.ry-stor .h5{margin:0;font-size:20px;font-weight:700}
.ry-stor p{font-size:14.5px;color:#B4AA9B;margin-top:2px}
.ry-stor hr{border:0;border-top:1px solid #3A3226;margin:9px 0}
.ry-stor .mm{display:flex;gap:12px;font-size:12.5px;font-weight:600;color:#B4AA9B}
.ry-stor .mm span{display:flex;gap:5px;align-items:center}
.ry-start{border-radius:26px;padding:20px;background:linear-gradient(135deg,#D6EE5E,#AACD2F);color:#15190A;margin-bottom:12px;box-shadow:0 12px 24px -8px rgba(201,230,74,.35)}
.ry-start .h{display:flex;justify-content:space-between;align-items:flex-start}
.ry-start .h5{margin:0;font-family:var(--ry-display);font-size:23px;line-height:1.15}
.ry-start p{font-size:14.5px;font-weight:500;margin-top:6px}
.ry-start .hand{font-size:38px;opacity:.9}
.ry-start .ch{display:inline-flex;align-items:center;gap:5px;font-size:12.5px;font-weight:700;background:rgba(21,25,10,.2);border-radius:999px;padding:5px 10px;margin-top:12px}
.ry-start .bt{display:flex;gap:10px;margin-top:14px}
.ry-start .go{flex:1;display:flex;align-items:center;justify-content:center;gap:8px;background:#15190A;color:#C9E64A;font-weight:600;font-size:17px;border-radius:999px;padding:13px}
.ry-start .sf{width:50px;height:50px;border-radius:50%;background:rgba(21,25,10,.2);display:grid;place-items:center;font-size:19px}
.ry-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:18px}
.ry-st{background:#211C16;border-radius:18px;padding:13px 14px}
.ry-st .ry-ic{font-size:19px;margin-bottom:6px}
.ry-st b{display:block;font-family:var(--ry-display);font-size:18px;font-variant-numeric:tabular-nums}
.ry-st span{font-size:12.5px;color:#B4AA9B}
.ry-sh .h5{margin:0;font-size:20px;font-weight:700}
.ry-sh p{font-size:14.5px;color:#B4AA9B;margin:1px 0 12px}
.ry-cg{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.ry-ctile{background:#211C16;border-radius:20px;padding:14px;display:grid;gap:10px}
.ry-ctile .tp{display:flex;justify-content:space-between;align-items:flex-start}
.ry-ctile b{display:block;font-size:17px;font-weight:600}
.ry-ctile span.s{font-size:14.5px;color:#B4AA9B}
.ry-pb{font-weight:800;font-size:10.5px;letter-spacing:.05em;padding:4px 8px;border-radius:999px;background:linear-gradient(135deg,#F4EBDD,#D8C6A5);color:#15190A}
/* swipe screen */
.ry-sw-top{display:flex;align-items:center;justify-content:space-between;padding:6px 18px 0}
.ry-circ{width:38px;height:38px;border-radius:50%;background:#211C16;display:grid;place-items:center;font-size:18px}
.ry-sw-top .n{font-weight:600;font-size:17px;font-variant-numeric:tabular-nums}
.ry-sw-top .tr{position:relative}
.ry-sw-top .tr em{position:absolute;right:-5px;top:-5px;font-style:normal;font-size:11px;font-weight:800;background:#F2545B;color:#15190A;min-width:19px;height:19px;border-radius:10px;display:grid;place-items:center;padding:0 5px}
.ry-prog{height:4px;border-radius:2px;background:#2D261E;margin:14px 18px 0;overflow:hidden}
.ry-prog i{display:block;height:100%;width:19%;border-radius:2px;background:linear-gradient(90deg,#AACD2F,#D6EE5E)}
.ry-deck{position:relative;height:540px;margin-top:20px}
.ry-card-s{position:absolute;left:25px;width:340px;height:500px;border-radius:30px;overflow:hidden;box-shadow:0 26px 40px -14px rgba(0,0,0,.65)}
.ry-card-s.back{top:34px;transform:scale(.95);background:#211C16;filter:brightness(.8)}
.ry-card-s.front{top:12px;transform:translateX(36px) rotate(7deg)}
.ry-card-s .sc{position:absolute;left:0;right:0;bottom:0;height:110px;background:linear-gradient(transparent,rgba(0,0,0,.6))}
.ry-card-s .lv{position:absolute;left:16px;bottom:16px;display:flex;gap:6px;align-items:center;font-size:13px;font-weight:600;color:#fff;background:rgba(0,0,0,.35);border-radius:999px;padding:6px 11px}
.ry-stamp{position:absolute;left:20px;top:28px;font-family:var(--ry-display);font-weight:700;font-size:40px;letter-spacing:.04em;color:#3BD9A5;border:5px solid #3BD9A5;border-radius:14px;padding:2px 14px;transform:rotate(-14deg);background:rgba(10,30,20,.18)}
.ry-sw-info{text-align:center;font-size:14px;color:#B4AA9B;font-weight:600}
.ry-sw-btn{display:flex;justify-content:center;align-items:center;gap:26px;margin-top:14px}
.ry-sw-btn .rb{width:70px;height:70px;font-size:31px}
.ry-sw-btn .rb.u{width:48px;height:48px;font-size:22px;background:#2D261E;color:#F4EFE3}
.ry-sw-foot{text-align:center;font-size:13px;color:#B4AA9B;margin-top:16px;padding:0 40px}
.ry-sw-foot b{display:inline-flex;gap:5px;align-items:center;color:#15190A;background:#C9E64A;border-radius:999px;padding:3px 10px;font-weight:700;margin-bottom:8px}
/* similar screen */
.ry-nv{display:flex;align-items:center;gap:6px;padding:4px 14px 0;font-size:17px;color:#C9E64A}
.ry-nv .tt{position:absolute;left:0;right:0;text-align:center;color:#F4EFE3;font-weight:600;pointer-events:none}
.ry-sim-h{padding:14px 18px 0}
.ry-sim-h .h5{margin:0;font-family:var(--ry-display);font-size:26px;line-height:1.1}
.ry-sim-h p{font-size:14px;color:#B4AA9B;margin-top:6px}
.ry-grp{margin:14px 16px 0;background:#211C16;border-radius:22px;padding:14px}
.ry-grp .gh{display:flex;justify-content:space-between;font-size:14px;color:#B4AA9B;font-weight:600;margin-bottom:10px}
.ry-grp .tt{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.ry-th{position:relative;aspect-ratio:1;border-radius:14px;overflow:hidden}
.ry-th.sel{box-shadow:0 0 0 3px #F2545B}
.ry-th .ck{position:absolute;right:6px;top:6px;width:22px;height:22px;border-radius:50%;background:#F2545B;color:#15190A;display:grid;place-items:center;font-size:12px}
.ry-th .bst{position:absolute;left:6px;top:6px;font-size:11.5px;font-weight:800;color:#15190A;background:linear-gradient(135deg,#D6EE5E,#AACD2F);padding:3px 8px;border-radius:999px}
.ry-bot{position:absolute;left:0;right:0;bottom:0;padding:22px 16px 34px;background:linear-gradient(transparent,#16120E 36%)}
.ry-bot .dl{display:flex;justify-content:center;align-items:center;gap:8px;background:linear-gradient(135deg,#F2545B,#F77A52);color:#15190A;font-weight:700;font-size:17px;border-radius:999px;padding:15px}


.ry-ui{font-family:var(--ry-app);color:#F4EFE3}
.ry-it{width:40px;height:40px;border-radius:12px;display:grid;place-items:center;font-size:20px;flex:none}

.ry-fp{display:flex;align-items:center;gap:18px;margin-top:auto;padding-top:14px;flex-wrap:wrap}
.ry-fp figure{margin:0;display:grid;gap:10px;justify-items:center}
.ry-fp .pic{width:116px;height:116px;border-radius:18px;overflow:hidden;box-shadow:0 14px 24px -14px rgba(0,0,0,.5)}
.ry-fp .grid{display:grid;grid-template-columns:repeat(8,1fr);gap:2px;width:116px;padding:6px;border-radius:12px;background:#211C16;border:1px solid #352D23}
.ry-fp .grid i{aspect-ratio:1;border-radius:2px;background:#3A3226}
.ry-fp .grid i.o{background:#C9E64A}
.ry-fp .eq{font-family:var(--ry-display);font-weight:700;font-size:40px;color:var(--ry-olive);margin-bottom:34px}
.ry-fp figcaption{font-family:var(--ry-mono);font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--ry-muted)}
.ry-match{margin-left:6px;align-self:center;display:inline-flex;gap:8px;align-items:center;background:#3BD9A5;color:#15190A;font-family:var(--ry-app);font-weight:700;font-size:14px;border-radius:999px;padding:9px 15px}
.ry-vid{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:22px;margin-top:auto;padding-top:10px;align-items:stretch}
.ry-vl{display:grid;gap:10px;align-content:start}
.ry-vr{display:flex;align-items:center;gap:12px;background:#211C16;border:1px solid #2F271D;border-radius:18px;padding:11px 14px 11px 11px;font-family:var(--ry-app);color:#F4EFE3}
.ry-vr .th{width:50px;height:50px;border-radius:12px;overflow:hidden;flex:none}
.ry-vr .m{min-width:0;flex:1}
.ry-vr b{display:block;font-size:15px;font-weight:600;line-height:1.2}
.ry-vr .bar{height:6px;border-radius:3px;background:#2D261E;margin-top:7px;overflow:hidden}
.ry-vr .bar i{display:block;height:100%;border-radius:3px;background:linear-gradient(90deg,#AACD2F,#D6EE5E)}
.ry-vr .sz{font-size:13px;color:#B4AA9B;white-space:nowrap;font-variant-numeric:tabular-nums}
.ry-sheet{background:#211C16;border:1px solid #2F271D;border-radius:22px;padding:18px;font-family:var(--ry-app);color:#F4EFE3;display:flex;flex-direction:column;gap:14px}
.ry-sheet .h4{margin:0;font-family:var(--ry-display);font-size:19px;letter-spacing:-.01em}
.ry-seg{display:grid;grid-template-columns:repeat(3,1fr);background:#16120E;border-radius:13px;padding:3px}
.ry-seg span{text-align:center;font-size:14px;font-weight:600;padding:8px 0;border-radius:10px;color:#B4AA9B}
.ry-seg span.on{background:#C9E64A;color:#15190A}
.ry-cmp{display:grid;gap:8px}
.ry-cmp div{display:grid;grid-template-columns:62px 1fr;gap:10px;align-items:center;font-size:13px;color:#B4AA9B}
.ry-cmp i{display:block;height:12px;border-radius:6px}
.ry-cmp .o i{width:100%;background:#4A3F31}
.ry-cmp .n i{width:46%;background:linear-gradient(90deg,#AACD2F,#D6EE5E)}
.ry-go{background:linear-gradient(135deg,#D6EE5E,#AACD2F);color:#15190A;font-weight:700;font-size:15.5px;text-align:center;padding:12px;border-radius:999px;display:flex;justify-content:center;gap:8px;align-items:center}


/* stamps: dark ink on a solid mint / coral fill, as in the app */
.ry-stamp{position:absolute;font-family:var(--ry-display);font-weight:800;letter-spacing:.06em;color:#15190A;border:4px solid #15190A;border-radius:14px;padding:3px 14px;box-shadow:0 0 0 4px rgba(255,255,255,.6);white-space:nowrap}
.ry-stamp.k{background:linear-gradient(135deg,#3BD9A5,#5CE5C0);transform:rotate(-14deg)}
.ry-stamp.d{background:linear-gradient(135deg,#F2545B,#F77A52);transform:rotate(14deg)}
.ry-card-s .ry-stamp{font-size:36px}
.ry-fly .ry-stamp{font-size:clamp(13px,1.4vw,19px);border-width:3px;border-radius:9px;padding:2px 8px;box-shadow:0 0 0 3px rgba(255,255,255,.6);width:auto;margin-left:0;left:50%;translate:-50% 0}
.ry-card-s.front.del{transform:translateX(-36px) rotate(-7deg)}
.ry-card-s.front.del .ry-stamp{left:auto;right:20px}

/* safe */
.ry-safe{padding-top:clamp(110px,13vw,190px);background:linear-gradient(180deg,var(--ry-bg),var(--ry-bg2))}
.ry-safe .ry-mid::before{content:"";position:absolute;inset:6% 2%;border-radius:50%;background:radial-gradient(closest-side,var(--ry-glow-red),transparent);z-index:0}
.ry-steps{list-style:none;padding:0;margin:34px 0 0;display:grid;counter-reset:s}
.ry-steps li{display:grid;grid-template-columns:52px 1fr;gap:18px;padding-bottom:26px;position:relative;counter-increment:s}
.ry-steps li::before{content:counter(s);width:52px;height:52px;border-radius:50%;display:grid;place-items:center;font:800 1.2rem/1 var(--ry-display);background:var(--ry-surface);border:2px solid var(--ry-line2);color:var(--ry-text);position:relative;z-index:2}
.ry-steps li:not(:last-child)::after{content:"";position:absolute;left:25px;top:52px;bottom:0;width:2px;background:var(--ry-line)}
.ry-steps li:last-child{padding-bottom:0}
.ry-steps li.go::before{background:linear-gradient(135deg,#F2545B,#F77A52);color:#15190A;border-color:transparent}
.ry-steps li.ok::before{background:linear-gradient(135deg,#3BD9A5,#5CE5C0);color:#15190A;border-color:transparent}
.ry-steps b{display:block;font:800 1.25rem/1.2 var(--ry-display);letter-spacing:-.015em;margin-top:2px}
.ry-steps span.d{display:block;color:var(--ry-muted);margin-top:5px}
/* trash screen */
.ry-tgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;padding:0 16px}
.ry-tgrid .c{position:relative;aspect-ratio:1;border-radius:12px;overflow:hidden}
.ry-tgrid .c b{position:absolute;right:6px;top:6px;width:20px;height:20px;border-radius:50%;background:#F2545B;color:#15190A;display:grid;place-items:center;font-size:11px}
.ry-trh{padding:6px 18px 12px}
.ry-trh .h5{margin:0;font-size:19px;font-weight:700}
.ry-trh p{font-size:13.5px;color:#B4AA9B;margin-top:3px}
.ry-trnote{font-size:12.5px;color:#B4AA9B;padding:12px 24px 0;text-align:center}

/* night bands */
.ry-night{--ry-text:var(--ry-night-text);--ry-muted:var(--ry-night-muted);--ry-olive:var(--ry-night-accent);--ry-focus:var(--ry-night-accent);--ry-surface:var(--ry-night-surface);--ry-surface2:var(--ry-night-surface2);--ry-line:var(--ry-night-line);--ry-line2:var(--ry-night-line2);color:var(--ry-night-text);background:linear-gradient(180deg,var(--ry-night-a),var(--ry-night-b))}
.ry-night::before{content:"";position:absolute;z-index:-1;inset:0;background-image:linear-gradient(rgba(244,239,227,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(244,239,227,.05) 1px,transparent 1px);background-size:72px 72px;-webkit-mask-image:radial-gradient(ellipse 80% 70% at 70% 40%,#000 15%,transparent 75%);mask-image:radial-gradient(ellipse 80% 70% at 70% 40%,#000 15%,transparent 75%);pointer-events:none}
.ry-night .ry-list li{background:var(--ry-night-surface);border-color:var(--ry-night-line)}
.ry-night .ry-list .ic{background:linear-gradient(135deg,var(--ry-hl-a),var(--ry-hl-b));color:var(--ry-ink)}
.ry-cleanup .ry-mid::after{content:"";position:absolute;inset:6% 0;border-radius:50%;background:radial-gradient(closest-side,rgba(201,230,74,.2),transparent);z-index:0}
.ry-float{position:absolute;z-index:4;display:flex;align-items:center;gap:9px;background:#C9E64A;color:#15190A;font:800 .95rem/1 var(--ry-display);padding:11px 15px;border-radius:999px;box-shadow:0 14px 30px rgba(0,0,0,.4)}
.ry-float .ry-ic{font-size:18px}
.ry-fpbox{margin-top:34px;padding:20px;border-radius:24px;background:var(--ry-night-surface);border:1px solid var(--ry-night-line)}
.ry-fpbox .ry-fp{margin-top:0;padding-top:0;flex-wrap:wrap}
.ry-fpbox .ry-cap{text-align:left;margin-top:16px;color:var(--ry-night-muted)}
.ry-fpbox .pic{width:104px;height:104px}.ry-fpbox .grid{width:104px}

/* compress */
.ry-compress{background:var(--ry-bg)}
.ry-proline{display:flex;align-items:center;gap:12px;margin-top:20px;font-weight:600;color:var(--ry-muted);font-size:16.5px}
.ry-pearl{display:inline-flex;font-family:var(--ry-app);font-weight:800;font-size:12.5px;letter-spacing:.07em;color:#15190A;background:linear-gradient(135deg,#F4EBDD,#D8C6A5);border-radius:999px;padding:5px 12px;box-shadow:inset 0 0 0 1px rgba(21,25,10,.2)}
.ry-sheetwrap{background:var(--ry-night-b);border-radius:32px;padding:clamp(20px,3vw,30px);box-shadow:0 40px 80px -30px rgba(40,30,0,.5);border:1px solid var(--ry-night-line)}
.ry-sheetwrap .ry-vid{margin-top:0;grid-template-columns:1fr}

/* private */
.ry-private{text-align:center}
.ry-orbit{position:relative;width:min(300px,70vw);aspect-ratio:1;margin:0 auto 18px;display:grid;place-items:center}
.ry-orbit i{position:absolute;border-radius:50%;border:1.5px solid var(--ry-orb)}
.ry-orbit i:nth-child(1){inset:0}.ry-orbit i:nth-child(2){inset:13%;border-style:dashed}.ry-orbit i:nth-child(3){inset:26%}
.ry-orbit img{position:relative;width:34%;aspect-ratio:1;height:auto;border-radius:24%;box-shadow:0 0 70px 6px rgba(201,230,74,.35),0 22px 44px rgba(0,0,0,.5)}
.ry-orbit .dot{position:absolute;width:44px;height:44px;border-radius:50%;background:var(--ry-night-surface);border:1px solid var(--ry-night-line2);display:grid;place-items:center;color:var(--ry-night-accent);font-size:21px}
.ry-orbit .dot.d1{left:50%;top:0;margin:-22px 0 0 -22px}.ry-orbit .dot.d2{right:7%;bottom:14%}.ry-orbit .dot.d3{left:7%;bottom:14%}
.ry-private h2{max-width:13em;margin-inline:auto;font-size:clamp(38px,5.6vw,72px)}
.ry-private .ry-lead{margin-inline:auto;color:var(--ry-night-muted)}
.ry-private .ry-k{justify-content:center}
.ry-no{list-style:none;margin:28px 0 0;padding:0;display:flex;flex-wrap:wrap;gap:8px;justify-content:center}
.ry-no li{display:inline-flex;align-items:center;gap:8px;border:1px solid var(--ry-night-line2);border-radius:999px;padding:8px 16px 8px 12px;font-size:15.5px;font-weight:600}
.ry-no .ry-ic{color:var(--ry-night-accent);font-size:16px;stroke-width:3}
.ry-cols{display:grid;grid-template-columns:1fr 1fr;border:1px solid var(--ry-night-line2);border-radius:28px;overflow:hidden;background:var(--ry-night-surface);text-align:left;margin-top:44px}
.ry-col{padding:clamp(22px,3vw,34px)}
.ry-col+.ry-col{border-left:1px dashed var(--ry-night-line2);background:var(--ry-night-surface2)}
.ry-col h3{font-size:24px;margin:2px 0 18px}
.ry-col .ry-k{margin-bottom:14px}
.ry-col ul{list-style:none;margin:0;padding:0;display:grid;gap:13px}
.ry-col li{display:flex;gap:11px;font-size:16.5px;line-height:1.4}
.ry-col li .ry-ic{margin-top:3px;font-size:17px;color:var(--ry-night-accent);stroke-width:2.8}
.ry-col.out li .ry-ic{color:var(--ry-night-warm)}
.ry-col.out .ry-k{color:var(--ry-night-warm)}
.ry-note{margin:22px auto 0;max-width:62ch;border-left:3px solid #C9E64A;padding:4px 0 4px 18px;font-size:16.5px;color:var(--ry-night-muted);text-align:left}
.ry-note a{color:var(--ry-night-accent);white-space:nowrap}

/* plans */
.ry-plans-sec{background:var(--ry-bg)}
.ry-sec-h{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:12px 48px;align-items:end;margin-bottom:40px}
.ry-sec-h .ry-k{grid-column:1/-1}
.ry-sec-h .ry-lead{margin-top:0;justify-self:end}
.ry-pro-g{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.ry-card{position:relative;overflow:hidden;border-radius:30px;border:1px solid var(--ry-line);background:var(--ry-surface);padding:clamp(24px,3.2vw,36px);box-shadow:var(--ry-shadow)}
.ry-card h3{font-size:clamp(26px,2.6vw,32px);margin:0 0 22px}
.ry-card .ry-k{margin-bottom:14px}
.ry-card ul{list-style:none;margin:0;padding:0;display:grid;gap:15px}
.ry-card li{display:flex;gap:12px;font-size:17.5px;line-height:1.4}
.ry-card li .ry-ic{margin-top:4px;font-size:18px;color:var(--ry-olive);stroke-width:3}
.ry-card.pro{border:1px solid #D8C6A5}
.ry-card.pro::before{content:"";position:absolute;left:0;right:0;top:0;height:6px;background:linear-gradient(90deg,#F4EBDD,#D8C6A5 60%,#C9E64A)}
.ry-plan-list{margin-top:16px;border-radius:30px;border:1px solid var(--ry-line);background:var(--ry-surface);overflow:hidden}
.ry-plan{display:grid;grid-template-columns:minmax(0,260px) minmax(0,1fr);gap:8px 28px;padding:24px clamp(22px,3vw,34px);align-items:baseline}
.ry-plan+.ry-plan{border-top:1px solid var(--ry-line)}
.ry-plan h3{font-size:22px}
.ry-plan p{color:var(--ry-muted);font-size:17px}
.ry-plan-f{padding:20px clamp(22px,3vw,34px);background:var(--ry-bg2);border-top:1px solid var(--ry-line);font-size:15px;color:var(--ry-muted);line-height:1.55}

/* closing */
.ry-end{text-align:center;padding:clamp(84px,11vw,150px) 0}
.ry-end .ic{width:104px;height:104px;border-radius:25px;margin:0 auto 30px;box-shadow:0 24px 44px -16px rgba(40,60,0,.6),0 0 0 1px rgba(0,0,0,.1)}
.ry-end h2{max-width:14ch;margin:0 auto 18px;font-size:clamp(40px,6vw,78px)}
.ry-end p.l{font-size:clamp(18px,1.5vw,21px);margin-bottom:30px;color:var(--ry-muted)}
.ry-end .ry-badge{background:transparent}
.ry-conf{position:absolute;inset:0;z-index:-1;pointer-events:none}
.ry-conf i{position:absolute;width:10px;height:18px;border-radius:3px;opacity:.9}

/* footer */
.ry-foot{border-top:1px solid var(--ry-line);background:var(--ry-bg2);padding:44px 0 40px;font-size:16px}
.ry-foot-in{display:grid;grid-template-columns:1.5fr 1fr 1fr;gap:32px}
.ry-foot .ry-brand{font-size:19px;margin-bottom:12px}
.ry-foot p{color:var(--ry-muted);max-width:38ch}
.ry-foot h2{font-family:var(--ry-mono);font-size:12.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--ry-muted);font-weight:600;margin-bottom:12px}
.ry-foot ul{list-style:none;margin:0;padding:0;display:grid;gap:6px}
.ry-foot li a{color:var(--ry-text);text-decoration:none;display:inline-block;padding:4px 0}
.ry-foot li a:hover{text-decoration:underline}
.ry-legal{margin-top:34px;padding-top:20px;border-top:1px solid var(--ry-line);font-size:14px;color:var(--ry-muted);display:flex;gap:8px 28px;flex-wrap:wrap}

/* legal / article */
.ry-art{padding:clamp(28px,4vw,56px) 0 clamp(64px,8vw,110px)}
.ry-art-g{display:grid;grid-template-columns:260px minmax(0,1fr);gap:clamp(32px,5vw,72px);align-items:start}
.ry-toc{position:sticky;top:92px;font-size:15.5px}
.ry-toc .back{display:inline-flex;gap:8px;align-items:center;margin-bottom:26px;color:var(--ry-muted);text-decoration:none;font-weight:600;font-size:15.5px;padding:4px 0}
.ry-toc .back:hover{color:var(--ry-text)}
.ry-toc details{margin:0}
.ry-toc summary{list-style:none;cursor:pointer;font-family:var(--ry-mono);font-size:12.5px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--ry-olive);margin-bottom:14px;display:flex;align-items:center;gap:10px}
.ry-toc summary::-webkit-details-marker{display:none}
.ry-toc summary::before{content:"";width:26px;height:3px;border-radius:3px;background:currentColor}
.ry-toc ol{list-style:none;margin:0;padding:0;border-left:1px solid var(--ry-line2)}
.ry-toc ol ol{border:0;margin:0 0 6px 16px}
.ry-toc a{display:block;padding:6px 0 6px 16px;margin-left:-1px;border-left:2px solid transparent;color:var(--ry-muted);text-decoration:none;line-height:1.35}
.ry-toc a:hover{color:var(--ry-text);border-left-color:var(--ry-hl-b)}
.ry-toc ol ol a{font-size:14.5px;padding:4px 0 4px 14px}
.ry-prose{max-width:70ch;min-width:0}
.ry-prose h1{font-size:clamp(42px,5.6vw,72px);letter-spacing:-.03em;margin:0 0 16px}
.ry-prose .updated{font-family:var(--ry-mono);font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--ry-muted);margin-bottom:30px}
.ry-prose .updated.sub{font-family:var(--ry-body);font-size:20px;text-transform:none;letter-spacing:0}
.ry-prose .summary{background:var(--ry-surface);border:1px solid var(--ry-line);border-left:5px solid var(--ry-hl-b);border-radius:8px 22px 22px 8px;padding:22px 26px;font-size:18.5px;line-height:1.55;margin-bottom:12px;box-shadow:var(--ry-shadow)}
.ry-prose section{margin-top:52px;padding-top:26px;border-top:1px solid var(--ry-line);scroll-margin-top:90px}
.ry-prose h2{font-size:clamp(25px,2.6vw,32px);letter-spacing:-.02em;line-height:1.12;margin:0 0 16px;display:flex;gap:16px;align-items:baseline}
.ry-prose h2 .no{font-family:var(--ry-mono);font-size:13px;letter-spacing:.06em;color:var(--ry-olive);font-weight:600;flex:none;min-width:2.2em}
.ry-prose h3{font-size:21px;letter-spacing:-.01em;margin:30px 0 8px;line-height:1.2}
.ry-prose p,.ry-prose li{font-size:18px;line-height:1.7;text-wrap:pretty}
.ry-prose p{margin:0 0 18px}
.ry-prose ul{padding-left:22px;margin:0 0 18px}
.ry-prose strong{font-weight:700}
.ry-prose a{word-break:break-word}
.ry-prose .contact{font-size:24px;font-weight:700;font-family:var(--ry-display)}
.ry-prose .end{margin-top:56px;padding:24px 28px;border:1px dashed var(--ry-line2);border-radius:22px;display:flex;justify-content:space-between;gap:16px 24px;align-items:center;flex-wrap:wrap;font-size:17px}

/* responsive */
@media (max-width:1060px){
.ry-hero-in{grid-template-columns:1fr;gap:44px}
.ry-stage{justify-self:center}
.ry-two{grid-template-columns:1fr}
.ry-two.flip>:first-child{order:0}
.ry-sec-h{grid-template-columns:1fr}.ry-sec-h .ry-lead{justify-self:start}
.ry-spec ul{grid-template-columns:repeat(2,1fr)}
.ry-spec li:nth-child(3){border-left:0;padding-left:0}.ry-spec li:nth-child(n+3){border-top:1px solid var(--ry-line)}
.ry-art-g{grid-template-columns:1fr;gap:28px}
.ry-toc{position:static;border:1px solid var(--ry-line);border-radius:20px;padding:18px 20px;background:var(--ry-surface)}
.ry-toc summary{margin-bottom:0}
.ry-toc details[open] summary{margin-bottom:14px}
.ry-foot-in{grid-template-columns:1fr 1fr}.ry-foot-in>:first-child{grid-column:1/-1}
}
@media (max-width:760px){
.ry-nav a.opt{display:none}
.ry-pro-g,.ry-cols{grid-template-columns:1fr}
.ry-col+.ry-col{border-left:0;border-top:1px dashed var(--ry-night-line2)}
.ry-plan{grid-template-columns:1fr}
.ry-fly{display:none}
.ry-prose h2{flex-direction:column;gap:6px}
.ry-foot-in{grid-template-columns:1fr}
.ry-top-in{gap:8px}
.ry-brand{font-size:19px}
.ry-nav a{padding:9px 10px}
}
@media (min-width:1061px){.ry-toc summary{pointer-events:none;cursor:default}}
.ry-toc summary::after{content:"";margin:-4px 4px 0 auto;width:9px;height:9px;border-right:2px solid currentColor;border-bottom:2px solid currentColor;transform:rotate(45deg);flex:none}
.ry-toc details[open] summary::after{transform:rotate(225deg);margin-top:4px}
@media (min-width:1061px){.ry-toc summary::after{display:none}}
@media (max-width:1060px){.ry-stage{--ry-s:.6}.ry-sun{top:auto;bottom:170px;right:-90px;width:340px}}
@media (max-width:560px){
.ry-stage{--ry-s:.5;width:100%;max-width:420px}
.ry-stage .a{right:auto;left:calc(412px*var(--ry-s)*.8)}
.ry-chip.c1{display:none}.ry-chip.c2{left:0;top:-4px;transform:scale(.85);transform-origin:left top}
.ry-hero h1{font-size:clamp(46px,14.5vw,64px)}
.ry-mid .ry-fit{--s:.74}
.ry-spec li{padding:22px 16px}
.ry-badge{font-size:16px}
}
@media (max-width:560px){.ry-conf i:nth-child(n+9){display:none}.ry-conf i{opacity:.5}}
@media (max-width:420px){.ry-stage{--ry-s:.45}.ry-mid .ry-fit{--s:.7}}
@media (max-width:375px){.ry-stage{--ry-s:.43}}
@media (max-width:360px){.ry-stage{--ry-s:.41}}
@media (max-width:340px){.ry-stage{--ry-s:.375}.ry-mid .ry-fit{--s:.62}}

@media (prefers-reduced-motion:no-preference){
.ry-hero .ry-card-s.front{animation:ry-sw 7s cubic-bezier(.3,.7,.2,1) -3.2s infinite}
.ry-hero .ry-stamp{animation:ry-st 7s ease -3.2s infinite}
.ry-conf i{animation:ry-fall 9s ease-in-out infinite}
@keyframes ry-sw{0%,8%{transform:translateX(0) rotate(0)}38%,62%{transform:translateX(36px) rotate(7deg)}82%,100%{transform:translateX(0) rotate(0)}}
@keyframes ry-st{0%,14%{opacity:0;transform:rotate(-14deg) scale(1.5)}34%,64%{opacity:1;transform:rotate(-14deg) scale(1)}80%,100%{opacity:0;transform:rotate(-14deg) scale(1)}}
@keyframes ry-fall{0%,100%{translate:0 0}50%{translate:0 14px}}
}
@media print{.ry-top,.ry-stage{display:none}}

.ry-finepill{display:inline-block;background:var(--ry-surface);border:1px solid var(--ry-line);border-radius:999px;padding:6px 14px}
'''

SPRITE = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
<defs>
<linearGradient id="ry-g1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFD66B"/><stop offset="1" stop-color="#FF8A5B"/></linearGradient>
<linearGradient id="ry-g2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE3C2"/><stop offset="1" stop-color="#F08A7A"/></linearGradient>
<linearGradient id="ry-g3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E4F4DF"/><stop offset="1" stop-color="#8CCFAE"/></linearGradient>
<linearGradient id="ry-g4" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F6E7B6"/><stop offset="1" stop-color="#D3B873"/></linearGradient>
<linearGradient id="ry-h1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3F7F4F"/><stop offset="1" stop-color="#2F6B4F"/></linearGradient>
<linearGradient id="ry-h2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8CBF5A"/><stop offset="1" stop-color="#5E9A48"/></linearGradient>
<linearGradient id="ry-h3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#C98A52"/><stop offset="1" stop-color="#9C6238"/></linearGradient>
</defs>
<symbol id="ry-ph1" viewBox="0 0 300 300" preserveAspectRatio="xMidYMid slice"><rect width="300" height="300" fill="url(#ry-g1)"/><circle cx="214" cy="86" r="44" fill="#FFF6D6"/><path d="M0 300V190L96 90l78 92 44-42 82 96v-0V300z" fill="url(#ry-h2)"/><path d="M0 300V248l84-72 92 124z" fill="url(#ry-h1)"/></symbol>
<symbol id="ry-ph2" viewBox="0 0 300 300" preserveAspectRatio="xMidYMid slice"><rect width="300" height="300" fill="url(#ry-g2)"/><circle cx="92" cy="104" r="38" fill="#FFF3DF"/><path d="M0 300V210l70-48 80 70 60-56 90 66V300z" fill="url(#ry-h3)"/><path d="M0 300V256l110-44 190 52V300z" fill="url(#ry-h1)"/></symbol>
<symbol id="ry-ph3" viewBox="0 0 300 300" preserveAspectRatio="xMidYMid slice"><rect width="300" height="300" fill="url(#ry-g3)"/><circle cx="232" cy="64" r="30" fill="#FFFBE6"/><path d="M0 300V170l60-60 70 80 54-40 116 90V300z" fill="url(#ry-h2)"/><path d="M0 300V240l100-60 120 120z" fill="url(#ry-h1)"/></symbol>
<symbol id="ry-ph4" viewBox="0 0 300 300" preserveAspectRatio="xMidYMid slice"><rect width="300" height="300" fill="url(#ry-g4)"/><circle cx="150" cy="120" r="50" fill="#FFF6D6"/><path d="M0 300V224l90-50 70 60 70-68 70 56V300z" fill="url(#ry-h2)"/><path d="M0 300V262l150-44 150 50V300z" fill="url(#ry-h1)"/></symbol>
<symbol id="ry-i-check" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></symbol>
<symbol id="ry-i-x" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></symbol>
<symbol id="ry-i-undo" viewBox="0 0 24 24"><path d="M9 14L4 9l5-5"/><path d="M4 9h10.5a5.5 5.5 0 010 11H11"/></symbol>
<symbol id="ry-i-play" viewBox="0 0 24 24"><path d="M8 5.2v13.6a.6.6 0 00.9.5l10.6-6.8a.6.6 0 000-1L8.9 4.7a.6.6 0 00-.9.5z" fill="currentColor" stroke="none"/></symbol>
<symbol id="ry-i-shuffle" viewBox="0 0 24 24"><path d="M16 4h4v4M4 20L20 4M20 16v4h-4M14.5 14.5L20 20M4 4l5 5"/></symbol>
<symbol id="ry-i-copy" viewBox="0 0 24 24"><rect x="8" y="8" width="12" height="12" rx="3"/><path d="M16 8V6a2 2 0 00-2-2H6a2 2 0 00-2 2v8a2 2 0 002 2h2"/></symbol>
<symbol id="ry-i-stack" viewBox="0 0 24 24"><path d="M7 4.5h10"/><rect x="4" y="8" width="16" height="12" rx="2.5"/><path d="M4.5 17l4-4 3.5 3.5 2.5-2.5 5 4.5"/></symbol>
<symbol id="ry-i-film" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M8 5v14M16 5v14M3 9.5h5M3 14.5h5M16 9.5h5M16 14.5h5"/></symbol>
<symbol id="ry-i-phone" viewBox="0 0 24 24"><rect x="6.5" y="2.5" width="11" height="19" rx="3"/><path d="M10.5 18.5h3"/></symbol>
<symbol id="ry-i-person" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="4.5"/><circle cx="12" cy="10" r="3"/><path d="M6.5 19c.8-3 3-4.5 5.5-4.5s4.700 1.500 5.500 4.500"/></symbol>
<symbol id="ry-i-live" viewBox="0 0 24 24"><circle cx="12" cy="12" r="2.6"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="9.5" stroke-dasharray="1.2 3.1"/></symbol>
<symbol id="ry-i-flame" viewBox="0 0 24 24"><path d="M12 3c.6 3.600 5.500 5.600 5.500 10.500a5.500 5.500 0 01-11 0c0-2.200 1-3.700 2.200-4.800.3 1.600 1 2.300 2 2.600C10.400 8.600 10.800 5.800 12 3z" fill="currentColor" stroke="none"/></symbol>
<symbol id="ry-i-down" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7.500v8M8.500 12.500l3.500 3.500 3.500-3.500"/></symbol>
<symbol id="ry-i-checkc" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M8 12.300l3 3 5-5.800"/></symbol>
<symbol id="ry-i-gear" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3.200"/><path d="M12 2.800v3M12 18.200v3M2.800 12h3M18.200 12h3M5.500 5.500l2.100 2.100M16.400 16.400l2.100 2.100M5.500 18.500l2.100-2.100M16.400 7.600l2.100-2.100"/></symbol>
<symbol id="ry-i-bolt" viewBox="0 0 24 24"><path d="M13.500 2L5 13.500h6L10 22l9-12h-6z" fill="currentColor" stroke="none"/></symbol>
<symbol id="ry-i-trash" viewBox="0 0 24 24"><path d="M4 7h16M9 7V4.500h6V7M6 7l1 13h10l1-13M10 11v6M14 11v6"/></symbol>
<symbol id="ry-i-shield" viewBox="0 0 24 24"><path d="M12 3l7.500 3v5.500c0 4.800-3.200 8.300-7.500 9.800-4.300-1.500-7.500-5-7.500-9.800V6z"/><path d="M8.500 12.300l2.500 2.500 4.500-5"/></symbol>
<symbol id="ry-i-hand" viewBox="0 0 24 24"><path d="M3.500 12h17M8 7.500L3.500 12 8 16.500M16 7.500l4.500 4.500-4.500 4.500"/></symbol>
<symbol id="ry-i-share" viewBox="0 0 24 24"><path d="M12 15V4M8 8l4-4 4 4M5 12v7.500h14V12"/></symbol>
<symbol id="ry-i-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2.500v2.500M12 19v2.500M2.500 12H5M19 12h2.500M5.300 5.300l1.800 1.800M16.900 16.900l1.800 1.800M5.300 18.700l1.800-1.800M16.900 7.100l1.800-1.800"/></symbol>
<symbol id="ry-i-seal" viewBox="0 0 24 24"><path d="M12 2.500l2.300 1.700 2.800-.1.900 2.700 2.300 1.600-.9 2.700.9 2.700-2.300 1.600-.9 2.700-2.800-.1L12 21.500l-2.300-1.700-2.800.1-.9-2.700-2.300-1.600.9-2.700-.9-2.700 2.300-1.600.9-2.700 2.800.1z" fill="currentColor" stroke="none"/><path d="M8.300 12.200l2.500 2.500 4.800-5" stroke="#15190A" stroke-width="2.200"/></symbol>
<symbol id="ry-i-photo" viewBox="0 0 24 24"><rect x="3" y="4.500" width="18" height="15" rx="3"/><circle cx="9" cy="10" r="1.600"/><path d="M4 17l5-4.500 3.500 3 3-2.500 4.500 4"/></symbol>
<symbol id="ry-i-vid" viewBox="0 0 24 24"><rect x="3" y="6" width="13" height="12" rx="3"/><path d="M16 10.500l5-3v9l-5-3"/></symbol>
<symbol id="ry-i-cloudoff" viewBox="0 0 24 24"><path d="M7 18a4 4 0 01-.4-8A6 6 0 0118 10.500a3.800 3.800 0 01-.5 7.500H7z"/><path d="M3.500 3.500l17 17"/></symbol>
<symbol id="ry-i-chev" viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></symbol>
<symbol id="ry-i-arrow" viewBox="0 0 24 24"><path d="M4 12h15M13 6l6 6-6 6"/></symbol>
<symbol id="ry-i-lock" viewBox="0 0 24 24"><rect x="5" y="10.500" width="14" height="10" rx="3"/><path d="M8 10.500V8a4 4 0 018 0v2.500"/></symbol>
</svg>'''

# ------------------------------------------------------------------ small builders
def I(n, cls=''):
    return f'<svg class="ry-ic{" " + cls if cls else ""}" aria-hidden="true" focusable="false"><use href="#ry-i-{n}"/></svg>'


def PH(n):
    return f'<svg class="ry-ph" aria-hidden="true" focusable="false"><use href="#ry-ph{n}"/></svg>'


SB = ('<div class="ry-sb"><span>9:41</span><svg viewBox="0 0 66 13" aria-hidden="true"><g fill="#F4EFE3"><rect x="0" y="8" width="3" height="5" rx="1"/>'
      '<rect x="5" y="5.5" width="3" height="7.5" rx="1"/><rect x="10" y="3" width="3" height="10" rx="1"/><rect x="15" y="0" width="3" height="13" rx="1"/></g>'
      '<path d="M25 4.5a7 7 0 0110 0M27.5 7.2a3.7 3.7 0 015 0" stroke="#F4EFE3" stroke-width="1.7" fill="none" stroke-linecap="round"/>'
      '<circle cx="30" cy="10.5" r="1.5" fill="#F4EFE3"/><rect x="41.5" y=".5" width="22" height="12" rx="3.5" fill="none" stroke="#F4EFE3" opacity=".5"/>'
      '<rect x="43.5" y="2.5" width="16" height="8" rx="2" fill="#F4EFE3"/></svg></div>')


def device(cls, screen, label):
    return (f'<figure class="ry-fit {cls}" role="img" aria-label="{label}"><div class="ry-dev" aria-hidden="true"><div class="ry-bz"><div class="ry-scr">'
            f'<div class="ry-isl"></div>{SB}{screen}<div class="ry-hi"></div></div></div></div></figure>')


def screen_home():
    return f'''<div class="ry-pad">
<div class="ry-hh"><div><div class="t">Roomy</div><div class="g">Good morning &#9728;&#65039;</div></div><div class="ry-hb"><span class="ry-gear">{I('gear')}</span></div></div>
<div class="ry-card2"><div class="ry-stor"><div class="ry-ring"><svg viewBox="0 0 92 92"><circle cx="46" cy="46" r="40" fill="none" stroke="#3A3226" stroke-width="12"/><circle cx="46" cy="46" r="40" fill="none" stroke="#F2545B" stroke-width="12" stroke-linecap="round" stroke-dasharray="234 252"/></svg><div class="c"><b>93%</b><small>used</small></div></div>
<div style="min-width:0"><div class="h5">18.4 GB free</div><p>of 256 GB on this iPhone</p><hr><div class="mm"><span>{I('photo')} 14,820</span><span>{I('vid')} 612</span></div></div></div></div>
<div class="ry-start"><div class="h"><div><div class="h5">Start swiping</div><p>1,248 photos &amp; videos left to review</p></div><span class="hand">{I('hand')}</span></div>
<span class="ch">{I('bolt', 'f')} 50 free swipes left</span>
<div class="bt"><span class="go">{I('play')} Let&rsquo;s go</span><span class="sf">{I('shuffle')}</span></div></div>
<div class="ry-stats"><div class="ry-st"><span style="color:#3BD9A5">{I('down')}</span><b>2.4 GB</b><span>Freed</span></div><div class="ry-st"><span style="color:#C9E64A">{I('checkc')}</span><b>318</b><span>Reviewed</span></div><div class="ry-st"><span style="color:#FF8A3D">{I('flame', 'f')}</span><b>6</b><span>Day streak</span></div></div>
<div class="ry-sh"><div class="h5">Smart Cleanup</div><p>Find the biggest wins in seconds</p></div>
<div class="ry-cg"><div class="ry-ctile"><div class="tp"><span class="ry-it c">{I('copy')}</span></div><div><b>Duplicates</b><span class="s">Tap to scan</span></div></div>
<div class="ry-ctile"><div class="tp"><span class="ry-it p">{I('stack')}</span></div><div><b>Similar Photos</b><span class="s">3 groups found</span></div></div></div></div>'''


def screen_swipe(var='keep'):
    if var == 'del':
        front = f'<div class="ry-card-s front del">{PH(2)}<div class="sc"></div><span class="lv">{I("person")} Selfie</span><span class="ry-stamp d">DELETE</span></div>'
        back = f'<div class="ry-card-s back">{PH(4)}</div>'
    else:
        front = f'<div class="ry-card-s front">{PH(1)}<div class="sc"></div><span class="lv">{I("live")} Live</span><span class="ry-stamp k">KEEP</span></div>'
        back = f'<div class="ry-card-s back">{PH(3)}</div>'
    return f'''<div class="ry-sw-top"><span class="ry-circ">{I('x')}</span><span class="n">12 of 64</span><span class="tr"><span class="ry-circ">{I('trash')}</span><em>3</em></span></div>
<div class="ry-prog"><i></i></div>
<div class="ry-deck">{back}{front}</div>
<div class="ry-sw-btn"><span class="ry-rb x rb">{I('x', 'b')}</span><span class="ry-rb u rb">{I('undo')}</span><span class="ry-rb k rb">{I('check', 'b')}</span></div>
<div class="ry-sw-foot"><b>{I('bolt', 'f')} 45 free swipes left</b><br>Nothing is deleted until you confirm in the Trash.</div>'''


def screen_similar():
    def grp(n, a):
        return (f'<div class="ry-grp"><div class="gh"><span>3 photos</span><span>Aug 14</span></div><div class="tt">'
                f'<div class="ry-th">{PH(a)}<span class="bst">Best</span></div>'
                f'<div class="ry-th sel">{PH(a)}<span class="ck">{I("check", "b")}</span></div>'
                f'<div class="ry-th sel">{PH(n)}<span class="ck">{I("check", "b")}</span></div></div></div>')
    return f'''<div class="ry-nv" style="position:relative"><span>{I('chev')}</span><span style="font-size:17px">Back</span><span class="tt">Similar Photos</span></div>
<div class="ry-sim-h"><div class="h5">3 groups found</div><p>We picked the best photo in each group (marked &ldquo;Best&rdquo;). The rest are selected for deletion.</p></div>
{grp(4, 1)}{grp(2, 2)}{grp(3, 3)}
<div class="ry-bot"><div class="dl">Delete 6 &middot; 41 MB</div></div>'''


def screen_trash():
    cells = ''.join(f'<div class="c">{PH(n)}<b>{I("check", "b")}</b></div>' for n in [4, 2, 3, 1, 3, 2, 1, 4, 2, 3, 4, 1])
    return f'''<div class="ry-sw-top"><span class="ry-circ">{I('x')}</span><span class="n">Trash</span><span class="ry-circ" style="visibility:hidden"></span></div>
<div class="ry-trh" style="margin-top:12px"><div class="h5">12 items &middot; 38 MB</div><p>Tap a photo to keep it. Long-press to preview.</p></div>
<div class="ry-tgrid">{cells}</div>
<div class="ry-trnote">Deleted items go to Photos &rsaquo; Recently Deleted for 30 days.</div>
<div class="ry-bot"><div class="dl">Delete 12 &middot; 38 MB</div></div>'''


FP_PATTERN = '1001010101000101010111101001010101101010100010110101110101001001'


def fp_grid():
    return '<div class="grid">' + ''.join(f'<i class="o"></i>' if c == '1' else '<i></i>' for c in FP_PATTERN) + '</div>'


def conf(n=18):
    cols = ['#3BD9A5', '#F2545B', '#15190A', '#FFFFFF', '#FF8A3D']
    out = ''
    for k in range(n):
        left = (5 + (k * 13) % 17) if k % 2 == 0 else (80 + (k * 11) % 16)
        top = 6 + (k * 29) % 84
        out += (f'<i style="left:{left}%;top:{top}%;background:{cols[k % 5]};transform:rotate({(k * 47) % 180}deg);animation-delay:-{(k * 7) % 9}s"></i>')
    return f'<div class="ry-conf" aria-hidden="true">{out}</div>'


HILLS = ('<svg class="ry-hills" viewBox="0 0 1440 280" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path class="far" d="M0 120 L200 40 L420 130 L620 60 L880 150 L1100 50 L1440 140 V280 H0Z"/>'
         '<path class="mid" d="M0 190 L260 100 L520 200 L760 120 L1020 210 L1260 120 L1440 180 V280 H0Z"/><path class="near" d="M0 250 Q360 190 720 240 T1440 220 V280 H0Z"/></svg>')


def badge():
    return '<span class="ry-badge" aria-disabled="true"><i aria-hidden="true"></i>Coming soon to the App Store</span>'


# ------------------------------------------------------------------ shell (head, nav, footer)
class Ctx:
    def __init__(self, base, key):
        self.base = base            # '' on /roomy/…, '../' on /roomy/privacy/
        self.key = key
        self.home = './' if base == '' else '../'

    def m(self, f): return f'{self.base}media/{f}'
    def p(self, k): return f'{self.base}{k}.html'


def nav(c):
    if c.key == 'index':
        items = [('#swipe', 'Swipe', True), ('#cleanup', 'Clean-up', True), ('#private', 'Private', True), ('#pro', 'Roomy Pro', True),
                 (c.p('privacy'), 'Privacy', False), (c.p('support'), 'Support', False)]
        links = ''.join(f'<a href="{h}"{"" if not opt else " class=opt"}>{t}</a>' for h, t, opt in items)
    else:
        links = ''.join(f'<a href="{c.p(k)}"{" aria-current=page" if k == c.key else ""}>{t}</a>'
                        for k, t in (('privacy', 'Privacy'), ('terms', 'Terms'), ('support', 'Support')))
    return (f'<header class="ry-top"><div class="ry-wrap ry-top-in"><a class="ry-brand" href="{c.home}"><img src="{c.m("icon-180.png")}" width="34" height="34" alt="">Roomy</a>'
            f'<nav class="ry-nav" aria-label="Roomy">{links}</nav></div></header>')


def footer(c):
    return f'''<footer class="ry-foot"><div class="ry-wrap"><div class="ry-foot-in">
<div><a class="ry-brand" href="{c.home}"><img src="{c.m("icon-180.png")}" width="34" height="34" alt="" loading="lazy">Roomy</a><p>Roomy: Swipe Photo Cleaner. Swipe your storage back, privately, on your iPhone.</p></div>
<nav aria-label="Roomy pages"><h2>Roomy</h2><ul><li><a href="{c.p('privacy')}">Privacy</a></li><li><a href="{c.p('terms')}">Terms</a></li><li><a href="{c.p('support')}">Support</a></li></ul></nav>
<div><h2>Contact</h2><ul><li><a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a></li></ul></div></div>
<div class="ry-legal"><span>Roomy is made by Izotz Cristobal Mota.</span><span>Coming soon to the App Store. Made for iPhone, iOS 17 or later.</span><span>iPhone is a trademark of Apple Inc.</span></div></div></footer>'''


def shell(c, title, desc, canon, main, js=''):
    css = CSS.replace('@LIGHT_ROOT@', ':root{' + decl(LIGHT) + ';color-scheme:light dark}').replace('@DARK_ROOT@', ':root{' + decl(DARK) + '}')
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#FBF8EF" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#16120E" media="(prefers-color-scheme: dark)">
<link rel="canonical" href="{canon}">
<link rel="icon" type="image/png" href="{c.m("icon-180.png")}">
<link rel="apple-touch-icon" href="{c.m("icon-180.png")}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://seizeapps.com/roomy/media/icon-512.png">
<meta name="twitter:card" content="summary">
<style>{css}</style>
</head>
<body>
<a class="ry-skip" href="#main">Skip to content</a>
{SPRITE}
{nav(c)}
{main}
{footer(c)}
{js}
</body>
</html>
'''


# ------------------------------------------------------------------ home
def home(c):
    li = lambda ic, t, d: f'<li><span class="ic">{I(ic)}</span><div><b>{t}</b><span class="d">{d}</span></div></li>'
    h = f'<main id="main">'
    h += f'''<div class="ry-heroholder"><section class="ry-hero" aria-labelledby="ry-h-hero"><span class="ry-sun" aria-hidden="true"></span>{HILLS}
<div class="ry-wrap ry-hero-in"><div>
<div class="ry-brandrow"><img src="{c.m("icon-180.png")}" width="60" height="60" alt="Roomy app icon"><span>Roomy: Swipe Photo Cleaner</span></div>
<h1 id="ry-h-hero">Swipe your <span class="ry-mark">storage</span> back.</h1>
<p class="ry-lead">Storage full again? Roomy turns cleaning your camera roll into a quick, satisfying swipe: left to delete, right to keep.</p>
<div class="ry-hero-row">{badge()}<p class="ry-fact">{I('lock')}Photos stay on your iPhone</p></div></div>
<div><div class="ry-stage">
{device('a', screen_swipe(), 'Illustration of the Roomy swipe screen: a sunset photo with a KEEP stamp')}
{device('b', screen_home(), 'Illustration of the Roomy home screen: storage, the Start swiping card and Smart Cleanup')}
<div class="ry-chip c2"><span class="ic" style="background:rgba(59,217,165,.16);color:#3BD9A5">{I('down')}</span><div><span class="s">Freed</span><b>2.4 GB</b></div></div>
<div class="ry-chip c1"><span class="ic" style="background:rgba(255,138,61,.16);color:#FF8A3D">{I('flame', 'f')}</span><div><span class="s">Day streak</span><b>6</b></div></div>
</div><p class="ry-fine"><span class="ry-finepill">Illustrations of the app, drawn with sample data.</span></p></div></div></section></div>
<section class="ry-spec" aria-label="Roomy at a glance"><div class="ry-wrap"><ul>
<li><span class="n">50</span><span class="t">free swipes every day. Undoing a swipe gives one back.</span></li>
<li><span class="n">30<u>days</u></span><span class="t">in Photos &rsaquo; Recently Deleted before anything is gone for good.</span></li>
<li><span class="n">Never</span><span class="t">uploaded: your photos are analyzed on your iPhone.</span></li>
<li><span class="n">12</span><span class="t">localizations, from English to Japanese and Portuguese.</span></li></ul></div></section>'''
    # swipe (lime)
    h += f'''<section class="ry-band ry-lime" id="swipe" aria-labelledby="ry-h-swipe"><div class="ry-wrap ry-two">
<div class="ry-mid"><span class="ry-fly l" aria-hidden="true">{PH(2)}<span class="ry-stamp d">DELETE</span></span><span class="ry-fly r" aria-hidden="true">{PH(3)}<span class="ry-stamp k">KEEP</span></span>
{device('', screen_swipe('del'), 'Illustration of the Roomy swipe screen with a DELETE stamp on a photo swiped left')}</div>
<div><p class="ry-k">Swipe to clean</p><h2 class="ry-h" id="ry-h-swipe">Left to delete. Right to keep.</h2>
<p class="ry-lead">One photo at a time, one quick swipe each. Undo steps back one swipe at a time.</p>
<ul class="ry-list">
{li('stack', 'Month by month', 'Clean one month at a time, revisit &ldquo;On This Day&rdquo; memories, or shuffle.')}
{li('person', 'A pile for each kind', 'Screenshots, selfies and Live Photos each get their own pile.')}
{li('flame', 'See what you&rsquo;ve freed', 'See how much space you&rsquo;ve freed, keep a daily streak and share your result. The share image has no photos in it.')}
</ul></div></div></section>'''
    # safe
    h += f'''<section class="ry-band ry-safe" id="safe" aria-labelledby="ry-h-safe"><div class="ry-wrap ry-two flip">
<div class="ry-mid">{device('', screen_trash(), 'Illustration of the Roomy Trash with twelve photos waiting to be deleted')}</div>
<div><p class="ry-k">Safe by default</p><h2 class="ry-h" id="ry-h-safe">Nothing goes until you say so.</h2>
<p class="ry-lead">Swiping left only moves a photo to Roomy&rsquo;s Trash. It is a suggestion, not a deletion.</p>
<ol class="ry-steps">
<li class="go"><div><b>Swipe left</b><span class="d">The photo moves to Roomy&rsquo;s Trash. Your library is untouched. Nothing is deleted until you confirm in the Trash.</span></div></li>
<li><div><b>Review the Trash</b><span class="d">Rescue photos you want to keep, and delete the rest for good.</span></div></li>
<li class="ok"><div><b>Confirm</b><span class="d">Nothing is deleted until you empty the Trash, and iOS asks you to confirm.</span></div></li>
<li><div><b>30 days of grace</b><span class="d">Deleted items go to Photos &rsaquo; Recently Deleted, where iOS keeps them for 30 days.</span></div></li></ol></div></div></section>'''
    # cleanup (night)
    h += f'''<section class="ry-band ry-night ry-cleanup" id="cleanup" aria-labelledby="ry-h-clean"><div class="ry-wrap ry-two">
<div><p class="ry-k">On your iPhone</p><h2 class="ry-h" id="ry-h-clean">Smart cleanup finds the clutter.</h2>
<p class="ry-lead">Duplicates, near-identical shots and heavy videos, found and sorted for you.</p>
<ul class="ry-list">
{li('copy', 'Duplicates', 'Finds exact copies across your library.')}
{li('stack', 'Similar shots', 'Groups bursts and near-identical photos and marks the best one to keep.')}
{li('film', 'Large videos', 'Sorted by size, so you see what&rsquo;s really taking up space.')}
</ul>
<div class="ry-fpbox" role="group" aria-label="Illustration: an original photo and its copy share the same visual fingerprint"><div class="ry-fp ry-ui" aria-hidden="true">
<figure><div class="pic">{PH(1)}</div>{fp_grid()}<figcaption>Original</figcaption></figure><span class="eq">=</span>
<figure><div class="pic">{PH(1)}</div>{fp_grid()}<figcaption>Copy</figcaption></figure>
<span class="ry-match ry-ui">{I('check', 'b')} Duplicate</span></div>
<p class="ry-cap">Roomy compares a small visual fingerprint of each photo, on your iPhone.</p></div></div>
<div class="ry-mid">{device('', screen_similar(), 'Illustration of Roomy Similar Photos: three groups with the best photo of each marked Best')}
<span class="ry-float" style="left:-2%;top:-1%">{I('stack')}3 groups found</span><span class="ry-float" style="right:0;bottom:14%;background:#3BD9A5">{I('check', 'b')}Best</span></div></div></section>'''
    # compress
    h += f'''<section class="ry-band ry-compress" id="compress" aria-labelledby="ry-h-comp"><div class="ry-wrap ry-two flip">
<div><div class="ry-sheetwrap"><div class="ry-vid ry-ui" role="img" aria-label="Illustration of Roomy compressing a large video: three sizes and a smaller copy">
<div class="ry-vl" aria-hidden="true">
<div class="ry-vr"><span class="th">{PH(2)}</span><div class="m"><b>0:48 &middot; 3840&times;2160</b><div class="bar"><i style="width:100%"></i></div></div><span class="sz">1.8 GB</span></div>
<div class="ry-vr"><span class="th">{PH(3)}</span><div class="m"><b>2:15 &middot; 1920&times;1080</b><div class="bar"><i style="width:62%"></i></div></div><span class="sz">1.1 GB</span></div>
<div class="ry-vr"><span class="th">{PH(4)}</span><div class="m"><b>0:32 &middot; 1920&times;1080</b><div class="bar"><i style="width:34%"></i></div></div><span class="sz">612 MB</span></div></div>
<div class="ry-sheet" aria-hidden="true"><div class="h4">Compress video</div><div class="ry-seg"><span>High</span><span class="on">Medium</span><span>Small</span></div>
<div class="ry-cmp"><div class="o"><span>Original</span><i></i></div><div class="n"><span>Copy</span><i></i></div></div><div class="ry-go">{I('film')} Compress video</div></div></div></div>
<p class="ry-cap">Illustration, drawn with sample data.</p></div>
<div><p class="ry-k">Compress big videos</p><h2 class="ry-h" id="ry-h-comp">Big videos, smaller.</h2>
<p class="ry-proline"><span class="ry-pearl">PRO</span><span>Compressing is part of Roomy Pro.</span></p>
<p class="ry-lead">Pick High, Medium or Small quality. Roomy saves a smaller copy that keeps the original date and location, and replaces the original only once you allow it.</p>
<ul class="ry-list">
{li('check', 'Only if it&rsquo;s worth it', 'The original is replaced only when the copy is at least 10 percent smaller; otherwise it is left untouched.')}
{li('film', 'Free to review', 'Reviewing large videos and deleting them one by one is free.')}
</ul></div></div></section>'''
    # private (night)
    h += f'''<section class="ry-band ry-night ry-private" id="private" aria-labelledby="ry-h-priv"><div class="ry-wrap">
<div class="ry-orbit" aria-hidden="true"><i></i><i></i><i></i><img src="{c.m("icon-256.png")}" width="102" height="102" alt="" loading="lazy">
<span class="dot d1">{I('lock')}</span><span class="dot d2">{I('cloudoff')}</span><span class="dot d3">{I('shield')}</span></div>
<p class="ry-k">Private by design</p><h2 class="ry-h" id="ry-h-priv">Your photos never leave your iPhone.</h2>
<p class="ry-lead">Your photos are analyzed on your iPhone and never uploaded.</p>
<ul class="ry-no" aria-label="What Roomy does not have"><li>{I('check')} No ads</li><li>{I('check')} No account</li><li>{I('check')} No tracking</li><li>{I('check')} No AI service</li><li>{I('check')} No server of ours</li></ul>
<div class="ry-cols"><div class="ry-col in"><p class="ry-k">Stays on your iPhone</p><h3>Everything about your photos.</h3><ul>
<li>{I('check')}<span>Your photos and videos, and their metadata</span></li><li>{I('check')}<span>The visual fingerprints used to find duplicates and similar shots</span></li><li>{I('check')}<span>Your review progress and cleanup statistics</span></li></ul></div>
<div class="ry-col out"><p class="ry-k">Leaves your iPhone</p><h3>Purchase bookkeeping.</h3><ul>
<li>{I('arrow')}<span>An anonymous ID and your iPhone&rsquo;s vendor identifier</span></li><li>{I('arrow')}<span>Your Roomy purchases</span></li><li>{I('arrow')}<span>Which screen led you to the purchase screen</span></li></ul></div></div>
<p class="ry-note">Roomy uses RevenueCat for purchase analytics; RevenueCat never receives your photos, your name or your email. <a href="{c.p('privacy')}">Read the privacy policy</a></p></div></section>'''
    # plans
    chk = lambda t: f'<li>{I("check")}<span>{t}</span></li>'
    h += f'''<section class="ry-band ry-plans-sec" id="pro" aria-labelledby="ry-h-pro"><div class="ry-wrap">
<div class="ry-sec-h"><p class="ry-k">Free &amp; Roomy Pro</p><h2 class="ry-h" id="ry-h-pro">Free to start. Pro when you want more.</h2>
<p class="ry-lead">Prices vary by country and are shown in the app before you buy.</p></div>
<div class="ry-pro-g"><div class="ry-card"><p class="ry-k">What&rsquo;s free</p><h3>Start swiping today.</h3><ul>
{chk('50 swipes every day (undoing a swipe gives it back)')}{chk('The Trash: review it, rescue photos, delete the rest for good')}{chk('Finding duplicates, similar shots and screenshots')}{chk('Reviewing large videos and deleting them one by one')}</ul></div>
<div class="ry-card pro"><p class="ry-k"><span class="ry-pearl">PRO</span> What Roomy Pro adds</p><h3>Do it all in a few taps.</h3><ul>
{chk('Unlimited swipes')}{chk('Delete duplicates and similar shots in one tap')}{chk('Compress big videos')}</ul></div></div>
<div class="ry-plan-list"><div class="ry-plan"><h3>Roomy Pro Weekly</h3><p>Auto-renewing subscription, renews every week.</p></div>
<div class="ry-plan"><h3>Roomy Pro Yearly</h3><p>Auto-renewing subscription, renews every year. Starts with a 3-day free trial for eligible new subscribers.</p></div>
<div class="ry-plan"><h3>Roomy Pro Lifetime</h3><p>One-time purchase, no subscription.</p></div>
<p class="ry-plan-f">Payment is charged to your Apple Account at confirmation of purchase. Subscriptions renew automatically unless auto-renew is turned off at least 24 hours before the end of the current period. Manage or cancel your subscription in your App Store account settings. Any unused portion of a free trial is forfeited when you purchase a subscription. Details in the <a href="{c.p('terms')}">Terms of Use</a>.</p></div></div></section>'''
    # closing CTA
    h += f'''<section class="ry-band ry-lime ry-end" aria-labelledby="ry-h-end">{conf()}<div class="ry-wrap">
<img class="ic" src="{c.m("icon-256.png")}" width="104" height="104" alt="Roomy app icon" loading="lazy">
<h2 id="ry-h-end">Your iPhone is full. Let&rsquo;s fix that.</h2><p class="l">Left to delete, right to keep.</p>{badge()}</div></section></main>'''
    return h

# ------------------------------------------------------------------ legal pages (privacy, terms, support)
def _kicker(key):
    return {'privacy': 'Privacy policy', 'terms': 'Terms of use', 'support': 'Help and contact'}[key]


def legal(c, body):
    body = re.sub(r'<a href="https://apps\.apple\.com[^"]*"[^>]*>(.*?)</a>', r'\1', body)   # nothing on apps.apple.com (isolation)
    h1 = re.search(r'<h1>(.*?)</h1>', body, re.S).group(1)
    upd = re.search(r'<p class="updated">(.*?)</p>', body, re.S).group(1)
    summ = re.search(r'<p class="summary">(.*?)</p>', body, re.S)
    rest = body[body.index('<h2>'):]
    secs = re.findall(r'<h2>(.*?)</h2>(.*?)(?=<h2>|\Z)', rest, re.S)
    toc, out = [], []
    for n, (title, inner) in enumerate(secs, 1):
        title = re.sub(r'^\d+\.\s*', '', title.strip())
        sid = f's{n}'
        subs = re.findall(r'<h3>(.*?)</h3>', inner)
        for j, t in enumerate(subs, 1):
            inner = inner.replace(f'<h3>{t}</h3>', f'<h3 id="{sid}-{j}">{t}</h3>', 1)
        toc.append((sid, title, [(f'{sid}-{j}', t) for j, t in enumerate(subs, 1)]))
        out.append(f'<section id="{sid}" aria-labelledby="{sid}-h"><h2 id="{sid}-h"><span class="no">{n:02d}</span><span>{title}</span></h2>{inner.strip()}</section>')
    li = ''
    for sid, t, subs in toc:
        sub = ''.join(f'<li><a href="#{i}">{s}</a></li>' for i, s in subs)
        li += f'<li><a href="#{sid}">{t}</a>{"<ol>" + sub + "</ol>" if sub else ""}</li>'
    sub_cls = ' sub' if c.key == 'support' else ''
    lead = f'<p class="updated{sub_cls}">{upd}</p>'
    main = f'''<main id="main" class="ry-art"><div class="ry-wrap ry-art-g">
<aside class="ry-toc" aria-label="On this page"><a class="back" href="{c.home}">{I('chev')} Back to Roomy</a>
<details open><summary>On this page</summary><nav aria-label="Sections"><ol>{li}</ol></nav></details></aside>
<article class="ry-prose"><p class="ry-k">{_kicker(c.key)}</p><h1>{h1}</h1>{lead}
{'<p class="summary">' + summ.group(1) + '</p>' if summ else ''}
{''.join(out)}
<div class="end"><span>Questions about Roomy? <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a></span><a href="{c.home}">Back to Roomy</a></div>
</article></div></main>'''
    return main


TOC_JS = ('<script>(function(){var d=document.querySelector(".ry-toc details");if(!d)return;var m=matchMedia("(min-width:1061px)");'
          'if(!m.matches)d.open=false;d.addEventListener("toggle",function(){if(m.matches&&!d.open)d.open=true})})();</script>')


def _base_of(body):
    m = re.search(r'<!--(\S*?)terms\.html-->', body)
    return m.group(1) if m else ''


def page(app, lang, key, title, desc, body, host, alts):
    base = _base_of(body)
    body = re.sub(r'<!--\S*?terms\.html-->', '', body)
    c = Ctx(base, key)
    canon = f'{host}roomy/' if key == 'index' else f'{host}roomy/{key}.html'
    if key == 'index':
        return shell(c, title, desc, canon, home(c))
    return shell(c, title, desc, canon, legal(c, body), TOC_JS)
