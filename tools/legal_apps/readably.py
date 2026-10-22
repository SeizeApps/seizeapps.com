"""Readably: config for tools/gen_legal_apps.py. Facts: Readably 0.1.0 (12) at SeizeRepo 5ee88ea7e, local-first.
Every voice runs on the iPhone; the whole cloud stack (relay, plans, account, Fish Audio / OpenRouter voices) is
parked behind ReadablyApp.cloudEnabled = false and is NOT described here. Network use is exactly: a user-started
voice download from Hugging Face, the Pro "Read from a link" fetch, StoreKit, RevenueCat."""
from .common import terms, rights

# Spruce green from Palette.swift (#1F6B63 light / #7CC7BA dark) on the app's paper (#F5F0E6) and night (#14161A).
APP = dict(
    slug='readably', name='Readably', icon='readably.png',
    appStoreUrl='https://apps.apple.com/app/id6821341514',
    email='hello@seizeapps.com', publisher='Izotz Cristobal Mota (Seize Apps)',
    updated_en='October 22, 2026',
    theme=dict(
        light=dict(mark='#1F6B63', bg='#F5F0E6', fg='#1E2623', muted='#56605B', line='#DCD5C5', soft='#E8EFE9'),
        dark=dict(mark='#7CC7BA', bg='#14161A', fg='#ECEFEE', muted='#A5AEAF', line='#2A2F36'),
    ),
    pages={},
)

PRIVACY = r'''
<h1>Privacy Policy</h1>
<p class="updated">Last updated: @updated@</p>
<p class="summary"><strong>The short version:</strong> Readably reads your text aloud on your iPhone. What you read stays on your iPhone: every voice runs on the device, nothing you paste or import is sent to us or to any AI service, and there is no account, no advertising and no tracking. Readably reaches the internet only for four things: a voice download you start yourself, a web page you ask it to read (a Pro tool), Apple's App Store, and purchase bookkeeping by RevenueCat.</p>

<h2>Who is responsible</h2>
<p>Readably (App Store name "Readably - Text to Speech") is published by <strong>Izotz Cristobal Mota</strong> (Seize Apps), Basque Country, Spain, who is the data controller for the app ("we", "us"). Contact for anything about your data: @mail@.</p>

<h2>What stays on your iPhone</h2>
<p>Your library is stored in the app's private container: for each document its title, language, the full text split into paragraphs, your reading position, when you added and last opened it, and an optional voice you chose for it. Your preferences (appearance, text size, chosen voice, whether the lock screen shows text) live in the app's settings, together with a cached copy of whether Readably Pro is active. Other files, all on the device: the voice files you download (kept out of backups), a cache of audio already rendered for sentences you have read (it may be emptied by iOS and is kept out of backups), and your pronunciation rules. When you save audio, a temporary file is written while it is rendered.</p>
<p>Readably does not use iCloud or CloudKit, does not sync your documents anywhere and has no server of its own: we cannot see your library. Like any app's data, your documents can be included in your device backup (iCloud Backup or a computer backup) if you have backups turned on; those backups are between you and Apple. Deleting Readably deletes its data.</p>

<h2>No cloud voices, no AI service</h2>
<p>This version of Readably has no cloud voices and contacts no server of ours. Speech is generated on your iPhone, either by the open-source Kokoro-82M model that you download (run with the FluidAudio library) or by the voices built into iOS. Language detection and text recognition use Apple's on-device frameworks. No text, document or audio is sent to an AI provider.</p>

<h2>What Readably downloads, and from where</h2>
<ul>
<li><strong>On-device voices (Hugging Face).</strong> Only when you tap Download in the first-run welcome or in Settings › On-device voices, Readably downloads the Kokoro voice files (roughly 90 to 185 MB depending on the language) from Hugging Face (huggingface.co, Hugging Face, Inc.). It sends no text, no account and no identifier of ours; as with any download, Hugging Face sees your internet address and the details iOS adds to a request. After that the voices work offline, and you can delete them in Settings at any time. What Hugging Face keeps is described in <a href="https://huggingface.co/privacy" rel="noopener">its privacy policy</a>.</li>
<li><strong>Read from a link (Readably Pro).</strong> When you paste a web address, your iPhone fetches that page directly (with a private session that keeps no cookies or cache, a 15 second limit and an 8 MB cap), sending your language preferences and a browser-style user agent. The site you named sees your internet address and those details. Only the article text is kept as a document; the address is not kept. Nothing goes through a server of ours.</li>
<li><strong>Purchases.</strong> Apple's StoreKit talks to Apple for the catalogue, purchases, restore and entitlements.</li>
</ul>

<h2>Camera, lock screen and notifications</h2>
<p>The only permission Readably ever asks for is the camera, and only when a Pro user (or trial) taps Scan text: the pages are read by Apple's document scanner and turned into text on your iPhone with Apple's text recognition; the pictures are not saved or sent anywhere. Readably never asks for the microphone, photos, location, contacts or notifications, and it sends no notifications. It plays audio in the background so that listening continues with the screen locked.</p>
<p>While Readably reads, the lock screen shows a Live Activity and Now Playing controls. By default they show the document title (cut to 80 characters) and the sentence being read (cut to 220), which anyone looking at your locked iPhone can see; Settings › Show text on the lock screen turns that off, leaving only the kind of text. The Live Activity extension has no network access and stores nothing.</p>

<h2>Purchases</h2>
<p>Readably's core is free. Readably Pro is an optional one-time lifetime purchase (not a subscription), and the 30-day trial is a free item you can take once per Apple Account. Apple processes the payment; Readably checks your purchase with Apple's StoreKit on the device, caches only whether Pro is paid and when a trial ends, and can restore purchases from Apple. We never receive your name, email or payment details from a purchase.</p>

__RC__

<h2>Writing to us</h2>
<p>Suggest an improvement, Report a problem and, for Pro owners, the feedback option open a draft in your own mail app addressed to @email@. A Pro feedback draft can include the Readably version and build, iOS version and device model; you can read and change the draft first. Nothing is sent unless you send it, and we use your email only to read and answer it.</p>

<h2>Deleting your data and how long it stays</h2>
<p>Your documents and reading positions stay until you delete them: delete a document in the Library (its paragraphs go with it), delete downloaded voices per language in Settings › On-device voices, delete pronunciation rules one by one, or delete the app to remove everything stored on the device. The audio cache is size-limited and may be emptied by iOS at any time. There is no account and no server-side data to delete. To ask RevenueCat to delete its purchase record, write to @mail@.</p>

<h2>Children</h2>
<p>Readably is not directed at children and is not in the App Store's Kids Category. It does not ask anyone for a name or email address.</p>

__RIGHTS__

<h2>Changes</h2>
<p>If this policy changes, the new version will be published on this page with a new date. Readably was built so that cloud voices can be added later; they are switched off in this version, and this page will be updated before any release that turns them on.</p>

<h2>Contact</h2>
<p>@mail@</p>
'''
from .common import revenuecat
PRIVACY = PRIVACY.replace('__RC__', revenuecat(
    'Readably',
    'product, price, dates and Apple\'s transaction data',
    'your documents, text, audio, name or email',
    extra='Once per install it asks RevenueCat to read the existing purchase history from Apple, and it labels the install as a TestFlight or App Store build. '
          'Readably itself sends nothing else to RevenueCat: no screen or feature events. The library runs only in release builds on a real device. ',
    where='When Readably is open')).replace('__RIGHTS__', rights(
    'Readably keeps your library only on your device, so it leaves with the app when you delete it, and we hold no personal data about you to produce. For what RevenueCat holds, or for an email you sent, write to us.',
    'The legal basis for the purchase records is the performance of the purchase and our legitimate interest in keeping track of sales. '))

TERMS = terms('Readably', 'Readably', 'Izotz Cristobal Mota (Seize Apps)', [
    ('Free use and Readably Pro',
     '<p>Readably is free to use: all voices, unlimited listening, and importing by paste, PDF or text file. Readably Pro is an optional one-time in-app purchase, not a subscription, billed by Apple at the price the App Store shows before you confirm. It opens five tools: Read from a link, Scan text, EPUB books, Save as audio and Pronunciations. Family Sharing is on for it, and you can restore it on your other devices with the same Apple Account from the Pro screen or Settings.</p>'
     '<p>The 30-day trial is a free item that opens the same tools for 30 days, counted from the day you take it, once per Apple Account. Nothing is charged when it ends and nothing renews; the tools close again and the documents you added keep working. If you buy Pro, it always takes over from the trial. Refunds are handled by Apple under the App Store\'s policies; we can\'t issue refunds directly.</p>'),
    ('Your content',
     '<p>The text you paste or import stays on your device, as our <a href="@privacy@">Privacy Policy</a> explains; we have no access to it, which also means you are responsible for your own backups. You are responsible for what you import or fetch and for having the right to use it: Readably reads the text aloud for you and does not change who owns it. Audio you save is created on your device and goes only where you send it.</p>'),
    ('Voices and open-source software',
     '<p>The on-device voices are downloaded from a third-party host only when you ask for them. They are large (about 90 to 185 MB), and reading aloud for a long time uses battery and can warm your iPhone. Readably includes open-source components, including the Kokoro model and the FluidAudio library, under their own licences, which are listed in Settings › Acknowledgements.</p>'),
    ('Acceptable use',
     '<p>Don\'t reverse-engineer, resell or misuse Readably, and don\'t use it in any way that breaks the law or Apple\'s terms.</p>'),
], extra_warranty='Speech is generated automatically and can mispronounce words or misread layouts, so don\'t rely on Readably alone where an error could cause harm. ')

SUPPORT = r'''
<h1>Support</h1>
<p class="updated">Readably: text to speech that stays on your iPhone.</p>

<h2>Contact</h2>
<p class="contact">@mail@</p>
<p>Write to us about anything. The Suggest an improvement and Report a problem rows at the bottom of Settings open an email addressed to us.</p>

<h2>Common questions</h2>

<h3>Do I need an internet connection?</h3>
<p>Only to download the on-device voices (once, when you ask for it), to read a web page by link (Pro) and for purchases. After the voices are downloaded, reading works offline and nothing you read leaves your iPhone.</p>

<h3>The voice download is large. Can I remove it?</h3>
<p>Yes. Settings › On-device voices shows each language with its size and lets you delete it. You can download it again later.</p>

<h3>What does Readably Pro unlock?</h3>
<p>Read from a link, Scan text (camera or scanned PDF), EPUB books, Save as audio and Pronunciations. The free core, with all voices and unlimited listening, is never limited. It is a one-time purchase, with no subscription.</p>

<h3>How do I get Pro back on a new device?</h3>
<p>Sign in with the same Apple Account, open the Pro screen and tap Restore Purchases.</p>

<h3>How does the free trial work?</h3>
<p>You can take the 30-day trial once per Apple Account. It counts 30 days from the day you take it, charges nothing when it ends, and the documents you added stay.</p>

<h3>How do I get a refund?</h3>
<p>Purchases are handled by Apple. Request a refund at <a href="https://reportaproblem.apple.com" rel="noopener">reportaproblem.apple.com</a>.</p>

<h3>Anyone can read my lock screen. Can I hide what is being read?</h3>
<p>Yes: turn off Settings › Show text on the lock screen. The Live Activity then shows only the kind of text instead of the title and sentence.</p>

<h3>A word is pronounced wrongly.</h3>
<p>With Readably Pro, add a rule in Pronunciations to say it your way.</p>

<h3>Where is my data? How do I delete it?</h3>
<p>Your library stays on your iPhone, is not synced and is never sent to us. Delete a document in the Library, delete voices in Settings, or delete the app. See the <a href="@privacy@">Privacy Policy</a>.</p>
'''

APP['pages'] = {
    ('en', 'privacy'): dict(title='Readably · Privacy Policy',
                            desc='Readably privacy: what you read stays on your iPhone. On-device voices, no account, no ads, no tracking.', body=PRIVACY),
    ('en', 'terms'): dict(title='Readably · Terms of Use', desc='Terms of use for Readably.', body=TERMS),
    ('en', 'support'): dict(title='Readably · Support', desc='Help and contact for Readably.', body=SUPPORT),
}
