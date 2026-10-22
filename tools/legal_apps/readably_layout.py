"""Readably's own site for tools/gen_legal_apps.py (slug 'readably'): the home page and the privacy, terms and
support pages. Nothing here is shared with another app's pages: every class is prefixed `rd-`, the type is a
New York serif for what is read and Avenir Next for the controls, and the palette is the app's own (Paper and Night,
Palette.swift) plus the deep-spruce plates the store art uses.

Pages are stand-alone on purpose (App Review 4.3): the only links are the app's own pages, its own media under
readably/media/, mailto:hello@seizeapps.com, the vendors and regulators the legal text names, and Apple's legal pages.
No fonts, scripts or images are fetched from anywhere else.

page() builds all four pages; audit() measures every foreground/background pair the stylesheet can put on screen in
light and dark, text over a plate included (the scrim blended over the plate's brightest pixel), from the generated
page itself. gen_legal_apps.py refuses to write a page whose audit is not ok; tools/check_contrast.py prints the table.
The images live in readably/media/ and are prepared by hand (cropped store screens and the app's plates).
"""
import functools
import os
import re

MIN = 4.5
HERE = os.path.dirname(os.path.abspath(__file__))
MEDIA = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'readably', 'media')

# Paper and Night from Palette.swift, with the dark surfaces leaned a hair toward spruce so they sit with the plates.
LIGHT = dict(bg='#F5F0E6', surface='#FBF8F1', raised='#EBE4D4', fg='#1F1B16', sec='#4F483C', muted='#625B4D',
             accent='#1F6B63', onaccent='#F8F5EE', atext='#1B645C', line='#D6CCB5', tint='#DAE6D6', word='#9CCDBF')
DARK = dict(bg='#131A19', surface='#1B2423', raised='#26302F', fg='#EDE8DD', sec='#BCB6A8', muted='#A7A194',
            accent='#7CC7BA', onaccent='#0F1A18', atext='#8FD3C7', line='#34423F', tint='#22332F', word='#336B62')

# Colours that do not change with the mode: the dark spruce bands, the app's own Paper/Night halves.
CREAM, CREAM2, GOLD = '#F8F5EE', '#E6E0D2', '#E8CB8E'
SPRUCE = (7, 24, 21)
PAPER, NIGHT = '#F5F0E6', '#14161A'
PAPER_LABEL, NIGHT_LABEL = '#5A5347', '#B0AA9C'

# (name, plate, scrim alpha where the text sits): the text on each dark band is measured against the brightest
# pixel of that plate under that scrim.
BANDS = {'honest': ('header.jpg', .76), 'lock': ('lockscreen.jpg', .8), 'close': ('search.jpg', .78),
         'head': ('header.jpg', .8), 'foot': ('header.jpg', .88)}
HERO_PLATE, HERO_ALPHA = 'search.jpg', .2     # dark mode only: the plate's share over --bg behind the headline

CSS = r'''
:root{@LIGHT@;color-scheme:light dark;
--serif:"New York","Iowan Old Style",Charter,"Palatino Linotype",Georgia,serif;
--sans:"Avenir Next","Helvetica Neue",system-ui,"Segoe UI",Roboto,Arial,sans-serif;
--cream:@CREAM@;--cream2:@CREAM2@;--gold:@GOLD@;--spruce:7,24,21;--hero-plate:0}
@media (prefers-color-scheme:dark){:root{@DARK@;--hero-plate:1}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--bg);color:var(--fg);font:18px/1.6 var(--serif);-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
img{max-width:100%}
a{color:var(--atext);text-underline-offset:3px;text-decoration-thickness:1px}
a:focus-visible,summary:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
.rd-skip{position:absolute;left:12px;top:-64px;background:var(--fg);color:var(--bg);padding:10px 16px;border-radius:10px;font:600 15px var(--sans);z-index:30}
.rd-skip:focus{top:12px}

/* top bar */
.rd-bar{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--bg) 86%,transparent);backdrop-filter:saturate(1.4) blur(18px);-webkit-backdrop-filter:saturate(1.4) blur(18px);border-bottom:1px solid transparent;transition:border-color .2s}
.rd-bar.rd-scrolled{border-bottom-color:var(--line)}
.rd-bar-in{max-width:1240px;margin:0 auto;padding:12px 24px;display:flex;align-items:center;justify-content:space-between;gap:16px}
.rd-brand{display:flex;align-items:center;gap:10px;color:var(--fg);text-decoration:none;font:600 19px/1 var(--serif);letter-spacing:-.01em;border-radius:10px}
.rd-brand img{width:30px;height:30px;border-radius:22.37%;display:block;box-shadow:0 0 0 1px var(--line)}
.rd-nav{display:flex;gap:2px;font:500 15px/1 var(--sans)}
.rd-nav a{color:var(--sec);text-decoration:none;padding:11px 13px;border-radius:999px;position:relative}
.rd-nav a:hover{color:var(--fg);background:color-mix(in srgb,var(--raised) 70%,transparent)}
.rd-nav a[aria-current=page]{color:var(--fg)}
.rd-nav a[aria-current=page]::after{content:"";position:absolute;left:13px;right:13px;bottom:4px;height:2px;border-radius:2px;background:var(--accent)}

/* hero */
.rd-hero{position:relative;text-align:center;padding:clamp(52px,8vw,112px) 24px 0;margin:0 auto;isolation:isolate}
.rd-hero::before{content:"";position:absolute;left:0;right:0;top:-80px;height:min(780px,100%);z-index:-1;background:url(media/search.jpg) 50% 0/cover no-repeat;opacity:calc(var(--hero-plate)*@HERO_A@);-webkit-mask-image:linear-gradient(transparent 70px,#000 190px,#000 40%,transparent);mask-image:linear-gradient(transparent 70px,#000 190px,#000 40%,transparent);pointer-events:none}
.rd-hero-in{max-width:1240px;margin:0 auto}
.rd-eyebrow{font:600 13px/1.2 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--atext);margin:0 0 18px}
.rd-hero h1{font:500 clamp(40px,7.4vw,104px)/1.02 var(--serif);letter-spacing:-.03em;margin:0 auto;max-width:15em;text-wrap:balance}
.rd-w{padding:0 .04em;margin:0 -.04em;border-radius:.08em;background:linear-gradient(var(--word),var(--word)) 0 62%/0 .74em no-repeat;transition:background-size .16s ease-out;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.rd-w.rd-on{background-size:100% .74em}
@media (prefers-reduced-motion:reduce){.rd-w{transition:none}}
.rd-lede{font:400 clamp(19px,2vw,25px)/1.45 var(--serif);color:var(--sec);max-width:34em;margin:clamp(22px,3vw,34px) auto 0;text-wrap:balance}
.rd-cta{display:flex;flex-direction:column;align-items:center;gap:14px;margin-top:clamp(26px,3.2vw,40px)}
.rd-cta-row{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:12px 26px}
.rd-chip{display:inline-flex;align-items:center;gap:11px;padding:11px 20px 11px 16px;border-radius:999px;border:1.5px solid color-mix(in srgb,var(--fg) 34%,transparent);background:transparent;color:var(--fg);font:600 15.5px/1 var(--sans);letter-spacing:.005em;cursor:default;user-select:none}
.rd-chip svg{width:20px;height:20px;flex:none;fill:var(--accent)}
.rd-link{font:500 15.5px/1 var(--sans);color:var(--atext);text-decoration:none;border-bottom:1.5px solid color-mix(in srgb,var(--atext) 45%,transparent);padding:4px 0}
.rd-link:hover{border-bottom-color:var(--atext)}
.rd-note{font:400 14.5px/1.4 var(--sans);color:var(--sec);margin:0}

/* phones: pure cqw geometry inside a container stage, so every panel scales as one picture */
.rd-stage{container-type:inline-size;position:relative;overflow:hidden;border-radius:clamp(22px,3vw,40px);background:#0f2f2b var(--plate) center/cover no-repeat;isolation:isolate}
.rd-layer{position:absolute;inset:0;-webkit-mask-image:linear-gradient(#000 calc(100% - var(--fade,15cqw)),transparent);mask-image:linear-gradient(#000 calc(100% - var(--fade,15cqw)),transparent)}
.rd-pw{position:absolute;width:var(--w);filter:drop-shadow(0 calc(var(--w)*.06) calc(var(--w)*.08) rgba(6,18,16,.38))}
.rd-ph{--r:calc(var(--w)*.15);position:relative;padding:calc(var(--w)*.032);border-radius:var(--r);
background:linear-gradient(160deg,#3a3e45,#22252a 40%,#2b2f35);
box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.16),inset 0 0 0 calc(var(--w)*.03) #1c1e22,0 0 0 1px rgba(0,0,0,.4)}
.rd-ph::before,.rd-ph::after{content:"";position:absolute;width:calc(var(--w)*.012);background:#33373d;border-radius:2px}
.rd-ph::before{left:calc(var(--w)*-.011);top:18%;height:7%}
.rd-ph::after{right:calc(var(--w)*-.011);top:24%;height:11%}
.rd-scr{aspect-ratio:var(--ar,668/1363);background:var(--fill,#F5F0E6);border-radius:calc(var(--r) - var(--w)*.032);overflow:hidden;position:relative}
.rd-scr img{display:block;width:100%;height:100%;object-fit:cover}

.rd-hero-wrap{max-width:1240px;margin:clamp(40px,5.5vw,72px) auto 0}
.rd-hero-stage{--plate:url(media/header.jpg);aspect-ratio:1192/860}
.rd-hero-stage .rd-c{--w:32cqw;left:34%;top:5cqw;z-index:3}
.rd-hero-stage .rd-l{--w:25cqw;left:5.5%;top:34cqw;z-index:1}
.rd-hero-stage .rd-r{--w:25cqw;left:69.5%;top:34cqw;z-index:1}
.rd-hero-stage .rd-layer{--fade:7cqw}
.rd-call{position:absolute;z-index:4;display:none;align-items:center;gap:8px;padding:8px 14px 8px 10px;border-radius:999px;background:var(--surface);color:var(--fg);font:600 14px/1 var(--sans);box-shadow:0 8px 24px rgba(4,14,12,.38),0 0 0 1px rgba(0,0,0,.12);white-space:nowrap}
.rd-call::before{content:"";width:14px;height:14px;border-radius:5px;background:var(--tint);box-shadow:inset 0 0 0 1.5px color-mix(in srgb,var(--accent) 60%,transparent);flex:none}
.rd-call.rd-wd::before{background:var(--word)}
.rd-call::after{content:"";position:absolute;top:50%;height:2px;background:var(--gold);border-radius:2px;transform:translateY(-1px)}
.rd-call-l{right:67.6%;top:28.8cqw}
.rd-call-l::after{left:100%;width:calc(var(--g,0)*1px + 3.5cqw)}
.rd-call-r{left:66.4%;top:24.8cqw}
.rd-call-r::after{right:100%;width:calc(var(--g,0)*1px + 3cqw)}
@media (min-width:1100px){.rd-call{display:inline-flex}}

/* the four things it does not do */
.rd-ledger{max-width:1240px;margin:clamp(48px,7vw,96px) auto 0;padding:0 24px}
.rd-ledger ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,1fr);background:var(--surface);border:1px solid var(--line);border-radius:22px}
.rd-ledger li{padding:clamp(20px,2.6vw,34px) clamp(18px,2.2vw,30px);border-left:1px solid var(--line)}
.rd-ledger li:first-child{border-left:0}
.rd-ledger .rd-lab{font:600 12.5px/1.2 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin:0 0 10px}
.rd-ledger b{display:block;font:500 clamp(28px,3.2vw,44px)/1.05 var(--serif);letter-spacing:-.02em;margin-bottom:10px}
.rd-ledger p{margin:0;font:400 15.5px/1.45 var(--sans);color:var(--sec)}

/* feature rows */
.rd-feat{max-width:1240px;margin:0 auto;padding:clamp(72px,10vw,150px) 24px 0;display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:clamp(36px,6vw,96px);align-items:center}
.rd-feat.rd-rev{grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr)}
.rd-feat.rd-rev .rd-copy{order:2}
.rd-copy h2{font:500 clamp(34px,4.6vw,62px)/1.04 var(--serif);letter-spacing:-.025em;margin:0 0 .5em;text-wrap:balance}
.rd-copy>p:not(.rd-eyebrow){margin:0 0 1em;font:400 clamp(18px,1.5vw,21px)/1.55 var(--serif);color:var(--sec);max-width:30em}
.rd-facts{list-style:none;margin:28px 0 0;padding:0;font:400 16px/1.5 var(--sans);color:var(--fg);max-width:32em}
.rd-facts li{padding:14px 0;border-top:1px solid var(--line);display:flex;gap:18px}
.rd-facts li:last-child{border-bottom:1px solid var(--line)}
.rd-facts b{font:600 16px/1.5 var(--serif);flex:none;width:9em;color:var(--fg)}
.rd-facts span{color:var(--sec)}
.rd-chips{display:flex;flex-wrap:wrap;gap:8px;margin:22px 0 0;padding:0;list-style:none;font:500 15px/1 var(--sans)}
.rd-chips li{padding:10px 16px;border-radius:999px;background:var(--surface);border:1px solid var(--line);color:var(--fg)}

.rd-panel{aspect-ratio:10/10.4;--plate:url(media/follow.jpg)}
.rd-panel .rd-c1{--w:52cqw;left:24%;top:11cqw}
.rd-p-offline{--plate:url(media/offline.jpg);aspect-ratio:10/8.8}
.rd-p-offline .rd-c1{--w:58cqw;left:21%;top:10cqw}
.rd-p-pdf{--plate:url(media/library.jpg)}
.rd-p-pro{--plate:url(media/pro.jpg);aspect-ratio:10/9.6}
.rd-p-pro .rd-c1{--w:66cqw;left:17%;top:10cqw}
@media (min-width:961px){.rd-p-pro{aspect-ratio:10/11.4;align-self:center}
.rd-p-pro .rd-c1{--w:78cqw;left:11%;top:11cqw}}
.rd-p-offline,.rd-p-pdf,.rd-p-pro{box-shadow:0 0 0 1px var(--line)}
@media (prefers-color-scheme:dark){
.rd-p-offline{--plate:url(media/search.jpg)}
.rd-p-pdf{--plate:url(media/header.jpg)}
.rd-p-pro{--plate:url(media/night.jpg)}}

/* read along: the reading view, drawn in CSS from the app's own text */
.rd-read{--plate:url(media/follow.jpg);aspect-ratio:10/9.6;display:grid;place-items:center;padding:clamp(24px,5vw,56px)}
.rd-card{width:100%;max-width:540px;background:var(--surface);color:var(--fg);border-radius:22px;padding:clamp(20px,4.5cqw,34px);box-shadow:0 30px 60px -20px rgba(4,14,12,.55),0 0 0 1px rgba(0,0,0,.08)}
.rd-card-t{display:flex;justify-content:space-between;gap:12px;font:600 14px/1 var(--sans);color:var(--sec);padding-bottom:16px;margin-bottom:6px;border-bottom:1px solid var(--line)}
.rd-card p{margin:0;font:400 clamp(17px,3.4cqw,22px)/1.7 var(--serif)}
.rd-s{background:var(--tint);padding:.12em .22em;border-radius:.3em;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.rd-sw{background:var(--word);padding:.06em .1em;border-radius:.22em}
.rd-key{display:flex;flex-wrap:wrap;gap:8px 22px;margin:22px 0 0;padding:16px 0 0;border-top:1px solid var(--line);font:500 13px/1 var(--sans);letter-spacing:.1em;text-transform:uppercase;color:var(--sec)}
.rd-key span{display:inline-flex;align-items:center;gap:9px}
.rd-key span::before{content:"";width:22px;height:12px;border-radius:4px;background:var(--tint);box-shadow:inset 0 0 0 1.5px color-mix(in srgb,var(--accent) 55%,transparent)}
.rd-key span.rd-kw::before{background:var(--word)}
.rd-rail{margin-top:20px}
.rd-rail div{position:relative;height:6px;border-radius:6px;background:var(--raised);box-shadow:inset 0 0 0 1px var(--line)}
.rd-rail div::before{content:"";position:absolute;left:0;top:0;bottom:0;width:20%;border-radius:6px;background:var(--accent)}
.rd-rail div::after{content:"";position:absolute;left:20%;top:50%;width:20px;height:20px;margin:-10px 0 0 -10px;border-radius:50%;background:var(--accent);box-shadow:0 0 0 4px var(--surface)}
.rd-rail ol{display:flex;justify-content:space-between;list-style:none;margin:14px 0 0;padding:0;font:500 13px/1 var(--sans);color:var(--sec)}

/* pdf rows */
.rd-copy>p.rd-ill,.rd-card p.rd-ill,.rd-ill{margin:14px 0 0;max-width:none;font:500 13px/1.4 var(--sans);letter-spacing:.04em;color:var(--sec)}
.rd-ill-c{max-width:1240px;margin:22px auto 0;padding:0 24px;text-align:center}
.rd-rows{list-style:none;margin:28px 0 0;padding:0;display:grid;gap:10px;max-width:32em}
.rd-rows li{display:grid;grid-template-columns:5.6em 1fr;gap:14px;align-items:center;padding:14px 18px;border-radius:16px;background:var(--surface);border:1px solid var(--line)}
.rd-rows em{font:600 12px/1 var(--sans);font-style:normal;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.rd-rows div{font:400 16px/1.4 var(--serif)}
.rd-rows s{color:var(--muted);text-decoration-thickness:1.5px}
.rd-rows small{display:block;font:400 15px/1.4 var(--sans);color:var(--sec);margin-top:4px}
.rd-rows mark{background:var(--word);color:var(--fg);border-radius:.2em;padding:0 .2em}

/* library and lock screen: a dark band with the lock-screen plate */
.rd-lock{margin-top:clamp(72px,10vw,150px);background:rgb(var(--spruce)) url(media/lockscreen.jpg) center 30%/cover no-repeat;position:relative;isolation:isolate;overflow:hidden}
.rd-lock::before{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,rgba(var(--spruce),@LOCK_A@),rgba(var(--spruce),@LOCK_A@) 46%,rgba(var(--spruce),.3))}
.rd-lock-in{max-width:1240px;margin:0 auto;padding:clamp(60px,8vw,110px) 24px 0;display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:clamp(24px,5vw,80px);align-items:stretch}
.rd-lock .rd-copy{padding-bottom:clamp(48px,7vw,100px);align-self:center}
.rd-lock .rd-eyebrow{color:var(--gold)}
.rd-lock .rd-copy h2{color:var(--cream)}
.rd-lock .rd-copy>p:not(.rd-eyebrow){color:var(--cream2)}
.rd-lock .rd-facts{color:var(--cream)}
.rd-lock .rd-facts li{border-color:rgba(248,245,238,.28)}
.rd-lock .rd-facts b{color:var(--cream)}
.rd-lock .rd-facts span{color:var(--cream2)}
.rd-lock-vis{position:relative;container-type:inline-size;aspect-ratio:10/9.2;min-height:340px}
.rd-lock-vis .rd-layer{--fade:12cqw}
.rd-lock-vis .rd-b{--w:46cqw;left:3%;top:15cqw}
.rd-lock-vis .rd-f{--w:50cqw;left:45%;top:2cqw;z-index:2}

/* day and night */
.rd-twin-head{max-width:1240px;margin:0 auto;padding:clamp(80px,11vw,160px) 24px 0;text-align:center}
.rd-twin-head h2{font:500 clamp(34px,5.4vw,76px)/1.03 var(--serif);letter-spacing:-.028em;margin:0 auto .4em;max-width:14em;text-wrap:balance}
.rd-twin-head p:not(.rd-eyebrow){font:400 clamp(18px,1.7vw,22px)/1.55 var(--serif);color:var(--sec);max-width:36em;margin:0 auto}
.rd-twin-head .rd-eyebrow{margin-bottom:18px}
.rd-twin-wrap{max-width:1240px;margin:clamp(34px,5vw,60px) auto 0;padding:0 24px}
.rd-twin{aspect-ratio:1192/720;background:linear-gradient(90deg,@PAPER@ 50%,@NIGHT@ 50%);box-shadow:0 0 0 1px color-mix(in srgb,var(--fg) 22%,transparent)}
.rd-twin .rd-layer{--fade:11cqw}
.rd-twin .rd-pa{--w:28cqw;left:11%;top:9cqw}
.rd-twin .rd-pb{--w:28cqw;left:61%;top:9cqw}
.rd-tag{position:absolute;top:3.4cqw;font:600 13px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase;transform:translateX(-50%);z-index:2}
.rd-tag-a{left:25%;color:@PAPER_LABEL@}
.rd-tag-b{left:75%;color:@NIGHT_LABEL@}
.rd-specs{max-width:1240px;margin:clamp(28px,4vw,48px) auto 0;padding:0 24px;display:grid;grid-template-columns:repeat(4,1fr);gap:clamp(16px,2.6vw,36px)}
.rd-specs>div{border-top:1px solid var(--line);padding-top:16px;font:400 15.5px/1.45 var(--sans);color:var(--sec)}
.rd-specs h3{font:600 12.5px/1.2 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin:0 0 14px}
.rd-seg{display:inline-flex;padding:3px;border-radius:12px;background:var(--raised);font:500 14.5px/1 var(--sans);margin-bottom:12px;cursor:default;user-select:none}
.rd-seg span{padding:9px 14px;border-radius:9px;color:var(--sec)}
.rd-seg span.rd-sel{background:var(--surface);color:var(--fg);box-shadow:0 1px 3px rgba(0,0,0,.18)}
.rd-aa{display:flex;align-items:baseline;gap:18px;margin-bottom:12px;font-family:var(--serif);color:var(--fg);line-height:1}
.rd-aa span:nth-child(1){font-size:15px}.rd-aa span:nth-child(2){font-size:19px}.rd-aa span:nth-child(3){font-size:24px}.rd-aa span:nth-child(4){font-size:30px}
.rd-big{display:block;font:500 clamp(28px,2.6vw,38px)/1.1 var(--serif);letter-spacing:-.015em;color:var(--fg);margin-bottom:12px}

/* the honest part */
.rd-honest{margin-top:clamp(88px,12vw,170px);background:rgb(var(--spruce)) url(media/header.jpg) center/cover no-repeat;position:relative;isolation:isolate;color:var(--cream)}
.rd-honest::before{content:"";position:absolute;inset:0;z-index:-1;background:rgba(var(--spruce),@HONEST_A@)}
.rd-honest-in{max-width:1240px;margin:0 auto;padding:clamp(64px,9vw,128px) 24px clamp(56px,8vw,112px)}
.rd-honest .rd-eyebrow{color:var(--gold)}
.rd-honest h2{font:500 clamp(36px,6vw,84px)/1.04 var(--serif);letter-spacing:-.028em;margin:0;max-width:14em;text-wrap:balance;color:var(--cream)}
.rd-honest h2 em{display:block;color:var(--gold);font-style:italic;font-weight:400;margin-top:.12em}
.rd-honest .rd-cols{margin-top:clamp(40px,6vw,80px);display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(24px,4vw,64px);border-top:1px solid rgba(232,203,142,.5);padding-top:clamp(24px,3vw,36px)}
.rd-honest h3{font:600 20px/1.25 var(--serif);margin:0 0 12px;color:var(--cream)}
.rd-honest p{margin:0;font:400 16.5px/1.6 var(--sans);color:var(--cream2)}
.rd-honest p+p{margin-top:.8em}

/* pro */
.rd-copy>p.rd-buy{margin-top:26px;padding:20px 22px;border-radius:18px;background:var(--surface);border:1px solid var(--line);font:400 15.5px/1.55 var(--sans);color:var(--sec);max-width:34em}
.rd-buy b{color:var(--fg);font-weight:600}

/* close */
.rd-close-wrap{max-width:1240px;margin:clamp(88px,12vw,170px) auto 0;padding:0 24px}
.rd-close{position:relative;overflow:hidden;border-radius:clamp(22px,3vw,40px);background:rgb(var(--spruce)) url(media/search.jpg) center/cover;text-align:center;padding:clamp(56px,9vw,120px) 24px;isolation:isolate}
.rd-close::before{content:"";position:absolute;inset:0;background:rgba(var(--spruce),@CLOSE_A@);z-index:-1}
.rd-close img{width:92px;height:92px;border-radius:22.37%;box-shadow:0 18px 40px rgba(0,0,0,.4),0 0 0 1px rgba(255,255,255,.14)}
.rd-close h2{font:500 clamp(32px,4.8vw,64px)/1.05 var(--serif);letter-spacing:-.025em;color:var(--cream);margin:26px auto 0;max-width:14em;text-wrap:balance}
.rd-close p{margin:16px auto 0;font:400 clamp(17px,1.5vw,20px)/1.5 var(--serif);color:var(--cream2);max-width:30em}
.rd-close .rd-cta{margin-top:28px}
.rd-close .rd-chip{color:var(--cream);border-color:rgba(248,245,238,.55)}
.rd-close .rd-chip svg{fill:var(--cream)}
.rd-close .rd-link{color:var(--cream);border-bottom-color:rgba(248,245,238,.5)}
.rd-close .rd-note{color:var(--cream2)}
.rd-close a:focus-visible,.rd-honest a:focus-visible,.rd-lock a:focus-visible,.rd-foot a:focus-visible,.rd-lhead a:focus-visible{outline-color:var(--gold)}

/* footer */
.rd-foot{margin-top:clamp(64px,9vw,120px);background:rgb(var(--spruce)) url(media/header.jpg) center/cover;position:relative;isolation:isolate;color:var(--cream2)}
.rd-foot::before{content:"";position:absolute;inset:0;z-index:-1;background:rgba(var(--spruce),@FOOT_A@)}
.rd-foot-in{max-width:1240px;margin:0 auto;padding:clamp(40px,5vw,64px) 24px 44px;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:28px 48px;align-items:start;font:400 14.5px/1.6 var(--sans)}
.rd-foot-brand{display:flex;align-items:center;gap:14px;color:var(--cream);text-decoration:none;font:500 clamp(20px,2vw,26px)/1.2 var(--serif);letter-spacing:-.01em}
.rd-foot-brand img{width:44px;height:44px;border-radius:22.37%;flex:none;box-shadow:0 0 0 1px rgba(255,255,255,.18)}
.rd-foot nav{display:flex;flex-wrap:wrap;gap:6px 24px;justify-content:flex-end}
.rd-foot nav a{color:var(--cream);text-decoration:none;padding:6px 0}
.rd-foot nav a:hover{text-decoration:underline}
.rd-foot-colo{grid-column:1/-1;margin:0;border-top:1px solid rgba(248,245,238,.22);padding-top:20px;display:flex;flex-wrap:wrap;gap:4px 28px;justify-content:space-between}
.rd-foot-colo span{max-width:40em}

/* legal pages */
.rd-lhead-wrap{max-width:1160px;margin:clamp(16px,2.4vw,28px) auto 0;padding:0 24px}
.rd-lhead{position:relative;overflow:hidden;border-radius:clamp(22px,3vw,36px);background:rgb(var(--spruce)) url(media/header.jpg) center/cover;padding:clamp(28px,4vw,52px) clamp(24px,5vw,64px) clamp(32px,5vw,60px);isolation:isolate}
.rd-lhead::before{content:"";position:absolute;inset:0;background:rgba(var(--spruce),@HEAD_A@);z-index:-1}
.rd-back{display:inline-flex;gap:8px;align-items:center;font:500 15px/1 var(--sans);text-decoration:none;color:var(--gold);margin-bottom:clamp(28px,5vw,64px);padding:8px 0}
.rd-back:hover{text-decoration:underline}
.rd-lhead h1{font:500 clamp(40px,5.8vw,72px)/1.03 var(--serif);letter-spacing:-.028em;margin:0 0 12px;color:var(--cream)}
.rd-updated{font:400 16px/1.4 var(--sans);color:var(--cream2);margin:0}
.rd-doc{max-width:1160px;margin:0 auto;padding:clamp(28px,4vw,52px) 24px 0;display:grid;grid-template-columns:230px minmax(0,1fr);gap:0 clamp(32px,6vw,88px);align-items:start}
.rd-short{grid-column:2;grid-row:1;max-width:68ch;margin:0 0 clamp(28px,4vw,44px);padding:24px 28px;border-radius:20px;background:var(--surface);border:1px solid var(--line);box-shadow:0 18px 40px -22px rgba(31,27,22,.4);font:400 19px/1.6 var(--serif)}
.rd-short h2{font:600 12.5px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--atext);margin:0 0 12px}
.rd-short p{margin:0}
.rd-toc{grid-column:1;grid-row:1/span 3;position:sticky;top:84px;font:400 15px/1.4 var(--sans)}
.rd-toc summary{list-style:none;font:600 12px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--muted);padding:6px 0 14px;cursor:default}
.rd-toc summary::-webkit-details-marker{display:none}
.rd-toc ol{list-style:none;margin:0;padding:0;border-left:1px solid var(--line)}
.rd-toc a{display:block;padding:7px 0 7px 16px;margin-left:-1px;border-left:2px solid transparent;color:var(--sec);text-decoration:none;border-radius:0 6px 6px 0}
.rd-toc a:hover{color:var(--fg);border-left-color:var(--accent)}
.rd-toc a[aria-current=location]{color:var(--fg);font-weight:600;border-left-color:var(--accent)}
.rd-toc ol ol{border-left:0}
.rd-toc ol ol a{padding-left:30px;font-size:14px}
.rd-body{grid-column:2;max-width:68ch;font:400 19px/1.7 var(--serif)}
.rd-body h2{font:500 clamp(26px,2.6vw,32px)/1.2 var(--serif);letter-spacing:-.015em;margin:1.7em 0 .55em;padding-top:.9em;border-top:1px solid var(--line);scroll-margin-top:84px}
.rd-body>h2:first-child{margin-top:0;border-top:0;padding-top:0}
.rd-body h3{font:600 20px/1.3 var(--serif);margin:1.8em 0 .4em;scroll-margin-top:84px}
.rd-body p{margin:0 0 1.1em}
.rd-body ul{margin:0 0 1.2em;padding-left:1.2em}
.rd-body li{margin:0 0 .8em;padding-left:.2em}
.rd-body li::marker{color:var(--atext)}
.rd-body strong{font-weight:650}
.rd-body .contact{font:500 clamp(22px,2.4vw,28px)/1.3 var(--serif)}

/* responsive */
@media (max-width:960px){
.rd-feat,.rd-feat.rd-rev,.rd-lock-in{grid-template-columns:minmax(0,1fr);gap:36px}
.rd-feat.rd-rev .rd-copy{order:0}
.rd-lock-in{gap:0}
.rd-lock-vis{max-width:560px;width:100%;margin:0 auto}
.rd-lock::before{background:rgba(var(--spruce),@LOCK_A@)}
.rd-ledger ul{grid-template-columns:repeat(2,1fr)}
.rd-ledger li:nth-child(3){border-left:0}
.rd-ledger li:nth-child(n+3){border-top:1px solid var(--line)}
.rd-honest .rd-cols{grid-template-columns:1fr}
.rd-specs{grid-template-columns:repeat(2,1fr)}
.rd-doc{grid-template-columns:minmax(0,1fr)}
.rd-short,.rd-body{grid-column:1}
.rd-toc{grid-column:1;grid-row:2;position:static;margin:0 0 28px;border:1px solid var(--line);border-radius:16px;background:var(--surface);padding:0 18px}
.rd-toc summary{padding:16px 0;cursor:pointer;display:flex;justify-content:space-between;align-items:center}
.rd-toc summary::after{content:"+";font:500 20px/1 var(--sans);letter-spacing:0}
.rd-toc[open] summary::after{content:"\2212"}
.rd-toc[open]{padding-bottom:12px}
.rd-body{grid-row:3}
.rd-foot-in{grid-template-columns:1fr}
.rd-foot nav{justify-content:flex-start}
}
@media (max-width:700px){
.rd-honest::before{background:rgba(var(--spruce),.92)}
.rd-lock::before{background:rgba(var(--spruce),.9)}
.rd-panel{aspect-ratio:10/10.2}
.rd-panel .rd-c1{--w:60cqw;left:20%;top:9cqw}
.rd-p-offline{aspect-ratio:10/9.4}
.rd-p-offline .rd-c1{--w:66cqw;left:17%;top:9cqw}
.rd-p-pro{aspect-ratio:10/8.4}
.rd-p-pro .rd-c1{--w:76cqw;left:12%;top:9cqw}
.rd-hero-stage{aspect-ratio:1/1.5}
.rd-hero-stage .rd-c{--w:70cqw;left:15%;top:7cqw}
.rd-hero-stage .rd-l,.rd-hero-stage .rd-r{display:none}
.rd-hero-stage .rd-layer{--fade:18cqw}
.rd-twin{aspect-ratio:1/.92}
.rd-twin .rd-pa{--w:40cqw;left:8%;top:14cqw}
.rd-twin .rd-pb{--w:40cqw;left:52%;top:14cqw}
.rd-twin .rd-layer{--fade:16cqw}
.rd-tag{top:5cqw}
}
@media (max-width:560px){
body{font-size:17px}
.rd-bar-in{padding:10px 14px}
.rd-nav a{padding:11px 9px}
.rd-nav a[aria-current=page]::after{left:9px;right:9px}
.rd-brand{font-size:18px}
.rd-hero,.rd-feat,.rd-ledger,.rd-twin-wrap,.rd-twin-head,.rd-specs,.rd-close-wrap,.rd-doc,.rd-lhead-wrap,.rd-lock-in,.rd-honest-in,.rd-foot-in{padding-left:16px;padding-right:16px}
.rd-ledger ul{grid-template-columns:1fr 1fr}
.rd-ledger li{padding:18px 16px}
.rd-ledger p{font-size:15px}
.rd-facts li{flex-direction:column;gap:2px}
.rd-facts b{width:auto}
.rd-rows li{grid-template-columns:1fr;gap:8px}
.rd-specs{grid-template-columns:1fr}
.rd-call-l,.rd-call-r{display:none}
.rd-short{padding:20px 20px;font-size:17.5px}
.rd-body{font-size:17.5px}
.rd-lhead{padding-left:20px;padding-right:20px}
.rd-cta-row{flex-direction:column;gap:14px}
}
'''

ICON = ('<svg viewBox="0 0 22 22" aria-hidden="true" focusable="false"><rect x="0.5" y="8.5" width="2" height="5" rx="1"/>'
        '<rect x="3.7" y="5.5" width="2" height="11" rx="1"/><rect x="6.9" y="7" width="2" height="8" rx="1"/>'
        '<rect x="10.1" y="2" width="2" height="18" rx="1"/><rect x="13.3" y="4.5" width="2" height="13" rx="1"/>'
        '<rect x="16.5" y="7.5" width="2" height="7" rx="1"/><rect x="19.7" y="9" width="2" height="4" rx="1"/></svg>')

# ---------------------------------------------------------------- contrast audit


def _lum(h):
    h = h.lstrip('#')
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]


def _ratio(a, b):
    la, lb = _lum(a), _lum(b)
    if la < lb:
        la, lb = lb, la
    return (la + .05) / (lb + .05)


def _hex(c):
    return '#%02X%02X%02X' % tuple(round(v) for v in c)


def _rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


@functools.lru_cache(maxsize=None)
def _brightest(plate):
    """The plate's brightest pixel (by luminance), on a 1/4 grid: the worst case behind any text over it."""
    try:
        from PIL import Image
    except ImportError:
        raise SystemExit('readably_layout.audit needs Pillow to measure text over the plates: pip install pillow')
    im = Image.open(os.path.join(MEDIA, plate)).convert('RGB')
    im = im.resize((max(1, im.width // 4), max(1, im.height // 4)))
    return max(im.getdata(), key=lambda p: _lum(_hex(p)))


def _over(plate, alpha, base=SPRUCE):
    px = _brightest(plate)
    return _hex([alpha * base[i] + (1 - alpha) * px[i] for i in range(3)])


def _vars(block):
    return dict(re.findall(r'--([a-z0-9]+):(#[0-9A-Fa-f]{6})', block))


# text colour name -> the backgrounds it is drawn on
TEXT_ON = [('fg', ('bg', 'surface', 'raised', 'tint')), ('sec', ('bg', 'surface', 'raised', 'tint')),
           ('atext', ('bg', 'surface', 'raised', 'tint')), ('muted', ('bg', 'surface', 'raised')),
           ('accent', ('bg', 'surface'))]
LABELS = dict(fg='body text', sec='secondary text', atext='link / accent text', muted='muted text', accent='focus ring / icon')
BGLAB = dict(bg='page', surface='card', raised='raised surface', tint='sentence tint')


def audit(html):
    """Every text/background pair the stylesheet can show, read from the <style> of a generated page.
    -> (rows, ok); a row is (mode, label, fg, bg, ratio)."""
    style = re.search(r'<style>(.*?)</style>', html, re.S).group(1)
    light = _vars(re.search(r':root\{([^}]*)\}', style).group(1))
    dark = dict(light, **_vars(re.search(r'prefers-color-scheme:dark\)\{:root\{([^}]*)\}', style).group(1)))
    rows = []
    for mode, v in (('light', light), ('dark', dark)):
        for fg, bgs in TEXT_ON:
            for bg in bgs:
                rows.append((mode, f'{LABELS[fg]} on {BGLAB[bg]}', v[fg], v[bg], _ratio(v[fg], v[bg])))
        rows.append((mode, 'spoken word on highlight', v['fg'], v['word'], _ratio(v['fg'], v['word'])))
        rows.append((mode, 'label on accent', v['onaccent'], v['accent'], _ratio(v['onaccent'], v['accent'])))
    # dark mode: the headline sits on the plate that is blended over the page colour
    hero = _over(HERO_PLATE, 1 - HERO_ALPHA, base=_rgb(dark['bg']))
    for fg in ('fg', 'sec', 'atext'):
        rows.append(('dark', f'{LABELS[fg]} on hero plate (worst case)', dark[fg], hero, _ratio(dark[fg], hero)))
    # dark bands, the same in both modes: cream, cream2 and gold on the scrim over the brightest plate pixel
    for name, (plate, a) in BANDS.items():
        bg = _over(plate, a)
        for label, fg in (('cream', CREAM), ('light cream', CREAM2), ('gold', GOLD)):
            for mode in ('light', 'dark'):
                rows.append((mode, f'{label} text on {name} band (worst case)', fg, bg, _ratio(fg, bg)))
    for mode in ('light', 'dark'):
        rows.append((mode, 'Paper label on the Paper half', PAPER_LABEL, PAPER, _ratio(PAPER_LABEL, PAPER)))
        rows.append((mode, 'Night label on the Night half', NIGHT_LABEL, NIGHT, _ratio(NIGHT_LABEL, NIGHT)))
    return rows, all(r[4] >= MIN for r in rows)


# ---------------------------------------------------------------- shared chrome


def css():
    f = lambda d: ';'.join(f'--{k}:{v}' for k, v in d.items())
    out = CSS.replace('@LIGHT@', f(LIGHT)).replace('@DARK@', f(DARK))
    for k, v in dict(CREAM=CREAM, CREAM2=CREAM2, GOLD=GOLD, PAPER=PAPER, NIGHT=NIGHT, PAPER_LABEL=PAPER_LABEL,
                     NIGHT_LABEL=NIGHT_LABEL, HERO_A=str(HERO_ALPHA), HONEST_A=str(BANDS['honest'][1]),
                     LOCK_A=str(BANDS['lock'][1]), CLOSE_A=str(BANDS['close'][1]), HEAD_A=str(BANDS['head'][1]),
                     FOOT_A=str(BANDS['foot'][1])).items():
        out = out.replace(f'@{k}@', v)
    return out


NAV = (('privacy', 'Privacy', 'privacy.html'), ('terms', 'Terms', 'terms.html'), ('support', 'Support', 'support.html'))
MAIL = 'hello@seizeapps.com'


def bar(cur):
    links = ''.join(f'<a href="{h}"{" aria-current=page" if k == cur else ""}>{t}</a>' for k, t, h in NAV)
    return ('<header class="rd-bar" id="bar"><div class="rd-bar-in"><a class="rd-brand" href="./" aria-label="Readably home">'
            '<img src="media/readably-icon-180.png" width="30" height="30" alt="">Readably</a>'
            f'<nav class="rd-nav" aria-label="Readably">{links}</nav></div></header>')


FOOT = ('<footer class="rd-foot"><div class="rd-foot-in">'
        '<a class="rd-foot-brand" href="./"><img src="media/readably-icon-180.png" width="44" height="44" alt="">'
        'Text to speech that stays on your iPhone.</a>'
        '<nav aria-label="Footer"><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a>'
        f'<a href="support.html">Support</a><a href="mailto:{MAIL}">{MAIL}</a></nav>'
        '<p class="rd-foot-colo"><span>Readably 0.1.0. Speech by Kokoro-82M (Apache 2.0) and Apple&rsquo;s voices.</span>'
        '<span>For iPhone, iOS 17 or later.</span></p></div></footer>')

SCRIPT = '''<script>
(function(){
var bar=document.getElementById('bar');
function s(){bar.classList.toggle('rd-scrolled',window.scrollY>8)}
s();addEventListener('scroll',s,{passive:true});
var ws=[].slice.call(document.querySelectorAll('.rd-w'));
if(ws.length&&!matchMedia('(prefers-reduced-motion:reduce)').matches)setTimeout(function(){
var last=ws.length-1,i=0;ws.forEach(function(w){w.classList.remove('rd-on')});ws[0].classList.add('rd-on');
var t=setInterval(function(){ws[i].classList.remove('rd-on');i++;ws[i].classList.add('rd-on');if(i===last)clearInterval(t)},150)},1400);
var d=document.querySelector('.rd-toc');
if(d){var mq=matchMedia('(min-width:961px)');
function sync(){d.open=mq.matches?true:d.hasAttribute('data-user')}
sync();mq.addEventListener('change',sync);
d.addEventListener('toggle',function(){if(mq.matches&&!d.open)d.open=true;else if(!mq.matches)d.setAttribute('data-user','')});
var links=[].slice.call(d.querySelectorAll('a')),hs=links.map(function(a){return document.getElementById(a.hash.slice(1))});
if('IntersectionObserver' in window){var cur=null;var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){cur=e.target}});
if(cur){links.forEach(function(a,k){if(hs[k]===cur)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current')})}},{rootMargin:'-84px 0px -70% 0px'});
hs.forEach(function(h){if(h)io.observe(h)})}}
})();
</script>'''


def shell(title, desc, canonical, cur, main, home):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
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
<meta property="og:image" content="https://seizeapps.com/readably/media/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Readably: text to speech that stays on your iPhone.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://seizeapps.com/readably/media/og.jpg">
<link rel="icon" href="media/readably-icon-180.png">
<link rel="apple-touch-icon" href="media/readably-icon-180.png">
<style>{css()}</style>
</head>
<body>
<a class="rd-skip" href="#main">Skip to content</a>
{bar(cur)}
<main id="main">
{main}
</main>
{FOOT}
{SCRIPT}
</body>
</html>
'''


# ---------------------------------------------------------------- home


def phone(src, alt, ar='668/1363', w=668, h=1363, cls='', eager=False, fill=None, extra=''):
    st = f' style="--ar:{ar}' + (f';--fill:{fill}' if fill else '') + '"'
    ld = '' if eager else ' loading="lazy"'
    return (f'<div class="rd-pw {cls}"{extra}><div class="rd-ph"><div class="rd-scr"{st}>'
            f'<img src="media/{src}" width="{w}" height="{h}" alt="{alt}"{ld} decoding="async"></div></div></div>')


def layer(*phones):
    return '<div class="rd-layer">' + ''.join(phones) + '</div>'


HERO_WORDS = ['Text', 'to', 'speech', 'that', 'stays', 'on', 'your', 'iPhone']


def h1():
    out = []
    for i, w in enumerate(HERO_WORDS):
        on = ' rd-on' if i == len(HERO_WORDS) - 1 else ''
        out.append(f'<span class="rd-w{on}">{w}</span>' + ('.' if i == len(HERO_WORDS) - 1 else ''))
    return ' '.join(out)


def status(extra=''):
    return (f'<span class="rd-chip" role="note" aria-disabled="true">{ICON}Coming soon to the App Store</span>')


def cta(light=False):
    return (f'<div class="rd-cta"><div class="rd-cta-row">{status()}<a class="rd-link" href="privacy.html">Read the privacy policy</a></div>'
            '<p class="rd-note">iPhone, iOS 17 or later</p></div>')


def home():
    hero = f'''
<section class="rd-hero" aria-labelledby="t"><div class="rd-hero-in">
<p class="rd-eyebrow">Readably for iPhone</p>
<h1 id="t">{h1()}</h1>
<p class="rd-lede">Natural voices that run on your iPhone. Private, offline after one download, no account. Paste text or open a PDF and just listen.</p>
{cta()}
<div class="rd-hero-wrap"><div class="rd-stage rd-hero-stage">
{layer(
    phone('03-library.webp', 'The Readably library: five documents, each with how far you got.', cls='rd-l', eager=True),
    phone('06-night.webp', 'The reading view in Night: the same page, with the spoken word highlighted in spruce.', cls='rd-r', eager=True),
    phone('01-follow.webp', 'The reading view: the sentence being read is tinted and the spoken word is highlighted.', cls='rd-c', eager=True))}
<span class="rd-call rd-call-l rd-wd" style="--g:12">Spoken word</span>
<span class="rd-call rd-call-r" style="--g:12">Sentence</span>
</div></div>
</div></section>

<section class="rd-ledger" aria-label="What Readably does not do">
<ul>
<li><p class="rd-lab">Account</p><b>None</b><p>Open it and listen.</p></li>
<li><p class="rd-lab">Ads</p><b>None</b><p>No advertising, no tracking.</p></li>
<li><p class="rd-lab">Listening meter</p><b>None</b><p>Listening is unlimited.</p></li>
<li><p class="rd-lab">Your text</p><b>Stays here</b><p>It never leaves your iPhone.</p></li>
</ul>
</section>

<section class="rd-feat" aria-labelledby="f1">
<div class="rd-copy">
<p class="rd-eyebrow">Read along</p>
<h2 id="f1">Hear it. Follow every word.</h2>
<p>The sentence and the word being spoken stay highlighted, so your eyes and your ears move together. The reading view is calm, set in a serif typeface, and large type is the default.</p>
<ul class="rd-facts">
<li><b>Tap to start</b><span>Tap any sentence to begin from there, or jump a sentence back or forward with one tap.</span></li>
<li><b>Speed</b><span>From 0.5&times; to 3&times;, changed while it plays.</span></li>
<li><b>Preview</b><span>Hear a voice read the same sentence before you choose it. Readably detects the language of your text and picks a voice to match.</span></li>
</ul>
</div>
<div class="rd-stage rd-read" role="img" aria-label="The reading view: a tinted sentence, the spoken word marked inside it, and the 0.5 to 3 times speed control.">
<div class="rd-card" aria-hidden="true">
<div class="rd-card-t"><span>Pride and Prejudice</span><span>Heart &middot; 1.0&times;</span></div>
<p>It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife. <span class="rd-s">However little known the feelings or views of such a man may be on his first entering a <span class="rd-sw">neighbourhood,</span> this truth is so well fixed in the minds of the surrounding families.</span></p>
<div class="rd-key"><span>Sentence</span><span class="rd-kw">Spoken word</span></div>
<div class="rd-rail"><div></div><ol><li>0.5&times;</li><li>1&times;</li><li>2&times;</li><li>3&times;</li></ol></div>
<p class="rd-ill">Illustration, not a screenshot.</p>
</div>
</div>
</section>

<section class="rd-feat rd-rev" aria-labelledby="f2">
<div class="rd-copy">
<p class="rd-eyebrow">On-device voices</p>
<h2 id="f2">Natural voices, in your pocket.</h2>
<p>Voices in English, Spanish and French run on the iPhone itself. Download them once from inside the app and they keep working offline. Apple&rsquo;s built-in voices are there from the first launch, for every language your iPhone has a voice for.</p>
<ul class="rd-chips" aria-label="Languages with downloadable voices"><li>English</li><li>Espa&ntilde;ol</li><li>Fran&ccedil;ais</li></ul>
<ul class="rd-facts">
<li><b>One download</b><span>About 127 MB for English; Spanish and French are separate downloads. You start it, and you can delete the voices in Settings at any time.</span></li>
<li><b>Offline</b><span>After that, no connection is needed to listen.</span></li>
</ul>
</div>
<div class="rd-stage rd-panel rd-p-offline">
{layer(phone('05-offline.webp', 'Settings, On-device voices: English, Espa&ntilde;ol and Fran&ccedil;ais tabs, the voices ready, and the storage they use on this iPhone.', ar='668/911', h=911, cls='rd-c1', fill='#F6F1E7'))}
</div>
</section>

<section class="rd-feat" aria-labelledby="f3">
<div class="rd-copy">
<p class="rd-eyebrow">PDFs and text</p>
<h2 id="f3">PDFs, read the way you would.</h2>
<p>Paste text, or open a PDF or a text file. Readably cleans the page as it imports it, so it sounds like a person reading.</p>
<ul class="rd-rows">
<li><em>Skipped</em><div><s>12</s><small>Page numbers</small></div></li>
<li><em>Skipped</em><div><s>Chapter 3 &middot; The Harbour</s><small>Repeated headers and footers</small></div></li>
<li><em>Joined</em><div>light- house &rarr; <mark>lighthouse</mark><small>Words split across lines</small></div></li>
</ul>
<p class="rd-ill">Illustration with sample text, not a screenshot.</p>
<ul class="rd-facts">
<li><b>Scans</b><span>Pages that are only pictures need the text scanning in Readably Pro.</span></li>
</ul>
</div>
<div class="rd-stage rd-panel rd-p-pdf">
{layer(phone('04-pdf.webp', 'The Harbour Lights, a PDF, in the reading view with a sentence and a word highlighted.', cls='rd-c1'))}
</div>
</section>

<section class="rd-lock" aria-labelledby="f4">
<div class="rd-lock-in">
<div class="rd-copy">
<p class="rd-eyebrow">Library and Lock Screen</p>
<h2 id="f4">Lock your phone. It keeps reading.</h2>
<p>Play, pause and skip from the Lock Screen. Your library keeps each document with how far you got, and opens it at the sentence you left.</p>
<ul class="rd-facts">
<li><b>Lock Screen</b><span>A Live Activity and Now Playing controls. A setting hides the text there if you would rather.</span></li>
<li><b>Library</b><span>Every document, with how far you got.</span></li>
</ul>
</div>
<div class="rd-lock-vis">
{layer(
    phone('03-library.webp', 'The Library: five documents, each with a progress bar.', cls='rd-b'),
    phone('02-lockscreen.webp', 'The Lock Screen with Now Playing controls and the sentence being read.', cls='rd-f'))}
</div>
</div>
</section>

<section aria-labelledby="f5">
<div class="rd-twin-head">
<p class="rd-eyebrow">Day and night</p>
<h2 id="f5">Easy on the eyes, day or night.</h2>
<p>Light, dark, or whatever your iPhone uses. Large type, a highlighted word and no interruptions are the defaults, and it works with VoiceOver and Dynamic Type.</p>
</div>
<div class="rd-twin-wrap">
<div class="rd-stage rd-twin">
<span class="rd-tag rd-tag-a">Paper</span><span class="rd-tag rd-tag-b">Night</span>
{layer(
    phone('04-pdf.webp', 'The reading view in the light Paper look.', cls='rd-pa'),
    phone('06-night.webp', 'The same reading view in the dark Night look.', cls='rd-pb'))}
</div>
</div>
<div class="rd-specs">
<div><h3>Appearance</h3><div class="rd-seg" role="img" aria-label="Appearance: System, Light or Dark"><span>System</span><span class="rd-sel">Light</span><span>Dark</span></div><p>Light, dark or whatever your iPhone uses.</p></div>
<div><h3>Text size</h3><div class="rd-aa" role="img" aria-label="Four text sizes"><span>Aa</span><span>Aa</span><span>Aa</span><span>Aa</span></div><p>Four sizes, and Dynamic Type.</p></div>
<div><h3>Speed</h3><span class="rd-big">0.5&times; to 3&times;</span><p>Changed while it plays.</p></div>
<div><h3>VoiceOver</h3><span class="rd-big">Supported</span><p>Readably works with VoiceOver and Dynamic Type.</p></div>
</div>
<p class="rd-ill rd-ill-c">Appearance and text size are illustrations, not screenshots.</p>
</section>

<section class="rd-honest" aria-labelledby="h1">
<div class="rd-honest-in">
<p class="rd-eyebrow">Plainly</p>
<h2 id="h1">No account. No ads. No meter. <em>Your text never leaves your iPhone.</em></h2>
<div class="rd-cols">
<div><h3>The download</h3><p>The natural voices are a one-time download you start yourself: about 127 MB for English; Spanish and French are separate downloads.</p><p>Apple&rsquo;s built-in voices need nothing.</p></div>
<div><h3>The battery</h3><p>Speaking takes real work from your iPhone, so a long session uses battery and can warm it up.</p><p>Plug in if you like, or switch to a built-in voice, which is lighter.</p></div>
<div><h3>The network</h3><p>Readably goes online for the voice download you start, for a web page you ask it to read, and for purchases. Nothing you read goes with it.</p><p>No advertising, no tracking.</p></div>
</div>
</div>
</section>

<section class="rd-feat rd-rev" aria-labelledby="f6">
<div class="rd-copy">
<p class="rd-eyebrow">Readably Pro</p>
<h2 id="f6">Tools around the text.</h2>
<p>Everything above is yours without paying. Readably Pro is one purchase, not a subscription, for the tools around the text.</p>
<ul class="rd-facts">
<li><b>Read from a link</b><span>Paste a web address and Readably reads the article without the clutter.</span></li>
<li><b>Scan text</b><span>Use the camera, or import a scanned PDF.</span></li>
<li><b>EPUB books</b><span>Open an EPUB from Files and read it chapter by chapter, with your place kept.</span></li>
<li><b>Save as audio</b><span>Turn a document into an M4A file you can play anywhere, offline.</span></li>
<li><b>Pronunciations</b><span>Teach Readably how to say names and tricky words, once, for every document.</span></li>
</ul>
<p class="rd-buy"><b>About the purchase.</b> Readably Pro is a one-time purchase, not a subscription: you pay once and keep it, and Family Sharing is on. The Readably Pro screen starts a free 30-day month, one per Apple Account. When it ends, the five tools close again and nothing is charged unless you buy; the documents you added stay in your library and keep reading. The price is shown in the app before you buy, and Restore Purchases is always in the Readably Pro screen.</p>
</div>
<div class="rd-stage rd-panel rd-p-pro">
{layer(phone('07-pro.webp', 'The Readably Pro screen listing the five tools: read from a link, scan text, EPUB books, save as audio and pronunciations.', ar='668/776', h=776, cls='rd-c1', fill='#FBF8F0'))}
</div>
</section>

<section class="rd-close-wrap" aria-labelledby="c1">
<div class="rd-close">
<img src="media/readably-icon-512.png" width="92" height="92" alt="Readably app icon: seven rounded spruce bars on cream" loading="lazy">
<h2 id="c1">Read it out loud, privately.</h2>
<p>Paste text or open a PDF, and just listen.</p>
{cta()}
</div>
</section>
'''
    return hero


# ---------------------------------------------------------------- legal pages


def _curly(html):
    """Straight quotes and apostrophes to curly ones in the text of an HTML fragment (tags and attributes untouched)."""
    out, prev = [], ' '
    for part in re.split(r'(<[^>]+>)', html):
        if part.startswith('<'):
            if re.match(r'</?(p|li|ul|ol|h[1-6]|div|br)\b', part):
                prev = ' '
            out.append(part)
            continue
        buf = []
        for ch in part:
            if ch == '"':
                ch = '“' if prev in ' \n\t([—–' else '”'
            elif ch == "'":
                ch = '‘' if prev in ' \n\t([—–' else '’'
            buf.append(ch)
            prev = ch
        out.append(''.join(buf))
    return ''.join(out)


def _mailto(html, mail):
    """Turn the plain address in the text into a mailto link (the ones already inside a link stay as they are)."""
    out, depth = [], 0
    for part in re.split(r'(<[^>]+>)', html):
        if part.startswith('<'):
            if re.match(r'<a\b', part):
                depth += 1
            elif part.startswith('</a'):
                depth -= 1
            out.append(part)
        else:
            out.append(part if depth else part.replace(mail, f'<a href="mailto:{mail}">{mail}</a>'))
    return ''.join(out)


def _slug(t, used):
    s = re.sub(r'[^a-z0-9]+', '-', re.sub(r'<[^>]+>', '', t).lower()).strip('-')[:48] or 'section'
    s = f's-{s}'
    n, base = 2, s
    while s in used:
        s = f'{base}-{n}'; n += 1
    used.add(s)
    return s


def legal(app, key, body):
    body = _mailto(_curly(body), app['email'])
    take = lambda pat, b: (lambda m: (m.group(1).strip(), b.replace(m.group(0), '', 1)) if m else ('', b))(re.search(pat, b, re.S))
    title, body = take(r'<h1>(.*?)</h1>', body)
    upd, body = take(r'<p class="updated">(.*?)</p>', body)
    short, body = take(r'<p class="summary">(.*?)</p>', body)
    used, toc, out = set(), [], []
    parts = re.split(r'(<h2>.*?</h2>)', body.strip(), flags=re.S)
    cur = None
    for part in parts:
        m = re.match(r'<h2>(.*?)</h2>', part, re.S)
        if m:
            i = _slug(m.group(1), used)
            cur = [m.group(1), i, []]
            toc.append(cur)
            out.append(f'<h2 id="{i}">{m.group(1)}</h2>')
        else:
            def h3(mm):
                j = _slug(mm.group(1), used)
                if cur is not None:
                    cur[2].append((mm.group(1), j))
                return f'<h3 id="{j}">{mm.group(1)}</h3>'
            out.append(re.sub(r'<h3>(.*?)</h3>', h3, part, flags=re.S))
    lis = ''
    for t, i, subs in toc:
        sub = ''.join(f'<li><a href="#{j}">{s}</a></li>' for s, j in subs)
        lis += f'<li><a href="#{i}">{t}</a>' + (f'<ol>{sub}</ol>' if sub else '') + '</li>'
    stamp = (f'<p class="rd-updated">{upd}</p>' if upd else '')
    box = (f'<section class="rd-short" aria-labelledby="sv"><h2 id="sv">The short version</h2><p>{short.replace("<strong>The short version:</strong>", "").strip()}</p></section>'
           if short else '')
    return f'''
<div class="rd-lhead-wrap"><header class="rd-lhead">
<a class="rd-back" href="./"><span aria-hidden="true">&larr;</span> Readably</a>
<h1>{title}</h1>
{stamp}
</header></div>
<div class="rd-doc">
{box}
<details class="rd-toc" open><summary>On this page</summary><nav aria-label="On this page"><ol>{lis}</ol></nav></details>
<article class="rd-body">
{''.join(out)}
</article>
</div>
'''


def page(app, lang, key, title, desc, body, host, alts):
    slug = app['slug']
    canonical = f'{host}{slug}/' if key == 'index' else f'{host}{slug}/{key}.html'
    main = home() if key == 'index' else legal(app, key, body)
    return shell(title, desc, canonical, key, main, key == 'index')
