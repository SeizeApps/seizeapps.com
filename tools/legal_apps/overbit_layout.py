"""Overbit's own site layout for tools/gen_legal_apps.py (slug 'overbit'): the home page and the three legal pages.
It shares no template, class name or stylesheet with another app's pages: everything is prefixed `ob-`, the type is
Helvetica Neue + the system monospace, and nothing links out of /overbit/ except the vendors and regulators the legal
text already names, Apple's legal and refund pages, and mailto:hello@seizeapps.com. No fonts, CDNs, analytics or
libraries; the only script is a few inline lines (the RSI line drawing itself, the table of contents on legal pages),
all of it inert under prefers-reduced-motion.

Identity: an instrument, not a brand surface (the app's own words). Ink #0B1114 with a green-teal cast, steel blue
for the one dominant accent, mint (oversold) and Bitcoin orange (overbought) only as signal colours, mono readouts,
hairlines. The app is dark only, so the hero and the plate stages are dark in both modes; the rest of the page
follows the system (light canvas #F4F8FA, or the app's #111A1F > #18252C surfaces).

Pages: index (home, canonical /overbit/, linked as "./"), privacy, terms, support. page() is called once per page by
build_app(); for the three legal pages the h1 / updated line / short version / h2 sections are lifted out of the text in
overbit.py (re-marked, never reworded) and the h2 list becomes the table of contents.

Contrast: audit(html) reads the <style> of a generated page and measures every text/background pair the stylesheet
can put on screen (and the graphics that carry meaning, at 3:1) in light and dark: build_app() refuses to write a page
under the minimum, and `python3 tools/gen_legal_apps.py --contrast` prints the table. Text that sits on a plate is
inside a scrim of alpha >= 0.9 (token --ob-scrim) and is measured against that scrim over pure white, the worst case
a plate pixel can be.
"""
import re

MIN = 4.5

LIGHT = dict(bg='#F4F8FA', card='#FFFFFF', raised='#EAF1F4', text='#101A1F', muted='#506069', line='#D5E0E5',
             link='#1F6F8C', accent='#1F6F8C', mint='#0E7A4E', ember='#9A5300', focus='#17627F',
             top='#FFFFFF', bot='#FFFFFF', chipline='#1F5FBF')
DARK = dict(bg='#0B1114', card='#111A1F', raised='#18252C', text='#EDF3F5', muted='#93A8B0', line='#243239',
            link='#9AD3E8', accent='#6FC1DD', mint='#3DDC97', ember='#F7931A', focus='#B9E4F2',
            top='#18252C', bot='#111A1F', chipline='#4D9BFF')
# surfaces that are the instrument's dark in both modes (hero, plate tiles, closing band, footer, legal header)
INV = dict(bg='#0B1114', card='#111A1F', raised='#18252C', text='#EDF3F5', muted='#A3B6BD', line='#26343B',
           link='#9AD3E8', accent='#6FC1DD', mint='#3DDC97', ember='#F7931A', focus='#B9E4F2', lead='#C9D8DD',
           top='#18252C', bot='#111A1F', chipline='#4D9BFF')
CONST = dict(badgebg='#EDF3F5', badgefg='#0B1114', chipbg='#0F3A66', chipfg='#EDF3F5', 
             tagbg='#6FC1DD', tagfg='#0B1114', skipbg='#EDF3F5', skipfg='#0B1114')
SCRIM = '.92'

CSS = r'''
:root{@@LIGHT@@;@@CONST@@;--ob-scrim:@@SCRIM@@;color-scheme:light dark;
  --ob-shadow:0 1px 0 rgba(16,26,31,.04),0 14px 34px -20px rgba(16,26,31,.30);--ob-lift:0 22px 44px -26px rgba(11,17,20,.55);
  --ob-sans:"Helvetica Neue","HelveticaNeue","Arial Nova","Segoe UI",Arial,sans-serif;
  --ob-mono:ui-monospace,"SF Mono",Menlo,Consolas,"Liberation Mono",monospace}
@media (prefers-color-scheme:dark){:root{@@DARK@@;--ob-shadow:none;--ob-lift:none}}
.ob-inv{@@INV@@;--ob-shadow:none;color:var(--ob-text)}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;scroll-padding-top:24px}
body{margin:0;background:var(--ob-bg);color:var(--ob-text);font:400 17px/1.55 var(--ob-sans);-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;overflow-x:clip}
img,svg{display:block;max-width:100%}
a{color:var(--ob-link);text-underline-offset:.18em;text-decoration-thickness:1px}
a:hover{text-decoration-thickness:2px}
:focus-visible{outline:2px solid var(--ob-focus);outline-offset:3px;border-radius:4px}
.ob-skip{position:absolute;left:12px;top:-64px;background:var(--ob-skipbg);color:var(--ob-skipfg);padding:12px 16px;border-radius:10px;z-index:20;font-weight:600}
.ob-skip:focus{top:12px}
.ob-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.ob-wrap{width:min(1200px,100% - 48px);margin-inline:auto}
.ob-eyebrow{font:500 12px/1.2 var(--ob-mono);letter-spacing:.14em;text-transform:uppercase;color:var(--ob-muted);margin:0}
.ob-eyebrow b{font-weight:500;color:var(--ob-accent)}
h1,h2,h3{font-family:var(--ob-sans);font-weight:600;margin:0;text-wrap:balance}

/* top bar */
.ob-top{display:flex;align-items:center;justify-content:space-between;padding:14px 0;position:relative;z-index:3}
.ob-brand{display:flex;align-items:center;gap:12px;color:var(--ob-text);text-decoration:none;font-weight:600;font-size:18px;letter-spacing:-.01em;min-height:44px}
.ob-brand img{width:32px;height:32px;border-radius:22.37%}
.ob-nav{display:flex;gap:2px}
.ob-nav a{color:var(--ob-muted);text-decoration:none;font:500 13px/1 var(--ob-mono);letter-spacing:.04em;min-height:44px;padding:0 12px;display:inline-flex;align-items:center;border-radius:8px}
.ob-nav a:hover{color:var(--ob-text);background:rgba(127,160,175,.16)}
.ob-nav a[aria-current]{color:var(--ob-text);box-shadow:inset 0 -2px 0 var(--ob-accent);border-radius:8px 8px 0 0}

/* phone: the screen runs off the bottom edge of whatever holds it */
.ob-phone{--w:300px;width:var(--w);padding:8px 8px 0;border-radius:calc((var(--w) - 16px)*.125 + 8px) calc((var(--w) - 16px)*.125 + 8px) 0 0;
  background:linear-gradient(180deg,#52666F 0%,#26343A 22%,#1A252B 100%);
  box-shadow:0 0 0 1px rgba(207,227,234,.16),0 -1px 0 rgba(255,255,255,.18) inset,0 40px 80px -30px rgba(0,0,0,.6)}
.ob-phone img{width:100%;height:auto;aspect-ratio:720/1485}

/* hero */
.ob-hero{position:relative;overflow:hidden;background:#0B1114;isolation:isolate}
.ob-hero::before{content:"";position:absolute;inset:0;z-index:-2;background:url(media/plate-header.jpg) center 40%/cover no-repeat}
.ob-hero::after{content:"";position:absolute;inset:0;z-index:-1;
  background:linear-gradient(90deg,rgba(11,17,20,.96) 0%,rgba(11,17,20,var(--ob-scrim)) 62%,rgba(11,17,20,.45) 90%,rgba(11,17,20,.6) 100%),linear-gradient(180deg,rgba(11,17,20,0) 70%,#0B1114 100%)}
.ob-hero-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,560px);gap:40px;align-items:end;min-height:680px}
.ob-hero-copy{align-self:center;padding:24px 0 112px}
.ob-glow{width:72px;height:72px;border-radius:22.37%;margin:0 0 30px;box-shadow:0 0 0 1px rgba(207,227,234,.2),0 0 28px 2px rgba(111,193,221,.32),0 0 90px 10px rgba(46,139,255,.28)}
.ob-hero h1{font-size:clamp(40px,5.4vw,70px);line-height:1;letter-spacing:-.035em;margin:20px 0 22px;max-width:11.5em}
.ob-hero h1 span{color:var(--ob-accent)}
.ob-lead{font-size:clamp(18px,1.6vw,21px);line-height:1.5;color:var(--ob-lead);max-width:33em;margin:0}
.ob-badges{display:flex;flex-wrap:wrap;gap:12px;margin-top:32px;align-items:center}
.ob-badge{display:inline-flex;align-items:center;justify-content:center;gap:10px;padding:14px 20px;border-radius:14px;background:var(--ob-badgebg);color:var(--ob-badgefg);font-weight:600;font-size:16px;line-height:1;cursor:default;user-select:none}
.ob-badge i{width:8px;height:8px;border-radius:50%;background:#0E7A4E;box-shadow:0 0 0 4px rgba(14,122,78,.2)}
.ob-chip{font:500 13px/1 var(--ob-mono);color:var(--ob-lead);border:1px solid rgba(207,227,234,.3);padding:14px 16px;border-radius:14px;letter-spacing:.02em;text-align:center}
.ob-cap{margin:22px 0 0;font:500 12.5px/1.5 var(--ob-mono);letter-spacing:.02em;color:var(--ob-muted);max-width:40em}
.ob-hero-device{--pw:340px;position:relative;display:flex;justify-content:flex-end;align-self:end}
.ob-hero-device .ob-phone{--w:var(--pw)}
.ob-float{position:absolute;right:calc(var(--pw) + 24px);bottom:210px;display:flex;gap:12px;align-items:center;padding:12px 18px 12px 12px;border-radius:18px;
  background:rgba(17,26,31,.9);-webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px);border:1px solid rgba(207,227,234,.2);box-shadow:0 24px 48px -20px rgba(0,0,0,.7);white-space:nowrap}
.ob-float em{position:absolute;top:-10px;left:14px;font:600 10px/1 var(--ob-mono);letter-spacing:.14em;text-transform:uppercase;font-style:normal;color:var(--ob-badgefg);background:var(--ob-badgebg);padding:4px 7px;border-radius:5px}
.ob-glyph{flex:none;width:36px;height:36px;border-radius:50%;display:grid;place-items:center;border:1.5px solid currentColor;color:var(--ob-mint)}
.ob-glyph svg{width:16px;height:16px}
.ob-float strong{display:block;font-weight:600;font-size:15px;line-height:1.2;color:var(--ob-text)}
.ob-float span.ob-sub{display:block;font:400 12.5px/1.3 var(--ob-mono);color:var(--ob-muted);margin-top:3px}

/* readout strip: overlaps the hero so the phone tucks under it */
.ob-spec{position:relative;z-index:2;margin-top:-56px}
.ob-strip{display:grid;grid-template-columns:repeat(4,1fr);margin:0;background:linear-gradient(180deg,var(--ob-top),var(--ob-bot));border:1px solid var(--ob-line);border-radius:24px;box-shadow:var(--ob-shadow),var(--ob-lift)}
.ob-strip>div{padding:28px 28px 26px;border-left:1px solid var(--ob-line)}
.ob-strip>div:first-child{border-left:0}
.ob-strip dt{font:500 clamp(30px,3.4vw,44px)/1 var(--ob-mono);letter-spacing:-.04em;font-variant-numeric:tabular-nums}
.ob-strip dt small{font-size:.5em;letter-spacing:0;color:var(--ob-muted);margin:0 .12em}
.ob-ice{color:var(--ob-accent)}.ob-mint{color:var(--ob-mint)}.ob-ember{color:var(--ob-ember)}
.ob-strip dd{margin:10px 0 0;color:var(--ob-muted);font-size:15px;line-height:1.4;max-width:15em}

/* bento */
.ob-section{padding:96px 0 24px}
.ob-section-head{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:24px 64px;align-items:end;margin-bottom:40px}
.ob-section-head h2{font-size:clamp(32px,4.2vw,52px);line-height:1.04;letter-spacing:-.03em;margin:16px 0 0}
.ob-section-head p{margin:0;color:var(--ob-muted);font-size:18px;max-width:30em}
.ob-bento{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));gap:16px;align-items:stretch}
.ob-tile{position:relative;overflow:hidden;border:1px solid var(--ob-line);border-radius:28px;background:linear-gradient(180deg,var(--ob-top),var(--ob-bot));box-shadow:var(--ob-shadow);padding:34px;display:flex;flex-direction:column;min-width:0;isolation:isolate}
.ob-tile.ob-inv{box-shadow:var(--ob-lift);border-color:rgba(207,227,234,.12);background:linear-gradient(180deg,#18252C,#111A1F)}
.ob-tile h3{font-size:clamp(24px,2.4vw,32px);line-height:1.1;letter-spacing:-.025em;margin:14px 0 12px}
.ob-tile>p{margin:0;color:var(--ob-muted);font-size:16.5px;max-width:30em}
.ob-vis{margin-top:auto;padding-top:26px}
.ob-tag{display:inline-flex;align-items:center;font:600 11px/1 var(--ob-mono);letter-spacing:.12em;padding:6px 8px;border-radius:6px;background:var(--ob-tagbg);color:var(--ob-tagfg);vertical-align:middle;margin-left:10px;text-transform:uppercase}
.ob-plate::before{content:"";position:absolute;inset:0;z-index:-2;background:var(--plate) var(--pos,center)/cover no-repeat}
.ob-plate::after{content:"";position:absolute;inset:0;z-index:-1;background:var(--scrim)}
.ob-t1{grid-column:span 8}
.ob-t2{grid-column:span 4;grid-row:span 2;padding-bottom:0;--plate:url(media/plate-one-alert.jpg);--pos:50% 60%;
  --scrim:linear-gradient(180deg,rgba(11,17,20,var(--ob-scrim)) 0,rgba(11,17,20,var(--ob-scrim)) 300px,rgba(11,17,20,.5) 560px,rgba(11,17,20,.35) 100%)}
.ob-t3{grid-column:span 4}
.ob-t4{grid-column:span 4}
.ob-t5{grid-column:span 5}
.ob-t6{grid-column:span 7;padding-bottom:0;flex-direction:row;gap:24px;--plate:url(media/plate-your-levels.jpg);--pos:80% 40%;
  --scrim:linear-gradient(90deg,rgba(11,17,20,.96) 0,rgba(11,17,20,var(--ob-scrim)) 62%,rgba(11,17,20,.4) 100%)}
.ob-t7{grid-column:span 12;padding-bottom:0;flex-direction:row;gap:24px;--plate:url(media/plate-pro.jpg);--pos:70% 40%;
  --scrim:linear-gradient(90deg,rgba(11,17,20,.96) 0,rgba(11,17,20,var(--ob-scrim)) 64%,rgba(11,17,20,.35) 100%)}
.ob-t8{grid-column:span 7;--plate:url(media/plate-on-chain.jpg);--pos:85% 35%;
  --scrim:linear-gradient(90deg,rgba(11,17,20,.96) 0,rgba(11,17,20,var(--ob-scrim)) 80%,rgba(11,17,20,.6) 100%)}
.ob-t9{grid-column:span 5}
.ob-tx{flex:1;min-width:0;padding-bottom:34px;display:flex;flex-direction:column}
.ob-t7 .ob-tx{justify-content:center}
.ob-shot{margin-top:auto;padding-top:28px;display:flex;justify-content:center}
.ob-t2 .ob-shot{margin-top:0;padding-top:32px;flex:1;align-items:flex-start}
.ob-t2 .ob-phone{--w:min(calc(100% + 28px),372px);margin:0 -14px}
.ob-t6 .ob-shot,.ob-t7 .ob-shot{margin-top:auto;padding-top:36px;align-self:flex-end;flex:none}
.ob-t6 .ob-phone{--w:268px}
.ob-t6 .ob-shot{height:400px;overflow:hidden}
.ob-t7 .ob-shot{height:520px;overflow:hidden}
.ob-t7 .ob-phone{--w:290px;margin-right:36px}

/* diagram */
.ob-diagram{position:relative;margin:26px 0 0}
.ob-diagram svg{width:100%;height:auto;overflow:visible}
.ob-axis,.ob-pin{position:absolute;font:500 12px/1 var(--ob-mono)}
.ob-axis{right:0;padding:4px 6px;border-radius:5px;background:var(--ob-card)}
.ob-axis.hi{color:var(--ob-ember)}.ob-axis.lo{color:var(--ob-mint)}
.ob-pin{width:22px;height:22px;margin:-11px 0 0 -11px;border-radius:50%;display:grid;place-items:center;background:var(--ob-card);border:1.5px solid currentColor;font-size:10.5px;letter-spacing:0}
.ob-pin.hi{color:var(--ob-ember)}.ob-pin.lo{color:var(--ob-mint)}.ob-pin.mid{color:var(--ob-muted)}
.ob-steps{list-style:none;margin:20px 0 0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.ob-steps li{border-top:1px solid var(--ob-line);padding-top:12px;font-size:15px;line-height:1.35;color:var(--ob-text)}
.ob-steps b{display:block;font:600 12px/1 var(--ob-mono);letter-spacing:.1em;margin-bottom:8px}
.ob-steps .hi b{color:var(--ob-ember)}.ob-steps .lo b{color:var(--ob-mint)}.ob-steps .mid b{color:var(--ob-muted)}
.ob-tile>p.ob-note,.ob-note{font:500 11.5px/1.4 var(--ob-mono);color:var(--ob-muted);letter-spacing:.08em;text-transform:uppercase;margin:16px 0 0}
.ob-line{fill:none;stroke:var(--ob-text);stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round}
.js .ob-diagram .ob-line{stroke-dasharray:1;stroke-dashoffset:0;transition:stroke-dashoffset 2.4s cubic-bezier(.45,.1,.2,1)}
.js .ob-diagram.pre .ob-line{stroke-dashoffset:1}
.js .ob-diagram .ob-dots,.js .ob-diagram .ob-pin{transition:opacity .6s ease 1.5s}
.js .ob-diagram.pre .ob-dots,.js .ob-diagram.pre .ob-pin{opacity:0}

/* gauge */
.ob-gauge{display:flex;align-items:center;gap:20px}
.ob-gauge svg{width:168px;height:auto;flex:none;overflow:visible}
.ob-gauge strong{display:block;font-size:26px;font-weight:600;letter-spacing:-.02em;line-height:1.1}
.ob-gauge span{display:block;color:var(--ob-muted);font-size:15px;line-height:1.35;margin-top:6px}

/* readout */
.ob-drag{border:1px solid var(--ob-line);border-radius:16px;background:var(--ob-raised);padding:14px 14px 0;overflow:hidden}
.ob-read{display:grid;grid-template-columns:repeat(3,auto);justify-content:start;gap:4px 22px;font:500 12px/1.2 var(--ob-mono);margin:0}
.ob-read dt{color:var(--ob-muted);letter-spacing:.1em;font-size:10.5px}
.ob-read dd{margin:0;font-size:14px;color:var(--ob-text)}
.ob-read div{display:flex;flex-direction:column;gap:5px}
.ob-drag svg{width:100%;height:auto;margin-top:6px}
.ob-ex{display:inline-block;font:600 10px/1 var(--ob-mono);letter-spacing:.14em;text-transform:uppercase;color:var(--ob-muted);border:1px solid var(--ob-line);border-radius:5px;padding:4px 6px;margin:0 0 10px}

/* timeframes */
.ob-chips{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin:0;padding:0;list-style:none}
.ob-chips li{position:relative;height:52px;border-radius:12px;display:grid;place-items:center;font:500 14px/1 var(--ob-mono);color:var(--ob-muted);background:var(--ob-raised);border:1px solid var(--ob-line)}
.ob-chips li svg{position:absolute;top:6px;right:6px;width:10px;height:10px;color:var(--ob-muted)}
.ob-chips li.on{color:var(--ob-chipfg);background:var(--ob-chipbg);border-color:var(--ob-chipline);font-weight:600;box-shadow:0 0 0 3px rgba(77,155,255,.18)}
.ob-key{display:flex;flex-wrap:wrap;gap:6px 22px;margin:16px 0 0;font:500 12.5px/1.3 var(--ob-mono);color:var(--ob-muted)}
.ob-key span{display:flex;align-items:center;gap:8px}
.ob-key svg{width:11px;height:11px}
.ob-key i{width:14px;height:14px;border-radius:4px;background:var(--ob-chipbg);border:1px solid var(--ob-chipline)}
.ob-cap2{margin:12px 0 0;font-weight:600;font-size:16px;color:var(--ob-text)}

/* facts + ledger */
.ob-facts{margin:24px 0 0;padding:0;list-style:none;font:500 13.5px/1.35 var(--ob-mono);color:var(--ob-muted)}
.ob-facts li{display:flex;gap:12px;padding:11px 0;border-top:1px solid var(--ob-line)}
.ob-facts li::before{content:"";flex:none;width:6px;height:6px;margin-top:.45em;border-radius:50%;background:var(--ob-accent)}
.ob-ledger{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:26px 0 0;max-width:36em}
.ob-ledger>div{border:1px solid var(--ob-line);border-radius:16px;padding:16px 16px 6px;background:rgba(11,17,20,.55)}
.ob-ledger h4{font:600 11px/1 var(--ob-mono);letter-spacing:.14em;text-transform:uppercase;color:var(--ob-muted);margin:0 0 12px}
.ob-ledger .pro h4{color:var(--ob-accent)}
.ob-ledger ul{list-style:none;margin:0;padding:0;font:500 13px/1.35 var(--ob-mono);color:var(--ob-text)}
.ob-ledger li{padding:9px 0;border-top:1px solid var(--ob-line)}
.ob-fine{margin:18px 0 0;font:500 12.5px/1.5 var(--ob-mono);color:var(--ob-lead);max-width:40em}
.ob-more{display:inline-flex;gap:8px;align-items:center;margin-top:auto;padding-top:22px;font-weight:600;font-size:15px;min-height:44px}

/* closing + footer */
.ob-close{position:relative;overflow:hidden;margin-top:96px;isolation:isolate;background:#0B1114;color:var(--ob-text)}
.ob-close::before{content:"";position:absolute;inset:0;z-index:-2;background:url(media/plate-search.jpg) 60% 50%/cover no-repeat}
.ob-close::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,rgba(11,17,20,.96) 0%,rgba(11,17,20,var(--ob-scrim)) 62%,rgba(11,17,20,.3) 100%)}
.ob-close .ob-wrap{padding:112px 0 104px}
.ob-close h2{font-size:clamp(34px,5vw,60px);line-height:1;letter-spacing:-.035em;margin:20px 0 20px;max-width:10em}
.ob-close p{color:var(--ob-lead);max-width:32em;margin:0 0 30px;font-size:18px}
.ob-close p.ob-eyebrow{color:var(--ob-muted);margin:0;font-size:12px}
.ob-close p.ob-langs{font:500 12.5px/1.6 var(--ob-mono);color:var(--ob-muted);max-width:44em;margin:34px 0 0}
.ob-foot{background:#0B1114;color:var(--ob-muted);border-top:1px solid rgba(207,227,234,.12);padding:44px 0 40px;font-size:14.5px}
.ob-foot-grid{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:28px 64px;align-items:start}
.ob-foot .ob-brand{margin-bottom:10px}
.ob-foot p{margin:0;max-width:34em}
.ob-foot nav{display:flex;flex-wrap:wrap;gap:0 4px;justify-content:flex-end}
.ob-foot nav a{color:var(--ob-lead);font:500 13px/1 var(--ob-mono);letter-spacing:.04em;min-height:44px;padding:0 12px;display:inline-flex;align-items:center;border-radius:8px;text-decoration:none}
.ob-foot nav a:hover{color:#fff;background:rgba(207,227,234,.1)}
.ob-print{grid-column:1/-1;border-top:1px solid rgba(207,227,234,.12);padding-top:22px;font:400 12.5px/1.55 var(--ob-mono);color:var(--ob-muted);max-width:none!important}

/* legal pages */
.ob-lhead{position:relative;isolation:isolate;overflow:hidden;border-radius:clamp(22px,3vw,34px);margin-top:16px;min-height:clamp(240px,24vw,320px);display:flex;align-items:flex-end;background:#0B1114;border:1px solid rgba(207,227,234,.14);box-shadow:var(--ob-lift)}
.ob-lhead>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:right center;z-index:-2}
.ob-lhead::before{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,rgba(11,17,20,.97) 0%,rgba(11,17,20,var(--ob-scrim)) 64%,rgba(11,17,20,.3) 100%)}
.ob-lhead>div{padding:clamp(24px,4vw,48px);width:100%}
.ob-back{display:inline-flex;align-items:center;gap:8px;min-height:44px;font:500 13px/1 var(--ob-mono);letter-spacing:.04em;color:var(--ob-lead);text-decoration:none;margin:-10px 0 6px -4px;padding:0 4px;border-radius:8px}
.ob-back:hover{color:#fff;text-decoration:underline}
.ob-lhead h1{font-size:clamp(38px,6vw,72px);line-height:1;letter-spacing:-.04em;margin:16px 0 14px}
.ob-upd{margin:0;font:500 13px/1.4 var(--ob-mono);letter-spacing:.03em;color:var(--ob-lead);max-width:44em}
.ob-lay{display:grid;grid-template-columns:260px minmax(0,72ch);justify-content:center;gap:clamp(32px,6vw,96px);padding:56px 0 120px;align-items:start}
.ob-toc{position:sticky;top:24px;font-size:15px;max-height:calc(100vh - 48px);overflow:auto;padding-right:4px}
.ob-toc summary{font:500 12px/1 var(--ob-mono);letter-spacing:.14em;text-transform:uppercase;color:var(--ob-muted);list-style:none;cursor:pointer;min-height:44px;display:flex;align-items:center;justify-content:space-between;gap:12px;border:1px solid var(--ob-line);border-radius:12px;padding:0 14px;background:var(--ob-card);display:none}
.ob-toc summary::-webkit-details-marker{display:none}
.ob-toc summary::after{content:"+";font-size:16px}
.ob-toc details[open] summary::after{content:"\2212"}
.ob-toc-h{font:500 12px/1 var(--ob-mono);letter-spacing:.14em;text-transform:uppercase;color:var(--ob-muted);margin:0 0 12px}
.ob-toc ol{list-style:none;margin:0;padding:0;border-left:1px solid var(--ob-line)}
.ob-toc ol ol{border:0;margin:0 0 6px 28px}
.ob-toc a{display:flex;gap:12px;padding:8px 8px 8px 16px;margin-left:-1px;border-left:2px solid transparent;color:var(--ob-muted);text-decoration:none;line-height:1.3;border-radius:0 8px 8px 0}
.ob-toc a b{font:500 11.5px/1.6 var(--ob-mono);color:var(--ob-accent);flex:none}
.ob-toc ol ol a{padding:5px 8px 5px 12px;font-size:14px}
.ob-toc a:hover{color:var(--ob-text);border-left-color:var(--ob-accent)}
.ob-toc a.is-on{color:var(--ob-text);border-left-color:var(--ob-accent);font-weight:600;background:rgba(127,160,175,.12)}
.ob-toc .ob-back2{display:inline-flex;align-items:center;min-height:44px;margin-top:18px;padding:0 4px;color:var(--ob-link);font-weight:600;text-decoration:none}
.ob-toc .ob-back2:hover{text-decoration:underline}
.ob-doc{max-width:72ch;font-size:17.5px;line-height:1.7}
.ob-short{margin:0 0 48px;padding:24px 28px;border:1px solid var(--ob-line);border-left:3px solid var(--ob-accent);border-radius:16px;background:linear-gradient(180deg,var(--ob-top),var(--ob-bot));box-shadow:var(--ob-shadow)}
.ob-short .ob-lbl{font:600 12px/1 var(--ob-mono);letter-spacing:.14em;text-transform:uppercase;color:var(--ob-accent);margin:0 0 12px}
.ob-short p:last-child{margin:0;font-size:18.5px;line-height:1.6}
.ob-sec h2{font-size:clamp(24px,2.6vw,30px);line-height:1.15;letter-spacing:-.025em;margin:56px 0 14px;padding-top:28px;border-top:1px solid var(--ob-line)}
.ob-sec:first-of-type h2{margin-top:0}
.ob-sec h2::before{content:attr(data-n);display:block;font:500 12px/1 var(--ob-mono);color:var(--ob-accent);letter-spacing:.12em;margin-bottom:12px}
.ob-sec h3{font-size:20px;line-height:1.25;letter-spacing:-.015em;margin:34px 0 8px}
.ob-doc p{margin:0 0 1.1em}
.ob-doc ul{padding-left:1.2em;margin:0 0 1.2em}
.ob-doc li{margin:0 0 .7em;padding-left:.3em}
.ob-doc li::marker{color:var(--ob-accent)}
.ob-doc strong{font-weight:650}
.ob-doc .contact{font-size:22px;font-weight:600}
.ob-doc a{word-break:break-word}

@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{animation:none!important;transition:none!important}}
@media (max-width:1180px){.ob-float{display:none}.ob-hero-grid{grid-template-columns:minmax(0,1fr) minmax(0,400px)}.ob-hero-device{--pw:320px}}
@media (max-width:1020px){
  .ob-hero-grid{grid-template-columns:1fr;min-height:0;gap:8px}
  .ob-hero-copy{padding:8px 0 24px}
  .ob-hero-device{justify-content:center;--pw:min(320px,82vw)}
  .ob-hero::after{background:linear-gradient(180deg,rgba(11,17,20,var(--ob-scrim)) 0%,rgba(11,17,20,var(--ob-scrim)) 66%,rgba(11,17,20,.6) 100%)}
  .ob-section-head{grid-template-columns:1fr}
  .ob-t1,.ob-t5,.ob-t6,.ob-t8,.ob-t9,.ob-t2,.ob-t7{grid-column:span 12}
  .ob-t3,.ob-t4{grid-column:span 6}
  .ob-t2{grid-row:auto;--scrim:linear-gradient(180deg,rgba(11,17,20,var(--ob-scrim)) 0,rgba(11,17,20,var(--ob-scrim)) 300px,rgba(11,17,20,.5) 600px,rgba(11,17,20,.35) 100%)}
  .ob-t6,.ob-t7{flex-direction:column;min-height:0}
  .ob-t6{--scrim:linear-gradient(180deg,rgba(11,17,20,var(--ob-scrim)) 0,rgba(11,17,20,var(--ob-scrim)) 500px,rgba(11,17,20,.45) 760px,rgba(11,17,20,.35) 100%)}
  .ob-t7{--scrim:linear-gradient(180deg,rgba(11,17,20,var(--ob-scrim)) 0,rgba(11,17,20,var(--ob-scrim)) 820px,rgba(11,17,20,.45) 1060px,rgba(11,17,20,.35) 100%)}
  .ob-t6 .ob-shot,.ob-t7 .ob-shot{align-self:center;padding-top:8px}
  .ob-t7 .ob-phone{margin-right:0}
  .ob-tx{padding-bottom:12px}
  .ob-t8{--scrim:linear-gradient(90deg,rgba(11,17,20,var(--ob-scrim)),rgba(11,17,20,var(--ob-scrim)))}
  .ob-strip{grid-template-columns:repeat(2,1fr)}
  .ob-strip>div{border-left:0;padding:24px 20px}
  .ob-strip>div:nth-child(even){border-left:1px solid var(--ob-line)}
  .ob-strip>div:nth-child(n+3){border-top:1px solid var(--ob-line)}
  .ob-lay{grid-template-columns:minmax(0,72ch);padding-top:32px}
  .ob-toc{position:static;max-height:none;overflow:visible}
  .ob-toc summary{display:flex}
  .ob-toc-h{display:none}
  .ob-toc details[open] summary{margin-bottom:12px}
  .ob-foot-grid{grid-template-columns:1fr}
  .ob-foot nav{justify-content:flex-start;margin-left:-12px}
  .ob-steps{grid-template-columns:1fr}
}
@media (max-width:680px){
  body{font-size:16.5px}
  .ob-wrap{width:calc(100% - 40px)}
  .ob-tile{padding:26px;border-radius:24px}
  .ob-t3,.ob-t4{grid-column:span 12}
  .ob-section{padding-top:72px}
  .ob-nav a{padding:0 9px;font-size:12.5px}
  .ob-brand{font-size:17px}
  .ob-hero h1{margin-top:16px}
  .ob-glow{width:60px;height:60px;margin-bottom:24px}
  .ob-badges{flex-direction:column;align-items:stretch}
  .ob-chips{gap:6px}
  .ob-chips li{height:42px;font-size:13px}
  .ob-gauge{flex-direction:column;align-items:flex-start}
  .ob-close .ob-wrap{padding:80px 0}
  .ob-ledger{grid-template-columns:1fr}
  .ob-t6 .ob-phone,.ob-t7 .ob-phone{--w:min(268px,100%)}
  .ob-doc{font-size:17px}
  .ob-lhead::before{background:linear-gradient(90deg,rgba(11,17,20,.97) 0%,rgba(11,17,20,var(--ob-scrim)) 80%,rgba(11,17,20,.7) 100%)}
  .ob-short{padding:20px}
  .ob-strip dd{font-size:14px}
}
'''

# (label, foreground var, background var) in the colour set that holds where the pair sits. 'mode' sets: light and dark
# resolve the page's themed vars; inv resolves the always-dark vars, which are the same in both modes.
TEXT = ('text', 'muted', 'link', 'accent', 'mint', 'ember')
SURF = ('bg', 'card', 'raised')

GRAPHICS = [  # meaning-carrying graphics and UI boundaries
    ('RSI line on card', 'text', 'card'), ('overbought line / dots on card', 'ember', 'card'),
    ('oversold line / dots on card', 'mint', 'card'), ('chart line on raised', 'accent', 'raised'),
    ('gauge arc on card', 'accent', 'card'), ('lock mark on chip', 'muted', 'raised'),
    ('focus ring on page', 'focus', 'bg'), ('focus ring on card', 'focus', 'card'),
    ('focus ring on raised', 'focus', 'raised'),
]


def _vars(block):
    return dict(re.findall(r'--ob-([a-z0-9]+):(#[0-9A-Fa-f]{6})', block))


def _block(style, opener):
    i = style.index(opener) + len(opener)
    depth, j = 1, i
    while depth:
        depth += {'{': 1, '}': -1}.get(style[j], 0); j += 1
    return style[i:j - 1]


def css():
    f = lambda d: ';'.join(f'--ob-{k}:{v}' for k, v in d.items())
    return (CSS.replace('@@LIGHT@@', f(LIGHT)).replace('@@DARK@@', f(DARK)).replace('@@INV@@', f(INV))
               .replace('@@CONST@@', f(CONST)).replace('@@SCRIM@@', SCRIM))


def audit(html):
    """Contrast of every text/background pair and meaningful graphic the stylesheet can show, read from the <style>
    of a generated page. -> (rows, ok); a row is (mode, label, fg, bg, ratio). Everything is held to 4.5:1 (graphics and focus rings need only 3:1; the stricter bar keeps one number). Importing gen_legal_apps here (not at the top) avoids an import cycle."""
    from gen_legal_apps import ratio, hexs
    style = re.search(r'<style>(.*?)</style>', html, re.S).group(1)
    root = _block(style, ':root{')
    light = _vars(root)
    dark = dict(light, **_vars(_block(style, '(prefers-color-scheme:dark){:root{')))
    inv = dict(light, **_vars(_block(style, '.ob-inv{')))
    scrim = float(re.search(r'--ob-scrim:([0-9.]+)', root).group(1))
    rows = []

    def add(mode, label, fg, bg):
        rows.append((mode, label, fg, bg, ratio(fg, bg)))

    for mode, v in (('light', light), ('dark', dark), ('inv', inv)):
        for s in SURF:
            for t in TEXT + (('lead',) if mode == 'inv' else ()):
                add(mode, f'{t} text on {s}', v[t], v[s])
        # the tile gradient runs raised > card in dark; the light tiles are white to white
        for t in TEXT:
            add(mode, f'{t} text on tile top', v[t], v['top']); add(mode, f'{t} text on tile bottom', v[t], v['bot'])
        for label, fg, bg in GRAPHICS:
            add(mode, label, v[fg], v[bg])
        add(mode, 'chip text on selected chip', v['chipfg'], v['chipbg'])
        add(mode, 'badge text', v['badgefg'], v['badgebg'])
        add(mode, 'Pro tag text', v['tagfg'], v['tagbg'])
        add(mode, 'skip link', v['skipfg'], v['skipbg'])
        add(mode, 'selected chip outline on card', v['chipline'], v['card'])
    worst = hexs(tuple(scrim * a + (1 - scrim) * 255 for a in (11, 17, 20)))  # scrim over a pure white plate pixel
    for t in ('text', 'lead', 'muted', 'link', 'accent', 'mint', 'ember'):
        add('plate', f'{t} text in the scrim (alpha {scrim}) over white', inv[t], worst)
    add('plate', 'badge text on its pill', inv['badgefg'], inv['badgebg'])
    return rows, all(r[4] >= MIN for r in rows)


# ------------------------------------------------------------------ content
NAV = [('privacy', 'Privacy', 'privacy.html'), ('terms', 'Terms', 'terms.html'), ('support', 'Support', 'support.html')]
MAIL = 'hello@seizeapps.com'
LOCK = ('<svg viewBox="0 0 10 10" aria-hidden="true"><rect x="1.5" y="4.5" width="7" height="4.5" rx="1" fill="currentColor"/>'
        '<path d="M3 4.5V3a2 2 0 0 1 4 0v1.5" fill="none" stroke="currentColor" stroke-width="1.2"/></svg>')
TFS = ['5m', '15m', '30m', '1h', '2h', '3h', '4h', '8h', '12h', '1D', '2D', '3D', '1W', '2W', '1M']

DIAG_D = 'M0.0,134.6C4.3,133.1 17.1,129.2 25.7,125.4C34.2,121.6 42.8,117.0 51.3,111.6C59.9,106.2 68.4,99.0 77.0,93.2C85.6,87.5 94.1,82.5 102.7,77.1C111.2,71.7 119.8,66.0 128.3,61.0C136.9,56.0 145.4,48.0 154.0,47.2C162.6,46.4 171.1,52.6 179.7,56.4C188.2,60.2 196.8,64.8 205.3,70.2C213.9,75.6 222.4,82.5 231.0,88.6C239.6,94.7 248.1,100.9 256.7,107.0C265.2,113.1 273.8,119.3 282.3,125.4C290.9,131.5 299.4,137.3 308.0,143.8C316.6,150.3 325.1,157.6 333.7,164.5C342.2,171.4 350.8,179.1 359.3,185.2C367.9,191.3 376.4,199.8 385.0,201.3C393.6,202.8 402.1,199.4 410.7,194.4C419.2,189.4 427.8,179.1 436.3,171.4C444.9,163.7 453.4,155.7 462.0,148.4C470.6,141.1 479.1,133.8 487.7,127.7C496.2,121.6 504.8,116.6 513.3,111.6C521.9,106.6 530.4,98.6 539.0,97.8C547.6,97.0 556.1,107.8 564.7,107.0C573.2,106.2 581.8,94.4 590.3,93.2C598.9,92.1 611.7,99.0 616.0,100.1'
CHART_D = 'M0.0,92.0C3.2,91.0 12.7,86.3 19.0,86.0C25.4,85.7 31.7,90.7 38.1,90.0C44.4,89.3 50.8,85.7 57.1,82.0C63.5,78.3 69.8,69.7 76.2,68.0C82.5,66.3 88.9,73.3 95.2,72.0C101.6,70.7 107.9,61.3 114.3,60.0C120.6,58.7 127.0,64.7 133.3,64.0C139.7,63.3 146.0,56.3 152.4,56.0C158.7,55.7 165.1,61.7 171.4,62.0C177.8,62.3 184.1,60.0 190.5,58.0C196.8,56.0 203.2,50.7 209.5,50.0C215.9,49.3 222.2,55.3 228.6,54.0C234.9,52.7 241.3,43.3 247.6,42.0C254.0,40.7 260.3,44.3 266.7,46.0C273.0,47.7 279.4,53.3 285.7,52.0C292.1,50.7 298.4,39.7 304.8,38.0C311.1,36.3 317.5,40.3 323.8,42.0C330.2,43.7 336.5,48.3 342.9,48.0C349.2,47.7 355.6,42.3 361.9,40.0C368.3,37.7 374.6,34.3 381.0,34.0C387.3,33.7 396.8,37.3 400.0,38.0'

DIAGRAM = f'''<div class="ob-diagram pre" id="ob-diagram">
<svg viewBox="0 0 640 260" role="img" aria-label="Illustration: an RSI line rises past the 70 line, stays in the overbought zone, falls back, then dips below the 30 line. Filled dots mark the only two crossings that raise an alert. The three steps below describe it in words.">
<defs>
<linearGradient id="obHi" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="var(--ob-ember)" stop-opacity=".22"/><stop offset="1" stop-color="var(--ob-ember)" stop-opacity=".03"/></linearGradient>
<linearGradient id="obLo" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="var(--ob-mint)" stop-opacity=".22"/><stop offset="1" stop-color="var(--ob-mint)" stop-opacity=".03"/></linearGradient>
</defs>
<rect x="0" y="15" width="640" height="69" fill="url(#obHi)"/>
<rect x="0" y="176" width="640" height="69" fill="url(#obLo)"/>
<line x1="0" x2="640" y1="84" y2="84" stroke="var(--ob-ember)" stroke-width="1.5" stroke-dasharray="4 5"/>
<line x1="0" x2="640" y1="176" y2="176" stroke="var(--ob-mint)" stroke-width="1.5" stroke-dasharray="4 5"/>
<path class="ob-line" pathLength="1" d="{DIAG_D}"/>
<g class="ob-dots">
<circle cx="91.7" cy="84" r="7" fill="var(--ob-ember)" stroke="var(--ob-card)" stroke-width="3"/>
<circle cx="347.9" cy="176" r="7" fill="var(--ob-mint)" stroke="var(--ob-card)" stroke-width="3"/>
<circle cx="616" cy="100.1" r="6" fill="var(--ob-text)" stroke="var(--ob-card)" stroke-width="3"/>
</g>
</svg>
<span class="ob-axis hi" style="top:32.3%;transform:translateY(-130%)">70</span>
<span class="ob-axis lo" style="top:67.7%;transform:translateY(30%)">30</span>
<span class="ob-pin hi" style="left:14.3%;top:14%" aria-hidden="true">01</span>
<span class="ob-pin mid" style="left:25%;top:11%" aria-hidden="true">02</span>
<span class="ob-pin lo" style="left:54.4%;top:86%" aria-hidden="true">03</span>
</div>
<ol class="ob-steps" aria-label="How one crossing reads">
<li class="hi"><b>01</b>A candle closes past 70. One alert.</li>
<li class="mid"><b>02</b>RSI stays in the zone. Nothing.</li>
<li class="lo"><b>03</b>A candle closes below 30. One alert.</li>
</ol>
<p class="ob-note">Illustration, not market data</p>'''

GAUGE = '''<div class="ob-gauge"><svg viewBox="0 0 200 190" role="img" aria-label="Example gauge reading 60.3, Neutral">
<path d="M43.43,156.57A80,80 0 1 1 156.57,156.57" fill="none" stroke="var(--ob-raised)" stroke-width="12" stroke-linecap="round"/>
<path d="M42.45,155.57A80,80 0 0 1 35.28,52.98" fill="none" stroke="var(--ob-mint)" stroke-width="5" stroke-linecap="round"/>
<path d="M164.72,52.98A80,80 0 0 1 157.55,155.57" fill="none" stroke="var(--ob-ember)" stroke-width="5" stroke-linecap="round"/>
<path d="M37.57,49.98A80,80 0 0 1 137.32,29.24" fill="none" stroke="var(--ob-accent)" stroke-width="12" stroke-linecap="round"/>
<circle cx="137.3" cy="29.2" r="6.5" fill="var(--ob-text)" stroke="var(--ob-card)" stroke-width="3"/>
<text x="100" y="92" text-anchor="middle" font-family="ui-monospace,Menlo,monospace" font-size="13" font-weight="500" fill="var(--ob-muted)" letter-spacing="2">RSI</text>
<text x="100" y="128" text-anchor="middle" font-family="ui-monospace,Menlo,monospace" font-size="38" font-weight="500" fill="var(--ob-text)" letter-spacing="-1.5">60.3</text>
</svg><div><strong>Neutral</strong><span>9.7 points from overbought.</span></div></div>
<p class="ob-note">Example reading</p>'''

CHART = f'''<div class="ob-drag"><p class="ob-ex">Example</p>
<dl class="ob-read">
<div><dt>TIME</dt><dd>Oct 6, 2:00 PM</dd></div>
<div><dt>PRICE</dt><dd>$86,187</dd></div>
<div><dt>RSI</dt><dd>60.3</dd></div>
</dl>
<svg viewBox="0 0 400 120" role="img" aria-label="Example price chart with a vertical crosshair on one candle.">
<defs><linearGradient id="obP" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="var(--ob-accent)" stop-opacity=".28"/><stop offset="1" stop-color="var(--ob-accent)" stop-opacity="0"/></linearGradient></defs>
<path d="{CHART_D}L400,120L0,120Z" fill="url(#obP)"/>
<path d="{CHART_D}" fill="none" stroke="var(--ob-accent)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
<line x1="304.8" x2="304.8" y1="0" y2="120" stroke="var(--ob-text)" stroke-width="1" stroke-dasharray="3 4" opacity=".6"/>
<circle cx="304.8" cy="38" r="5.5" fill="var(--ob-text)" stroke="var(--ob-raised)" stroke-width="3"/>
</svg></div>'''

ARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 4l8 8M12 5.5V12H5.5"/></svg>'


def _chips():
    out = []
    for t in TFS:
        if t == '4h':
            out.append(f'<li class="on">{t}<span class="ob-sr"> (free)</span></li>')
        else:
            out.append(f'<li>{t}{LOCK}<span class="ob-sr"> (Pro)</span></li>')
    return ''.join(out)


def _head(app, key, title, desc, canonical, host):
    icon = 'media/icon-256.png'
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="{LIGHT['bg']}" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="{DARK['bg']}" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{host}overbit/media/icon-512.png">
<link rel="icon" href="{icon}">
<link rel="apple-touch-icon" href="{icon}">
<script>document.documentElement.className+=' js'</script>
<style>{css()}</style>
</head>
'''


def _nav(key, cls='ob-nav'):
    items = ''.join(f'<a href="{h}"{" aria-current=page" if k == key else ""}>{l}</a>' for k, l, h in NAV)
    return f'<nav class="{cls}" aria-label="Overbit">{items}</nav>'


def _foot():
    return f'''<footer class="ob-foot ob-inv">
<div class="ob-wrap ob-foot-grid">
<div><a class="ob-brand" href="./"><img src="media/icon-256.png" width="32" height="32" loading="lazy" alt="">Overbit</a>
<p>Overbit is not financial advice. It is not a broker and does not trade; it only tells you when RSI crosses a level.</p></div>
<nav aria-label="Legal and support"><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a><a href="support.html">Support</a><a href="mailto:{MAIL}">{MAIL}</a></nav>
<p class="ob-print">Prices come from on-chain trading pools, not an exchange, and can differ slightly from exchange charts. Overbit is not affiliated with any exchange or trading pool.</p>
</div>
</footer>'''


def _home(app):
    return f'''<body>
<a class="ob-skip" href="#main">Skip to content</a>
<header class="ob-hero ob-inv">
<div class="ob-wrap">
<div class="ob-top"><a class="ob-brand" href="./" aria-label="Overbit home"><img src="media/icon-256.png" width="32" height="32" alt="">Overbit</a>{_nav('index')}</div>
<div class="ob-hero-grid">
<div class="ob-hero-copy">
<img class="ob-glow" src="media/icon-256.png" width="72" height="72" alt="The Overbit app icon: a Bitcoin glyph inside a blue ring, with an RSI line crossing an orange band above and a green band below.">
<p class="ob-eyebrow"><b>BTC</b> &middot; RSI &middot; Alerts</p>
<h1>Know when Bitcoin&rsquo;s RSI <span>crosses.</span></h1>
<p class="ob-lead">One notification when RSI crosses into oversold or overbought, then nothing until it crosses again.</p>
<div class="ob-badges">
<span class="ob-badge" role="note"><i aria-hidden="true"></i>Coming soon to the App Store</span>
<span class="ob-chip">iPhone &middot; iOS 17 or later</span>
</div>
<p class="ob-cap">Screenshots show Overbit Pro. Prices and RSI values in them are examples from the app, not advice.</p>
</div>
<div class="ob-hero-device">
<div class="ob-float" aria-hidden="true"><em>Example</em><span class="ob-glyph">{ARROW}</span><div><strong>1h oversold</strong><span class="ob-sub">RSI 28.6</span></div></div>
<div class="ob-phone"><img src="media/screen-01-on-chain.webp" width="720" height="1485" alt="Overbit on iPhone: the live Bitcoin price and chart, a row of timeframe chips, and an RSI 14 card with a gauge reading 60.3, Neutral, above a panel with the 30 and 70 lines."></div>
</div>
</div>
</div>
</header>

<main id="main">
<section class="ob-spec" aria-label="At a glance">
<div class="ob-wrap"><dl class="ob-strip">
<div><dt>15</dt><dd>timeframes, from 5 minutes to 1 month</dd></div>
<div><dt><span class="ob-ice">14</span><small>/</small><span class="ob-mint">30</span><small>/</small><span class="ob-ember">70</span></dt><dd>default RSI length, oversold and overbought</dd></div>
<div><dt>1</dt><dd>notification per crossing, nothing while RSI stays in the zone</dd></div>
<div><dt>0</dt><dd>accounts, sign-ins, ads or tracking</dd></div>
</dl></div>
</section>

<section class="ob-section" aria-labelledby="ob-h-signal">
<div class="ob-wrap">
<div class="ob-section-head">
<div><p class="ob-eyebrow"><b>01</b> &mdash; The signal</p><h2 id="ob-h-signal">One screen. One signal.</h2></div>
<p>Live Bitcoin price, a price chart and an RSI panel, nothing else. Overbit reads RSI on closed candles and speaks only when it crosses a line.</p>
</div>
<div class="ob-bento">

<article class="ob-tile ob-t1">
<p class="ob-eyebrow">Alerts</p>
<h3>One alert. No noise.</h3>
<p>A notification when a candle closes past the line. Nothing while RSI stays in the zone.</p>
{DIAGRAM}
</article>

<article class="ob-tile ob-t2 ob-inv ob-plate">
<p class="ob-eyebrow">History</p>
<h3>Every crossing, on the record.</h3>
<p>Alert history lists each alert with timeframe, direction, RSI, price and time.</p>
<div class="ob-shot"><div class="ob-phone"><img src="media/screen-02-one-alert.webp" width="720" height="1485" loading="lazy" alt="Overbit alert history: 1h overbought, 4h overbought, 1h oversold, 1D overbought and 4h oversold, each with its RSI value and price."></div></div>
</article>

<article class="ob-tile ob-t3">
<p class="ob-eyebrow">Gauge</p>
<h3>Where RSI stands.</h3>
<p>The gauge shows the current zone and the points left to the next level.</p>
<div class="ob-vis">{GAUGE}</div>
</article>

<article class="ob-tile ob-t4">
<p class="ob-eyebrow">Chart</p>
<h3>Drag to read any candle.</h3>
<p>Press and drag the chart to see the time, price and RSI of any candle.</p>
<div class="ob-vis">{CHART}</div>
</article>

<article class="ob-tile ob-t5">
<p class="ob-eyebrow">Timeframes</p>
<h3>5 minutes to 1 month.</h3>
<p>15 timeframes, each with its own alerts switch.</p>
<div class="ob-vis">
<ul class="ob-chips" aria-label="The 15 timeframes: 4h is free, the other 14 come with Pro">{_chips()}</ul>
<p class="ob-key"><span><i aria-hidden="true"></i>Free</span><span>{LOCK}With Pro</span></p>
<p class="ob-cap2">4h to start; switching between timeframes is part of Pro.</p>
</div>
</article>

<article class="ob-tile ob-t6 ob-inv ob-plate">
<div class="ob-tx">
<p class="ob-eyebrow">Settings</p>
<h3>Your timeframes, your levels.<span class="ob-tag">Pro</span></h3>
<p>Set the RSI length and the oversold and overbought lines. The defaults are 14, 30 and 70.</p>
<ul class="ob-facts">
<li>Choose which timeframes alert</li>
<li>RSI length, oversold and overbought lines</li>
<li>Notifications on or off in one place</li>
</ul>
</div>
<div class="ob-shot"><div class="ob-phone"><img src="media/screen-04-your-levels.webp" width="720" height="1485" loading="lazy" alt="Overbit settings: a grid of timeframes from 5m to 1M, an RSI length stepper set to 14, oversold 30 and overbought 70 fields, and a notifications toggle."></div></div>
</article>

<article class="ob-tile ob-t7 ob-inv ob-plate">
<div class="ob-tx">
<p class="ob-eyebrow">Overbit Pro</p>
<h3>Go further with Pro.</h3>
<p>A one-time purchase, not a subscription. Family Sharing is on.</p>
<div class="ob-ledger">
<div><h4>Included</h4><ul><li>One timeframe, 4h to start</li><li>RSI 14, levels 30 and 70</li><li>Chart, RSI panel and alert history</li></ul></div>
<div class="pro"><h4>With Pro</h4><ul><li>All 15 timeframes</li><li>Your own RSI length and levels</li><li>A feedback box to the developer</li></ul></div>
</div>
<p class="ob-fine">The App Store shows the price in your currency before you buy. Restore Purchases is always on the Pro screen.</p>
</div>
<div class="ob-shot"><div class="ob-phone"><img src="media/screen-05-pro.webp" width="720" height="1485" loading="lazy" alt="The Overbit Pro sheet: Every timeframe, your own levels, with three rows: unlimited timeframes, custom RSI length and levels, and a feedback box."></div></div>
</article>

<article class="ob-tile ob-t8 ob-inv ob-plate">
<p class="ob-eyebrow">On-chain</p>
<h3>Where the price comes from.</h3>
<p>Overbit reads Bitcoin&rsquo;s price from on-chain trading pools, not an exchange, so it can differ slightly from exchange charts. If the pools disagree, alerts on 15-minute and shorter timeframes pause until they agree.</p>
</article>

<article class="ob-tile ob-t9">
<p class="ob-eyebrow">Privacy</p>
<h3>What leaves your iPhone.</h3>
<p>No account, no sign-in, no ads, no tracking. A random ID registers your install so the server can send alerts; you can delete that record in the app.</p>
<a class="ob-more" href="privacy.html">Read the Privacy Policy <span aria-hidden="true">&rarr;</span></a>
</article>

</div>
</div>
</section>
</main>

<section class="ob-close ob-inv" aria-labelledby="ob-h-close">
<div class="ob-wrap">
<p class="ob-eyebrow">iPhone &middot; iOS 17 or later</p>
<h2 id="ob-h-close">Coming soon to the App Store.</h2>
<p>Overbit tells you when Bitcoin&rsquo;s RSI crosses into oversold or overbought. One notification when a candle closes past the line.</p>
<span class="ob-badge" role="note"><i aria-hidden="true"></i>Coming soon to the App Store</span>
<p class="ob-langs">App languages: English, Spanish, French, German, Italian, Portuguese, Japanese, Korean and Chinese.</p>
</div>
</section>

{_foot()}
<script>
(function(){{var d=document.getElementById('ob-diagram');if(!d)return;
if(!('IntersectionObserver' in window)||matchMedia('(prefers-reduced-motion: reduce)').matches){{d.classList.remove('pre');return}}
var io=new IntersectionObserver(function(e){{if(e[0].isIntersecting){{d.classList.remove('pre');io.disconnect()}}}},{{threshold:.4}});io.observe(d)}})();
</script>
</body>
</html>
'''


def _slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def _split(body):
    """h1, updated line, summary text, then the sections [(h2 text, html up to the next h2)]."""
    take = lambda pat: (lambda m: (m.group(1).strip(), body.replace(m.group(0), '', 1)) if m else ('', body))(re.search(pat, body, re.S))
    h1, body = take(r'<h1>(.*?)</h1>')
    upd, body = take(r'<p class="updated">(.*?)</p>')
    m = re.search(r'<p class="summary">(.*?)</p>', body, re.S)
    summ = ''
    if m:
        summ = re.sub(r'^\s*<strong>.*?</strong>\s*', '', m.group(1), flags=re.S).strip()
        body = body.replace(m.group(0), '', 1)
    parts = re.split(r'<h2>(.*?)</h2>', body)
    return h1, upd, summ, list(zip(parts[1::2], parts[2::2]))


def _legal(app, key, body):
    h1, upd, summ, secs = _split(body)
    toc, out = [], []
    for n, (h, chunk) in enumerate(secs, 1):
        h = re.sub(r'^\d+\.\s+', '', h.strip())
        sid = _slug(h); num = f'{n:02d}'
        subs = []

        def q(m):
            qid = _slug(m.group(1)); subs.append((qid, m.group(1)))
            return f'<h3 id="{qid}">{m.group(1)}</h3>'
        chunk = re.sub(r'<h3>(.*?)</h3>', q, chunk.strip())
        sub = ('<ol>' + ''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in subs) + '</ol>') if subs else ''
        toc.append(f'<li><a href="#{sid}"><b>{num}</b><span>{h}</span></a>{sub}</li>')
        out.append(f'<section class="ob-sec" aria-labelledby="{sid}"><h2 id="{sid}" data-n="{num}">{h}</h2>\n{chunk}</section>')
    short = (f'<aside class="ob-short" aria-labelledby="ob-short"><p class="ob-lbl" id="ob-short">The short version</p><p>{summ}</p></aside>\n'
             if summ else '')
    eyebrow = 'Help' if key == 'support' else 'Legal'
    updated = upd if re.match(r'(Last updated|Effective)', upd) else upd
    return f'''<body>
<a class="ob-skip" href="#main">Skip to content</a>
<header class="ob-wrap ob-top"><a class="ob-brand" href="./" aria-label="Overbit home"><img src="media/icon-256.png" width="32" height="32" alt="">Overbit</a>{_nav(key)}</header>
<main id="main" class="ob-wrap">
<header class="ob-lhead ob-inv"><img src="media/plate-search.jpg" width="1600" height="1066" alt="">
<div><a class="ob-back" href="./"><span aria-hidden="true">&larr;</span> Back to Overbit</a><p class="ob-eyebrow">{eyebrow}</p><h1>{h1}</h1><p class="ob-upd">{updated}</p></div></header>
<div class="ob-lay">
<aside class="ob-toc" aria-label="On this page"><details id="ob-toc-d" open><summary>On this page</summary><p class="ob-toc-h">On this page</p><ol>{''.join(toc)}</ol></details>
<a class="ob-back2" href="./"><span aria-hidden="true">&larr;&nbsp;</span> Back to Overbit</a></aside>
<article class="ob-doc">
{short}{chr(10).join(out)}
</article>
</div>
</main>
{_foot()}
<script>
(function(){{var d=document.getElementById('ob-toc-d'),mq=matchMedia('(max-width:1020px)');
function f(){{d.open=!mq.matches}}f();if(mq.addEventListener)mq.addEventListener('change',f);
var L={{}},A=[].slice.call(document.querySelectorAll('.ob-toc a[href^="#"]'));
A.forEach(function(a){{L[a.getAttribute('href').slice(1)]=a}});
var H=[].slice.call(document.querySelectorAll('.ob-doc h2[id],.ob-doc h3[id]'));
if(!('IntersectionObserver' in window)||!H.length)return;
var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{A.forEach(function(a){{a.classList.remove('is-on');a.removeAttribute('aria-current')}});
var a=L[e.target.id];if(a){{a.classList.add('is-on');a.setAttribute('aria-current','true')}}}}}})}},{{rootMargin:'-10% 0px -75% 0px'}});
H.forEach(function(h){{io.observe(h)}})}})();
</script>
</body>
</html>
'''


def page(app, lang, key, title, desc, body, host, alts):
    canonical = f'{host}overbit/' if key == 'index' else f'{host}overbit/{key}.html'
    head = _head(app, key, title, desc, canonical, host)
    return head + (_home(app) if key == 'index' else _legal(app, key, body))
