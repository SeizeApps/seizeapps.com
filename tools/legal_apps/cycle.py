"""Cycle Timers: config for tools/gen_legal_apps.py. Facts verified against the app's code at HEAD 252e1c78d
(0.0.23 build 30): App Group storage, no iCloud/CloudKit, RevenueCat in observer mode, PrivacyInfo = Device ID +
Purchase History, feedback by mailto, Cycle Pro = com.seizeapps.cycle.pro.lifetime, freeTimerCap = 4."""

APP = dict(
    slug='cycle', name='Cycle Timers', icon='cycle-timers.png',
    appStoreUrl='https://apps.apple.com/app/id6796827400',
    live=True,
    email='hello@seizeapps.com', publisher='Izotz Cristobal Mota',
    updated_en='October 22, 2026',
    # Teal, from the app's AccentColor (#0E7C6B light / #3CC9AE dark). Both pass 4.5:1 as text, so no adjustment.
    theme=dict(
        light=dict(mark='#0E7C6B', bg='#FFFFFF', fg='#1C1B1F', muted='#5F5A63', line='#ECE6EA', soft='#EFF8F6'),
        dark=dict(mark='#3CC9AE', bg='#141215', fg='#F3EFF2', muted='#B4ACB2', line='#2E2A2E', soft='#14201D'),
    ),
    pages={},
)

PRIVACY = r'''
<h1>Privacy Policy</h1>
<p class="updated">Last updated: @updated@</p>
<p class="summary"><strong>The short version:</strong> Cycle Timers keeps your tasks on your iPhone or iPad. There is no account, no advertising and no tracking, and your tasks, history and notes are never sent to us. The one thing that leaves your device is purchase bookkeeping: RevenueCat, our processor, receives an anonymous ID, your device's vendor identifier and your Cycle Timers App Store purchases. From version 0.0.23, if you write to us, you do it from your own mail app (see Writing to us for earlier versions).</p>

<h2>Who is responsible</h2>
<p>Cycle Timers ("Cycle") is published on the App Store by <strong>Izotz Cristobal Mota</strong>, Basque Country, Spain, who is the data controller for the app ("we", "us"). Contact for anything about your data: @mail@.</p>

<h2>Your tasks stay on your device</h2>
<p>Your tasks (name, icon, place and schedule), their completion history and any notes you add, and your settings are stored on your device, in a private App Group container shared only with Cycle's own Home Screen and Lock Screen widgets, so a widget can show your tasks and mark one done. Cycle does not use iCloud or CloudKit, so nothing syncs between devices, and it has no server of its own that receives your tasks: we cannot see them. Cycle makes no calls to any AI service. Completion history older than three years is removed automatically on the device. Deleting Cycle deletes this data. Like any app's data, it can be included in your device backup (iCloud Backup or a computer backup) if you have backups turned on; those backups are between you and Apple.</p>

<h2>No account, no ads, no tracking</h2>
<p>Cycle has no account system, contains no advertising or analytics SDK, and does not track you across apps or websites. Its only third-party library is RevenueCat's, used for purchase bookkeeping as described below. From version 0.0.23, how you use the Cycle Pro screen (when it opens, which button you tap) is written only to your device's own system log and is never sent anywhere.</p>

<h2>Purchases</h2>
<p>Cycle is free to start. Cycle Pro is an optional one-time in-app purchase (not a subscription) processed entirely by Apple through the App Store. Cycle checks your purchase with Apple's StoreKit on the device, and Restore Purchase asks Apple again. If you bought Cycle when it was a paid app (before version 0.0.20), Apple's record of that download unlocks Pro too. We never receive your name, email or payment details from a purchase.</p>

<h2>Purchase bookkeeping (RevenueCat)</h2>
<p>Cycle includes RevenueCat's library in "observer" mode: Apple's StoreKit still handles every purchase, and Cycle decides on the device whether Pro is active. When Cycle runs, the library creates a random anonymous ID for your install and sends RevenueCat, Inc. (United States) that ID, your device's vendor identifier (a number Apple gives the apps of one developer on one device; it is not the advertising identifier) and your App Store purchases of Cycle (product, price, dates and Apple's transaction data), together with the technical details the library sends with each request, such as app and iOS version, device model, language and App Store country. Like any server, RevenueCat also sees the internet address of each request. We use this only to keep a record of purchases and count them. Cycle never gives RevenueCat your tasks, history, notes, name or email, and we do not enable any advertising integration: it is not used to track you. Up to version 0.0.22, Cycle also told RevenueCat that the Cycle Pro screen opened (and which limit led you there: the timer limit, a widget size or Settings) and whether you tapped Buy, cancelled, were waiting for approval or restored; from version 0.0.23 that stays on your device.</p>
<p>RevenueCat is our processor and is based in the United States. What exactly it collects through its library, where and for how long it keeps it, and how it protects it are set out in its own privacy policy at <a href="https://www.revenuecat.com/privacy" rel="noopener">revenuecat.com/privacy</a>; we cannot see inside its systems and do not promise a retention period for it. Deleting Cycle does not delete what it already holds: write to @mail@ and we will ask it to delete the record.</p>

<h2>Writing to us</h2>
<p>Send Feedback, and Message the developer in Cycle Pro, open a draft in your own mail app addressed to @email@. The draft includes what you write and, at the end, your Cycle version and build, iOS version, device model and language, so you can read or remove them before sending. Nothing is sent unless you send it from your mail app. We use your email only to read and answer it.</p>
<p><strong>Versions up to 0.0.22.</strong> In these versions Message the developer did not open your mail app: after you tapped Send, it sent the text you wrote, the category you picked (idea, problem, love or other), the email address if you chose to leave one, your Cycle version and build, iOS version, device model and language, whether Cycle Pro was active, and a random identifier made for the install (used only to limit spam) to a Seize server (Supabase, our processor) in the EU, in Frankfurt. It is kept for 12 months and then deleted automatically. The text of the message, with the category and whether you have Pro, was also copied to a private Telegram chat that only the developer reads, and is deleted there after one month; the email address and the identifier were never sent there. Write to @mail@ to have a message deleted sooner, and tell us the text or email address you used so we can find it.</p>

<h2>Notifications and app badge</h2>
<p>If you allow notifications, Cycle schedules local reminders on your device when a task comes due. The optional app badge with the overdue count is also worked out on the device. Nothing about them is sent to a server.</p>

<h2>Photos, Siri and Shortcuts</h2>
<p>If you save your Cycle Wrapped card, Cycle asks for add-only access to Photos: it can add the image but cannot read your library. Sharing uses the iOS share sheet, and what you share and with whom is your choice. If you use Siri or Shortcuts to mark a task done, Cycle shares your task names with the system so they can be spoken or chosen in Shortcuts; Apple handles the request under its own privacy policy, and Cycle only acts on the task on your device. Cycle asks for no other permission: no camera, microphone, contacts, calendar or location.</p>

<h2>Children</h2>
<p>Cycle is a household-chores timer and is not directed at children. It does not ask anyone, including children, for personal information such as a name or email address.</p>

<h2>Your rights</h2>
<p>Under the GDPR you can ask for access to, correction or deletion of personal data, object to its use, or ask for a copy. Cycle keeps your tasks only on your device, so they leave with the app when you delete it. For what RevenueCat holds for us, or for an email you sent, write to @mail@. The legal basis for the purchase records is the performance of the purchase and our legitimate interest in keeping track of sales. You can also complain to the Spanish Data Protection Agency (<a href="https://www.aepd.es" rel="noopener">aepd.es</a>).</p>

<h2>Changes</h2>
<p>If this policy changes, the new version will be published on this page with a new date.</p>

<h2>Contact</h2>
<p>@mail@</p>
'''

TERMS = r'''
<h1>Terms of Use</h1>
<p class="updated">Effective @updated@</p>

<h2>1. Agreement</h2>
<p>These terms govern your use of Cycle Timers ("Cycle"), published on the App Store by Izotz Cristobal Mota, Basque Country, Spain ("we", "us"). By downloading or using Cycle you agree to these terms and to Apple's standard <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/" rel="noopener">Licensed Application End User License Agreement</a>, which applies to anything these terms don't cover.</p>

<h2>2. License</h2>
<p>We grant you a personal, non-exclusive, non-transferable license to use Cycle on Apple devices that you own or control, as permitted by the App Store terms. The app, its design and its code remain ours.</p>

<h2>3. Cycle Pro</h2>
<p>Cycle is free to use with up to 4 tasks and the Small Home Screen widget. Cycle Pro is an optional one-time in-app purchase, not a subscription, billed by Apple at the price shown in the App Store before you confirm. It unlocks unlimited tasks, the larger and Lock Screen widgets, Cycle Wrapped and Message the developer. You can restore it on your other devices with the same Apple Account from Settings → Restore Purchase. Refunds are handled by Apple under the App Store's policies; we can't issue refunds directly.</p>

<h2>4. Your content stays yours</h2>
<p>The tasks, history and notes you create in Cycle are yours. As our <a href="@privacy@">Privacy Policy</a> explains, they are stored on your device and we have no access to them, which also means you are responsible for your own backups. Deleting Cycle deletes its data on that device.</p>

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
<p>@mail@</p>
'''

SUPPORT = r'''
<h1>Support</h1>
<p class="updated">Cycle Timers: know when you last did it, and when it's due again.</p>

<h2>Contact</h2>
<p class="contact">@mail@</p>
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
<p>Your tasks stay on your device; Cycle doesn't sync them through iCloud and never sends them to us. They are included in your device backup if you have one turned on. See the <a href="@privacy@">Privacy Policy</a>.</p>

<h3>How do I delete my data?</h3>
<p>Delete a task from the app (you can also delete or edit single entries of its history), or delete Cycle to remove everything it stores on that device. There is no account to delete, and no "erase everything" button. To ask RevenueCat, our purchase processor, to delete its purchase record, write to @mail@.</p>
'''

APP['pages'] = {
    ('en', 'privacy'): dict(title='Cycle Timers · Privacy Policy',
                            desc='Cycle Timers privacy: your tasks stay on your device. No account, no ads, no tracking.', body=PRIVACY),
    ('en', 'terms'): dict(title='Cycle Timers · Terms of Use', desc='Terms of use for Cycle Timers.', body=TERMS),
    ('en', 'support'): dict(title='Cycle Timers · Support', desc='Help and contact for Cycle Timers.', body=SUPPORT),
}
