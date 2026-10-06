"""Atino's own privacy pages (05/10/2026).

Atino sends a redacted CV to third-party ranking services through a Seize relay, so it can't live under
the studio-wide policy. The text is the one that used to sit next to the job catalogue
(services/atino-corpus/site/privacy*.html), ported here with the infrastructure as it is now: the relay
runs on Supabase (EU region, Frankfurt) and the catalogue is on Supabase Storage; these pages are on
GitHub Pages. Paths follow Garum's convention:
  /atino/privacy/      English
  /atino/privacidad/   castellano
The CONFIRM(U7) notes are lawyer to-dos and stay in the generated HTML as comments.
Built with gen_site's chrome; run `python3 tools/gen_site.py`, which calls build_atino().
"""
from gen_site import head, header, footer, write, legal_main

PRIVACY = {
'en': '''
  <p class="eyebrow">Atino · Legal</p>
  <h1>Atino privacy policy</h1>
  <p class="effective">Effective date: 6 October 2026</p>

  <h2>1. Who we are</h2>
  <p>Atino is made by Izotz Cristobal Mota, trading as Seize Apps, in Spain. We are the controller of the personal data described in this policy. You can write to us about anything here at <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</p>
  <!-- CONFIRM(U7): no postal address and no data protection officer are named because neither is confirmed anywhere in this repo. -->

  <h2>2. The short version</h2>
  <ul>
    <li>Your CV stays on your iPhone. Atino never uploads the PDF, and the original text is never stored.</li>
    <li>Before any text leaves the iPhone, Atino removes your name and contact details — email, phone, home address, date of birth, ID numbers and more — on the phone itself.</li>
    <li>Only after you allow it, the redacted CV text is sent to rank jobs, and to explain your profile and a job's fit when you open them: through the Seize relay to Command Code and TypeSafe AI (Jev). You can see and edit the exact text before anything is sent.</li>
    <li>There is no account, no advertising and no tracking.</li>
    <li>The relay keeps no copy of the text. It keeps a small record per install — a random install ID, an App Attest key and the day's search counters — and, for a subscriber, the number Apple gives the subscription together with the IDs of the installs that used it, so the free limit works, one subscription is not shared without limit and abuse is stopped. Both are deleted after 60 days without activity.</li>
  </ul>

  <h2>3. What Atino handles, and why</h2>

  <h3>The CV text sent for ranking and explanations — your consent (Art. 6(1)(a) and Art. 9(2)(a) GDPR)</h3>
  <p>To rank jobs against your CV, Atino sends the redacted text of your CV, and the texts of the job adverts it is compared with, to the ranking service. The same text is sent when you open your profile (to read the occupations and skills in your CV) and when you open a job's fit breakdown (to explain how that job fits); nothing else is sent for them. A CV can reveal special-category data (for example, about health or trade-union membership), so we also rely on your explicit consent (Art. 9(2)(a)). You give it in the consent sheet before the first search. The app shows you the exact text in Settings › Your CV › “What leaves this iPhone”, and you can edit it; nothing is sent until you allow it. With daily alerts on, the same text is sent once a day to rank new jobs. You can withdraw at any time (section 6).</p>

  <h3>The purchase — performance of a contract (Art. 6(1)(b))</h3>
  <p>Apple processes the payment and manages the subscription. Atino never sees your payment details: it only receives the signed confirmation Apple issues that your subscription is active, and passes it to the relay once per request so the relay can tell free from Pro. The relay checks it against Apple's keys and does not keep the confirmation itself. It keeps only the number Apple gives the subscription (the original transaction ID), with the IDs of the installs it has let use it — no more than five phones in a day — and when each was last seen, so that one subscription cannot be shared without limit. We need this to provide what you paid for.</p>

  <h3>The install ID and App Attest key — our legitimate interest (Art. 6(1)(f))</h3>
  <p>The phone creates a random install ID (16 random bytes, kept in the iPhone's Keychain) and an App Attest key, so that requests cannot be replayed and one install cannot use more than its share: the free search of the day, fair use for Pro, and the shared budget that keeps the ranking service affordable. This is our legitimate interest in keeping Atino working for everyone; it is not used to track you.</p>

  <h3>The job catalogue download — no personal data</h3>
  <p>Your phone downloads the public job catalogue (a signed manifest and the job files) from the catalogue storage service described below. That is public job data, not personal data. The service sees a download request and your iPhone's internet address, as any download does; it never receives your CV.</p>

  <h3>These pages — an ordinary web request</h3>
  <p>These policy pages are hosted on seizeapps.com, which is served by GitHub Pages (GitHub Inc.). Viewing one is an ordinary web request: the host sees your internet address and the page you asked for, as any website does.</p>

  <h2>4. Who receives it</h2>
  <ul>
    <li><strong>Supabase (Supabase Inc., a United States company).</strong> Runs the Seize relay — a Supabase Edge Function with a Postgres database — and hosts the job catalogue on Supabase Storage, in the same project, in its European Union region (Frankfurt, Germany). The relay passes the text on and keeps no copy of it. The install and subscription records it does keep are stored in that database in Frankfurt. Like any host, Supabase's platform receives the internet address of each request, to the relay as to the catalogue, and may keep it in its own platform logs; the relay's own code neither reads nor stores it. Supabase acts on our instructions.</li>
    <!-- CONFIRM(U7): whether, and for how long, Supabase's platform logs keep the request's internet address is not stated anywhere in this repo. -->
    <li><strong>Command Code (United States).</strong> Receives the redacted text from the relay and passes it to Jev. It may keep the text under its own terms.</li>
    <li><strong>TypeSafe AI (United States).</strong> Runs Jev, the model that scores each job against your CV. It may keep the text under its own terms.</li>
    <li><strong>Apple.</strong> Handles the purchase and the App Store. Atino receives only the signed confirmation described above. The purchase and your Apple Account are governed by Apple's own terms.</li>
    <li><strong>GitHub (GitHub Inc., United States).</strong> Serves these policy pages, as described in section 3. It receives no CV text and nothing from the app.</li>
  </ul>
  <p>Transfers outside the EEA. Command Code and TypeSafe AI are in the United States, so the text is transferred outside the European Economic Area. The redacted CV text is sent to Command Code and TypeSafe AI in the United States. The transfer safeguard will be named here once it is confirmed with those providers. Supabase keeps the relay's data in Frankfurt, but the company is American.</p>
  <!-- CONFIRM(U7): the processor agreements and the exact transfer safeguard (the Commission's standard contractual clauses and, where certified, the EU-US Data Privacy Framework) are not visible in this repo; confirm them with Supabase, Command Code and TypeSafe AI before publishing. No safeguard is claimed here for Supabase or GitHub. -->

  <h2>5. How long</h2>
  <ul>
    <li><strong>On your iPhone.</strong> Your CV (the redacted text, never the PDF) and everything Atino makes from it stay until you delete the CV in the app or delete the app; withdrawing consent deletes them at once. Alert digests are kept for 2 days. The daily counts and your consent also live on the phone.</li>
    <li><strong>At the relay.</strong> One record per install, keyed by the random install ID: that ID, your App Attest key (its ID, public key and counter), the day's counters, your phone's time-zone name, and the short-lived tickets of the requests in flight. A ticket lasts 5 minutes. The record is deleted after 60 days without activity. The relay also keeps daily totals of what the ranking service costs it (no install ID, no text, no searches) for 90 days, to hold the shared budget.</li>
    <li><strong>At the relay, for a subscription.</strong> One record per subscription, keyed by the number Apple gives it (the original transaction ID): the IDs of the installs that used it and when each was last seen. No payment details and no copy of Apple's confirmation. The record is deleted after 60 days without activity.</li>
    <li><strong>Command Code and TypeSafe AI.</strong> The text may be kept under their own terms; we cannot delete those copies for you.</li>
    <!-- CONFIRM(U7): how long Command Code and TypeSafe AI keep the text is not in this repo; confirm before publishing. -->
    <li><strong>Apple.</strong> The purchase is Apple's record, under Apple's terms.</li>
  </ul>

  <h2>6. Your rights</h2>
  <p>You have the rights of access, rectification, erasure, restriction, objection and portability. You can withdraw your consent at any time: open Settings › Privacy › “Withdraw consent and delete my data”. That deletes your CV and everything made from it from the iPhone at once. To see or edit the text that would be sent: Settings › Your CV › “What leaves this iPhone”.</p>
  <p>Because Seize keeps no copy of your CV anywhere else, most requests are answered by deleting it in the app. For anything else, or to exercise any right, write to <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>. You can also complain to your data protection authority: in Spain, the Agencia Española de Protección de Datos (<a href="https://www.aepd.es" rel="noopener">aepd.es</a>), or the authority where you live.</p>

  <h2>7. Children</h2>
  <p>Atino is not meant for people under 16. We do not knowingly handle their data; if you believe a child has used the app, write to us and we will delete it.</p>

  <h2>8. Changes</h2>
  <p>We may update this policy; the date at the top changes. Atino versions its consent: if a change is material — who receives the text, or what they may keep — it comes with a new privacy version, and the app asks for your consent again before the next search. The policy in force is always the one at this address.</p>
''',
'es': '''
  <p class="eyebrow">Atino · Legal</p>
  <h1>Política de privacidad de Atino</h1>
  <p class="effective">Fecha de entrada en vigor: 6 de octubre de 2026</p>

  <h2>1. Quiénes somos</h2>
  <p>Atino lo desarrolla Izotz Cristobal Mota, con el nombre comercial de Seize Apps, en España. Somos el responsable de los datos personales que se describen en esta política. Para cualquier cosa relacionada con ella, escríbenos a <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</p>
  <!-- CONFIRM(U7): no se nombra ninguna dirección postal ni ningún delegado de protección de datos porque no consta ninguno en este repositorio. -->

  <h2>2. La versión corta</h2>
  <ul>
    <li>Tu CV se queda en tu iPhone. Atino nunca sube el PDF y el texto original no se guarda nunca.</li>
    <li>Antes de que salga ningún texto del iPhone, Atino quita tu nombre y tus datos de contacto —correo, teléfono, dirección, fecha de nacimiento, números de documento y más— en el propio teléfono.</li>
    <li>Solo después de que lo permitas, el texto redactado de tu CV se envía para ordenar ofertas, y para explicarte tu perfil y el encaje de una oferta cuando los abres: pasa por la pasarela de Seize hasta Command Code y TypeSafe AI (Jev). Puedes ver y editar el texto exacto antes de que se envíe nada.</li>
    <li>No hay cuenta, ni publicidad, ni seguimiento.</li>
    <li>La pasarela no guarda ninguna copia del texto. Guarda un registro pequeño por instalación —un identificador aleatorio, una clave de App Attest y los contadores de búsquedas del día— y, si eres suscriptor, el número que Apple da a la suscripción junto con los identificadores de las instalaciones que la han usado, para que funcione el límite gratuito, una suscripción no se comparta sin límite y se frene el abuso. Ambos se borran a los 60 días sin actividad.</li>
  </ul>

  <h2>3. Qué trata Atino, y por qué</h2>

  <h3>El texto del CV que se envía para ordenar ofertas y explicarlas — tu permiso (art. 6.1.a y art. 9.2.a del RGPD)</h3>
  <p>Para ordenar las ofertas frente a tu CV, Atino envía el texto redactado de tu CV, y los textos de las ofertas con los que se compara, al servicio de ordenación. El mismo texto se envía cuando abres tu perfil (para leer las ocupaciones y habilidades de tu CV) y cuando abres el desglose del encaje de una oferta (para explicar cómo encaja); no se envía nada más para ellos. Un CV puede revelar datos de categorías especiales (por ejemplo, de salud o de afiliación sindical), así que nos apoyamos también en tu consentimiento explícito (art. 9.2.a). Lo das en la hoja de permiso antes de la primera búsqueda. La app te enseña el texto exacto en Ajustes › Tu CV › «Lo que sale de este iPhone», y puedes editarlo; no se envía nada hasta que lo permitas. Con los avisos diarios activados, este mismo texto se envía una vez al día para ordenar las ofertas nuevas. Puedes retirar el permiso cuando quieras (sección 6).</p>

  <h3>La compra — ejecución de un contrato (art. 6.1.b)</h3>
  <p>Apple procesa el pago y gestiona la suscripción. Atino nunca ve tus datos de pago: solo recibe el comprobante firmado que emite Apple de que tu suscripción está activa, y se lo pasa a la pasarela una vez por petición para que distinga entre gratis y Pro. La pasarela lo comprueba con las claves de Apple y no guarda el comprobante en sí. Solo guarda el número que Apple da a la suscripción (el identificador de la transacción original), con los identificadores de las instalaciones a las que ha dejado usarla —no más de cinco teléfonos en un día— y cuándo se vio cada una por última vez, para que una suscripción no se pueda compartir sin límite. Lo necesitamos para darte lo que has pagado.</p>

  <h3>El identificador de instalación y la clave de App Attest — nuestro interés legítimo (art. 6.1.f)</h3>
  <p>El teléfono crea un identificador de instalación aleatorio (16 bytes aleatorios, guardados en el llavero del iPhone) y una clave de App Attest, para que las peticiones no se puedan repetir y una instalación no use más de lo que le toca: la búsqueda gratuita del día, el uso razonable de Pro y el presupuesto compartido que mantiene asequible el servicio de ordenación. Es nuestro interés legítimo en que Atino siga funcionando para todos; no se usa para seguirte.</p>

  <h3>La descarga del catálogo de ofertas — sin datos personales</h3>
  <p>Tu teléfono se descarga el catálogo público de ofertas (un manifiesto firmado y los archivos de ofertas) desde el servicio de almacenamiento del catálogo que se describe más abajo. Son ofertas públicas, no datos personales. El servicio ve una petición de descarga y la dirección de internet de tu iPhone, como en cualquier descarga; nunca recibe tu CV.</p>

  <h3>Estas páginas — una petición web corriente</h3>
  <p>Estas páginas de la política están alojadas en seizeapps.com, que sirve GitHub Pages (GitHub Inc.). Verlas es una petición web corriente: el servidor ve tu dirección de internet y la página que has pedido, como en cualquier sitio web.</p>

  <h2>4. Quién lo recibe</h2>
  <ul>
    <li><strong>Supabase (Supabase Inc., una empresa de Estados Unidos).</strong> Opera la pasarela de Seize —una Edge Function de Supabase con una base de datos Postgres— y aloja el catálogo de ofertas en Supabase Storage, en el mismo proyecto, en su región de la Unión Europea (Fráncfort, Alemania). La pasarela deja pasar el texto y no guarda ninguna copia. Los registros por instalación y por suscripción que sí guarda se almacenan en esa base de datos en Fráncfort. Como cualquier servidor, la plataforma de Supabase recibe la dirección de internet de cada petición, tanto a la pasarela como al catálogo, y puede conservarla en sus propios registros de plataforma; el código de la pasarela ni la lee ni la guarda. Supabase actúa siguiendo nuestras instrucciones.</li>
    <!-- CONFIRM(U7): no consta en este repositorio si los registros de la plataforma de Supabase conservan la dirección de internet de la petición, ni durante cuánto tiempo. -->
    <li><strong>Command Code (Estados Unidos).</strong> Recibe de la pasarela el texto redactado y se lo pasa a Jev. Puede conservar el texto según sus propias condiciones.</li>
    <li><strong>TypeSafe AI (Estados Unidos).</strong> Ejecuta Jev, el modelo que puntúa cada oferta frente a tu CV. Puede conservar el texto según sus propias condiciones.</li>
    <li><strong>Apple.</strong> Gestiona la compra y el App Store. Atino solo recibe el comprobante firmado que se describe arriba. La compra y tu cuenta de Apple se rigen por las condiciones de Apple.</li>
    <li><strong>GitHub (GitHub Inc., Estados Unidos).</strong> Sirve estas páginas de la política, como se describe en la sección 3. No recibe ningún texto del CV ni nada de la app.</li>
  </ul>
  <p>Transferencias fuera del EEE. Command Code y TypeSafe AI están en Estados Unidos, así que el texto sale del Espacio Económico Europeo. El texto redactado del CV se envía a Command Code y TypeSafe AI en Estados Unidos. La salvaguarda de la transferencia se nombrará aquí cuando se confirme con esos proveedores. Supabase guarda los datos de la pasarela en Fráncfort, pero la empresa es estadounidense.</p>
  <!-- CONFIRM(U7): los contratos de encargo y la salvaguarda exacta de la transferencia (las cláusulas contractuales tipo de la Comisión y, cuando corresponda, el Marco de Privacidad de Datos UE-EE. UU.) no constan en este repositorio; confírmalos con Supabase, Command Code y TypeSafe AI antes de publicar. Aquí no se afirma ninguna salvaguarda para Supabase ni para GitHub. -->

  <h2>5. Cuánto tiempo</h2>
  <ul>
    <li><strong>En tu iPhone.</strong> Tu CV (el texto redactado, nunca el PDF) y todo lo que Atino saca de él se quedan hasta que borres el CV en la app o borres la app; retirar el permiso los borra de inmediato. Los resúmenes de los avisos se guardan 2 días. Los contadores del día y tu permiso también viven en el teléfono.</li>
    <li><strong>En la pasarela.</strong> Un registro por instalación, con el identificador aleatorio como clave: ese identificador, tu clave de App Attest (su id, su clave pública y su contador), los contadores del día, el nombre de la zona horaria de tu teléfono y los pases temporales de las peticiones en curso. Un pase dura 5 minutos. El registro se borra a los 60 días sin actividad. La pasarela guarda además totales diarios de lo que le cuesta el servicio de ordenación (sin identificador, sin texto y sin búsquedas) durante 90 días, para sostener el presupuesto compartido.</li>
    <li><strong>En la pasarela, por suscripción.</strong> Un registro por suscripción, con el número que Apple le da (el identificador de la transacción original) como clave: los identificadores de las instalaciones que la han usado y cuándo se vio cada una por última vez. Sin datos de pago y sin copia del comprobante de Apple. El registro se borra a los 60 días sin actividad.</li>
    <li><strong>Command Code y TypeSafe AI.</strong> El texto puede conservarse según sus propias condiciones; esas copias no podemos borrarlas nosotros.</li>
    <!-- CONFIRM(U7): cuánto tiempo conservan el texto Command Code y TypeSafe AI no consta en este repositorio; confírmalo antes de publicar. -->
    <li><strong>Apple.</strong> La compra es un registro de Apple, sujeto a sus condiciones.</li>
  </ul>

  <h2>6. Tus derechos</h2>
  <p>Tienes derecho a acceder, rectificar, suprimir, limitar y oponerte al tratamiento, y a la portabilidad de tus datos. Puedes retirar tu permiso cuando quieras: abre Ajustes › Privacidad › «Retirar el permiso y borrar mis datos». Eso borra de una vez tu CV y todo lo que Atino ha sacado de él en el iPhone. Para ver o editar el texto que se enviaría: Ajustes › Tu CV › «Lo que sale de este iPhone».</p>
  <p>Como Seize no guarda ninguna copia de tu CV en ningún otro sitio, la mayoría de las solicitudes se resuelven borrándolo en la app. Para cualquier otra cosa, o para ejercer cualquier derecho, escribe a <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>. También puedes reclamar ante tu autoridad de protección de datos: en España, la Agencia Española de Protección de Datos (<a href="https://www.aepd.es" rel="noopener">aepd.es</a>), o la autoridad del lugar donde vivas.</p>

  <h2>7. Menores</h2>
  <p>Atino no está pensado para menores de 16 años. No tratamos sus datos a sabiendas; si crees que un menor ha usado la app, escríbenos y lo borraremos.</p>

  <h2>8. Cambios</h2>
  <p>Podemos actualizar esta política; la fecha de arriba cambia. Atino versiona su permiso: si el cambio es importante —quién recibe el texto o qué puede conservar—, llega con una nueva versión de privacidad y la app te pide el permiso otra vez antes de la siguiente búsqueda. La política vigente es siempre la que está en esta dirección.</p>
''',
}

PAGES = [
    ('en', 'privacy', 'privacy', 'Atino privacy policy — Seize Apps',
     'Atino privacy: your CV stays on your iPhone, name and contact details are removed on the phone, and redacted text is sent only with your permission.'),
    ('es', 'privacy', 'privacidad', 'Política de privacidad de Atino — Seize Apps',
     'Privacidad de Atino: tu CV se queda en tu iPhone, tu nombre y tus datos de contacto se quitan en el teléfono y el texto redactado solo se envía con tu permiso.'),
]


def build_atino():
    slugs = {lang: slug for lang, _, slug, _, _ in PAGES}
    alts = {L: f'https://seizeapps.com/atino/{s}/' for L, s in slugs.items()}
    for lang, _, slug, title, desc in PAGES:
        root = '../../'
        canonical = f'atino/{slug}/'
        switch = {L: f'{root}atino/{s}/' for L, s in slugs.items()}
        html = (head(lang, title, desc, root, canonical, alts=alts) + header(lang, root, canonical, switch=switch)
                + legal_main(lang, PRIVACY[lang]) + footer(lang, root))
        write(f'atino/{slug}/index.html', html)
