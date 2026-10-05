"""Roomy's privacy page (/roomy/privacy/), English only like the app.

Ported from a hand-made page (4a9a712) into a generator on 05/10/2026; the text is unchanged.
Built with gen_site's chrome; run `python3 tools/gen_site.py`, which calls build_roomy().
"""
from gen_site import head, header, footer, write

TITLE = 'Roomy privacy — Seize Apps'
DESC = 'Roomy privacy: photos stay on your iPhone. No accounts, no tracking, no personal data collected.'

BODY = '''

  <p class="eyebrow">Roomy · Legal</p>
  <h1>Roomy privacy</h1>
  <p class="effective">Last updated: September 2026</p>
  <p><strong>The short version:</strong> Roomy analyzes your photo library on your iPhone only. No accounts, no analytics, no ads, no personal data collected. App Store privacy label: Data Not Collected.</p>

  <h2>Who is responsible</h2>
  <p>Roomy is published on the App Store by <strong>Izotz Cristobal Mota</strong> (Seize Apps, Basque Country, Spain), the data controller. Contact for anything about your data: <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</p>

  <h2>Your photos stay on your iPhone</h2>
  <p>Roomy analyzes your photo library entirely on your device to help you find photos and videos to remove. Your photos, videos and their metadata are never uploaded, shared or sold.</p>

  <h2>No accounts, no tracking</h2>
  <p>Roomy does not require an account, does not use analytics or advertising SDKs, and does not track you across apps or websites. Roomy does not collect any personal data.</p>

  <h2>Data stored on your device</h2>
  <p>Roomy stores your review progress (which items you kept or marked for deletion), cleanup statistics and your preferences locally on your iPhone. Deleting the app removes this data.</p>

  <h2>Purchases</h2>
  <p>Subscriptions and purchases are processed by Apple through the App Store. Roomy never sees your payment information.</p>

  <h2>Notifications</h2>
  <p>If you turn on daily reminders, Roomy schedules local notifications on your device. No data is sent to a server.</p>

  <h2>Children</h2>
  <p>Roomy does not knowingly collect any personal information from anyone, including children.</p>

  <h2>Your rights</h2>
  <p>Because Roomy does not collect personal data, there is nothing for us to access or erase on a server. Local data leaves with the app when you delete it. Questions: <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>. You can also complain to the Spanish Data Protection Agency (<a href="https://www.aepd.es" rel="noopener">aepd.es</a>).</p>

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
            + f'<main class="shell legal">\n{BODY}\n</main>\n' + footer('en', root))
    write(f'{path}index.html', html)
