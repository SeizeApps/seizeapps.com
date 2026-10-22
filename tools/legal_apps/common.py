"""Fragments shared by the per-app legal pages (English). Tokens (@mail@, @updated@, @privacy@ ...) are
filled by tools/gen_legal_apps.py. Each fragment is plain text a lawyer can read; nothing here is app-specific
except what is passed in."""

APPLE_EULA = 'https://www.apple.com/legal/internet-services/itunes/dev/stdeula/'


def terms(name, short, publisher, mid, extra_warranty=''):
    """Terms of Use: fixed opening and closing sections around the app's own `mid` sections [(heading, html)]."""
    secs = [
        ('Agreement',
         f'<p>These terms govern your use of {name} ("{short}"), published on the App Store by {publisher}, Basque Country, Spain ("we", "us"). '
         f'By downloading or using {short} you agree to these terms and to Apple\'s standard <a href="{APPLE_EULA}" rel="noopener">Licensed Application End User License Agreement</a>, '
         f'which applies to anything these terms don\'t cover.</p>'),
        ('License',
         f'<p>We grant you a personal, non-exclusive, non-transferable license to use {short} on Apple devices that you own or control, as permitted by the App Store terms. '
         f'The app, its design and its code remain ours.</p>'),
    ] + list(mid) + [
        ('Warranty and liability',
         f'<p>{short} is provided "as is", without warranties of any kind. To the maximum extent permitted by law, we are not liable for indirect or consequential damages arising from your use of {short}, '
         f'and our total liability is limited to the amount you paid for {short} in the twelve months before the claim. {extra_warranty}Nothing in these terms limits rights that consumer law grants you and that cannot be waived.</p>'),
        ('Changes',
         f'<p>We may update these terms as {short} evolves; the current version always lives at this address with its effective date above. Continued use after a change means you accept the updated terms.</p>'),
        ('Governing law',
         '<p>These terms are governed by the laws of Spain. Consumers in the EU also keep the protections of their country of residence.</p>'),
    ]
    out = ['<h1>Terms of Use</h1>', '<p class="updated">Effective @updated@</p>']
    for i, (h, b) in enumerate(secs, 1):
        out.append(f'<h2>{i}. {h}</h2>\n{b}')
    out.append('<h2>Contact</h2>\n<p>@mail@</p>')
    return '\n\n'.join(out) + '\n'


def rights(own, basis=''):
    """Your rights (GDPR). `own`: what is true of this app's data; `basis`: legal basis sentence if any."""
    return (f'<h2>Your rights</h2>\n<p>Under the GDPR you can ask for access to, correction or deletion of personal data, object to its use, or ask for a copy. {own} '
            f'To exercise any right, write to @mail@. {basis}You can also complain to the Spanish Data Protection Agency (<a href="https://www.aepd.es" rel="noopener">aepd.es</a>) '
            f'or to the authority where you live.</p>')


CHANGES = '<h2>Changes</h2>\n<p>If this policy changes, the new version will be published on this page with a new date.</p>'
CONTACT = '<h2>Contact</h2>\n<p>@mail@</p>'
RC_URL = 'https://www.revenuecat.com/privacy'


def revenuecat(name, sent, never, extra='', where='Whenever {name} runs on your device'):
    """Purchase-bookkeeping section. `sent`: what the app hands the library; `never`: what it never hands it."""
    return (f'<h2>Purchase analytics (RevenueCat)</h2>\n'
            f'<p>{name} includes the software library of RevenueCat, Inc. (United States), used for purchase bookkeeping only: Apple\'s StoreKit still handles every purchase and {name} still decides on your device whether Pro is active. '
            f'{where.format(name=name)}, the library creates a random anonymous ID for your install and sends RevenueCat that ID, your device\'s vendor identifier (a number Apple gives the apps of one developer on one device; it is not the advertising identifier) '
            f'and the App Store purchases you make in {name} ({sent}). {extra}'
            f'The library also adds the technical details such a library sends with its requests (for example the app and iOS version, device model, language and App Store country), and, like any server, RevenueCat sees the internet address of each request. '
            f'We use this to keep a record of purchases and to count them. {name} never gives RevenueCat {never}, and we do not enable any advertising integration: it is not used to track you.</p>\n'
            f'<p>RevenueCat is our processor. What it collects through its library, where and for how long it keeps it, and how it protects it are set out in its own privacy policy at '
            f'<a href="{RC_URL}" rel="noopener">revenuecat.com/privacy</a>; we cannot see inside its systems and we do not promise a retention period for it. '
            f'Deleting {name} does not delete what RevenueCat already holds: write to @mail@ and we will ask it to delete the record.</p>')
