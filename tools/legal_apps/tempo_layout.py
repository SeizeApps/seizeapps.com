"""Tempo's own site for tools/gen_legal_apps.py (slug 'tempo'): home (/tempo/), privacy, terms, support.

Shares no template, class name or stylesheet with the other apps' pages: everything is prefixed `tw-`. It is one
design system. Dark navy "stages" (the app's own world: #060E1F canvas, blue #007AFF, cyan, the cream-and-gold dial
of the icon as the one warm note) sit on a warm paper page in light mode and on a lifted navy page in dark mode.
Numerals use ui-rounded, text Avenir Next, both system fonts. Everything is inline: no external font, script, CDN
or analytics, and no script at all. Every link goes to Tempo's own pages, its own media, the contact address, the
App Store listing and the vendors and regulators the legal text already names (checked by isolation() below).

The text of privacy, terms and support lives in tools/legal_apps/tempo.py and is only re-wrapped here: the h2s become
numbered sections with a contents list (a sticky card on desktop, a collapsible one on phones), the .summary
paragraph becomes the short-version panel. The home page is written below (HOME_*), from the live App Store text and
the 1.0.3 source named in tempo.py.

Colours: every colour a text can sit on is a 6-digit hex custom property of :root (light) or of the dark :root, and
audit() measures PAIRS from the stylesheet of each generated page, in both modes. gen_legal_apps.py refuses to write
a page if one pair is under 4.5:1 (UI boundaries and large text included: one bar for everything).
"""
import math, re

MIN = 4.5
STORE = 'https://apps.apple.com/app/id6761499275'
MAIL = 'izotz@seizeapps.com'

LIGHT = dict(bg='#FAF8F3', bg2='#F1EEE5', card='#FFFFFF', fg='#0B1426', muted='#4B5870', link='#0A5BC4',
             linkbg='#E6F0FF', amber='#8A5A00')
DARK = dict(bg='#060E1F', bg2='#0D1A33', card='#111D38', fg='#EAF0FA', muted='#A9B6CD', link='#6DB6FF',
            linkbg='#12284D', amber='#FFB020')
# Same in both modes: the navy world of the app, and the glass chips that float on it.
STAGE = dict(sta='#10285C', stb='#060E1F', stfg='#F2F5FB', stmuted='#B1BFD6', cyan='#22D3EE', stlink='#8CCBFF',
             focus='#7FD4FF', navbg='#08101F', navfg='#E6ECF7', pillbg='#FFFFFF', pillfg='#0B1426',
             chipbg='#141E38', chipfg='#FFFFFF', chipmuted='#B9C6DC', proplan='#0B1A38')

PAIRS = [
    ('body text on page', 'fg', 'bg'), ('body text on alternate band', 'fg', 'bg2'), ('body text on card', 'fg', 'card'),
    ('muted text on page', 'muted', 'bg'), ('muted text on alternate band', 'muted', 'bg2'), ('muted text on card', 'muted', 'card'),
    ('link / eyebrow on page', 'link', 'bg'), ('link / eyebrow on alternate band', 'link', 'bg2'), ('link / eyebrow on card', 'link', 'card'),
    ('link on tinted panel', 'link', 'linkbg'), ('body text on tinted panel', 'fg', 'linkbg'),
    ('caveat label on card', 'amber', 'card'), ('caveat label on page', 'amber', 'bg'),
    ('text on stage (lighter end)', 'stfg', 'sta'), ('text on stage (navy end)', 'stfg', 'stb'),
    ('muted text on stage (lighter end)', 'stmuted', 'sta'), ('muted text on stage (navy end)', 'stmuted', 'stb'),
    ('cyan eyebrow on stage (lighter end)', 'cyan', 'sta'), ('cyan eyebrow on stage (navy end)', 'cyan', 'stb'),
    ('link on stage (lighter end)', 'stlink', 'sta'), ('link on stage (navy end)', 'stlink', 'stb'),
    ('text on Pro plan card', 'stfg', 'proplan'), ('muted text on Pro plan card', 'stmuted', 'proplan'), ('cyan on Pro plan card', 'cyan', 'proplan'),
    ('nav text on bar', 'navfg', 'navbg'), ('nav pill label', 'pillfg', 'pillbg'), ('link on bar', 'stlink', 'navbg'),
    ('notification text on glass chip', 'chipfg', 'chipbg'), ('notification muted on glass chip', 'chipmuted', 'chipbg'),
    ('focus ring on page', 'link', 'bg'), ('focus ring on stage (lighter end)', 'focus', 'sta'),
    ('focus ring on stage (navy end)', 'focus', 'stb'), ('focus ring on bar', 'focus', 'navbg'),
]

CSS = r'''
:root{%(light)s;%(stage)s;color-scheme:light dark;
--disp:"Avenir Next","Avenir","Segoe UI",system-ui,sans-serif;
--num:ui-rounded,"SF Pro Rounded","SF Compact Rounded","Avenir Next","Avenir","Segoe UI",system-ui,sans-serif;
--line:#E2DDD0;--line2:#D3CDBC;--gold:#AE8E63;--edge:rgba(255,255,255,.14);
--shadow:0 1px 2px rgba(11,20,38,.06),0 18px 40px -18px rgba(11,20,38,.22)}
@media (prefers-color-scheme:dark){:root{%(dark)s;--line:#1B2A45;--line2:#2A3C5E;--gold:#CDB287;--shadow:0 1px 0 rgba(255,255,255,.04) inset,0 24px 48px -20px rgba(0,0,0,.65)}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%%;scroll-behavior:smooth;scroll-padding-top:84px}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{animation:none!important;transition:none!important}}
body.tw{margin:0;background:var(--bg);color:var(--fg);font-family:var(--disp);font-size:18px;line-height:1.6;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;overflow-x:hidden}
:where(.tw) img{max-width:100%%;height:auto;display:block}
:where(.tw) a{color:var(--link);text-underline-offset:.2em;text-decoration-thickness:1px}
:where(.tw) a:hover{text-decoration-thickness:2px}
:where(.tw) :focus-visible{outline:3px solid var(--link);outline-offset:3px;border-radius:6px}
.tw-stage :focus-visible,.tw-bar :focus-visible,.tw-pro-plan :focus-visible{outline-color:var(--focus)}
:where(.tw) h1,:where(.tw) h2,:where(.tw) h3{font-family:var(--disp);margin:0;text-wrap:balance}
:where(.tw) p{margin:0}
.tw-skip{position:absolute;left:12px;top:-80px;z-index:60;background:var(--pillbg);color:var(--pillfg)!important;padding:11px 18px;border-radius:12px;font-weight:700;text-decoration:none}
.tw-skip:focus{top:12px}
.tw-wrap{max-width:1120px;margin:0 auto;padding:0 28px}
.tw-eyebrow{font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;color:var(--link);margin:0 0 16px}
.tw-stage .tw-eyebrow,.tw-pro-plan .tw-eyebrow{color:var(--cyan)}
.tw-num{font-family:var(--num);font-weight:700;font-variant-numeric:tabular-nums;letter-spacing:-.02em}
.tw-pro{display:inline-block;font-size:.68rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;padding:3px 9px;border-radius:999px;border:1px solid currentColor;color:var(--link);vertical-align:middle;margin-left:10px;position:relative;top:-1px;line-height:1.4}
.tw-stage .tw-pro,.tw-pro-plan .tw-pro{color:var(--cyan)}

/* bar */
.tw-bar{position:sticky;top:0;z-index:40;background:rgba(8,16,31,.9);-webkit-backdrop-filter:saturate(1.4) blur(16px);backdrop-filter:saturate(1.4) blur(16px);border-bottom:1px solid rgba(255,255,255,.08);color:var(--navfg)}
.tw-bar-in{display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:64px}
.tw-brand{display:flex;align-items:center;gap:11px;color:var(--navfg)!important;text-decoration:none!important;font-weight:700;font-size:1.12rem;letter-spacing:-.01em}
.tw-brand img{width:34px;height:34px;border-radius:8px;box-shadow:0 0 0 1px rgba(255,255,255,.18)}
.tw-bar ul{display:flex;gap:4px;list-style:none;margin:0;padding:0;align-items:center}
.tw-bar li a{display:inline-block;padding:9px 12px;color:var(--navfg);text-decoration:none;font-size:.94rem;font-weight:500;border-radius:999px}
.tw-bar li a:hover{background:rgba(255,255,255,.1)}
.tw-bar li a[aria-current]{font-weight:800;background:rgba(255,255,255,.1)}
.tw-bar li a.tw-get{background:var(--pillbg);color:var(--pillfg);font-weight:700;margin-left:8px;padding:9px 18px;white-space:nowrap}
.tw-bar li a.tw-get:hover{background:#DCE8FA}

/* stage = the app's navy world */
.tw-stage{position:relative;color:var(--stfg);background:radial-gradient(120%% 95%% at 50%% 0%%,var(--sta) 0%%,var(--stb) 66%%);isolation:isolate;overflow:hidden}
.tw-stage a{color:var(--stlink)}
.tw-stage .tw-muted{color:var(--stmuted)}
.tw-rings{position:absolute;left:50%%;top:var(--ry,60%%);width:min(1500px,170vw);aspect-ratio:1;transform:translate(-50%%,-50%%);z-index:-1;pointer-events:none;
 background:repeating-radial-gradient(circle at 50%% 50%%,transparent 0 46px,rgba(34,211,238,.11) 46px 47px);-webkit-mask-image:radial-gradient(closest-side,#000 10%%,transparent 78%%);mask-image:radial-gradient(closest-side,#000 10%%,transparent 78%%)}
.tw-glow{position:absolute;inset:auto 0 0 0;height:60%%;z-index:-1;background:radial-gradient(60%% 70%% at 50%% 100%%,rgba(0,122,255,.4),transparent 70%%)}
.tw-topo{position:absolute;z-index:-1;pointer-events:none;color:rgba(34,211,238,.28);width:var(--tw,900px);height:var(--tw,900px);left:var(--tx,50%%);top:var(--ty,50%%);margin:calc(var(--tw,900px)/-2) 0 0 calc(var(--tw,900px)/-2)}
.tw-topo use{vector-effect:non-scaling-stroke}
.tw-object{border:1px solid var(--edge);box-shadow:0 0 0 1px rgba(0,0,0,.35),var(--shadow),0 0 70px -30px rgba(0,122,255,.55)}

/* store badge: Apple's own artwork, clear space = 1/4 of its height */
.tw-badge{display:inline-flex;padding:14px;border-radius:20px;line-height:0;transition:transform .25s cubic-bezier(.3,1.4,.5,1)}
.tw-badge:hover{transform:translateY(-2px)}
.tw-badge img,.tw-badge picture{height:54px;width:auto;display:block}
.tw-badge img{aspect-ratio:119.66/40}

/* hero */
.tw-hero{padding-bottom:104px}
.tw-hero-copy{text-align:center;padding:58px 0 0;max-width:840px;margin:0 auto}
.tw-icon{width:104px;height:104px;border-radius:23%%;margin:0 auto 30px;box-shadow:0 0 0 1px rgba(255,255,255,.2),0 24px 50px -12px rgba(0,0,0,.65),0 0 80px -10px rgba(174,142,99,.5)}
.tw-hero h1{font-size:clamp(2.7rem,7.2vw,5.9rem);line-height:1.02;letter-spacing:-.04em;font-weight:700;color:#fff}
.tw-hero h1 em{font-style:normal;color:var(--cyan)}
.tw-lede{font-size:clamp(1.1rem,1.9vw,1.38rem);line-height:1.5;color:var(--stmuted);max-width:36em;margin:26px auto 0}
.tw-cta{display:flex;gap:6px 14px;justify-content:center;align-items:center;flex-wrap:wrap;margin-top:22px}
.tw-chips{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;list-style:none;padding:0;margin:8px 0 0}
.tw-chips li{font-size:.88rem;font-weight:600;color:var(--stfg);padding:7px 14px;border:1px solid rgba(255,255,255,.2);border-radius:999px;background:rgba(255,255,255,.05)}
.tw-chips li::before{content:"";display:inline-block;width:6px;height:6px;border-radius:50%%;background:var(--cyan);margin-right:9px;vertical-align:middle;position:relative;top:-1px}
.tw-devices{position:relative;height:770px;margin:56px auto 0;max-width:1000px}
.tw-phone{position:absolute;margin:0;width:var(--w,300px);padding:9px;border-radius:calc(var(--w,300px)*.17);background:linear-gradient(155deg,#2F3C64 0%%,#10182E 38%%,#0A1022 100%%);box-shadow:0 0 0 1px rgba(255,255,255,.18) inset,0 0 0 1px #02050D,0 40px 80px -20px rgba(0,0,0,.7),0 0 120px -30px rgba(0,122,255,.5)}
.tw-phone img{width:100%%;border-radius:calc(var(--w,300px)*.145);aspect-ratio:660/1434;background:#070E20}
.tw-front{--w:340px;left:50%%;margin-left:-170px;top:0;z-index:3}
.tw-bk{--w:276px;top:78px;z-index:1}
.tw-bk img{filter:brightness(.82)}
.tw-bl{left:50%%;margin-left:-378px;transform:rotate(-4deg);transform-origin:80%% 90%%}
.tw-br{left:50%%;margin-left:102px;transform:rotate(4deg);transform-origin:20%% 90%%}
.tw-float{position:absolute;z-index:4;display:flex;gap:12px;align-items:center;background:rgba(20,30,56,.96);color:var(--chipfg);border:1px solid rgba(255,255,255,.18);border-radius:20px;padding:12px 18px 12px 12px;box-shadow:0 20px 40px -14px rgba(0,0,0,.7);max-width:320px;text-align:left}
.tw-float img{width:38px;height:38px;border-radius:9px;flex:none}
.tw-float b{display:block;font-size:.76rem;letter-spacing:.07em;text-transform:uppercase;color:var(--chipmuted);font-weight:700;line-height:1.3}
.tw-float span{display:block;font-size:1rem;font-weight:600;line-height:1.3}
.tw-fa{left:50%%;margin-left:-520px;top:170px}
.tw-fb{left:50%%;margin-left:230px;top:470px}

/* proof strip */
.tw-proof-wrap{position:relative;z-index:5;margin-top:-52px}
.tw-proof{display:grid;grid-template-columns:repeat(4,1fr);background:var(--card);border:1px solid var(--line);border-radius:26px;box-shadow:var(--shadow);overflow:hidden;margin:0;padding:0;list-style:none}
.tw-proof li{padding:28px 28px 26px}
.tw-proof li+li{border-left:1px solid var(--line)}
.tw-proof .n{display:block;font-size:clamp(2rem,3.4vw,2.9rem);line-height:1;color:var(--fg)}
.tw-proof .n small{font-size:.46em;letter-spacing:0;color:var(--muted);margin-left:5px;font-weight:700}
.tw-proof p{margin-top:12px;color:var(--muted);font-size:.95rem;line-height:1.45}

/* sections */
.tw-sec{padding:120px 0}
.tw-sec.alt{background:var(--bg2)}
.tw-statement{padding:130px 0 40px;text-align:center}
.tw-statement p{font-size:clamp(1.9rem,4.6vw,3.6rem);line-height:1.12;letter-spacing:-.035em;font-weight:600;max-width:17em;margin:0 auto;text-wrap:balance}
.tw-statement p span{color:var(--muted)}
.tw-split{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.05fr);gap:84px;align-items:center}
.tw-split.rev{grid-template-columns:minmax(0,1.05fr) minmax(0,1fr)}
.tw-split.rev .tw-copy{order:2}
.tw-copy h2,.tw-head h2{font-size:clamp(2.2rem,4.6vw,3.6rem);line-height:1.04;letter-spacing:-.035em;font-weight:700}
.tw-copy>p,.tw-head>p{margin-top:22px;color:var(--muted);font-size:1.16rem;max-width:30em}
.tw-copy>p strong{color:var(--fg);font-weight:700}
.tw-head{text-align:center;max-width:820px;margin:0 auto}
.tw-head>p{margin-left:auto;margin-right:auto;max-width:34em}
.tw-note{margin-top:26px;font-size:.94rem;color:var(--muted);max-width:34em}
.tw-copy .tw-note{margin-top:22px}

/* arrive: time-first rows */
.tw-rules{margin:34px 0 0;padding:0;list-style:none;border-top:1px solid var(--line)}
.tw-rule{display:grid;grid-template-columns:128px minmax(0,1fr);gap:4px 22px;align-items:start;padding:20px 0;border-bottom:1px solid var(--line)}
.tw-rule .tw-num{font-size:2.5rem;line-height:1;color:var(--link);white-space:nowrap}
.tw-rule .tw-num small{font-size:.42em;color:var(--muted);margin-left:4px;letter-spacing:0}
.tw-rule h3{font-size:1.02rem;font-weight:700;letter-spacing:0;line-height:1.35}
.tw-rule p{font-size:.98rem;line-height:1.5;color:var(--muted);margin-top:4px}
.tw-rule p strong{color:var(--fg);font-weight:600}
.tw-track{display:flex;height:16px;gap:3px;margin-top:14px}
.tw-track i{display:block;border-radius:6px;background:linear-gradient(90deg,#007AFF,#00BBFF)}
.tw-track .w{background:transparent;border:1.5px dashed var(--muted)}
.tw-track .g{background:repeating-linear-gradient(135deg,var(--line2) 0 3px,transparent 3px 7px);border:1px solid var(--line2)}
.tw-fine{font-size:.88rem;color:var(--muted);margin-top:12px}

/* stage visuals */
.tw-visual{position:relative;border-radius:36px;padding:48px 40px;display:flex;justify-content:center;align-items:center;min-height:560px}
.tw-visual.fade{align-items:flex-start;padding:52px 40px 0;height:640px}
.tw-plate{position:relative;width:min(var(--w,360px),100%%);border-radius:26px;overflow:hidden;margin:0;flex:none;box-shadow:0 0 0 1px rgba(255,255,255,.14),0 30px 60px -20px rgba(0,0,0,.75);background:#0A1530}
.tw-plate img{width:100%%;background:#0A1530}
.tw-plate.cut{border-radius:28px 28px 0 0}
.tw-plate.cut img{-webkit-mask-image:linear-gradient(#000 80%%,transparent);mask-image:linear-gradient(#000 80%%,transparent)}
.tw-cap{position:absolute;left:0;right:0;bottom:14px;text-align:center;font-size:.82rem;color:var(--stmuted);padding:0 20px}
.tw-notes{position:absolute;left:18px;top:96px;display:grid;gap:12px;justify-items:start;z-index:3}
.tw-note-card{display:flex;gap:12px;align-items:center;background:rgba(20,30,56,.96);color:var(--chipfg);border:1px solid rgba(255,255,255,.18);border-radius:20px;padding:12px 18px 12px 12px;box-shadow:0 20px 40px -14px rgba(0,0,0,.7);max-width:300px}
.tw-note-card img{width:38px;height:38px;border-radius:9px;flex:none}
.tw-note-card b{display:block;font-size:.76rem;letter-spacing:.07em;text-transform:uppercase;color:var(--chipmuted);font-weight:700;line-height:1.3}
.tw-note-card span{display:block;font-size:1rem;font-weight:600;line-height:1.3}
.tw-note-card+.tw-note-card{margin-left:26px}
.tw-places .tw-visual{padding-bottom:62px}
.tw-places .tw-plate{--w:392px}

/* today */
.tw-figs{display:grid;grid-template-columns:repeat(3,1fr);margin:64px auto 0;max-width:980px;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.tw-fig{padding:44px 20px 40px;text-align:center}
.tw-fig+.tw-fig{border-left:1px solid var(--line)}
.tw-fig .tw-num{display:block;font-size:clamp(2.5rem,5.2vw,4.6rem);line-height:1;white-space:nowrap}
.tw-fig.main .tw-num{color:var(--link)}
.tw-fig .l{display:block;margin-top:14px;font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;color:var(--muted)}
.tw-today-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,.9fr);gap:72px;align-items:center;margin:64px auto 0;max-width:980px}
.tw-daybar{position:relative;height:20px;border-radius:999px;background:var(--bg2);border:1px solid var(--line2)}
.tw-daybar i{position:absolute;top:2px;bottom:2px;border-radius:999px;background:linear-gradient(90deg,#007AFF,#00BBFF)}
.tw-axis{display:flex;justify-content:space-between;margin-top:12px;font-size:.82rem;color:var(--muted);font-family:var(--num);font-variant-numeric:tabular-nums;font-weight:700}
.tw-styles{list-style:none;margin:30px 0 0;padding:0;border-top:1px solid var(--line)}
.tw-styles li{padding:15px 0;border-bottom:1px solid var(--line);font-size:1rem;line-height:1.45;color:var(--muted)}
.tw-styles li strong{color:var(--fg);font-weight:700}
.tw-lower{border-radius:32px;padding:44px 40px 0;height:500px;display:flex;justify-content:center;align-items:flex-end}
.tw-lowphone{width:min(344px,100%%);padding:9px 9px 0;border-radius:46px 46px 0 0;background:linear-gradient(155deg,#2F3C64 0%%,#10182E 38%%,#0A1022 100%%);box-shadow:0 0 0 1px rgba(255,255,255,.18) inset,0 0 0 1px #02050D,0 0 100px -30px rgba(0,122,255,.5);margin:0;-webkit-mask-image:linear-gradient(transparent 0,#000 22%%);mask-image:linear-gradient(transparent 0,#000 22%%)}
.tw-lowphone img{border-radius:38px 38px 0 0;width:100%%;aspect-ratio:660/894;background:#070E20}

/* control + surfaces */
.tw-surfaces{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;list-style:none;margin:32px 0 0;padding:0}
.tw-surfaces li{border:1px solid var(--line);background:var(--card);border-radius:18px;padding:16px 8px 14px;text-align:center;font-weight:700;font-size:.9rem;line-height:1.25}
.tw-surfaces svg{display:block;margin:0 auto 10px;width:48px;height:48px}

/* routine facts */
.tw-facts{list-style:none;margin:30px 0 0;padding:0;border-top:1px solid var(--line)}
.tw-facts li{padding:15px 0 15px 30px;border-bottom:1px solid var(--line);position:relative;font-size:1.02rem;line-height:1.5}
.tw-facts li::before{content:"";position:absolute;left:2px;top:23px;width:9px;height:9px;border-radius:50%%;background:var(--gold)}

/* recaps */
.tw-recap-art{min-height:600px;padding:0;overflow:hidden}
.tw-recap-art .tw-phone{--w:236px;top:60px}
.tw-recap-art .a{left:50%%;margin-left:-218px;z-index:1;transform:rotate(-3deg)}
.tw-recap-art .b{left:50%%;margin-left:-14px;top:116px;z-index:2;transform:rotate(3deg)}
.tw-recap-art::after{content:"";position:absolute;left:0;right:0;bottom:0;height:90px;background:linear-gradient(transparent,var(--stb));z-index:3;pointer-events:none}
.tw-quote{margin-top:26px;font-size:1rem;color:var(--muted);font-style:italic;max-width:32em}

/* focus */
.tw-dial{position:relative;width:min(360px,76vw);aspect-ratio:1;border-radius:50%%;display:grid;place-items:center;text-align:center}
.tw-dial::before{content:"";position:absolute;inset:0;border-radius:50%%;background:repeating-conic-gradient(from -1deg,rgba(255,255,255,.36) 0 2deg,transparent 2deg 6deg);-webkit-mask:radial-gradient(farthest-side,transparent 88%%,#000 89%%,#000 94%%,transparent 95%%);mask:radial-gradient(farthest-side,transparent 88%%,#000 89%%,#000 94%%,transparent 95%%);opacity:.7}
.tw-dial::after{content:"";position:absolute;inset:7%%;border-radius:50%%;background:conic-gradient(from 0deg,#00BBFF,#007AFF 60%%,#00BBFF);-webkit-mask:radial-gradient(farthest-side,transparent calc(100%% - 14px),#000 calc(100%% - 13px));mask:radial-gradient(farthest-side,transparent calc(100%% - 14px),#000 calc(100%% - 13px));filter:drop-shadow(0 0 18px rgba(0,187,255,.55))}
.tw-dial .tw-num{font-size:clamp(3.4rem,9vw,5.4rem);line-height:1;display:block;color:#fff}
.tw-dial small{display:block;margin-top:10px;font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;font-weight:700;color:var(--stmuted)}
.tw-tags{display:flex;flex-wrap:wrap;gap:8px;list-style:none;padding:0;margin:26px 0 0}
.tw-tags li{padding:7px 14px;border-radius:999px;border:1px solid var(--line2);font-size:.9rem;font-weight:600;background:var(--card)}

/* free vs pro */
.tw-plans{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:60px;text-align:left}
.tw-plan{border-radius:32px;padding:44px;border:1px solid var(--line);background:var(--card);box-shadow:var(--shadow)}
.tw-pro-plan{color:var(--stfg);border:1px solid var(--edge);background:radial-gradient(120%% 90%% at 50%% 0%%,#12306E 0%%,var(--proplan) 70%%);position:relative;overflow:hidden;isolation:isolate}
.tw-plan h3{font-size:1.7rem;letter-spacing:-.03em;font-weight:700}
.tw-plan .k{font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;color:var(--muted);margin-bottom:12px;display:block}
.tw-pro-plan .k{color:var(--cyan)}
.tw-plan ul{list-style:none;padding:0;margin:26px 0 0}
.tw-plan li{padding:13px 0 13px 32px;border-top:1px solid var(--line);position:relative;line-height:1.45}
.tw-pro-plan li{border-top-color:rgba(255,255,255,.14)}
.tw-plan li::before{content:"";position:absolute;left:3px;top:20px;width:12px;height:7px;border-left:2.5px solid var(--link);border-bottom:2.5px solid var(--link);transform:rotate(-45deg)}
.tw-pro-plan li::before{border-color:var(--cyan)}
.tw-buy{margin:30px auto 0;max-width:46em;font-size:.94rem;color:var(--muted);text-align:center}
.tw-good{display:grid;grid-template-columns:auto minmax(0,1fr);gap:8px 22px;align-items:start;text-align:left;margin:30px auto 0;max-width:980px;background:var(--card);border:1px solid var(--line);border-left:5px solid #E09A00;border-radius:20px;padding:24px 28px;box-shadow:var(--shadow)}
.tw-good b{font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;color:var(--amber);font-weight:800;padding-top:.45em;white-space:nowrap}
.tw-good p{max-width:70ch}

/* privacy band */
.tw-privacy{padding:132px 0;text-align:center}
.tw-privacy h2{font-size:clamp(2.2rem,5.4vw,4.4rem);line-height:1.04;letter-spacing:-.04em;font-weight:700;max-width:14em;margin:0 auto;color:#fff}
.tw-privacy h2 span{display:block}
.tw-privacy h2 .d{color:var(--cyan)}
.tw-privacy p.lead{max-width:36em;margin:28px auto 0;color:var(--stmuted);font-size:1.12rem}
.tw-privacy .go{margin-top:30px}
.tw-privacy .go a{display:inline-block;padding:12px 24px;border-radius:999px;border:1px solid rgba(255,255,255,.28);background:rgba(255,255,255,.07);color:#fff;font-weight:700;text-decoration:none;font-size:1rem}
.tw-privacy .go a:hover{background:rgba(255,255,255,.14)}

/* closing */
.tw-closing{padding:128px 0 120px;text-align:center}
.tw-closing .tw-icon{width:88px;height:88px;margin-bottom:28px;box-shadow:0 0 0 1px rgba(174,142,99,.6),0 18px 36px -12px rgba(11,20,38,.45),0 0 60px -16px rgba(174,142,99,.5)}
.tw-closing h2{font-size:clamp(2.2rem,4.6vw,3.6rem);line-height:1.04;letter-spacing:-.035em;font-weight:700;max-width:13em;margin:0 auto}
.tw-closing .tw-cta{margin-top:26px}
.tw-closing .tw-fine{margin:6px 0 0}

/* footer */
.tw-foot{padding:52px 0 64px;border-top:1px solid var(--line);font-size:.94rem;color:var(--muted)}
.tw-foot .row{display:flex;flex-wrap:wrap;gap:24px 48px;justify-content:space-between;align-items:flex-start}
.tw-foot .row>div{flex:1 1 360px;max-width:560px}
.tw-foot .b{display:flex;align-items:center;gap:10px;color:var(--fg);font-weight:700;font-size:1.05rem}
.tw-foot .b img{width:28px;height:28px;border-radius:7px}
.tw-foot p{margin-top:10px;max-width:46em}
.tw-foot nav{display:flex;flex-wrap:wrap;gap:4px 26px}
.tw-foot nav a{color:var(--fg);text-decoration:none;font-weight:600;padding:6px 0}
.tw-foot nav a:hover{text-decoration:underline}
.tw-foot .small{margin-top:30px;font-size:.84rem}

/* legal pages */
.tw-lhero{padding:46px 0 52px}
.tw-back{display:inline-flex;gap:8px;align-items:center;font-weight:700;font-size:.95rem;text-decoration:none;margin-bottom:28px;padding:4px 0}
.tw-back:hover{text-decoration:underline}
.tw-lhero h1{font-size:clamp(2.6rem,6vw,4.6rem);line-height:1.02;letter-spacing:-.04em;font-weight:700;color:#fff}
.tw-lhero .upd{margin-top:16px;color:var(--stmuted);font-size:1rem}
.tw-lgrid{display:grid;grid-template-columns:276px minmax(0,1fr);gap:72px;padding-top:56px;padding-bottom:110px;align-items:start}
.tw-side{position:sticky;top:88px;max-height:calc(100vh - 110px);overflow:auto;background:var(--card);border:1px solid var(--line);border-radius:22px;padding:22px 22px 18px;box-shadow:var(--shadow)}
.tw-toc-h{display:block;font-size:.74rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);font-weight:800;margin:0 0 12px}
.tw-toc{list-style:none;margin:0;padding:0;counter-reset:toc}
.tw-toc>li{counter-increment:toc}
.tw-toc a{display:flex;gap:10px;color:var(--fg);text-decoration:none;font-size:.93rem;line-height:1.35;padding:7px 8px;margin:0 -8px;border-radius:9px}
.tw-toc a::before{content:counter(toc,decimal-leading-zero);font-family:var(--num);font-weight:700;font-size:.78rem;line-height:1.75;color:var(--muted);flex:none;min-width:1.6em}
.tw-toc a:hover{background:var(--bg2)}
.tw-toc ul{list-style:none;margin:0 0 4px;padding:0 0 0 34px}
.tw-toc ul a{font-size:.88rem;color:var(--muted);padding:5px 8px}
.tw-toc ul a::before{content:none}
.tw-sib{margin:14px 0 0;padding:14px 0 0;border-top:1px solid var(--line);display:grid;gap:2px;list-style:none}
.tw-sib a{display:flex;justify-content:space-between;color:var(--fg);text-decoration:none;font-weight:700;font-size:.93rem;padding:7px 8px;margin:0 -8px;border-radius:9px}
.tw-sib a::after{content:"\2192";color:var(--muted)}
.tw-sib a:hover{background:var(--bg2)}
.tw-sib a[aria-current]{color:var(--link)}
.tw-mtoc{display:none;margin:0 0 28px;background:var(--card);border:1px solid var(--line);border-radius:18px;box-shadow:var(--shadow)}
.tw-mtoc summary{cursor:pointer;list-style:none;padding:16px 20px;font-weight:800;font-size:.95rem;display:flex;justify-content:space-between;align-items:center}
.tw-mtoc summary::-webkit-details-marker{display:none}
.tw-mtoc summary::after{content:"+";font-family:var(--num);font-size:1.4rem;line-height:1;color:var(--link)}
.tw-mtoc[open] summary::after{content:"\2212"}
.tw-mtoc .in{padding:0 20px 16px}
.tw-prose{max-width:70ch;font-size:1.08rem;line-height:1.72;min-width:0}
.tw-prose .tw-short{font-size:1.14rem;line-height:1.6;padding:26px 28px;border-radius:22px;background:var(--linkbg);border:1px solid var(--line);border-left:5px solid #007AFF;margin:0 0 48px}
.tw-prose .tw-short strong{font-weight:800}
.tw-sec-doc{counter-increment:doc}
.tw-prose{counter-reset:doc}
.tw-prose h2{font-size:1.6rem;letter-spacing:-.025em;line-height:1.2;margin:58px 0 16px;font-weight:700;scroll-margin-top:92px;padding-top:32px;border-top:1px solid var(--line);display:flex;gap:14px;align-items:baseline}
.tw-prose h2::before{content:counter(doc,decimal-leading-zero);counter-increment:doc;font-family:var(--num);font-size:.9rem;font-weight:700;color:var(--muted);flex:none;min-width:1.9em}
.tw-prose h2.first{margin-top:0;border-top:0;padding-top:0}
.tw-prose h3{font-size:1.14rem;line-height:1.35;margin:34px 0 8px;font-weight:700;scroll-margin-top:92px}
.tw-prose p{margin:0 0 1.15em}
.tw-prose ul{padding-left:1.2em;margin:0 0 1.2em}
.tw-prose li{margin:0 0 .8em;padding-left:.3em}
.tw-prose li::marker{color:var(--gold)}
.tw-prose strong{font-weight:700}
.tw-prose .contact{font-size:1.3rem;font-weight:700}
.tw-prose .contact a{display:inline-block;padding:14px 22px;border-radius:16px;background:var(--linkbg);border:1px solid var(--line)}
.tw-prose .updated{display:none}
.tw-docnav{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:64px;padding-top:36px;border-top:1px solid var(--line)}
.tw-docnav a{display:block;border:1px solid var(--line);background:var(--card);border-radius:16px;padding:16px 18px;text-decoration:none;color:var(--fg);font-weight:700}
.tw-docnav a small{display:block;font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-bottom:6px;font-weight:800}
.tw-docnav a:hover{border-color:var(--link)}
.tw-docnav a[aria-current]{background:var(--linkbg)}

/* responsive */
@media (max-width:1100px){
 .tw-fa{margin-left:-440px}.tw-fb{margin-left:170px}
}
@media (max-width:980px){
 .tw-split,.tw-split.rev{grid-template-columns:minmax(0,1fr);gap:48px}
 .tw-split.rev .tw-copy{order:0}
 .tw-sec{padding:88px 0}
 .tw-plans{grid-template-columns:1fr}
 .tw-proof{grid-template-columns:1fr 1fr}
 .tw-proof li:nth-child(3){border-left:0}
 .tw-proof li:nth-child(n+3){border-top:1px solid var(--line)}
 .tw-lgrid{grid-template-columns:minmax(0,1fr);gap:0;padding-top:34px}
 .tw-side{display:none}
 .tw-mtoc{display:block}
 .tw-docnav{grid-template-columns:1fr}
 .tw-today-grid{grid-template-columns:minmax(0,1fr);gap:44px}
 .tw-fa,.tw-fb{display:none}
 .tw-devices{height:680px}
 .tw-front{--w:300px;margin-left:-150px}
 .tw-bl{margin-left:-340px;--w:240px}.tw-br{margin-left:100px;--w:240px}
}
@media (max-width:640px){
 body.tw{font-size:17px}
 .tw-wrap{padding-left:20px;padding-right:20px}
 .tw-bar-in{min-height:58px;gap:6px}
 .tw-brand{font-size:1.02rem;gap:8px}.tw-brand img{width:30px;height:30px}
 .tw-bar ul{gap:0}
 .tw-bar li.tw-t{display:none}
 .tw-bar li a{padding:9px 7px;font-size:.88rem}
 .tw-bar li a.tw-get{margin-left:4px;padding:9px 14px}
 .tw-hero{padding-bottom:70px}
 .tw-hero-copy{padding-top:34px}
 .tw-icon{width:88px;height:88px;margin-bottom:24px}
 .tw-devices{height:600px;margin-top:30px}
 .tw-front{--w:272px;margin-left:-136px}
 .tw-bk{display:none}
 .tw-float{display:none}
 .tw-proof-wrap{margin-top:-34px}
 .tw-proof li{padding:20px 18px}
 .tw-statement{padding:90px 0 20px}
 .tw-rule{grid-template-columns:1fr;gap:2px}
 .tw-rule .tw-num{font-size:2.2rem;margin-bottom:6px}
 .tw-visual{padding:30px 16px;border-radius:28px;min-height:0}
 .tw-visual.fade{padding:32px 16px 0;height:520px}
 .tw-places .tw-visual{flex-direction:column;gap:18px;padding:22px 16px 56px}
 .tw-notes{position:static;order:-1;width:100%%;justify-items:stretch}
 .tw-note-card{max-width:none;width:100%%}
 .tw-note-card+.tw-note-card{margin-left:0}
 .tw-places .tw-plate{--w:100%%}
 .tw-figs{grid-template-columns:1fr;margin-top:44px}
 .tw-fig{padding:28px 10px}
 .tw-fig+.tw-fig{border-left:0;border-top:1px solid var(--line)}
 .tw-lower{height:400px;padding:30px 16px 0}
 .tw-surfaces{grid-template-columns:1fr 1fr}
 .tw-recap-art{min-height:500px}
 .tw-recap-art .tw-phone{--w:190px;top:44px}
 .tw-recap-art .a{margin-left:-172px}.tw-recap-art .b{margin-left:-18px;top:92px}
 .tw-plan{padding:30px 24px;border-radius:26px}
 .tw-good{grid-template-columns:1fr;padding:22px 22px}
 .tw-privacy,.tw-closing{padding:92px 0}
 .tw-prose{font-size:1.04rem}
 .tw-prose .tw-short{padding:22px;margin-bottom:36px;font-size:1.02rem;line-height:1.58}
 .tw-prose h2{margin-top:44px;padding-top:26px}
 .tw-lhero{padding:30px 0 36px}
 .tw-foot nav{gap:2px 22px}
}
@media (max-width:380px){.tw-bar li a{padding:9px 5px;font-size:.84rem}.tw-brand span{display:none}}
'''


def css():
    f = lambda d: ';'.join(f'--{k}:{v}' for k, v in d.items())
    return CSS % dict(light=f(LIGHT), dark=f(DARK), stage=f(STAGE))


def _vars(block):
    return dict(re.findall(r'--([a-z0-9]+):(#[0-9A-Fa-f]{6})', block))


def audit(html):
    """Contrast of every PAIRS entry, read from the <style> of a generated page -> (rows, ok); a row is
    (mode, label, fg, bg, ratio). Also fails (ok False) if the page links outside Tempo's allowed set."""
    from gen_legal_apps import ratio
    style = re.search(r'<style>(.*?)</style>', html, re.S).group(1)
    light = _vars(re.search(r':root\{([^}]*)\}', style).group(1))
    dark = dict(light, **_vars(re.search(r'prefers-color-scheme:dark\)\{:root\{([^}]*)\}', style).group(1)))
    rows = []
    for mode, v in (('light', light), ('dark', dark)):
        for label, fg, bg in PAIRS:
            rows.append((mode, label, v[fg], v[bg], ratio(v[fg], v[bg])))
    bad = isolation(html)
    if bad:
        print('tempo: link outside the allowed set:', bad)
    return rows, all(r[4] >= MIN for r in rows) and not bad


ALLOWED = (STORE, 'mailto:' + MAIL, 'https://apps.apple.com/account/subscriptions', 'https://reportaproblem.apple.com',
           'https://www.apple.com/legal/', 'https://www.revenuecat.com/privacy', 'https://www.aepd.es')


def isolation(html):
    """Every href/src/srcset that is not Tempo's own page, media or anchor, nor in ALLOWED."""
    bad = []
    html = re.sub(r'<link rel="canonical"[^>]*>', '', html)  # the page's own address
    for u in re.findall(r'(?:href|src|srcset)="([^"]*)"', html):
        if u.startswith('#') or u == './' or re.fullmatch(r'(?:media/[\w.-]+|[a-z]+\.html(?:#[\w-]+)?)', u): continue
        if u.startswith(ALLOWED) or u in ALLOWED: continue
        if u.startswith('https://apps.apple.com/app/id6761499275') or u.startswith('https://aepd.es') or u.startswith('https://revenuecat.com'): continue
        bad.append(u)
    return bad


# ------------------------------------------------------------------ art
def topo(n=9, seed=3):
    """Nested wobbly closed curves, like the contour shape of the recap story: one <symbol> reused where needed."""
    ph = [(2, .09, 0.7 + seed), (3, .06, 2.1 + seed), (5, .035, 4.0 + seed), (7, .018, 1.3 + seed)]
    paths = []
    for k in range(n):
        base = 70 + k * 52
        amp = 0.55 + k * 0.1
        pts = []
        for i in range(160):
            t = 2 * math.pi * i / 160
            r = base * (1 + amp * sum(a * math.sin(m * t + p + k * 0.22) for m, a, p in ph))
            pts.append(f'{500 + r * math.cos(t):.1f},{500 + r * math.sin(t):.1f}')
        paths.append('M' + ' L'.join(pts) + 'Z')
    return ''.join(f'<path d="{d}"/>' for d in paths)


def topo_use(**style):
    st = ';'.join(f'--{k}:{v}' for k, v in style.items())
    return f'<svg class="tw-topo" style="{st}" viewBox="0 0 1000 1000" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true" focusable="false"><use href="#tw-topo"/></svg>'


def sprite():
    return (f'<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><symbol id="tw-topo" viewBox="0 0 1000 1000">{topo()}</symbol></svg>')


def badge(on_dark=True, light_dark=False):
    """Apple's own artwork (media/badge-*.svg). Navy stage: the white badge. Light/dark page: black, white in dark mode."""
    alt = 'Download on the App Store'
    if light_dark:
        art = (f'<picture><source media="(prefers-color-scheme:dark)" srcset="media/badge-white.svg">'
               f'<img src="media/badge-black.svg" width="120" height="40" alt="{alt}"></picture>')
    else:
        art = f'<img src="media/badge-{"white" if on_dark else "black"}.svg" width="120" height="40" alt="{alt}">'
    return f'<a class="tw-badge" href="{STORE}" rel="noopener" aria-label="Download Tempo on the App Store">{art}</a>'


def img(src, w, h, alt, extra=''):
    # Hero images (fetchpriority=high) load eagerly; everything below the fold is lazy (placeholder colour is in the CSS).
    lazy = '' if ('fetchpriority' in extra or 'data-eager' in extra) else ' loading="lazy"'
    extra = extra.replace(' data-eager', '')
    return f'<img src="media/{src}" width="{w}" height="{h}" alt="{alt}"{lazy} decoding="async"{extra}>'


# ------------------------------------------------------------------ chrome
LINKS = [('privacy', 'Privacy'), ('terms', 'Terms'), ('support', 'Support')]


def bar(key):
    items = ''.join(f'<li{" class=tw-t" if k == "terms" else ""}><a href="{k}.html"{" aria-current=page" if k == key else ""}>{l}</a></li>' for k, l in LINKS)
    return (f'<header class="tw-bar"><div class="tw-wrap tw-bar-in">'
            f'<a class="tw-brand" href="./" aria-label="Tempo, home"><img src="media/tempo-icon-96.png" width="34" height="34" alt=""><span>Tempo</span></a>'
            f'<nav aria-label="Tempo"><ul>{items}<li><a class="tw-get" href="{STORE}" rel="noopener">Get Tempo</a></li></ul></nav>'
            f'</div></header>')


def footer():
    return (f'<footer class="tw-foot"><div class="tw-wrap"><div class="row">'
            f'<div><span class="b"><img src="media/tempo-icon-96.png" width="28" height="28" alt="">Tempo Work</span>'
            f'<p>Your workday, understood. Published by Izotz Cristobal Mota. Tempo is a personal time-tracking tool, not an employer&rsquo;s timekeeping system: review your records before using them for payroll or compliance.</p></div>'
            f'<nav aria-label="Tempo pages"><a href="./">Home</a><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a><a href="support.html">Support</a>'
            f'<a href="mailto:{MAIL}">{MAIL}</a></nav></div>'
            f'<p class="small">&copy; 2026 Izotz Cristobal Mota. Tempo requires iOS 17 or later and runs on iPhone. App Store is a service mark of Apple Inc.</p></div></footer>')


def head(title, desc, canon, og=True):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://seizeapps.com/tempo/media/tempo-icon-320.png">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="{STAGE['navbg']}">
<link rel="icon" type="image/png" href="media/tempo-icon-180.png">
<link rel="apple-touch-icon" href="media/tempo-icon-180.png">
<style>{css()}</style>
</head>
'''


# ------------------------------------------------------------------ home
def notif(text, when=None, cls='tw-note-card'):
    return (f'<div class="{cls}"><img src="media/tempo-icon-96.png" width="38" height="38" alt=""><div><b>Tempo</b><span>{text}</span></div></div>')


SURF = {
    'Widgets': '<svg viewBox="0 0 52 52" aria-hidden="true" focusable="false"><rect x="4" y="4" width="44" height="44" rx="13" fill="#0C1B3B"/><circle cx="26" cy="26" r="12" fill="none" stroke="#1F3A6B" stroke-width="4"/><path d="M26 14a12 12 0 0 1 11.4 8.3" fill="none" stroke="#00BBFF" stroke-width="4" stroke-linecap="round"/><rect x="19" y="23" width="14" height="6" rx="3" fill="#EAF0FA"/></svg>',
    'Live Activities': '<svg viewBox="0 0 52 52" aria-hidden="true" focusable="false"><rect x="3" y="15" width="46" height="22" rx="11" fill="#0C1B3B"/><circle cx="14" cy="26" r="6" fill="#007AFF"/><rect x="25" y="23" width="18" height="6" rx="3" fill="#00BBFF"/></svg>',
    'Siri': '<svg viewBox="0 0 52 52" aria-hidden="true" focusable="false"><defs><radialGradient id="tw-so" cx=".35" cy=".3" r=".9"><stop offset="0" stop-color="#7FE3FF"/><stop offset=".55" stop-color="#007AFF"/><stop offset="1" stop-color="#0044CC"/></radialGradient></defs><circle cx="26" cy="26" r="21" fill="url(#tw-so)"/><ellipse cx="26" cy="26" rx="21" ry="8" fill="none" stroke="#fff" stroke-opacity=".6" stroke-width="2" transform="rotate(-24 26 26)"/></svg>',
    'Control Center': '<svg viewBox="0 0 52 52" aria-hidden="true" focusable="false"><rect x="4" y="4" width="20" height="20" rx="8" fill="#007AFF"/><rect x="28" y="4" width="20" height="20" rx="8" fill="#0C1B3B"/><rect x="4" y="28" width="20" height="20" rx="8" fill="#0C1B3B"/><rect x="28" y="28" width="20" height="20" rx="8" fill="#00BBFF"/></svg>',
}


def home():
    surf = ''.join(f'<li>{svg}{n}</li>' for n, svg in SURF.items())
    return f'''<body class="tw" id="top">
<a class="tw-skip" href="#main">Skip to content</a>
{sprite()}
{bar('index')}
<header class="tw-stage tw-hero">
<div class="tw-rings" style="--ry:78%" aria-hidden="true"></div><div class="tw-glow" aria-hidden="true"></div>
<div class="tw-wrap">
<div class="tw-hero-copy">
<img class="tw-icon" src="media/tempo-icon-320.png" width="104" height="104" alt="Tempo app icon: a cream dial with a gold and charcoal ring and a single needle" fetchpriority="high">
<p class="tw-eyebrow">A calmer way to track work</p>
<h1>Your workday, <em>remembered.</em></h1>
<p class="tw-lede">Tempo keeps recorded work, your daily target and remaining time in one place. Arrive, and the day starts. Leave, and it ends.</p>
<div class="tw-cta">{badge(True)}</div>
<ul class="tw-chips"><li>On device</li><li>No account required</li><li>No ads</li></ul>
</div>
<div class="tw-devices">
<figure class="tw-phone tw-bk tw-bl">{img('tempo-recap-story.jpg', 660, 1434, 'A Tempo monthly recap story opening with the title August 2026 and a blue topographic shape', ' data-eager')}</figure>
<figure class="tw-phone tw-bk tw-br">{img('tempo-recap-share.jpg', 660, 1434, 'The Tempo share card composer: a summary card reading 164 h 30 min, My month in Tempo, with format and card design options', ' data-eager')}</figure>
<figure class="tw-phone tw-front">{img('hero-today.jpg', 660, 1434, 'Tempo Today screen: 6h 30m recorded today, a target of 8h 00m, 1h 30m remaining, and a timeline of the day in intervals', ' fetchpriority="high"')}</figure>
{notif('Started at 9:02 at Office', cls='tw-float tw-fa')}
{notif('Ended at 18:10, 8h 4m', cls='tw-float tw-fb')}
</div>
</div>
</header>

<main id="main">
<div class="tw-wrap tw-proof-wrap">
<ul class="tw-proof" aria-label="How automatic tracking behaves">
<li><span class="n tw-num">&asymp;2<small>min</small></span><p>Tempo waits this long on arrival, so GPS jitter cannot open a session.</p></li>
<li><span class="n tw-num">&asymp;3<small>min</small></span><p>And this long on leaving, so a short step outside cannot close one.</p></li>
<li><span class="n tw-num">15<small>min</small></span><p>Back within that window and it is the same session, not a new one.</p></li>
<li><span class="n tw-num">0<small>accounts</small></span><p>No sign-in, no advertising. Your records stay on your iPhone.</p></li>
</ul>
</div>

<section class="tw-statement" aria-label="Tempo in a sentence"><div class="tw-wrap"><p>Your workday, understood. <span>Your time, under your control.</span></p></div></section>

<section class="tw-sec tw-places" id="arrive" aria-labelledby="h-arrive">
<div class="tw-wrap tw-split">
<div class="tw-copy">
<p class="tw-eyebrow">Automatic</p>
<h2 id="h-arrive">Arrive, and the day starts.</h2>
<p>Set up a workplace and Tempo records your real arrival and departure. Home counts as a workplace too. It waits a moment before it acts, and it never asks you to confirm anything.</p>
<ol class="tw-rules" aria-label="How a session is recorded">
<li class="tw-rule"><span class="tw-num" aria-hidden="true">&asymp;2<small>min</small></span><div><h3>Arriving</h3><p>Tempo waits a couple of minutes inside your workplace, then <strong>starts the session at the time you arrived.</strong></p><div class="tw-track" aria-hidden="true"><i class="w" style="flex:0 0 16%"></i><i style="flex:1"></i></div></div></li>
<li class="tw-rule"><span class="tw-num" aria-hidden="true">&asymp;3<small>min</small></span><div><h3>Leaving</h3><p>Once you have been away about three minutes, <strong>it ends the session at the time you left.</strong></p><div class="tw-track" aria-hidden="true"><i style="flex:1"></i><i class="w" style="flex:0 0 22%"></i></div></div></li>
<li class="tw-rule"><span class="tw-num" aria-hidden="true">15<small>min</small></span><div><h3>Back quickly</h3><p><strong>Back within 15 minutes, it is one session.</strong> Later the same day, a return to work starts a new one; coming home does not.</p><div class="tw-track" aria-hidden="true"><i style="flex:0 0 38%"></i><i class="g" style="flex:0 0 14%"></i><i style="flex:1"></i></div></div></li>
</ol>
<p class="tw-fine">Schematic, not to scale.</p>
<p class="tw-note">Automatic tracking depends on iOS permissions (Always location), device settings and signal, and delivery in the background is not guaranteed. Notifications only tell you what happened. Prefer to stay fully manual? Start and stop whenever you like.</p>
</div>
<div class="tw-visual tw-stage tw-object">
<div class="tw-rings" style="--ry:50%" aria-hidden="true"></div>
<figure class="tw-plate" role="group" aria-label="Example place in Tempo"><img src="media/plate-places.jpg" width="800" height="1146" alt="Tempo Places: a map with green zone circles and a panel for a workplace called Home studio showing a 90m radius, 3h 42m today and 31h 15m this week" loading="lazy" decoding="async"></figure>
<div class="tw-notes" role="group" aria-label="Examples of Tempo notifications">
{notif('Started at 9:02 at Office')}
{notif('Ended at 18:10, 8h 4m')}
</div>
<p class="tw-cap">An example place in Tempo, with its radius and the time recorded there.</p>
</div>
</div>
</section>

<section class="tw-sec alt" id="today" aria-labelledby="h-today">
<div class="tw-wrap">
<div class="tw-head">
<p class="tw-eyebrow">Today</p>
<h2 id="h-today">Your day, in intervals.</h2>
<p>Recorded time, your target and what is left, always in one place. No scores, no streaks: just the hours as they happened.</p>
</div>
<div class="tw-figs">
<div class="tw-fig main"><span class="tw-num">6h 30m</span><span class="l">Recorded today</span></div>
<div class="tw-fig"><span class="tw-num">8h 00m</span><span class="l">Target</span></div>
<div class="tw-fig"><span class="tw-num">1h 30m</span><span class="l">Remaining</span></div>
</div>
<div class="tw-today-grid">
<div>
<div class="tw-daybar" role="img" aria-label="A day from midnight to midnight with two recorded intervals marked in blue"><i style="left:33%;width:15%"></i><i style="left:51%;width:19%"></i></div>
<div class="tw-axis" aria-hidden="true"><span>12 AM</span><span>12 PM</span><span>12 AM</span></div>
<p class="tw-fine">Illustration of the Today view, with example numbers.</p>
<ul class="tw-styles">
<li><strong>Big Number</strong> is where you start: recorded time, front and center.</li>
<li><strong>Dayline</strong> and <strong>Cards</strong> are two more ways to read your day <span class="tw-pro">Pro</span></li>
</ul>
</div>
<div class="tw-lower tw-stage tw-object">
<div class="tw-rings" style="--ry:80%" aria-hidden="true"></div>
<figure class="tw-lowphone">{img('today-lower.jpg', 660, 894, 'The lower half of the Tempo Today screen: a card titled Your day in intervals with a timeline and 2 intervals, a Your week card, and a Start Session button')}</figure>
</div>
</div>
</div>
</section>

<section class="tw-sec" id="control" aria-labelledby="h-control">
<div class="tw-wrap tw-split rev">
<div class="tw-copy">
<p class="tw-eyebrow">Control</p>
<h2 id="h-control">You stay in control.</h2>
<p>Start and stop by hand whenever you want. Correct any finished record in History: add, edit, split or merge, with overlaps kept out. <strong>Export every record, or erase them all, without Pro.</strong></p>
<ul class="tw-surfaces" aria-label="Where Tempo shows up">{surf}</ul>
<p class="tw-note">Monday to Friday is where you start; your working days are always editable.</p>
</div>
<div class="tw-visual fade tw-stage tw-object">
<div class="tw-rings" style="--ry:50%" aria-hidden="true"></div>
<figure class="tw-plate cut" style="--w:380px">{img('plate-history.jpg', 800, 1260, 'Tempo History in month view: 170h 45m recorded over 22 days, with a calendar grid of daily totals and weekly totals')}</figure>
</div>
</div>
</section>

<section class="tw-sec alt" id="week" aria-labelledby="h-week">
<div class="tw-wrap tw-split">
<div class="tw-copy">
<p class="tw-eyebrow">Routine <span class="tw-pro">Pro</span></p>
<h2 id="h-week">Fits the week you actually work.</h2>
<p>Home days, office days, days off. Set a pattern for this week and next, and shape the rest around it.</p>
<ul class="tw-facts">
<li>Multiple workplaces and a target for each day</li>
<li>Intensive schedules and a custom home start time</li>
<li>Optional finish-at-target behavior</li>
<li>Personalized reminders and overtime notifications</li>
</ul>
</div>
<div class="tw-visual tw-stage tw-object">
<div class="tw-rings" style="--ry:50%" aria-hidden="true"></div>
<figure class="tw-plate" style="--w:420px">{img('plate-routine.jpg', 800, 818, 'Tempo Weekly Plan: tiles for this week and next, each marked Home, Office or Day off, with an Intensive Schedule switch')}</figure>
</div>
</div>
</section>

<section class="tw-sec" id="recaps" aria-labelledby="h-recaps">
<div class="tw-wrap tw-split rev">
<div class="tw-copy">
<p class="tw-eyebrow">Insights and recaps <span class="tw-pro">Pro</span></p>
<h2 id="h-recaps">Time, remembered.</h2>
<p>Revisit eligible months and years as animated stories, with pause, replay and speed controls. Then make a card of it: choose a layout, preview exactly what you reveal, and share, copy or save an image.</p>
<p class="tw-quote">Workplace names and precise coordinates are never included. Recaps use your recorded history; Tempo does not invent missing work or measure productivity from hours alone.</p>
</div>
<div class="tw-visual tw-recap-art tw-stage tw-object">
{topo_use(tw='820px', tx='50%', ty='46%')}
<figure class="tw-phone a">{img('tempo-recap-story.jpg', 660, 1434, 'A Tempo recap story opening: August 2026, a little perspective on the time that was yours, above a blue topographic shape')}</figure>
<figure class="tw-phone b">{img('tempo-recap-share.jpg', 660, 1434, 'The Tempo share card composer: a summary card reading 164 h 30 min, My month in Tempo, with Share card, Save image and Copy image buttons')}</figure>
</div>
</div>
</section>

<section class="tw-sec alt" id="focus" aria-labelledby="h-focus">
<div class="tw-wrap tw-split">
<div class="tw-copy">
<p class="tw-eyebrow">Focus</p>
<h2 id="h-focus">Focus, kept apart.</h2>
<p>A timer for short, protected sprints: 25 minutes by default, and you can change the length. It keeps counting when your phone locks, and a notification tells you when a phase ends. <strong>Focus never touches your work records.</strong></p>
<ul class="tw-tags" aria-label="With Tempo Pro"><li>Short and long breaks</li><li>Focus stats</li><li>Your choice of sounds, silence included</li></ul>
<p class="tw-note">Focus cycles, stats and sounds are part of Tempo Pro. The timer itself is not.</p>
</div>
<div class="tw-visual tw-stage tw-object" style="min-height:480px">
<div class="tw-rings" style="--ry:50%" aria-hidden="true"></div>
<div class="tw-dial" role="img" aria-label="A dial showing a 25 minute focus timer"><div><span class="tw-num">25:00</span><small>Focus</small></div></div>
</div>
</div>
</section>

<section class="tw-sec" id="plans" aria-labelledby="h-plans">
<div class="tw-wrap">
<div class="tw-head">
<p class="tw-eyebrow">Free to start</p>
<h2 id="h-plans">Everything you need to keep your own time.</h2>
</div>
<div class="tw-plans">
<div class="tw-plan"><span class="k">Included</span><h3>Tempo</h3>
<ul>
<li>Manual start and stop</li>
<li>Automatic tracking of one place</li>
<li>Corrections to any finished record in History</li>
<li>The last 30 days in Calendar and analytics</li>
<li>Export everything, or erase everything</li>
<li>The Focus timer</li>
<li>Core widgets, Live Activity and Siri</li>
</ul></div>
<div class="tw-plan tw-pro-plan">{topo_use(tw='700px', tx='100%', ty='0%')}<span class="k">Optional</span><h3>Tempo Pro</h3>
<ul>
<li>Dayline and Cards for Today</li>
<li>Insights and animated recaps, with shareable cards</li>
<li>Flexible routines and multiple workplaces</li>
<li>Focus cycles, stats and sounds</li>
<li>Personalized reminders and overtime alerts</li>
</ul></div>
</div>
<p class="tw-buy">Pro is available through in-app purchase, as a subscription or a one-time purchase. Prices, billing periods and any eligible offers are displayed before purchase. Subscriptions renew automatically unless cancelled through your Apple account. Restore Purchases is available in the app.</p>
<div class="tw-good" role="note"><b>Good to know</b><p>Automatic tracking depends on iOS. Background tracking relies on permissions (&ldquo;Always&rdquo; location is needed for automatic starts), device settings, signal and whether the app was force-quit, so delivery is not guaranteed. Tempo is a personal time-tracking tool, not an employer&rsquo;s timekeeping system: review your records before using them for payroll or compliance.</p></div>
</div>
</section>

<section class="tw-stage tw-privacy" id="privacy" aria-labelledby="h-priv">
{topo_use(tw='1300px', tx='50%', ty='50%')}
<div class="tw-wrap">
<p class="tw-eyebrow">Local-first by design</p>
<h2 id="h-priv"><span>No account.</span><span>No ads.</span><span class="d">Your records stay on your iPhone.</span></h2>
<p class="lead">Tempo has no account, no advertising and no developer-operated location backend. Apple services support maps, location and purchases; sharing sends the image only to the destination you choose.</p>
<p class="go"><a href="privacy.html">Read the privacy policy</a></p>
</div>
</section>

<section class="tw-closing" aria-labelledby="h-close">
<div class="tw-wrap">
<img class="tw-icon" src="media/tempo-icon-180.png" width="88" height="88" alt="" decoding="async">
<h2 id="h-close">Make your workday easier to understand.</h2>
<div class="tw-cta">{badge(light_dark=True)}</div>
<p class="tw-fine">Tempo Work for iPhone, iOS 17 or later. Pro is optional.</p>
</div>
</section>
</main>
{footer()}
</body>
</html>
'''


# ------------------------------------------------------------------ legal pages
def _slug(s, used):
    base = re.sub(r'[^a-z0-9]+', '-', re.sub(r'<[^>]+>|&\w+;', '', s).lower()).strip('-')[:40].strip('-') or 's'
    n, i = base, 2
    while n in used: n, i = f'{base}-{i}', i + 1
    used.add(n)
    return n


def legal(key, title_h1, upd, short, secs):
    used, toc, out = set(), [], []
    for i, (h, chunk) in enumerate(secs):
        h = re.sub(r'^\d+\.\s+', '', h.strip())
        sid = _slug(h, used)
        subs = []
        def mark(m):
            q = m.group(1); qid = _slug(q, used); subs.append((qid, q))
            return f'<h3 id="{qid}">{q}</h3>'
        chunk = re.sub(r'<h3>(.*?)</h3>', mark, chunk.strip())
        toc.append((sid, h, subs))
        out.append(f'<h2 id="{sid}"{" class=first" if i == 0 and not short else ""}>{h}</h2>\n{chunk}')
    lis = ''.join(f'<li><a href="#{sid}">{h}</a>' + (('<ul>' + ''.join(f'<li><a href="#{q}">{t}</a></li>' for q, t in subs) + '</ul>') if subs else '') + '</li>'
                  for sid, h, subs in toc)
    sib = ''.join(f'<li><a href="{k}.html"{" aria-current=page" if k == key else ""}>{l}</a></li>' for k, l in LINKS)
    side = (f'<aside class="tw-side" aria-label="On this page"><span class="tw-toc-h">On this page</span><ol class="tw-toc">{lis}</ol>'
            f'<ul class="tw-sib" aria-label="Tempo pages">{sib}<li><a href="./">Back to Tempo</a></li></ul></aside>')
    mside = (f'<details class="tw-mtoc"><summary>On this page</summary><div class="in"><ol class="tw-toc">{lis}</ol>'
             f'<ul class="tw-sib" aria-label="Tempo pages">{sib}<li><a href="./">Back to Tempo</a></li></ul></div></details>')
    cards = ''.join(f'<a href="{k}.html"{" aria-current=page" if k == key else ""}><small>{"You are here" if k == key else "Also"}</small>{l}</a>' for k, l in LINKS)
    summ = f'<div class="tw-short">{short}</div>\n' if short else ''
    topo_art = topo_use(tw='820px', tx='84%', ty='30%')
    return f'''<body class="tw" id="top">
<a class="tw-skip" href="#main">Skip to content</a>
{sprite()}
{bar(key)}
<header class="tw-stage tw-lhero"><div class="tw-rings" style="--ry:140%" aria-hidden="true"></div>{topo_art}
<div class="tw-wrap"><a class="tw-back" href="./"><span aria-hidden="true">&larr;</span> Tempo</a>
<h1>{title_h1}</h1>
<p class="upd">{upd}</p></div></header>
<main id="main"><div class="tw-wrap tw-lgrid">
{side}
<div>
{mside}
<article class="tw-prose">
{summ}{chr(10).join(out)}
<nav class="tw-docnav" aria-label="More from Tempo">{cards}</nav>
</article>
</div>
</div></main>
{footer()}
</body>
</html>
'''


def _split(body):
    take = lambda pat: (lambda m: (m.group(1).strip(), body.replace(m.group(0), '', 1)) if m else ('', body))(re.search(pat, body, re.S))
    h1, body = take(r'<h1>(.*?)</h1>')
    upd, body = take(r'<p class="updated">(.*?)</p>')
    m = re.search(r'<p class="summary">(.*?)</p>', body, re.S)
    short = m.group(1).strip() if m else ''
    if m: body = body.replace(m.group(0), '', 1)
    parts = re.split(r'<h2>(.*?)</h2>', body)
    return h1, upd, short, list(zip(parts[1::2], parts[2::2]))


def page(app, lang, key, title, desc, body, host, alts):
    canon = f'{host}{app["slug"]}/' if key == 'index' else f'{host}{app["slug"]}/{key}.html'
    if key == 'index':
        html = head(title, desc, canon) + home()
    else:
        h1, upd, short, secs = _split(body)
        html = head(title, desc, canon) + legal(key, h1, upd, short, secs)
    bad = isolation(html)
    if bad: raise SystemExit(f'tempo/{key}: link outside the allowed set: {bad}')
    return html
