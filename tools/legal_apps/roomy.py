"""Roomy: config for tools/gen_legal_apps.py (replaces gen_legal_roomy.py). Facts: Roomy 0.0.4 (3) at SeizeRepo
5ee88ea7e: no backend, no accounts, no iCloud/CloudKit, Photos read/write + add-only, local review-state.json,
one local daily reminder, RevenueCat analytics-only, Roomy Pro = yearly (3-day intro), weekly, lifetime.
The old text listed "the onboarding" as a paywall trigger; 0.0.4 has none (triggers: swipe limit, smart cleanup,
compress, Settings)."""
from .common import terms, rights, revenuecat

# Lime #C9E64A (single forced-dark theme in the app). 1.4:1 on white, so light-mode text uses a darker olive of
# the same hue (found by the generator); the declared lime stays on borders and in dark mode.
APP = dict(
    slug='roomy', name='Roomy', icon='roomy.png',
    appStoreUrl='https://apps.apple.com/app/id6817891679',
    email='hello@seizeapps.com', publisher='Izotz Cristobal Mota (Seize Apps)',
    updated_en='October 22, 2026',
    dir_copies=('privacy',),
    theme=dict(
        light=dict(mark='#C9E64A', bg='#FFFFFF', fg='#1E1C17', muted='#5A5748', line='#E9E6D8'),
        dark=dict(mark='#C9E64A', bg='#16120E', fg='#F3F0E6', muted='#B1AC9C', line='#2E2920'),
    ),
    pages={},
)

PRIVACY = r'''
<h1>Roomy privacy</h1>
<p class="updated">Last updated: @updated@</p>
<p class="summary"><strong>The short version:</strong> Roomy looks at your photo library on your iPhone only: your photos, videos and their metadata are never uploaded, shared or sold. There is no account, no advertising, no tracking and no server of ours. The one thing that leaves your iPhone is purchase bookkeeping: RevenueCat, our processor, receives an anonymous ID, your iPhone's vendor identifier, your Roomy purchases and which screen led you to the purchase screen.</p>

<h2>Who is responsible</h2>
<p>Roomy ("Roomy: Swipe Photo Cleaner") is published on the App Store by <strong>Izotz Cristobal Mota</strong> (Seize Apps), Basque Country, Spain, who is the data controller for the app ("we", "us"). Contact for anything about your data: @mail@.</p>

<h2>Your photos stay on your iPhone</h2>
<p>Roomy asks for access to your photo library (full access or the photos you select) so you can review items and remove the ones you no longer need, and, to save the smaller copy of a compressed video, for permission to add to it. It reads thumbnails, sizes, dates and, for video compression, the location and favorite flag of a video so it can carry them onto the compressed copy. Duplicates and similar shots are found on the iPhone, by comparing a small visual fingerprint of each photo; the photos themselves are never uploaded, shared or sold, and Roomy never gives them or anything about them to RevenueCat or to anyone else.</p>
<p>If a photo or video is in iCloud Photos and not on the phone, iOS downloads it from your iCloud when Roomy needs to show or compress it; that transfer is between your iPhone and Apple. The duplicate scan never downloads anything.</p>

<h2>What Roomy stores on your device</h2>
<p>Roomy keeps your review progress (the identifiers of the photos you kept or moved to the Trash, and their sizes), cleanup statistics such as items reviewed and space freed, caches of the visual fingerprints and file sizes it has already worked out, and your preferences (haptics, reminder, sort order and similar), all inside the app. It stores identifiers and numbers, never the images. While it compresses a video, a temporary file is written and removed afterwards. Roomy also reads your iPhone's total and available storage to show it on the home screen; nothing is sent anywhere. Roomy does not use iCloud or CloudKit, so nothing syncs between devices. Like any app's data, what is stored on your iPhone can be included in your device backup if you have backups turned on; those backups are between you and Apple. Deleting Roomy removes this data.</p>

<h2>What Roomy deletes, and when</h2>
<p>Swiping left only moves an item to Roomy's Trash; nothing is deleted until you confirm in Roomy and in the iOS dialog. Deleted items go to Photos › Recently Deleted, where iOS keeps them for 30 days. When you compress a video, Roomy saves the smaller copy and removes the original in a single change only if the copy is at least 10 percent smaller; otherwise the original is left untouched.</p>

<h2>No accounts, no ads, no tracking, no AI</h2>
<p>Roomy has no account or sign-in, shows no advertising, does not ask for tracking permission and does not track you across apps or websites. Its only third-party library is RevenueCat's, used for purchase bookkeeping as described below. Roomy makes no calls to any AI service.</p>

<h2>Purchases</h2>
<p>Roomy is free to start. Roomy Pro is sold through the App Store as a yearly subscription (with a free introductory period for eligible new subscribers), a weekly subscription or a one-time lifetime purchase. Apple processes the payment and any renewal; Roomy never sees your payment information. Roomy checks your purchases with Apple's StoreKit on your iPhone, remembers only which products are active, and can restore purchases from Apple.</p>

__RC__

<h2>Notifications, sharing and email</h2>
<p>If you turn on the daily reminder, Roomy asks for notification permission and schedules one repeating local notification with fixed text at the hour you choose. It is not a push notification and nothing is sent to a server. "Share my result" renders an image of the space you freed, with no photos in it, and offers it through the iOS share sheet; where it goes is your choice.</p>
<p>The email drafts the app opens (Suggest a Feature, Report a Bug, and Contact Support when the purchase screen cannot load its plans) go to @email@ only if you send them. Report a Bug and Contact Support fill in your Roomy version, iOS version and device model (Contact Support also your App Store country); you can read and change the draft first. We use your email only to read and answer it.</p>

<h2>Deleting your data and how long it stays</h2>
<p>Everything Roomy stores is on your iPhone and stays until you reset it or delete the app: Settings › Reset review progress clears which items you kept or skipped (your Trash and your library are untouched), and deleting Roomy removes the rest. There is no account and no server-side data to delete. To ask RevenueCat to delete its purchase record, write to @mail@.</p>

<h2>Children</h2>
<p>Roomy is not directed at children and is not in the App Store's Kids Category. It does not ask anyone for a name or email address.</p>

__RIGHTS__

<h2>Changes</h2>
<p>If this policy changes, the new version will be published on this page with a new date.</p>

<h2>Contact</h2>
<p>@mail@</p>
'''
PRIVACY = PRIVACY.replace('__RC__', revenuecat(
    'Roomy',
    'product, price, dates and Apple\'s transaction data',
    'your photos, videos or their metadata, what you kept or deleted, your name or your email',
    extra='Roomy also tells it, as a paywall impression, which situation opened the Roomy Pro screen (the daily swipe limit, one-tap cleanup, video compression or the upgrade button in Settings), and where you got to in the purchase (screen shown, buy tapped, bought, cancelled, pending, failed, restore started, succeeded or failed) together with the plan involved. It asks RevenueCat once per install to read your existing purchase history from Apple and labels the install as a TestFlight or App Store build. The library runs only in release builds on a real device. ',
    where='Whenever Roomy is open')).replace('__RIGHTS__', rights(
    'Roomy has no account and keeps no records of its own on a server, and what it stores on your iPhone leaves with the app when you delete it. The only data about you that Roomy sends off your iPhone is what RevenueCat holds for us (see above): to ask for access, correction or deletion of it, write to us and we will pass the request on to RevenueCat.',
    'The legal basis for the purchase records is the performance of the purchase and our legitimate interest in keeping track of sales. '))

TERMS = terms('Roomy: Swipe Photo Cleaner', 'Roomy', 'Izotz Cristobal Mota (Seize Apps)', [
    ('Roomy Pro',
     '<p>Roomy is free to start, with a limit of 50 swipes a day (an undo gives one back) and with the Trash and the deletion of a single large video always free. Roomy Pro unlocks unlimited swipes, one-tap Delete in Duplicates and Similar, and video compression. It is sold as an auto-renewing yearly or weekly subscription or as a one-time lifetime purchase that does not renew. The price is shown by the App Store before you confirm. A free introductory period is offered on the yearly plan to eligible new subscribers only; if you take it, any unused part is forfeited when you buy a subscription.</p>'
     '<p>Subscriptions are charged to your Apple Account at confirmation and renew automatically unless you turn off auto-renewal at least 24 hours before the end of the current period. Manage or cancel them in your Apple Account\'s subscription settings. If you own the lifetime purchase and also have an active subscription, you can cancel the subscription. Restore Purchases is always available in the purchase screen and in Settings. Purchases are processed by Apple, and refunds are handled by Apple under the App Store\'s policies: we can\'t issue refunds directly.</p>'),
    ('Your photos and what you delete',
     '<p>You decide what Roomy deletes. Roomy only moves an item to its Trash when you swipe, and asks you to confirm before anything is removed from your library, but you are responsible for the photos and videos you choose to delete or compress. Deleted items go to Photos › Recently Deleted for 30 days, where iOS lets you recover them. Keep your own backups: as our <a href="@privacy@">Privacy Policy</a> explains, your photos stay on your device and we have no access to them or copies of them.</p>'),
    ('Video compression',
     '<p>Compression creates a smaller HEVC copy that keeps the date, location and favorite status of the original, and replaces the original only when the copy is at least 10 percent smaller. The copy is re-encoded, so it will not be identical to the original.</p>'),
    ('Acceptable use',
     '<p>Don\'t reverse-engineer, resell or misuse Roomy, and don\'t use it in any way that breaks the law or Apple\'s terms.</p>'),
])

SUPPORT = r'''
<h1>Support</h1>
<p class="updated">Roomy: swipe to clean up your photos and videos.</p>

<h2>Contact</h2>
<p class="contact">@mail@</p>
<p>The Suggest a Feature and Report a Bug rows at the bottom of Settings open an email addressed to us; the bug report fills in your Roomy version, iOS version and device model so we can help faster.</p>

<h2>Common questions</h2>

<h3>Does Roomy upload my photos?</h3>
<p>No. Roomy works on your iPhone only and has no server. See the <a href="@privacy@">Privacy Policy</a>.</p>

<h3>Can I recover something I deleted?</h3>
<p>Swiping left only moves an item to Roomy\'s Trash. After you confirm, deleted items stay in Photos › Recently Deleted for 30 days, and you can recover them there.</p>

<h3>Roomy only shows some of my photos.</h3>
<p>You gave Roomy access to selected photos only. Use "Choose more photos" in Roomy, or allow full access in the iPhone\'s Settings › Privacy &amp; Security › Photos › Roomy.</p>

<h3>What does the free version include?</h3>
<p>50 swipes a day, with the Trash and the deletion of a single large video always free. Roomy Pro adds unlimited swipes, one-tap Delete in Duplicates and Similar, and video compression.</p>

<h3>How do I restore my purchase?</h3>
<p>Sign in with the same Apple Account, open the purchase screen or Settings and tap Restore Purchases.</p>

<h3>How do I cancel my subscription or get a refund?</h3>
<p>Subscriptions are managed by Apple: open <a href="https://apps.apple.com/account/subscriptions" rel="noopener">your Apple Account\'s subscriptions</a>. Request a refund at <a href="https://reportaproblem.apple.com" rel="noopener">reportaproblem.apple.com</a>. The purchase screen also offers a Contact Support email if its plans don\'t load.</p>

<h3>The daily reminder doesn\'t show up.</h3>
<p>Turn it on in Roomy\'s Settings, allow notifications for Roomy in the iPhone\'s Settings › Notifications, and check that no Focus mode is silencing it.</p>

<h3>How do I start over?</h3>
<p>Settings › Reset review progress clears which items you kept or skipped. Your Trash and your library are untouched.</p>
'''

APP['pages'] = {
    ('en', 'privacy'): dict(title='Roomy · Privacy Policy',
                            desc='Roomy privacy: photos stay on your iPhone. No accounts, no ads, no tracking. Purchase bookkeeping through RevenueCat.', body=PRIVACY),
    ('en', 'terms'): dict(title='Roomy · Terms of Use', desc='Terms of use for Roomy.', body=TERMS),
    ('en', 'support'): dict(title='Roomy · Support', desc='Help and contact for Roomy.', body=SUPPORT),
}
