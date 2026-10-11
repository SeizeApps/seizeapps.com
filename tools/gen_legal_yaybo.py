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
from gen_site import head, header, footer, write, legal_main

PRIVACY = {
'en': '''
  <p class="eyebrow">Yaybo · Legal</p>
  <h1>Yaybo privacy policy</h1>
  <p class="effective">Last updated: October 11, 2026</p>
  <p>Yaybo is a learning app for children ages 4 to 8, used with a grown-up. This page is written for parents and guardians. It says what Yaybo keeps, where it keeps it, what leaves your devices, and how you delete it. Yaybo is available on the United States App Store only.</p>

  <h2>The short version</h2>
  <ul>
    <li>What you tell Yaybo about your child stays on your devices and in your own iCloud. We never receive it.</li>
    <li>Yaybo has no accounts, no email sign-up, no ads, no tracking and no third-party advertising or social SDKs.</li>
    <li>Yaybo never records your child's voice and never uses the camera, photos or location.</li>
    <li>If you subscribe, a purchase-analytics service sees the purchase and your device's technical details. Never anything about your child.</li>
    <li>You can review and delete everything Yaybo keeps, in the Parent Zone, behind the grown-up gate.</li>
  </ul>

  <h2>Who we are</h2>
  <p>Yaybo is published on the App Store by <strong>Izotz Cristobal Mota</strong>, trading as Seize Apps, in the Basque Country, Spain. We are the operator of Yaybo for the purposes of the U.S. Children's Online Privacy Protection Act (COPPA) and responsible for the information described on this page. Write to us about anything here at <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>. Please do not put your child's name or details in an email.</p>
  <!-- CONFIRM: the COPPA online notice asks for the operator's name, postal address, telephone number and email address. Only the name, country and email are confirmed anywhere in the repo (same block as Atino's and Roomy's policies); add the postal address and a telephone number here if Izotz wants them on the page. -->

  <h2>What Yaybo keeps, and where</h2>
  <p>Yaybo stores this on your device, and in your private iCloud database (hosted by Apple; Seize has no access to it) so that a second iPhone or iPad signed in to the same Apple Account shows the same family:</p>
  <ul>
    <li>your child's first name (or the nickname you choose), grade level, age range and U.S. state;</li>
    <li>the answers you gave while setting up, including anything you chose to share about how your child learns;</li>
    <li>your child's progress, rewards, island and streak;</li>
    <li>voice notes you record for your child (your own recording, five seconds at most).</li>
  </ul>
  <p>Because this stays on your devices and in your iCloud, Seize does not collect it. iCloud sync is on by default and you can turn it off in the Parent Zone; with it off, the data stays on the device only. Yaybo does not ask for a last name, birth date, photo, email address or any account.</p>

  <h2>What Yaybo never collects</h2>
  <p>Last name; birth date; photos or camera; <strong>audio of your child</strong> (Yaybo has no microphone use for children); location (Yaybo uses the state you pick, never the device's location); email address or any account; free text about your child; the advertising identifier (IDFA); App Tracking Transparency prompts. Yaybo does not track you or your child across other companies' apps and websites, and there are no chat, social or sharing features through which anyone could reach your child.</p>

  <h2>Microphone, notifications and Apple's age category</h2>
  <ul>
    <li><strong>Microphone.</strong> The only time Yaybo uses it is when a grown-up taps Record to leave a short voice note for the child, in the Parent Zone, behind the grown-up gate. Yaybo asks for permission then and not before. The recording stays on your devices and in your iCloud.</li>
    <li><strong>Notifications.</strong> Reminders go to the grown-up, not to the child, and are scheduled on your device. We run no push-notification server. Yaybo asks for permission right after a purchase, and you can say no.</li>
    <li><strong>Apple's age category.</strong> In places where a state law asks app stores and apps to handle age (today Texas, Utah and Louisiana), Apple may tell Yaybo which age category your Apple Account belongs to. Yaybo uses that only to follow the law: for a minor's account, the subscription screen explains that a parent approves the purchase through Apple. Yaybo keeps the answer in memory only, never stores it, never sends it to anyone and never uses it to change what a child sees.</li>
  </ul>

  <h2>Purchase analytics (RevenueCat)</h2>
  <p>To understand how many families subscribe, Yaybo uses RevenueCat, a US purchase-analytics service (RevenueCat, Inc.). It is switched on only after a grown-up passes the parental gate to buy or restore a subscription (or opens the subscription screen or the Parent Zone behind that gate), never on a child's own device, and never while a child is playing. When it is on, RevenueCat receives an anonymous app user ID, the device's IP address, device and OS information, the device's vendor identifier (IDFV), the App Store storefront country, an App Tracking Transparency status flag, and the purchase itself. It never receives your child's name, age, answers or progress. After it has been switched on, it stays on until you close the app. We do not use these for advertising, we do not track you across other companies' apps, and RevenueCat acts only as our service provider.</p>
  <p>The vendor identifier is a number Apple gives the apps of one developer on a device; it is not the advertising identifier. The App Tracking Transparency flag is the device's tracking-permission status: Yaybo never asks to track, so it reads "not determined" unless you or Screen Time turned tracking off. Yaybo sets no attributes of its own in RevenueCat. RevenueCat stores this data in the United States.</p>
  <p>Apple processes the payment. We never see your card or your Apple Account details. Apple, not Yaybo or RevenueCat, decides whether a subscription is active.</p>
  <!-- CONFIRM: sentences above are docs/kids-us/11-revenuecat-disclosure.md §3.2; RevenueCat's storage in the United States (Amazon Web Services) is as read for Roomy and Atino on 6-7 October 2026. -->

  <h2>Children's privacy (COPPA)</h2>
  <p>Yaybo is directed to children under 13 and is built to collect no personal information from them.</p>
  <ul>
    <li><strong>Operator:</strong> Izotz Cristobal Mota, trading as Seize Apps, Basque Country, Spain, <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</li>
    <li><strong>What we collect from a child:</strong> nothing. The learning data above stays on the family's devices and iCloud. The only information that reaches a service provider is the purchase data described under "Purchase analytics", and only after a grown-up passes the parental gate.</li>
    <li><strong>Consent:</strong> the purchase-analytics step happens only after a grown-up passes the parental gate and buys or restores a subscription, or opens the subscription screen or the Parent Zone behind that gate, never on a device a grown-up told Yaybo is the child's own, and never where Apple tells Yaybo the account belongs to a minor.</li>
    <li><strong>Who can reach your child:</strong> nobody. Yaybo has no chat, no social features, no user-generated content shared with others, no ads and no links out that a child can open without the grown-up gate.</li>
    <li><strong>Your rights, as a parent or guardian:</strong> you can review everything Yaybo keeps for a child in the Parent Zone; you can delete one child ("Delete") or everything ("Delete all data"); you can decline purchase analytics by not buying or restoring through Yaybo and by leaving the subscription screen and the Parent Zone alone, and you can write to us to ask for what RevenueCat holds about your device to be deleted; you can ask us anything at <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</li>
  </ul>

  <h2>Keeping and deleting data</h2>
  <ul>
    <li><strong>On your devices and in your iCloud:</strong> kept until you delete it. "Delete" on a child, or "Delete all data", in the Parent Zone removes the data from the device and, while iCloud sync is on, from the family's iCloud (the deletion syncs to your other devices). The Parent Zone says whether iCloud is syncing. Deleting the app alone leaves the iCloud copy; you can remove it in <strong>Settings › Apple Account › iCloud › Manage Account Storage</strong>. Deleting your data does not cancel a subscription: that is in <strong>Settings › Apple Account › Subscriptions</strong>.</li>
    <!-- CONFIRM: the iCloud storage path is re-checked on the current iOS before publishing (spec §5.4). -->
    <li><strong>At RevenueCat:</strong> we keep purchase records only as long as we need them to show that a subscription existed (billing, refunds, support), and we use them for nothing else. RevenueCat states no fixed period for how long it keeps end-user data, and deleting Yaybo does not delete what it already holds: write to <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a> and we will ask it to delete the record tied to your device.</li>
    <!-- CONFIRM: RevenueCat's retention terms and our data processing agreement for Yaybo's RevenueCat project are not visible in the repo (privacy policy read June 2026: no fixed period for end-user data; DPA August 2026). State the period here once confirmed. -->
    <li><strong>Our own servers:</strong> Seize runs none for Yaybo, so there is nothing else to delete.</li>
  </ul>

  <h2>Selling, sharing and tracking</h2>
  <p>We do not sell your personal information or your child's, and we do not share it for advertising across other companies' apps and websites. Yaybo does not track you, so there is nothing to opt out of.</p>

  <h2>How we protect it</h2>
  <p>The learning data never leaves Apple's infrastructure (your device and your iCloud). Access to App Store Connect and to the RevenueCat dashboard is limited to named Seize developers with two-factor authentication. Seize keeps a written information-security program for Yaybo.</p>
  <!-- CONFIRM: "a written information-security program" must be true when this page is published (docs/kids-us/10-... document to be written in P10, release gate). Cut the last sentence if it does not exist yet. -->

  <h2>Changes</h2>
  <p>If we change what Yaybo collects, we will update this page and, if it touches your child's information, ask for your consent again inside the app before the change takes effect.</p>

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
    <li>Lo que le cuentas a Yaybo sobre tu hijo o hija se queda en tus dispositivos y en tu propio iCloud. Nosotros nunca lo recibimos.</li>
    <li>Yaybo no tiene cuentas, ni registro por correo, ni anuncios, ni seguimiento, ni SDK de publicidad o redes sociales de terceros.</li>
    <li>Yaybo nunca graba la voz de tu hijo o hija y nunca usa la cámara, las fotos ni la ubicación.</li>
    <li>Si te suscribes, un servicio de analítica de compras ve la compra y los datos técnicos de tu dispositivo. Nunca nada sobre tu hijo o hija.</li>
    <li>Puedes ver y borrar todo lo que guarda Yaybo en la Zona de padres, tras la puerta para adultos.</li>
  </ul>

  <h2>Quiénes somos</h2>
  <p>Yaybo la publica en la App Store <strong>Izotz Cristobal Mota</strong>, con el nombre comercial Seize Apps, en el País Vasco (España). Somos el operador de Yaybo a efectos de la ley estadounidense de protección de la privacidad infantil en línea (COPPA) y los responsables de la información que describe esta página. Escríbenos sobre cualquier cosa de aquí a <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>. Por favor, no pongas en un correo el nombre ni los datos de tu hijo o hija.</p>

  <h2>Qué guarda Yaybo, y dónde</h2>
  <p>Yaybo guarda esto en tu dispositivo y en tu base de datos privada de iCloud (alojada por Apple; Seize no tiene acceso) para que un segundo iPhone o iPad con la misma cuenta de Apple muestre la misma familia:</p>
  <ul>
    <li>el nombre de pila de tu hijo o hija (o el apodo que elijas), su curso, su tramo de edad y su estado de EE. UU.;</li>
    <li>las respuestas que diste al configurar la app, incluido lo que quisieras contar sobre cómo aprende;</li>
    <li>su progreso, sus premios, su isla y su racha;</li>
    <li>las notas de voz que grabas para tu hijo o hija (tu propia grabación, de cinco segundos como máximo).</li>
  </ul>
  <p>Como esto se queda en tus dispositivos y en tu iCloud, Seize no lo recoge. La sincronización con iCloud viene activada y puedes desactivarla en la Zona de padres; desactivada, los datos se quedan solo en el dispositivo. Yaybo no pide apellidos, fecha de nacimiento, fotos, correo electrónico ni ninguna cuenta.</p>

  <h2>Qué no recoge nunca Yaybo</h2>
  <p>Apellidos; fecha de nacimiento; fotos o cámara; <strong>audio de tu hijo o hija</strong> (Yaybo no usa el micrófono con niños); ubicación (Yaybo usa el estado que eliges, nunca la ubicación del dispositivo); correo electrónico o cuenta alguna; texto libre sobre tu hijo o hija; el identificador publicitario (IDFA); avisos de App Tracking Transparency. Yaybo no te sigue ni a ti ni a tu hijo o hija por las apps y webs de otras empresas, y no tiene chat, funciones sociales ni formas de compartir por las que alguien pudiera llegar hasta él o ella.</p>

  <h2>Micrófono, notificaciones y la categoría de edad de Apple</h2>
  <ul>
    <li><strong>Micrófono.</strong> Solo lo usa Yaybo cuando una persona adulta pulsa Grabar para dejar una nota de voz al niño o niña, en la Zona de padres y tras la puerta para adultos. Yaybo pide el permiso en ese momento y no antes. La grabación se queda en tus dispositivos y en tu iCloud.</li>
    <li><strong>Notificaciones.</strong> Los recordatorios van a la persona adulta, no al niño, y se programan en tu dispositivo. No tenemos servidor de notificaciones push. Yaybo pide el permiso justo después de una compra, y puedes decir que no.</li>
    <li><strong>La categoría de edad de Apple.</strong> Donde una ley estatal pide a las tiendas y a las apps gestionar la edad (hoy Texas, Utah y Luisiana), Apple puede decirle a Yaybo a qué categoría de edad pertenece tu cuenta de Apple. Yaybo lo usa solo para cumplir la ley: en la cuenta de un menor, la pantalla de suscripción explica que un padre o madre aprueba la compra a través de Apple. Yaybo guarda la respuesta solo en memoria, no la almacena, no la envía a nadie y no la usa para cambiar lo que ve un niño.</li>
  </ul>

  <h2>Analítica de compras (RevenueCat)</h2>
  <p>Para saber cuántas familias se suscriben, Yaybo usa RevenueCat, un servicio estadounidense de analítica de compras (RevenueCat, Inc.). Solo se activa después de que una persona adulta pase la puerta parental para comprar o restaurar una suscripción (o abra la pantalla de suscripción o la Zona de padres tras esa puerta), nunca en el dispositivo propio de un niño y nunca mientras un niño juega. Cuando está activo, RevenueCat recibe un identificador anónimo de usuario de la app, la dirección IP del dispositivo, información del dispositivo y del sistema, el identificador de proveedor del dispositivo (IDFV), el país de la tienda de App Store, un indicador del estado de App Tracking Transparency y la propia compra. Nunca recibe el nombre, la edad, las respuestas ni el progreso de tu hijo o hija. Una vez activado, sigue activo hasta que cierras la app. No usamos estos datos para publicidad, no te seguimos por las apps de otras empresas y RevenueCat actúa solo como nuestro proveedor de servicios.</p>
  <p>El identificador de proveedor es un número que Apple da a las apps de un mismo desarrollador en un dispositivo; no es el identificador publicitario. El indicador de App Tracking Transparency es el estado del permiso de seguimiento del dispositivo: Yaybo nunca pide seguir, así que figura como «no determinado» salvo que tú o Tiempo de uso hayáis desactivado el seguimiento. Yaybo no define ningún atributo propio en RevenueCat. RevenueCat guarda estos datos en Estados Unidos.</p>
  <p>Apple procesa el pago. Nunca vemos tu tarjeta ni los datos de tu cuenta de Apple. Es Apple, no Yaybo ni RevenueCat, quien decide si una suscripción está activa.</p>

  <h2>Privacidad de los menores (COPPA)</h2>
  <p>Yaybo está dirigida a menores de 13 años y está hecha para no recoger información personal de ellos.</p>
  <ul>
    <li><strong>Operador:</strong> Izotz Cristobal Mota, con el nombre comercial Seize Apps, País Vasco (España), <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</li>
    <li><strong>Qué recogemos de un menor:</strong> nada. Los datos de aprendizaje de arriba se quedan en los dispositivos y el iCloud de la familia. Lo único que llega a un proveedor de servicios son los datos de compra descritos en «Analítica de compras», y solo después de que una persona adulta pase la puerta parental.</li>
    <li><strong>Consentimiento:</strong> el paso de la analítica de compras ocurre solo después de que una persona adulta pase la puerta parental y compre o restaure una suscripción, o abra la pantalla de suscripción o la Zona de padres tras esa puerta; nunca en un dispositivo que un adulto haya indicado que es el propio del niño, y nunca cuando Apple le diga a Yaybo que la cuenta es de un menor.</li>
    <li><strong>Quién puede llegar hasta tu hijo o hija:</strong> nadie. Yaybo no tiene chat, ni funciones sociales, ni contenido de usuarios compartido con otros, ni anuncios, ni enlaces externos que un niño pueda abrir sin la puerta para adultos.</li>
    <li><strong>Tus derechos, como madre, padre o tutor:</strong> puedes ver en la Zona de padres todo lo que Yaybo guarda de un niño; puedes borrar a un niño («Borrar») o todo («Borrar todos los datos»); puedes rechazar la analítica de compras no comprando ni restaurando desde Yaybo y sin abrir la pantalla de suscripción ni la Zona de padres, y puedes escribirnos para pedir que se borre lo que RevenueCat tiene de tu dispositivo; y puedes preguntarnos lo que quieras en <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</li>
  </ul>

  <h2>Conservación y borrado de los datos</h2>
  <ul>
    <li><strong>En tus dispositivos y en tu iCloud:</strong> se conservan hasta que los borres. «Borrar» un niño, o «Borrar todos los datos», en la Zona de padres quita los datos del dispositivo y, mientras la sincronización con iCloud esté activada, del iCloud de la familia (el borrado se sincroniza con tus otros dispositivos). La Zona de padres indica si iCloud está sincronizando. Borrar solo la app deja la copia de iCloud; puedes quitarla en <strong>Ajustes › Cuenta de Apple › iCloud › Gestionar almacenamiento de la cuenta</strong>. Borrar tus datos no cancela una suscripción: eso se hace en <strong>Ajustes › Cuenta de Apple › Suscripciones</strong>.</li>
    <li><strong>En RevenueCat:</strong> conservamos los registros de compra solo mientras los necesitamos para demostrar que existió una suscripción (facturación, reembolsos, soporte), y no los usamos para nada más. RevenueCat no indica un plazo fijo de conservación de los datos de usuarios finales, y borrar Yaybo no borra lo que ya tiene: escribe a <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a> y le pediremos que borre el registro de tu dispositivo.</li>
    <li><strong>Nuestros servidores:</strong> Seize no tiene ninguno para Yaybo, así que no hay nada más que borrar.</li>
  </ul>

  <h2>Venta, cesión y seguimiento</h2>
  <p>No vendemos tu información personal ni la de tu hijo o hija, y no la cedemos para publicidad en las apps y webs de otras empresas. Yaybo no te sigue, así que no hay nada a lo que darse de baja.</p>

  <h2>Cómo la protegemos</h2>
  <p>Los datos de aprendizaje nunca salen de la infraestructura de Apple (tu dispositivo y tu iCloud). El acceso a App Store Connect y al panel de RevenueCat se limita a desarrolladores de Seize con nombre y verificación en dos pasos. Seize mantiene un programa escrito de seguridad de la información para Yaybo.</p>

  <h2>Cambios</h2>
  <p>Si cambiamos lo que recoge Yaybo, actualizaremos esta página y, si afecta a la información de tu hijo o hija, te pediremos el consentimiento otra vez dentro de la app antes de que el cambio surta efecto.</p>

  <h2>Contacto</h2>
  <p>Seize Apps · Izotz Cristobal Mota<br><a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a> · seizeapps.com</p>
''',
}

TERMS = {
'en': '''
  <p class="eyebrow">Yaybo · Legal</p>
  <h1>Yaybo terms of use</h1>
  <p class="effective">Effective October 11, 2026</p>
  <p>These terms are for the grown-up who sets up and pays for Yaybo. They sit on top of Apple's standard <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Licensed Application End User License Agreement</a>, which applies to anything these terms don't cover. How Yaybo treats your family's data is in the <a href="../privacy/">Yaybo privacy policy</a>.</p>

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
    <li><strong>Managing and cancelling.</strong> Manage or cancel in <strong>Settings › Apple Account › Subscriptions</strong> on your device. Cancelling stops the next renewal; you keep access until the end of the period you have paid for. Deleting the app does not cancel the subscription.</li>
    <li><strong>Refunds.</strong> Apple handles payments and refunds, under the App Store's refund policy (reportaproblem.apple.com). We cannot issue refunds directly.</li>
    <li><strong>If the plan ends.</strong> Your child's island, stars and progress are kept and stay viewable; the learning activities close until a grown-up renews. Nothing your child made is deleted because a plan ended.</li>
    <li><strong>Restore.</strong> "Restore" on the plan screen brings back a subscription you already own, on a new device or after reinstalling.</li>
    <li><strong>Purchases by minors.</strong> Where Apple's family or age settings require a parent's approval for a purchase, the purchase waits for that approval and completes by itself when it is given.</li>
  </ul>

  <h2>4. The grown-up gate, and supervising your child</h2>
  <p>Everything that costs money, leaves the app or changes your family's data sits behind a grown-up gate: a short challenge a young child is not meant to pass. The gate helps, but you are responsible for supervising how your child uses their device, including Screen Time, Ask to Buy and what else is installed on it.</p>

  <h2>5. Your family's information stays yours</h2>
  <p>What you enter in Yaybo, and what your child makes in it, is yours. As the <a href="../privacy/">privacy policy</a> describes, it is stored on your devices and in your own iCloud, and we have no access to it, which also means you are responsible for keeping your own backups. You can delete a child, or everything, in the Parent Zone.</p>

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
  <p>Estas condiciones son para la persona adulta que configura y paga Yaybo. Se suman al <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Contrato de licencia de usuario final de la aplicación con licencia</a> estándar de Apple, que se aplica a todo lo que estas condiciones no cubran. Cómo trata Yaybo los datos de tu familia está en la <a href="../privacidad/">política de privacidad de Yaybo</a>.</p>

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
    <li><strong>Gestionar y cancelar.</strong> Gestiónala o cancélala en <strong>Ajustes › Cuenta de Apple › Suscripciones</strong> de tu dispositivo. Cancelar detiene la siguiente renovación; conservas el acceso hasta el final del periodo ya pagado. Borrar la app no cancela la suscripción.</li>
    <li><strong>Reembolsos.</strong> Apple gestiona los pagos y los reembolsos, según su política de reembolsos de la App Store (reportaproblem.apple.com). Nosotros no podemos reembolsar directamente.</li>
    <li><strong>Si el plan termina.</strong> La isla, las estrellas y el progreso de tu hijo o hija se conservan y se pueden ver; las actividades de aprendizaje se cierran hasta que una persona adulta renueve. Nada de lo que haya hecho tu hijo o hija se borra porque termine un plan.</li>
    <li><strong>Restaurar.</strong> «Restaurar» en la pantalla del plan recupera una suscripción que ya tienes, en un dispositivo nuevo o tras reinstalar.</li>
    <li><strong>Compras de menores.</strong> Cuando los ajustes de familia o de edad de Apple exigen la aprobación de un padre o madre para una compra, la compra espera esa aprobación y se completa sola cuando se da.</li>
  </ul>

  <h2>4. La puerta para adultos y la supervisión de tu hijo o hija</h2>
  <p>Todo lo que cuesta dinero, sale de la app o cambia los datos de tu familia está tras una puerta para adultos: un reto corto que un niño pequeño no debería superar. La puerta ayuda, pero la supervisión de cómo usa tu hijo o hija su dispositivo es tuya, incluido Tiempo de uso, Pedir permiso para comprar y qué más hay instalado.</p>

  <h2>5. La información de tu familia sigue siendo tuya</h2>
  <p>Lo que introduces en Yaybo, y lo que tu hijo o hija crea en ella, es tuyo. Como describe la <a href="../privacidad/">política de privacidad</a>, se guarda en tus dispositivos y en tu propio iCloud, y nosotros no tenemos acceso, lo que también significa que las copias de seguridad son cosa tuya. Puedes borrar a un niño, o todo, en la Zona de padres.</p>

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
     'Yaybo privacy and children’s privacy (COPPA): what you tell Yaybo about your child stays on your devices and in your iCloud; no ads, no tracking, no child audio.'),
    ('es', 'privacy', 'privacidad', 'Política de privacidad de Yaybo — Seize Apps',
     'Privacidad de Yaybo y privacidad infantil (COPPA): lo que cuentas sobre tu hijo o hija se queda en tus dispositivos y en tu iCloud; sin anuncios, sin seguimiento, sin audio de niños.'),
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
                    + legal_main(lang, texts[lang]) + footer(lang, root))
            write(f'yaybo/{slug}/index.html', html)
