# Generates seizeapps.com: index.html + apps/*.html from one data block.
# Legal pages (privacy.html, terms.html) are edited by hand and only share the
# header/footer markup below — keep them in sync when this changes.
# Identity: SEIZE 2026 (brand/design-tokens.json v2.1, brand/sheets/02-web-ui-system.png).
import os
SITE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root

def head(title, desc, root, canonical, og_title=None):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#060E1F">
<meta name="description" content="{desc}">
<link rel="canonical" href="https://seizeapps.com/{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Seize Apps">
<meta property="og:title" content="{og_title or title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://seizeapps.com/{canonical}">
<meta property="og:image" content="https://seizeapps.com/assets/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<title>{title}</title>
<link rel="icon" type="image/png" sizes="64x64" href="{root}favicon.png">
<link rel="icon" type="image/png" sizes="32x32" href="{root}favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="{root}favicon-16.png">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{root}assets/site.css?v=2026-09-16b">
</head>
<body>
'''

def header(root, current=None):
    def nav(href, label, key):
        cur=' aria-current="page"' if current==key else ''
        return f'<a href="{root}{href}"{cur}>{label}</a>'
    return f'''<header class="site-header shell">
  <a class="brand" href="{root}index.html" aria-label="Seize home">
    <img class="brand-mark" src="{root}assets/seize-mark.png?v=1" alt="" width="36" height="36">
    <span class="wordmark">SEIZE</span>
  </a>
  <nav class="site-nav" aria-label="Main">
    {nav('index.html#apps','Apps','apps')}
    {nav('index.html#philosophy','Philosophy','philosophy')}
    {nav('index.html#studio','Studio','studio')}
    <a class="button small" href="mailto:hello@seizeapps.com">Get in touch</a>
  </nav>
</header>
'''

def footer(root):
    return f'''<footer class="site-footer">
  <div class="footer-inner shell">
    <div class="footer-brand">
      <img src="{root}assets/seize-mark.png?v=1" alt="" width="28" height="28">
      <div>
        <p class="footer-signoff">Apps for a brighter tomorrow.</p>
        <p class="copyright">© 2026 Seize Apps · Izotz Cristobal Mota &amp; Sendoa Sola · Basque Country, Spain</p>
      </div>
    </div>
    <nav class="footer-links" aria-label="Footer">
      <a href="{root}index.html#apps">Apps</a>
      <a href="{root}privacy.html">Privacy</a>
      <a href="{root}terms.html">Terms</a>
      <a href="https://github.com/SeizeApps" rel="noopener">GitHub</a>
      <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>
    </nav>
  </div>
</footer>
</body>
</html>
'''

# Wave motif from the brand sheet — inline SVG, no image.
WAVE='''<svg class="wave" viewBox="0 0 1440 420" preserveAspectRatio="none" aria-hidden="true">
  <defs>
    <linearGradient id="wg" x1="0" x2="1" y1="0" y2="0">
      <stop offset="0" stop-color="#007AFF" stop-opacity="0"/>
      <stop offset=".45" stop-color="#007AFF" stop-opacity=".55"/>
      <stop offset=".75" stop-color="#22D3EE" stop-opacity=".7"/>
      <stop offset="1" stop-color="#22D3EE" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <path d="M0 300 C 240 200, 420 380, 700 260 S 1120 120, 1440 240" fill="none" stroke="url(#wg)" stroke-width="2"/>
  <path d="M0 340 C 260 240, 460 420, 760 300 S 1160 160, 1440 280" fill="none" stroke="url(#wg)" stroke-width="1.5" opacity=".6"/>
  <path d="M0 260 C 220 160, 400 340, 660 220 S 1080 80, 1440 200" fill="none" stroke="url(#wg)" stroke-width="1" opacity=".4"/>
</svg>'''

APPS=[
 dict(slug='cycle-timers', name='Cycle Timers', icon='cycle-timers.png', lead='Izotz Cristobal Mota',
      one='Recurring household timers you read at a glance — from the Home Screen widget, without opening the app.',
      tags=['Household','Widgets','iOS'], privacy_id='cycle-timers',
      lede='Every chore has a cycle. <strong>Cycle Timers</strong> turns the things you repeat and forget — fresh water for the plants, clean sheets, the cat litter — into glanceable rings that drain over time and restart the moment you mark them done.',
      meta=['iOS 17+','Home Screen &amp; Lock Screen widgets','No account'],
      features=[('01 / SEE','Time, at a glance','Colour and shape tell you what is fresh, what is close, and what needs attention now. No lists to read.'),
                ('02 / TAP','Done means restarted','One tap marks a task done and begins its next cycle — directly from the Home Screen widget if you like.'),
                ('03 / KEEP','Yours, not ours','No account and no tracking. Your timers stay on your device, where a household tool belongs.')],
      privacy='Cycle Timers collects no data whatsoever. Timers live on your device, in a private container shared only with the app\'s own widgets; reminders are scheduled locally.',
      shots=[('cycle-01-home.jpg','Six rings, one glance'),('cycle-02-edit.jpg','A timer is a name, an icon and a cycle')]),
 dict(slug='tempo', name='Tempo', icon='tempo.png', lead='Izotz Cristobal Mota',
      one='A workday companion that remembers your hours for you — arrive, work, leave — and keeps the record yours to correct.',
      tags=['Work','Time tracking','Calendar'], privacy_id='tempo',
      lede='Your work day is measured in what you got done, not in hours watched. <strong>Tempo</strong> notices when you arrive at work and when you leave, adds it up into one honest day, and lets you review, split or correct any of it. Manual mode from day one; automatic tracking only if you choose to draw a work zone.',
      meta=['iOS 17+','Live Activities','Calendar export','No account'],
      features=[('01 / ARRIVE','Hands-free hours','Draw a work zone once and Tempo does the rest with the location evidence iOS already keeps. Separate visits add up to one accurate workday.'),
                ('02 / SEE','Today, clearly','Time worked, your daily target, arrival and leave — one screen, and a month view that shows on-time, light and overtime days at a glance.'),
                ('03 / OWN','Your record, editable','Review, correct, split, merge or export. If a boundary was uncertain, Tempo asks instead of guessing.')],
      privacy='Tempo keeps your work sessions, zones and targets on your device. Location is used only to detect the work zone you drew, on the phone, and is never sent anywhere. No account, no analytics.',
      shots=[('tempo-01-welcome.jpg','Your workday, remembered'),('tempo-02-today.jpg','Today: time worked against your target'),('tempo-03-calendar.jpg','A month of days, coloured by how they went')]),
 dict(slug='drip', name='Drip', icon='drip.png', lead='Sendoa Sola',
      one='See exactly where your money drips: every subscription, bill and membership shown as what it really costs a year.',
      tags=['Subscriptions','Budget','ES · EN'], privacy_id='drip',
      lede='Monthly hides the pain. <strong>Drip</strong> tracks every recurring service — subscriptions, bills, memberships — and puts the true yearly cost next to what you pay each month. In English and Spanish. No account, no ads, no premium tier: just the number, and what to do about it.',
      meta=['iOS 17+','Widgets &amp; Siri Shortcuts','English · Spanish'],
      features=[('01 / REVEAL','Annual cost, always','That "just €9.99 a month" is €120 a year. Drip shows both, for every service, all the time — with a dashboard by category and billing cycle.'),
                ('02 / CONTROL','Know what\'s next','The next 14 days of charges at a glance, free-trial alerts, a monthly budget, and a swipe to mark a charge as paid. Pause a service instead of deleting it.'),
                ('03 / KEEP','Yours, not ours','No account and no tracking. Your services live on your device and in your own iCloud — never on a server of ours.')],
      privacy='Drip stores your services on your device, in a private container shared only with its widgets and Siri shortcuts, and in your own iCloud account — never anywhere we can see.',
      shots=[('drip-01-dashboard.jpg','Dashboard: the yearly figure first'),('drip-03-services.jpg','Every service, monthly and yearly'),('drip-04-detail.jpg','One service in detail'),('drip-02-dashboard-2.jpg','Where it drips most, by category')]),
 dict(slug='anchor', name='Anchor', icon='anchor.png', lead='Sendoa Sola',
      one='Daily support for eating-disorder recovery: routines that hold you and tools for the hard moment — alongside professional treatment, never instead of it.',
      tags=['Recovery','Routines','ES · EN'], privacy_id='anchor',
      lede='<strong>Anchor</strong> accompanies people recovering from an eating disorder. Routines that hold you — meals, rest, movement — confirmed with a tap; a single door, <em>Now</em>, for the hard moment: ride the urge, breathe with guidance, let an emotion pass, or open your safety plan. No calories, no weight, no streaks. Ever.',
      meta=['iOS 17+','Live Activities','Apple Health (optional, read-only)','English · Spanish'],
      features=[('01 / HOLD','Routines, not rules','Meals, rest and movement as daily blocks. Confirm with a tap; if a day doesn\'t go to plan, that\'s okay — Anchor says so.'),
                ('02 / NOW','One door for the hard moment','Urge surfing with a fifteen-minute companion, guided breathing without breath holds, "let it pass" for a strong emotion, and a safety plan with your people and your region\'s helplines, two taps away.'),
                ('03 / SEE','Without numbers','An emotional check-in with no scores, strategies grounded in DBT, CBT, ACT and self-compassion with their evidence in plain sight, and progress shown as the shape of your week — not a grade.')],
      privacy='Everything you enter stays on your device and in your own private iCloud. Apple Health is optional and read-only (sleep, activity), never weight or nutrition, and never leaves the phone. No analytics, no ads, no AI chat.',
      shots=[('anchor-01-home.jpg','Home: the next routine, and «Now»'),('anchor-02-now.jpg','«What\'s going on?» routes to the right tool'),('anchor-05-checkin.jpg','Check-in without numbers'),('anchor-06-strategies.jpg','Strategies, with their evidence')],
      extra='Anchor is not a medical device and does not replace professional treatment. If you are in danger or your own thoughts scare you, please contact your local emergency number.'),
 dict(slug='kover', name='Kover', icon='kover.png', lead='Sendoa Sola',
      one='Snap the receipt, and Kover watches the warranty: what is covered, until when, and a nudge before it runs out.',
      tags=['Warranties','Receipts','ES · EN'], privacy_id='kover',
      lede='Receipts fade, warranties expire quietly. <strong>Kover</strong> reads the date, store and amount from a photo or PDF of the receipt, works out the legal guarantee for your country, and keeps the photo, the serial number and the support contact in one place — with a reminder a month, a week and the day before it ends.',
      meta=['iOS 17+','Camera, Photos or PDF','English · Spanish'],
      features=[('01 / SCAN','The receipt does the typing','Camera, photo library or a PDF from your email: Kover pulls the date, store, amount and country. You add the name and it is filed.'),
                ('02 / WATCH','Covered until, in plain words','Legal guarantee by country — 36 months in Spain — plus any extended warranty on top. «3 years left», not a countdown of days. Reminders at one month, one week and the day of.'),
                ('03 / CLAIM','Everything for the day you need it','Serial number, support phone or website one tap away, the receipt photo, and a PDF to share. Claimed, replaced or gone: archive instead of delete.')],
      privacy='Kover keeps your products and receipt photos on your device and in your own iCloud account. Receipts are read on the phone with Apple\'s Vision framework — nothing is uploaded, no account, no analytics.',
      shots=[('kover-01-products.jpg','Next to expire, and the whole shelf'),('kover-02-detail.jpg','One product: covered until, in plain words'),('kover-03-scan.jpg','Camera, library or PDF'),('kover-04-add.jpg','The legal guarantee fills itself in')]),
 dict(slug='tandem', name='Tandem', icon='tandem.png', lead='Sendoa Sola',
      one='Fair expense splitting for couples: each pays in proportion to what they earn, and the month settles with one number.',
      tags=['Couples','Expenses','ES · EN'], privacy_id='tandem',
      lede='Fifty-fifty is only fair when you earn the same. <strong>Tandem</strong> takes two incomes and every shared expense — rent, groceries, the dinner out — and splits each one in proportion, so the month ends with a single transfer that both of you understand. One phone keeps the books for both.',
      meta=['iOS 17+','Widgets','English · Spanish'],
      features=[('01 / SPLIT','Proportional by default','Enter both incomes once. Every expense is split by that ratio — or 50/50, a custom share, or paid in full — and the ratio is frozen with the expense, so a raise next year never reopens last year\'s months.'),
                ('02 / SETTLE','One number a month','Who paid what, who owes whom, and the transfer that squares it. Mark it settled; undo it if you were too quick.'),
                ('03 / SEE','Where it goes','Recurring expenses that log themselves, reports by category, and a monthly bar of who actually paid.')],
      privacy='Tandem keeps names, incomes and expenses on your device and in your own iCloud account. Nothing is shared with anyone — not with us, and not with a server.',
      shots=[('tandem-01-dashboard.jpg','This month: shared, paid, to settle'),('tandem-02-expenses.jpg','Fixed and variable, by month'),('tandem-04-settle.jpg','Settle up: the math, in the open'),('tandem-03-reports.jpg','Who paid, month by month')]),
]

# ---------- index.html
cards=''.join(f'''
    <a class="app-card" href="apps/{a['slug']}.html">
      <img src="assets/icons/{a['icon']}" alt="" width="64" height="64">
      <h3>{a['name']}</h3>
      <p class="one-liner">{a['one']}</p>
      <div class="tags">{''.join(f'<span>{t}</span>' for t in a['tags'])}</div>
      <span class="card-more">Learn more <span aria-hidden="true">→</span></span>
    </a>''' for a in APPS)

index=head('Seize Apps — Extraordinary iOS apps for everyday life',
 'Seize designs and builds exceptional iOS apps that make life better: Cycle Timers, Tempo, Drip, Anchor, Kover and Tandem. An independent studio from the Basque Country.',
 '', '', og_title='Seize — Ideas into extraordinary.')+header('')+f'''<main>
  <section class="hero" aria-labelledby="hero-title">
    {WAVE}
    <div class="shell hero-grid">
      <div class="hero-copy">
        <p class="eyebrow">Apps for a brighter tomorrow</p>
        <h1 id="hero-title">Ideas into <span>extraordinary.</span></h1>
        <p class="lede">We design and build exceptional iOS apps that make life better. Small, native and private by design — each one does a single job, beautifully.</p>
        <div class="cta-row">
          <a class="button" href="#apps">Explore our apps</a>
          <a class="button ghost" href="#philosophy">Our philosophy</a>
        </div>
      </div>
      <div class="hero-phone" aria-hidden="true">
        <div class="phone"><img src="assets/shots/anchor-01-home.jpg" alt="" width="552" height="1200"></div>
      </div>
    </div>
  </section>

  <section class="section shell" id="apps" aria-labelledby="apps-title">
    <div class="section-head">
      <div><p class="eyebrow">Apps</p><h2 id="apps-title">Six apps, <span>six jobs.</span></h2></div>
      <p>Household rhythms, the working day, recurring money, recovery, warranties and the bills a couple shares. Different problems, one way of building: a screen you understand at a glance, your data on your device, Spanish and English from day one.</p>
    </div>
    <div class="app-grid">{cards}
    </div>
  </section>

  <section class="section shell" id="philosophy" aria-labelledby="philosophy-title">
    <div class="section-head">
      <div><p class="eyebrow">Philosophy</p><h2 id="philosophy-title">Beautiful. Useful. <span>Human. Possible.</span></h2></div>
      <p>Four words we hold every screen against. If a feature fails one of them, it doesn't ship — however clever it is.</p>
    </div>
    <div class="values">
      <div class="value"><span class="num">01</span><h3>Beautiful</h3><p>Design with an opinion: one dominant colour, weight before size, motion that means something. The kind of care you notice without being told.</p></div>
      <div class="value"><span class="num">02</span><h3>Useful</h3><p>Every app answers one real question people ask every day, and answers it on the first screen. No dashboards for their own sake.</p></div>
      <div class="value"><span class="num">03</span><h3>Human</h3><p>No accounts, no analytics, no advertising, no dark patterns. Your data lives on your iPhone and in your own iCloud — we never see it. Copy written for people, in two languages.</p></div>
      <div class="value"><span class="num">04</span><h3>Possible</h3><p>Native all the way: SwiftUI, widgets, Live Activities, Siri and Apple Health when they earn their place. Small teams can build things that feel first-party.</p></div>
    </div>
  </section>

  <section class="section shell" id="studio" aria-labelledby="studio-title">
    <div class="section-head">
      <div><p class="eyebrow">Studio</p><h2 id="studio-title">Two developers, <span>one bar.</span></h2></div>
      <p>Seize Apps is Izotz and Sendoa, from the Basque Country. Every app has one of us as its lead — the person who decides what ships and who answers for it — and both of us behind the same standard of craft.</p>
    </div>
    <div class="studio">
      <div class="person">
        <div class="initials a" aria-hidden="true">IC</div>
        <div><h3>Izotz Cristobal Mota</h3><p class="role">Co-founder · Developer</p><p class="bio">Leads Cycle Timers and Tempo, and the studio's shared foundations.</p></div>
      </div>
      <div class="person">
        <div class="initials b" aria-hidden="true">SS</div>
        <div><h3>Sendoa Sola</h3><p class="role">Co-founder · Developer</p><p class="bio">Leads Drip, Anchor, Kover and Tandem.</p></div>
      </div>
      <p class="studio-note">We are not an agency and we don't take client work: we make our own apps, ship them ourselves, and stay small enough that the person who wrote the code is the one reading your email.</p>
    </div>
  </section>

  <section class="shell" id="contact" aria-labelledby="contact-title">
    <div class="contact">
      <div><p class="eyebrow">Contact</p><h2 id="contact-title">Say hello.</h2><p class="note" style="margin-top:10px">Questions, ideas, a bug you found — one address, and we read everything.</p></div>
      <a class="button" href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>
    </div>
  </section>
</main>
'''+footer('')
open(os.path.join(SITE,'index.html'),'w').write(index)

# ---------- app pages
for a in APPS:
    shots=''.join(f'<figure><div class="phone"><img src="../assets/shots/{f}" alt="{a["name"]} screenshot: {cap}" loading="lazy" width="552" height="1200"></div><figcaption>{cap}</figcaption></figure>' for f,cap in a['shots'])
    feats=''.join(f'<div class="feature"><span class="num">{n}</span><h3>{t}</h3><p>{p}</p></div>' for n,t,p in a['features'])
    extra=f'<p class="note" style="margin-top:20px">{a["extra"]}</p>' if a.get('extra') else ''
    page=head(f'{a["name"]} — Seize Apps', a['one'].replace('"','&quot;'), '../', f'apps/{a["slug"]}.html')+header('../','apps')+f'''<main>
  <section class="app-hero shell" aria-labelledby="app-title">
    <div class="app-hero-copy">
      <img class="icon" src="../assets/icons/{a['icon']}" alt="" width="96" height="96">
      <p class="eyebrow">Seize Apps · iOS</p>
      <h1 id="app-title">{a['name']}</h1>
      <p class="lede">{a['lede']}</p>
      <div class="app-meta">{''.join(f'<span>{m}</span>' for m in a['meta'])}</div>
      <!-- App Store badge: remove `hidden` and set the href when the app is live (see README). -->
      <a class="store-badge button" href="#" hidden>Download on the App Store</a>
      {extra}
    </div>
  </section>
  <section class="shell" aria-label="Screenshots"><div class="shots shots-{len(a['shots'])}">{shots}</div></section>

  <section class="section shell" aria-labelledby="what-title">
    <div class="section-head">
      <div><p class="eyebrow">What it does</p><h2 id="what-title">One job, <span>done well.</span></h2></div>
    </div>
    <div class="features">{feats}</div>
  </section>

  <section class="shell" aria-labelledby="privacy-title">
    <div class="privacy-box">
      <div><p class="eyebrow">Privacy</p><h3 id="privacy-title" style="margin-bottom:10px">Yours, not ours.</h3><p>{a['privacy']}</p><p class="note" style="margin-top:14px">Published on the App Store by {a['lead']} · Seize Apps.</p></div>
      <div class="links"><a class="button ghost" href="../privacy.html#{a['privacy_id']}">Privacy policy</a><a class="button ghost" href="mailto:hello@seizeapps.com?subject={a['name']}">Contact</a></div>
    </div>
  </section>
</main>
'''+footer('../')
    open(os.path.join(SITE,'apps',f'{a["slug"]}.html'),'w').write(page)
print('ok', len(APPS), 'apps')
