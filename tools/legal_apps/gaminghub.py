"""GamingHub: config for tools/gen_legal_apps.py. Facts: GamingHub 0.5.2 (41) at SeizeRepo 5ee88ea7e. Release ships
five games (The Mind, Impostor, Codigo Secreto, Wavelength, Times Up); Streak, Coartada and Rewind are withheld, so
Rewind's iTunes/Apple Music flow is not described here. Online play runs on Supabase (anonymous auth, rooms,
Edge Functions, Realtime); the project's region is not in the repo and is not stated. Camera is the only permission."""
from .common import terms, rights, revenuecat

# Blue from AccentColor (#0077FF) and the app's dark-UI blue (#5DD4FF, SeizeTheme.accentCyan). #0077FF is 4.1:1
# on white, so light-mode text uses a slightly darker blue of the same hue (found by the generator).
APP = dict(
    slug='gaminghub', name='GamingHub', icon='gaminghub.png',
    appStoreUrl='https://apps.apple.com/app/id6761752010',
    email='hello@seizeapps.com', publisher='Izotz Cristobal Mota (Seize Apps)',
    updated_en='October 22, 2026',
    theme=dict(
        light=dict(mark='#0077FF', bg='#FFFFFF', fg='#1A1814', muted='#5B574E', line='#E8E4DC'),
        dark=dict(mark='#5DD4FF', bg='#0E0D0C', fg='#F5F2EC', muted='#B0AA9E', line='#2B2823'),
    ),
    pages={},
)

PRIVACY = r'''
<h1>Privacy Policy</h1>
<p class="updated">Last updated: @updated@</p>
<p class="summary"><strong>The short version:</strong> GamingHub has no account, no email, no password, no advertising and no tracking. To run a room it sends the display name and avatar you choose, an anonymous ID created for your device and what you do in the game to our server, where the other players in that room can see it; rooms are deleted when they empty and in any case after 12 hours. Purchase bookkeeping goes to RevenueCat. Secret game data (your role, word or cards) goes only to your own device.</p>

<h2>Who is responsible</h2>
<p>GamingHub ("GamingHub: Party Games") is published on the App Store by <strong>Izotz Cristobal Mota</strong> (Seize Apps), Basque Country, Spain, who is the data controller for the app ("we", "us"). Contact for anything about your data: @mail@.</p>

<h2>What stays on your device</h2>
<p>GamingHub keeps these on your device only: the display name you chose (a new install is given a random first name you can change), your settings (haptics, sounds, reduced animation, colour-blind mode, language), the room you were last in (so you can return to it; it is treated as expired after 12 hours), which rooms you have already played in the free trial of each paid game, and which games you own. It uses no App Group, no files and no Keychain of its own, and does not use iCloud or CloudKit, so nothing syncs between devices. Like any app's data, it can be included in your device backup if you have backups turned on; those backups are between you and Apple.</p>

<h2>What reaches our server when you play online</h2>
<p>Online play runs on Supabase (Supabase Inc.), our processor. When you open the app it signs your device in anonymously, which gives it a random ID; there is no sign-in screen and we do not know who you are. To create or join a room, the app then sends our server your display name, your avatar, that anonymous ID, the room code and your language, and then your moves. Everything that is shared in a room is stored in it and visible to the other players in that room: the list of players with their names, avatars and whether they are connected, whether the host owns the game, who was removed by the host, and the content of the game, including any short text you type, such as a clue. Secret game data (your role, your word, your cards) is stored separately and only your own device can read it. The server itself changes game state; the app can only read it.</p>
<p>A room holds its data for at most 12 hours of inactivity: every room carries an expiry that is renewed on each move, and an expired room is deleted automatically every 15 minutes together with its secret data. When the last player leaves, the room and its secrets are deleted immediately. We keep no game history. Because your display name sits next to your anonymous ID in the room for that time, we do not claim the name cannot be tied to that ID while the room exists. The anonymous sign-in record itself (the random ID) is kept by Supabase; it holds no name or email, and we do not delete these records automatically. Supabase's platform may keep standard request logs, such as internet addresses, under its own terms: its policy is at <a href="https://supabase.com/privacy" rel="noopener">supabase.com/privacy</a>, and how long it keeps them is not something we can see.</p>

<h2>Names, other players' content and moderation</h2>
<p>There is no chat. Display names are filtered on your device and again on our server, and a room's host can remove a player (a removed player cannot rejoin that room). You can report a player or a problem from the app: this opens an email to us, which includes the room code, the player's name and a reason you can edit, and it leaves your device only if you send it.</p>

<h2>Camera and the only permission</h2>
<p>The only permission GamingHub asks for is the camera, used by the scanner that reads a room's QR code so you can join instantly. It reads a room code; no photo or video is saved or sent. GamingHub asks for no microphone, photos, location, contacts or tracking permission, and sends no notifications. Sharing a room invite uses the iOS share sheet with the game name and room code, and where it goes is your choice.</p>

<h2>No ads, no tracking, no AI</h2>
<p>GamingHub shows no advertising, does not ask for tracking permission and does not track you across apps or websites. Its only third-party software is the Supabase client library and RevenueCat's library. GamingHub makes no calls to any AI service.</p>

<h2>Purchases</h2>
<p>GamingHub is free to download; The Mind is free, and the other games are unlocked with optional one-time purchases (each game, a bundle or a lifetime unlock; none is a subscription). Apple processes the payment; GamingHub never sees your payment details, checks your purchases with Apple's StoreKit on your device and can restore them from Apple. The free trial of a paid game (a limited number of rooms) is counted on your device from room codes, so reinstalling the app resets it.</p>

__RC__

<h2>Deleting your data and how long it stays</h2>
<p>You can change your name in Settings, leave a room (your secret data is deleted at once, and the room when it is empty) and ask the host to remove another player. Rooms disappear on their own after 12 hours without activity. Deleting the app removes its settings, name and trial count from your device. There is no account to delete. To ask RevenueCat to delete its purchase record, or to ask us to remove an anonymous sign-in record, write to @mail@.</p>

<h2>Children</h2>
<p>GamingHub is a party game for groups; it is not directed at children and is not in the App Store's Kids Category. It does not ask anyone for a name or email address, but players do type display names and short game text that other players in the room can see.</p>

__RIGHTS__

<h2>Changes</h2>
<p>If this policy changes, the new version will be published on this page with a new date. If a later version of GamingHub adds games that use other services, this page will be updated before they ship.</p>

<h2>Contact</h2>
<p>@mail@</p>
'''
PRIVACY = PRIVACY.replace('__RC__', revenuecat(
    'GamingHub',
    'product, price, dates and Apple\'s transaction data',
    'your display name, room codes, the anonymous sign-in ID or what you play',
    extra='When a store sheet opens GamingHub also tells it which game or bundle it was about, and how a purchase or restore went (sheet shown, buy tapped, bought, cancelled, pending, failed, restore started, succeeded or failed). It asks RevenueCat once per install to read your existing purchase history from Apple and labels the install as a TestFlight or App Store build. The library runs only in release builds on a real device. ',
    where='Whenever GamingHub is open')).replace('__RIGHTS__', rights(
    'GamingHub has no account. Rooms are deleted automatically, and the only other data about you that we hold is the anonymous sign-in record, what RevenueCat holds for us and any email you sent: write to us to access, correct or delete them.',
    'The legal basis for running a room is the performance of the game you asked for, and for the purchase records the performance of the purchase and our legitimate interest in keeping track of sales. '))

TERMS = terms('GamingHub: Party Games', 'GamingHub', 'Izotz Cristobal Mota (Seize Apps)', [
    ('Games and purchases',
     '<p>GamingHub is free to download, and The Mind is free to play. The other games can be played for free in a limited number of rooms (three per game, counted on your device) or in any room whose host owns that game; to host one, or to play beyond the trial, you unlock it with an optional in-app purchase: a single game, a bundle of the paid games, or a lifetime unlock of every game, current and future. These are one-time purchases, not subscriptions, billed by Apple at the price the App Store shows before you confirm, and Family Sharing is on. Restore Purchases is always available in the unlock sheet. Purchases are processed by Apple, and refunds are handled by Apple under the App Store\'s policies: we can\'t issue refunds directly. Games listed as coming soon are not for sale.</p>'),
    ('Online play and other players',
     '<p>Online games need an internet connection and are shared with the other people in your room: your display name, avatar and what you type are visible to them for as long as the room exists, up to 12 hours of inactivity. Choose a name you are happy to share and don\'t type anything unlawful, abusive or that belongs to someone else. The host of a room can remove a player, and you can report a player or a problem from the app. We may remove content or players, or block access to online play, if these terms are broken.</p>'),
    ('Your data',
     '<p>As our <a href="@privacy@">Privacy Policy</a> explains, GamingHub has no account, keeps a room only while it is in use and keeps its settings on your device. Because there is no account, unlocked games are tied to your Apple Account through the App Store, not to GamingHub.</p>'),
    ('Availability',
     '<p>Games and features can change, and online play depends on third-party services and your connection; we don\'t promise it will always be available or uninterrupted. The mechanics of the games are our own versions of well-known party-game formats.</p>'),
    ('Acceptable use',
     '<p>Don\'t reverse-engineer, resell or misuse GamingHub, don\'t try to cheat the free trial or tamper with rooms, and don\'t use it in any way that breaks the law or Apple\'s terms.</p>'),
])

SUPPORT = r'''
<h1>Support</h1>
<p class="updated">GamingHub: party games for the room you are in.</p>

<h2>Contact</h2>
<p class="contact">@mail@</p>
<p>The Suggest a Feature and Report a Bug rows in Settings open an email addressed to us; the bug report fills in your GamingHub version, iOS version and device model. To report a player or a problem during a game, use the report option in the room: it opens an email with the room code, the player\'s name and a reason you can edit.</p>

<h2>Common questions</h2>

<h3>I can\'t join a room.</h3>
<p>Check the room code (or scan the QR code: GamingHub asks for camera access only for that) and your connection. A room expires after 12 hours without activity, and a player who was removed by the host can\'t rejoin that room.</p>

<h3>Which games are free?</h3>
<p>The Mind is free. The other games can be tried in three rooms each (or in any room whose host owns the game); after that you unlock them with a one-time purchase: one game, the bundle, or lifetime. There are no subscriptions and no ads.</p>

<h3>How do I restore my purchases on a new device?</h3>
<p>Sign in with the same Apple Account, open any unlock sheet and tap Restore Purchases.</p>

<h3>How do I get a refund?</h3>
<p>Purchases are handled by Apple. Request a refund at <a href="https://reportaproblem.apple.com" rel="noopener">reportaproblem.apple.com</a>.</p>

<h3>I reinstalled the app and my free rooms are back.</h3>
<p>The free trial is counted on your device, so reinstalling resets it. Your purchases are not affected: restore them from the unlock sheet.</p>

<h3>Can I change my name?</h3>
<p>Yes, in Settings. Names that don\'t pass the name filter are replaced.</p>

<h3>Where is my data? How do I delete it?</h3>
<p>GamingHub has no account. Your settings stay on your device, and a room and its secret data are deleted when it empties and in any case after 12 hours. See the <a href="@privacy@">Privacy Policy</a>, or write to us.</p>
'''

APP['pages'] = {
    ('en', 'privacy'): dict(title='GamingHub · Privacy Policy',
                            desc='GamingHub privacy: no account, no ads, no tracking. Rooms are deleted when they empty and after 12 hours.', body=PRIVACY),
    ('en', 'terms'): dict(title='GamingHub · Terms of Use', desc='Terms of use for GamingHub.', body=TERMS),
    ('en', 'support'): dict(title='GamingHub · Support', desc='Help and contact for GamingHub.', body=SUPPORT),
}
