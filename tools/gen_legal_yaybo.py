"""Yaybo's own privacy policy and terms (11/10/2026).

Yaybo is the one Seize app made for children (ages 4 to 8, used with a grown-up), so it can't live under the
studio-wide policy: it needs a COPPA notice. The text comes from docs/kids-us/12-privacy-page.md in the SeizeRepo
(branch feat/kids-us-app); every sentence about RevenueCat is docs/kids-us/11-revenuecat-disclosure.md §3.2, word
for word where it matters. Change those two first, then this file.

Paths follow Atino's convention (English at the root of the app's folder, castellano beside it):
  /yaybo/privacy/      /yaybo/privacidad/     privacy policy with the COPPA section
  /yaybo/terms/        /yaybo/condiciones/    terms of use (the paywall's own Terms link is Apple's standard EULA)
Built with gen_site's chrome; run `python3 tools/gen_site.py`, which calls build_yaybo().
The CONFIRM notes are facts only Izotz can supply; they stay in the generated HTML as comments.
"""
import os
from gen_site import head, header, footer, write, legal_main

# What the page says depends on two facts about the build that ships; the page must describe THAT build (Guideline 2.3.1,
# the COPPA notice must be accurate). Both are Izotz's decisions, so they are switches, not edits:
#   YAYBO_REVENUECAT=on|off   whether the archive carries a REVENUECAT_API_KEY (docs/kids-us/11-revenuecat-disclosure.md).
#                             Recommended for 0.1.0: off. The default stays "on" so the page is never softer than the code.
#   iCloud: 0.1.0 keeps data on the device (YayboStore.cloudKitSchemaDeployed = false), so the page says so. When the
#           schema is deployed, edit the "device only" sentences (marked ICLOUD) in the same commit as the flag.
# The operator's postal address and phone are the COPPA notice's §312.4(d)(1) facts only Izotz can supply; until he does the
# page carries a visible marker and tools/check_yaybo_legal.py fails (so the PR cannot merge by accident).
RC_STATE = os.environ.get('YAYBO_REVENUECAT', 'on')
assert RC_STATE in ('on', 'off'), RC_STATE
OPERATOR_ADDRESS = os.environ.get('YAYBO_OPERATOR_ADDRESS', '[OPERATOR POSTAL ADDRESS]')
OPERATOR_PHONE = os.environ.get('YAYBO_OPERATOR_PHONE', '[OPERATOR PHONE]')
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
    "o abra la pantalla de suscripción de un plan caducado, o abra la pantalla de suscripción dentro de la Zona de padres "
    "(ambas tras esa puerta), y nunca en el dispositivo propio de un niño. Abrir solo la Zona de padres no activa nada. "
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
   'collect': '''<li><strong>What we collect from a child:</strong> nothing. The learning data above stays on the family's device. The only information that reaches a service provider is the purchase data described under "Purchase analytics" (including the device's vendor identifier, a persistent identifier), only after a grown-up passes the parental gate, and used only for the internal operations named there. Because RevenueCat stays on for the rest of that session, its background requests can continue while a child plays; they carry nothing about your child.</li>''',
   'when': '''<li><strong>When purchase analytics turns on:</strong> only after a grown-up passes the parental gate and buys or restores a subscription, or opens the subscription screen of a lapsed plan or the subscription screen inside the Parent Zone (both behind that gate). Opening the Parent Zone alone starts nothing. Never on a device a grown-up told Yaybo is the child's own, and never where Apple tells Yaybo the account belongs to a minor. The grown-up gate is how Yaybo keeps children out of grown-up screens; Yaybo collects no personal information from a child that would need a parent's consent.</li>''',
   'rights': '''you can decline purchase analytics by not buying or restoring through Yaybo and by not opening the subscription screen (opening the Parent Zone alone starts nothing), and you can write to us to ask for what RevenueCat holds about your device to be deleted; ''',
   'keep': '''<li><strong>At RevenueCat:</strong> we use these records only to record and verify subscription purchases and to count subscribers in aggregate, and keep them only as long as we need them for billing, refunds, support and legal records. If you ask us, we ask RevenueCat to delete the record tied to your device, and we aim to have it deleted within 30 days of your request. RevenueCat states no fixed period for how long it keeps end-user data, and deleting Yaybo does not delete what it already holds: write to <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>. We do not keep this information for any other purpose or without end.</li>
    <!-- CONFIRM: the 30-day target and RevenueCat's retention terms / data processing agreement for Yaybo's RevenueCat project are not visible in the repo (privacy policy read June 2026: no fixed period for end-user data). Replace with RevenueCat's confirmed deletion timeframe, and COPPA §312.10 needs a concrete one. -->''',
   'protect': '''Access to App Store Connect (which Apple protects with two-factor authentication) and to the RevenueCat dashboard is limited to the Seize developers who work on Yaybo.''',
  },
  'es': {
   'short': "Si una persona adulta compra o restaura una suscripción, un servicio de analítica de compras ve la compra y los datos técnicos de tu dispositivo. Nunca nada sobre tu hijo o hija.",
   'section': '''<h2>Analítica de compras (RevenueCat)</h2>
  <p>''' + RC_PARAGRAPH_ES + '''</p>
  <p>RevenueCat es RevenueCat, Inc. El identificador de proveedor es un número que Apple da a las apps de un mismo desarrollador en un dispositivo; no es el identificador publicitario. El indicador de App Tracking Transparency es el estado del permiso de seguimiento del dispositivo: Yaybo nunca pide seguir, así que figura como «no determinado» salvo que tú o Tiempo de uso hayáis desactivado el seguimiento. Yaybo no define ningún atributo propio en RevenueCat. RevenueCat guarda estos datos en Estados Unidos.</p>
  <p>Apple procesa el pago. Nunca vemos tu tarjeta ni los datos de tu cuenta de Apple. Es Apple, no Yaybo ni RevenueCat, quien decide si una suscripción está activa.</p>''',
   'collect': '''<li><strong>Qué recogemos de un menor:</strong> nada. Los datos de aprendizaje de arriba se quedan en el dispositivo de la familia. Lo único que llega a un proveedor de servicios son los datos de compra descritos en «Analítica de compras» (incluido el identificador de proveedor del dispositivo, un identificador persistente), solo después de que una persona adulta pase la puerta parental, y solo para las operaciones internas que se nombran allí. Como RevenueCat sigue activo el resto de esa sesión, sus peticiones en segundo plano pueden continuar mientras un niño juega; no llevan nada sobre tu hijo o hija.</li>''',
   'when': '''<li><strong>Cuándo se activa la analítica de compras:</strong> solo después de que una persona adulta pase la puerta parental y compre o restaure una suscripción, o abra la pantalla de suscripción de un plan caducado o la pantalla de suscripción dentro de la Zona de padres (ambas tras esa puerta). Abrir solo la Zona de padres no activa nada. Nunca en un dispositivo que un adulto haya indicado que es el propio del niño, y nunca cuando Apple le diga a Yaybo que la cuenta es de un menor. La puerta para adultos sirve para que los niños no entren en las pantallas de adultos; Yaybo no recoge de un niño información personal que necesite el consentimiento de un padre o madre.</li>''',
   'rights': '''puedes rechazar la analítica de compras no comprando ni restaurando desde Yaybo y sin abrir la pantalla de suscripción (abrir solo la Zona de padres no activa nada), y puedes escribirnos para pedir que se borre lo que RevenueCat tiene de tu dispositivo; ''',
   'keep': '''<li><strong>En RevenueCat:</strong> usamos estos registros solo para registrar y verificar las compras de suscripción y para contar suscriptores de forma agregada, y los conservamos solo mientras los necesitamos para facturación, reembolsos, soporte y registros legales. Si nos lo pides, pedimos a RevenueCat que borre el registro de tu dispositivo y buscamos que quede borrado en un máximo de 30 días desde tu petición. RevenueCat no indica un plazo fijo de conservación de los datos de usuarios finales, y borrar Yaybo no borra lo que ya tiene: escribe a <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>. No conservamos esta información para ningún otro fin ni indefinidamente.</li>''',
   'protect': '''El acceso a App Store Connect (que Apple protege con verificación en dos pasos) y al panel de RevenueCat se limita a los desarrolladores de Seize que trabajan en Yaybo.''',
  },
 },
 'off': {
  'en': {
   'short': "Yaybo sends nothing about you or your child to any analytics, advertising or tracking service.",
   'section': '''<h2>Purchases</h2>
  <p>Yaybo contains no third-party analytics, advertising or tracking software. Apple processes the payment. We never see your card or your Apple Account details, and we receive no purchase data. Apple, not Yaybo, decides whether a subscription is active.</p>''',
   'collect': '''<li><strong>What we collect from a child:</strong> nothing. The learning data above stays on the family's device, and Yaybo sends no information about a child, or about the device, to Seize or to any third party.</li>''',
   'when': '', 'rights': '',
   'keep': '''<li><strong>Purchases:</strong> Apple keeps the record of a purchase under your Apple Account; we receive none of it.</li>''',
   'protect': '''Access to App Store Connect (which Apple protects with two-factor authentication) is limited to the Seize developers who work on Yaybo.''',
  },
  'es': {
   'short': "Yaybo no envía nada sobre ti ni sobre tu hijo o hija a ningún servicio de analítica, publicidad o seguimiento.",
   'section': '''<h2>Compras</h2>
  <p>Yaybo no contiene software de analítica, publicidad ni seguimiento de terceros. Apple procesa el pago. Nunca vemos tu tarjeta ni los datos de tu cuenta de Apple, y no recibimos datos de compra. Es Apple, no Yaybo, quien decide si una suscripción está activa.</p>''',
   'collect': '''<li><strong>Qué recogemos de un menor:</strong> nada. Los datos de aprendizaje de arriba se quedan en el dispositivo de la familia, y Yaybo no envía información sobre un niño, ni sobre el dispositivo, a Seize ni a ningún tercero.</li>''',
   'when': '', 'rights': '',
   'keep': '''<li><strong>Compras:</strong> Apple guarda el registro de una compra en tu cuenta de Apple; nosotros no recibimos nada de él.</li>''',
   'protect': '''El acceso a App Store Connect (que Apple protege con verificación en dos pasos) se limita a los desarrolladores de Seize que trabajan en Yaybo.''',
  },
 },
}


def fill(text, lang):
    r = RC[RC_STATE][lang]
    for k, v in (('RC_SHORT', r['short']), ('RC_SECTION', r['section']), ('COPPA_COLLECT', r['collect']),
                 ('COPPA_WHEN', r['when']), ('RIGHTS_RC', r['rights']), ('KEEP_RC', r['keep']), ('PROTECT_RC', r['protect']),
                 ('ADDRESS', OPERATOR_ADDRESS), ('PHONE', OPERATOR_PHONE), ('SUBS_PATH', SUBSCRIPTIONS_PATH[lang])):
        text = text.replace('@@' + k + '@@', v)
    assert '@@' not in text, text[text.index('@@'):][:80]
    return text

PRIVACY = {
'en': '''
  <p class="eyebrow">Yaybo · Legal</p>
  <h1>Yaybo privacy policy</h1>
  <p class="effective">Last updated: October 11, 2026</p>
  <p>Yaybo is a learning app for children ages 4 to 8, used with a grown-up. This page is written for parents and guardians. It says what Yaybo keeps, where it keeps it, what leaves your devices, and how you delete it. Yaybo is available on the United States App Store only.</p>

  <h2>The short version</h2>
  <ul>
    <li>What you tell Yaybo about your child stays on your device. We never receive it.</li>
    <li>Yaybo has no accounts, no email sign-up, no ads, no tracking and no third-party advertising or social SDKs.</li>
    <li>Yaybo never records your child's voice and never uses the camera, photos or location.</li>
    <li>@@RC_SHORT@@</li>
    <li>You can review and delete everything Yaybo keeps, in the Parent Zone, behind the grown-up gate.</li>
  </ul>

  <h2>Who we are</h2>
  <p>Yaybo is published on the App Store by <strong>Izotz Cristobal Mota</strong>, trading as Seize Apps, in the Basque Country, Spain. We are the operator of Yaybo for the purposes of the U.S. Children's Online Privacy Protection Act (COPPA) and responsible for the information described on this page. Write to us about anything here at <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>. Please do not put your child's name or details in an email.</p>
  <p>Operator contact, as the COPPA online notice requires: Izotz Cristobal Mota, trading as Seize Apps, @@ADDRESS@@, telephone @@PHONE@@, <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</p>
  <!-- OPERATOR: postal address and telephone are facts only Izotz can supply (16 CFR 312.4(d)(1)); set YAYBO_OPERATOR_ADDRESS and YAYBO_OPERATOR_PHONE when running tools/gen_site.py. tools/check_yaybo_legal.py fails while the markers are in the page. -->

  <h2>What Yaybo keeps, and where</h2>
  <p>Yaybo stores this on the device it runs on, and nowhere else:</p>
  <ul>
    <li>your child's first name (or the nickname you choose), grade level, age range and U.S. state;</li>
    <li>the answers you gave while setting up, including anything you chose to share about how your child learns;</li>
    <li>your child's progress, rewards, island and streak;</li>
    <li>voice notes you record for your child (your own recording, five seconds at most).</li>
  </ul>
  <p>Because this stays on your device, Seize does not collect it. Yaybo does not ask for a last name, birth date, photo, email address or any account. A later version may offer optional iCloud sync between your own devices; we will update this page before it does.</p>
  <!-- ICLOUD: 0.1.0 ships with YayboStore.cloudKitSchemaDeployed = false, so data is device-only. Flip these sentences in the same commit as the flag. -->
  <p>From the Parent Zone, behind the grown-up gate, a grown-up can send a progress report as a picture ("Send to my phone"). It shows your child's first name and progress, and it goes only where you send it, through Apple's share sheet; Yaybo does not send it anywhere.</p>

  <h2>What Yaybo never collects</h2>
  <p>Last name; birth date; photos or camera; <strong>audio of your child</strong> (Yaybo has no microphone use for children); location (Yaybo uses the state you pick, never the device's location); email address or any account; free text about your child; the advertising identifier (IDFA); App Tracking Transparency prompts. Yaybo does not track you or your child across other companies' apps and websites, and there are no chat, social or sharing features through which anyone could reach your child.</p>

  <h2>Microphone, notifications and Apple's age category</h2>
  <ul>
    <li><strong>Microphone.</strong> The only time Yaybo uses it is when a grown-up taps Record to leave a short voice note for the child, in the Parent Zone, behind the grown-up gate. Yaybo asks for permission then and not before. The recording stays on your device.</li>
    <li><strong>Notifications.</strong> Reminders go to the grown-up, not to the child, and are scheduled on your device. We run no push-notification server. Yaybo asks for permission right after a purchase, and you can say no.</li>
    <li><strong>Apple's age category.</strong> In places where a state law asks app stores and apps to handle age (today Texas, Utah and Louisiana), Apple may tell Yaybo which age category your Apple Account belongs to. Yaybo uses that only to follow the law: for a minor's account, the subscription screen explains that a parent approves the purchase through Apple. Yaybo keeps the answer in memory only, never stores it, never sends it to anyone and never uses it to change what a child sees.</li>
  </ul>

  @@RC_SECTION@@

  <h2>Children's privacy (COPPA)</h2>
  <p>Yaybo is directed to children under 13 and is built to collect no personal information from them.</p>
  <ul>
    <li><strong>Operator:</strong> Izotz Cristobal Mota, trading as Seize Apps, @@ADDRESS@@, telephone @@PHONE@@, <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</li>
    @@COPPA_COLLECT@@
    @@COPPA_WHEN@@
    <li><strong>Who can reach your child:</strong> nobody. Yaybo has no chat, no social features, no user-generated content shared with others, no ads and no links out that a child can open without the grown-up gate.</li>
    <li><strong>Your rights, as a parent or guardian:</strong> you can review everything Yaybo keeps for a child in the Parent Zone; you can delete one child ("Delete") or everything ("Delete all data"); @@RIGHTS_RC@@you can ask us anything at <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</li>
  </ul>

  <h2>Keeping and deleting data</h2>
  <ul>
    <li><strong>On your device:</strong> kept until you delete it. "Delete" on a child, or "Delete all data", in the Parent Zone removes the data from the device, and so does deleting the app. If you back up your device (iCloud Backup or a computer), the backup may hold a copy; that backup is yours, kept by Apple under your Apple Account, and you manage it in your device's backup settings. Deleting your data does not cancel a subscription: that is in <strong>@@SUBS_PATH@@</strong>.</li>
    @@KEEP_RC@@
    <li><strong>Our own servers:</strong> Seize runs none for Yaybo, so there is nothing else to delete.</li>
  </ul>

  <h2>Selling, sharing and tracking</h2>
  <p>We do not sell your personal information or your child's, and we do not share it for advertising across other companies' apps and websites. Yaybo does not track you, so there is nothing to opt out of.</p>

  <h2>How we protect it</h2>
  <p>The learning data never leaves your device. @@PROTECT_RC@@ Seize runs no server for Yaybo.</p>
  <!-- SECURITY PROGRAM: do NOT add "Seize keeps a written information-security program" until docs/kids-us/release/information-security-program.md in the SeizeRepo is signed by Izotz (16 CFR 312.8); tools/check_yaybo_legal.py reads the signature line. -->

  <h2>Changes</h2>
  <p>If we change what Yaybo collects, we will update this page and its date, and we will not start collecting a child's personal information without first following the notice and parental-consent rules of COPPA.</p>

  <h2>Contact</h2>
  <p>Seize Apps · Izotz Cristobal Mota<br><a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a> · seizeapps.com</p>
''',
'es': '''
  <p class="eyebrow">Yaybo · Legal</p>
  <h1>Política de privacidad de Yaybo</h1>
  <p class="effective">Última actualización: 11 de octubre de 2026</p>
  <p><em>Yaybo se publica en la App Store de Estados Unidos y su política principal está en inglés. Esta es una traducción de cortesía: si hay alguna diferencia, vale la versión en inglés.</em></p>
  <p>Yaybo es una app para aprender, pensada para niños de 4 a 8 años y para usar con una persona adulta. Esta página está escrita para madres, padres y tutores: dice qué guarda Yaybo, dónde lo guarda, qué sale de tus dispositivos y cómo se borra.</p>

  <h2>La versión corta</h2>
  <ul>
    <li>Lo que le cuentas a Yaybo sobre tu hijo o hija se queda en tu dispositivo. Nosotros nunca lo recibimos.</li>
    <li>Yaybo no tiene cuentas, ni registro por correo, ni anuncios, ni seguimiento, ni SDK de publicidad o redes sociales de terceros.</li>
    <li>Yaybo nunca graba la voz de tu hijo o hija y nunca usa la cámara, las fotos ni la ubicación.</li>
    <li>@@RC_SHORT@@</li>
    <li>Puedes ver y borrar todo lo que guarda Yaybo en la Zona de padres, tras la puerta para adultos.</li>
  </ul>

  <h2>Quiénes somos</h2>
  <p>Yaybo la publica en la App Store <strong>Izotz Cristobal Mota</strong>, con el nombre comercial Seize Apps, en el País Vasco (España). Somos el operador de Yaybo a efectos de la ley estadounidense de protección de la privacidad infantil en línea (COPPA) y los responsables de la información que describe esta página. Escríbenos sobre cualquier cosa de aquí a <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>. Por favor, no pongas en un correo el nombre ni los datos de tu hijo o hija.</p>
  <p>Contacto del operador, como exige el aviso en línea de COPPA: Izotz Cristobal Mota, con el nombre comercial Seize Apps, @@ADDRESS@@, teléfono @@PHONE@@, <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</p>

  <h2>Qué guarda Yaybo, y dónde</h2>
  <p>Yaybo guarda esto en el dispositivo en el que se ejecuta, y en ningún otro sitio:</p>
  <ul>
    <li>el nombre de pila de tu hijo o hija (o el apodo que elijas), su curso, su tramo de edad y su estado de EE. UU.;</li>
    <li>las respuestas que diste al configurar la app, incluido lo que quisieras contar sobre cómo aprende;</li>
    <li>su progreso, sus premios, su isla y su racha;</li>
    <li>las notas de voz que grabas para tu hijo o hija (tu propia grabación, de cinco segundos como máximo).</li>
  </ul>
  <p>Como esto se queda en tu dispositivo, Seize no lo recoge. Yaybo no pide apellidos, fecha de nacimiento, fotos, correo electrónico ni ninguna cuenta. Una versión futura podría ofrecer sincronización opcional con iCloud entre tus propios dispositivos; actualizaremos esta página antes de que lo haga.</p>
  <p>Desde la Zona de padres, tras la puerta para adultos, una persona adulta puede enviar un informe de progreso como imagen («Enviar a mi móvil»). Muestra el nombre de pila de tu hijo o hija y su progreso, y va solo adonde tú lo envíes, mediante la hoja de compartir de Apple; Yaybo no lo envía a ningún sitio.</p>

  <h2>Qué no recoge nunca Yaybo</h2>
  <p>Apellidos; fecha de nacimiento; fotos o cámara; <strong>audio de tu hijo o hija</strong> (Yaybo no usa el micrófono con niños); ubicación (Yaybo usa el estado que eliges, nunca la ubicación del dispositivo); correo electrónico o cuenta alguna; texto libre sobre tu hijo o hija; el identificador publicitario (IDFA); avisos de App Tracking Transparency. Yaybo no te sigue ni a ti ni a tu hijo o hija por las apps y webs de otras empresas, y no tiene chat, funciones sociales ni formas de compartir por las que alguien pudiera llegar hasta él o ella.</p>

  <h2>Micrófono, notificaciones y la categoría de edad de Apple</h2>
  <ul>
    <li><strong>Micrófono.</strong> Solo lo usa Yaybo cuando una persona adulta pulsa Grabar para dejar una nota de voz al niño o niña, en la Zona de padres y tras la puerta para adultos. Yaybo pide el permiso en ese momento y no antes. La grabación se queda en tu dispositivo.</li>
    <li><strong>Notificaciones.</strong> Los recordatorios van a la persona adulta, no al niño, y se programan en tu dispositivo. No tenemos servidor de notificaciones push. Yaybo pide el permiso justo después de una compra, y puedes decir que no.</li>
    <li><strong>La categoría de edad de Apple.</strong> Donde una ley estatal pide a las tiendas y a las apps gestionar la edad (hoy Texas, Utah y Luisiana), Apple puede decirle a Yaybo a qué categoría de edad pertenece tu cuenta de Apple. Yaybo lo usa solo para cumplir la ley: en la cuenta de un menor, la pantalla de suscripción explica que un padre o madre aprueba la compra a través de Apple. Yaybo guarda la respuesta solo en memoria, no la almacena, no la envía a nadie y no la usa para cambiar lo que ve un niño.</li>
  </ul>

  @@RC_SECTION@@

  <h2>Privacidad de los menores (COPPA)</h2>
  <p>Yaybo está dirigida a menores de 13 años y está hecha para no recoger información personal de ellos.</p>
  <ul>
    <li><strong>Operador:</strong> Izotz Cristobal Mota, con el nombre comercial Seize Apps, @@ADDRESS@@, teléfono @@PHONE@@, <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</li>
    @@COPPA_COLLECT@@
    @@COPPA_WHEN@@
    <li><strong>Quién puede llegar hasta tu hijo o hija:</strong> nadie. Yaybo no tiene chat, ni funciones sociales, ni contenido de usuarios compartido con otros, ni anuncios, ni enlaces externos que un niño pueda abrir sin la puerta para adultos.</li>
    <li><strong>Tus derechos, como madre, padre o tutor:</strong> puedes ver en la Zona de padres todo lo que Yaybo guarda de un niño; puedes borrar a un niño («Borrar») o todo («Borrar todos los datos»); @@RIGHTS_RC@@y puedes preguntarnos lo que quieras en <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</li>
  </ul>

  <h2>Conservación y borrado de los datos</h2>
  <ul>
    <li><strong>En tu dispositivo:</strong> se conservan hasta que los borres. «Borrar» un niño, o «Borrar todos los datos», en la Zona de padres quita los datos del dispositivo, y borrar la app también. Si haces copia de seguridad del dispositivo (copia de iCloud o en un ordenador), la copia puede contener una versión; esa copia es tuya, la guarda Apple en tu cuenta de Apple y la gestionas en los ajustes de copia del dispositivo. Borrar tus datos no cancela una suscripción: eso se hace en <strong>@@SUBS_PATH@@</strong>.</li>
    @@KEEP_RC@@
    <li><strong>Nuestros servidores:</strong> Seize no tiene ninguno para Yaybo, así que no hay nada más que borrar.</li>
  </ul>

  <h2>Venta, cesión y seguimiento</h2>
  <p>No vendemos tu información personal ni la de tu hijo o hija, y no la cedemos para publicidad en las apps y webs de otras empresas. Yaybo no te sigue, así que no hay nada a lo que darse de baja.</p>

  <h2>Cómo la protegemos</h2>
  <p>Los datos de aprendizaje nunca salen de tu dispositivo. @@PROTECT_RC@@ Seize no tiene ningún servidor para Yaybo.</p>

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
  <p class="effective">Effective October 11, 2026</p>
  <p>These terms are for the grown-up who sets up and pays for Yaybo. They sit on top of Apple's standard <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Licensed Application End User License Agreement</a>, which applies to anything these terms don't cover. How Yaybo treats your family's data is in the <a href="../privacy/">Yaybo privacy policy</a>. These terms are linked from Yaybo's App Store description.</p>

  <h2>1. Who we are, and who these terms are for</h2>
  <p>Yaybo is published on the App Store by Izotz Cristobal Mota, trading as Seize Apps, in the Basque Country, Spain ("we", "us"). You must be a parent or legal guardian, and at least 18, to set Yaybo up, to subscribe and to accept these terms. Children use Yaybo only with, and under the supervision of, a grown-up. Yaybo is available on the United States App Store only.</p>

  <h2>2. What Yaybo is, and is not</h2>
  <p>Yaybo is a daily learning plan for children in Pre-K to 2nd grade: phonics, reading, math, money, time and handwriting, practiced in short sessions. It is practice, not schooling. It is not a test, an assessment of your child's abilities, a diagnosis or professional advice, and we cannot promise any result. What you tell Yaybo about how your child learns is used only to shape practice. If you have a concern about your child's development, please speak to a teacher or a qualified professional.</p>

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
  <p>Everything that costs money, leaves the app or changes your family's data sits behind a grown-up gate: a short challenge a young child is not meant to pass. The gate helps, but you are responsible for supervising how your child uses their device, including Screen Time, Ask to Buy and what else is installed on it.</p>

  <h2>5. Your family's information stays yours</h2>
  <p>What you enter in Yaybo, and what your child makes in it, is yours. As the <a href="../privacy/">privacy policy</a> describes, it is stored on your device, and we have no access to it, which also means you are responsible for keeping your own backups. You can delete a child, or everything, in the Parent Zone.</p>

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
  <p class="effective">En vigor desde el 11 de octubre de 2026</p>
  <p><em>Yaybo se publica en la App Store de Estados Unidos y sus condiciones principales están en inglés. Esta es una traducción de cortesía: si hay alguna diferencia, vale la versión en inglés.</em></p>
  <p>Estas condiciones son para la persona adulta que configura y paga Yaybo. Se suman al <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Contrato de licencia de usuario final de la aplicación con licencia</a> estándar de Apple, que se aplica a todo lo que estas condiciones no cubran. Cómo trata Yaybo los datos de tu familia está en la <a href="../privacidad/">política de privacidad de Yaybo</a>. Estas condiciones se enlazan desde la descripción de Yaybo en la App Store.</p>

  <h2>1. Quiénes somos y a quién se dirigen estas condiciones</h2>
  <p>Yaybo la publica en la App Store Izotz Cristobal Mota, con el nombre comercial Seize Apps, en el País Vasco (España) («nosotros»). Para configurar Yaybo, suscribirte y aceptar estas condiciones debes ser madre, padre o tutor legal y tener al menos 18 años. Los niños usan Yaybo solo con una persona adulta y bajo su supervisión. Yaybo está disponible solo en la App Store de Estados Unidos.</p>

  <h2>2. Qué es Yaybo, y qué no es</h2>
  <p>Yaybo es un plan diario de aprendizaje para niños de Pre-K a 2.º de primaria (de EE. UU.): fonética, lectura, matemáticas, dinero, hora y escritura a mano, practicados en sesiones cortas. Es práctica, no escolarización. No es un examen, una evaluación de las capacidades de tu hijo o hija, un diagnóstico ni un consejo profesional, y no podemos prometer ningún resultado. Lo que le cuentas a Yaybo sobre cómo aprende tu hijo o hija sirve solo para dar forma a la práctica. Si algo te preocupa del desarrollo de tu hijo o hija, habla con su docente o con un profesional cualificado.</p>

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
  <p>Todo lo que cuesta dinero, sale de la app o cambia los datos de tu familia está tras una puerta para adultos: un reto corto que un niño pequeño no debería superar. La puerta ayuda, pero la supervisión de cómo usa tu hijo o hija su dispositivo es tuya, incluido Tiempo de uso, Pedir permiso para comprar y qué más hay instalado.</p>

  <h2>5. La información de tu familia sigue siendo tuya</h2>
  <p>Lo que introduces en Yaybo, y lo que tu hijo o hija crea en ella, es tuyo. Como describe la <a href="../privacidad/">política de privacidad</a>, se guarda en tu dispositivo, y nosotros no tenemos acceso, lo que también significa que las copias de seguridad son cosa tuya. Puedes borrar a un niño, o todo, en la Zona de padres.</p>

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
     'Yaybo privacy and children’s privacy (COPPA): what you tell Yaybo about your child stays on your device; no ads, no tracking, no child audio.'),
    ('es', 'privacy', 'privacidad', 'Política de privacidad de Yaybo — Seize Apps',
     'Privacidad de Yaybo y privacidad infantil (COPPA): lo que cuentas sobre tu hijo o hija se queda en tu dispositivo; sin anuncios, sin seguimiento, sin audio de niños.'),
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
