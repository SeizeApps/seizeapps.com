"""Cycle Timers' own pages: /cycle/privacy, /cycle/terms and /cycle/support (English).

Stand-alone on purpose (22/10/2026): no studio chrome, no links to other apps, no shared site.css.
Its own small stylesheet in Cycle's green/teal (#0E7C6B light / #3CC9AE dark; 22/10/2026, replaced the raspberry). Contrast: accent 5.1:1 on white, 4.72:1 on the summary tint, 9.0:1 and 8.1:1 in dark, light and dark.
Facts checked against SeizeRepo PR #122 (feat/cycle-jp-cleaning @ 31946ce16): App Group storage
(UserDefaults + completion-log.jsonl), no iCloud/CloudKit entitlement, RevenueCat in observer mode
(purchasesAreCompletedBy: .myApp), PrivacyInfo.xcprivacy = Device ID + Purchase History, feedback by
mailto, Cycle Pro = non-consumable com.seizeapps.cycle.pro.lifetime, freeTimerCap = 4.
Run alone (`python3 tools/gen_legal_cycle.py`) or through `python3 tools/gen_site.py`.
"""
import os

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://seizeapps.com/cycle/'
EMAIL = 'hello@seizeapps.com'
APP_STORE = 'https://apps.apple.com/app/id6796827400'
UPDATED = 'October 22, 2026'
MAIL = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'

CSS = '''
:root{--accent:#0E7C6B;--bg:#FFFFFF;--fg:#1C1B1F;--muted:#5F5A63;--line:#ECE6EA;--soft:#EFF8F6;color-scheme:light dark}
@media (prefers-color-scheme:dark){:root{--accent:#3CC9AE;--bg:#141215;--fg:#F3EFF2;--muted:#B4ACB2;--line:#2E2A2E;--soft:#14201D}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.6 -apple-system,BlinkMacSystemFont,"Helvetica Neue",Helvetica,Arial,sans-serif}
.wrap{max-width:720px;margin:0 auto;padding:0 20px}
header{border-bottom:1px solid var(--line)}
header .wrap{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:8px 16px;padding-top:14px;padding-bottom:14px}
.brand{display:flex;align-items:center;gap:10px;font-weight:700;font-size:18px;color:var(--fg);text-decoration:none}
.brand img{width:32px;height:32px;border-radius:8px}
nav a{color:var(--muted);text-decoration:none;margin-left:16px;font-size:15px}
nav a:first-child{margin-left:0}
nav a[aria-current=page]{color:var(--accent);font-weight:600}
main{padding:32px 0 48px}
h1{font-size:32px;line-height:1.2;margin:0 0 4px}
h2{font-size:20px;margin:32px 0 8px}
h3{font-size:17px;margin:20px 0 4px}
p,li{margin:0 0 12px}
ul{padding-left:22px}
a{color:var(--accent)}
.updated{color:var(--muted);font-size:15px;margin-bottom:24px}
.summary{background:var(--soft);border-left:4px solid var(--accent);border-radius:8px;padding:14px 16px;margin:0 0 8px}
.contact{font-size:20px;font-weight:600}
footer{border-top:1px solid var(--line);color:var(--muted);font-size:14px}
footer .wrap{padding-top:20px;padding-bottom:32px}
footer a{color:var(--muted)}
'''

PAGES = [('privacy', 'Privacy'), ('terms', 'Terms'), ('support', 'Support')]


def page(slug, title, desc, body):
    nav = ''.join(f'<a href="{s}.html"{" aria-current=page" if s == slug else ""}>{label}</a>' for s, label in PAGES)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}{slug}.html">
<meta name="theme-color" content="#0E7C6B" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#141215" media="(prefers-color-scheme: dark)">
<link rel="icon" href="../assets/icons/cycle-timers.png">
<link rel="apple-touch-icon" href="../assets/icons/cycle-timers.png">
<style>{CSS}</style>
</head>
<body>
<header><div class="wrap">
<a class="brand" href="{APP_STORE}"><img src="../assets/icons/cycle-timers.png" alt="" width="32" height="32">Cycle Timers</a>
<nav aria-label="Cycle Timers">{nav}</nav>
</div></header>
<main><div class="wrap">
{body}
</div></main>
<footer><div class="wrap">
<p>Cycle Timers by Izotz Cristobal Mota · Basque Country, Spain · {MAIL}</p>
<p><a href="privacy.html">Privacy Policy</a> · <a href="terms.html">Terms of Use</a> · <a href="support.html">Support</a> · <a href="{APP_STORE}">Cycle Timers on the App Store</a></p>
</div></footer>
</body>
</html>
'''


PRIVACY = f'''
<h1>Privacy Policy</h1>
<p class="updated">Last updated: {UPDATED}</p>
<p class="summary"><strong>The short version:</strong> Cycle Timers keeps your tasks on your iPhone or iPad. There is no account, no advertising and no tracking, and your tasks, history and notes are never sent to us. The one thing that leaves your device is purchase bookkeeping: RevenueCat, our processor, receives an anonymous ID, your device's vendor identifier and your Cycle Timers App Store purchases. If you write to us, you do it from your own mail app.</p>

<h2>Who is responsible</h2>
<p>Cycle Timers ("Cycle") is published on the App Store by <strong>Izotz Cristobal Mota</strong>, Basque Country, Spain, who is the data controller for the app ("we", "us"). Contact for anything about your data: {MAIL}.</p>

<h2>Your tasks stay on your device</h2>
<p>Your tasks (name, icon, place and schedule), their completion history and any notes you add, and your settings are stored on your device, in a private App Group container shared only with Cycle's own Home Screen and Lock Screen widgets, so a widget can show your tasks and mark one done. Cycle does not sync them through iCloud and has no server of its own that receives them: we cannot see them. Completion history older than three years is removed automatically on the device. Deleting Cycle deletes this data. Like any app's data, it can be included in your device backup (iCloud Backup or a computer backup) if you have backups turned on; those backups are between you and Apple.</p>

<h2>No account, no ads, no tracking</h2>
<p>Cycle has no account system, contains no advertising or analytics SDK, and does not track you across apps or websites. Its only third-party library is RevenueCat's, used for purchase bookkeeping as described below.</p>

<h2>Purchases</h2>
<p>Cycle is free to start. Cycle Pro is an optional one-time in-app purchase (not a subscription) processed entirely by Apple through the App Store. Cycle checks your purchase with Apple's StoreKit on the device, and Restore Purchase asks Apple again. If you bought Cycle when it was a paid app (before version 0.0.20), Apple's record of that download unlocks Pro too. We never receive your name, email or payment details from a purchase.</p>

<h2>Purchase bookkeeping (RevenueCat)</h2>
<p>Cycle includes RevenueCat's library in "observer" mode: Apple's StoreKit still handles every purchase, and Cycle decides on the device whether Pro is active. When Cycle runs, the library creates a random anonymous ID for your install and sends RevenueCat, Inc. (United States) that ID, your device's vendor identifier (a number Apple gives the apps of one developer on one device; it is not the advertising identifier) and your App Store purchases of Cycle (product, price, dates and Apple's transaction data), together with the technical details the library sends with each request, such as app and iOS version, device model, language and App Store country. Like any server, RevenueCat also sees the internet address of each request. We use this only to keep a record of purchases and count them. Cycle never gives RevenueCat your tasks, history, notes, name or email, and we do not enable any advertising integration: it is not used to track you. From version 0.0.23, what you do on the Cycle Pro screen stays on your device.</p>
<p>RevenueCat is our processor and keeps this data on Amazon Web Services in the United States, under a data processing addendum that makes the EU standard contractual clauses available for that transfer. It states no fixed retention period, and deleting Cycle does not delete what it already holds: write to {MAIL} and we will ask it to delete the record. RevenueCat's own policy is at <a href="https://www.revenuecat.com/privacy" rel="noopener">revenuecat.com/privacy</a>.</p>

<h2>Writing to us</h2>
<p>Send Feedback, and Message the developer in Cycle Pro, open a draft in your own mail app addressed to {EMAIL}. The draft includes what you write and, at the end, your Cycle version and build, iOS version, device model and language, so you can read or remove them before sending. Nothing is sent unless you send it from your mail app. We use your email only to read and answer it.</p>

<h2>Notifications and app badge</h2>
<p>If you allow notifications, Cycle schedules local reminders on your device when a task comes due. The optional app badge with the overdue count is also worked out on the device. Nothing about them is sent to a server.</p>

<h2>Photos, Siri and Shortcuts</h2>
<p>If you save your Cycle Wrapped card, Cycle asks for add-only access to Photos: it can add the image but cannot read your library. Sharing uses the iOS share sheet, and what you share and with whom is your choice. If you use Siri or Shortcuts to mark a task done, Apple handles the request under its own privacy policy; Cycle only acts on the task on your device.</p>

<h2>Children</h2>
<p>Cycle does not ask anyone, including children, for personal information such as a name or email address.</p>

<h2>Your rights</h2>
<p>Under the GDPR you can ask for access to, correction or deletion of personal data, object to its use, or ask for a copy. Cycle keeps your tasks only on your device, so they leave with the app when you delete it. For what RevenueCat holds for us, or for an email you sent, write to {MAIL}. The legal basis for the purchase records is the performance of the purchase and our legitimate interest in keeping track of sales. You can also complain to the Spanish Data Protection Agency (<a href="https://www.aepd.es" rel="noopener">aepd.es</a>).</p>

<h2>Changes</h2>
<p>If this policy changes, the new version will be published on this page with a new date.</p>

<h2>Contact</h2>
<p>{MAIL}</p>
'''

TERMS = f'''
<h1>Terms of Use</h1>
<p class="updated">Effective {UPDATED}</p>

<h2>1. Agreement</h2>
<p>These terms govern your use of Cycle Timers ("Cycle"), published on the App Store by Izotz Cristobal Mota, Basque Country, Spain ("we", "us"). By downloading or using Cycle you agree to these terms and to Apple's standard <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/" rel="noopener">Licensed Application End User License Agreement</a>, which applies to anything these terms don't cover.</p>

<h2>2. License</h2>
<p>We grant you a personal, non-exclusive, non-transferable license to use Cycle on Apple devices that you own or control, as permitted by the App Store terms. The app, its design and its code remain ours.</p>

<h2>3. Cycle Pro</h2>
<p>Cycle is free to use with up to 4 tasks and the Small Home Screen widget. Cycle Pro is an optional one-time in-app purchase, not a subscription, billed by Apple at the price shown in the App Store before you confirm. It unlocks unlimited tasks, the larger and Lock Screen widgets, Cycle Wrapped and Message the developer. You can restore it on your other devices with the same Apple Account from Settings → Restore Purchase. Refunds are handled by Apple under the App Store's policies; we can't issue refunds directly.</p>

<h2>4. Your content stays yours</h2>
<p>The tasks, history and notes you create in Cycle are yours. As our <a href="privacy.html">Privacy Policy</a> explains, they are stored on your device and we have no access to them, which also means you are responsible for your own backups. Deleting Cycle deletes its data on that device.</p>

<h2>5. Reminders</h2>
<p>Cycle is an organizational tool. Reminders are local notifications delivered by iOS, and they depend on your device's settings (such as notification permissions and Focus modes). Don't rely on Cycle alone for anything where a missed reminder could cause harm, such as medication or safety checks.</p>

<h2>6. Acceptable use</h2>
<p>Don't reverse-engineer, resell or misuse Cycle, and don't use it in any way that breaks the law or Apple's terms.</p>

<h2>7. Warranty and liability</h2>
<p>Cycle is provided "as is", without warranties of any kind. To the maximum extent permitted by law, we are not liable for indirect or consequential damages arising from your use of Cycle, and our total liability is limited to the amount you paid for Cycle in the twelve months before the claim. Nothing in these terms limits rights that consumer law grants you and that cannot be waived.</p>

<h2>8. Changes</h2>
<p>We may update these terms as Cycle evolves; the current version always lives at this address with its effective date above. Continued use after a change means you accept the updated terms.</p>

<h2>9. Governing law</h2>
<p>These terms are governed by the laws of Spain. Consumers in the EU also keep the protections of their country of residence.</p>

<h2>Contact</h2>
<p>{MAIL}</p>
'''

SUPPORT = f'''
<h1>Support</h1>
<p class="updated">Cycle Timers: know when you last did it, and when it's due again.</p>

<h2>Contact</h2>
<p class="contact">{MAIL}</p>
<p>The quickest way is Settings → Send Feedback in the app: it opens an email with your Cycle version, iOS version and device model already filled in, so we can help faster.</p>

<h2>Common questions</h2>

<h3>How many tasks can I track for free?</h3>
<p>Up to 4 tasks, with the Small Home Screen widget. Cycle Pro, a one-time purchase with no subscription, unlocks unlimited tasks, Medium and Large widgets (plus Extra Large on iPad), Lock Screen widgets, Cycle Wrapped and Message the developer.</p>

<h3>I bought Cycle Pro. How do I get it on a new device?</h3>
<p>Sign in with the same Apple Account, open Cycle, then Settings → Restore Purchase.</p>

<h3>I paid for Cycle when it was a paid app.</h3>
<p>If you bought Cycle before version 0.0.20, Pro is already yours. Update to the latest version; if Pro doesn't show as unlocked, tap Settings → Restore Purchase.</p>

<h3>How do I get a refund?</h3>
<p>Purchases are handled by Apple. Request a refund at <a href="https://reportaproblem.apple.com" rel="noopener">reportaproblem.apple.com</a>.</p>

<h3>My reminders don't arrive.</h3>
<p>Check Settings → Notifications in Cycle, then the iPhone's Settings → Notifications → Cycle, and any Focus mode that might be silencing it. A paused task doesn't send reminders.</p>

<h3>How do I add a widget?</h3>
<p>Touch and hold an empty area of the Home Screen, tap Edit → Add Widget, and choose Cycle. Tap a ring on the widget to mark that task done without opening the app.</p>

<h3>Where is my data? Is it backed up?</h3>
<p>Your tasks stay on your device; Cycle doesn't sync them through iCloud and never sends them to us. They are included in your device backup if you have one turned on. See the <a href="privacy.html">Privacy Policy</a>.</p>

<h3>How do I delete my data?</h3>
<p>Delete a task from the app, or delete Cycle to remove everything it stores on that device. To ask RevenueCat, our purchase processor, to delete its purchase record, write to {MAIL}.</p>
'''


def build_cycle():
    out = os.path.join(SITE, 'cycle')
    os.makedirs(out, exist_ok=True)
    pages = {
        'privacy': ('Cycle Timers · Privacy Policy',
                    'Cycle Timers privacy: your tasks stay on your device. No account, no ads, no tracking.', PRIVACY),
        'terms': ('Cycle Timers · Terms of Use', 'Terms of use for Cycle Timers.', TERMS),
        'support': ('Cycle Timers · Support', 'Help and contact for Cycle Timers.', SUPPORT),
    }
    for slug, (title, desc, body) in pages.items():
        with open(os.path.join(out, f'{slug}.html'), 'w', encoding='utf-8') as f:
            f.write(page(slug, title, desc, body.strip()))


if __name__ == '__main__':
    build_cycle()
