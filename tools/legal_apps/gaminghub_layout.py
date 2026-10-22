"""GamingHub's own site for tools/gen_legal_apps.py (slug 'gaminghub'): the home page and the three legal pages in one
design system that shares no template, class name or stylesheet with any other app (everything is prefixed `gx-`).

Identity: the app's own UI, warm near-black with cream type and one neon per game (Theme/GameBrand.swift), set on the
store plates, with the real screens in CSS device frames. The legal pages keep the same dark art header and the same
type. The app has no light theme, so the site's light mode is warm paper (#F5F2EC) with the dark stages and game cards
kept dark on it, the way the app's cards sit on its surfaces.

Page order on the home page: hero + facts strip, room code, resume strip, Impostor, the five games, Unison (a short
strip), Vault (a tall stage), languages, free and paid, privacy.

Colours. Every colour used for text lives in the palette tables below and is emitted into the stylesheet as a custom
property (`:root` for the paper surfaces in both modes, `.k-<name>` classes for the dark stages and game cards). Text
that sits on a plate is never measured against the plate: audit() measures it against the stage colour with the scrim
(`--scrim-pct`) laid over a pure white pixel, the worst case whatever the art shows through. audit() reads every
colour back from the generated page, in both modes, and gen_legal_apps.py refuses to write a page if a pair is under
4.5:1. All text colours are opaque on purpose, so what is measured is what is drawn.

Images are WebP in gaminghub/media/ with intrinsic width/height; nothing leaves the page except mailto:, the
vendors and regulators the legal text names, and Apple's own legal and refund pages. No fonts, scripts or styles are
loaded from anywhere; the one inline script only marks the current section in the contents list.
"""
import re

MIN = 4.5
SCRIM = 90  # percent of the stage colour laid over the art under any text

# Paper surfaces (home sections and legal pages), per mode. Everything is a text/background pair in audit().
LIGHT = dict(canvas='#F5F2EC', canvas2='#EDE7DA', ink='#1A1814', muted='#5B574E', card='#FFFDF8', chip='#E9E4D9',
             line='#D9D3C6', link='#0A5BC4', kick='#8A4B0B', btn='#1A1814', btn_ink='#F5F2EC')
DARK = dict(canvas='#0E0D0C', canvas2='#121110', ink='#F5F2EC', muted='#B0AA9E', card='#181614', chip='#221F1B',
            line='#2E2A25', link='#8FDCFF', kick='#F2B35E', btn='#F5F2EC', btn_ink='#0A0908')
# Fixed on every dark surface, both modes.
FIXED = dict(stage='#0A0908', cream='#F5F2EC', cream2='#D6D2CA', cream3='#B9B5AD', peach='#FFD9A8', sfocus='#8FDCFF')

# a = accent, b = second colour, deep/mid = the card gradient. Games from Theme/GameBrand.swift; hub, lang, top,
# hero and priv are the site's own stages (the store plates are bluer than the app, so they get a blue hub).
KEYS = {
    'hub': dict(a='#5DD4FF', b='#BFEAFF', deep='#06101A', mid='#0A1E33'),
    'uni': dict(a='#5EE6A0', b='#9AD8FF', deep='#07130D', mid='#10241A'),
    'imp': dict(a='#FF4D6D', b='#F2C46D', deep='#14080C', mid='#2A1219'),
    'vault': dict(a='#F5B742', b='#7FD1C2', deep='#120E06', mid='#241D10'),
    'spot': dict(a='#3FD8E0', b='#FFC23D', deep='#061214', mid='#0F2328'),
    'fish': dict(a='#FF8A3D', b='#5FD0FF', deep='#140B05', mid='#2A180C'),
    'hero': dict(a='#7FD9FF', b='#FFD9A8', deep='#070A12', mid='#0A1020'),
    'priv': dict(a='#8FDCFF', b='#FFD9A8', deep='#06101A', mid='#0A1E33'),
}
GAME_ORDER = ['uni', 'imp', 'vault', 'spot', 'fish']

CSS = r'''
:root{__LIGHT__;__FIXED__;--scrim-pct:__SCRIM__%;--sh:0 1px 0 rgba(26,24,20,.05),0 34px 60px -30px rgba(70,45,10,.45),0 14px 26px -16px rgba(70,45,10,.26);--dots:rgba(26,24,20,.075);color-scheme:light dark;
--f-ui:ui-rounded,"SF Pro Rounded","Hiragino Maru Gothic ProN","Arial Rounded MT Bold",system-ui,"Segoe UI",sans-serif;
--f-text:system-ui,"Avenir Next","Segoe UI",sans-serif;
--f-serif:ui-serif,"New York","Iowan Old Style",Georgia,serif;
--f-mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;
--f-cond:"Avenir Next Condensed","DIN Condensed","Arial Narrow","Roboto Condensed",system-ui,sans-serif;
--pad:clamp(20px,4vw,56px);--wrap:1240px}
@media (prefers-color-scheme:dark){:root{__DARK__;--sh:0 24px 44px -28px rgba(0,0,0,.75);--dots:rgba(245,242,236,.05)}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{animation:none!important;transition:none!important}}
body{margin:0;background:var(--canvas);color:var(--ink);font:400 17px/1.6 var(--f-text);-webkit-font-smoothing:antialiased;overflow-x:hidden}
img{max-width:100%;height:auto;display:block}
a{color:var(--link);text-underline-offset:3px}
a:focus-visible,summary:focus-visible{outline:3px solid var(--link);outline-offset:3px;border-radius:8px}
.gx-dark a:focus-visible{outline-color:var(--sfocus)}
h1,h2,h3,p,ul,ol,dl,dd,figure{margin:0}
.gx-skip{position:absolute;left:12px;top:-64px;background:var(--cream);color:#1A1814;padding:12px 18px;border-radius:12px;font-weight:600;z-index:100;text-decoration:none}
.gx-skip:focus{top:12px;outline:3px solid #0A5BC4}
.gx-brand{display:inline-flex;align-items:center;gap:12px;text-decoration:none;color:var(--cream);font:800 20px/1 var(--f-ui);letter-spacing:-.01em;min-height:44px}
.gx-brand img{width:38px;height:38px;border-radius:10px;box-shadow:0 0 0 1px rgba(245,242,236,.22),0 6px 18px rgba(0,0,0,.45)}
.gx-kicker{font:600 12px/1.3 var(--f-mono);letter-spacing:.2em;text-transform:uppercase;color:var(--a,var(--kick));display:flex;align-items:center;gap:12px}
.gx-kicker i{font-style:normal;color:var(--cream3)}
.gx-kicker::after{content:"";height:1px;width:44px;background:currentColor;opacity:.5}
.gx-paper .gx-kicker{--a:var(--kick)}.gx-paper .gx-kicker i{color:var(--muted)}

/* phone frame */
.gx-phone{--w:260px;width:var(--w);flex:none;padding:7px;border-radius:calc(var(--w)*.165);background:linear-gradient(150deg,#4a453e 0%,#17150f 38%,#2d2924 100%);
box-shadow:0 0 0 1px rgba(245,242,236,.20),inset 0 0 0 1px rgba(0,0,0,.6),0 50px 90px -24px rgba(0,0,0,.85),0 0 110px -18px var(--glow,rgba(93,212,255,.5));position:relative}
.gx-phone::after{content:"";position:absolute;inset:7px;border-radius:calc(var(--w)*.165 - 7px);pointer-events:none;background:linear-gradient(115deg,rgba(255,255,255,.10) 0%,rgba(255,255,255,0) 28%)}
.gx-phone__s{aspect-ratio:600/1240;overflow:hidden;border-radius:calc(var(--w)*.165 - 7px);background:#0A0908}
.gx-phone__s img{width:100%;margin-top:-10.4%}

/* nav */
.gx-nav{position:relative;display:flex;align-items:center;justify-content:space-between;gap:12px;max-width:var(--wrap);margin:0 auto;padding:18px var(--pad)}
.gx-nav ul{list-style:none;padding:0;display:flex;gap:4px;align-items:center}
.gx-nav a:not(.gx-brand){display:inline-flex;align-items:center;min-height:44px;color:var(--cream2);text-decoration:none;font:500 15px/1 var(--f-text);padding:0 14px;border-radius:99px}
.gx-nav a:not(.gx-brand):hover{color:var(--cream);background:rgba(245,242,236,.12)}
.gx-nav a[aria-current=page]{color:var(--cream);box-shadow:inset 0 0 0 1px rgba(245,242,236,.4)}
@media (max-width:640px){.gx-nav .hide-s{display:none}.gx-nav a:not(.gx-brand){padding:0 11px;font-size:14.5px}}
@media (max-width:480px){.gx-nav{gap:6px}.gx-nav ul{gap:6px}.gx-nav a:not(.gx-brand){padding:0 8px;font-size:14px}.gx-nav--legal .gx-brand span{display:none}}
@media (max-width:370px){.gx-nav .gx-brand span{display:none}}

/* hero */
.gx-hero{position:relative;isolation:isolate;overflow:hidden;color:var(--cream);background:var(--deep);border-radius:0 0 clamp(28px,4vw,56px) clamp(28px,4vw,56px)}
.gx-hero__bg{position:absolute;inset:0;z-index:-2;background:url(media/plate-header.webp) 50% 18%/cover no-repeat}
.gx-hero::before{content:"";position:absolute;inset:0;z-index:-1;background:
 linear-gradient(180deg,color-mix(in srgb,var(--deep) 92%,transparent) 0,color-mix(in srgb,var(--deep) var(--scrim-pct),transparent) 96px,transparent 190px),
 radial-gradient(ellipse 62% 54% at 50% 38%,color-mix(in srgb,var(--deep) 94%,transparent) 0%,color-mix(in srgb,var(--deep) var(--scrim-pct),transparent) 62%,transparent 100%)}
.gx-hero__copy{max-width:860px;margin:clamp(22px,4.4vw,56px) auto 0;padding:0 var(--pad);text-align:center;display:flex;flex-direction:column;align-items:center}
.gx-hero .gx-kicker{justify-content:center}.gx-hero .gx-kicker::after{display:none}
.gx-hero h1{font:800 clamp(46px,8.4vw,112px)/.96 var(--f-ui);letter-spacing:-.035em;margin:20px 0 0;text-wrap:balance}
.gx-hero h1 em{font:italic 500 1em/1 var(--f-serif);letter-spacing:-.02em;color:var(--peach)}
.gx-lede{font:400 clamp(17px,1.7vw,21px)/1.55 var(--f-text);color:var(--cream2);max-width:44ch;margin-top:22px}
.gx-soon{display:inline-flex;align-items:center;gap:12px;margin-top:30px;padding:12px 22px 12px 18px;border-radius:99px;background:var(--deep);border:1px solid rgba(245,242,236,.4);font:600 15px/1.2 var(--f-text);color:var(--cream);max-width:100%}
.gx-soon b{flex:none;width:9px;height:9px;border-radius:50%;background:#7BD389;box-shadow:0 0 0 4px rgba(123,211,137,.22)}
.gx-soon .b{font-weight:400;color:var(--cream3)}
@media (max-width:480px){.gx-soon .b{display:none}.gx-soon{font-size:14px;padding:11px 18px 11px 16px}}
@media (prefers-reduced-motion:no-preference){.gx-soon b{animation:gx-pulse 2.6s ease-in-out infinite}}
@keyframes gx-pulse{50%{box-shadow:0 0 0 8px rgba(123,211,137,0)}}
.gx-fan{display:flex;justify-content:center;align-items:flex-start;height:clamp(300px,42vw,580px);overflow:hidden;margin-top:clamp(34px,4.6vw,64px);padding-top:10px}
.gx-fan .gx-phone{margin:0 clamp(-60px,-3.4vw,-22px);transform-origin:50% 100%}
.gx-fan .p1{--w:clamp(130px,16vw,236px);transform:translateY(clamp(30px,5vw,80px)) rotate(-11deg);--glow:rgba(94,230,160,.55);z-index:1}
.gx-fan .p2{--w:clamp(150px,19vw,272px);transform:translateY(clamp(12px,2.2vw,34px)) rotate(-5.5deg);--glow:rgba(255,77,109,.55);z-index:2}
.gx-fan .p3{--w:clamp(176px,23vw,330px);--glow:rgba(93,212,255,.6);z-index:4}
.gx-fan .p4{--w:clamp(150px,19vw,272px);transform:translateY(clamp(12px,2.2vw,34px)) rotate(5.5deg);--glow:rgba(245,183,66,.55);z-index:2}
.gx-fan .p5{--w:clamp(130px,16vw,236px);transform:translateY(clamp(30px,5vw,80px)) rotate(11deg);--glow:rgba(63,216,224,.55);z-index:1}
@media (max-width:720px){.gx-fan .p1,.gx-fan .p5{display:none}.gx-fan .gx-phone{margin:0 -26px}}
@media (max-width:430px){.gx-fan .p2,.gx-fan .p4{--w:126px}.gx-fan .p3{--w:168px}}
@media (prefers-reduced-motion:no-preference){.gx-fan .p3{animation:gx-float 8s ease-in-out infinite}}
@keyframes gx-float{50%{transform:translateY(-10px)}}
.gx-stripband{position:relative;z-index:5;background:var(--stage);border-top:1px solid rgba(245,242,236,.2)}
.gx-strip{max-width:var(--wrap);margin:0 auto;list-style:none;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr))}
.gx-strip li{padding:clamp(20px,2.6vw,34px) clamp(14px,2.4vw,32px);display:flex;flex-direction:column;gap:10px;align-items:flex-start}
.gx-strip li:first-child{padding-left:var(--pad)}.gx-strip li+li{border-left:1px solid rgba(245,242,236,.14)}
.gx-strip b{font:500 clamp(38px,4.6vw,64px)/1 var(--f-mono);letter-spacing:-.04em;color:var(--cream)}
.gx-strip span{font:600 12px/1.3 var(--f-mono);letter-spacing:.2em;text-transform:uppercase;color:var(--cream3)}
@media (max-width:720px){.gx-strip{grid-template-columns:repeat(2,minmax(0,1fr))}.gx-strip li:nth-child(3){border-left:0}.gx-strip li:nth-child(n+3){border-top:1px solid rgba(245,242,236,.14)}.gx-strip li{padding:20px 22px}}

/* stages */
.gx-stage{position:relative;isolation:isolate;overflow:hidden;color:var(--cream);background:var(--deep);border-radius:clamp(26px,3.4vw,48px);margin:clamp(12px,1.6vw,20px) clamp(10px,1.6vw,20px);box-shadow:0 0 0 1px rgba(245,242,236,.10)}
.gx-stage__bg{position:absolute;inset:0;z-index:-2;background:var(--plate) 50% 50%/cover no-repeat;filter:hue-rotate(var(--hue,0deg)) saturate(1.15) brightness(var(--br,1))}
.gx-stage::before{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(var(--dir,90deg),var(--deep) 0%,color-mix(in srgb,var(--deep) var(--scrim-pct),transparent) 50%,color-mix(in srgb,var(--deep) 16%,transparent) 82%,transparent 100%)}
.gx-stage--rev{--dir:270deg}
.gx-in{max-width:var(--wrap);margin:0 auto;padding:clamp(40px,6vw,92px) var(--pad) 0;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(24px,5vw,72px);align-items:stretch;min-height:clamp(560px,52vw,720px)}
.gx-stage--rev .gx-copy{order:2}
.gx-copy{max-width:520px;align-self:center;padding-bottom:clamp(40px,6vw,92px)}
.gx-copy h2{margin:18px 0 0;text-wrap:balance}
.gx-copy p.t{margin-top:20px;color:var(--cream2);font-size:18px;line-height:1.62;max-width:46ch}
.gx-copy p.t+p.t{margin-top:14px}
.gx-meta{display:flex;flex-wrap:wrap;gap:8px;margin-top:26px;list-style:none;padding:0}
.gx-meta li{font:500 13px/1 var(--f-mono);letter-spacing:.06em;padding:9px 13px;border-radius:99px;border:1px solid rgba(245,242,236,.28);background:var(--deep);color:var(--cream2)}
.gx-meta li.on{border-color:var(--a);color:var(--a)}
.gx-table{margin-top:26px;max-width:46ch;border-top:1px solid rgba(245,242,236,.2)}
.gx-table div{display:grid;grid-template-columns:132px minmax(0,1fr);gap:16px;padding:13px 0;border-bottom:1px solid rgba(245,242,236,.14)}
.gx-table dt{font:600 12px/1.6 var(--f-mono);letter-spacing:.14em;text-transform:uppercase;color:var(--a);padding-top:2px}
.gx-table dd{font-size:16px;line-height:1.5;color:var(--cream2)}
@media (max-width:480px){.gx-table div{grid-template-columns:1fr;gap:2px}}
.gx-vis{position:relative;display:flex;justify-content:center;align-items:flex-start;min-height:clamp(440px,46vw,640px);clip-path:inset(-400px -400px 0 -400px)}
.gx-vis::before{content:"";position:absolute;left:50%;top:46%;width:min(640px,110%);aspect-ratio:1;transform:translate(-50%,-50%);background:radial-gradient(closest-side,color-mix(in srgb,var(--a) 42%,transparent),transparent 72%);z-index:0}
.gx-vis .gx-phone{--glow:color-mix(in srgb,var(--a) 55%,transparent);z-index:1;margin-top:clamp(20px,3vw,48px)}
.gx-vis .back{--w:clamp(170px,19vw,252px);margin-right:calc(var(--w)*-.16);margin-top:clamp(60px,7vw,110px);transform:rotate(-6deg);z-index:1}
.gx-vis .front{--w:clamp(190px,22vw,300px);transform:rotate(3.5deg);z-index:2}
.gx-stage--rev .gx-vis .back{margin-right:0;margin-left:calc(var(--w)*-.16);order:2;transform:rotate(6deg)}
.gx-stage--rev .gx-vis .front{transform:rotate(-3.5deg)}
@media (prefers-reduced-motion:no-preference){.gx-vis .front{animation:gx-float2 9s ease-in-out infinite}}
@keyframes gx-float2{50%{translate:0 -9px}}
/* a short strip and a tall stage break the rhythm */
.gx-stage--strip .gx-in{min-height:0;padding-top:clamp(36px,4.4vw,56px)}
.gx-stage--strip .gx-copy{padding-bottom:clamp(36px,4.4vw,56px)}
.gx-stage--strip .gx-vis{min-height:0;height:clamp(300px,28vw,380px)}
.gx-stage--strip .gx-vis .back{margin-top:clamp(40px,4vw,60px)}
.gx-stage--strip .gx-vis .front{--w:clamp(200px,23vw,310px);margin-top:clamp(14px,1.6vw,24px)}
.gx-stage--tall .gx-in{min-height:clamp(680px,66vw,900px);padding-top:clamp(56px,7vw,112px)}
.gx-stage--tall .gx-copy{padding-bottom:clamp(56px,7vw,112px)}
.gx-stage--tall .gx-vis{min-height:clamp(600px,60vw,860px)}
.gx-stage--tall .gx-vis .back{--w:clamp(190px,22vw,300px)}
.gx-stage--tall .gx-vis .front{--w:clamp(230px,27vw,372px)}
@media (max-width:860px){
 .gx-in{grid-template-columns:1fr;min-height:0!important;gap:8px}.gx-copy{padding-bottom:12px!important}
 .gx-stage--rev .gx-copy{order:0}
 .gx-stage::before{background:linear-gradient(180deg,var(--deep) 0%,color-mix(in srgb,var(--deep) var(--scrim-pct),transparent) 62%,color-mix(in srgb,var(--deep) 20%,transparent) 100%)}
 .gx-vis,.gx-stage--tall .gx-vis,.gx-stage--strip .gx-vis{height:430px;min-height:0}
 .gx-vis .back,.gx-stage--tall .gx-vis .back,.gx-stage--strip .gx-vis .back{--w:150px;margin-top:70px}
 .gx-vis .front,.gx-stage--tall .gx-vis .front,.gx-stage--strip .gx-vis .front{--w:190px;margin-top:clamp(20px,3vw,48px)}
 .gx-stage--strip .gx-vis{height:340px}
}
.t-hub h2{font:800 clamp(36px,4.6vw,64px)/1.02 var(--f-ui);letter-spacing:-.03em}
.t-imp h2{font:italic 600 clamp(38px,5vw,70px)/1.02 var(--f-serif);letter-spacing:-.02em}
.t-uni h2{font:300 clamp(38px,5vw,70px)/1.02 var(--f-ui);letter-spacing:-.035em}
.t-vault h2{font:800 clamp(30px,3.8vw,54px)/1.06 var(--f-mono);letter-spacing:.01em;text-transform:uppercase}
.t-spot h2{font:800 clamp(42px,5.4vw,78px)/.98 var(--f-cond);letter-spacing:.005em;text-transform:uppercase}
.gx-ticket{margin-top:28px;display:inline-block;padding:16px 22px 18px;border-radius:18px;border:1px dashed rgba(245,242,236,.4);background:var(--deep)}
.gx-ticket small{display:block;font:600 11px/1 var(--f-mono);letter-spacing:.24em;color:var(--cream3);text-transform:uppercase}
.gx-ticket strong{display:block;margin-top:10px;font:500 clamp(30px,4.2vw,48px)/1 var(--f-mono);letter-spacing:.28em;margin-right:-.28em;color:var(--cream)}
.gx-word{margin-top:26px;display:inline-block;padding:16px 22px;border-radius:14px;border:1px solid color-mix(in srgb,var(--a) 60%,transparent);background:var(--deep)}
.gx-word small{display:block;font:600 11px/1.3 var(--f-mono);letter-spacing:.2em;color:var(--a);text-transform:uppercase}
.gx-word span{display:block;margin-top:8px;font:italic 500 28px/1.1 var(--f-serif);color:var(--cream)}
.gx-crews{display:flex;gap:10px;margin-top:26px;flex-wrap:wrap}
.gx-crews span{font:700 12px/1 var(--f-mono);letter-spacing:.14em;padding:11px 14px;border-radius:10px;background:var(--deep)}
.gx-crews .cu{color:var(--copper);border:1px solid var(--copper)}
.gx-crews .ja{color:var(--b);border:1px solid var(--b)}
.gx-langs{display:flex;flex-wrap:wrap;gap:8px;margin-top:26px;list-style:none;padding:0;max-width:500px}
.gx-langs li{font:500 15px/1 var(--f-text);padding:11px 15px;border-radius:99px;background:var(--deep);border:1px solid color-mix(in srgb,var(--a) 55%,transparent);color:var(--cream)}
.gx-cap{font:400 13px/1.45 var(--f-mono);letter-spacing:.04em;color:var(--cream3);margin-top:18px;max-width:46ch}

/* paper sections */
.gx-paper{position:relative;background:linear-gradient(180deg,var(--canvas),var(--canvas2) 50%,var(--canvas))}
.gx-paper::before{content:"";position:absolute;inset:0;pointer-events:none;background:radial-gradient(var(--dots) 1px,transparent 1.3px) 0 0/22px 22px;-webkit-mask-image:linear-gradient(180deg,#000,transparent 70%);mask-image:linear-gradient(180deg,#000,transparent 70%)}
.gx-sec{position:relative;max-width:var(--wrap);margin:0 auto;padding:clamp(56px,8vw,112px) var(--pad) clamp(40px,5vw,72px)}
.gx-sec h2{font:800 clamp(36px,5vw,68px)/1.02 var(--f-ui);letter-spacing:-.035em;margin-top:16px;text-wrap:balance}
.gx-sec h2 em{font:italic 500 1em/1 var(--f-serif);letter-spacing:-.02em}
.gx-sec p.sub{color:var(--muted);font-size:19px;max-width:52ch;margin-top:18px}
.gx-games{list-style:none;padding:0;margin:clamp(30px,4vw,52px) 0 0;display:grid;grid-template-columns:repeat(6,minmax(0,1fr));grid-auto-rows:1fr;gap:clamp(12px,1.6vw,20px)}
.gx-game{grid-column:span 2;position:relative;isolation:isolate;overflow:hidden;min-height:390px;border-radius:30px;padding:24px 26px 26px;color:var(--cream);display:flex;flex-direction:column;background:linear-gradient(155deg,var(--mid) 0%,var(--deep) 78%);box-shadow:0 0 0 1px color-mix(in srgb,var(--a) 30%,transparent),var(--sh)}
.gx-game:nth-child(n+4){grid-column:span 3}
.gx-game::before{content:"";position:absolute;z-index:-1;right:-14%;top:-30%;width:90%;aspect-ratio:1;background:radial-gradient(closest-side,color-mix(in srgb,var(--a) 30%,transparent),transparent 72%)}
.gx-game .art{position:absolute;z-index:-1;right:-2%;top:15%;width:54%;max-width:280px;height:auto;color:var(--a)}
.gx-game:nth-child(n+4) .art{width:42%;right:4%;top:13%}
.gx-game .top{display:flex;align-items:center;justify-content:space-between;gap:10px}
.gx-game .chip{font:600 11px/1 var(--f-mono);letter-spacing:.16em;text-transform:uppercase;padding:8px 12px;border-radius:99px;border:1px solid color-mix(in srgb,var(--a) 60%,transparent);color:var(--a);background:var(--deep)}
.gx-game .no{font:500 12px/1 var(--f-mono);letter-spacing:.14em;color:var(--cream3)}
.gx-game h3{margin-top:auto;padding-top:96px}
.gx-game .tag{font:italic 500 20px/1.25 var(--f-serif);color:var(--b);margin-top:6px}
.gx-game .blurb{color:var(--cream2);font-size:15.5px;line-height:1.55;margin-top:14px;max-width:40ch}
.gx-game .meta{font:500 12.5px/1 var(--f-mono);letter-spacing:.06em;color:var(--cream3);margin-top:18px}
.k-uni h3{font:300 46px/1 var(--f-ui);letter-spacing:-.03em}
.k-imp h3{font:italic 600 48px/1 var(--f-serif);letter-spacing:-.02em}
.k-vault h3{font:800 42px/1 var(--f-mono);letter-spacing:.02em;text-transform:uppercase}
.k-spot h3{font:800 54px/.95 var(--f-cond);letter-spacing:.01em;text-transform:uppercase}
.k-fish h3{font:800 46px/1 var(--f-ui);letter-spacing:-.03em}
@media (max-width:980px){.gx-game,.gx-game:nth-child(n+4){grid-column:span 3}.gx-game:last-child{grid-column:span 6}.gx-game .art,.gx-game:nth-child(n+4) .art{width:44%}}
@media (max-width:640px){.gx-games{grid-template-columns:1fr;grid-auto-rows:auto}.gx-game,.gx-game:nth-child(n+4),.gx-game:last-child{grid-column:auto;min-height:340px}.gx-game .art,.gx-game:nth-child(n+4) .art{width:46%;top:14%}}

/* resume strip */
.gx-resume{padding:clamp(34px,4.4vw,56px) 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.gx-resume .gx-sec{padding-top:0;padding-bottom:0;display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:clamp(24px,5vw,72px);align-items:center}
.gx-resume h2{font:700 clamp(26px,3vw,38px)/1.12 var(--f-ui);letter-spacing:-.025em;margin-top:12px}
.gx-resume p.sub{margin-top:10px;font-size:17px}
.gx-flow{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));list-style:none;padding:0;position:relative}
.gx-flow::before{content:"";position:absolute;left:10%;right:10%;top:11px;height:2px;background:linear-gradient(90deg,var(--line),var(--kick),var(--line))}
.gx-flow li{position:relative;text-align:center;padding-top:36px;font:600 12px/1.3 var(--f-mono);letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.gx-flow li::before{content:"";position:absolute;top:4px;left:50%;width:16px;height:16px;margin-left:-8px;border-radius:50%;background:var(--canvas);border:2px solid var(--muted)}
.gx-flow li:first-child::before,.gx-flow li:last-child::before{border-color:var(--kick);background:var(--kick)}
.gx-flow li:last-child{color:var(--ink)}
@media (max-width:860px){.gx-resume .gx-sec{grid-template-columns:1fr}}
@media (max-width:520px){.gx-flow{grid-template-columns:1fr;gap:10px}.gx-flow::before{left:7px;right:auto;top:8px;bottom:8px;width:2px;height:auto;background:linear-gradient(180deg,var(--kick),var(--line),var(--kick))}.gx-flow li{text-align:left;padding:0 0 0 32px}.gx-flow li::before{left:0;top:1px;margin-left:0}}

/* free and paid */
.gx-fair{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(12px,1.6vw,20px);margin-top:clamp(28px,4vw,48px);list-style:none;padding:0}
.gx-fair>li{position:relative;overflow:hidden;display:flex;flex-direction:column;background:var(--card);border:1px solid var(--line);border-radius:26px;padding:30px 28px 28px;box-shadow:var(--sh)}
.gx-fair>li::before{content:"";position:absolute;left:0;right:0;top:0;height:5px;background:var(--c)}
.gx-fair .n{font:500 64px/1 var(--f-mono);letter-spacing:-.04em;color:var(--ink)}
.gx-fair .n small{font-size:20px;letter-spacing:0;color:var(--muted);margin-left:6px}
.gx-fair h3{font:700 21px/1.25 var(--f-ui);margin-top:20px;letter-spacing:-.01em}
.gx-fair p.d{color:var(--muted);margin-top:8px;font-size:16px}
.gx-vz{margin-top:auto;padding-top:26px}
.gx-plays{display:flex;gap:8px}
.gx-plays i{flex:1;height:96px;border-radius:16px;background:var(--btn);color:var(--btn-ink);display:flex;flex-direction:column;justify-content:space-between;padding:12px 12px 10px;font:600 11px/1 var(--f-mono);font-style:normal;letter-spacing:.14em;text-transform:uppercase}
.gx-plays i b{font:300 38px/1 var(--f-ui);letter-spacing:-.04em}
.gx-ripple{position:relative;height:112px;border-radius:18px;background:linear-gradient(155deg,var(--mid),var(--deep));border:1px solid color-mix(in srgb,var(--a) 40%,transparent);overflow:hidden;color:var(--a)}
.gx-ripple svg{position:absolute;right:-8%;top:-22%;width:62%;height:auto}
.gx-ripple span{position:absolute;left:16px;bottom:14px;font:600 11px/1 var(--f-mono);letter-spacing:.16em;text-transform:uppercase;color:var(--a)}
.gx-seats{position:relative;height:112px;border-radius:18px;background:var(--chip);border:1px solid var(--line);display:grid;place-items:center}
.gx-seats::before{content:"";width:150px;height:58px;border-radius:50%;border:1.5px dashed var(--muted);opacity:.7;position:absolute}
.gx-seats b{position:relative;font:600 11px/1 var(--f-mono);letter-spacing:.14em;text-transform:uppercase;color:var(--ink)}
.gx-seat{position:absolute;width:30px;height:30px;border-radius:50%;background:var(--btn);color:var(--btn-ink);display:grid;place-items:center;font:700 12px/1 var(--f-text)}
.gx-seat.s1{left:20%;top:16%}.gx-seat.s2{right:20%;top:16%}.gx-seat.s3{left:20%;bottom:16%}.gx-seat.s4{right:20%;bottom:16%}
.gx-seat.host{box-shadow:0 0 0 2px var(--card),0 0 0 4px #D9951C}
.gx-tiers{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(10px,1.4vw,16px);list-style:none;padding:0;margin-top:clamp(16px,2vw,24px)}
.gx-tiers li{border:1px solid var(--line);background:var(--card);border-radius:18px;padding:16px 18px;box-shadow:var(--sh)}
.gx-tiers b{display:block;font:700 17px/1.3 var(--f-ui)}
.gx-tiers span{display:block;margin-top:4px;font:600 11.5px/1.5 var(--f-mono);letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.gx-fine{color:var(--muted);font-size:15.5px;margin-top:20px;max-width:72ch}
@media (max-width:860px){.gx-fair{grid-template-columns:1fr}.gx-tiers{grid-template-columns:1fr}}

/* privacy band */
.gx-priv .gx-in{display:block;text-align:center;min-height:0;padding-top:clamp(64px,9vw,120px);padding-bottom:clamp(56px,7vw,96px)}
.gx-priv::before{background:radial-gradient(80% 90% at 50% 40%,var(--deep) 0%,color-mix(in srgb,var(--deep) var(--scrim-pct),transparent) 100%)}
.gx-priv .gx-kicker{justify-content:center}.gx-priv .gx-kicker::after{display:none}
.gx-priv h2{font:800 clamp(40px,6.4vw,92px)/.98 var(--f-ui);letter-spacing:-.04em;margin:20px auto 0;max-width:14ch;text-wrap:balance}
.gx-priv h2 em{font:italic 500 1em/1 var(--f-serif);color:var(--peach)}
.gx-priv p.lead{color:var(--cream2);max-width:54ch;margin:24px auto 0;font-size:18px}
.gx-priv__grid{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);gap:clamp(14px,2vw,28px);text-align:left;margin:clamp(36px,5vw,60px) auto 0;max-width:1000px}
.gx-none{background:var(--deep);border:1px solid rgba(245,242,236,.22);border-radius:26px;padding:26px 28px 14px}
.gx-none h3{font:600 12px/1.3 var(--f-mono);letter-spacing:.2em;text-transform:uppercase;color:var(--a)}
.gx-none ul{list-style:none;padding:0;margin-top:12px}
.gx-none li{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:14px 0;border-top:1px solid rgba(245,242,236,.14);font:500 18px/1.2 var(--f-text);color:var(--cream)}
.gx-none li span{font:600 12px/1 var(--f-mono);letter-spacing:.14em;text-transform:uppercase;color:var(--cream3);display:flex;align-items:center;gap:8px;white-space:nowrap}
.gx-none li span::before{content:"";width:14px;height:2px;border-radius:2px;background:currentColor}
.gx-none li.yes b{font-weight:700}
.gx-none li.yes span{color:var(--a)}
.gx-none li.yes span::before{width:12px;height:7px;border-radius:0;background:none;border-left:2px solid currentColor;border-bottom:2px solid currentColor;transform:rotate(-45deg) translateY(-2px)}
.gx-trust{display:grid;gap:10px;list-style:none;padding:0}
.gx-trust li{background:var(--deep);border:1px solid rgba(245,242,236,.22);border-radius:22px;padding:18px 22px;display:grid;grid-template-columns:118px minmax(0,1fr);gap:16px;align-items:center}
.gx-trust b{font:500 26px/1 var(--f-mono);letter-spacing:-.04em;color:var(--cream);white-space:nowrap}
.gx-trust p{font-size:15.5px;line-height:1.5;color:var(--cream2)}
.gx-priv a.more{display:inline-flex;align-items:center;min-height:48px;margin-top:clamp(28px,4vw,44px);font:600 16px/1 var(--f-text);color:#0A0908;background:var(--cream);padding:0 26px;border-radius:99px;text-decoration:none}
.gx-priv a.more:hover{background:#fff}
@media (max-width:860px){.gx-priv__grid{grid-template-columns:1fr}.gx-trust li{grid-template-columns:104px minmax(0,1fr)}}
@media (max-width:520px){.gx-trust li{grid-template-columns:1fr;gap:6px}}

/* footer */
.gx-foot{max-width:var(--wrap);margin:0 auto;padding:clamp(44px,6vw,80px) var(--pad) 36px}
.gx-foot__top{display:flex;flex-wrap:wrap;gap:28px 40px;justify-content:space-between;align-items:center}
.gx-foot__id{flex:1 1 420px;min-width:0}
.gx-foot .gx-brand{color:var(--ink)}
.gx-foot .gx-brand img{box-shadow:0 0 0 1px var(--line)}
.gx-foot p.tag{font:italic 500 clamp(19px,1.8vw,22px)/1.35 var(--f-serif);margin-top:10px;text-wrap:balance;color:var(--ink)}
.gx-foot ul{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:8px}
.gx-foot nav a{display:inline-flex;align-items:center;min-height:44px;padding:0 18px;border-radius:99px;border:1px solid var(--line);background:var(--card);color:var(--ink);text-decoration:none;font:500 15px/1 var(--f-text)}
.gx-foot nav a:hover{background:var(--chip)}
.gx-foot__bot{margin-top:36px;padding-top:20px;border-top:1px solid var(--line);color:var(--muted);font-size:14px;display:flex;flex-wrap:wrap;gap:8px 28px;justify-content:space-between}
@media (max-width:640px){.gx-foot nav a{padding:0 20px;min-height:46px}.gx-foot ul{gap:10px}}

/* legal pages */
.gx-top{--tw:720px;position:relative;isolation:isolate;box-shadow:inset 0 -1px 0 rgba(245,242,236,.3);overflow:hidden;color:var(--cream);background:var(--deep);border-radius:0 0 clamp(26px,3.4vw,48px) clamp(26px,3.4vw,48px)}
.gx-top__bg{position:absolute;inset:0;z-index:-2;background:url(media/plate-search.webp) 50% 40%/cover;filter:brightness(1.05)}
.gx-top::before{content:"";position:absolute;inset:0;z-index:-1;background:
 linear-gradient(180deg,color-mix(in srgb,var(--deep) var(--scrim-pct),transparent) 0,color-mix(in srgb,var(--deep) var(--scrim-pct),transparent) 104px,transparent 210px),
 linear-gradient(90deg,var(--deep) 0%,color-mix(in srgb,var(--deep) var(--scrim-pct),transparent) calc(max(0px,50% - var(--wrap)/2) + var(--pad) + var(--tw) + 24px),color-mix(in srgb,var(--deep) 30%,transparent) 100%)}
.gx-top__t{max-width:var(--wrap);margin:0 auto;padding:clamp(34px,5vw,76px) var(--pad) clamp(40px,5.4vw,76px)}
.gx-top__t>*{max-width:var(--tw)}
.gx-top h1{font:800 clamp(42px,6.4vw,88px)/1 var(--f-ui);letter-spacing:-.04em;margin-top:18px}
.gx-top h1 em{font:italic 500 1em/1 var(--f-serif);color:var(--peach)}
.gx-top h1::after{content:"";display:block;width:76px;height:5px;border-radius:5px;background:linear-gradient(90deg,#FF9A55,#F5B742);margin-top:22px}
.gx-top .meta{display:inline-block;font:500 13px/1.5 var(--f-mono);letter-spacing:.08em;color:var(--cream2);margin-top:20px;padding:6px 12px;border-radius:10px;background:color-mix(in srgb,var(--deep) var(--scrim-pct),transparent)}
.gx-top .gx-kicker::after{display:none}
.gx-legal{max-width:var(--wrap);margin:0 auto;padding:clamp(32px,5vw,72px) var(--pad) 0;display:grid;grid-template-columns:270px minmax(0,1fr);gap:clamp(28px,6vw,96px);align-items:start}
.gx-toc--d{position:sticky;top:20px}
.gx-toc h2,.gx-toc summary{font:600 12px/1 var(--f-mono);letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}
.gx-toc h2{margin-bottom:14px}
.gx-toc ol{list-style:none;margin:0;padding:0;border-left:1px solid var(--line)}
.gx-toc ol a{display:block;padding:8px 14px;margin-left:-1px;border-left:2px solid transparent;color:var(--muted);text-decoration:none;font:500 15px/1.35 var(--f-text)}
.gx-toc ol a:hover,.gx-toc ol a[aria-current]{color:var(--ink);border-left-color:var(--link)}
.gx-toc ol a[aria-current]{font-weight:600}
.gx-toc ol .sub a{padding-left:28px;font-size:14px}
.gx-also{margin-top:26px;padding-top:18px;border-top:1px solid var(--line)}
.gx-also p{font:600 12px/1 var(--f-mono);letter-spacing:.2em;text-transform:uppercase;color:var(--muted);margin-bottom:6px}
.gx-also a{display:flex;align-items:center;min-height:44px;color:var(--link);font:600 15px/1.3 var(--f-text);text-decoration:none}
.gx-also a:hover{text-decoration:underline}
.gx-toc--m{display:none;margin-bottom:18px;border:1px solid var(--line);border-radius:18px;background:var(--card);padding:0 18px;box-shadow:var(--sh)}
.gx-toc--m summary{display:flex;align-items:center;justify-content:space-between;min-height:52px;cursor:pointer;list-style:none}
.gx-toc--m summary::-webkit-details-marker{display:none}
.gx-toc--m summary::after{content:"";width:9px;height:9px;border-right:2px solid currentColor;border-bottom:2px solid currentColor;transform:rotate(45deg) translateY(-2px)}
.gx-toc--m[open] summary::after{transform:rotate(-135deg)}
.gx-toc--m .gx-also{margin-bottom:10px}
.gx-toc--m ol{margin-bottom:6px}
.gx-doc{max-width:70ch;min-width:0;counter-reset:gxsec}
.gx-short{position:relative;background:var(--card);border:1px solid var(--line);border-radius:22px;padding:24px 26px 24px 32px;box-shadow:var(--sh)}
.gx-short::before{content:"";position:absolute;left:0;top:20px;bottom:20px;width:4px;border-radius:0 4px 4px 0;background:linear-gradient(180deg,#5DD4FF,#0077FF)}
.gx-short .k{font:600 12px/1 var(--f-mono);letter-spacing:.2em;text-transform:uppercase;color:var(--kick);margin-bottom:12px}
.gx-short p:last-child{font-size:18.5px;line-height:1.65;margin:0}
.gx-facts{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;list-style:none;padding:0;margin-top:14px}
.gx-facts li{border:1px solid var(--line);background:var(--card);border-radius:16px;padding:14px 16px}
.gx-facts b{display:block;font:500 24px/1.1 var(--f-mono);letter-spacing:-.03em}
.gx-facts span{display:block;margin-top:6px;font:600 11px/1.4 var(--f-mono);letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.gx-sec2{margin-top:clamp(40px,5vw,56px)}
.gx-doc h2{font:700 clamp(24px,2.6vw,32px)/1.2 var(--f-ui);letter-spacing:-.02em;margin:0 0 14px;scroll-margin-top:24px;display:flex;align-items:baseline;gap:14px}
.gx-doc h2::before{counter-increment:gxsec;content:counter(gxsec,decimal-leading-zero);font:600 13px/1 var(--f-mono);letter-spacing:.14em;color:var(--kick);flex:none}
.gx-doc h3{font:700 19px/1.3 var(--f-ui);letter-spacing:-.01em;margin:0 0 6px;scroll-margin-top:24px}
.gx-doc p{font-size:18px;line-height:1.72;margin:0 0 18px;color:var(--ink)}
.gx-doc strong{font-weight:650}
.gx-q{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:20px 24px 4px;margin:0 0 12px}
.gx-q p{font-size:17px;line-height:1.65}
.gx-doc .contact{display:flex;align-items:center;min-height:56px;width:fit-content;max-width:100%;padding:0 24px;border:1px solid var(--line);background:var(--card);border-radius:99px;font:600 20px/1.2 var(--f-ui);box-shadow:var(--sh);overflow-wrap:anywhere}
.gx-end{margin-top:56px;padding-top:24px;border-top:1px solid var(--line);color:var(--muted);font-size:15px}
.gx-doc .gx-end{font-size:15px;margin-bottom:0;color:var(--muted)}
@media (max-width:900px){.gx-legal{grid-template-columns:1fr;gap:20px}.gx-toc--d{display:none}.gx-toc--m{display:block}.gx-facts{grid-template-columns:1fr}}
@media (max-width:480px){.gx-doc p{font-size:17px}.gx-doc .contact{font-size:17px;padding:0 18px}}
'''

# ---------------------------------------------------------------------------------------------- colour maths
def _rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _lum(h):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = _rgb(h)
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def ratio(a, b):
    la, lb = _lum(a), _lum(b)
    if la < lb:
        la, lb = lb, la
    return (la + 0.05) / (lb + 0.05)


def _over_white(deep, pct):
    """The stage colour at `pct` % over a pure white pixel: the lightest thing text can sit on under the scrim."""
    a = pct / 100
    return '#%02X%02X%02X' % tuple(round(c * a + 255 * (1 - a)) for c in _rgb(deep))


def _decl(d, extra=None):
    return ';'.join(f'--{k.replace("_", "-")}:{v}' for k, v in {**d, **(extra or {})}.items())


def css():
    keys = '\n'.join(f'.k-{k}{{--a:{v["a"]};--b:{v["b"]};--deep:{v["deep"]};--mid:{v["mid"]}}}' for k, v in KEYS.items())
    keys += '\n.k-vault{--copper:#FF9C54}'
    return (CSS.replace('__LIGHT__', _decl(LIGHT)).replace('__DARK__', _decl(DARK)).replace('__FIXED__', _decl(FIXED))
            .replace('__SCRIM__', str(SCRIM))) + keys + '\n'


# ---------------------------------------------------------------------------------------------- audit
def _vars(block):
    return {k: v for k, v in re.findall(r'--([a-z0-9-]+):(#[0-9A-Fa-f]{6})', block)}


def _header_scrim(style, f, scrim):
    """The legal header's real scrim, read from the stylesheet: a vertical layer (nav band) over a left-to-right layer.
    Text sits in two places: the nav (top band, full width) and the text column (--tw wide from the wrap's left edge).
    Worst case is the art at pure white under the composited alpha, evaluated at every viewport width 320-2560."""
    top = re.sub(r'\s*\n\s*', '', re.search(r'\.gx-top::before\{([^}]*)\}', style).group(1))
    v = re.search(r'linear-gradient\(180deg,color-mix\(in srgb,var\(--deep\) (var\(--scrim-pct\)|\d+%),transparent\) 0,color-mix\(in srgb,var\(--deep\) \1,transparent\) (\d+)px', top)
    h = re.search(r'linear-gradient\(90deg,var\(--deep\) 0%,color-mix\(in srgb,var\(--deep\) (var\(--scrim-pct\)|\d+%),transparent\) (calc\(.*?\)),color-mix\(in srgb,var\(--deep\) (\d+)%,transparent\) 100%\)', top)
    if not (v and h):
        return [('both', 'legal header: scrim layers not recognised', f['cream2'], f['stage'], 0.0)]
    pct = lambda t: scrim if t.startswith('var') else int(t.rstrip('%'))
    band, v_a = int(v.group(2)), pct(v.group(1)) / 100
    h_hold, h_end = pct(h.group(1)) / 100, int(h.group(3)) / 100
    wrap = int(re.search(r'--wrap:(\d+)px', style).group(1))
    tw = int(re.search(r'\.gx-top\{--tw:(\d+)px', style).group(1))
    pad = lambda w: min(56, max(20, 0.04 * w))
    nav_h = 18 * 2 + int(re.search(r'\.gx-nav a:not\(\.gx-brand\)\{[^}]*min-height:(\d+)px', style).group(1))
    expr = h.group(2)
    stop = lambda w: eval(re.sub(r'[^0-9.+\-*/(),maxpd ]', '', expr.replace('calc', '').replace('var(--wrap)', str(wrap)).replace('var(--pad)', str(pad(w)))
                                  .replace('var(--tw)', str(tw)).replace('50%', str(w / 2)).replace('px', '')), {'max': max})
    # nav band: both layers cover it, the weaker one is the right edge of the horizontal layer
    nav_alpha = 1 - (1 - v_a) * (1 - min(h_hold, h_end)) if nav_h <= band else 0.0
    # text column: must end before the horizontal layer starts to fade
    col_ok = all(max(0, (w - wrap) / 2) + pad(w) + tw <= stop(w) for w in range(320, 2561, 4))
    col_alpha = h_hold if col_ok else 0.0
    out = []
    for name, al in (('nav band', nav_alpha), ('text column', col_alpha)):
        worst = _over_white(KEYS['priv']['deep'], al * 100)
        for fgn in ('cream', 'cream2', 'peach'):
            out.append(('both', f'legal header {name}: {fgn} on art under the real scrim ({al:.0%}, art at white)', f[fgn], worst, round(ratio(f[fgn], worst), 2)))
    meta = re.search(r'\.gx-top \.meta\{([^}]*)\}', style).group(1)
    ok_meta = 'background:color-mix(in srgb,var(--deep) var(--scrim-pct),transparent)' in meta
    out.append(('both', 'legal header: meta line has its own scrim', f['cream2'], f['stage'], round(ratio(f['cream2'], _over_white(KEYS['priv']['deep'], scrim)), 2) if ok_meta else 0.0))
    return out



def audit(html):
    """Contrast of every text/background pair the stylesheet can put on screen, read back from the <style> of a
    generated page: the paper surfaces in light and dark, the dark stages and game cards in 'both'. Text on art is
    measured against the stage colour at the scrim over white. -> (rows, ok); a row is (mode, label, fg, bg, ratio)."""
    style = re.search(r'<style>(.*?)</style>', html, re.S).group(1)
    root = re.search(r':root\{(.*?)\}\n@media', style, re.S).group(1)
    light = _vars(root)
    dark = dict(light, **_vars(re.search(r'prefers-color-scheme:dark\)\{:root\{([^}]*)\}', style).group(1)))
    scrim = int(re.search(r'--scrim-pct:(\d+)%', root).group(1))
    rows = []

    def add(mode, label, fg, bg):
        rows.append((mode, label, fg, bg, round(ratio(fg, bg), 2)))

    for mode, v in (('light', light), ('dark', dark)):
        for surf in ('canvas', 'canvas2', 'card', 'chip'):
            for fgn in ('ink', 'muted', 'link', 'kick'):
                if surf == 'chip' and fgn == 'kick':
                    continue
                add(mode, f'{fgn} on {surf}', v[fgn], v[surf])
        add(mode, 'button text on button', v['btn-ink'], v['btn'])
    f = light
    for fgn in ('cream', 'cream2', 'cream3'):
        add('both', f'{fgn} on stage', f[fgn], f['stage'])
    add('both', 'dark button text on cream', '#0A0908', f['cream'])
    add('both', 'skip link text', '#1A1814', f['cream'])
    for k, kv in re.findall(r'\.k-([a-z]+)\{([^}]*)\}', style):
        c = _vars(kv)
        if 'deep' not in c:
            continue
        worst = _over_white(c['deep'], scrim)
        for fgn, fgc in (('cream', f['cream']), ('cream2', f['cream2']), ('cream3', f['cream3']), ('accent', c['a']), ('second colour', c['b'])):
            add('both', f'{k}: {fgn} on art under scrim (worst case)', fgc, worst)
            add('both', f'{k}: {fgn} on card/inset', fgc, c['deep'])
            add('both', f'{k}: {fgn} on card gradient end', fgc, c['mid'])
        add('both', f'{k}: peach on art under scrim (worst case)', f['peach'], worst)
        add('both', f'{k}: focus ring on dark', f['sfocus'], c['deep'])
    rows += _header_scrim(style, f, scrim)
    for fgn in ('copper',):
        m = re.search(r'--copper:(#[0-9A-Fa-f]{6})', style)
        v = re.search(r'\.k-vault\{--a:[^}]*--deep:(#[0-9A-Fa-f]{6})', style)
        add('both', 'vault: copper crew on card/inset', m.group(1), v.group(1))
    return rows, all(r[4] >= MIN for r in rows)


# ---------------------------------------------------------------------------------------------- pieces
MAIL = 'hello@seizeapps.com'
NAV = [('./', 'Home', 'index'), ('privacy.html', 'Privacy', 'privacy'), ('terms.html', 'Terms', 'terms'), ('support.html', 'Support', 'support')]


def _phone(cls, name, w, h, alt, lazy=True, prio=False):
    attrs = ' loading="lazy" decoding="async"' if lazy else (' fetchpriority="high"' if prio else '')
    return (f'<figure class="gx-phone {cls}"><div class="gx-phone__s"><img src="media/{name}.webp" width="{w}" height="{h}" '
            f'alt="{alt}"{attrs}></div></figure>')


SHOTS = {
    'unison': ('shot-unison', 600, 1303, 'Unison in play: a glowing card numbered 42 and a Call an Echo button.'),
    'imp-word': ('shot-impostor-word', 603, 1311, 'Impostor word screen showing the secret word Star, for your eyes only.'),
    'imp-clue': ('shot-impostor-clue', 600, 1303, 'Impostor in the clue round: a masquerade invitation sealed with red wax and the order the players speak in.'),
    'lobby': ('shot-lobby-qr', 603, 1311, 'The lobby: a room code, a QR code to scan, Copy and Share buttons, the language setting and the list of players.'),
    'vault-ring': ('shot-vault-ringleader', 603, 1311, 'Vault, ringleader view: the Copper Crew’s turn, the score, a hint field and the blueprint grid of words.'),
    'vault-heist': ('shot-vault-heist', 603, 1311, 'Vault, the heist briefing: the Copper Crew and the Jade Crew.'),
    'spot-play': ('shot-spoton-ko-play', 603, 1311, 'Spot On in a Korean room: the dial, the clue giver and the two team scores.'),
    'spot-teams': ('shot-spoton-ko-teams', 603, 1311, 'Spot On in a Korean room: the team screen.'),
}


def ph(cls, key, lazy=True, prio=False):
    n, w, h, alt = SHOTS[key]
    return _phone(cls, n, w, h, alt, lazy, prio)


def _nav(key, legal=False):
    brand = '<a class="gx-brand" href="./" aria-label="GamingHub, home"><img src="media/icon-180.png" width="38" height="38" alt=""><span>GamingHub</span></a>'
    if legal:
        links = ''.join(f'<li><a href="{h}"{" aria-current=page" if k == key else ""}>{l}</a></li>' for h, l, k in NAV)
        return f'<nav class="gx-nav gx-nav--legal" aria-label="GamingHub">{brand}<ul>{links}</ul></nav>'
    return (f'<nav class="gx-nav" aria-label="GamingHub">{brand}<ul><li class="hide-s"><a href="#games">Games</a></li>'
            f'<li><a href="privacy.html">Privacy</a></li><li><a href="support.html">Support</a></li></ul></nav>')


def _footer():
    chips = ''.join(f'<li><a href="{h}">{l}</a></li>' for h, l in (('privacy.html', 'Privacy'), ('terms.html', 'Terms'), ('support.html', 'Support')))
    return (f'<footer class="gx-foot"><div class="gx-foot__top"><div class="gx-foot__id"><a class="gx-brand" href="./">'
            f'<img src="media/icon-180.png" width="38" height="38" alt="">GamingHub</a>'
            f'<p class="tag">GamingHub, party games for the room you are in.</p></div>'
            f'<nav aria-label="Footer"><ul>{chips}<li><a href="mailto:{MAIL}">{MAIL}</a></li></ul></nav></div>'
            f'<div class="gx-foot__bot"><span>GamingHub: Party Games, coming soon to the App Store for iPhone.</span>'
            f'<span>&copy; 2026 Izotz Cristobal Mota</span></div></footer>')


ART = {
    'uni': '<svg class="art" viewBox="0 0 400 300" fill="none" stroke="currentColor" aria-hidden="true"><g stroke-opacity=".28"><circle cx="300" cy="110" r="60"/><circle cx="300" cy="110" r="110"/><circle cx="300" cy="110" r="170"/><circle cx="300" cy="110" r="240"/></g><circle cx="290" cy="82" r="44" stroke-width="13" stroke-opacity=".4"/><circle cx="340" cy="94" r="44" stroke-width="13" stroke-opacity=".4"/><circle cx="312" cy="96" r="10" fill="currentColor" stroke="none" fill-opacity=".6"/></svg>',
    'imp': '<svg class="art" viewBox="0 0 200 120" aria-hidden="true"><path fill="currentColor" fill-opacity=".34" fill-rule="evenodd" d="M8 52C8 20 58 10 100 30c42-20 92-10 92 22 0 32-40 56-72 38-10-6-30-6-40 0C48 108 8 84 8 52Z M38 54q20-16 44 0-22 14-44 0Z M162 54q-20-16-44 0 22 14 44 0Z"/></svg>',
    'vault': '<svg class="art" viewBox="0 0 300 300" fill="none" stroke="currentColor" aria-hidden="true"><rect x="40" y="30" width="230" height="230" rx="52" stroke-opacity=".3" stroke-width="3"/><circle cx="155" cy="145" r="84" stroke-opacity=".38" stroke-width="12"/><circle cx="155" cy="145" r="108" stroke-opacity=".34" stroke-width="3" stroke-dasharray="3 14.6"/><path d="M155 145 214 86" stroke-opacity=".55" stroke-width="16" stroke-linecap="round"/><circle cx="155" cy="145" r="17" fill="currentColor" stroke="none" fill-opacity=".55"/></svg>',
    'spot': '<svg class="art" viewBox="0 0 300 200" fill="none" stroke="currentColor" aria-hidden="true"><g stroke-opacity=".36" stroke-width="3"><path d="M20 180A130 130 0 0 1 280 180"/><path d="M52 180A98 98 0 0 1 248 180" stroke-opacity=".26"/><path d="M84 180A66 66 0 0 1 216 180" stroke-opacity=".2"/></g><g stroke-opacity=".26" stroke-width="2"><path d="M150 180V50M150 180 72 80M150 180 228 80M150 180 40 118M150 180 260 118"/></g><path d="M150 180 206 74" stroke="#FFC23D" stroke-opacity=".85" stroke-width="7" stroke-linecap="round"/><circle cx="150" cy="180" r="12" fill="#FFC23D" stroke="none" fill-opacity=".9"/></svg>',
    'fish': '<svg class="art" viewBox="0 0 260 220" fill="none" stroke="currentColor" aria-hidden="true"><path d="M52 66C40 150 80 196 130 196s90-46 78-130" stroke-opacity=".45" stroke-width="5" stroke-linecap="round"/><ellipse cx="130" cy="66" rx="78" ry="14" stroke-opacity=".45" stroke-width="5"/><g fill="currentColor" stroke="none" fill-opacity=".28"><rect x="86" y="112" width="44" height="26" rx="5" transform="rotate(-14 108 125)"/><rect x="122" y="130" width="44" height="26" rx="5" transform="rotate(10 144 143)"/><rect x="100" y="146" width="44" height="26" rx="5" transform="rotate(-4 122 159)"/></g><g stroke-opacity=".5" stroke-width="3"><circle cx="196" cy="100" r="9"/><circle cx="76" cy="140" r="6"/><circle cx="172" cy="40" r="7"/><circle cx="196" cy="24" r="4"/></g></svg>',
}
GAMES = [
    ('uni', 'Unison', 'Free', 'Silent, as one', 'Play your cards in ascending order without talking. Silence is the whole game.', '2&ndash;4 players &middot; 15&ndash;25 min'),
    ('imp', 'Impostor', 'Three free plays', 'Someone wears the mask', 'At a masquerade ball everyone knows the secret word except one guest. Give clues, whisper, and unmask the impostor.', '3&ndash;12 players &middot; 10&ndash;20 min'),
    ('vault', 'Vault', 'Three free plays', 'A word heist', 'Two rival crews crack safe-deposit boxes with one-word hints. Careful with the Alarm.', '4&ndash;20 players &middot; 15&ndash;30 min'),
    ('spot', 'Spot On', 'Three free plays', 'One clue, one arrow', 'Read the dial, give a clue and land closest to the bullseye.', '4&ndash;12 players &middot; 30&ndash;45 min'),
    ('fish', 'Fishbowl', 'Three free plays', 'Slips against the clock', 'Three rounds, one bowl of name slips. Describe, mime, catch.', '4&ndash;20 players &middot; 20&ndash;40 min'),
]


def _stage(key, cls, plate, hue, br, head, inner_copy, vis, extra=''):
    return (f'<section class="gx-stage gx-dark k-{key} {cls}" aria-labelledby="{head}" style="--plate:url(media/{plate}.webp);--hue:{hue}deg;--br:{br}">\n'
            f' <div class="gx-stage__bg" aria-hidden="true"></div>\n <div class="gx-in">\n  <div class="gx-copy">\n{inner_copy}\n  </div>\n'
            f'  <div class="gx-vis">\n{vis}\n  </div>\n </div>\n</section>')


def _home():
    hero = f'''<header class="gx-hero gx-dark k-hero">
 <div class="gx-hero__bg" aria-hidden="true"></div>
 {_nav('index')}
 <div class="gx-hero__copy">
  <p class="gx-kicker">Party games &middot; For iPhone</p>
  <h1>Game night, <em>one phone each.</em></h1>
  <p class="gx-lede">Create a room, share the code and every friend plays from their own phone. Each device shows only what you&rsquo;re allowed to see: your role, your word, your cards.</p>
  <p class="gx-soon"><b aria-hidden="true"></b><span>Coming soon to the App Store</span><span class="b">for iPhone</span></p>
 </div>
 <div class="gx-fan" role="group" aria-label="Screens from five games">
  {ph('p1', 'unison', False)}{ph('p2', 'imp-word', False)}{ph('p3', 'lobby', False, True)}{ph('p4', 'vault-ring', False)}{ph('p5', 'spot-play', False)}
 </div>
 <div class="gx-stripband"><ul class="gx-strip" aria-label="GamingHub at a glance"><li><b>5</b><span>Games</span></li><li><b>2&ndash;20</b><span>Players</span></li><li><b>9</b><span>Languages</span></li><li><b>0</b><span>Accounts</span></li></ul></div>
</header>'''
    room = _stage('hub', 't-hub', 'plate-one-code', 0, 1.1, 'h-room', '''   <p class="gx-kicker"><i>01</i> Room code</p>
   <h2 id="h-room">One code. Everyone&rsquo;s in.</h2>
   <p class="t">Create a room and share the code or the QR. Friends join from their own phone and appear in the live lobby as they arrive.</p>
   <div class="gx-ticket"><small>Room code</small><strong>EVDF4C</strong></div>''',
                  f'   {ph("back", "imp-clue")}\n   {ph("front", "lobby")}')
    resume = '''<section class="gx-resume gx-paper" aria-labelledby="h-resume"><div class="gx-sec">
 <div><p class="gx-kicker">Your table, resumed</p><h2 id="h-resume">Back at your table, whatever happened.</h2><p class="sub">Resume your table after a call, a lock screen or a restart.</p></div>
 <ol class="gx-flow" aria-label="Interruptions you can resume from"><li>In the game</li><li>A call</li><li>Lock screen</li><li>A restart</li><li>Your table</li></ol>
</div></section>'''
    imp = _stage('imp', 't-imp gx-stage--rev', 'plate-secrets', 136, 1.35, 'h-secret', f'''   <p class="gx-kicker"><i>02</i> Impostor</p>
   <h2 id="h-secret">Secrets stay on your phone.</h2>
   <p class="t">At a masquerade ball everyone knows the secret word except one guest. Give clues, whisper, and unmask the impostor.</p>
   <p class="t">Your role, your word and your cards go only to your own device.</p>
   <div class="gx-word"><small>Your word &middot; for your eyes only</small><span>Star</span></div>
   <dl class="gx-table"><div><dt>Players</dt><dd>3&ndash;12 players, about 10&ndash;20 minutes.</dd></div><div><dt>Try it</dt><dd>Three free plays; free at any table whose host owns it.</dd></div></dl>''',
                  f'   {ph("back", "imp-clue")}\n   {ph("front", "imp-word")}')
    cards = ''
    for i, (k, name, chip, tag, blurb, meta) in enumerate(GAMES, 1):
        cards += (f'<li class="gx-game k-{k}">{ART[k]}<div class="top"><span class="chip">{chip}</span><span class="no">0{i} / 05</span></div>'
                  f'<h3>{name}</h3><p class="tag">{tag}</p><p class="blurb">{blurb}</p><p class="meta">{meta}</p></li>\n')
    games = f'''<section class="gx-paper" id="games" aria-labelledby="h-games"><div class="gx-sec">
 <p class="gx-kicker"><i>03</i> The table</p>
 <h2 id="h-games">Five games, <em>one table.</em></h2>
 <p class="sub">Pick a game, share the code, and everyone plays from their own phone. Each one has its own look, its own rules and its own way of keeping a secret.</p>
 <ul class="gx-games">
{cards} </ul>
</div></section>'''
    uni = _stage('uni', 't-uni gx-stage--rev gx-stage--strip', 'plate-in-sync', -64, 1.25, 'h-silence', '''   <p class="gx-kicker"><i>04</i> Unison</p>
   <h2 id="h-silence">Play in silence. Play in sync.</h2>
   <p class="t">Play your cards in ascending order without talking. Silence is the whole game.</p>
   <ul class="gx-meta"><li class="on">Unison is free</li><li>2&ndash;4 players</li><li>15&ndash;25 min</li></ul>''',
                 f'   {ph("back", "lobby")}\n   {ph("front", "unison")}')
    vault = _stage('vault', 't-vault gx-stage--tall', 'plate-two-crews', 188, 1.35, 'h-vault', '''   <p class="gx-kicker"><i>05</i> The heist</p>
   <h2 id="h-vault">Two crews. One vault.</h2>
   <p class="t">Give one-word hints and crack your crew&rsquo;s safes first. Careful with the Alarm.</p>
   <div class="gx-crews"><span class="cu">COPPER CREW</span><span class="ja">JADE CREW</span></div>
   <dl class="gx-table"><div><dt>Ringleaders</dt><dd>Each crew has a Ringleader who sees the blueprint and gives one hint and one number per turn.</dd></div><div><dt>Players</dt><dd>4&ndash;20 players, about 15&ndash;30 minutes.</dd></div></dl>''',
                   f'   {ph("back", "vault-heist")}\n   {ph("front", "vault-ring")}')
    langs = ''.join(f'<li lang="{c}">{n}</li>' for c, n in (('en', 'English'), ('es', 'Espa&ntilde;ol'), ('fr', 'Fran&ccedil;ais'), ('de', 'Deutsch'), ('it', 'Italiano'),
                                                              ('pt', 'Portugu&ecirc;s'), ('ja', '日本語'), ('ko', '한국어'), ('zh', '中文')))
    lang = _stage('spot', 't-spot gx-stage--rev', 'plate-search', -30, 1.25, 'h-lang', f'''   <p class="gx-kicker"><i>06</i> Nine languages</p>
   <h2 id="h-lang">Play in your language.</h2>
   <p class="t">Each room is played in the language its creator picks, and everyone at the table sees the game in it.</p>
   <ul class="gx-langs" aria-label="Languages">{langs}</ul>
   <p class="gx-cap">Pictured: a Spot On table playing in Korean.</p>''',
                  f'   {ph("back", "spot-teams")}\n   {ph("front", "spot-play")}')
    fair = f'''<section class="gx-paper" id="fair" aria-labelledby="h-fair"><div class="gx-sec">
 <p class="gx-kicker"><i>07</i> Fair to the whole table</p>
 <h2 id="h-fair">Try before you buy. <em>Never a subscription.</em></h2>
 <ul class="gx-fair">
  <li style="--c:#2FBF7E"><p class="n">1<small>free game</small></p><h3>Unison is free.</h3><p class="d">Silent, as one: 2&ndash;4 players, about 15&ndash;25 minutes.</p>
   <div class="gx-vz"><div class="gx-ripple k-uni" role="img" aria-label="Unison, free to play">{ART["uni"].replace('class="art" ', '').replace('aria-hidden="true"', '')}<span>Free</span></div></div></li>
  <li style="--c:#E0364F"><p class="n">3<small>free plays</small></p><h3>Every other game is a one-time purchase.</h3><p class="d">Each paid game comes with three free plays so you can try it first.</p>
   <div class="gx-vz"><div class="gx-plays" role="img" aria-label="Three free plays"><i><b>1</b>Play</i><i><b>2</b>Play</i><i><b>3</b>Play</i></div></div></li>
  <li style="--c:#D9951C"><p class="n">0<small>plays spent</small></p><h3>If the host owns it, everyone plays free.</h3><p class="d">The whole table plays, and nobody spends a play.</p>
   <div class="gx-vz"><div class="gx-seats" role="img" aria-label="A table of four around a host who owns the game: everyone plays free"><span class="gx-seat s1 host">H</span><span class="gx-seat s2">A</span><span class="gx-seat s3">B</span><span class="gx-seat s4">C</span><b>Plays free</b></div></div></li>
 </ul>
 <ul class="gx-tiers" aria-label="Ways to unlock a paid game"><li><b>A single game</b><span>Impostor, Vault, Spot On or Fishbowl</span></li><li><b>All 4 games</b><span>The four paid games</span></li><li><b>GamingHub Lifetime</b><span>Every game, including future ones</span></li></ul>
 <p class="gx-fine">One-time purchases, never a subscription. Purchases are shared with your family through Family Sharing and can be restored from Settings.</p>
</div></section>'''
    priv = f'''<section class="gx-stage gx-dark gx-priv k-priv" aria-labelledby="h-priv" style="--plate:url(media/plate-header.webp);--hue:0deg;--br:1">
 <div class="gx-stage__bg" aria-hidden="true"></div>
 <div class="gx-in">
  <p class="gx-kicker"><i>08</i> Privacy</p>
  <h2 id="h-priv">Just a <em>name</em> you choose.</h2>
  <p class="lead">No account, no email, no ads and no tracking. Online play uses an anonymous device ID; rooms are deleted when empty and after 12 hours.</p>
  <div class="gx-priv__grid">
   <div class="gx-none"><h3>Nothing to sign up for</h3><ul><li>Account<span>None</span></li><li>Email<span>None</span></li><li>Ads<span>None</span></li><li>Tracking<span>None</span></li><li class="yes"><b>A name you choose</b><span>That&rsquo;s it</span></li></ul></div>
   <ul class="gx-trust"><li><b>12 h</b><p>A room is deleted when it empties, and in any case after 12 hours.</p></li><li><b>Camera</b><p>The only permission GamingHub asks for, used to scan a room&rsquo;s QR code. Nothing is saved.</p></li><li><b>No chat</b><p>Names are filtered, the host can remove a player, and you can report one from the app.</p></li></ul>
  </div>
  <a class="more" href="privacy.html">Read the privacy policy</a>
 </div>
</section>'''
    return f'''{hero}
<main id="main">
{room}
{resume}
{imp}
{games}
{uni}
{vault}
{lang}
{fair}
{priv}
</main>
{_footer()}'''


# ---------------------------------------------------------------------------------------------- legal pages
def _slug(text):
    return re.sub(r'[^a-z0-9]+', '-', re.sub(r'<[^>]+>', '', text).lower()).strip('-')


def _plain(h):
    return re.sub(r'<[^>]+>', '', h).strip()


def _split(body):
    """h1, the updated/effective line, the .summary paragraph, and [(h2 text, chunk html)]."""
    take = lambda pat: (lambda m: (m.group(1).strip(), body.replace(m.group(0), '', 1)) if m else ('', body))(re.search(pat, body, re.S))
    h1, body = take(r'<h1>(.*?)</h1>')
    upd, body = take(r'<p class="updated">(.*?)</p>')
    summ, body = take(r'<p class="summary">(.*?)</p>')
    parts = re.split(r'<h2>(.*?)</h2>', body)
    return h1, upd, summ, [(re.sub(r'^\d+\.\s+', '', h.strip()), c.strip()) for h, c in zip(parts[1::2], parts[2::2])]


def _legal(app, key, body, title):
    h1, upd, summ, secs = _split(body)
    words = h1.split()
    h1html = (' '.join(words[:-1]) + ' ' if len(words) > 1 else '') + f'<em>{words[-1]}</em>'
    meta = f'GamingHub: Party Games &middot; {upd}' if re.match(r'(Last updated|Effective)', upd) else upd
    toc, out = [], []
    for h, chunk in secs:
        sid = _slug(h)
        toc.append((sid, h, 1))
        if '<h3>' in chunk:
            qs = re.split(r'<h3>(.*?)</h3>', chunk)
            lead = qs[0].strip()
            items = ''
            for q, a in zip(qs[1::2], qs[2::2]):
                qid = _slug(q)
                toc.append((qid, _plain(q), 2))
                items += f'<article class="gx-q"><h3 id="{qid}">{q}</h3>\n{a.strip()}</article>\n'
            out.append(f'<section class="gx-sec2" aria-labelledby="s-{sid}"><h2 id="{sid}">{h}</h2>\n{lead}\n{items}</section>')
        else:
            out.append(f'<section class="gx-sec2" aria-labelledby="{sid}"><h2 id="{sid}">{h}</h2>\n{chunk}</section>')
    # a section with a single level only needs the h2 ids for the TOC; the support page lists its questions too
    toc_items = ''.join(f'<li{" class=sub" if lv == 2 else ""}><a href="#{i}">{t}</a></li>' for i, t, lv in toc)
    also = [('terms.html', 'Terms of Use', 'terms'), ('support.html', 'Support', 'support'), ('privacy.html', 'Privacy Policy', 'privacy')]
    also_html = ''.join(f'<a href="{h}">{l}</a>' for h, l, k in also if k != key) + '<a href="./">&larr; Back to GamingHub</a>'
    also_block = f'<div class="gx-also"><p>Also</p>{also_html}</div>'
    toc_d = f'<aside class="gx-toc gx-toc--d" aria-label="On this page"><h2>On this page</h2><ol>{toc_items}</ol>{also_block}</aside>'
    toc_m = f'<details class="gx-toc gx-toc--m"><summary>On this page</summary><ol>{toc_items}</ol>{also_block}</details>'
    short = ''
    if summ:
        text = re.sub(r'^<strong>The short version:</strong>\s*', '', summ)
        facts = ''
        if key == 'privacy':
            facts = ('<ul class="gx-facts" aria-label="Three facts"><li><b>12 h</b><span>Rooms expire</span></li><li><b>Camera</b><span>The only permission</span></li>'
                     '<li><b>No chat</b><span>Names filtered, host can remove</span></li></ul>')
        short = f'<div class="gx-short" role="note"><p class="k">The short version</p><p>{text}</p></div>\n{facts}'
    mail = f'<a href="mailto:{MAIL}">{MAIL}</a>'
    end = f'<p class="gx-end">Questions about {app["name"]} or these pages? Write to {mail}. <a href="./">Back to the GamingHub home page</a>.</p>'
    kick = 'Legal' if key != 'support' else 'Help'
    return f'''<a class="gx-skip" href="#doc">Skip to the page</a>
<header class="gx-top gx-dark k-priv">
 <div class="gx-top__bg" aria-hidden="true"></div>
 {_nav(key, True)}
 <div class="gx-top__t">
  <p class="gx-kicker">{kick}</p>
  <h1>{h1html}</h1>
  <p class="meta">{meta}</p>
 </div>
</header>
<div class="gx-legal">
 {toc_d}
 <main class="gx-doc" id="doc">
  {toc_m}
  {short}
  {chr(10).join(out)}
  {end}
 </main>
</div>
{_footer()}'''


SCRIPT = '''<script>(function(){var l=document.querySelectorAll('.gx-toc--d a[href^="#"]');if(!l.length||!('IntersectionObserver' in window))return;var m={};l.forEach(function(a){m[a.getAttribute('href').slice(1)]=a});var o=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){l.forEach(function(a){a.removeAttribute('aria-current')});var a=m[e.target.id];if(a)a.setAttribute('aria-current','location')}})},{rootMargin:'-15% 0px -75% 0px'});document.querySelectorAll('.gx-doc [id]').forEach(function(h){if(m[h.id])o.observe(h)})})();</script>'''


def page(app, lang, key, title, desc, body, host, alts):
    canonical = f'{host}{app["slug"]}/' if key == 'index' else f'{host}{app["slug"]}/{key}.html'
    if key == 'index':
        inner = '<a class="gx-skip" href="#main">Skip to content</a>\n' + _home()
        pre = '<link rel="preload" as="image" href="media/plate-header.webp" type="image/webp">\n'
        cls, script = 'gx-home', ''
    else:
        inner, pre, cls, script = _legal(app, key, body, title), '', 'gx-page', SCRIPT
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="color-scheme" content="light dark">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="{LIGHT['canvas']}" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="{DARK['canvas']}" media="(prefers-color-scheme: dark)">
<link rel="icon" href="media/icon-180.png">
<link rel="apple-touch-icon" href="media/icon-180.png">
{pre}<style>{css()}</style>
</head>
<body class="{cls}">
{inner}
{script}
</body>
</html>
'''
