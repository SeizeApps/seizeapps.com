"""Roomy's privacy page (/roomy/privacy/), English only like the app.

Ported from a hand-made page (4a9a712) into a generator on 05/10/2026; the text is unchanged.
Built with gen_site's chrome; run `python3 tools/gen_site.py`, which calls build_roomy().
"""
from gen_site import head, header, footer, write, legal_main

TITLE = 'Roomy privacy — Seize Apps'
DESC = 'Roomy privacy: photos stay on your iPhone. No accounts, no ads, no tracking. From version 0.0.3, purchase analytics through RevenueCat.'

BODY = '''

  <p class="eyebrow">Roomy · Legal</p>
  <h1>Roomy privacy</h1>
  <p class="effective">Last updated: October 2026</p>
  <p><strong>The short version:</strong> Roomy analyzes your photo library on your iPhone only: your photos, videos and their metadata are never uploaded, shared or sold. No accounts, no ads, no tracking. From version 0.0.3, Roomy also reports your purchases to RevenueCat, our processor, for purchase analytics (see Purchase analytics below). Versions before 0.0.3 do not contain that library and collect no data.</p>

  <h2>Who is responsible</h2>
  <p>Roomy is published on the App Store by <strong>Izotz Cristobal Mota</strong> (Seize Apps, Basque Country, Spain), the data controller. Contact for anything about your data: <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</p>

  <h2>Your photos stay on your iPhone</h2>
  <p>Roomy analyzes your photo library entirely on your device to help you find photos and videos to remove. Your photos, videos and their metadata are never uploaded, shared or sold, and Roomy never gives them to RevenueCat or to anyone else. If a photo or video is in iCloud Photos and not on the phone, iOS downloads it from your iCloud when Roomy needs to show or compress it; that transfer is between your iPhone and Apple.</p>

  <h2>No accounts, no ads, no tracking</h2>
  <p>Roomy does not require an account, does not use advertising SDKs, and does not track you across apps or websites. Its one third-party library, RevenueCat's, is used for purchase analytics only (see below).</p>

  <h2>Data stored on your device</h2>
  <p>Roomy stores your review progress (which items you kept or marked for deletion), cleanup statistics and your preferences locally on your iPhone. Deleting the app removes this data.</p>

  <h2>Purchases</h2>
  <p>Subscriptions and purchases are processed by Apple through the App Store. Roomy never sees your payment information. Apple's StoreKit still handles every purchase, and Roomy still decides on your iPhone whether Roomy Pro is active.</p>

  <h2>Purchase analytics (RevenueCat)</h2>
  <p>From version 0.0.3, Roomy includes RevenueCat's software library, used for analytics only: Apple's StoreKit still handles every purchase and Roomy still decides on your iPhone whether Roomy Pro is active. Whenever Roomy is open, the library gives your install a random anonymous ID and sends RevenueCat, Inc. (United States) that ID, your iPhone's vendor identifier (a number Apple gives the apps of one developer on a device; it is not the advertising identifier), your App Store purchases and subscription status (product, price, dates and Apple's transaction data), the time you last used Roomy, your iPhone model, iOS and app version, language and App Store country. When the Roomy Pro screen opens, Roomy also tells it which situation opened it (the onboarding, the daily swipe limit, one-tap cleanup, video compression or the upgrade button in Settings), which plan you chose and how a purchase or restore ended (bought, cancelled, pending, failed or restored). Like any server, RevenueCat also sees the internet address of each request. We use it to count subscribers, trials and renewals and to see how people move through the purchase screen. Roomy never gives RevenueCat your photos, videos or their metadata, what you kept or deleted, your name or your email, and we do not enable its advertising integrations: it is not used to track you. RevenueCat is our processor; it keeps this data on Amazon Web Services in the United States, under a data processing addendum that makes the EU standard contractual clauses available for that transfer. It states no fixed retention period, and deleting Roomy does not delete what it already holds: write to <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a> and we will ask it to delete the record. Versions of Roomy before 0.0.3 do not contain this library and send nothing to RevenueCat. RevenueCat's own policy is at <a href="https://www.revenuecat.com/privacy" rel="noopener">revenuecat.com/privacy</a>.</p>
  <!-- CONFIRM: RevenueCat's addendum makes the EU standard contractual clauses available (revenuecat.com/dpa, read 7 October 2026); a UK transfer mechanism, a fixed retention period for end-user data, our acceptance of the addendum for Roomy's RevenueCat project and how to find one install's record on request are not visible in this repo. Same open items as Tempo and Atino. -->

  <h2>Emails and notifications</h2>
  <p>The email drafts the app opens (Suggest a Feature, Report a Bug, and Contact Support when the purchase screen cannot load its plans) go to hello@seizeapps.com only if you send them. Report a Bug and Contact Support fill in your app version, iOS version and iPhone model (Contact Support also your App Store country); you can read and change the draft first.</p>
  <p>If you turn on daily reminders, Roomy schedules local notifications on your device. No data is sent to a server.</p>

  <h2>Children</h2>
  <p>Roomy does not ask for personal information such as your name or email, from anyone, including children. The purchase analytics above is an anonymous install ID with purchase and screen events, not an account.</p>

  <h2>Your rights</h2>
  <p>Roomy has no account and keeps no records of its own on a server. The only data about you that Roomy sends off your iPhone is what RevenueCat holds for us (see Purchase analytics): to ask for access, correction or deletion, write to <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a> and we will pass it on to RevenueCat. Everything else leaves with the app when you delete it. You can also complain to the Spanish Data Protection Agency (<a href="https://www.aepd.es" rel="noopener">aepd.es</a>).</p>

  <h2>Changes</h2>
  <p>If this policy changes, the updated version will be published on this page and in the app.</p>

  <p class="fineprint">This page is a product privacy notice adapted from Roomy’s in-repo draft for App Store listing. It is not a law-firm opinion; human counsel should review before relying on it for compliance.</p>

'''


def build_roomy():
    path = 'roomy/privacy/'
    root = '../../'
    # English only: one URL, no hreflang; the other languages of the switch go to the general policy.
    alts = {'en': f'https://seizeapps.com/{path}'}
    switch = {'es': f'{root}es/privacy.html', 'fr': f'{root}fr/privacy.html'}
    html = (head('en', TITLE, DESC, root, path, alts=alts) + header('en', root, path, switch=switch)
            + legal_main('en', BODY) + footer('en', root))
    write(f'{path}index.html', html)
