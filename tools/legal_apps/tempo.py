"""Tempo: config for tools/gen_legal_apps.py. Facts: Tempo 1.0.2 (56) at SeizeRepo 5ee88ea7e: local SwiftData store
(cloudKitDatabase: .none), App Group for the widget, no networking code of its own, no third-party SDK and no
RevenueCat in this checkout (verify against the shipping binary before publishing), Core Location + MapKit,
StoreKit 2 subscriptions and a lifetime unlock. Contact is hello@ (the code never uses izotz@)."""
from .common import terms, rights, CHANGES, CONTACT

# Accent #007AFF (AccentColor.colorset, no dark variant). 4.0:1 on white, so light-mode text uses a darker blue
# of the same hue; the dark canvas is the app's #060E1F.
APP = dict(
    slug='tempo', name='Tempo', icon='tempo.png',
    appStoreUrl='https://apps.apple.com/app/id6761499275',
    email='hello@seizeapps.com', publisher='Izotz Cristobal Mota (Seize Apps)',
    updated_en='October 22, 2026',
    theme=dict(
        light=dict(mark='#007AFF', bg='#FFFFFF', fg='#0B1426', muted='#525F78', line='#E1E7F0'),
        dark=dict(mark='#007AFF', bg='#060E1F', fg='#EAF0FA', muted='#A4B2CA', line='#1B2A45'),
    ),
    pages={},
)

PRIVACY = r'''
<h1>Privacy Policy</h1>
<p class="updated">Last updated: @updated@</p>
<p class="summary"><strong>The short version:</strong> Tempo keeps your work history, your zones and your settings on your iPhone. There is no account, no advertising, no analytics and no third-party library in the app, and we run no server that receives your work records or your location. Location is used on your device to recognise arriving at and leaving your zones. Two things reach Apple, not us: the text you type when you search for a place, and the coordinates of your first home and first work zones when Tempo estimates your commute distance.</p>

<h2>Who is responsible</h2>
<p>Tempo is published on the App Store by <strong>Izotz Cristobal Mota</strong> (Seize Apps), Basque Country, Spain, who is the data controller for the app ("we", "us"). Contact for anything about your data: @mail@.</p>

<h2>What Tempo stores on your iPhone</h2>
<ul>
<li><strong>Work history.</strong> Your sessions are kept in a local database inside the app: the start and end of each working interval, the zone it belongs to, the events and reviews that led to it, and the corrections you make. It is not synced anywhere.</li>
<li><strong>Location evidence.</strong> When Tempo decides whether a session should start, stop or be reviewed, it keeps the evidence for that decision on the iPhone: individual location fixes (latitude, longitude, accuracy and time), the zone concerned, how the fix arose (for example a zone entry or exit) and your permission state at the time. This is evidence around zone checks, not a continuous trail of where you have been.</li>
<li><strong>Zones and settings.</strong> Each home or work zone you create (its name, centre coordinates, radius, type and schedule) and your preferences are stored in the app's settings. A copy of your settings and of the state a widget needs (the current session, its status, today's total and your daily target) is placed in an App Group container shared only with Tempo's own widgets and Live Activity.</li>
<li><strong>Small items.</strong> Onboarding progress, a cached commute distance, a cached copy of whether Pro is active, Focus timer preferences and statistics, a short ledger that limits "Start Tempo?" prompts to one a day (pruned after 14 days), your language choice and the last "What's new" you saw.</li>
<li><strong>Recovery files.</strong> If an update has to migrate an older format of your data, a backup of it is written inside the app, protected until the first unlock after a restart, and removed by "Erase all local data". If the app ever cannot open its database, it can bundle the raw files so that you can save them wherever you choose.</li>
</ul>
<p>Tempo does not use iCloud or CloudKit, so nothing syncs between devices, and it does not use the Keychain. Like any app's data, what is stored on your iPhone can be included in your device backup (iCloud Backup or a computer backup) if you have backups turned on; those backups are between you and Apple. Tempo does not control that.</p>

<h2>Location</h2>
<p>Manual tracking works without any location permission. If you turn on automatic tracking, Tempo asks for location access (first "While Using the App", then "Always") and uses Apple's Core Location on the device to register your zones as geofences, receive entry and exit events and, when needed, take a single fix to verify where you are. Continuous location updates run only while the app is open (for example while the Places map tab is on screen), never in the background. Tempo does not declare background location updates; a background refresh task may run a few minutes before a pending "Start Tempo?" prompt to take a fresh fix and cancel the prompt if you have already left. For a home zone, location never starts, stops or freezes a session by itself: Tempo at most asks one "Start Tempo?" question a day while you are there, and one "You left" question. You control the permission in iOS Settings at any time.</p>
<p>None of this location data is sent to us: Tempo contains no code that sends your work records or coordinates to a server of ours.</p>

<h2>What reaches Apple</h2>
<p>Tempo uses Apple's MapKit for place search and routes, so two things leave the app for Apple's servers, under Apple's privacy terms and not ours: the text you type in the zone search bar, and, to compute a one-way driving distance for the "Commute Saved" card, the centre coordinates of your first home zone and first work zone. The result is cached on your iPhone. Saying that we do not collect your location does not mean that Apple's platform services never process it; how long Apple keeps such requests is set by Apple and we cannot see it. Apple also processes your purchases (see below).</p>

<h2>No account, no ads, no analytics, no third-party library</h2>
<p>Tempo has no account or sign-in, shows no advertising, does not ask for tracking permission and does not track you across apps or websites. It contains no analytics, crash-reporting or advertising library, and no third-party software library at all; its privacy manifest declares no tracking and no collected data. Diagnostics stay on your iPhone: system log entries and an on-screen tracking-diagnostics view. Tempo makes no calls to any AI service.</p>

<h2>Notifications, widgets and Siri</h2>
<p>Notifications are local only: Tempo schedules them on your iPhone and does not use push notifications or a push server. They can include leave-soon and overtime alerts, "Start Tempo?" and "You left" questions (with the zone name and your usual start time), end-of-day and review notices and Focus timer endings, with action buttons such as Start or End Session. Tempo's widgets, Live Activity and Control read their data from the shared App Group container and have no network or location access of their own. If you use Siri or Shortcuts, Tempo's App Intents let you ask for your hours or start and stop a session; Apple handles the request under its own privacy policy.</p>

<h2>Photos and sharing</h2>
<p>If you tap Save on a Wrapped share card (a Pro feature), Tempo asks for add-only access to Photos: it can add the image but cannot read your library. Sharing a card uses the iOS share sheet or the clipboard, and where it goes is your choice. "Export all data" writes a JSON file of your records, readable records, raw recovery material, settings and zones included, to a location you pick; it is free and nothing is sent anywhere.</p>

<h2>Purchases</h2>
<p>Tempo is free to start. Tempo Pro is sold through the App Store as a monthly or yearly subscription or as a one-time lifetime purchase. Apple processes the payment and any renewal; Tempo checks your purchases with Apple's StoreKit on the device, caches only whether Pro is active, and can restore purchases from Apple. We never receive your name, email or payment details from a purchase. We see aggregated, anonymous sales and download statistics from App Store Connect.</p>

<h2>Writing to us</h2>
<p>Suggest a Feature, Report a Bug and the startup "Contact Tempo support" button open a draft in your own mail app addressed to @email@. The bug report fills in the Tempo version, iOS version and device model, and you can read and change the draft first. Nothing is sent unless you send it, and we use your email only to read and answer it.</p>

<h2>Deleting your data and how long we keep it</h2>
<p>All of Tempo's data is on your iPhone and stays until you change or delete it: you can correct or delete sessions, delete a zone, use <em>Settings › Data &amp; privacy › Erase all local data</em> (which also removes Tempo's notifications and ends the Live Activity), reset all settings, or delete the app. We hold no copy and there is no account to delete. Tempo does not apply an automatic expiry to location evidence stored with your sessions, so it stays until you erase it.</p>

<h2>Children</h2>
<p>Tempo is not directed to children under 13 and is not in the App Store's Kids Category. It does not ask anyone for a name or email address.</p>

@rights@

<h2>Changes</h2>
<p>If this policy changes, the new version will be published on this page with a new date. If a later version of Tempo adds a third-party library or a server, this page will be updated before it ships.</p>

<h2>Contact</h2>
<p>@mail@</p>
'''.replace('@rights@', rights(
    'Tempo keeps your records only on your device, so they leave with the app when you delete it, and we hold no personal data about you to produce.',
    'Apart from an email you send us, we process no personal data about you. '))

TERMS = terms('Tempo', 'Tempo', 'Izotz Cristobal Mota (Seize Apps)', [
    ('Tempo Pro',
     '<p>Tempo is free to use for manual and automatic tracking, corrections, JSON export and erasing your data. Tempo Pro is optional and unlocks additional features such as the Dayline and Cards home styles, custom start schedules and finish-at-target, Focus cycles and saving share cards to Photos. It is sold as an auto-renewing monthly or yearly subscription (the App Store may offer a free introductory period to new subscribers; its terms are shown before you confirm) or as a one-time lifetime purchase that does not renew. The price is shown by the App Store before you confirm.</p>'
     '<p>Subscriptions are charged to your Apple Account at confirmation and renew automatically unless you cancel at least 24 hours before the end of the current period. Manage or cancel them in your Apple Account\'s subscription settings. Restore Purchases is always available on the Tempo Pro screen. Purchases are processed by Apple, and refunds are handled by Apple under the App Store\'s policies: we can\'t issue refunds directly.</p>'),
    ('Your data stays yours',
     '<p>Your work history, zones and settings are stored on your device. As our <a href="@privacy@">Privacy Policy</a> explains, we have no access to them, which also means you are responsible for your own backups. You can export everything as a JSON file at any time, and delete it with Erase all local data.</p>'),
    ('Automatic tracking is best-effort',
     '<p>Automatic tracking depends on iOS: region events can be delayed or unavailable because of signal, interference, reduced location accuracy, changed permissions, system limits, a restart or force-quitting the app, and Tempo can\'t guarantee that a session starts or stops at the right moment. Tempo is a personal time-tracking tool, not an employer\'s timekeeping system. Check your records yourself and correct them before you rely on them for payroll, billing, legal or employment purposes.</p>'),
    ('Acceptable use',
     '<p>Don\'t reverse-engineer, resell or misuse Tempo, and don\'t use it in any way that breaks the law or Apple\'s terms.</p>'),
])

SUPPORT = r'''
<h1>Support</h1>
<p class="updated">Tempo: your working hours, tracked for you.</p>

<h2>Contact</h2>
<p class="contact">@mail@</p>
<p>The quickest way is the Report a Bug row at the bottom of Settings in the app: it opens an email with your Tempo version, iOS version and device model already filled in, so we can help faster.</p>

<h2>Common questions</h2>

<h3>Tempo didn't start or stop a session by itself.</h3>
<p>Automatic tracking relies on location events from iOS. Check Settings › Privacy &amp; Security › Location Services › Tempo: choose Always and keep Precise Location on, and make sure Background App Refresh is allowed. iOS can delay region events, and force-quitting the app can stop them. Manual tracking always works without location, and you can correct any session afterwards.</p>

<h3>How do I correct a session?</h3>
<p>Open the session in Tempo and edit it. Corrections are kept with the session on your iPhone.</p>

<h3>Why does a home zone only ask me a question?</h3>
<p>For a home zone, Tempo never starts or stops a session on its own. It asks one "Start Tempo?" question a day while you are there, and one "You left" question when you go.</p>

<h3>How do I restore Tempo Pro on a new device?</h3>
<p>Sign in with the same Apple Account, open the Tempo Pro screen and tap Restore Purchases.</p>

<h3>How do I cancel my subscription or get a refund?</h3>
<p>Subscriptions are managed by Apple: open <a href="https://apps.apple.com/account/subscriptions" rel="noopener">your Apple Account's subscriptions</a>. Request a refund at <a href="https://reportaproblem.apple.com" rel="noopener">reportaproblem.apple.com</a>.</p>

<h3>Where is my data? Can I export it?</h3>
<p>Your work history, zones and settings stay on your iPhone and are never sent to us; Tempo does not sync through iCloud. Settings › Data &amp; privacy › Export all data saves a JSON file to a place you choose. See the <a href="@privacy@">Privacy Policy</a>.</p>

<h3>How do I delete my data?</h3>
<p>Settings › Data &amp; privacy › Erase all local data removes your sessions, zones, notifications and widget data from the device, or delete the app. There is no account and nothing on a server to delete.</p>
'''

APP['pages'] = {
    ('en', 'privacy'): dict(title='Tempo · Privacy Policy',
                            desc='Tempo privacy: your work history and zones stay on your iPhone. No account, no ads, no analytics, no third-party library.', body=PRIVACY),
    ('en', 'terms'): dict(title='Tempo · Terms of Use', desc='Terms of use for Tempo.', body=TERMS),
    ('en', 'support'): dict(title='Tempo · Support', desc='Help and contact for Tempo.', body=SUPPORT),
}
