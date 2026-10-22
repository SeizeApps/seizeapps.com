"""Overbit: config for tools/gen_legal_apps.py. Facts: Overbit 0.1.2 (6) at SeizeRepo 5ee88ea7e. Not local-only:
the app registers an install UUID, locale, Pro flag and (while alerts are on) an APNs token and watched timeframes
with a Supabase backend, reads candles from it, and has a Pro feedback box that writes to it. RevenueCat is
analytics-only. The Supabase region (Frankfurt) is the one named in the backend's own README, not provable from code.
The destination of the feedback notification webhook is a vault secret and is not named."""
from .common import terms, rights, revenuecat

# Ice blue #6FC1DD from SeizeTheme.accent (dark-only app). 2.0:1 on white, so light-mode text uses a darker blue
# of the same hue (found by the generator).
APP = dict(
    slug='overbit', name='Overbit', icon='overbit.png',
    appStoreUrl='https://apps.apple.com/app/id6819401777',
    email='hello@seizeapps.com', publisher='Izotz Cristobal Mota (Seize Apps)',
    updated_en='October 22, 2026',
    theme=dict(
        light=dict(mark='#6FC1DD', bg='#FFFFFF', fg='#101A1F', muted='#506069', line='#E0E8EC'),
        dark=dict(mark='#6FC1DD', bg='#0B1114', fg='#E8EFF2', muted='#A0B0B8', line='#1F2D33'),
    ),
    pages={},
)

PRIVACY = r'''
<h1>Privacy Policy</h1>
<p class="updated">Last updated: @updated@</p>
<p class="summary"><strong>The short version:</strong> Overbit has no account and no advertising, and does not track you. It is not purely local, though: to fetch prices and to push you alerts it talks to our server, which keeps one record per install under a random ID (never your name or email), and purchase bookkeeping goes to RevenueCat. If you write to us through the Pro feedback box, what you type reaches us too. You can delete your server record from the app at any time.</p>

<h2>Who is responsible</h2>
<p>Overbit ("Overbit: BTC RSI Alerts") is published on the App Store by <strong>Izotz Cristobal Mota</strong> (Seize Apps), Basque Country, Spain, who is the data controller for the app ("we", "us"). Contact for anything about your data: @mail@.</p>

<h2>What stays on your iPhone</h2>
<p>Your settings (the timeframes you watch, RSI length, oversold and overbought levels, whether alerts are on), the history of alerts you received, the random install ID described below, the notification token and registration state, and a cached copy of whether Overbit Pro is active are stored on your iPhone, in the app's settings. Overbit does not use iCloud or CloudKit, so nothing syncs between devices, and it uses no files, App Group or Keychain of its own. Like any app's data, it can be included in your device backup if you have backups turned on; those backups are between you and Apple.</p>

<h2>What reaches our server</h2>
<p>Overbit uses a Supabase project (Supabase Inc., our processor, in its Frankfurt, Germany region as described in our backend documentation) for three things. It never sends it your name, email, location, advertising ID or anything about your other apps.</p>
<ul>
<li><strong>Prices.</strong> Each time Overbit refreshes, it asks our server for the latest price and the candles of the timeframe you look at. The request carries only our public app key; like any server, ours and Supabase's platform receive the internet address of each request, and Supabase may keep standard request logs under its own terms (<a href="https://supabase.com/privacy" rel="noopener">supabase.com/privacy</a>).</li>
<li><strong>Registration for alerts.</strong> Overbit registers this install with a random ID created on your iPhone (not your Apple ID, not your advertising ID), your device language and region setting, and whether Overbit Pro is unlocked. While alerts are on and iOS allows Overbit to notify you, the registration also carries your Apple push-notification token, whether it is a development or production token, and, for each timeframe you watch, its RSI length and levels. If alerts are off, the token is empty and the timeframes are empty. The server keeps one record for the install and one for each watched timeframe, and a log of the alerts it has sent (timeframe, candle, direction and time), which is deleted after 90 days. When Apple reports that a token is no longer valid, the server clears it. The server does not delete the install record on its own when you delete the app; it stays until you use Delete my data.</li>
<li><strong>Alerts.</strong> Every minute our server reads the public price of Bitcoin from on-chain pools, using a blockchain node provider (Alchemy), and when RSI crosses a level it asks Apple's push service (APNs) to deliver your notification. Those providers receive nothing from your phone and nothing about you.</li>
</ul>
<p>If the app cannot reach its server, a background task may fall back to a local notification created on your iPhone. Overbit then does not send you the same alert twice.</p>

<h2>Feedback (Overbit Pro)</h2>
<p>If you use the feedback box (a Pro feature), Overbit sends our server your message (up to 2,000 characters), the reply email only if you type one, the app version and build, iOS version, device model, language setting, your random install ID, whether Pro is on and the list of timeframes you watch. A copy is kept with the message until we delete it, and at most five messages a day per install are accepted. When a message arrives, a notification with the first 500 characters of your message, your reply email if you gave one, and a few of these details is sent to a notification channel that we configure; we do not name that service here. We use your message and reply email only to read and answer it. Using Delete my data (below) also deletes your feedback messages.</p>

<h2>Permissions and notifications</h2>
<p>The only permission Overbit asks for is notifications (alerts and sound), the first time you turn alerts on, never at launch. Overbit registers with Apple's push service only after you allow notifications. It asks for no location, camera, photos, contacts, microphone or tracking permission, and runs background tasks (refresh and processing) so that alerts can be prepared when iOS allows. The notification text contains only the timeframe, direction and RSI levels.</p>

<h2>No ads, no tracking, no AI</h2>
<p>Overbit shows no advertising, does not ask for tracking permission and does not track you across apps or websites. Apart from RevenueCat's library (below), it contains no analytics, crash-reporting or advertising library. Overbit makes no calls to any AI service.</p>

<h2>Purchases</h2>
<p>Overbit is free to download. Overbit Pro is an optional one-time in-app purchase (not a subscription): it unlocks every timeframe, custom RSI length and levels, and the feedback box. Apple processes the payment; Overbit checks your purchase with Apple's StoreKit on your iPhone, caches only whether Pro is active, and can restore purchases from Apple. We never receive your name, email or payment details from a purchase.</p>

__RC__

<h2>Deleting your data and how long it stays</h2>
<p><em>Settings › Your data › Delete my data</em> deletes this install's record on our server, with its watched timeframes, its alert log and any feedback messages you sent, turns your alerts off and stops Overbit registering until you turn alerts on again. It does not remove your settings and alert history on the iPhone (those go when you delete the app) and it does not reach RevenueCat: to ask RevenueCat to delete its purchase record, write to @mail@ and we will ask it. Without using it, the server keeps an install's record until you delete it, and alert logs for 90 days. The price history the server stores is public market data and holds nothing about you.</p>

<h2>Children</h2>
<p>Overbit is not directed at children and is not in the App Store's Kids Category. It does not ask anyone for a name or email address.</p>

__RIGHTS__

<h2>Changes</h2>
<p>If this policy changes, the new version will be published on this page with a new date.</p>

<h2>Contact</h2>
<p>@mail@</p>
'''
PRIVACY = PRIVACY.replace('__RC__', revenuecat(
    'Overbit',
    'product, price, dates and Apple\'s transaction data',
    'your timeframes, alerts, price settings, feedback, name or email',
    extra='When the Pro screen opens, Overbit also tells it that it opened and where you got to (buy tapped, bought, cancelled, pending, failed, restore started, succeeded or failed) with the product involved. It asks RevenueCat once per install to read your existing purchase history from Apple and labels the install as a TestFlight or App Store build. The library runs only in release builds on a real device. ',
    where='Whenever Overbit is open')).replace('__RIGHTS__', rights(
    'What we hold about you is the install record on our server (which you can delete yourself in the app), any email you sent and what RevenueCat holds for us: write to us to access, correct or delete them.',
    'The legal basis for the alert service is the performance of what you asked for, and for the purchase records the performance of the purchase and our legitimate interest in keeping track of sales. '))

TERMS = terms('Overbit: BTC RSI Alerts', 'Overbit', 'Izotz Cristobal Mota (Seize Apps)', [
    ('Not financial advice',
     '<p>Overbit shows the price of Bitcoin and its RSI, and alerts you when RSI crosses a level you chose. It is not a broker, does not trade or hold anything for you, and nothing in it is financial, investment or trading advice. Decisions you make are your own, and you can lose money trading.</p>'),
    ('Prices and alerts',
     '<p>Prices are read from on-chain liquidity pools (PancakeSwap and Aerodrome on Base, Uniswap on Ethereum), not from an exchange, so they can lag or differ from the charts you see elsewhere. Alerts can arrive late or be skipped: they depend on those pools, on our server, on Apple\'s push service, on your iOS notification settings and network, and on background execution that iOS controls; short-timeframe alerts (15 minutes and under) pause when pools disagree. Don\'t rely on Overbit alone for anything where a late or missing alert could cost you. Overbit is not affiliated with PancakeSwap, Aerodrome, Uniswap or Coinbase.</p>'),
    ('Overbit Pro',
     '<p>Overbit is free with one timeframe, RSI 14 and levels 30/70. Overbit Pro is an optional one-time in-app purchase, not a subscription, billed by Apple at the price the App Store shows before you confirm, with Family Sharing on. It unlocks all fifteen timeframes (5 minutes to 1 month), custom RSI length and levels, and the feedback box. Restore Purchases is always available on the Pro screen. Purchases are processed by Apple, and refunds are handled by Apple under the App Store\'s policies: we can\'t issue refunds directly.</p>'),
    ('Your data',
     '<p>As our <a href="@privacy@">Privacy Policy</a> explains, Overbit has no account, keeps your settings on your device and keeps one record per install on our server, which you can delete in the app at any time. Feedback is a one-way message to us, limited to five a day per install.</p>'),
    ('Acceptable use',
     '<p>Don\'t reverse-engineer, resell or misuse Overbit, don\'t overload our server, and don\'t use it in any way that breaks the law or Apple\'s terms.</p>'),
], extra_warranty='We are not liable for any trading or financial loss arising from prices, alerts or their absence. ')

SUPPORT = r'''
<h1>Support</h1>
<p class="updated">Overbit: Bitcoin RSI alerts, when an overbought or oversold candle closes.</p>

<h2>Contact</h2>
<p class="contact">@mail@</p>
<p>The Suggest a Feature and Report a Bug rows at the bottom of Settings open an email addressed to us; the bug report fills in your Overbit version, iOS version and device model. Overbit Pro also has a feedback box in Settings.</p>

<h2>Common questions</h2>

<h3>My alerts don\'t arrive.</h3>
<p>Check that alerts are on in Overbit\'s Settings and that notifications are allowed for Overbit in the iPhone\'s Settings › Notifications. Alerts also depend on your connection and on iOS background activity, and they can arrive late or be skipped, especially on short timeframes when the price pools disagree. You are alerted when a candle closes with RSI across your levels, not when the price merely touches them.</p>

<h3>The price differs from my exchange.</h3>
<p>Overbit reads on-chain pools, not an exchange, so the price can lag or differ a little. See the notes in Settings.</p>

<h3>What does the free version include?</h3>
<p>One timeframe, RSI 14 and levels 30/70. Overbit Pro, a one-time purchase with no subscription, adds all fifteen timeframes, a custom RSI length and levels, and the feedback box.</p>

<h3>How do I restore Overbit Pro?</h3>
<p>Sign in with the same Apple Account, open the Pro screen and tap Restore Purchases.</p>

<h3>How do I get a refund?</h3>
<p>Purchases are handled by Apple. Request a refund at <a href="https://reportaproblem.apple.com" rel="noopener">reportaproblem.apple.com</a>.</p>

<h3>How do I delete my data?</h3>
<p>Settings › Your data › Delete my data removes your install\'s record, timeframes, alert log and feedback from our server and turns alerts off. Delete the app to remove what is stored on the iPhone. To ask RevenueCat to delete its purchase record, write to us. See the <a href="@privacy@">Privacy Policy</a>.</p>
'''

APP['pages'] = {
    ('en', 'privacy'): dict(title='Overbit · Privacy Policy',
                            desc='Overbit privacy: no account, no ads, no tracking. One random-ID record per install for alerts, which you can delete in the app.', body=PRIVACY),
    ('en', 'terms'): dict(title='Overbit · Terms of Use', desc='Terms of use for Overbit.', body=TERMS),
    ('en', 'support'): dict(title='Overbit · Support', desc='Help and contact for Overbit.', body=SUPPORT),
}
