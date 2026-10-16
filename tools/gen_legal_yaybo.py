"""Yaybo's own privacy policy and terms (11/10/2026).

Yaybo is the one Seize app made for children (ages 4 to 9, used with a grown-up), so it can't live under the
studio-wide policy: it needs a COPPA notice. The text comes from docs/kids-us/release/privacy-policy-v1.md in the SeizeRepo
(rewritten 15/10/2026 for the v1 build: iCloud sync and the family link on, Read-aloud, the parent note and the Apple Ads
attribution post; re-checked against the code at d7f191dee on 16/10/2026: per-child "Never listen", "Sign your letters as", the
email rows, the attribution post per subscription, Delete all data; the table is ~/yaybo-work/legal-sync-2026-10-16.md); every sentence about RevenueCat is docs/kids-us/11-revenuecat-disclosure.md §3.2, word for word where it
matters. Change those first, then this file.

Paths follow Atino's convention (English at the root of the app's folder, castellano beside it):
  /yaybo/privacy/      /yaybo/privacidad/     privacy policy with the COPPA section
  /yaybo/terms/        /yaybo/condiciones/    terms of use (the paywall's own Terms link is Apple's standard EULA)
Built with gen_site's chrome; run `python3 tools/gen_site.py`, which calls build_yaybo().
The CONFIRM notes are facts only Izotz can supply; they stay in the generated HTML as comments.
"""
import os
from gen_site import head, header, footer, write, legal_main

# What the page says depends on one fact about the build that ships; the page must describe THAT build (Guideline 2.3.1,
# the COPPA notice must be accurate). It is Izotz's decision, so it is a switch, not an edit:
#   YAYBO_REVENUECAT=on|off   whether the archive carries a REVENUECAT_API_KEY (docs/kids-us/11-revenuecat-disclosure.md).
#                             Decided ON on 15/10/2026; the default stays "on" so the page is never softer than the code.
# iCloud sync and the family link are ON for 0.1.0 (decided 15/10/2026, A2): the sentences say so, and go live with the
# CloudKit Production deploy and the YayboStore.cloudKitSchemaDeployed flip (branch w7/icloud-on). This PR is not merged before then.
# The operator's postal address and phone are the COPPA notice's §312.4(d)(1) facts. They are Izotz's own public facts, given on
# 15/10/2026, and live here as defaults so a plain `python3 tools/gen_site.py` keeps them; the environment variables override them.
RC_STATE = os.environ.get('YAYBO_REVENUECAT', 'on')
assert RC_STATE in ('on', 'off'), RC_STATE
OPERATOR_ADDRESS = {
    'en': os.environ.get('YAYBO_OPERATOR_ADDRESS', 'Ugarana kalea 3, piso 3, 48141 Ugarana, Bizkaia, Spain'),
    'es': os.environ.get('YAYBO_OPERATOR_ADDRESS', 'Ugarana kalea 3, piso 3, 48141 Ugarana, Bizkaia, España'),
}
OPERATOR_PHONE = os.environ.get('YAYBO_OPERATOR_PHONE', '+34 672 53 17 63')
SUBSCRIPTIONS_PATH = {'en': 'Settings › [your name] › Subscriptions', 'es': 'Ajustes › [tu nombre] › Suscripciones'}

# Sentence-for-sentence the same as docs/kids-us/11-revenuecat-disclosure.md §3.2 (minus its last sentence, which this page
# says its own way); tools/check_yaybo_legal.py diffs it against that file.
RC_PARAGRAPH_EN = ("To understand how many families subscribe, Yaybo uses RevenueCat, a US purchase-analytics service. "
    "We use it only to record and verify subscription purchases and to count, in aggregate, how many families subscribe; "
    "never to contact anyone, build a profile or show ads. "
    "It is switched on only after a grown-up passes the parental gate and then buys or restores a subscription, "
    "or opens the subscription screen of a lapsed plan, or opens the subscription screen inside the Parent Zone "
    "(both behind that gate), and never on a child's own device. Opening the Parent Zone alone starts nothing. "
    "Once it is on, it stays on, including while a child is playing, until you close the app. "
    "When it is on, RevenueCat receives an anonymous app user ID, the device's IP address, device and OS information, "
    "<strong>the device's vendor identifier (IDFV)</strong>, the App Store storefront country, an App Tracking Transparency "
    "status flag, and the purchase itself. It never receives your child's name, age, answers or progress. "
    "We do not use these for advertising, we do not track you across other companies' apps, and RevenueCat acts only as "
    "our service provider.")
RC_PARAGRAPH_ES = ("Para saber cuántas familias se suscriben, Yaybo usa RevenueCat, un servicio estadounidense de analítica de compras. "
    "Lo usamos solo para registrar y verificar las compras de suscripción y para contar, de forma agregada, cuántas familias se suscriben; "
    "nunca para contactar con nadie, crear un perfil ni mostrar anuncios. "
    "Solo se activa después de que una persona adulta pase la puerta parental y luego compre o restaure una suscripción, "
    "o abra la pantalla de suscripción de un plan caducado, o abra la pantalla de suscripción dentro de la Zona para padres "
    "(ambas tras esa puerta), y nunca en el dispositivo propio de un niño. Abrir solo la Zona para padres no activa nada. "
    "Una vez activado, sigue activo, también mientras un niño juega, hasta que cierras la app. "
    "Cuando está activo, RevenueCat recibe un identificador anónimo de usuario de la app, la dirección IP del dispositivo, información del "
    "dispositivo y del sistema, <strong>el identificador de proveedor del dispositivo (IDFV)</strong>, el país de la tienda de App Store, "
    "un indicador del estado de App Tracking Transparency y la propia compra. Nunca recibe el nombre, la edad, las respuestas ni el progreso "
    "de tu hijo o hija. No usamos estos datos para publicidad, no te seguimos por las apps de otras empresas y RevenueCat actúa solo como "
    "nuestro proveedor de servicios.")

RC = {
 'on': {
  'en': {
   'short': "If a grown-up buys or restores a subscription, a purchase-analytics service sees the purchase and your device's technical details. Never anything about your child.",
   'section': '''<h2>Purchase analytics (RevenueCat)</h2>
  <p>''' + RC_PARAGRAPH_EN + '''</p>
  <p>RevenueCat is RevenueCat, Inc. The vendor identifier is a number Apple gives the apps of one developer on a device; it is not the advertising identifier. The App Tracking Transparency flag is the device's tracking-permission status: Yaybo never asks to track, so it reads "not determined" unless you or Screen Time turned tracking off. Yaybo sets no attributes of its own in RevenueCat. RevenueCat stores this data in the United States.</p>
  <p>Apple processes the payment. We never see your card or your Apple Account details. Apple, not Yaybo or RevenueCat, decides whether a subscription is active.</p>
  <!-- CONFIRM: the first paragraph is docs/kids-us/11-revenuecat-disclosure.md §3.2 (tools/check_yaybo_legal.py diffs it); RevenueCat's storage in the United States (Amazon Web Services) is as read for Roomy and Atino on 6-7 October 2026. -->''',
   'collect': '''<li><strong>What we collect from a child:</strong> nothing. The learning data above stays on the family's devices and in their own iCloud. What reaches us is what a parent chooses to send (a note) or what Apple sends about an ad (an anonymous token, posted automatically the first time the app opens), and neither comes from the child's side of the app. The only other flow is the purchase data that reaches a service provider, described under "Purchase analytics" (including the device's vendor identifier, a persistent identifier), only after a grown-up passes the parental gate, and used only for the internal operations named there. Because RevenueCat stays on for the rest of that session, its background requests can continue while a child plays; they carry nothing about your child.</li>''',
   'when': '''<li><strong>When purchase analytics turns on:</strong> only after a grown-up passes the parental gate and buys or restores a subscription, or opens the subscription screen of a lapsed plan or the subscription screen inside the Parent Zone (both behind that gate). Opening the Parent Zone alone starts nothing. Never on a device a grown-up told Yaybo is the child's own, and never where Apple tells Yaybo the account belongs to a minor. The grown-up gate is how Yaybo keeps children out of grown-up screens; Yaybo collects no personal information from a child that would need a parent's consent.</li>''',
   'rights': '''you can decline purchase analytics by not buying or restoring through Yaybo and by not opening the subscription screen (opening the Parent Zone alone starts nothing), and you can write to us to ask for what RevenueCat holds about your device to be deleted; ''',
   'keep': '''<li><strong>At RevenueCat:</strong> we use these records only to record and verify subscription purchases and to count subscribers in aggregate, and keep them only as long as we need them for billing, refunds, support and legal records. If you ask us, we ask RevenueCat to delete the record tied to your device, and we aim to have it deleted within 30 days of your request. RevenueCat states no fixed period for how long it keeps end-user data, and deleting Yaybo does not delete what it already holds: write to <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>. We do not keep this information for any other purpose or without end.</li>
    <!-- CONFIRM: the 30-day target and RevenueCat's retention terms / data processing agreement for Yaybo's RevenueCat project are not visible in the repo (privacy policy read June 2026: no fixed period for end-user data). Replace with RevenueCat's confirmed deletion timeframe, and COPPA §312.10 needs a concrete one. -->''',
   'protect': '''Access to our server, to App Store Connect (which Apple protects with two-factor authentication) and to the RevenueCat dashboard is limited to the named Seize developers who work on Yaybo, with two-factor authentication.''',
   'leaves': '''<li><strong>Purchase analytics.</strong> Only after a grown-up passes the gate and buys, restores or opens the subscription screen, never on a child's own device. It goes to RevenueCat, a US service provider; see "Purchase analytics (RevenueCat)" below.</li>''',
   'leaves_tail': '''The only other third-party service that receives anything is RevenueCat, described below.''',
   'age': ''' and to keep purchase analytics off a child's own device''',
  },
  'es': {
   'short': "Si una persona adulta compra o restaura una suscripción, un servicio de analítica de compras ve la compra y los datos técnicos de tu dispositivo. Nunca nada sobre tu hijo o hija.",
   'section': '''<h2>Analítica de compras (RevenueCat)</h2>
  <p>''' + RC_PARAGRAPH_ES + '''</p>
  <p>RevenueCat es RevenueCat, Inc. El identificador de proveedor es un número que Apple da a las apps de un mismo desarrollador en un dispositivo; no es el identificador publicitario. El indicador de App Tracking Transparency es el estado del permiso de seguimiento del dispositivo: Yaybo nunca pide seguir, así que figura como «no determinado» salvo que tú o Tiempo de uso hayáis desactivado el seguimiento. Yaybo no define ningún atributo propio en RevenueCat. RevenueCat guarda estos datos en Estados Unidos.</p>
  <p>Apple procesa el pago. Nunca vemos tu tarjeta ni los datos de tu cuenta de Apple. Es Apple, no Yaybo ni RevenueCat, quien decide si una suscripción está activa.</p>''',
   'collect': '''<li><strong>Qué recogemos de un menor:</strong> nada. Los datos de aprendizaje de arriba se quedan en los dispositivos de la familia y en su propio iCloud. Lo que nos llega es lo que una persona adulta elige enviar (una nota) o lo que Apple envía sobre un anuncio (un token anónimo, enviado automáticamente la primera vez que se abre la app), y ninguna de las dos cosas viene del lado del niño en la app. El único otro flujo son los datos de compra que llegan a un proveedor de servicios, descritos en «Analítica de compras» (incluido el identificador de proveedor del dispositivo, un identificador persistente), solo después de que una persona adulta pase la puerta parental, y solo para las operaciones internas que se nombran allí. Como RevenueCat sigue activo el resto de esa sesión, sus peticiones en segundo plano pueden continuar mientras un niño juega; no llevan nada sobre tu hijo o hija.</li>''',
   'when': '''<li><strong>Cuándo se activa la analítica de compras:</strong> solo después de que una persona adulta pase la puerta parental y compre o restaure una suscripción, o abra la pantalla de suscripción de un plan caducado o la pantalla de suscripción dentro de la Zona para padres (ambas tras esa puerta). Abrir solo la Zona para padres no activa nada. Nunca en un dispositivo que un adulto haya indicado que es el propio del niño, y nunca cuando Apple le diga a Yaybo que la cuenta es de un menor. La puerta para adultos sirve para que los niños no entren en las pantallas de adultos; Yaybo no recoge de un niño información personal que necesite el consentimiento de un padre o madre.</li>''',
   'rights': '''puedes rechazar la analítica de compras no comprando ni restaurando desde Yaybo y sin abrir la pantalla de suscripción (abrir solo la Zona para padres no activa nada), y puedes escribirnos para pedir que se borre lo que RevenueCat tiene de tu dispositivo; ''',
   'keep': '''<li><strong>En RevenueCat:</strong> usamos estos registros solo para registrar y verificar las compras de suscripción y para contar suscriptores de forma agregada, y los conservamos solo mientras los necesitamos para facturación, reembolsos, soporte y registros legales. Si nos lo pides, pedimos a RevenueCat que borre el registro de tu dispositivo y buscamos que quede borrado en un máximo de 30 días desde tu petición. RevenueCat no indica un plazo fijo de conservación de los datos de usuarios finales, y borrar Yaybo no borra lo que ya tiene: escribe a <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>. No conservamos esta información para ningún otro fin ni indefinidamente.</li>''',
   'protect': '''El acceso a nuestro servidor, a App Store Connect (que Apple protege con verificación en dos pasos) y al panel de RevenueCat se limita a los desarrolladores de Seize que trabajan en Yaybo, con verificación en dos pasos.''',
   'leaves': '''<li><strong>Analítica de compras.</strong> Solo después de que una persona adulta pase la puerta y compre, restaure o abra la pantalla de suscripción, nunca en el dispositivo propio de un niño. Va a RevenueCat, un proveedor de servicios estadounidense; véase «Analítica de compras (RevenueCat)» más abajo.</li>''',
   'leaves_tail': '''El único otro servicio de terceros que recibe algo es RevenueCat, descrito más abajo.''',
   'age': ''' y para mantener la analítica de compras fuera del dispositivo propio de un niño''',
  },
 },
 'off': {
  'en': {
   'short': "Yaybo sends no purchase data to any analytics service.",
   'section': '''<h2>Purchases</h2>
  <p>Yaybo's code includes a purchase-analytics library (RevenueCat), but this version ships without the key that switches it on, so the library never starts and sends nothing. Yaybo contains no advertising or tracking software. Apple processes the payment. We never see your card or your Apple Account details, and we receive no purchase data. Apple, not Yaybo, decides whether a subscription is active.</p>''',
   'collect': '''<li><strong>What we collect from a child:</strong> nothing. The learning data above stays on the family's devices and in their own iCloud. What reaches us is what a parent chooses to send (a note) or what Apple sends about an ad (an anonymous token, posted automatically the first time the app opens), and neither comes from the child's side of the app. Yaybo sends no purchase data to any analytics service.</li>''',
   'when': '', 'rights': '',
   'keep': '''<li><strong>Purchases:</strong> Apple keeps the record of a purchase under your Apple Account; we receive none of it.</li>''',
   'protect': '''Access to our server and to App Store Connect (which Apple protects with two-factor authentication) is limited to the named Seize developers who work on Yaybo, with two-factor authentication.''',
   'leaves': '', 'leaves_tail': '', 'age': '',
  },
  'es': {
   'short': "Yaybo no envía datos de compra a ningún servicio de analítica.",
   'section': '''<h2>Compras</h2>
  <p>El código de Yaybo incluye una biblioteca de analítica de compras (RevenueCat), pero esta versión se publica sin la clave que la activa, así que la biblioteca nunca arranca y no envía nada. Yaybo no contiene software de publicidad ni de seguimiento. Apple procesa el pago. Nunca vemos tu tarjeta ni los datos de tu cuenta de Apple, y no recibimos datos de compra. Es Apple, no Yaybo, quien decide si una suscripción está activa.</p>''',
   'collect': '''<li><strong>Qué recogemos de un menor:</strong> nada. Los datos de aprendizaje de arriba se quedan en los dispositivos de la familia y en su propio iCloud. Lo que nos llega es lo que una persona adulta elige enviar (una nota) o lo que Apple envía sobre un anuncio (un token anónimo, enviado automáticamente la primera vez que se abre la app), y ninguna de las dos cosas viene del lado del niño en la app. Yaybo no envía datos de compra a ningún servicio de analítica.</li>''',
   'when': '', 'rights': '',
   'keep': '''<li><strong>Compras:</strong> Apple guarda el registro de una compra en tu cuenta de Apple; nosotros no recibimos nada de él.</li>''',
   'protect': '''El acceso a nuestro servidor y a App Store Connect (que Apple protege con verificación en dos pasos) se limita a los desarrolladores de Seize que trabajan en Yaybo, con verificación en dos pasos.''',
   'leaves': '', 'leaves_tail': '', 'age': '',
  },
 },
}


def fill(text, lang):
    r = RC[RC_STATE][lang]
    for k, v in (('RC_SHORT', r['short']), ('RC_SECTION', r['section']), ('COPPA_COLLECT', r['collect']),
                 ('COPPA_WHEN', r['when']), ('LEAVES_RC', r['leaves']), ('LEAVES_RC_TAIL', r['leaves_tail']), ('AGE_RC', r['age']), ('RIGHTS_RC', r['rights']), ('KEEP_RC', r['keep']), ('PROTECT_RC', r['protect']),
                 ('ADDRESS', OPERATOR_ADDRESS[lang]), ('PHONE', OPERATOR_PHONE), ('SUBS_PATH', SUBSCRIPTIONS_PATH[lang])):
        text = text.replace('@@' + k + '@@', v)
    assert '@@' not in text, text[text.index('@@'):][:80]
    return text

PRIVACY = {
'en': '''
  <p class="eyebrow">Yaybo · Legal</p>
  <h1>Yaybo privacy policy</h1>
  <p class="effective">Last updated: October 16, 2026</p>
  <p>Yaybo is a learning app for children ages 4 to 9 (Pre-K to 3rd grade), used with a grown-up. This page is written for parents and guardians. It says what Yaybo keeps, where it keeps it, what leaves your devices, who can see it and how you delete it. Yaybo is offered in the United States and Canada.</p>

  <h2>The short version</h2>
  <ul>
    <li>What you tell Yaybo about your child (first name, grade, answers, progress) stays on your devices and, when iCloud Sync is on, in your own iCloud. It never reaches Seize: we cannot read it.</li>
    <li>Yaybo has no accounts, no email sign-up, no ads, no tracking and no third-party advertising or social SDKs.</li>
    <li>Yaybo never records, stores or sends your child's voice. If a grown-up turns on Read-aloud, your device listens on its own while your child holds a button, and the sound is dropped at once. A grown-up can also tell Yaybo never to listen to one particular child.</li>
    <li>Two small things go to our own server, neither about your child: a note you choose to write to us, and an anonymous token from Apple that lets us tell which ad, if any, brought you (sent the first time Yaybo opens).</li>
    <li>@@RC_SHORT@@</li>
    <li>You can share the weekly report with another grown-up through your own iCloud, only if you choose to; that grown-up can then send your child high-fives, signed with a name they pick.</li>
    <li>You can review and delete everything Yaybo keeps, in the Parent Zone, behind the grown-up gate.</li>
  </ul>

  <h2>Who we are</h2>
  <p>Yaybo is published on the App Store by <strong>Izotz Cristobal Mota</strong>, trading as Seize Apps, in the Basque Country, Spain. We are the operator of Yaybo for the purposes of the U.S. Children's Online Privacy Protection Act (COPPA) and responsible for the information described on this page. Write to us about anything here at <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>. Please do not put your child's name or details in an email.</p>
  <p>Operator contact, as the COPPA online notice requires: Izotz Cristobal Mota, trading as Seize Apps, @@ADDRESS@@, telephone @@PHONE@@, <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</p>
  <!-- OPERATOR: postal address and telephone are Izotz's own public facts (16 CFR 312.4(d)(1)); the defaults live in OPERATOR_ADDRESS / OPERATOR_PHONE below, and YAYBO_OPERATOR_ADDRESS / YAYBO_OPERATOR_PHONE override them. tools/check_yaybo_legal.py fails while an [OPERATOR ...] marker is in the page. -->

  <h2>What Yaybo keeps, and where</h2>
  <p>Yaybo keeps this on your devices and, when iCloud Sync is on, in your own private iCloud database. That database is Apple's and is yours: Seize cannot read it. It is why a second iPhone or iPad signed in to the same Apple Account shows the same family. iCloud Sync is on by default; you can turn it off in Parent Zone › Settings, and the change applies the next time Yaybo opens.</p>
  <ul>
    <li>your child's first name (or the nickname you choose), grade level and, if you pick one, the U.S. state (families outside the U.S. can answer "outside the U.S.");</li>
    <li>the answers you gave while setting up, including anything you chose to share about how your child learns;</li>
    <li>your child's progress, rewards, island and streak;</li>
    <li>recordings of your own voice that you make for your child: a high-five (up to 5 seconds) and, for School words, a word of this week's spelling list (up to 3 seconds);</li>
    <li>the spelling words you type;</li>
    <li>the choices you make in the Parent Zone, including whether Yaybo may ever listen to a child (see "The microphone"; the Read-aloud switch itself stays on the one device).</li>
  </ul>
  <p>Because this stays on your devices and in your own iCloud, Seize does not collect it. Yaybo does not ask for a last name, birth date, photo, email address or any account. Yaybo uses the state you pick, never the device's location.</p>

  <h2>The microphone</h2>
  <p>Yaybo asks for the microphone only on grown-up screens, behind the grown-up gate, and never at launch. When iOS asks, it shows this message: "Yaybo uses the microphone to record the voice notes and school words you choose and, only if you turn on Read-aloud in the Parent Zone, to listen while your child reads. What your child says is never recorded or sent."</p>
  <ul>
    <li><strong>Recording your own voice</strong> for a high-five (Parent Zone, or the linked viewer if you share with another grown-up) or for a spelling word (Parent Zone › Settings › School words). The recording stays on your devices and in your own iCloud when iCloud Sync is on, and in the shared space if you share; it is never sent to Seize.</li>
    <li><strong>Read-aloud (optional, off until a grown-up turns it on in the Parent Zone, per device).</strong> When it is on, your child can read a word or a story page out loud: your device listens only while your child holds a button (6 seconds at most) and decides, using Apple's speech recognition (SpeechAnalyzer) on the device itself, whether it heard the word. The sound is not recorded, saved or sent, and no text of it is kept. It never marks an answer wrong: when it is not sure, Yaybo reads the word aloud and your child checks it themselves. The first time you turn Read-aloud on, iOS downloads Apple's speech model to your device; that download comes from Apple and carries none of your child's data.</li>
    <li><strong>Never listen (per child).</strong> Each child has a "Never listen" switch in Parent Zone › Settings › Read-aloud. When it is on, Yaybo never opens the microphone for that child, on any device and even if Read-aloud is on, and your child taps "I said it" instead. That choice is kept with the child's profile, so it follows the child to your other devices through your own iCloud when Sync is on.</li>
  </ul>

  <h2>What Yaybo never collects</h2>
  <p>Last name; birth date; photos or camera; <strong>audio of your child</strong> (see "The microphone": it is processed on the device and dropped); location (Yaybo uses the state you pick, never the device's location); email address or any account; free text about your child; the advertising identifier (IDFA); App Tracking Transparency prompts. Yaybo does not track you or your child across other companies' apps and websites, and there are no chat or social features through which a stranger could reach your child.</p>

  <h2>Notifications and Apple's age category</h2>
  <ul>
    <li><strong>Notifications.</strong> Reminders go to the grown-up, not to the child, and are scheduled on your device. We run no push-notification server. Yaybo asks for permission only on grown-up screens, and you can say no.</li>
    <li><strong>Apple's age category.</strong> In places where a state law asks app stores and apps to handle age (today Texas, Utah and Louisiana), Apple may tell Yaybo which age category your Apple Account belongs to. Yaybo keeps the answer in memory only, never stores it, never sends it to anyone and never uses it to change what a child sees. It is used only to decide who approves a purchase@@AGE_RC@@.</li>
  </ul>

  <h2>What leaves your device</h2>
  <ul>
    <li><strong>A note you write.</strong> Only if you open Parent Zone › Settings › Help, pass the grown-up gate and tap Send. It goes to our own server (Seize's Supabase project, Frankfurt, Germany) and carries your note, the app version and build, the iOS version, the device model and the language. No email address, no name, nothing about your child. Its text is also forwarded to a private Telegram chat that only the developer reads (see "Notes you send us").</li>
    <li><strong>An email you write.</strong> Only if you tap "Suggest a Feature" or "Report a Bug" in Parent Zone › Settings (behind the grown-up gate, after a notice asking you not to include your child's name) or write to us yourself. Your email app sends it from your own address: we receive what you write, your address and, for "Report a Bug", the app version, iOS version and device model that the message starts with. Yaybo sends nothing itself, and we use the email only to answer you.</li>
    <li><strong>Apple Ads attribution.</strong> The first time Yaybo opens (if that attempt fails, once more at the next launch, then never) and once for each subscription it finds active on the device (a purchase, the free trial or a restore; never one shared through Family Sharing). It goes to the same server and carries Apple's anonymous attribution token (never your name or Apple Account) and, for a subscription, its original transaction number. This post is not behind the grown-up gate: it happens as the app opens, on whoever's device it is, whether or not an ad brought you; see "Where our ads came from".</li>
    @@LEAVES_RC@@
    <li><strong>The payment.</strong> When you subscribe, handled entirely by Apple; we never see your card or your Apple Account details.</li>
  </ul>
  <p>Nothing else leaves: no third-party advertising SDK, no advertising identifier, no tracking. The text of a note also reaches Telegram, described under "Notes you send us". @@LEAVES_RC_TAIL@@</p>

  <h2>Notes you send us</h2>
  <p>If you, the parent, write to us from the Parent Zone, we receive your note, the app version, the iOS version, the device model and the language. We do not receive your name, your email address, your child's name or anything from your child's profile. When you send us a note from the Parent Zone, its text is also forwarded to a private Telegram chat that only the developer reads, so we can read it quickly. Telegram (Telegram Messenger Inc.) is used only to deliver the note to the developer; it does not receive the app version, build, iOS version, device model or language that travel with the note. Please don't include your child's full name or other personal details in the note. To limit abuse we keep a one-way hash of the date and your network address for two days; the address itself is not stored by us, though our hosting provider logs it for its standard log window. Please do not include your child's information: we delete any we find. The note sheet warns you on the device if it sees your child's name, and closes after five minutes without an edit. Notes are deleted from our server 12 months after you send them. To have a note deleted sooner, email <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a> with roughly when you sent it and a few words of it. We cannot answer notes sent from the app; to hear back, email us.</p>
  <!-- CONFIRM: the log window of Seize's Supabase hosting plan (counsel Q-FBK-3). -->

  <h2>Where our ads came from</h2>
  <p>Apple gives every app a small anonymous token, through its AdServices framework, that says whether the install came from an Apple Ads ad. It needs no permission prompt and carries no advertising identifier. The first time Yaybo opens, it posts that token, and nothing else, to Seize's own server (once more after "Delete all data", which starts the attribution afresh). That happens as the app opens, before anything a grown-up does, because the token is only useful early; the token carries nothing about your child, and nothing a child entered is involved.</p>
  <p>Our server passes the token on to Apple's attribution service, which answers which campaign, ad group, keyword and ad the install came from, and the country or region and date of the click. If no ad brought the install, we store nothing. If one did, we store that answer, together with a one-way hash of the token to drop a duplicate, and never the token itself. We do not receive who you are, and we do not share the token or the answer.</p>
  <p>For each subscription Yaybo finds active on the device (a purchase, the free trial or a restore), the app also sends the App Store's purchase reference (the original transaction number), never for one shared through Family Sharing, and Apple tells our server when a subscription starts, renews or ends (the event, the product, the price and that reference; never a name, an email address or an Apple Account), so we can tell which keywords paid for themselves. We keep this for 12 months. It is not used to track you across other companies' apps or websites, and nothing from your child's side of the app is involved.</p>

  @@RC_SECTION@@

  <h2>Sharing with another grown-up (optional)</h2>
  <p>If you, the parent, link another person's phone from the Parent Zone (Settings › Other phones › Link a parent's phone), Yaybo puts your child's first name, avatar choice, this week's and last week's report (counts and plain-English skill names) and any high-fives that person sends into your own iCloud, and shares that space only with the people you invite through Apple's sharing sheet. The invited person needs an iCloud account and sees a grown-ups-only view: no lessons, no purchases. We, Seize, do not receive any of it and cannot see it. You can stop sharing at any time (the same screen, "Stop sharing"), which removes the shared space; deleting a child or all data removes it too. A high-five that has been delivered to your device leaves iCloud after 14 days.</p>
  <p>A high-five is a sticker, a phrase or a short note (80 characters at most) and, if the sender records one, a voice note of up to 5 seconds. The first time a linked phone sends one, it asks the grown-up how to sign their letters ("Sign your letters as": Mom, Dad, Grandma, Grandpa or a first name of up to 20 characters). That choice stays on that phone, each high-five carries it, and your child's screen says who the letter is from.</p>
  <p>Without sharing, you can also send a week's report to yourself, as plain text or as a picture, with the iOS share sheet; where it goes from there is your choice, and Seize receives nothing.</p>

  <h2>Children's privacy (COPPA) and Canada</h2>
  <p>Yaybo is directed to children under 13 and is built to collect no personal information from them.</p>
  <ul>
    <li><strong>Operator:</strong> Izotz Cristobal Mota, trading as Seize Apps, @@ADDRESS@@, telephone @@PHONE@@, <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</li>
    @@COPPA_COLLECT@@
    <li><strong>When Yaybo contacts our server on its own:</strong> once, the first time it opens, to post Apple's anonymous ad token (see "Where our ads came from"), and once for each subscription it finds active on the device, to post the purchase reference. A note goes only when a grown-up sends one.</li>
    @@COPPA_WHEN@@
    <li><strong>Who can reach your child:</strong> nobody you have not chosen. Yaybo has no chat, no social features, no ads and no links out that a child can open without the grown-up gate. The one exception is a high-five from a grown-up you yourself invite through the family link (see "Sharing with another grown-up"): a sticker, a short phrase or note and an optional voice note, which appears in your child's mailbox in the app. You can stop sharing at any time.</li>
    <li><strong>Your rights, as a parent or guardian (and under Canada's PIPEDA and Quebec's Law 25 for families there):</strong> you can review everything Yaybo keeps for a child in the Parent Zone; you can delete one child (the child's "Delete…" menu in Parent Zone › Children) or everything ("Delete all data" in Settings, which also removes anything shared and the note on the device of which ad brought you to Yaybo), and deleting stays possible when a subscription has ended (Grown-ups › Your child's data, on the plans screen, no purchase needed); you can refuse optional features (Read-aloud and linking a phone are off until you turn them on, and you can tell Yaybo never to listen to a particular child); @@RIGHTS_RC@@you can ask us anything at <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>. Please do not put your child's name in an email.</li>
    <li><strong>Canada:</strong> Yaybo is offered to Canadian families in English. The grown-up screens and this page also have a Spanish translation, and there is no French version. Your information is processed in the United States and Germany by Apple, our service provider and our server host, as described above. The person responsible for privacy at Seize Apps is Izotz Cristobal Mota, <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</li>
  </ul>

  <h2>Keeping and deleting data</h2>
  <ul>
    <li><strong>Your child's name, answers, progress, rewards, and your voice recordings and School words:</strong> on your devices and in your own iCloud, kept until you delete them. "Delete…" on a child, or "Delete all data", in the Parent Zone removes them from your devices and, when iCloud Sync is on, from your iCloud and your other devices too (when Sync is off, a copy already in iCloud is not touched: turn Sync on and open Yaybo first if you want it removed); a School list can also be deleted on its own. Deleting the app alone removes it from that device but leaves any iCloud copy: remove that in Settings › [your name] › iCloud › Manage Account Storage. If you back up your device (iCloud Backup or a computer), the backup may hold a copy; that backup is yours, kept by Apple under your Apple Account. Deleting your data does not cancel a subscription: that is in <strong>@@SUBS_PATH@@</strong>.</li>
    <li><strong>The shared report, your child's name and high-fives, if you share:</strong> in your own iCloud, shared with the people you invite, until you stop sharing (Parent Zone › Settings › Other phones › Link a parent's phone › Stop sharing) or delete; a delivered high-five leaves iCloud after 14 days.</li>
    <li><strong>Notes you send us:</strong> on our server for 12 months; to have one deleted sooner, email <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</li>
    <li><strong>The ad-attribution answer and the purchase reference:</strong> on our server for 12 months; email <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a> to have them deleted sooner.</li>
    <li><strong>Yaybo's own record that it already sent the ad token and the purchase reference:</strong> on your device, until you choose "Delete all data" (the app calls it "the note of which ad brought you to Yaybo"). It is not on our server; what is there is in the line above.</li>
    <li><strong>The abuse-limit hash:</strong> on our server for 2 days, then automatic.</li>
    @@KEEP_RC@@
  </ul>

  <h2>Selling, sharing and tracking</h2>
  <p>We do not sell your personal information or your child's, and we do not share it for advertising across other companies' apps and websites. Yaybo does not track you, so there is nothing to opt out of.</p>

  <h2>How we protect it</h2>
  <p>The learning data never leaves your devices and your own iCloud, which Seize cannot read. @@PROTECT_RC@@</p>
  <!-- SECURITY PROGRAM: do NOT add "Seize keeps a written information-security program" until docs/kids-us/release/information-security-program.md in the SeizeRepo is signed by Izotz (16 CFR 312.8); tools/check_yaybo_legal.py reads the signature line. -->

  <h2>Changes</h2>
  <p>If we change what Yaybo collects, we will update this page and its date, and we will not start collecting a child's personal information without first following the notice and parental-consent rules of COPPA.</p>

  <h2>Contact</h2>
  <p>Seize Apps · Izotz Cristobal Mota<br><a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a> · seizeapps.com</p>
''',
'es': '''
  <p class="eyebrow">Yaybo · Legal</p>
  <h1>Política de privacidad de Yaybo</h1>
  <p class="effective">Última actualización: 16 de octubre de 2026</p>
  <p><em>Yaybo se publica en la App Store de Estados Unidos y de Canadá y su política principal está en inglés. Esta es una traducción de cortesía: si hay alguna diferencia, vale la versión en inglés.</em></p>
  <p>Yaybo es una app para aprender, pensada para niños de 4 a 9 años (de Pre-K a 3.º de primaria de EE. UU.) y para usar con una persona adulta. Esta página está escrita para madres, padres y tutores: dice qué guarda Yaybo, dónde lo guarda, qué sale de tus dispositivos, quién puede verlo y cómo se borra. Yaybo se ofrece en Estados Unidos y en Canadá.</p>

  <h2>La versión corta</h2>
  <ul>
    <li>Lo que le cuentas a Yaybo sobre tu hijo o hija (nombre de pila, curso, respuestas, progreso) se queda en tus dispositivos y, si la sincronización con iCloud está activada, en tu propio iCloud. Nunca llega a Seize: no podemos leerlo.</li>
    <li>Yaybo no tiene cuentas, ni registro por correo, ni anuncios, ni seguimiento, ni SDK de publicidad o redes sociales de terceros.</li>
    <li>Yaybo nunca graba, guarda ni envía la voz de tu hijo o hija. Si una persona adulta activa la lectura en voz alta, tu dispositivo escucha por sí solo mientras tu hijo o hija mantiene pulsado un botón, y el sonido se descarta al instante. Una persona adulta también puede indicar a Yaybo que no escuche nunca a un niño o niña concreto.</li>
    <li>Dos cosas pequeñas van a nuestro propio servidor, ninguna sobre tu hijo o hija: una nota que eliges escribirnos y un token anónimo de Apple que nos permite saber qué anuncio, si lo hubo, te trajo (se envía la primera vez que Yaybo se abre).</li>
    <li>@@RC_SHORT@@</li>
    <li>Puedes compartir el informe semanal con otra persona adulta a través de tu propio iCloud, solo si lo eliges; esa persona podrá enviar choques de manos a tu hijo o hija, firmados con el nombre que ella elija.</li>
    <li>Puedes ver y borrar todo lo que guarda Yaybo en la Zona para padres, tras la puerta para adultos.</li>
  </ul>

  <h2>Quiénes somos</h2>
  <p>Yaybo la publica en la App Store <strong>Izotz Cristobal Mota</strong>, con el nombre comercial Seize Apps, en el País Vasco (España). Somos el operador de Yaybo a efectos de la ley estadounidense de protección de la privacidad infantil en línea (COPPA) y los responsables de la información que describe esta página. Escríbenos sobre cualquier cosa de aquí a <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>. Por favor, no pongas en un correo el nombre ni los datos de tu hijo o hija.</p>
  <p>Contacto del operador, como exige el aviso en línea de COPPA: Izotz Cristobal Mota, con el nombre comercial Seize Apps, @@ADDRESS@@, teléfono @@PHONE@@, <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</p>

  <h2>Qué guarda Yaybo, y dónde</h2>
  <p>Yaybo guarda esto en tus dispositivos y, si la sincronización con iCloud está activada, en tu propia base de datos privada de iCloud. Esa base de datos es de Apple y es tuya: Seize no puede leerla. Por eso un segundo iPhone o iPad con la misma cuenta de Apple muestra la misma familia. La sincronización con iCloud viene activada por defecto; puedes desactivarla en Zona para padres › Ajustes, y el cambio se aplica la próxima vez que se abra Yaybo.</p>
  <ul>
    <li>el nombre de pila de tu hijo o hija (o el apodo que elijas), su curso y, si eliges uno, el estado de EE. UU. (las familias de fuera de EE. UU. pueden responder «fuera de EE. UU.»);</li>
    <li>las respuestas que diste al configurar la app, incluido lo que quisieras contar sobre cómo aprende;</li>
    <li>su progreso, sus premios, su isla y su racha;</li>
    <li>grabaciones de tu propia voz que haces para tu hijo o hija: un choque de manos (hasta 5 segundos) y, en las Palabras de la escuela, una palabra de la lista de ortografía de esta semana (hasta 3 segundos);</li>
    <li>las palabras de ortografía que escribes;</li>
    <li>las decisiones que tomas en la Zona para padres, incluido si Yaybo puede escuchar alguna vez a un niño o niña (véase «El micrófono»; el interruptor de lectura en voz alta se queda en ese único dispositivo).</li>
  </ul>
  <p>Como esto se queda en tus dispositivos y en tu propio iCloud, Seize no lo recoge. Yaybo no pide apellidos, fecha de nacimiento, fotos, correo electrónico ni ninguna cuenta. Yaybo usa el estado que eliges, nunca la ubicación del dispositivo.</p>

  <h2>El micrófono</h2>
  <p>Yaybo pide el micrófono solo en pantallas de personas adultas, tras la puerta para adultos, y nunca al abrir la app. Cuando iOS lo pide, muestra este mensaje: «Yaybo usa el micrófono para grabar las notas de voz y las palabras de la escuela que elijas. Solo si activas «Lectura en voz alta» en la Zona para padres, también lo usa para escuchar mientras tu hijo o hija lee. Lo que dice tu hijo o hija nunca se graba ni se envía.»</p>
  <ul>
    <li><strong>Grabar tu propia voz</strong> para un choque de manos (Zona para padres, o el visor vinculado si compartes con otra persona adulta) o para una palabra de ortografía (Zona para padres › Ajustes › Palabras de la escuela). La grabación se queda en tus dispositivos y, si la sincronización con iCloud está activada, en tu propio iCloud, y en el espacio compartido si compartes; nunca se envía a Seize.</li>
    <li><strong>Lectura en voz alta (opcional, desactivada hasta que una persona adulta la active en la Zona para padres, en cada dispositivo).</strong> Cuando está activada, tu hijo o hija puede leer en voz alta una palabra o una página de un cuento: tu dispositivo escucha solo mientras tu hijo o hija mantiene pulsado un botón (6 segundos como máximo) y decide, con el reconocimiento de voz de Apple (SpeechAnalyzer) en el propio dispositivo, si ha oído la palabra. El sonido no se graba, no se guarda ni se envía, y no se conserva ningún texto de él. Nunca marca una respuesta como incorrecta: cuando no está seguro, Yaybo lee la palabra en voz alta y tu hijo o hija lo comprueba por sí mismo. La primera vez que activas la lectura en voz alta, iOS descarga a tu dispositivo el modelo de voz de Apple; esa descarga viene de Apple y no lleva ningún dato de tu hijo o hija.</li>
    <li><strong>No escuchar nunca (por niño).</strong> Cada niño o niña tiene un interruptor «No escuchar nunca a mi hijo o hija» en Zona para padres › Ajustes › Lectura en voz alta. Cuando está activado, Yaybo no abre nunca el micrófono para ese niño o niña, en ningún dispositivo y aunque la lectura en voz alta esté activada, y en su lugar toca «I said it». Esa decisión se guarda con el perfil del niño o niña, así que le sigue a tus otros dispositivos a través de tu propio iCloud cuando la sincronización está activada.</li>
  </ul>

  <h2>Qué no recoge nunca Yaybo</h2>
  <p>Apellidos; fecha de nacimiento; fotos o cámara; <strong>audio de tu hijo o hija</strong> (véase «El micrófono»: se procesa en el dispositivo y se descarta); ubicación (Yaybo usa el estado que eliges, nunca la ubicación del dispositivo); correo electrónico o cuenta alguna; texto libre sobre tu hijo o hija; el identificador publicitario (IDFA); avisos de App Tracking Transparency. Yaybo no te sigue ni a ti ni a tu hijo o hija por las apps y webs de otras empresas, y no tiene chat ni funciones sociales por las que un desconocido pudiera llegar hasta él o ella.</p>

  <h2>Notificaciones y la categoría de edad de Apple</h2>
  <ul>
    <li><strong>Notificaciones.</strong> Los recordatorios van a la persona adulta, no al niño, y se programan en tu dispositivo. No tenemos servidor de notificaciones push. Yaybo pide el permiso solo en pantallas de personas adultas, y puedes decir que no.</li>
    <li><strong>La categoría de edad de Apple.</strong> Donde una ley estatal pide a las tiendas y a las apps gestionar la edad (hoy Texas, Utah y Luisiana), Apple puede decirle a Yaybo a qué categoría de edad pertenece tu cuenta de Apple. Yaybo guarda la respuesta solo en memoria, no la almacena, no la envía a nadie y no la usa para cambiar lo que ve un niño. Se usa solo para decidir quién aprueba una compra@@AGE_RC@@.</li>
  </ul>

  <h2>Qué sale de tu dispositivo</h2>
  <ul>
    <li><strong>Una nota que escribes.</strong> Solo si abres Zona para padres › Ajustes › Ayuda, pasas la puerta para adultos y pulsas Enviar. Va a nuestro propio servidor (el proyecto de Supabase de Seize, en Fráncfort, Alemania) y lleva tu nota, la versión y la compilación de la app, la versión de iOS, el modelo del dispositivo y el idioma. Ni dirección de correo, ni nombre, ni nada sobre tu hijo o hija. Su texto se reenvía además a un chat privado de Telegram que solo lee el desarrollador (véase «Notas que nos envías»).</li>
    <li><strong>Un correo que escribes.</strong> Solo si pulsas «Sugerir una función» o «Reportar un error» en Zona para padres › Ajustes (tras la puerta para adultos y un aviso que pide no incluir el nombre de tu hijo o hija) o nos escribes tú por tu cuenta. Tu app de correo lo envía desde tu propia dirección: recibimos lo que escribes, tu dirección y, con «Reportar un error», la versión de la app, la versión de iOS y el modelo del dispositivo con los que empieza el mensaje. Yaybo no envía nada por sí misma, y usamos el correo solo para responderte.</li>
    <li><strong>Atribución de Apple Ads.</strong> La primera vez que Yaybo se abre (si ese intento falla, una vez más en el siguiente arranque y nunca más) y una vez por cada suscripción que encuentre activa en el dispositivo (una compra, la prueba gratuita o una restauración; nunca una compartida mediante Compartir en familia). Va al mismo servidor y lleva el token anónimo de atribución de Apple (nunca tu nombre ni tu cuenta de Apple) y, con una suscripción, su número de transacción original. Este envío no está tras la puerta para adultos: ocurre al abrirse la app, en el dispositivo de quien sea, haya o no un anuncio detrás; véase «De dónde venían nuestros anuncios».</li>
    @@LEAVES_RC@@
    <li><strong>El pago.</strong> Cuando te suscribes, lo gestiona por completo Apple; nunca vemos tu tarjeta ni los datos de tu cuenta de Apple.</li>
  </ul>
  <p>No sale nada más: ningún SDK de publicidad de terceros, ningún identificador publicitario, ningún seguimiento. El texto de una nota llega además a Telegram, como se describe en «Notas que nos envías». @@LEAVES_RC_TAIL@@</p>

  <h2>Notas que nos envías</h2>
  <p>Si tú, madre, padre o tutor, nos escribes desde la Zona para padres, recibimos tu nota, la versión de la app, la versión de iOS, el modelo del dispositivo y el idioma. No recibimos tu nombre, tu correo electrónico, el nombre de tu hijo o hija ni nada de su perfil. Cuando nos envías una nota desde la Zona para padres, su texto se reenvía además a un chat privado de Telegram que solo lee el desarrollador, para que podamos leerla enseguida. Telegram (Telegram Messenger Inc.) se usa únicamente para hacer llegar la nota al desarrollador; no recibe la versión de la app, la compilación, la versión de iOS, el modelo del dispositivo ni el idioma que viajan con la nota. Por favor, no incluyas en la nota el nombre completo de tu hijo o hija ni otros datos personales. Para limitar abusos guardamos dos días un hash irreversible de la fecha y de tu dirección de red; nosotros no guardamos la dirección, aunque nuestro proveedor de alojamiento la registra durante el plazo habitual de sus registros. Por favor, no incluyas información de tu hijo o hija: borramos la que encontremos. La hoja de la nota te avisa en el dispositivo si ve el nombre de tu hijo o hija, y se cierra tras cinco minutos sin cambios. Las notas se borran de nuestro servidor 12 meses después de enviarlas. Para que borremos una antes, escribe a <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a> con más o menos cuándo la enviaste y unas palabras de ella. No podemos responder a las notas enviadas desde la app; para recibir respuesta, escríbenos por correo.</p>

  <h2>De dónde venían nuestros anuncios</h2>
  <p>Apple da a cada app un pequeño token anónimo, mediante su framework AdServices, que dice si la instalación vino de un anuncio de Apple Ads. No necesita ningún aviso de permiso y no lleva ningún identificador publicitario. La primera vez que Yaybo se abre, envía ese token, y nada más, al servidor propio de Seize (una vez más tras «Eliminar todos los datos», que reinicia la atribución). Ocurre al abrirse la app, antes de cualquier cosa que haga una persona adulta, porque el token solo sirve al principio; el token no lleva nada sobre tu hijo o hija, y no interviene nada que un niño haya introducido.</p>
  <p>Nuestro servidor pasa el token al servicio de atribución de Apple, que responde de qué campaña, grupo de anuncios, palabra clave y anuncio venía la instalación, y el país o región y la fecha del clic. Si ningún anuncio trajo la instalación, no guardamos nada. Si lo hubo, guardamos esa respuesta, junto con un hash irreversible del token para descartar un duplicado, y nunca el token en sí. No recibimos quién eres, y no compartimos ni el token ni la respuesta.</p>
  <p>Por cada suscripción que Yaybo encuentre activa en el dispositivo (una compra, la prueba gratuita o una restauración), la app envía además la referencia de compra de la App Store (el número de transacción original), nunca en una compartida mediante Compartir en familia, y Apple avisa a nuestro servidor cuando una suscripción empieza, se renueva o termina (el evento, el producto, el precio y esa referencia; nunca un nombre, un correo ni una cuenta de Apple), para que podamos saber qué palabras clave se pagaron solas. Lo conservamos 12 meses. No se usa para seguirte por las apps o webs de otras empresas, y no interviene nada del lado de tu hijo o hija en la app.</p>

  @@RC_SECTION@@

  <h2>Compartir con otra persona adulta (opcional)</h2>
  <p>Si tú, madre, padre o tutor, vinculas el teléfono de otra persona desde la Zona para padres (Ajustes › Otros teléfonos › Vincular el teléfono de un padre o madre), Yaybo pone el nombre de pila de tu hijo o hija, el avatar elegido, el informe de esta semana y de la pasada (recuentos y nombres de habilidades en lenguaje claro) y los choques de manos que esa persona envíe en tu propio iCloud, y comparte ese espacio solo con las personas que invites mediante la hoja de compartir de Apple. La persona invitada necesita una cuenta de iCloud y ve una vista solo para personas adultas: sin lecciones ni compras. Nosotros, Seize, no recibimos nada de esto ni podemos verlo. Puedes dejar de compartir cuando quieras (en la misma pantalla, «Dejar de compartir»), lo que elimina el espacio compartido; borrar a un niño o todos los datos también lo elimina. Un choque de manos ya entregado en tu dispositivo sale de iCloud a los 14 días.</p>
  <p>Un choque de manos es una pegatina, una frase o una nota corta (80 caracteres como máximo) y, si quien lo envía la graba, una nota de voz de hasta 5 segundos. La primera vez que un teléfono vinculado envía uno, pregunta a la persona adulta cómo quiere firmar sus cartas («Firmar tus cartas como»: Mamá, Papá, Abuela, Abuelo o un nombre de pila de hasta 20 caracteres). Esa elección se queda en ese teléfono, cada choque de manos la lleva y la pantalla de tu hijo o hija dice de quién es la carta.</p>
  <p>Sin compartir, también puedes enviarte a ti mismo el informe de una semana, como texto o como imagen, con la hoja de compartir de iOS; adónde va después es decisión tuya, y Seize no recibe nada.</p>

  <h2>Privacidad de los menores (COPPA) y Canadá</h2>
  <p>Yaybo está dirigida a menores de 13 años y está hecha para no recoger información personal de ellos.</p>
  <ul>
    <li><strong>Operador:</strong> Izotz Cristobal Mota, con el nombre comercial Seize Apps, @@ADDRESS@@, teléfono @@PHONE@@, <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</li>
    @@COPPA_COLLECT@@
    <li><strong>Cuándo Yaybo contacta con nuestro servidor por su cuenta:</strong> una vez, la primera vez que se abre, para enviar el token anónimo de anuncios de Apple (véase «De dónde venían nuestros anuncios»), y una vez por cada suscripción que encuentre activa en el dispositivo, para enviar la referencia de compra. Una nota solo va cuando una persona adulta la envía.</li>
    @@COPPA_WHEN@@
    <li><strong>Quién puede llegar hasta tu hijo o hija:</strong> nadie que tú no hayas elegido. Yaybo no tiene chat, ni funciones sociales, ni anuncios, ni enlaces externos que un niño pueda abrir sin la puerta para adultos. La única excepción es un choque de manos de una persona adulta a quien invitas tú misma o mismo mediante el vínculo familiar (véase «Compartir con otra persona adulta»): una pegatina, una frase o nota corta y una nota de voz opcional, que aparece en el buzón de tu hijo o hija en la app. Puedes dejar de compartir cuando quieras.</li>
    <li><strong>Tus derechos, como madre, padre o tutor (y, para las familias de allí, según la PIPEDA de Canadá y la Ley 25 de Quebec):</strong> puedes ver en la Zona para padres todo lo que Yaybo guarda de un niño; puedes borrar a un niño (el menú «Eliminar…» del niño en Zona para padres › Niños) o todo («Eliminar todos los datos» en Ajustes, que también elimina lo que esté compartido y la nota en el dispositivo de qué anuncio te trajo a Yaybo), y borrar sigue siendo posible cuando una suscripción ha terminado (Adultos › Los datos de tu hijo o hija, en la pantalla de planes, sin comprar nada); puedes rechazar las funciones opcionales (la lectura en voz alta y vincular un teléfono están desactivadas hasta que las actives, y puedes indicar a Yaybo que no escuche nunca a un niño o niña concreto); @@RIGHTS_RC@@y puedes preguntarnos lo que quieras en <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>. Por favor, no pongas el nombre de tu hijo o hija en un correo.</li>
    <li><strong>Canadá:</strong> Yaybo se ofrece a las familias canadienses en inglés. Las pantallas para personas adultas y esta página tienen además una traducción al castellano, y no hay versión en francés. Tu información la tratan en Estados Unidos y Alemania Apple, nuestro proveedor de servicios y el alojamiento de nuestro servidor, como se describe arriba. La persona responsable de la privacidad en Seize Apps es Izotz Cristobal Mota, <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</li>
  </ul>

  <h2>Conservación y borrado de los datos</h2>
  <ul>
    <li><strong>El nombre de tu hijo o hija, las respuestas, el progreso, los premios, y tus grabaciones de voz y Palabras de la escuela:</strong> en tus dispositivos y en tu propio iCloud, hasta que los borres. «Eliminar…» en un niño, o «Eliminar todos los datos», en la Zona para padres los quita de tus dispositivos y, si la sincronización con iCloud está activada, también de tu iCloud y de tus otros dispositivos (con la sincronización desactivada, una copia que ya esté en iCloud no se toca: activa la sincronización y abre Yaybo antes si quieres quitarla); una lista de la escuela también se puede borrar por separado. Borrar solo la app la quita de ese dispositivo pero deja cualquier copia de iCloud: quítala en Ajustes › [tu nombre] › iCloud › Gestionar almacenamiento de la cuenta. Si haces copia de seguridad del dispositivo (copia de iCloud o en un ordenador), la copia puede contener una versión; esa copia es tuya, la guarda Apple en tu cuenta de Apple. Borrar tus datos no cancela una suscripción: eso se hace en <strong>@@SUBS_PATH@@</strong>.</li>
    <li><strong>El informe compartido, el nombre de tu hijo o hija y los choques de manos, si compartes:</strong> en tu propio iCloud, compartidos con las personas que invites, hasta que dejes de compartir (Zona para padres › Ajustes › Otros teléfonos › Vincular el teléfono de un padre o madre › Dejar de compartir) o borres; un choque de manos entregado sale de iCloud a los 14 días.</li>
    <li><strong>Las notas que nos envías:</strong> en nuestro servidor 12 meses; para que borremos una antes, escribe a <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</li>
    <li><strong>La respuesta de atribución y la referencia de compra:</strong> en nuestro servidor 12 meses; escribe a <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a> para que se borren antes.</li>
    <li><strong>El registro propio de Yaybo de que ya envió el token de anuncios y la referencia de compra:</strong> en tu dispositivo, hasta que elijas «Eliminar todos los datos» (la app lo llama «la nota de qué anuncio te trajo a Yaybo»). No está en nuestro servidor; lo que hay allí está en la línea anterior.</li>
    <li><strong>El hash contra abusos:</strong> en nuestro servidor 2 días, y luego se borra solo.</li>
    @@KEEP_RC@@
  </ul>

  <h2>Venta, cesión y seguimiento</h2>
  <p>No vendemos tu información personal ni la de tu hijo o hija, y no la cedemos para publicidad en las apps y webs de otras empresas. Yaybo no te sigue, así que no hay nada a lo que darse de baja.</p>

  <h2>Cómo la protegemos</h2>
  <p>Los datos de aprendizaje nunca salen de tus dispositivos ni de tu propio iCloud, que Seize no puede leer. @@PROTECT_RC@@</p>

  <h2>Cambios</h2>
  <p>Si cambiamos lo que recoge Yaybo, actualizaremos esta página y su fecha, y no empezaremos a recoger información personal de un menor sin cumplir antes las reglas de aviso y consentimiento parental de COPPA.</p>

  <h2>Contacto</h2>
  <p>Seize Apps · Izotz Cristobal Mota<br><a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a> · seizeapps.com</p>
''',
}

TERMS = {
'en': '''
  <p class="eyebrow">Yaybo · Legal</p>
  <h1>Yaybo terms of use</h1>
  <p class="effective">Effective October 16, 2026</p>
  <p>These terms are for the grown-up who sets up and pays for Yaybo. They sit on top of Apple's standard <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Licensed Application End User License Agreement</a>, which applies to anything these terms don't cover. How Yaybo treats your family's data is in the <a href="../privacy/">Yaybo privacy policy</a>. These terms are linked from Yaybo's App Store description.</p>

  <h2>1. Who we are, and who these terms are for</h2>
  <p>Yaybo is published on the App Store by Izotz Cristobal Mota, trading as Seize Apps, in the Basque Country, Spain ("we", "us"). You must be a parent or legal guardian, and at least 18, to set Yaybo up, to subscribe and to accept these terms. Children use Yaybo only with, and under the supervision of, a grown-up. Yaybo is offered on the United States and Canadian App Stores.</p>

  <h2>2. What Yaybo is, and is not</h2>
  <p>Yaybo is a daily learning plan for children in Pre-K to 3rd grade: phonics, reading, spelling, math, money, time and handwriting, practiced in short sessions. It is practice, not schooling. It is not a test, an assessment of your child's abilities, a diagnosis or professional advice, and we cannot promise any result. What you tell Yaybo about how your child learns is used only to shape practice. If you have a concern about your child's development, please speak to a teacher or a qualified professional.</p>

  <h2>3. The Yaybo Plus subscription</h2>
  <ul>
    <li><strong>What it is.</strong> Yaybo Plus is an auto-renewing subscription, weekly or yearly, that unlocks Yaybo's learning activities. One plan covers up to four children in your family, on your devices and, through Apple Family Sharing, on those of the family members you share with.</li>
    <li><strong>Price and length.</strong> The price and length of each plan are shown on the plan screen before you confirm, and Apple shows them again when you buy. Payment is charged to your Apple Account when you confirm the purchase.</li>
    <li><strong>Renewal.</strong> A subscription renews automatically for the same length unless you cancel at least 24 hours before the end of the current period. Apple charges the renewal within 24 hours before the period ends.</li>
    <li><strong>Free trial.</strong> New subscribers to the yearly plan who are eligible get a 7-day free trial, once per Apple Account. If you do not cancel at least 24 hours before the trial ends, it turns into the paid yearly subscription. The weekly plan has no trial. Any unused part of a free trial is forfeited when you buy a subscription.</li>
    <li><strong>Managing and cancelling.</strong> Manage or cancel in <strong>@@SUBS_PATH@@</strong> on your device. Cancelling stops the next renewal; you keep access until the end of the period you have paid for. Deleting the app does not cancel the subscription.</li>
    <li><strong>Refunds.</strong> Apple handles payments and refunds, under the App Store's refund policy (reportaproblem.apple.com). We cannot issue refunds directly.</li>
    <li><strong>If the plan ends.</strong> Your child's island, stars and progress are kept, and are back the moment a grown-up renews; the learning activities close until then. Nothing your child made is deleted because a plan ended.</li>
    <li><strong>Restore.</strong> "Restore" on the plan screen brings back a subscription you already own, on a new device or after reinstalling.</li>
    <li><strong>Purchases by minors.</strong> Where Apple's family or age settings require a parent's approval for a purchase, the purchase waits for that approval and completes by itself when it is given.</li>
  </ul>

  <h2>4. The grown-up gate, and supervising your child</h2>
  <p>Everything that costs money, opens a link or an email, or changes your family's data sits behind a grown-up gate: a short challenge a young child is not meant to pass. The gate helps, but you are responsible for supervising how your child uses their device, including Screen Time, Ask to Buy and what else is installed on it.</p>

  <h2>5. Your family's information stays yours</h2>
  <p>What you enter in Yaybo, and what your child makes in it, is yours. As the <a href="../privacy/">privacy policy</a> describes, it is stored on your devices and, when iCloud Sync is on, in your own iCloud, and we have no access to it, which also means you are responsible for keeping your own backups. You can delete a child, or everything, in the Parent Zone.</p>

  <h2>6. Content, and what is ours</h2>
  <p>Yaybo, its characters (including Yaybo the axolotl), artwork, voices, lessons and code are ours or used under licence. We grant you a personal, non-exclusive, non-transferable licence to use Yaybo on Apple devices you own or control, as the App Store terms permit. Don't copy, resell or reverse-engineer them, and don't use Yaybo in a way that breaks the law or Apple's terms.</p>

  <h2>7. Warranty and liability</h2>
  <p>Yaybo is provided "as is", without warranties of any kind. To the maximum extent permitted by law, we are not liable for indirect or consequential damages arising from your use of Yaybo; our total liability is limited to the amount you paid for Yaybo in the twelve months before the claim. Nothing in these terms limits rights that consumer law grants you and that cannot be waived.</p>

  <h2>8. Changes</h2>
  <p>We may update these terms as Yaybo evolves; the current version always lives at this address with its effective date above. Continued use after a change means you accept the updated terms.</p>

  <h2>9. Governing law</h2>
  <p>These terms are governed by the laws of Spain. You also keep any rights that the law of the place where you live gives you and that cannot be waived by contract.</p>
  <!-- CONFIRM: governing law for a US-only consumer app (the studio-wide terms say Spain); on the counsel list (docs/kids-us §5.4). -->

  <h2>Contact</h2>
  <p><a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a></p>
''',
'es': '''
  <p class="eyebrow">Yaybo · Legal</p>
  <h1>Condiciones de uso de Yaybo</h1>
  <p class="effective">En vigor desde el 16 de octubre de 2026</p>
  <p><em>Yaybo se publica en las App Store de Estados Unidos y de Canadá y sus condiciones principales están en inglés. Esta es una traducción de cortesía: si hay alguna diferencia, vale la versión en inglés.</em></p>
  <p>Estas condiciones son para la persona adulta que configura y paga Yaybo. Se suman al <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Contrato de licencia de usuario final de la aplicación con licencia</a> estándar de Apple, que se aplica a todo lo que estas condiciones no cubran. Cómo trata Yaybo los datos de tu familia está en la <a href="../privacidad/">política de privacidad de Yaybo</a>. Estas condiciones se enlazan desde la descripción de Yaybo en la App Store.</p>

  <h2>1. Quiénes somos y a quién se dirigen estas condiciones</h2>
  <p>Yaybo la publica en la App Store Izotz Cristobal Mota, con el nombre comercial Seize Apps, en el País Vasco (España) («nosotros»). Para configurar Yaybo, suscribirte y aceptar estas condiciones debes ser madre, padre o tutor legal y tener al menos 18 años. Los niños usan Yaybo solo con una persona adulta y bajo su supervisión. Yaybo se ofrece en las App Store de Estados Unidos y de Canadá.</p>

  <h2>2. Qué es Yaybo, y qué no es</h2>
  <p>Yaybo es un plan diario de aprendizaje para niños de Pre-K a 3.º de primaria (de EE. UU.): fonética, lectura, ortografía, matemáticas, dinero, hora y escritura a mano, practicados en sesiones cortas. Es práctica, no escolarización. No es un examen, una evaluación de las capacidades de tu hijo o hija, un diagnóstico ni un consejo profesional, y no podemos prometer ningún resultado. Lo que le cuentas a Yaybo sobre cómo aprende tu hijo o hija sirve solo para dar forma a la práctica. Si algo te preocupa del desarrollo de tu hijo o hija, habla con su docente o con un profesional cualificado.</p>

  <h2>3. La suscripción Yaybo Plus</h2>
  <ul>
    <li><strong>Qué es.</strong> Yaybo Plus es una suscripción de renovación automática, semanal o anual, que desbloquea las actividades de aprendizaje de Yaybo. Un plan cubre hasta cuatro niños de tu familia, en tus dispositivos y, mediante Compartir en familia de Apple, en los de los miembros de la familia con quienes lo compartas.</li>
    <li><strong>Precio y duración.</strong> El precio y la duración de cada plan se muestran en la pantalla del plan antes de que confirmes, y Apple vuelve a mostrarlos al comprar. El pago se carga en tu cuenta de Apple al confirmar la compra.</li>
    <li><strong>Renovación.</strong> La suscripción se renueva automáticamente por el mismo periodo salvo que la canceles al menos 24 horas antes de que termine el periodo en curso. Apple cobra la renovación en las 24 horas anteriores al final del periodo.</li>
    <li><strong>Prueba gratuita.</strong> Quienes se suscriben por primera vez al plan anual y cumplen los requisitos tienen una prueba gratuita de 7 días, una vez por cuenta de Apple. Si no cancelas al menos 24 horas antes de que acabe la prueba, se convierte en la suscripción anual de pago. El plan semanal no tiene prueba. La parte no usada de una prueba gratuita se pierde al comprar una suscripción.</li>
    <li><strong>Gestionar y cancelar.</strong> Gestiónala o cancélala en <strong>@@SUBS_PATH@@</strong> de tu dispositivo. Cancelar detiene la siguiente renovación; conservas el acceso hasta el final del periodo ya pagado. Borrar la app no cancela la suscripción.</li>
    <li><strong>Reembolsos.</strong> Apple gestiona los pagos y los reembolsos, según su política de reembolsos de la App Store (reportaproblem.apple.com). Nosotros no podemos reembolsar directamente.</li>
    <li><strong>Si el plan termina.</strong> La isla, las estrellas y el progreso de tu hijo o hija se conservan y vuelven en cuanto una persona adulta renueve; las actividades de aprendizaje se cierran hasta entonces. Nada de lo que haya hecho tu hijo o hija se borra porque termine un plan.</li>
    <li><strong>Restaurar.</strong> «Restaurar» en la pantalla del plan recupera una suscripción que ya tienes, en un dispositivo nuevo o tras reinstalar.</li>
    <li><strong>Compras de menores.</strong> Cuando los ajustes de familia o de edad de Apple exigen la aprobación de un padre o madre para una compra, la compra espera esa aprobación y se completa sola cuando se da.</li>
  </ul>

  <h2>4. La puerta para adultos y la supervisión de tu hijo o hija</h2>
  <p>Todo lo que cuesta dinero, abre un enlace o un correo, o cambia los datos de tu familia está tras una puerta para adultos: un reto corto que un niño pequeño no debería superar. La puerta ayuda, pero la supervisión de cómo usa tu hijo o hija su dispositivo es tuya, incluido Tiempo de uso, Pedir permiso para comprar y qué más hay instalado.</p>

  <h2>5. La información de tu familia sigue siendo tuya</h2>
  <p>Lo que introduces en Yaybo, y lo que tu hijo o hija crea en ella, es tuyo. Como describe la <a href="../privacidad/">política de privacidad</a>, se guarda en tus dispositivos y, si la sincronización con iCloud está activada, en tu propio iCloud, y nosotros no tenemos acceso, lo que también significa que las copias de seguridad son cosa tuya. Puedes borrar a un niño, o todo, en la Zona para padres.</p>

  <h2>6. Contenido, y qué es nuestro</h2>
  <p>Yaybo, sus personajes (incluido Yaybo, el ajolote), ilustraciones, voces, lecciones y código son nuestros o se usan con licencia. Te concedemos una licencia personal, no exclusiva e intransferible para usar Yaybo en dispositivos Apple que poseas o controles, según permiten las condiciones de la App Store. No los copies, revendas ni descompiles, y no uses Yaybo de forma que incumpla la ley o las condiciones de Apple.</p>

  <h2>7. Garantía y responsabilidad</h2>
  <p>Yaybo se ofrece «tal cual», sin garantías de ningún tipo. En la máxima medida que permite la ley, no respondemos de daños indirectos o consecuentes derivados de tu uso de Yaybo; nuestra responsabilidad total se limita al importe que hayas pagado por Yaybo en los doce meses anteriores a la reclamación. Nada de estas condiciones limita los derechos que la ley de consumo te concede y que no se pueden renunciar.</p>

  <h2>8. Cambios</h2>
  <p>Podemos actualizar estas condiciones a medida que Yaybo evolucione; la versión vigente está siempre en esta dirección, con su fecha de entrada en vigor arriba. Seguir usando Yaybo tras un cambio significa que aceptas las condiciones actualizadas.</p>

  <h2>9. Ley aplicable</h2>
  <p>Estas condiciones se rigen por la ley española. Conservas además los derechos que te dé la ley del lugar donde vives y que no se puedan renunciar por contrato.</p>

  <h2>Contacto</h2>
  <p><a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a></p>
''',
}

# (lang, kind, slug, title, description)
PAGES = [
    ('en', 'privacy', 'privacy', 'Yaybo privacy policy — Seize Apps',
     'Yaybo privacy and children’s privacy (COPPA): what you tell Yaybo about your child stays on your devices and your own iCloud; no ads, no tracking, your child’s voice is never recorded.'),
    ('es', 'privacy', 'privacidad', 'Política de privacidad de Yaybo — Seize Apps',
     'Privacidad de Yaybo y privacidad infantil (COPPA): lo que cuentas sobre tu hijo o hija se queda en tus dispositivos y en tu propio iCloud; sin anuncios, sin seguimiento, la voz de tu hijo o hija nunca se graba.'),
    ('en', 'terms', 'terms', 'Yaybo terms of use — Seize Apps',
     'Terms of use for Yaybo, including the Yaybo Plus subscription, the free trial on the yearly plan, the grown-up gate and refunds.'),
    ('es', 'terms', 'condiciones', 'Condiciones de uso de Yaybo — Seize Apps',
     'Condiciones de uso de Yaybo: la suscripción Yaybo Plus, la prueba gratuita del plan anual, la puerta para adultos y los reembolsos.'),
]


def build_yaybo():
    for kind, texts in (('privacy', PRIVACY), ('terms', TERMS)):
        slugs = {lang: slug for lang, k, slug, _, _ in PAGES if k == kind}
        alts = {L: f'https://seizeapps.com/yaybo/{s}/' for L, s in slugs.items()}
        for lang, k, slug, title, desc in PAGES:
            if k != kind:
                continue
            root = '../../'
            canonical = f'yaybo/{slug}/'
            switch = {L: f'{root}yaybo/{s}/' for L, s in slugs.items()}
            html = (head(lang, title, desc, root, canonical, alts=alts) + header(lang, root, canonical, switch=switch)
                    + legal_main(lang, fill(texts[lang], lang)) + footer(lang, root))
            write(f'yaybo/{slug}/index.html', html)
