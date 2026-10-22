"""Cycle Timers' own site for tools/gen_legal_apps.py (slug 'cycle'): home, privacy, terms, support.

Nothing here is shared with the other apps' pages: every class is prefixed `cy-`, the stylesheet is inline, the type
is a system stack (SF Rounded / Avenir Next / Helvetica), and every image is cycle/media/*. Pages link only to each
other, to the App Store listing, to mailto:, and to the vendors and regulators the legal text names.

Identity. Cycle looks like a first-party Apple app: warm paper (#F6F5F1) in light, charcoal (#111211) in dark,
neutral chrome, and colour only where the app has it, in the rings (green, yellow, orange, red). The teal accent
(#0E7C6B light / #3CC9AE dark) is used for fills, marks and a few words; teal text on paper is the darker #0B6B5C.

Home = real screenshots in CSS device frames, the app's own plates behind the hero, the widget band and the close,
an interactive replica of the Large widget (tap a ring, Undo), the template catalogue, the free/Pro split and the
Wrapped card. Legal pages = same header and footer, a sticky table of contents that follows the reader, ~68ch prose.

audit(html) reads the <style> of a generated page and measures every foreground/background pair listed in PAIRS in
light and dark: text >= 4.5:1, ring arcs and UI marks >= 3:1. Text that sits on a plate is measured against the
lightest and darkest pixel the plate can show under its scrim (read from the image file when Pillow is present,
black/white otherwise). gen_legal_apps.py refuses to write a page whose audit fails.
"""
import os
import re

MIN, UIMIN = 4.5, 3.0
SITE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STORE = 'https://apps.apple.com/app/id6796827400'
MAIL = 'hello@seizeapps.com'

# Colours that change with the appearance.
LIGHT = dict(bg='#F6F5F1', bg2='#EEEDE7', card='#FFFFFF', ink='#1C1C1E', lead='#48484A', ink2='#5C5C61',
             accent='#0E7C6B', atext='#0B6B5C', onaccent='#FFFFFF', soft='#E3F0EC',
             btn='#111211', onbtn='#FFFFFF', screen='#F6F5F1', track='#E4E4E2',
             fresh='#1E8E3E', soon='#BD8A00', due='#C5690A', over='#FF3B30', tick='#FFFFFF')
DARK = dict(bg='#111211', bg2='#171918', card='#1D1F1E', ink='#F4F3EF', lead='#D0D0D2', ink2='#A8A8AD',
            accent='#3CC9AE', atext='#3CC9AE', onaccent='#111211', soft='#16302A',
            btn='#F4F3EF', onbtn='#111211', screen='#111211', track='#363837',
            fresh='#30D158', soon='#FFD60A', due='#FF9F0A', over='#FF453A', tick='#111211')
# Colours that are the same in both appearances (surfaces that are always dark, the Wrapped palette).
FIXED = dict(band='#0D3A1D', bandtext='#F4F7F4', bandlead='#D3E3D8', bandeyebrow='#7FE3C9',
             wdg1='#2C2E2D', wdg2='#1A1C1B', wdgtext='#F4F3EF', wdgmuted='#C9CBCA', wdgtoast='#2A2C2B',
             wfresh='#30D158', wsoon='#FFD60A', wdue='#FF9F0A', wover='#FF453A',
             ink_w='#101412', paper_w='#F4F0E7', paperlead_w='#CFC9BC', paperlabel_w='#4F514C', wmint='#7BE6CC',
             wfreshd='#1E8E3E', wsoond='#A87900', wdued='#C5690A', black='#000000', white='#FFFFFF',
             notif='#ECEBE6', notifd='#262827')

# Scrims over plates: (rgb, alpha floor under any text).
HERO_SCRIM_A = 0.85      # alpha of the page colour over the hero plate wherever text sits
CLOSE_SCRIM_A = 0.85
BAND_SCRIM = ((6, 28, 14), 0.78)
LEGAL_PLATE_A = 0.22     # most of the plate that can reach the legal-hero text edge
DARK_PLATE_FILTER = 0.16
DARK_PLATE_OPACITY = 0.9

CSS = r'''
:root{color-scheme:light dark;--shadow:0 1px 2px rgba(28,28,30,.06),0 18px 40px -18px rgba(28,28,30,.22);--line:rgba(60,60,67,.16);--plate-filter:none;--plate-op:.8;
--display:ui-rounded,"SF Pro Rounded","Avenir Next Rounded","Avenir Next",ui-sans-serif,"Helvetica Neue",Helvetica,Arial,sans-serif;
--body:"Avenir Next",ui-sans-serif,"Helvetica Neue",Helvetica,Arial,sans-serif;
/*FIXED*/}
:root{/*LIGHT*/}
@media (prefers-color-scheme:dark){:root{/*DARK*/--shadow:0 1px 2px rgba(0,0,0,.4),0 24px 48px -20px rgba(0,0,0,.7);--line:rgba(235,235,245,.14);--plate-filter:brightness(.16) saturate(.9);--plate-op:.9}}
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;scroll-padding-top:84px}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{transition:none!important;animation:none!important}}
body{margin:0;background:var(--bg);color:var(--ink);font:400 1.0625rem/1.55 var(--body);-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;overflow-wrap:break-word}
img,svg{max-width:100%}
a{color:inherit}
:focus-visible{outline:3px solid var(--accent);outline-offset:3px;border-radius:6px}
.cy-skip{position:absolute;left:12px;top:-60px;background:var(--btn);color:var(--onbtn);padding:10px 16px;border-radius:10px;z-index:100;text-decoration:none;font-weight:600}
.cy-skip:focus{top:12px}
.cy-wrap{width:min(1160px,100% - 48px);margin-inline:auto}
.cy-vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}

/* header */
.cy-head{position:sticky;top:0;z-index:50;background:color-mix(in srgb,var(--bg) 84%,transparent);-webkit-backdrop-filter:saturate(1.6) blur(18px);backdrop-filter:saturate(1.6) blur(18px);border-bottom:1px solid var(--line)}
.cy-head .cy-wrap{display:flex;align-items:center;gap:28px;height:60px}
.cy-brand{display:flex;align-items:center;gap:10px;text-decoration:none;font:700 1.0625rem var(--display);letter-spacing:-.01em}
.cy-brand img{width:30px;height:30px;border-radius:22.37%;box-shadow:0 0 0 1px var(--line)}
.cy-nav{display:flex;gap:26px;margin-left:auto;margin-right:6px}
.cy-nav a{text-decoration:none;font-size:.9375rem;color:var(--ink2);padding:6px 2px}
.cy-nav a:hover,.cy-nav a[aria-current=page]{color:var(--ink)}
.cy-mini{background:var(--btn);color:var(--onbtn);text-decoration:none;font:600 .875rem var(--body);padding:8px 16px;border-radius:999px;white-space:nowrap}
.cy-mini:hover{opacity:.88}
@media (max-width:760px){.cy-nav{display:none}.cy-mini{margin-left:auto}}

/* App Store button */
.cy-store{display:inline-flex;align-items:center;gap:11px;background:#000;color:#fff;text-decoration:none;padding:9px 22px 9px 16px;border-radius:12px;box-shadow:0 0 0 1px rgba(255,255,255,.28) inset,0 10px 24px -10px rgba(0,0,0,.5);transition:transform .25s cubic-bezier(.3,.9,.4,1.2)}
@media (prefers-color-scheme:dark){.cy-store{box-shadow:0 0 0 1px rgba(255,255,255,.55) inset,0 10px 24px -10px rgba(0,0,0,.6)}}
.cy-store:hover{transform:translateY(-2px)}
.cy-store:focus-visible{outline-offset:4px}
.cy-store svg{width:26px;height:26px;fill:#fff;flex:none}
.cy-store span{display:flex;flex-direction:column;line-height:1;text-align:left}
.cy-store small{font:500 .6875rem var(--body);letter-spacing:.01em;margin-bottom:3px}
.cy-store b{font:600 1.5rem/1 var(--body);letter-spacing:-.02em}

/* type */
.cy-eyebrow{font:700 .8125rem var(--body);letter-spacing:.14em;text-transform:uppercase;color:var(--atext);margin:0 0 14px}
.cy-h2{font:800 clamp(2rem,4.6vw,3.6rem)/1.05 var(--display);letter-spacing:-.03em;margin:0 0 20px;text-wrap:balance}
.cy-lede{font-size:clamp(1.0625rem,1.5vw,1.3125rem);font-weight:500;line-height:1.5;color:var(--lead);margin:0 0 18px;max-width:34em;text-wrap:pretty}
.cy-lede strong{color:var(--ink);font-weight:700}
.cy-section{padding:clamp(64px,9vw,128px) 0}

/* hero */
.cy-hero{position:relative;overflow:hidden;text-align:center;padding:clamp(48px,7vw,92px) 0 0}
.cy-hero::before{content:"";position:absolute;inset:0;background:url(media/plate-header.jpg) center 20%/cover no-repeat;filter:var(--plate-filter);opacity:var(--plate-op);z-index:0}
.cy-hero::after{content:"";position:absolute;inset:0;z-index:0;background:radial-gradient(ellipse 56% 52% at 50% 30%,var(--bg) 0%,color-mix(in srgb,var(--bg) /*HEROA*/%,transparent) 55%,transparent 100%),linear-gradient(to bottom,transparent 72%,var(--bg) 100%)}
.cy-hero>*{position:relative;z-index:1}
.cy-mark{width:88px;height:88px;border-radius:22.37%;display:block;margin:0 auto 26px;box-shadow:0 0 0 1px var(--line),0 18px 36px -12px rgba(20,108,54,.5)}
.cy-kicker{margin:0 0 14px;font:700 .8125rem var(--body);letter-spacing:.16em;text-transform:uppercase;color:var(--lead)}
.cy-hero h1{margin:0;font:800 clamp(2.7rem,8.6vw,6.75rem)/.98 var(--display);letter-spacing:-.035em;text-wrap:balance}
.cy-hero .cy-lede{margin:26px auto 0;max-width:27em;font-size:clamp(1.25rem,2vw,1.4375rem);color:var(--lead)}
.cy-hero .cy-lede em{font-style:normal;font-weight:700;color:var(--accent)}
.cy-cta{display:flex;flex-wrap:wrap;gap:18px 24px;justify-content:center;align-items:center;margin-top:34px}
.cy-cta p{margin:0;color:var(--lead);font-size:.9375rem}
.cy-stage{display:flex;justify-content:center;align-items:flex-start;gap:clamp(18px,2.6vw,36px);margin-top:clamp(44px,6vw,72px);height:clamp(400px,50vw,740px);overflow:hidden;padding-top:6px}
.cy-stage .cy-phone{flex:none}
.cy-stage .cy-s1,.cy-stage .cy-s3{--w:clamp(140px,19vw,278px);margin-top:clamp(40px,6vw,88px)}
.cy-stage .cy-s2{--w:clamp(190px,24.5vw,350px)}
@media (max-width:640px){
  .cy-stage{justify-content:flex-start;padding-left:24px;gap:16px;height:clamp(380px,112vw,470px)}
  .cy-stage .cy-s1{display:none}
  .cy-stage .cy-s2,.cy-stage .cy-s3{--w:min(236px,60vw)}
  .cy-stage .cy-s3{margin-top:34px}
  .cy-hero::after{background:radial-gradient(ellipse 130% 70% at 50% 34%,var(--bg) 0%,color-mix(in srgb,var(--bg) /*HEROA*/%,transparent) 60%,transparent 100%),linear-gradient(to bottom,transparent 72%,var(--bg) 100%)}
}

/* phone + tablet frames */
.cy-phone{--w:300px;position:relative;margin:0;width:var(--w);padding:calc(var(--w)*.03);border-radius:calc(var(--w)*.165);background:linear-gradient(145deg,#4a4b4e 0%,#141415 22%,#050505 60%,#2d2e30 100%);box-shadow:0 0 0 1px rgba(0,0,0,.55),0 0 0 calc(var(--w)*.006) rgba(255,255,255,.07) inset,0 40px 70px -26px rgba(10,30,18,.45),0 14px 28px -14px rgba(10,30,18,.3)}
.cy-phone::before,.cy-phone::after{content:"";position:absolute;width:calc(var(--w)*.012);background:#2b2c2e;border-radius:2px}
.cy-phone::before{left:calc(var(--w)*-.009);top:19%;height:calc(var(--w)*.17);box-shadow:0 calc(var(--w)*.22) 0 #2b2c2e}
.cy-phone::after{right:calc(var(--w)*-.009);top:27%;height:calc(var(--w)*.26)}
.cy-phone img{display:block;width:100%;height:auto;aspect-ratio:680/1480;object-fit:cover;border-radius:calc(var(--w)*.135);background:var(--screen)}
.cy-pad{--w:520px;position:relative;margin:0;width:var(--w);max-width:100%;padding:calc(var(--w)*.032);border-radius:calc(var(--w)*.06);background:linear-gradient(145deg,#4a4b4e,#0a0a0b 30%,#050505 70%,#2d2e30);box-shadow:0 0 0 1px rgba(0,0,0,.55),0 40px 70px -26px rgba(10,30,18,.45)}
.cy-pad img{display:block;width:100%;height:auto;aspect-ratio:1050/1400;object-fit:cover;border-radius:calc(var(--w)*.03);background:var(--screen)}

/* spec strip */
.cy-spec{border-top:1px solid var(--line);border-bottom:1px solid var(--line);background:var(--card)}
.cy-spec dl{display:grid;grid-template-columns:repeat(4,1fr);margin:0}
.cy-spec dl>div{padding:22px 24px;border-left:1px solid var(--line)}
.cy-spec dl>div:first-child{border-left:0;padding-left:0}
.cy-spec dt{font:700 .75rem var(--body);letter-spacing:.14em;text-transform:uppercase;color:var(--ink2);margin:0 0 6px}
.cy-spec dd{margin:0;font:700 1.125rem/1.25 var(--display);letter-spacing:-.01em}
@media (max-width:760px){.cy-spec dl{grid-template-columns:1fr 1fr}.cy-spec dl>div{padding:16px 14px;border-left:0;border-top:1px solid var(--line)}.cy-spec dl>div:nth-child(-n+2){border-top:0}.cy-spec dl>div:nth-child(even){border-left:1px solid var(--line);padding-left:18px}.cy-spec dl>div:nth-child(odd){padding-left:0}}

/* statement */
.cy-statement{padding:clamp(72px,10vw,136px) 0 clamp(8px,2vw,24px);text-align:center}
.cy-statement p{margin:0 auto;max-width:17em;font:800 clamp(1.9rem,5.2vw,4.1rem)/1.1 var(--display);letter-spacing:-.03em;color:var(--ink2);text-wrap:balance}
.cy-statement p em{font-style:normal;color:var(--ink)}

/* split */
.cy-split{display:grid;grid-template-columns:1fr 1fr;gap:clamp(40px,7vw,110px);align-items:center}
.cy-split.cy-rev .cy-copy{order:2}
.cy-visual{display:flex;justify-content:center;align-items:center;position:relative}
.cy-glow{position:absolute;inset:6% 4%;border-radius:50%;background:radial-gradient(closest-side,color-mix(in srgb,var(--fresh) 22%,transparent),transparent);filter:blur(10px);z-index:0}
.cy-visual>*{position:relative;z-index:1}
.cy-visual>.cy-glow{position:absolute}
@media (max-width:860px){.cy-split{grid-template-columns:1fr;gap:44px}.cy-split.cy-rev .cy-copy{order:0}}

/* rings */
.cy-ring{display:block;flex:none}
.cy-ring .t{fill:none;stroke:var(--track)}
.cy-ring .a{fill:none;stroke-linecap:round;transition:stroke-dashoffset .6s cubic-bezier(.3,.9,.3,1.1)}
.cy-ring text{font-family:var(--display);font-weight:800;fill:var(--ink);font-variant-numeric:tabular-nums;text-anchor:middle}
.cy-ring .u{font-weight:600;font-size:11px;fill:var(--ink2)}
.c-fresh{stroke:var(--fresh)}.c-soon{stroke:var(--soon)}.c-due{stroke:var(--due)}.c-over{stroke:var(--over)}
.cy-states{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin:30px 0 0;padding:0;list-style:none;max-width:32em}
.cy-states li{display:flex;align-items:center;gap:14px;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:12px 16px;box-shadow:var(--shadow)}
.cy-states strong{display:block;font:700 1rem/1.2 var(--display)}
.cy-states span{display:block;font-size:.875rem;color:var(--ink2);line-height:1.3}
@media (max-width:640px){.cy-states{grid-template-columns:1fr}}

/* dark band */
.cy-band{position:relative;overflow:hidden;color:var(--bandtext);background:var(--band);isolation:isolate}
.cy-band::before{content:"";position:absolute;inset:0;background:url(media/plate-glance.jpg) center/cover no-repeat;z-index:-2}
.cy-band::after{content:"";position:absolute;inset:0;z-index:-1;background:rgba(/*BANDRGB*/,/*BANDA*/)}
.cy-band .cy-eyebrow{color:var(--bandeyebrow)}
.cy-band .cy-lede{color:var(--bandlead)}
.cy-band .cy-lede strong,.cy-band .cy-h2{color:#fff}
.cy-band :focus-visible{outline-color:var(--bandeyebrow)}
.cy-matrix{list-style:none;margin:28px 0 0;padding:0;max-width:30em;border-top:1px solid rgba(255,255,255,.28)}
.cy-matrix li{display:flex;justify-content:space-between;align-items:center;gap:16px;padding:13px 0;border-bottom:1px solid rgba(255,255,255,.28);font-size:1.0625rem}
.cy-matrix small{display:block;font-size:.875rem;color:var(--bandlead)}
.cy-tagp{font:700 .75rem var(--body);letter-spacing:.08em;text-transform:uppercase;border:1px solid currentColor;border-radius:6px;padding:2px 8px;white-space:nowrap}
.cy-realwidget{margin:0;width:min(100%,420px);border-radius:34px;box-shadow:0 36px 60px -24px rgba(0,0,0,.65)}
.cy-realwidget img{display:block;width:100%;height:auto;border-radius:34px;background:var(--wdg2)}
.cy-widget{width:min(100%,400px);border-radius:34px;padding:18px 18px 16px;background:linear-gradient(160deg,var(--wdg1),var(--wdg2));color:var(--wdgtext);box-shadow:0 0 0 1px rgba(255,255,255,.1) inset,0 36px 60px -24px rgba(0,0,0,.65);font-family:var(--display)}
.cy-widget .cy-ring text{fill:var(--wdgtext)}.cy-widget .cy-ring .u{fill:var(--wdgmuted)}.cy-widget .cy-ring .t{stroke:rgba(235,235,245,.18)}
.cy-widget .c-fresh{stroke:var(--wfresh)}.cy-widget .c-soon{stroke:var(--wsoon)}.cy-widget .c-due{stroke:var(--wdue)}.cy-widget .c-over{stroke:var(--wover)}
.cy-widget header{display:flex;justify-content:space-between;align-items:center;font:600 .8125rem var(--body);color:var(--wdgmuted);margin-bottom:12px}
.cy-widget header>b{display:flex;align-items:center;gap:7px;font-weight:600;color:var(--wdgtext)}
.cy-widget .g{display:grid;grid-template-columns:repeat(3,1fr);gap:14px 6px}
.cy-widget button{all:unset;display:flex;flex-direction:column;align-items:center;gap:3px;cursor:pointer;border-radius:16px;padding:4px 0;text-align:center}
.cy-widget button:focus-visible{outline:3px solid var(--bandeyebrow);outline-offset:2px}
.cy-widget button .n{font:700 .8125rem var(--body);color:var(--wdgtext);margin-top:3px}
.cy-widget button .s{font:500 .6875rem var(--body);color:var(--wdgmuted)}
.cy-widget button svg{width:92%;max-width:96px;height:auto}
.cy-widget footer{margin-top:14px;text-align:center;font:600 .6875rem var(--body);letter-spacing:.2em;color:var(--wdgmuted)}
.cy-demo{display:flex;flex-direction:column;align-items:center;gap:16px;width:100%}
.cy-demo-bar{display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:10px 16px;min-height:44px;font-size:.9375rem;color:var(--bandlead);text-align:center}
.cy-demo-bar button{all:unset;cursor:pointer;font:700 .875rem var(--body);color:var(--bandeyebrow);text-decoration:underline;text-underline-offset:3px;border-radius:4px;padding:6px 4px}
.cy-demo-bar button:focus-visible{outline:3px solid var(--bandeyebrow);outline-offset:3px}
.cy-toast{display:inline-flex;align-items:center;gap:10px;background:var(--wdgtoast);color:var(--wdgtext);border-radius:999px;padding:9px 16px;font:600 .875rem var(--body);box-shadow:0 14px 30px -12px rgba(0,0,0,.5)}
.cy-toast i{width:16px;height:16px;border-radius:50%;background:var(--wfresh);display:inline-block;flex:none}
.cy-toast u{text-decoration:none;color:var(--bandeyebrow);margin-left:6px;font-weight:700}
.cy-count{font:600 .8125rem var(--body);color:var(--wdgmuted);white-space:nowrap}
.cy-count b{font-family:var(--display);font-weight:800;color:var(--wdgtext)}
.cy-row{margin-top:clamp(64px,9vw,120px)}
.cy-band .cy-split+.cy-split{margin-top:clamp(64px,9vw,120px)}
@media (max-width:860px){.cy-desktop-only{display:none}}

/* templates */
.cy-templates{margin-top:clamp(52px,7vw,88px);display:grid;grid-template-columns:repeat(5,1fr);gap:14px;align-items:start}
.cy-templates section{background:var(--card);border:1px solid var(--line);border-radius:22px;padding:20px 20px 16px;box-shadow:var(--shadow)}
.cy-templates h3{font:800 1.125rem var(--display);letter-spacing:-.015em;margin:0 0 12px}
.cy-templates ul{list-style:none;margin:0;padding:0}
.cy-templates li{display:flex;flex-direction:column;padding:9px 0;border-top:1px solid var(--line);font-size:.9375rem;line-height:1.3}
.cy-templates li:first-child{border-top:0}
.cy-templates li span{font-size:.8125rem;color:var(--ink2)}
.cy-templates .lead{border-color:color-mix(in srgb,var(--accent) 55%,var(--line))}
.cy-note{font-size:.9375rem;color:var(--ink2);margin:18px 0 0}
.cy-swipe{display:none;margin:0;font:600 .8125rem var(--body);letter-spacing:.02em;color:var(--ink2)}
@media (max-width:1100px){.cy-templates{grid-template-columns:repeat(3,1fr)}}
@media (max-width:700px){
  .cy-templates{display:flex;align-items:stretch;overflow-x:auto;scroll-snap-type:x mandatory;gap:12px;margin-inline:-24px;padding:6px 24px 22px;scroll-padding-left:24px;-webkit-overflow-scrolling:touch}
  .cy-templates section{flex:0 0 min(76%,290px);scroll-snap-align:start}
  .cy-templates:focus-visible{outline-offset:-3px}
  .cy-note{margin-top:0}
  .cy-swipe{display:block;margin:-8px 0 18px}
}
.cy-duo{display:flex;align-items:center}
.cy-duo .cy-phone:first-child{--w:clamp(150px,21vw,258px);margin-right:clamp(-30px,-2.5vw,-14px);transform:translateY(18px)}
.cy-duo .cy-phone:last-child{--w:clamp(160px,23vw,284px);z-index:2}
@media (max-width:860px){.cy-duo .cy-phone:first-child{display:none}.cy-duo .cy-phone:last-child{--w:min(290px,66vw)}}

/* calm + bento */
.cy-calm{background:var(--bg2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.cy-checks{list-style:none;margin:26px 0 0;padding:0;display:grid;gap:14px;max-width:32em}
.cy-checks li{display:grid;grid-template-columns:22px 1fr;gap:12px;font-size:1rem;line-height:1.45}
.cy-checks svg{width:22px;height:22px;margin-top:1px}
.cy-checks svg path{fill:none;stroke:var(--accent);stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
.cy-bento{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:clamp(48px,7vw,80px)}
.cy-card{background:var(--card);border:1px solid var(--line);border-radius:28px;padding:30px;box-shadow:var(--shadow);display:flex;flex-direction:column;gap:10px;position:relative;overflow:hidden}
.cy-card h3{font:800 1.5rem/1.1 var(--display);letter-spacing:-.02em;margin:0}
.cy-card p{margin:0;color:var(--ink2);font-size:1rem}
.cy-card .cy-mock{margin-top:auto;padding-top:20px}
.cy-pill{display:inline-flex;align-items:center;gap:10px;background:var(--bg2);border:1px solid var(--line);border-radius:999px;padding:11px 18px;font:600 .9375rem var(--body)}
.cy-pill svg{width:20px;height:20px;flex:none}
.cy-pill svg *{fill:none;stroke:var(--accent);stroke-width:2;stroke-linecap:round}
.cy-notif{background:var(--notif);border:1px solid var(--line);border-radius:22px;padding:14px 16px;display:grid;grid-template-columns:42px 1fr;gap:4px 12px;align-items:start}
.cy-notif img{width:42px;height:42px;border-radius:22.37%;grid-row:span 2}
.cy-notif strong{display:flex;justify-content:space-between;gap:8px;font-size:.9375rem;line-height:1.3;color:#1C1C1E}
.cy-notif strong span{font-weight:500;font-size:.8125rem;color:#5C5C61}
.cy-notif p{margin:0;font-size:.9375rem;line-height:1.35;color:#1C1C1E}
.cy-notif-act{grid-column:1/-1;margin-top:8px;display:flex}
.cy-notif-act span{flex:1;text-align:center;padding:10px;border-radius:14px;background:var(--accent);color:var(--onaccent);font:700 .9375rem var(--body)}
@media (prefers-color-scheme:dark){.cy-notif{background:var(--notifd)}.cy-notif strong,.cy-notif p{color:#F4F3EF}.cy-notif strong span{color:#B4B8B6}}
.cy-picks{display:flex;gap:12px}.cy-pick{position:relative;display:inline-block}.cy-pick b{position:absolute;right:-4px;top:-4px;width:22px;height:22px;border-radius:50%;background:var(--ink);color:var(--bg);font:700 .75rem/22px var(--body);text-align:center}.cy-pickempty{width:56px;height:56px;border-radius:50%;border:2px dashed var(--ink2)}
@media (max-width:900px){
  .cy-bento{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:12px;margin-inline:-24px;padding:6px 24px 22px;scroll-padding-left:24px}
  .cy-card{flex:0 0 min(80%,320px);scroll-snap-align:start}
  .cy-bento:focus-visible{outline-offset:-3px}
  .cy-swipe{display:block;margin:-8px 0 0}
}

/* pricing */
.cy-price{background:var(--bg2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.cy-price-head{text-align:center;max-width:40rem;margin:0 auto clamp(40px,6vw,64px)}
.cy-price-head .cy-lede{margin-inline:auto}
.cy-plans{display:grid;grid-template-columns:1fr 1fr;gap:18px;align-items:stretch}
.cy-plan{background:var(--card);border:1px solid var(--line);border-radius:30px;padding:clamp(26px,3.4vw,40px);box-shadow:var(--shadow);display:flex;flex-direction:column}
.cy-plan h3{font:800 1.75rem/1.1 var(--display);letter-spacing:-.025em;margin:0 0 6px}
.cy-plan .sub{color:var(--ink2);margin:0 0 20px}
.cy-plan .cy-checks{margin:0;max-width:none}
.cy-fourrings{margin-top:auto;padding-top:28px;display:flex;gap:14px}
.cy-plan.pro{border-color:color-mix(in srgb,var(--accent) 60%,var(--line));box-shadow:0 0 0 1px color-mix(in srgb,var(--accent) 35%,transparent),var(--shadow)}
.cy-tag{align-self:flex-start;background:var(--accent);color:var(--onaccent);font:700 .75rem var(--body);letter-spacing:.1em;text-transform:uppercase;padding:4px 10px;border-radius:999px;margin-bottom:14px}
.cy-tag.free{background:var(--bg2);color:var(--ink);box-shadow:0 0 0 1px var(--ink2) inset}
.cy-fine{text-align:center;color:var(--ink2);font-size:.9375rem;margin:26px auto 0;max-width:40em}
@media (max-width:900px){.cy-plans{grid-template-columns:1fr}}

/* wrapped */
.cy-wrapped{margin-top:18px;border-radius:36px;background:var(--ink_w);color:var(--paper_w);padding:clamp(30px,5vw,64px);display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(32px,6vw,80px);align-items:center;overflow:hidden}
.cy-wrapped .cy-eyebrow{color:var(--wmint)}
.cy-wrapped h3{font:800 clamp(2rem,4.2vw,3.25rem)/1.05 var(--display);letter-spacing:-.03em;margin:0 0 18px;color:var(--paper_w)}
.cy-wrapped p{margin:0;color:var(--paperlead_w);font-size:1.0625rem;max-width:30em}
.cy-wcard{justify-self:center;width:min(100%,330px);aspect-ratio:4/5;border-radius:34px;background:var(--paper_w);color:var(--ink_w);position:relative;overflow:hidden;box-shadow:0 40px 80px -30px rgba(0,0,0,.7);transform:rotate(3deg)}
.cy-wcard svg{position:absolute;left:15%;top:7%;width:70%;height:auto;transform:rotate(-90deg)}
.cy-wcard circle{fill:none;stroke-width:6.5;stroke-linecap:round}
.cy-wcard .t{stroke:rgba(16,20,18,.1)}
.cy-wcard figcaption{position:absolute;left:26px;right:26px;bottom:24px;font:800 1.75rem/1.05 var(--display);letter-spacing:-.02em}
.cy-wcard small{display:block;font:700 .75rem/1 var(--body);letter-spacing:.14em;text-transform:uppercase;color:var(--paperlabel_w);margin-bottom:10px}
@media (max-width:900px){.cy-wrapped{grid-template-columns:1fr;border-radius:28px}.cy-wcard{transform:rotate(2deg);width:min(100%,290px)}}

/* private */
.cy-private{display:grid;grid-template-columns:auto 1fr;gap:clamp(24px,4vw,56px);align-items:center}
.cy-private .cy-h2{font-size:clamp(1.8rem,3.6vw,2.7rem);margin-bottom:12px}
.cy-lock{width:96px;height:96px;border-radius:28px;background:var(--soft);display:grid;place-items:center;border:1px solid color-mix(in srgb,var(--accent) 35%,transparent)}
.cy-lock svg{width:46px;height:46px}.cy-lock svg *{fill:none;stroke:var(--accent);stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.cy-private a{color:var(--atext);text-underline-offset:3px}
@media (max-width:640px){.cy-private{grid-template-columns:1fr}}

/* closing */
.cy-close{position:relative;overflow:hidden;text-align:center;isolation:isolate}
.cy-close::before{content:"";position:absolute;inset:0;background:url(media/plate-search.jpg) center/cover no-repeat;filter:var(--plate-filter);opacity:var(--plate-op);z-index:-2}
.cy-close::after{content:"";position:absolute;inset:0;z-index:-1;background:radial-gradient(ellipse 100% 100% at 50% 50%,var(--bg) 0%,color-mix(in srgb,var(--bg) /*CLOSEA*/%,transparent) 60%,transparent 100%)}
.cy-close .cy-h2{font-size:clamp(2.3rem,6vw,4.5rem);margin-inline:auto;max-width:12em}
.cy-close .cy-lede{margin-inline:auto}

/* footer */
.cy-foot{border-top:1px solid var(--line);padding:56px 0 40px;color:var(--ink2);font-size:.9375rem;background:var(--bg)}
.cy-foot-grid{display:grid;grid-template-columns:1.35fr 1fr 1fr 1.2fr;gap:36px 40px}
.cy-foot3{grid-template-columns:1.6fr 1fr 1.2fr}
.cy-foot h2{font:700 .75rem var(--body);letter-spacing:.14em;text-transform:uppercase;color:var(--ink2);margin:0 0 14px}
.cy-foot ul{list-style:none;margin:0;padding:0;display:grid;gap:4px}
.cy-foot a{color:var(--ink);text-decoration:none;display:inline-block;padding:5px 0}
.cy-foot a:hover{text-decoration:underline;text-underline-offset:4px}
.cy-foot .brand{display:flex;align-items:center;gap:10px;font:700 1.0625rem var(--display);color:var(--ink);margin:0 0 12px}
.cy-foot .brand img{width:34px;height:34px;border-radius:22.37%;box-shadow:0 0 0 1px var(--line)}
.cy-foot p{margin:0 0 8px;max-width:26em}
.cy-pillnext{display:inline-block;font:700 .6875rem var(--body);letter-spacing:.1em;text-transform:uppercase;color:var(--atext);background:var(--soft);border:1px solid color-mix(in srgb,var(--accent) 45%,transparent);border-radius:999px;padding:4px 11px;margin-bottom:10px}
.cy-foot-end{margin-top:40px;padding-top:22px;border-top:1px solid var(--line);display:flex;flex-wrap:wrap;gap:8px 28px;justify-content:space-between;font-size:.8125rem}
.cy-foot-end p{margin:0;max-width:none}
@media (max-width:980px){.cy-foot-grid,.cy-foot3{grid-template-columns:1fr 1fr}}
@media (max-width:520px){.cy-foot-grid,.cy-foot3{grid-template-columns:1fr 1fr}.cy-foot-grid>:first-child,.cy-foot-grid>:last-child{grid-column:1/-1}}

/* legal */
.cy-lhero{position:relative;overflow:hidden;padding:clamp(40px,6vw,72px) 0 clamp(28px,4vw,44px);border-bottom:1px solid var(--line);isolation:isolate}
.cy-lhero::before{content:"";position:absolute;top:0;right:0;bottom:0;width:min(46%,560px);background:url(media/plate-header.jpg) 80% 40%/cover no-repeat;filter:var(--plate-filter);opacity:/*LPLATE*/;-webkit-mask-image:linear-gradient(to right,transparent 0%,#000 70%);mask-image:linear-gradient(to right,transparent 0%,#000 70%);z-index:-1}
.cy-narrow{width:min(1060px,100% - 48px)}
.cy-lhero h1{font:800 clamp(2.4rem,6vw,4.25rem)/1 var(--display);letter-spacing:-.035em;margin:0 0 14px}
.cy-updated{color:var(--lead);margin:0 0 22px;font-size:1.0625rem}
.cy-switch{display:flex;flex-wrap:wrap;gap:8px;margin:0;padding:0;list-style:none}
.cy-switch a{display:inline-block;text-decoration:none;font:600 .9375rem var(--body);padding:8px 16px;border-radius:999px;border:1px solid var(--ink2);color:var(--ink)}
.cy-switch a:hover{background:var(--card)}
.cy-switch a[aria-current=page]{background:var(--btn);color:var(--onbtn);border-color:var(--btn)}
.cy-legal{display:grid;grid-template-columns:250px minmax(0,1fr);gap:clamp(32px,6vw,84px);padding:clamp(36px,5vw,64px) 0 clamp(72px,9vw,120px);align-items:start}
.cy-rail{position:sticky;top:84px;max-height:calc(100vh - 104px);overflow:auto;font-size:.9375rem;padding-right:6px}
.cy-back{display:inline-flex;align-items:center;gap:8px;text-decoration:none;color:var(--atext);font-weight:700;font-size:.9375rem;margin:0 0 22px;padding:4px 0}
.cy-back:hover{text-decoration:underline;text-underline-offset:4px}
.cy-back svg{width:16px;height:16px}.cy-back svg *{fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.cy-rail h2{font:700 .75rem var(--body);letter-spacing:.14em;text-transform:uppercase;color:var(--ink2);margin:0 0 12px}
.cy-toc ol,.cy-tocm ol{list-style:none;margin:0;padding:0}
.cy-toc>ol{border-left:1px solid var(--line)}
.cy-toc a{display:block;padding:6px 0 6px 16px;margin-left:-1px;border-left:2px solid transparent;text-decoration:none;color:var(--ink2);line-height:1.35}
.cy-toc ol ol a{padding-left:30px;font-size:.875rem}
.cy-toc a:hover{color:var(--ink);border-left-color:var(--ink2)}
.cy-toc a.on{color:var(--ink);font-weight:700;border-left-color:var(--accent)}
.cy-tocm{display:none;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:0 16px}
.cy-tocm summary{cursor:pointer;padding:14px 0;font-weight:700;list-style:none;display:flex;justify-content:space-between;align-items:center}
.cy-tocm summary::-webkit-details-marker{display:none}
.cy-tocm summary::after{content:"+";font-size:1.25rem;line-height:1}
.cy-tocm[open] summary::after{content:"\2212"}
.cy-tocm[open] summary{border-bottom:1px solid var(--line);margin-bottom:8px}
.cy-tocm a{display:block;padding:8px 0;text-decoration:none;color:var(--ink);line-height:1.35}
.cy-tocm a.on{color:var(--atext);font-weight:700}
.cy-tocm ol ol a{padding-left:16px;font-size:.9375rem;color:var(--ink2)}
.cy-tocm ol{padding-bottom:10px}
@media (max-width:900px){
  .cy-legal{grid-template-columns:1fr;gap:28px}
  .cy-rail{position:static;max-height:none;overflow:visible;padding:0}
  .cy-toc{display:none}.cy-tocm{display:block}
  .cy-rail .cy-back{margin-bottom:14px}
}
.cy-prose{max-width:68ch;font-size:1.0625rem;line-height:1.65}
.cy-summary{background:var(--card);border:1px solid var(--line);border-radius:24px;padding:26px 28px;margin:0 0 44px;box-shadow:var(--shadow)}
.cy-prose .cy-summary h2{font:800 1.25rem var(--display);margin:0 0 14px;letter-spacing:-.02em;border:0;padding:0}
.cy-summary ul{list-style:none;margin:0;padding:0;display:grid;gap:12px}
.cy-summary li{display:grid;grid-template-columns:22px 1fr;gap:12px;line-height:1.55;margin:0}
.cy-summary li svg{width:22px;height:22px;margin-top:3px}.cy-summary li svg path{fill:none;stroke:var(--accent);stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
.cy-prose h2{font:800 1.625rem/1.2 var(--display);letter-spacing:-.025em;margin:2.5em 0 .7em;padding-top:1.3em;border-top:1px solid var(--line)}
.cy-prose>h2:first-child,.cy-prose>.cy-summary+h2{margin-top:0;border-top:0;padding-top:0}
.cy-prose h3{font:700 1.1875rem/1.3 var(--display);letter-spacing:-.01em;margin:1.8em 0 .45em}
.cy-prose p{margin:0 0 1.1em;text-wrap:pretty}
.cy-prose ul,.cy-prose ol{margin:0 0 1.1em;padding-left:1.3em}
.cy-prose li{margin:0 0 .45em}
.cy-prose a{color:var(--atext);text-underline-offset:3px;text-decoration-thickness:1px}
.cy-prose a:hover{text-decoration-thickness:2px}
.cy-prose strong{font-weight:700}
.cy-prose .contact{font:700 1.375rem/1.3 var(--display)}
.cy-prose h2,.cy-prose h3{scroll-margin-top:84px}
@media (max-width:640px){
  .cy-wrap{width:min(1160px,100% - 40px)}.cy-narrow{width:min(1060px,100% - 40px)}
  .cy-store b{font-size:1.375rem}
  .cy-section{padding:64px 0}
  .cy-summary{padding:22px 20px}
  .cy-lhero::before{width:60%}
  .cy-hide-m,.cy-lock{display:none}
  .cy-crop-m{height:430px;overflow:hidden;align-items:flex-start;-webkit-mask-image:linear-gradient(#000 78%,transparent);mask-image:linear-gradient(#000 78%,transparent)}
  .cy-wcard{width:min(100%,180px)}
  .cy-plan:not(.pro) .sub{display:none}
  .cy-plan{padding:24px 22px}
  .cy-plan h3{margin-bottom:16px}
  .cy-price-head{margin-bottom:28px}
  .cy-pad{--w:min(520px,80vw)!important}
  .cy-split{gap:32px}
  .cy-h2{margin-bottom:14px}
  .cy-matrix li{padding:10px 0}
  .cy-hero{padding-top:40px}
  .cy-mark{width:76px;height:76px;margin-bottom:20px}
  .cy-states{grid-template-columns:1fr 1fr;gap:10px}
  .cy-states li{flex-direction:column;align-items:flex-start;gap:8px;padding:14px}
  .cy-fourrings{display:none}
  .cy-section{padding:56px 0}
  .cy-statement{padding:56px 0 0}
  .cy-wrapped{padding:28px 22px}.cy-wcard{width:min(100%,250px)}
  .cy-visual .cy-phone{--w:min(260px,64vw)!important}
  .cy-bento{margin-inline:-20px;padding-inline:20px;scroll-padding-left:20px}
  .cy-templates{margin-inline:-20px;padding-inline:20px;scroll-padding-left:20px}
}
'''

# (label, foreground, background, minimum). A spec is a variable name, '#hex', ('mix', top, alpha, base) or
# ('plate', scrimvar, alpha, 'dark'|'light', plate file, mode-filtered) -- see _color().
PAIRS = []


def _add(label, fg, bg, mn=MIN):
    PAIRS.append((label, fg, bg, mn))


for _bg in ('bg', 'bg2', 'card', 'soft'):
    _add(f'body text on {_bg}', 'ink', _bg)
    _add(f'secondary text on {_bg}', 'ink2', _bg)
    _add(f'link/eyebrow text on {_bg}', 'atext', _bg)
for _bg in ('bg', 'bg2', 'card'):
    _add(f'lead text on {_bg}', 'lead', _bg)
_add('"one ring each" teal on page', 'accent', 'bg')
_add('label on teal fill (tags, buttons)', 'onaccent', 'accent')
_add('page-switch / mini button label', 'onbtn', 'btn')
_add('focus ring on page', 'accent', 'bg', UIMIN)
_add('focus ring on card', 'accent', 'card', UIMIN)
_add('check marks on card', 'accent', 'card', UIMIN)
_add('App Store button label', 'white', 'black')
_add('App Store button edge against the page', 'storeedge', 'bg', UIMIN)
_add('switch pill border on page', 'ink2', 'bg', UIMIN)
for _s in ('fresh', 'soon', 'due', 'over'):
    _add(f'{_s} ring arc on card', _s, 'card', UIMIN)
_add('fresh ring text label on card', 'ink', 'card')
# plates (hero and close: the page colour at >= .85 over the plate; legal hero edge; band)
for _kind in ('dark', 'light'):
    for _fg, _n in (('ink', 'ink'), ('lead', 'lead'), ('atext', 'teal eyebrow/links')):
        _add(f'hero {_n} over plate ({_kind} pixel)', _fg, ('plate', 'bg', HERO_SCRIM_A, _kind, 'plate-header.jpg'))
    _add(f'hero "one ring each" (23px bold = large text) over plate ({_kind} pixel)', 'accent', ('plate', 'bg', HERO_SCRIM_A, _kind, 'plate-header.jpg'), UIMIN)
    _add(f'close ink over plate ({_kind} pixel)', 'ink', ('plate', 'bg', CLOSE_SCRIM_A, _kind, 'plate-search.jpg'))
    _add(f'close lead over plate ({_kind} pixel)', 'lead', ('plate', 'bg', CLOSE_SCRIM_A, _kind, 'plate-search.jpg'))
    _add(f'legal title over plate edge ({_kind} pixel)', 'ink', ('plate', 'bg', 1 - LEGAL_PLATE_A, _kind, 'plate-header.jpg'))
    _add(f'legal subtitle over plate edge ({_kind} pixel)', 'lead', ('plate', 'bg', 1 - LEGAL_PLATE_A, _kind, 'plate-header.jpg'))
    for _fg in ('bandtext', 'bandlead', 'bandeyebrow', 'white'):
        _add(f'band {_fg} over plate ({_kind} pixel)', _fg, ('bandplate', _kind))
# the always-dark widget demo, toast, band controls
for _fg in ('wdgtext', 'wdgmuted'):
    for _bg in ('wdg1', 'wdg2'):
        _add(f'widget {_fg} on {_bg}', _fg, _bg)
for _s in ('wfresh', 'wsoon', 'wdue', 'wover'):
    _add(f'widget ring arc {_s}', _s, 'wdg1', UIMIN)
_add('toast text', 'wdgtext', 'wdgtoast')
_add('toast Undo', 'bandeyebrow', 'wdgtoast')
_add('toast dot', 'wfresh', 'wdgtoast', UIMIN)
# Wrapped
_add('Wrapped heading on ink', 'paper_w', 'ink_w')
_add('Wrapped body on ink', 'paperlead_w', 'ink_w')
_add('Wrapped eyebrow on ink', 'wmint', 'ink_w')
_add('Wrapped card title on paper', 'ink_w', 'paper_w')
_add('Wrapped card label on paper', 'paperlabel_w', 'paper_w')
for _s in ('wfreshd', 'wsoond', 'wdued'):
    _add(f'Wrapped ring {_s} on paper', _s, 'paper_w', UIMIN)
# notification mock
_add('notification title', ('fixed', '#1C1C1E'), 'notif_l')
_add('notification time', ('fixed', '#5C5C61'), 'notif_l')
_add('notification title (dark)', ('fixed', '#F4F3EF'), 'notif_d')
_add('notification time (dark)', ('fixed', '#B4B8B6'), 'notif_d')
_add('notification Mark Done label', 'onaccent', 'accent')
_add('pick badge', 'bg', 'ink')


def css():
    f = lambda d: ''.join(f'--{k}:{v};' for k, v in d.items())
    out = CSS.replace('/*FIXED*/', f(FIXED)).replace('/*LIGHT*/', f(LIGHT)).replace('/*DARK*/', f(DARK))
    out = out.replace('/*HEROA*/', str(round(HERO_SCRIM_A * 100))).replace('/*CLOSEA*/', str(round(CLOSE_SCRIM_A * 100)))
    out = out.replace('/*BANDRGB*/', ','.join(map(str, BAND_SCRIM[0]))).replace('/*BANDA*/', str(BAND_SCRIM[1]))
    out = out.replace('/*LPLATE*/', str(LEGAL_PLATE_A))
    return out


# ---------------------------------------------------------------- audit
def _vars(block):
    return dict(re.findall(r'--([a-z0-9_]+):(#[0-9A-Fa-f]{6})', block))


def _rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _hex(c):
    return '#%02X%02X%02X' % tuple(max(0, min(255, round(v))) for v in c)


def _blend(top, a, base):
    t, b = _rgb(top), _rgb(base)
    return _hex([t[i] * a + b[i] * (1 - a) for i in range(3)])


def _lum(h):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = _rgb(h)
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def _ratio(a, b):
    la, lb = _lum(a), _lum(b)
    if la < lb:
        la, lb = lb, la
    return (la + 0.05) / (lb + 0.05)


_PLATES = {}


def _plate_extremes(name):
    """(darkest, lightest) colour the plate can show, channel-wise; black/white when Pillow or the file is missing."""
    if name in _PLATES:
        return _PLATES[name]
    res = ((0, 0, 0), (255, 255, 255))
    try:
        from PIL import Image
        ext = Image.open(os.path.join(SITE, 'cycle', 'media', name)).convert('RGB').getextrema()
        res = (tuple(e[0] for e in ext), tuple(e[1] for e in ext))
    except Exception:
        pass
    _PLATES[name] = res
    return res


def _plate_px(v, mode, kind, plate):
    lo, hi = _plate_extremes(plate)
    px = _hex(lo if kind == 'dark' else hi)
    if mode == 'dark':
        px = _hex([c * DARK_PLATE_FILTER for c in _rgb(px)])
        px = _blend(px, DARK_PLATE_OPACITY, v['bg'])
    else:
        px = _blend(px, 0.8, v['bg'])
    return px


def _color(spec, v, mode):
    if isinstance(spec, str):
        if spec.startswith('#'):
            return spec
        if spec == 'storeedge':
            return '#000000' if mode == 'light' else '#8C8C8C'
        if spec == 'notif_l':
            return v['notif']
        if spec == 'notif_d':
            return v['notifd']
        return v[spec]
    tag = spec[0]
    if tag == 'fixed':
        return spec[1]
    if tag == 'mix':
        return _blend(_color(spec[1], v, mode), spec[2], _color(spec[3], v, mode))
    if tag == 'plate':  # page colour at alpha over the plate pixel
        return _blend(v[spec[1]], spec[2], _plate_px(v, mode, spec[3], spec[4]))
    if tag == 'bandplate':
        rgb, a = BAND_SCRIM
        px = _hex(_plate_extremes('plate-glance.jpg')[0 if spec[1] == 'dark' else 1])
        return _blend(_hex(rgb), a, px)
    raise KeyError(spec)


def audit(html):
    """Every PAIRS entry in light and dark, read from the <style> of a generated page.
    -> (rows, ok); a row is (mode, label, fg, bg, ratio) for each text pair (>= 4.5:1); the 3:1 pairs (ring arcs, focus ring, marks,
    large text) are checked in ok but not listed."""
    style = re.search(r'<style>(.*?)</style>', html, re.S).group(1)
    first = re.search(r':root\{(.*?)\}\s*:root\{(.*?)\}', style, re.S)
    fixed, light = _vars(first.group(1)), _vars(first.group(2))
    light = dict(fixed, **light)
    dark = dict(light, **_vars(re.search(r'prefers-color-scheme:dark\)\{:root\{(.*?)\}\}', style, re.S).group(1)))
    rows, ok = [], True
    for mode, v in (('light', light), ('dark', dark)):
        for label, fg, bg, mn in PAIRS:
            f, b = _color(fg, v, mode), _color(bg, v, mode)
            r = _ratio(f, b)
            if mn == MIN:  # gen_legal_apps prints every row against 4.5:1, so the 3:1 graphics checks stay inside ok
                rows.append((mode, label, f, b, r))
            ok &= r >= mn
    return rows, ok


# ---------------------------------------------------------------- pieces
APPLE = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12.152 6.896c-.948 0-2.415-1.078-3.96-1.04-2.04.027-3.91 1.183-4.961 3.014-2.117 3.675-.546 9.103 1.519 12.09 '
         '1.013 1.454 2.208 3.09 3.792 3.039 1.52-.065 2.09-.987 3.935-.987 1.831 0 2.35.987 3.96.948 1.637-.026 2.676-1.48 3.676-2.948 1.156-1.688 1.636-3.325 '
         '1.662-3.415-.039-.013-3.182-1.221-3.22-4.857-.026-3.04 2.48-4.494 2.597-4.559-1.429-2.09-3.623-2.324-4.39-2.376-2-.156-3.675 1.09-4.61 1.09zM15.53 '
         '3.83c.843-1.012 1.4-2.427 1.245-3.83-1.207.052-2.662.805-3.532 1.818-.78.896-1.454 2.338-1.273 3.714 1.338.104 2.715-.688 3.559-1.701"/></svg>')
CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.2 4.2L19 7"/></svg>'
C = 251.33


def ring(size, frac, state, num=None, unit=None):
    """A countdown ring. The stroke never renders thinner than 6.5px, so it holds 3:1 without its label."""
    sw = max(9, round(6.5 * 100 / size, 1))
    off = round(C * (1 - frac), 2)
    txt = ''
    if num is not None:
        txt = f'<text x="50" y="54" font-size="26">{num}</text><text class="u" x="50" y="68">{unit}</text>'
    return (f'<svg class="cy-ring" viewBox="0 0 100 100" width="{size}" height="{size}" aria-hidden="true">'
            f'<circle class="t" cx="50" cy="50" r="40" stroke-width="{sw}"/>'
            f'<circle class="a c-{state}" cx="50" cy="50" r="40" stroke-width="{sw}" transform="rotate(-90 50 50)" '
            f'stroke-dasharray="{C}" stroke-dashoffset="{off}"/>{txt}</svg>')


def store_button(extra=''):
    return (f'<a class="cy-store" href="{STORE}" rel="noopener" aria-label="Download Cycle Timers on the App Store"{extra}>{APPLE}'
            '<span><small>Download on the</small><b>App Store</b></span></a>')


def phone(src, alt, style='', lazy=True, dark=None, cls='', w=680, h=1480):
    load = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high" decoding="async"'
    pic = f'<source media="(prefers-color-scheme: dark)" srcset="media/{dark}">' if dark else ''
    img = f'<img src="media/{src}" width="{w}" height="{h}" alt="{alt}"{load}>'
    st = f' style="{style}"' if style else ''
    inner = f'<picture>{pic}{img}</picture>' if dark else img
    return f'<figure class="cy-phone {cls}"{st}>{inner}</figure>'


def head(title, desc, canonical, key):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="{LIGHT['bg']}" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="{DARK['bg']}" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="https://seizeapps.com/cycle/media/icon-512.png">
<link rel="icon" type="image/png" sizes="180x180" href="media/icon-180.png">
<link rel="apple-touch-icon" href="media/icon-180.png">
<style>{css()}</style>
</head>
'''


def header(key):
    cur = lambda k: ' aria-current="page"' if k == key else ''
    return f'''<a class="cy-skip" href="#main">Skip to content</a>
<header class="cy-head"><div class="cy-wrap">
<a class="cy-brand" href="./"><img src="media/icon-512.png" width="30" height="30" alt="">Cycle Timers</a>
<nav class="cy-nav" aria-label="Cycle Timers"><a href="./#rings">Rings</a><a href="./#widgets">Widgets</a><a href="./#templates">Templates</a><a href="./#pro">Free &amp; Pro</a><a href="support.html"{cur('support')}>Support</a></nav>
<a class="cy-mini" href="{STORE}" rel="noopener">App Store</a>
</div></header>
'''


def footer(key='index'):
    nxt = '<div><h2>Next</h2><span class="cy-pillnext">Coming in the next update</span><p>Starter packs, a history with notes, and fixed-day schedules such as every Monday.</p></div>\n' if key == 'index' else ''
    return f'''<footer class="cy-foot"><div class="cy-wrap">
<div class="cy-foot-grid{' cy-foot3' if key != 'index' else ''}">
<div><p class="brand"><img src="media/icon-512.png" width="34" height="34" alt="" loading="lazy">Cycle Timers</p>
<p>Made by Izotz Cristobal Mota, in the Basque Country.</p><p>For iPhone and iPad, iOS 17.0 or later.</p></div>
<nav aria-label="Cycle Timers pages"><h2>Pages</h2><ul><li><a href="./">Home</a></li><li><a href="privacy.html">Privacy Policy</a></li><li><a href="terms.html">Terms of Use</a></li><li><a href="support.html">Support</a></li></ul></nav>
<div><h2>Get in touch</h2><ul><li><a href="mailto:{MAIL}">Contact</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li><a href="{STORE}" rel="noopener">Cycle Timers on the App Store</a></li></ul></div>
{nxt}</div>
<div class="cy-foot-end"><p>&copy; 2026 Izotz Cristobal Mota</p><p>App Store is a service mark of Apple Inc. iPhone and iPad are trademarks of Apple Inc.</p></div>
</div></footer>
'''


# ---------------------------------------------------------------- home
# The interactive widget: (key, name, state, remaining fraction, centre number, unit, status, days until next, label)
DEMO = [
    ('vac', 'Vacuum', 'fresh', .71, '5', 'days', 'On track', 7),
    ('sheets', 'Change sheets', 'soon', .36, '5', 'days', 'Coming up', 14),
    ('mop', 'Mop floors', 'over', 1, '1', 'day over', 'Overdue', 7),
    ('bath', 'Clean bathroom', 'fresh', .86, '12', 'days', 'On track', 14),
    ('cat', 'Cat litter', 'soon', .25, '24', 'hours', 'Coming up', 4),
    ('plants', 'Water plants', 'due', .125, '12', 'hours', 'Due soon', 4),
]


def demo_widget():
    cells = []
    for k, name, st, fr, num, unit, status, nxt in DEMO:
        alabel = f'Mark {name} done. {num} {unit}, {status.lower()}.'
        cells.append(
            f'<button type="button" data-k="{k}" data-next="{nxt}" data-name="{name}" aria-label="{alabel}">'
            f'{ring(84, fr, st, num, unit)}<span class="n">{name}</span><span class="s">{status}</span></button>')
    return ('<div class="cy-widget" id="cy-widget" role="group" aria-label="Large Home Screen widget, illustrated">'
            '<header><b><svg width="16" height="16" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="38" fill="none" stroke="#8d908e" stroke-width="12"/></svg>Cycle</b>'
            '<span class="cy-count" id="cy-count" aria-live="polite"><b>5</b> on track &middot; <b>1</b> overdue</span></header>'
            f'<div class="g">{"".join(cells)}</div><footer>A LITTLE CARE. A FRESH START.</footer></div>')


def tpl_cards():
    data = [('Cleaning', [('Vacuum', 'every week'), ('Change sheets', 'every 2 weeks'), ('Mop floors', 'every week'), ('Dust', 'every 2 weeks')]),
            ('Bathroom', [('Clean bathroom', 'every 2 weeks'), ('Replace toothbrush', 'every 3 months'), ('Wash towels', 'every week')]),
            ('Home', [('Water plants', 'every 4 days'), ('Take out trash', 'every 3 days'), ('Smoke alarm test', 'every month'), ('Air filter', 'every 3 months')]),
            ('Pets', [('Cat litter', 'every 4 days'), ('Flea treatment', 'every month'), ('Water bowl', 'every 2 days')]),
            ('Kitchen', [('Leftovers', 'every 3 days'), ('Fresh fish', 'every 2 days'), ('Opened milk', 'every 5 days'), ('Bread', 'every 4 days'),
                         ('Fridge clean-out', 'every week'), ('Water filter', 'every 2 months')])]
    out = []
    for i, (h, items) in enumerate(data):
        lis = ''.join(f'<li>{n}<span>{e}</span></li>' for n, e in items)
        out.append(f'<section aria-labelledby="t-{h.lower()}"{" class=lead" if i == 0 else ""}><h3 id="t-{h.lower()}">{h}</h3><ul>{lis}</ul></section>')
    return ''.join(out)


def wrapped_card():
    rings = ''.join(
        f'<circle class="t" cx="50" cy="50" r="{r}" pathLength="100"/><circle cx="50" cy="50" r="{r}" pathLength="100" stroke="{c}" style="stroke-dasharray:{d} 100"/>'
        for r, c, d in ((44, FIXED['wfreshd'], 86), (34, FIXED['wsoond'], 64), (24, FIXED['wdued'], 41), (14, FIXED['ink_w'], 22)))
    return f'<figure class="cy-wcard" aria-hidden="true"><svg viewBox="0 0 100 100">{rings}</svg><figcaption><small>Cycle Wrapped</small>Your year in Cycle.</figcaption></figure>'


def home():
    ck = lambda t: f'<li>{CHECK}<span>{t}</span></li>'
    lock = ('<svg viewBox="0 0 48 48"><rect x="10" y="21" width="28" height="19" rx="5"/><path d="M16 21v-5a8 8 0 0116 0v5"/><path d="M24 29v4"/></svg>')
    states = ''.join(
        f'<li>{ring(44, fr, st)}<div><strong>{t}</strong><span>{s}</span></div></li>'
        for st, fr, t, s in (('fresh', .9, 'On track', 'Plenty of time left'), ('soon', .45, 'Coming up', 'Yellow as it nears'),
                             ('due', .2, 'Due soon', 'Orange, nearly there'), ('over', 1, 'Overdue', 'Red until you mark it done')))
    free_rings = ''.join(ring(64, f, s) for f, s in ((.9, 'fresh'), (.7, 'fresh'), (.4, 'soon'), (.18, 'due')))
    picks = ''.join(f'<span class="cy-pick">{ring(56, f, s)}<b aria-hidden="true">{n}</b></span>' for f, s, n in ((.9, 'fresh', 2), (.35, 'soon', 1), (.12, 'due', 3)))
    notif = ('<div class="cy-notif" role="img" aria-label="Notification from Cycle for Cat litter: This one\'s due, hit Mark Done once it\'s handled. Button: Mark Done.">'
             '<img src="media/icon-180.png" width="42" height="42" alt="" loading="lazy"><strong>Cat litter <span>now</span></strong>'
             '<p>This one\'s due &mdash; hit Mark Done once it\'s handled.</p><div class="cy-notif-act"><span>Mark Done</span></div></div>')
    return f'''<main id="main">

<section class="cy-hero" aria-labelledby="top">
<div class="cy-wrap">
<img class="cy-mark" src="media/icon-1024.png" width="88" height="88" alt="Cycle Timers app icon">
<p class="cy-kicker">Cleaning and household chores</p>
<h1 id="top"><span class="cy-vh">Cycle Timers: </span>Every chore,<br>on a ring.</h1>
<p class="cy-lede"><em>One ring each:</em> when you last did it, and when it is due again.</p>
<div class="cy-cta">{store_button()}<p>iPhone and iPad. Free to start.</p></div>
</div>
<div class="cy-stage" role="group" aria-label="Cycle Timers on iPhone">
{phone('02-templates.jpg', 'The Templates sheet in Cycle: A good place to start, with Leftovers, Fresh fish, Opened milk, Bread and more.', cls='cy-s1', lazy=False)}
{phone('25-iphone-final.jpg', 'Cycle on iPhone in light mode: Your home, in rhythm, with rings for Bathroom, Pet food, Fresh fish and Leftovers.', cls='cy-s2', lazy=False, dark='09-dashboard-dark.jpg')}
{phone('09-dashboard-dark.jpg', 'Cycle on iPhone in dark mode: Fresh fish overdue in red, Cat litter, Bathroom and Pet food counting down.', cls='cy-s3', lazy=False, dark='25-iphone-final.jpg')}
</div>
</section>

<section class="cy-spec" aria-label="At a glance"><div class="cy-wrap"><dl>
<div><dt>Devices</dt><dd>iPhone and iPad</dd></div><div><dt>Requires</dt><dd>iOS 17.0 or later</dd></div>
<div><dt>Languages</dt><dd>11</dd></div><div><dt>Privacy</dt><dd>No account, no tracking</dd></div>
</dl></div></section>

<section class="cy-statement" aria-label="What Cycle does"><div class="cy-wrap"><p>Set a timer for anything that repeats, <em>and forget about forgetting.</em></p></div></section>

<section class="cy-section" id="rings" aria-labelledby="h-rings" style="padding-top:clamp(40px,6vw,80px)">
<div class="cy-wrap cy-split">
<div class="cy-copy">
<p class="cy-eyebrow">At a glance</p>
<h2 class="cy-h2" id="h-rings">One look tells you what is due.</h2>
<p class="cy-lede">Cycle turns recurring household chores into countdown rings: the sheets every 2 weeks, the cat litter every 4 days, food that expires in 3 days. Each ring slowly drains from green to yellow to orange, and turns red when it is overdue.</p>
<ul class="cy-states" aria-label="Ring colours">{states}</ul>
</div>
<div class="cy-visual cy-crop-m"><div class="cy-glow"></div>{phone('06-dashboard-populated.jpg', 'Cycle dashboard with a header card, filters for All, Needs care and On track, and ring cards for Fresh fish, Cat litter, Bathroom and Pet food.', 'width:min(330px,70vw);--w:min(330px,70vw)', dark='09-dashboard-dark.jpg')}</div>
</div>
</section>

<section class="cy-section cy-band" id="widgets" aria-labelledby="h-widget">
<div class="cy-wrap cy-split cy-rev">
<div class="cy-copy">
<p class="cy-eyebrow">Widget-first</p>
<h2 class="cy-h2" id="h-widget">One tap, done.</h2>
<p class="cy-lede">Tap a ring on the Home Screen widget to mark it done and start its next cycle, <strong>without opening the app</strong>. Choose exactly which timers each widget shows.</p>
<ul class="cy-matrix" aria-label="Widgets by plan">
<li><span>Small</span><span class="cy-tagp">Free</span></li>
<li><span>Medium</span><span class="cy-tagp">Cycle Pro</span></li>
<li><span>Large</span><span class="cy-tagp">Cycle Pro</span></li>
<li><span>Extra Large <small>on iPad, eight rings</small></span><span class="cy-tagp">Cycle Pro</span></li>
<li><span>Lock Screen <small>your most urgent timers</small></span><span class="cy-tagp">Cycle Pro</span></li>
</ul>
</div>
<div class="cy-visual cy-desktop-only"><figure class="cy-realwidget"><img src="media/widget-large.webp" width="661" height="687" alt="The Large Cycle widget on the Home Screen: six rings for Cat litter, Bathroom, Pet food, Fresh fish, Leftovers and Water plants, each with its time left." loading="lazy" decoding="async"></figure></div>
</div>
<div class="cy-wrap cy-split">
<div class="cy-copy">
<p class="cy-eyebrow">Try it</p>
<h3 class="cy-h2" style="font-size:clamp(1.9rem,3.6vw,2.9rem)">Tap a ring.</h3>
<p class="cy-lede">A drawing of the Large widget that works like the real one: tap a ring and it is full again. Pressed by mistake? Undo takes one tap.</p>
</div>
<div class="cy-visual"><div class="cy-demo">{demo_widget()}
<div class="cy-demo-bar" id="cy-bar" aria-live="polite"><span>Mop floors is a day over. Tap it.</span></div></div></div>
</div>
</section>

<section class="cy-section" id="templates" aria-labelledby="h-tpl">
<div class="cy-wrap">
<div class="cy-split cy-rev">
<div class="cy-copy">
<p class="cy-eyebrow">Effortless</p>
<h2 class="cy-h2" id="h-tpl">Cleaning, and everything else that repeats.</h2>
<p class="cy-lede">Start from household templates (Cleaning, Bathroom, Home, Pets and Kitchen): vacuum, change the sheets, clean the bathroom, water the plants. Or make your own in seconds: <strong>name, icon, interval, done.</strong></p>
<p class="cy-lede">Did it yesterday? Backdate the timer to when you actually did it.</p>
</div>
<div class="cy-visual cy-hide-m"><div class="cy-glow"></div>
<div class="cy-duo">{phone('02-templates.jpg', 'The Templates sheet: A good place to start. Pick the things you care for.')}{phone('07-edit.jpg', 'The Edit Timer sheet: a large red ring for Fresh fish, repeat every 2 days, and a Last done date.')}</div></div>
</div>
<div class="cy-templates" tabindex="0" role="region" aria-label="Starter templates by category">{tpl_cards()}</div>
<p class="cy-swipe" aria-hidden="true">Swipe for more &rarr;</p>
<p class="cy-note">Twenty starting points. Each one is yours to change.</p>
</div>
</section>

<section class="cy-section cy-calm" aria-labelledby="h-calm">
<div class="cy-wrap">
<div class="cy-split">
<div class="cy-copy">
<p class="cy-eyebrow">Reassuring, not nagging</p>
<h2 class="cy-h2" id="h-calm">Calm until it matters.</h2>
<p class="cy-lede">Green for most of a cycle, warm colours only when it matters. No streaks, no guilt. One notification when something comes due, with a <strong>Mark Done</strong> button right on it.</p>
<ul class="cy-checks">{ck('An optional app badge shows the overdue count.')}{ck('Light and dark, following your device.')}</ul>
</div>
<div class="cy-visual cy-hide-m"><div class="cy-glow"></div>{phone('05-settings.jpg', 'Cycle Settings: A little more personal, with Overdue Notifications, the Badge Shows Overdue Count toggle, and Small, Medium and Large Widget rows.', '--w:min(310px,66vw)')}</div>
</div>
<div class="cy-bento" tabindex="0" role="region" aria-label="More about notifications, Siri and widgets">
<article class="cy-card"><h3>One notification, one button.</h3><p>When a timer comes due, Mark Done is right on the notification.</p><div class="cy-mock">{notif}</div></article>
<article class="cy-card"><h3>Ask Siri.</h3><p>Siri and Shortcuts can mark a timer done without opening anything.</p>
<div class="cy-mock"><span class="cy-pill"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8"/><path d="M12 8v4l2.5 2"/></svg>&ldquo;Mark cat litter done in Cycle&rdquo;</span></div></article>
<article class="cy-card"><h3>Widgets you choose.</h3><p>Pick exactly which timers each widget shows, and in which order.</p><div class="cy-mock cy-picks" aria-hidden="true">{picks}<span class="cy-pickempty"></span></div></article>
</div>
<p class="cy-swipe" aria-hidden="true">Swipe for more &rarr;</p>
</div>
</section>

<section class="cy-section" aria-labelledby="h-pad">
<div class="cy-wrap cy-split cy-rev">
<div class="cy-copy">
<p class="cy-eyebrow">iPhone and iPad</p>
<h2 class="cy-h2" id="h-pad">Room for every room.</h2>
<p class="cy-lede">Cycle works on iPhone and iPad. On iPad the dashboard fills the wider screen with more columns, and the Extra Large widget (Cycle Pro) fits eight rings on the Home Screen.</p>
</div>
<div class="cy-visual"><div class="cy-glow"></div><figure class="cy-pad" style="--w:min(520px,88vw)"><img src="media/23-ipad-final.jpg" width="1050" height="1400" loading="lazy" decoding="async" alt="Cycle on iPad in light mode: the dashboard in columns, with rings for Fresh fish, Cat litter, Bathroom, Pet food, Water plants and Leftovers."></figure></div>
</div>
</section>

<section class="cy-section cy-price" id="pro" aria-labelledby="h-pro">
<div class="cy-wrap">
<div class="cy-price-head"><p class="cy-eyebrow">Free to start</p>
<h2 class="cy-h2" id="h-pro">Free to start. Pro, once.</h2>
<p class="cy-lede">Cycle Pro is an optional one-time in-app purchase. No subscription, no recurring charges.</p></div>
<div class="cy-plans">
<article class="cy-plan"><span class="cy-tag free">Free</span><h3>Everything you need to begin.</h3><p class="sub">No account needed.</p>
<ul class="cy-checks">{ck('Up to 4 timers')}{ck('One Small Home Screen widget')}{ck('Templates, undo, backdating, notifications, Siri and Shortcuts')}</ul>
<div class="cy-fourrings" aria-hidden="true">{free_rings}</div></article>
<article class="cy-plan pro"><span class="cy-tag">Cycle Pro</span><h3>Once, and it is yours.</h3><p class="sub">A one-time purchase. The price is shown in the App Store.</p>
<ul class="cy-checks">{ck('Unlimited timers')}{ck('Medium and Large widgets, plus Extra Large on iPad')}{ck('Lock Screen widgets')}{ck('Cycle Wrapped, your year in Cycle')}{ck('Message the developer straight from Settings')}</ul></article>
</div>
<div class="cy-wrapped"><div><p class="cy-eyebrow">Cycle Pro</p><h3>Your year in Cycle.</h3>
<p>Cycle Wrapped is a year-end recap of everything you kept on top of, with a card to share. It opens in early December, and any time from Settings.</p></div>{wrapped_card()}</div>
</div>
</section>

<section class="cy-section" aria-labelledby="h-priv">
<div class="cy-wrap cy-private">
<div class="cy-lock" aria-hidden="true">{lock}</div>
<div><h2 class="cy-h2" id="h-priv">Private by design.</h2>
<p class="cy-lede" style="margin:0">No account, no tracking. Your timers stay on your device and are never sent to us. <a href="privacy.html">Read the privacy policy</a>.</p></div>
</div>
</section>

<section class="cy-section cy-close" aria-labelledby="h-close">
<div class="cy-wrap">
<h2 class="cy-h2" id="h-close">Make room for everyday life.</h2>
<p class="cy-lede">A little care. A fresh start.</p>
<div class="cy-cta">{store_button()}<p>iPhone and iPad. Free to start.</p></div>
</div>
</section>

</main>
'''


DEMO_JS = r'''<script>
(function(){
var w=document.getElementById('cy-widget');if(!w)return;
var bar=document.getElementById('cy-bar'),count=document.getElementById('cy-count'),C=251.33,last=null;
var HINT='<span>Mop floors is a day over. Tap it.</span>';
function snap(b){var a=b.querySelector('.a'),t=b.querySelectorAll('text');return{b:b,cls:a.getAttribute('class'),off:a.getAttribute('stroke-dashoffset'),n:t[0].textContent,u:t[1].textContent,s:b.querySelector('.s').textContent,al:b.getAttribute('aria-label')};}
function put(o){var a=o.b.querySelector('.a'),t=o.b.querySelectorAll('text');a.setAttribute('class',o.cls);a.setAttribute('stroke-dashoffset',o.off);t[0].textContent=o.n;t[1].textContent=o.u;o.b.querySelector('.s').textContent=o.s;o.b.setAttribute('aria-label',o.al);}
var orig=[].map.call(w.querySelectorAll('button'),snap);
function tally(){var over=w.querySelectorAll('.a.c-over').length,all=w.querySelectorAll('button').length;count.innerHTML='<b>'+(all-over)+'</b> on track &middot; <b>'+over+'</b> overdue';}
function show(h){bar.innerHTML=h;}
[].forEach.call(w.querySelectorAll('button'),function(b){
  b.addEventListener('click',function(){
    last=snap(b);var a=b.querySelector('.a'),t=b.querySelectorAll('text'),d=b.dataset.next;
    a.setAttribute('class','a c-fresh');a.setAttribute('stroke-dashoffset','0');
    t[0].textContent=d;t[1].textContent='days';b.querySelector('.s').textContent='On track';
    b.setAttribute('aria-label','Done. '+b.dataset.name+' next in '+d+' days.');
    tally();
    show('<span class="cy-toast"><i></i>Done. Next in '+d+' days.</span><button type="button" id="cy-undo">Undo</button><button type="button" id="cy-reset">Start over</button>');
    document.getElementById('cy-undo').addEventListener('click',function(){put(last);tally();show(HINT);b.focus();});
    document.getElementById('cy-reset').addEventListener('click',function(){orig.forEach(put);tally();show(HINT);});
  });
});
})();
</script>
'''

SPY_JS = r'''<script>
(function(){
var links=[].slice.call(document.querySelectorAll('.cy-rail a[href^="#"]'));if(!links.length)return;
var heads=links.map(function(a){return document.getElementById(a.getAttribute('href').slice(1));}).filter(function(h,i,s){return h&&s.indexOf(h)===i;});
var tick=false;
function spy(){tick=false;var cur=heads[0];heads.forEach(function(h){if(h.getBoundingClientRect().top<=140)cur=h;});
  if(window.scrollY>0&&window.innerHeight+window.scrollY>=document.body.scrollHeight-4)cur=heads[heads.length-1];
  links.forEach(function(a){var on=a.getAttribute('href')==='#'+cur.id;a.classList.toggle('on',on);if(on)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current');});}
window.addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(spy);}},{passive:true});
window.addEventListener('resize',spy);spy();
})();
</script>
'''


# ---------------------------------------------------------------- legal pages
def _slug(text, seen):
    s = re.sub(r'<[^>]+>', '', text).lower()
    s = re.sub(r'^\d+\.\s*', '', s)
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-') or 'section'
    base, n = s, 2
    while s in seen:
        s = f'{base}-{n}'
        n += 1
    seen.add(s)
    return s


def legal(key, body):
    take = lambda pat, b: (lambda m: (m.group(1).strip(), b.replace(m.group(0), '', 1)) if m else ('', b))(re.search(pat, b, re.S))
    h1, body = take(r'<h1>(.*?)</h1>', body)
    upd, body = take(r'<p class="updated">(.*?)</p>', body)
    m = re.search(r'<ul class="summary"(?: data-label="([^"]*)")?>(.*?)</ul>', body, re.S)
    summ = None
    if m:
        lis = re.findall(r'<li>(.*?)</li>', m.group(2), re.S)
        summ = (m.group(1) or 'In short', lis)
        body = body.replace(m.group(0), '', 1)
    seen, toc = set(), []

    def h2(mm):
        i = _slug(mm.group(1), seen)
        toc.append((2, i, re.sub(r'<[^>]+>', '', mm.group(1)).strip()))
        return f'<h2 id="{i}">{mm.group(1)}</h2>'

    def h3(mm):
        i = _slug(mm.group(1), seen)
        toc.append((3, i, re.sub(r'<[^>]+>', '', mm.group(1)).strip()))
        return f'<h3 id="{i}">{mm.group(1)}</h3>'

    body = re.sub(r'<h2>(.*?)</h2>', h2, body)
    body = re.sub(r'<h3>(.*?)</h3>', h3, body)
    items = ([(2, 'in-short', summ[0])] if summ else []) + toc
    ol = ''
    for n, (lvl, i, t) in enumerate(items):
        nxt = items[n + 1][0] if n + 1 < len(items) else 2
        if lvl == 2:
            ol += f'<li><a href="#{i}">{t}</a>' + ('<ol>' if nxt == 3 else '</li>')
        else:
            ol += f'<li><a href="#{i}">{t}</a></li>' + ('</ol></li>' if nxt == 2 else '')
    ol = f'<ol>{ol}</ol>'
    arrow = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M10 3L5 8l5 5"/></svg>'
    short = ''
    if summ:
        short = (f'<aside class="cy-summary" aria-labelledby="in-short"><h2 id="in-short">{summ[0]}</h2><ul>'
                 + ''.join(f'<li>{CHECK}<span>{li.strip()}</span></li>' for li in summ[1]) + '</ul></aside>\n')
    stamp = f'<p class="cy-updated">{upd}</p>'
    pages = (('privacy', 'Privacy Policy', 'privacy.html'), ('terms', 'Terms of Use', 'terms.html'), ('support', 'Support', 'support.html'))
    switch = '<ul class="cy-switch" aria-label="Cycle Timers pages">' + ''.join(
        f'<li><a href="{h}"{" aria-current=page" if k == key else ""}>{l}</a></li>' for k, l, h in pages) + '</ul>'
    return f'''<main id="main">
<section class="cy-lhero"><div class="cy-wrap cy-narrow">
<h1>{h1}</h1>
{stamp}
{switch}
</div></section>
<div class="cy-wrap cy-narrow cy-legal">
<div class="cy-rail"><a class="cy-back" href="./">{arrow}Back to Cycle Timers</a>
<nav class="cy-toc" aria-label="On this page"><h2>On this page</h2>{ol}</nav>
<details class="cy-tocm"><summary>On this page</summary>{ol}</details></div>
<article class="cy-prose">
{short}{body.strip()}
</article>
</div>
</main>
'''


def page(app, lang, key, title, desc, body, host, alts):
    canonical = f'{host}{app["slug"]}/' if key == 'index' else f'{host}{app["slug"]}/{key}.html'
    main = home() if key == 'index' else legal(key, body)
    script = DEMO_JS if key == 'index' else SPY_JS
    return head(title, desc, canonical, key) + '<body>\n' + header(key) + main + footer(key) + script + '</body>\n</html>\n'
