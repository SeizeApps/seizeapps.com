"""Atino: config for tools/gen_legal_apps.py. English and Spanish privacy text (the policy that was
gen_legal_atino.py, reconciled on 22/10/2026 with the code at SeizeRepo 5ee88ea7e: Atino 0.1.1 (7)).
Reconciled points: RevenueCat starts only after consent is stored (commit 7163e3824); the Keychain identity
survives deleting the app; personal files are not excluded from device backups; the job catalogue downloads at
every launch, before and without consent, and the countries you chose pick which files; withdrawing consent
does not remove Keychain items or what RevenueCat, the relay or the AI services already hold.
CONFIRM(U7) comments are lawyer to-dos and stay in the generated HTML."""
from .common import terms

# Amber from AtinoTheme (#FFB547, dark-only app). 1.8:1 on white, so light-mode text uses a darker amber of the
# same hue (found by the generator); the mark itself stays the declared accent on borders.
APP = dict(
    slug='atino', name='Atino', icon='atino.png',
    appStoreUrl='https://apps.apple.com/app/id6818553139',
    email='hello@seizeapps.com', publisher='Izotz Cristobal Mota, trading as Seize Apps',
    publisher_es='Izotz Cristobal Mota, con el nombre comercial de Seize Apps',
    updated_en='22 October 2026', updated_es='22 de octubre de 2026',
    dir_copies=('privacy', 'privacidad'), renderer='atino_layout',
    theme=dict(
        light=dict(mark='#FFB547', bg='#FFFDF8', fg='#1B2426', muted='#56625F', line='#E8E2D4', soft='#FFF4DE'),
        dark=dict(mark='#FFB547', bg='#0B1416', fg='#EAF0EE', muted='#A2B0AD', line='#22343A', soft='#1E2417'),
    ),
    pages={},
)

PRIVACY_EN = r'''
  <!--at-depth:@privacy@-->
  <h1>Atino privacy policy</h1>
  <p class="updated">Effective date: @updated@</p>

  <h2>1. Who we are</h2>
  <p>Atino is made by Izotz Cristobal Mota, trading as Seize Apps, in Spain. We are the controller of the personal data described in this policy. You can write to us about anything here at @mail@.</p>
  <!-- CONFIRM(U7): no postal address and no data protection officer are named because neither is confirmed anywhere in this repo. -->

  <h2>2. The short version</h2>
  <ul>
    <li>Your CV stays on your iPhone. Atino never uploads the PDF, and the original text is never stored.</li>
    <li>Before any text leaves the iPhone, Atino removes your name and contact details — email, phone, home address, date of birth, ID numbers and more — on the phone itself.</li>
    <li>Only after you allow it, the redacted CV text is sent to rank jobs, and to explain your profile and a job's fit when you open them: through the Seize relay to Command Code and TypeSafe AI (Jev). You can see and edit the exact text before anything is sent.</li>
    <li>There is no account, no advertising and no tracking.</li>
    <li>Only after you have given your consent, Atino starts RevenueCat, a purchase-analytics service, which learns about your subscription: an anonymous ID, your iPhone's vendor ID and your App Store purchases. RevenueCat never receives your CV, and Apple still takes the payment.</li>
    <li>Separately, and without waiting for your consent, your iPhone downloads the public job catalogue each time Atino starts. That host sees an ordinary download request, including which country files your iPhone asks for, but never your CV.</li>
    <li>The relay keeps no copy of the text. It keeps a small record per install — a random install ID, an App Attest key and the day's search counters — and, for a subscriber, the number Apple gives the subscription together with the IDs of the installs that used it, so the free limit works, one subscription is not shared without limit and abuse is stopped. Both are deleted after 60 days without activity.</li>
  </ul>

  <h2>3. What Atino handles, and why</h2>

  <h3>The CV text sent for ranking and explanations — your consent (Art. 6(1)(a) and Art. 9(2)(a) GDPR)</h3>
  <p>To rank jobs against your CV, Atino sends the redacted text of your CV, and the texts of the job adverts it is compared with, to the ranking service. The same text is sent when you open your profile (to read the occupations and skills in your CV) and when you open a job's fit breakdown (to explain how that job fits); nothing else is sent for them. A CV can reveal special-category data (for example, about health or trade-union membership), so we also rely on your explicit consent (Art. 9(2)(a)). You give it in the consent sheet before the first search. The app shows you the exact text in Settings › Your CV › “What leaves this iPhone”, and you can edit it; nothing is sent until you allow it. With daily alerts on, the same text is sent once a day to rank new jobs. You can withdraw at any time (section 7).</p>

  <h3>The purchase — performance of a contract (Art. 6(1)(b))</h3>
  <p>Apple processes the payment and manages the subscription. Atino never sees your payment details: it only receives the signed confirmation Apple issues that your subscription is active, and passes it to the relay once per request so the relay can tell free from Pro. The relay checks it against Apple's keys and does not keep the confirmation itself. It keeps only the number Apple gives the subscription (the original transaction ID), with the IDs of the installs it has let use it — no more than five phones — and when each was last seen, so that one subscription cannot be shared without limit. We need this to provide what you paid for.</p>

  <h3>The install ID and App Attest key — our legitimate interest (Art. 6(1)(f))</h3>
  <p>The phone creates a random install ID (16 random bytes, kept in the iPhone's Keychain) and an App Attest key, so that requests cannot be replayed and one install cannot use more than its share: the free search of the day, fair use for Pro, and the shared budget that keeps the ranking service affordable. This is our legitimate interest in keeping Atino working for everyone; it is not used to track you.</p>

  <h3>Purchase analytics (RevenueCat) — our legitimate interest (Art. 6(1)(f))</h3>
  <p>Atino includes RevenueCat's software library, used for analytics only: Apple's StoreKit still handles every purchase. Atino starts the library only once a consent for the current text of this policy is stored on your iPhone; before that, and if you never consent, it does not run. Once started, the library gives your install a random anonymous ID and sends RevenueCat, Inc. (United States) that ID, your iPhone's vendor identifier (a number Apple gives the apps of one developer on a device; it is not the advertising identifier) and your App Store purchases and subscription status (product, price, dates and Apple's transaction data). Atino also asks it once per install to read your existing purchase history from Apple and labels the install as a TestFlight or App Store build; it sends no other events. The library adds the technical details such a library sends with its requests (for example the app and iOS version, device model, language and App Store country), and, like any server, RevenueCat sees the internet address of each request. Once started it cannot be stopped within the same run: if you withdraw your consent, it stops at the next launch. We use it to count subscribers, trials and renewals and to check that purchases are recorded correctly. Atino never gives RevenueCat your name, email or CV, and we do not enable its advertising integrations: it is not used to track you.</p>

  <h3>The job catalogue download — no personal data</h3>
  <p>Each time Atino starts or returns to the foreground, your phone downloads the public job catalogue (a signed manifest and the job files) from the catalogue storage service described below. This does not wait for your consent, because the catalogue is public job data, not personal data. The service sees a download request and your iPhone's internet address, as any download does, and it sees which country files are requested, which follow the countries you chose in Atino (or, by default, the region of your iPhone). It never receives your CV.</p>

  <h3>These pages — an ordinary web request</h3>
  <p>These policy pages are hosted on seizeapps.com, which is served by GitHub Pages (GitHub Inc.). Viewing one is an ordinary web request: the host sees your internet address and the page you asked for, as any website does.</p>

  <h2>4. Who receives it</h2>
  <ul>
    <li><strong>Supabase (Supabase Inc., a United States company).</strong> Runs the Seize relay — a Supabase Edge Function with a Postgres database — and hosts the job catalogue on Supabase Storage, in the same project, in its European Union region (Frankfurt, Germany). The relay passes the text on and keeps no copy of it. The install and subscription records it does keep are stored in that database in Frankfurt. Like any host, Supabase's platform receives the internet address of each request, to the relay as to the catalogue, and may keep it in its own platform logs; the relay's own code neither reads nor stores it. Supabase acts on our instructions.</li>
    <!-- CONFIRM(U7): whether, and for how long, Supabase's platform logs keep the request's internet address is not stated anywhere in this repo. -->
    <li><strong>Command Code (United States).</strong> Receives the redacted text from the relay and passes it to Jev. It may keep the text under its own terms.</li>
    <li><strong>TypeSafe AI (United States).</strong> Runs Jev, the model that scores each job against your CV. It may keep the text under its own terms.</li>
    <li><strong>Apple.</strong> Handles the purchase and the App Store. Atino receives only the signed confirmation described above. The purchase and your Apple Account are governed by Apple's own terms.</li>
    <li><strong>RevenueCat (RevenueCat, Inc., United States).</strong> Our processor for the purchase analytics described in section 3, which it receives only after you have given consent. It acts on our instructions and publishes its own privacy policy at <a href="https://www.revenuecat.com/privacy" rel="noopener">revenuecat.com/privacy</a>. It never receives your CV text.</li>
    <!-- CONFIRM(U7): where RevenueCat stores the data, its transfer mechanism (it says it makes the EU standard contractual clauses available, revenuecat.com/dpa, read 6 October 2026), a UK mechanism, a fixed retention period for end-user data and our acceptance of the addendum are not visible in this repo. -->
    <li><strong>GitHub (GitHub Inc., United States).</strong> Serves these policy pages, as described in section 3. It receives no CV text and nothing from the app.</li>
  </ul>
  <p>Transfers outside the EEA. Command Code and TypeSafe AI are in the United States, so the text is transferred outside the European Economic Area. The redacted CV text is sent to Command Code and TypeSafe AI in the United States. The transfer safeguard will be named here once it is confirmed with those providers. Supabase keeps the relay's data in Frankfurt, but the company is American. RevenueCat is in the United States too, so its data is transferred as well; its own policy and data processing addendum describe how.</p>
  <!-- CONFIRM(U7): the processor agreements and the exact transfer safeguard (the Commission's standard contractual clauses and, where certified, the EU-US Data Privacy Framework) are not visible in this repo; confirm them with Supabase, Command Code and TypeSafe AI before publishing. No safeguard is claimed here for Supabase or GitHub. -->

  <h2>5. How long</h2>
  <ul>
    <li><strong>On your iPhone.</strong> Your CV (the redacted text, never the PDF) and everything Atino makes from it stay until you delete the CV in the app or delete the app; withdrawing consent deletes them at once. These files are not excluded from device backups, so they can be part of an iCloud or computer backup of your iPhone if you have backups turned on; those backups are between you and Apple. Alert digests are kept for 2 days. Your consent, your filters and your saved searches also live on the phone.</li>
    <li><strong>In the iPhone's Keychain.</strong> The random install ID, the App Attest key's ID, the last quota snapshot from the relay and the day's counters are kept in the Keychain, which is not backed up or synced. By design, neither withdrawing consent nor deleting Atino clears them, so that reinstalling does not reset the free limit; they hold no CV text, name or contact details.</li>
    <li><strong>At the relay.</strong> One record per install, keyed by the random install ID: that ID, your App Attest key (its ID, public key and counter), the day's counters, your phone's time-zone name, and the short-lived tickets of the requests in flight. A ticket lasts 5 minutes. The record is deleted after 60 days without activity. The relay also keeps daily totals of what the ranking service costs it (no install ID, no text, no searches) for 90 days, to hold the shared budget.</li>
    <li><strong>At the relay, for a subscription.</strong> One record per subscription, keyed by the number Apple gives it (the original transaction ID): the IDs of the installs that used it and when each was last seen. No payment details and no copy of Apple's confirmation. The record is deleted after 60 days without activity.</li>
    <li><strong>RevenueCat.</strong> How long it keeps the data in section 3 is set out in its own privacy policy and its agreement with us; we cannot see inside its systems and do not promise a retention period for it. Deleting Atino or withdrawing consent does not delete what RevenueCat already holds: write to us and we will ask it to delete the record.</li>
    <!-- CONFIRM(U7): RevenueCat states no fixed retention period for end-user data (privacy policy, June 2026; DPA, August 2026: customer data may be deleted from live systems 30 days after termination). -->
    <li><strong>Command Code and TypeSafe AI.</strong> The text may be kept under their own terms; we cannot delete those copies for you.</li>
    <!-- CONFIRM(U7): how long Command Code and TypeSafe AI keep the text is not in this repo; confirm before publishing. -->
    <li><strong>Apple.</strong> The purchase is Apple's record, under Apple's terms.</li>
  </ul>

  <h2>6. Permissions, notifications and background activity</h2>
  <p>Atino asks for no permission to read your photos, contacts, location, camera or microphone: you pick your CV with the system file picker, which gives Atino only that PDF. If you turn on the daily alert (Pro), Atino asks to send notifications, and only then. Alerts are local notifications created on your iPhone, not push notifications; the text can show the title and company of the best new job on your lock screen. To prepare the alert, iOS may wake Atino in the background (Background App Refresh) to update the job catalogue, rank, and post the notification, which sends the same redacted text once a day as described in section 3. Turning the alert off or withdrawing consent cancels that background refresh.</p>

  <h2>7. Your rights</h2>
  <p>You have the rights of access, rectification, erasure, restriction, objection and portability. You can withdraw your consent at any time: open Settings › Privacy › “Withdraw consent and delete my data”. That deletes your CV and everything made from it from the iPhone at once, cancels the daily alert and removes its notifications. It does not remove the Keychain items described in section 5, and it cannot delete what the relay, RevenueCat, Command Code or TypeSafe AI already hold (sections 4 and 5): write to us for that. To see or edit the text that would be sent: Settings › Your CV › “What leaves this iPhone”.</p>
  <p>Because Seize keeps no copy of your CV anywhere else, most requests are answered by deleting it in the app. For anything else, or to exercise any right, write to @mail@. You can also complain to your data protection authority: in Spain, the Agencia Española de Protección de Datos (<a href="https://www.aepd.es" rel="noopener">aepd.es</a>), or the authority where you live.</p>

  <h2>8. Children</h2>
  <p>Atino is not meant for people under 16. We do not knowingly handle their data; if you believe a child has used the app, write to us and we will delete it.</p>

  <h2>9. Changes</h2>
  <p>We may update this policy; the date at the top changes. Atino versions its consent: if a change is material — who receives the text, or what they may keep — it comes with a new privacy version, and the app asks for your consent again before the next search. The policy in force is always the one at this address.</p>
'''

PRIVACY_ES = r'''
  <!--at-depth:@privacidad@-->
  <h1>Política de privacidad de Atino</h1>
  <p class="updated">Fecha de entrada en vigor: @updated@</p>

  <h2>1. Quiénes somos</h2>
  <p>Atino lo desarrolla Izotz Cristobal Mota, con el nombre comercial de Seize Apps, en España. Somos el responsable de los datos personales que se describen en esta política. Para cualquier cosa relacionada con ella, escríbenos a @mail@.</p>
  <!-- CONFIRM(U7): no se nombra ninguna dirección postal ni ningún delegado de protección de datos porque no consta ninguno en este repositorio. -->

  <h2>2. La versión corta</h2>
  <ul>
    <li>Tu CV se queda en tu iPhone. Atino nunca sube el PDF y el texto original no se guarda nunca.</li>
    <li>Antes de que salga ningún texto del iPhone, Atino quita tu nombre y tus datos de contacto —correo, teléfono, dirección, fecha de nacimiento, números de documento y más— en el propio teléfono.</li>
    <li>Solo después de que lo permitas, el texto redactado de tu CV se envía para ordenar ofertas, y para explicarte tu perfil y el encaje de una oferta cuando los abres: pasa por la pasarela de Seize hasta Command Code y TypeSafe AI (Jev). Puedes ver y editar el texto exacto antes de que se envíe nada.</li>
    <li>No hay cuenta, ni publicidad, ni seguimiento.</li>
    <li>Solo después de que des tu permiso, Atino pone en marcha RevenueCat, un servicio de analítica de compras, que se entera de tu suscripción: un identificador anónimo, el identificador de proveedor de tu iPhone y tus compras en el App Store. RevenueCat nunca recibe tu CV y es Apple quien sigue cobrando.</li>
    <li>Aparte, y sin esperar a tu permiso, tu iPhone descarga el catálogo público de ofertas cada vez que se inicia Atino. Ese servidor ve una petición de descarga corriente, incluidos los archivos de país que pide tu iPhone, pero nunca tu CV.</li>
    <li>La pasarela no guarda ninguna copia del texto. Guarda un registro pequeño por instalación —un identificador aleatorio, una clave de App Attest y los contadores de búsquedas del día— y, si eres suscriptor, el número que Apple da a la suscripción junto con los identificadores de las instalaciones que la han usado, para que funcione el límite gratuito, una suscripción no se comparta sin límite y se frene el abuso. Ambos se borran a los 60 días sin actividad.</li>
  </ul>

  <h2>3. Qué trata Atino, y por qué</h2>

  <h3>El texto del CV que se envía para ordenar ofertas y explicarlas — tu permiso (art. 6.1.a y art. 9.2.a del RGPD)</h3>
  <p>Para ordenar las ofertas frente a tu CV, Atino envía el texto redactado de tu CV, y los textos de las ofertas con los que se compara, al servicio de ordenación. El mismo texto se envía cuando abres tu perfil (para leer las ocupaciones y habilidades de tu CV) y cuando abres el desglose del encaje de una oferta (para explicar cómo encaja); no se envía nada más para ellos. Un CV puede revelar datos de categorías especiales (por ejemplo, de salud o de afiliación sindical), así que nos apoyamos también en tu consentimiento explícito (art. 9.2.a). Lo das en la hoja de permiso antes de la primera búsqueda. La app te enseña el texto exacto en Ajustes › Tu CV › «Lo que sale de este iPhone», y puedes editarlo; no se envía nada hasta que lo permitas. Con los avisos diarios activados, este mismo texto se envía una vez al día para ordenar las ofertas nuevas. Puedes retirar el permiso cuando quieras (sección 7).</p>

  <h3>La compra — ejecución de un contrato (art. 6.1.b)</h3>
  <p>Apple procesa el pago y gestiona la suscripción. Atino nunca ve tus datos de pago: solo recibe el comprobante firmado que emite Apple de que tu suscripción está activa, y se lo pasa a la pasarela una vez por petición para que distinga entre gratis y Pro. La pasarela lo comprueba con las claves de Apple y no guarda el comprobante en sí. Solo guarda el número que Apple da a la suscripción (el identificador de la transacción original), con los identificadores de las instalaciones a las que ha dejado usarla —no más de cinco teléfonos— y cuándo se vio cada una por última vez, para que una suscripción no se pueda compartir sin límite. Lo necesitamos para darte lo que has pagado.</p>

  <h3>El identificador de instalación y la clave de App Attest — nuestro interés legítimo (art. 6.1.f)</h3>
  <p>El teléfono crea un identificador de instalación aleatorio (16 bytes aleatorios, guardados en el llavero del iPhone) y una clave de App Attest, para que las peticiones no se puedan repetir y una instalación no use más de lo que le toca: la búsqueda gratuita del día, el uso razonable de Pro y el presupuesto compartido que mantiene asequible el servicio de ordenación. Es nuestro interés legítimo en que Atino siga funcionando para todos; no se usa para seguirte.</p>

  <h3>Analítica de compras (RevenueCat) — nuestro interés legítimo (art. 6.1.f)</h3>
  <p>Atino incluye la biblioteca de software de RevenueCat, que se usa solo para analítica: el StoreKit de Apple sigue gestionando cada compra. Atino solo pone en marcha la biblioteca cuando hay guardado en tu iPhone un permiso para el texto vigente de esta política; antes de eso, y si nunca lo das, no se ejecuta. Una vez en marcha, la biblioteca da a tu instalación un identificador anónimo aleatorio y envía a RevenueCat, Inc. (Estados Unidos) ese identificador, el identificador de proveedor de tu iPhone (un número que Apple asigna a las apps de un mismo desarrollador en un dispositivo; no es el identificador de publicidad) y tus compras en el App Store y el estado de la suscripción (producto, precio, fechas y datos de transacción de Apple). Atino le pide además, una vez por instalación, que lea tu historial de compras en Apple, y marca la instalación como versión de TestFlight o del App Store; no envía ningún otro evento. La biblioteca añade los detalles técnicos que una biblioteca así envía con sus peticiones (por ejemplo la versión de la app y de iOS, el modelo del dispositivo, el idioma y el país del App Store) y, como cualquier servidor, RevenueCat ve la dirección de internet de cada petición. Una vez en marcha no se puede detener durante esa misma ejecución: si retiras tu permiso, se detiene en el siguiente inicio. Lo usamos para contar suscriptores, pruebas y renovaciones y para comprobar que las compras se registran bien. Atino nunca da a RevenueCat tu nombre, tu correo ni tu CV, y no activamos sus integraciones de publicidad: no se usa para seguirte.</p>

  <h3>La descarga del catálogo de ofertas — sin datos personales</h3>
  <p>Cada vez que se inicia Atino o vuelve a primer plano, tu teléfono se descarga el catálogo público de ofertas (un manifiesto firmado y los archivos de ofertas) desde el servicio de almacenamiento del catálogo que se describe más abajo. Esto no espera a tu permiso, porque el catálogo son ofertas públicas, no datos personales. El servicio ve una petición de descarga y la dirección de internet de tu iPhone, como en cualquier descarga, y ve qué archivos de país se piden, que siguen los países que elegiste en Atino (o, por defecto, la región de tu iPhone). Nunca recibe tu CV.</p>

  <h3>Estas páginas — una petición web corriente</h3>
  <p>Estas páginas de la política están alojadas en seizeapps.com, que sirve GitHub Pages (GitHub Inc.). Verlas es una petición web corriente: el servidor ve tu dirección de internet y la página que has pedido, como en cualquier sitio web.</p>

  <h2>4. Quién lo recibe</h2>
  <ul>
    <li><strong>Supabase (Supabase Inc., una empresa de Estados Unidos).</strong> Opera la pasarela de Seize —una Edge Function de Supabase con una base de datos Postgres— y aloja el catálogo de ofertas en Supabase Storage, en el mismo proyecto, en su región de la Unión Europea (Fráncfort, Alemania). La pasarela deja pasar el texto y no guarda ninguna copia. Los registros por instalación y por suscripción que sí guarda se almacenan en esa base de datos en Fráncfort. Como cualquier servidor, la plataforma de Supabase recibe la dirección de internet de cada petición, tanto a la pasarela como al catálogo, y puede conservarla en sus propios registros de plataforma; el código de la pasarela ni la lee ni la guarda. Supabase actúa siguiendo nuestras instrucciones.</li>
    <!-- CONFIRM(U7): no consta en este repositorio si los registros de la plataforma de Supabase conservan la dirección de internet de la petición, ni durante cuánto tiempo. -->
    <li><strong>Command Code (Estados Unidos).</strong> Recibe de la pasarela el texto redactado y se lo pasa a Jev. Puede conservar el texto según sus propias condiciones.</li>
    <li><strong>TypeSafe AI (Estados Unidos).</strong> Ejecuta Jev, el modelo que puntúa cada oferta frente a tu CV. Puede conservar el texto según sus propias condiciones.</li>
    <li><strong>Apple.</strong> Gestiona la compra y el App Store. Atino solo recibe el comprobante firmado que se describe arriba. La compra y tu cuenta de Apple se rigen por las condiciones de Apple.</li>
    <li><strong>RevenueCat (RevenueCat, Inc., Estados Unidos).</strong> Nuestro encargado del tratamiento para la analítica de compras que se describe en la sección 3, que solo recibe después de que des tu permiso. Actúa siguiendo nuestras instrucciones y publica su propia política de privacidad en <a href="https://www.revenuecat.com/privacy" rel="noopener">revenuecat.com/privacy</a>. Nunca recibe el texto de tu CV.</li>
    <!-- CONFIRM(U7): no constan en este repositorio dónde guarda los datos RevenueCat, su mecanismo de transferencia (dice poner a disposición las cláusulas contractuales tipo de la UE, revenuecat.com/dpa, leída el 6 de octubre de 2026), uno para el Reino Unido, un plazo de conservación fijo para los datos de usuarios finales ni que hayamos aceptado la adenda. -->
    <li><strong>GitHub (GitHub Inc., Estados Unidos).</strong> Sirve estas páginas de la política, como se describe en la sección 3. No recibe ningún texto del CV ni nada de la app.</li>
  </ul>
  <p>Transferencias fuera del EEE. Command Code y TypeSafe AI están en Estados Unidos, así que el texto sale del Espacio Económico Europeo. El texto redactado del CV se envía a Command Code y TypeSafe AI en Estados Unidos. La salvaguarda de la transferencia se nombrará aquí cuando se confirme con esos proveedores. Supabase guarda los datos de la pasarela en Fráncfort, pero la empresa es estadounidense. RevenueCat también está en Estados Unidos, así que sus datos también se transfieren; su propia política y su adenda de tratamiento de datos explican cómo.</p>
  <!-- CONFIRM(U7): los contratos de encargo y la salvaguarda exacta de la transferencia (las cláusulas contractuales tipo de la Comisión y, cuando corresponda, el Marco de Privacidad de Datos UE-EE. UU.) no constan en este repositorio; confírmalos con Supabase, Command Code y TypeSafe AI antes de publicar. Aquí no se afirma ninguna salvaguarda para Supabase ni para GitHub. -->

  <h2>5. Cuánto tiempo</h2>
  <ul>
    <li><strong>En tu iPhone.</strong> Tu CV (el texto redactado, nunca el PDF) y todo lo que Atino saca de él se quedan hasta que borres el CV en la app o borres la app; retirar el permiso los borra de inmediato. Estos archivos no están excluidos de las copias de seguridad del dispositivo, así que pueden formar parte de una copia de iCloud o de ordenador de tu iPhone si tienes las copias activadas; esas copias son cosa tuya y de Apple. Los resúmenes de los avisos se guardan 2 días. Tu permiso, tus filtros y tus búsquedas guardadas también viven en el teléfono.</li>
    <li><strong>En el llavero del iPhone.</strong> El identificador aleatorio de instalación, el id de la clave de App Attest, la última foto de la cuota que da la pasarela y los contadores del día se guardan en el llavero, que no entra en copias de seguridad ni se sincroniza. Por diseño, ni retirar el permiso ni borrar Atino los borra, para que reinstalar no reinicie el límite gratuito; no contienen texto del CV, nombre ni datos de contacto.</li>
    <li><strong>En la pasarela.</strong> Un registro por instalación, con el identificador aleatorio como clave: ese identificador, tu clave de App Attest (su id, su clave pública y su contador), los contadores del día, el nombre de la zona horaria de tu teléfono y los pases temporales de las peticiones en curso. Un pase dura 5 minutos. El registro se borra a los 60 días sin actividad. La pasarela guarda además totales diarios de lo que le cuesta el servicio de ordenación (sin identificador, sin texto y sin búsquedas) durante 90 días, para sostener el presupuesto compartido.</li>
    <li><strong>En la pasarela, por suscripción.</strong> Un registro por suscripción, con el número que Apple le da (el identificador de la transacción original) como clave: los identificadores de las instalaciones que la han usado y cuándo se vio cada una por última vez. Sin datos de pago y sin copia del comprobante de Apple. El registro se borra a los 60 días sin actividad.</li>
    <li><strong>RevenueCat.</strong> Cuánto tiempo conserva los datos de la sección 3 lo explican su propia política de privacidad y su contrato con nosotros; no podemos ver sus sistemas y no prometemos un plazo de conservación. Borrar Atino o retirar el permiso no borra lo que RevenueCat ya tiene: escríbenos y le pediremos que borre el registro.</li>
    <!-- CONFIRM(U7): RevenueCat no indica un plazo fijo de conservación de los datos de usuarios finales (política de privacidad de junio de 2026; adenda de agosto de 2026: los datos del cliente pueden borrarse de los sistemas en producción 30 días después de la terminación). -->
    <li><strong>Command Code y TypeSafe AI.</strong> El texto puede conservarse según sus propias condiciones; esas copias no podemos borrarlas nosotros.</li>
    <!-- CONFIRM(U7): cuánto tiempo conservan el texto Command Code y TypeSafe AI no consta en este repositorio; confírmalo antes de publicar. -->
    <li><strong>Apple.</strong> La compra es un registro de Apple, sujeto a sus condiciones.</li>
  </ul>

  <h2>6. Permisos, notificaciones y actividad en segundo plano</h2>
  <p>Atino no pide permiso para leer tus fotos, contactos, ubicación, cámara ni micrófono: eliges tu CV con el selector de archivos del sistema, que solo le da a Atino ese PDF. Si activas el aviso diario (Pro), Atino pide permiso para enviar notificaciones, y solo entonces. Los avisos son notificaciones locales creadas en tu iPhone, no notificaciones push; el texto puede mostrar en la pantalla de bloqueo el título y la empresa de la mejor oferta nueva. Para preparar el aviso, iOS puede despertar a Atino en segundo plano (actualización en segundo plano) para actualizar el catálogo, ordenar y publicar la notificación, lo que envía una vez al día el mismo texto redactado que se describe en la sección 3. Desactivar el aviso o retirar el permiso cancela esa actualización en segundo plano.</p>

  <h2>7. Tus derechos</h2>
  <p>Tienes derecho a acceder, rectificar, suprimir, limitar y oponerte al tratamiento, y a la portabilidad de tus datos. Puedes retirar tu permiso cuando quieras: abre Ajustes › Privacidad › «Retirar el permiso y borrar mis datos». Eso borra de una vez tu CV y todo lo que Atino ha sacado de él en el iPhone, cancela el aviso diario y retira sus notificaciones. No elimina los elementos del llavero que se describen en la sección 5, y no puede borrar lo que la pasarela, RevenueCat, Command Code o TypeSafe AI ya tienen (secciones 4 y 5): escríbenos para eso. Para ver o editar el texto que se enviaría: Ajustes › Tu CV › «Lo que sale de este iPhone».</p>
  <p>Como Seize no guarda ninguna copia de tu CV en ningún otro sitio, la mayoría de las solicitudes se resuelven borrándolo en la app. Para cualquier otra cosa, o para ejercer cualquier derecho, escribe a @mail@. También puedes reclamar ante tu autoridad de protección de datos: en España, la Agencia Española de Protección de Datos (<a href="https://www.aepd.es" rel="noopener">aepd.es</a>), o la autoridad del lugar donde vivas.</p>

  <h2>8. Menores</h2>
  <p>Atino no está pensado para menores de 16 años. No tratamos sus datos a sabiendas; si crees que un menor ha usado la app, escríbenos y lo borraremos.</p>

  <h2>9. Cambios</h2>
  <p>Podemos actualizar esta política; la fecha de arriba cambia. Atino versiona su permiso: si el cambio es importante —quién recibe el texto o qué puede conservar—, llega con una nueva versión de privacidad y la app te pide el permiso otra vez antes de la siguiente búsqueda. La política vigente es siempre la que está en esta dirección.</p>
'''


TERMS = terms('Atino: Jobs Ranked for You', 'Atino', 'Izotz Cristobal Mota, trading as Seize Apps', [
    ('Free use and Atino Pro',
     '<p>Atino is free to download. The free tier gives you one search per local day, the top 10 results and the location and workplace filters. Atino Pro is an optional auto-renewing subscription, weekly or monthly, that unlocks all results, every filter, more searches under a fair-use limit (currently 60 a day), saved searches, the daily alert and fit breakdowns. There is no free trial and no lifetime option, and Family Sharing is not enabled. The price is shown by the App Store before you confirm.</p>'
     '<p>Subscriptions are charged to your Apple Account at confirmation and renew automatically unless you cancel at least 24 hours before the end of the current period. Manage or cancel them in your Apple Account\'s subscription settings; Restore Purchases and Manage Subscription are in Atino\'s Pro sheet and Settings. One subscription can be used on a limited number of your devices at the same time. Purchases are processed by Apple, and refunds are handled by Apple under the App Store\'s policies: we can\'t issue refunds directly.</p>'),
    ('Your CV and your consent',
     '<p>Atino ranks jobs against a CV that you choose. Before the first search it asks for your consent to send the redacted text of your CV to the ranking services named in the <a href="@privacy@">Privacy Policy</a>; without it, searches don\'t run. Atino removes your name and contact details on your iPhone first, but redaction is automatic and can miss something, so read the text in Settings › Your CV › "What leaves this iPhone" and edit it before you allow it. You are responsible for the CV you load and for having the right to use it. You can withdraw your consent at any time in Settings › Privacy.</p>'),
    ('Jobs and match results',
     '<p>The jobs come from public company career pages and open data sources, and Apply opens the employer\'s own page. Atino is independent of the employers and of the job boards it draws from, and a job can change or disappear at any time. The match percentage and the explanations are automatic estimates, not a promise that a job fits, that you will be shortlisted or that you will be hired, and Atino doesn\'t apply for jobs on your behalf. Ranking needs an internet connection.</p>'),
    ('Fair use and limits',
     '<p>Searches and other requests are limited per install and per subscription so that the service stays affordable for everyone, and limits can be reached. Don\'t try to get around them, reverse-engineer Atino, resell it or misuse it, and don\'t use it in any way that breaks the law or Apple\'s terms.</p>'),
    ('Age',
     '<p>Atino is not meant for people under 16.</p>'),
])

SUPPORT = r'''
<h1>Support</h1>
<p class="updated">Atino: jobs ranked for you, with your CV staying on your iPhone.</p>

<h2>Contact</h2>
<p class="contact">@mail@</p>
<p>The Suggest a Feature and Report a Bug rows at the bottom of Settings open an email addressed to us; the bug report fills in your Atino version, iOS version and device model.</p>

<h2>Common questions</h2>

<h3>What leaves my iPhone?</h3>
<p>Only after you consent, the redacted text of your CV and the job texts it is compared with go through our relay to the ranking services. You can read and edit the exact text in Settings › Your CV › "What leaves this iPhone". The PDF itself never leaves. See the <a href="@privacy@">Privacy Policy</a>.</p>

<h3>How do I withdraw my consent and delete my data?</h3>
<p>Settings › Privacy › "Withdraw consent and delete my data". It deletes your CV and everything made from it from the iPhone, and cancels the daily alert. Write to us if you also want us to ask the relay, RevenueCat and the ranking services to delete what they hold.</p>

<h3>My CV is not read correctly.</h3>
<p>Atino reads PDF files. It uses the PDF's text and, if there is almost none (a scan), recognises the text on your iPhone in English, Spanish or Swedish. Use a PDF with selectable text where you can, and check the result in Settings › Your CV.</p>

<h3>What does the free version include?</h3>
<p>One search per local day, the top 10 results, and the location and workplace filters. Atino Pro, a weekly or monthly subscription, adds all results, every filter, more searches, saved searches, the daily alert and fit breakdowns.</p>

<h3>How do I restore, cancel or get a refund?</h3>
<p>Restore Purchases and Manage Subscription are in the Pro sheet and in Settings. You can also manage your subscriptions in the iPhone's Settings › Apple Account › Subscriptions. Request a refund at <a href="https://reportaproblem.apple.com" rel="noopener">reportaproblem.apple.com</a>.</p>

<h3>The daily alert doesn't arrive.</h3>
<p>The alert is a Pro feature. Check that notifications are allowed for Atino in the iPhone's Settings, that Background App Refresh is on; iOS decides when background work runs, so an alert can arrive late.</p>

<h3>I can't search any more today.</h3>
<p>The free version allows one search per local day, and Pro has a fair-use daily limit. The limit resets the next day.</p>
'''

APP['pages'] = {
    ('en', 'index'): dict(title='Atino: Jobs Ranked for You',
                          desc='Import your CV and Atino ranks current job ads across Europe by fit, with a short reason for each. Your name and contact details are removed on your iPhone first.', body=''),
    ('en', 'privacy'): dict(title='Atino privacy policy',
                            desc='Atino privacy: your CV stays on your iPhone, name and contact details are removed on the phone, and redacted text is sent only with your permission.', body=PRIVACY_EN),
    ('es', 'privacidad'): dict(title='Política de privacidad de Atino',
                               desc='Privacidad de Atino: tu CV se queda en tu iPhone, tu nombre y tus datos de contacto se quitan en el teléfono y el texto redactado solo se envía con tu permiso.', body=PRIVACY_ES),
    ('en', 'terms'): dict(title='Atino · Terms of Use', desc='Terms of use for Atino.', body=TERMS),
    ('en', 'support'): dict(title='Atino · Support', desc='Help and contact for Atino.', body=SUPPORT),
}
