# Generates seizeapps.com in English (root) and Spanish (/es/):
#   index.html · apps/<slug>.html · privacy.html · terms.html   (+ the same under es/)
# Run from anywhere: python3 tools/gen_site.py
# Identity: SEIZE 2026 (brand/design-tokens.json v2.1, brand/sheets/02-web-ui-system.png).
import os, sys
SITE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
CSS_V='2026-09-16c'
LANGS=['en','es']

# ---------------------------------------------------------------- UI strings
UI={
 'en': dict(
   nav_apps='Apps', nav_phil='Philosophy', nav_work='Work with us', nav_studio='Studio', nav_cta='Get in touch',
   lang_switch='Español', lang_switch_aria='Leer en castellano',
   footer_tag='Apps for a brighter tomorrow.', footer_privacy='Privacy', footer_terms='Terms',
   copyright='© 2026 Seize Apps · Izotz Cristobal Mota &amp; Sendoa Sola · Basque Country, Spain',
   site_title='Seize Apps — Extraordinary iOS apps for everyday life',
   site_desc='Seize designs and builds exceptional iOS apps that make life better: {apps}. An independent studio from the Basque Country that also builds apps and websites for clients.',
   og_title='Seize — Ideas into extraordinary.',
   hero_eyebrow='Apps for a brighter tomorrow', hero_h1='Ideas into <span>extraordinary.</span>',
   hero_lede='We design and build exceptional iOS apps that make life better. Small, native and private by design — each one does a single job, beautifully. And we build the same way for others.',
   hero_cta='Explore our apps', hero_cta2='Work with us',
   apps_eyebrow='Apps', apps_h2='{Count} apps, <span>{count} jobs.</span>',
   apps_p='Household rhythms, the working day, recurring money, recovery, warranties, the bills a couple shares and the training block. Different problems, one way of building: a screen you understand at a glance, your data on your device, Spanish and English from day one.',
   learn_more='Learn more',
   phil_eyebrow='Philosophy', phil_h2='Beautiful. Useful. <span>Human. Possible.</span>',
   phil_p='Four words we hold every screen against. If a feature fails one of them, it doesn\'t ship — however clever it is.',
   values=[('Beautiful','Design with an opinion: one dominant colour, weight before size, motion that means something. The kind of care you notice without being told.'),
           ('Useful','Every app answers one real question people ask every day, and answers it on the first screen. No dashboards for their own sake.'),
           ('Human','No accounts, no analytics, no advertising, no dark patterns. Your data lives on your iPhone and in your own iCloud — we never see it. Copy written for people, in two languages.'),
           ('Possible','Native all the way: SwiftUI, widgets, Live Activities, Siri and Apple Health when they earn their place. Small teams can build things that feel first-party.')],
   work_eyebrow='Work with us', work_h2='The same craft, <span>for your project.</span>',
   work_p='We take on a small number of client projects a year — the ones where we can bring the same standard we hold our own apps to. If you need something built well, talk to us.',
   work_items=[('iOS apps','Native Swift and SwiftUI, from the first sketch to the App Store: product thinking, design, code, review and the release itself. Widgets, Live Activities, Siri and iCloud when they earn their place.'),
               ('Websites and web apps','Fast, accessible sites and web applications that are pleasant to use and simple to keep — from a landing page like this one to a full product.'),
               ('Custom development','Tooling, integrations and the automation that removes a job nobody should be doing by hand. Scoped, delivered, documented.')],
   work_how_title='How it works', work_how=[('Scope','A written brief with what ships, what it costs and when. No surprises halfway.'),('One lead','One of us owns your project end to end and is the person you talk to.'),('Delivery','Working software at every milestone, source code and documentation yours from day one.')],
   work_cta='Tell us about your project', work_subject='Project inquiry',
   studio_eyebrow='Studio', studio_h2='Two developers, <span>one bar.</span>',
   studio_p='Seize Apps is Izotz and Sendoa, two co-founders from the Basque Country. Every app is the two of us: the same standard of craft, the same care, from the first sketch to the release.',
   role='Co-founder · Developer', bio_izotz='Product, design and code across the whole catalogue.', bio_sendoa='Product, design and code across the whole catalogue.',
   studio_note='We ship our own apps and we build for clients, and we stay small enough that the person who wrote the code is the one reading your email.',
   contact_eyebrow='Contact', contact_h2='Say hello.', contact_p='Questions, ideas, a project, a bug you found — one address, and we read everything.',
   app_eyebrow='Seize Apps · iOS', shots_aria='Screenshots', what_eyebrow='What it does', what_h2='One job, <span>done well.</span>',
   privacy_eyebrow='Privacy', privacy_h3='Yours, not ours.', published_by='A Seize Apps app.',
   privacy_policy='Privacy policy', contact='Contact', store_badge='Download on the App Store',
   shot_alt='{name} screenshot: {cap}',
 ),
 'es': dict(
   nav_apps='Apps', nav_phil='Filosofía', nav_work='Trabaja con nosotros', nav_studio='Estudio', nav_cta='Escríbenos',
   lang_switch='English', lang_switch_aria='Read in English',
   footer_tag='Apps para un mañana mejor.', footer_privacy='Privacidad', footer_terms='Términos',
   copyright='© 2026 Seize Apps · Izotz Cristobal Mota y Sendoa Sola · País Vasco',
   site_title='Seize Apps — Apps iOS extraordinarias para el día a día',
   site_desc='Seize diseña y construye apps iOS excepcionales que mejoran la vida: {apps}. Un estudio independiente del País Vasco que también desarrolla apps y webs para clientes.',
   og_title='Seize — Ideas hechas extraordinarias.',
   hero_eyebrow='Apps para un mañana mejor', hero_h1='Ideas hechas <span>extraordinarias.</span>',
   hero_lede='Diseñamos y construimos apps iOS excepcionales que mejoran la vida. Pequeñas, nativas y privadas por diseño: cada una hace una sola cosa, y la hace bien. Y construimos igual para otros.',
   hero_cta='Ver las apps', hero_cta2='Trabaja con nosotros',
   apps_eyebrow='Apps', apps_h2='{Count} apps, <span>{count} tareas.</span>',
   apps_p='Los ritmos de casa, la jornada de trabajo, el dinero que se va cada mes, la recuperación, las garantías, las cuentas de una pareja y el bloque de entrenamiento. Problemas distintos, una sola forma de construir: una pantalla que se entiende de un vistazo, tus datos en tu dispositivo, castellano e inglés desde el primer día.',
   learn_more='Ver más',
   phil_eyebrow='Filosofía', phil_h2='Bonito. Útil. <span>Humano. Posible.</span>',
   phil_p='Cuatro palabras contra las que medimos cada pantalla. Si una función falla en una de ellas, no sale, por ingeniosa que sea.',
   values=[('Bonito','Diseño con criterio: un color dominante, peso antes que tamaño, movimiento que significa algo. Ese cuidado que se nota sin que nadie te lo diga.'),
           ('Útil','Cada app responde a una pregunta real que la gente se hace a diario, y la responde en la primera pantalla. Nada de paneles por el gusto de tenerlos.'),
           ('Humano','Sin cuentas, sin analítica, sin publicidad, sin trucos. Tus datos viven en tu iPhone y en tu propio iCloud; nosotros nunca los vemos. Textos escritos para personas, en dos idiomas.'),
           ('Posible','Nativo de principio a fin: SwiftUI, widgets, Live Activities, Siri y Apple Health cuando aportan algo. Un equipo pequeño puede construir cosas que parecen de Apple.')],
   work_eyebrow='Trabaja con nosotros', work_h2='El mismo oficio, <span>para tu proyecto.</span>',
   work_p='Aceptamos unos pocos proyectos de clientes al año: los que nos permiten trabajar con el mismo nivel que exigimos a nuestras propias apps. Si necesitas algo bien hecho, hablemos.',
   work_items=[('Apps iOS','Swift y SwiftUI nativos, del primer boceto a la App Store: producto, diseño, código, revisión y la propia publicación. Widgets, Live Activities, Siri e iCloud cuando aportan.'),
               ('Webs y aplicaciones web','Sitios y aplicaciones web rápidos, accesibles y fáciles de mantener: desde una landing como esta hasta un producto completo.'),
               ('Desarrollo a medida','Herramientas, integraciones y la automatización que quita de en medio un trabajo que nadie debería hacer a mano. Con alcance, entregado y documentado.')],
   work_how_title='Cómo trabajamos', work_how=[('Alcance','Un documento con qué se entrega, cuánto cuesta y cuándo. Sin sorpresas a mitad de camino.'),('Un responsable','Uno de los dos lleva tu proyecto de principio a fin y es con quien hablas.'),('Entregas','Software que funciona en cada hito; el código y la documentación son tuyos desde el primer día.')],
   work_cta='Cuéntanos tu proyecto', work_subject='Consulta de proyecto',
   studio_eyebrow='Estudio', studio_h2='Dos desarrolladores, <span>un mismo listón.</span>',
   studio_p='Seize Apps somos Izotz y Sendoa, dos cofundadores del País Vasco. Cada app somos los dos: el mismo nivel de exigencia y el mismo cuidado, del primer boceto a la publicación.',
   role='Cofundador · Desarrollador', bio_izotz='Producto, diseño y código en todo el catálogo.', bio_sendoa='Producto, diseño y código en todo el catálogo.',
   studio_note='Publicamos nuestras propias apps y construimos para clientes, y seguimos siendo lo bastante pequeños como para que quien escribió el código sea quien lee tu correo.',
   contact_eyebrow='Contacto', contact_h2='Escríbenos.', contact_p='Preguntas, ideas, un proyecto, un fallo que has visto: una sola dirección, y lo leemos todo.',
   app_eyebrow='Seize Apps · iOS', shots_aria='Capturas', what_eyebrow='Qué hace', what_h2='Una sola cosa, <span>bien hecha.</span>',
   privacy_eyebrow='Privacidad', privacy_h3='Tuyo, no nuestro.', published_by='Una app de Seize Apps.',
   privacy_policy='Política de privacidad', contact='Contacto', store_badge='Descargar en la App Store',
   shot_alt='Captura de {name}: {cap}',
 ),
}

# ---------------------------------------------------------------- apps
def app(slug, name, icon, lead, privacy_id, shots, en, es, appstore=None):
    # `appstore`: el id numérico de App Store Connect, solo cuando la app está
    # publicada de verdad. Si está, la página saca el badge; si no, no hay
    # badge. Nunca se escribe el href a mano en el HTML.
    return dict(slug=slug, name=name, icon=icon, lead=lead, privacy_id=privacy_id,
                shots=shots, appstore=appstore, copy={'en':en,'es':es})

APPS=[
 app('cycle-timers','Cycle Timers','cycle-timers.png','Izotz Cristobal Mota','cycle-timers',
     ['cycle-01-home.jpg','cycle-02-edit.jpg'],
     dict(one='Recurring household timers you read at a glance — from the Home Screen widget, without opening the app.',
          tags=['Household','Widgets','iOS'],
          lede='Every chore has a cycle. <strong>Cycle Timers</strong> turns the things you repeat and forget — fresh water for the plants, clean sheets, the cat litter — into glanceable rings that drain over time and restart the moment you mark them done.',
          meta=['iOS 17+','Home Screen &amp; Lock Screen widgets','No account'],
          features=[('01 / SEE','Time, at a glance','Colour and shape tell you what is fresh, what is close, and what needs attention now. No lists to read.'),
                    ('02 / TAP','Done means restarted','One tap marks a task done and begins its next cycle — directly from the Home Screen widget if you like.'),
                    ('03 / KEEP','Yours, not ours','No account and no tracking. Your timers stay on your device, where a household tool belongs.')],
          privacy='Cycle Timers collects no data whatsoever. Timers live on your device, in a private container shared only with the app\'s own widgets; reminders are scheduled locally.',
          captions=['Six rings, one glance','A timer is a name, an icon and a cycle']),
     dict(one='Temporizadores recurrentes para la casa que lees de un vistazo, desde el widget, sin abrir la app.',
          tags=['Hogar','Widgets','iOS'],
          lede='Cada tarea de casa tiene su ciclo. <strong>Cycle Timers</strong> convierte lo que repites y olvidas —el agua de las plantas, las sábanas limpias, la arena del gato— en anillos que se vacían con el tiempo y vuelven a empezar en cuanto marcas la tarea como hecha.',
          meta=['iOS 17+','Widgets de inicio y pantalla de bloqueo','Sin cuenta'],
          features=[('01 / VER','El tiempo, de un vistazo','El color y la forma te dicen qué está reciente, qué se acerca y qué necesita atención ahora. Sin listas que leer.'),
                    ('02 / TOCAR','Hecho significa reiniciado','Un toque marca la tarea como hecha y empieza el siguiente ciclo, directamente desde el widget si quieres.'),
                    ('03 / GUARDAR','Tuyo, no nuestro','Sin cuenta y sin rastreo. Tus temporizadores se quedan en tu dispositivo, donde debe estar una herramienta de casa.')],
          privacy='Cycle Timers no recoge ningún dato. Los temporizadores viven en tu dispositivo, en un contenedor privado compartido solo con los widgets de la propia app; los recordatorios se programan en local.',
          captions=['Seis anillos, un vistazo','Un temporizador es un nombre, un icono y un ciclo'])),
 app('tempo','Tempo','tempo.png','Izotz Cristobal Mota','tempo',
     ['tempo-01-welcome.jpg','tempo-02-today.jpg','tempo-03-calendar.jpg'],
     dict(one='A workday companion that remembers your hours for you — arrive, work, leave — and keeps the record yours to correct.',
          tags=['Work','Time tracking','Calendar'],
          lede='Your work day is measured in what you got done, not in hours watched. <strong>Tempo</strong> notices when you arrive at work and when you leave, adds it up into one honest day, and lets you review, split or correct any of it. Manual mode from day one; automatic tracking only if you choose to draw a work zone.',
          meta=['iOS 17+','Live Activities','Calendar export','No account'],
          features=[('01 / ARRIVE','Hands-free hours','Draw a work zone once and Tempo does the rest with the location evidence iOS already keeps. Separate visits add up to one accurate workday.'),
                    ('02 / SEE','Today, clearly','Time worked, your daily target, arrival and leave — one screen, and a month view that shows on-time, light and overtime days at a glance.'),
                    ('03 / OWN','Your record, editable','Review, correct, split, merge or export. If a boundary was uncertain, Tempo asks instead of guessing.')],
          privacy='Tempo keeps your work sessions, zones and targets on your device. Location is used only to detect the work zone you drew, on the phone, and is never sent anywhere. No account, no analytics.',
          captions=['Your workday, remembered','Today: time worked against your target','A month of days, coloured by how they went']),
     dict(one='Un compañero de jornada que recuerda tus horas por ti —llegar, trabajar, salir— y deja el registro en tus manos para corregirlo.',
          tags=['Trabajo','Horas','Calendario'],
          lede='Tu jornada se mide por lo que sacas adelante, no por las horas que vigilas. <strong>Tempo</strong> se da cuenta de cuándo llegas al trabajo y cuándo te vas, lo suma en un día honesto y te deja revisar, partir o corregir cualquier tramo. Modo manual desde el primer día; seguimiento automático solo si decides dibujar una zona de trabajo.',
          meta=['iOS 17+','Live Activities','Exportar al calendario','Sin cuenta'],
          features=[('01 / LLEGAR','Horas sin tocar nada','Dibuja una zona de trabajo una vez y Tempo hace el resto con la ubicación que iOS ya guarda. Varias visitas suman una jornada exacta.'),
                    ('02 / VER','Hoy, claro','Tiempo trabajado, tu objetivo diario, llegada y salida en una pantalla, y una vista mensual que enseña de un vistazo los días en hora, cortos y con horas de más.'),
                    ('03 / TUYO','Tu registro, editable','Revisa, corrige, parte, fusiona o exporta. Si un límite no estaba claro, Tempo pregunta en vez de adivinar.')],
          privacy='Tempo guarda tus sesiones, zonas y objetivos en tu dispositivo. La ubicación se usa solo para detectar la zona de trabajo que dibujaste, en el propio teléfono, y nunca se envía a ningún sitio. Sin cuenta, sin analítica.',
          captions=['Tu jornada, recordada','Hoy: tiempo trabajado frente a tu objetivo','Un mes de días, coloreados según cómo fueron'])),
 app('drip','Drip','drip.png','Sendoa Sola','drip',
     ['drip-01-dashboard.jpg','drip-03-services.jpg','drip-04-detail.jpg','drip-02-dashboard-2.jpg'],
     dict(one='See exactly where your money drips: every subscription, bill and membership shown as what it really costs a year.',
          tags=['Subscriptions','Budget','ES · EN'],
          lede='Monthly hides the pain. <strong>Drip</strong> tracks every recurring service — subscriptions, bills, memberships — and puts the true yearly cost next to what you pay each month. In English and Spanish. No account, no ads, no subscription: just the number, and what to do about it.',
          meta=['iOS 17+','Widgets &amp; Siri Shortcuts','English · Spanish'],
          features=[('01 / REVEAL','Annual cost, always','That "just €9.99 a month" is €120 a year. Drip shows both, for every service, all the time — with a dashboard by category (the built-in ones and your own) and by billing cycle.'),
                    ('02 / CONTROL','Know what\'s next','The next 14 days of charges at a glance, free-trial alerts, a monthly budget, and a swipe to mark a charge as paid. Pause a service instead of deleting it.'),
                    ('03 / KEEP','Yours, not ours','No account and no tracking. Your services live on your device and in your own iCloud — never on a server of ours.')],
          privacy='Drip stores your services on your device, in a private container shared only with its widgets and Siri shortcuts, and in your own iCloud account — never anywhere we can see.',
          captions=['Dashboard: the yearly figure first','Every service, monthly and yearly','One service in detail','By category — yours included — and by cycle']),
     dict(one='Ve exactamente por dónde se te va el dinero: cada suscripción, recibo y cuota, con lo que cuesta de verdad al año.',
          tags=['Suscripciones','Presupuesto','ES · EN'],
          lede='Lo mensual esconde el daño. <strong>Drip</strong> lleva la cuenta de cada servicio recurrente —suscripciones, recibos, cuotas— y pone el coste anual real al lado de lo que pagas cada mes. En castellano e inglés. Sin cuenta, sin anuncios, sin suscripción: solo el número, y qué hacer con él.',
          meta=['iOS 17+','Widgets y atajos de Siri','Castellano · Inglés'],
          features=[('01 / VER','El coste anual, siempre','Ese «solo 9,99 € al mes» son 120 € al año. Drip enseña las dos cifras, para cada servicio, todo el tiempo, con un panel por categoría (las predefinidas y las tuyas) y por ciclo de cobro.'),
                    ('02 / CONTROLAR','Saber qué viene','Los cobros de los próximos 14 días de un vistazo, avisos de fin de prueba, un presupuesto mensual y un gesto para marcar un cobro como pagado. Pausa un servicio en vez de borrarlo.'),
                    ('03 / GUARDAR','Tuyo, no nuestro','Sin cuenta y sin rastreo. Tus servicios viven en tu dispositivo y en tu propio iCloud, nunca en un servidor nuestro.')],
          privacy='Drip guarda tus servicios en tu dispositivo, en un contenedor privado compartido solo con sus widgets y atajos de Siri, y en tu propia cuenta de iCloud; nunca en ningún sitio que podamos ver.',
          captions=['Panel: la cifra anual primero','Cada servicio, al mes y al año','Un servicio en detalle','Por categoría —también las tuyas— y por ciclo']), appstore='6812332005'),
 app('anchor','Anchor','anchor.png','Sendoa Sola','anchor',
     ['anchor-01-home.jpg','anchor-02-now.jpg','anchor-05-checkin.jpg','anchor-06-strategies.jpg'],
     dict(one='Daily support for eating-disorder recovery: routines that hold you and tools for the hard moment — alongside professional treatment, never instead of it.',
          tags=['Recovery','Routines','ES · EN'],
          lede='<strong>Anchor</strong> accompanies people recovering from an eating disorder. Routines that hold you — meals, rest, movement — confirmed with a tap; a single door, <em>Now</em>, for the hard moment: ride the urge, breathe with guidance, let an emotion pass, or open your safety plan. No calories, no weight, no streaks. Ever.',
          meta=['iOS 17+','Live Activities','Apple Health (optional, read-only)','English · Spanish'],
          features=[('01 / HOLD','Routines, not rules','Meals, rest and movement as daily blocks. Confirm with a tap; if a day doesn\'t go to plan, that\'s okay — Anchor says so.'),
                    ('02 / NOW','One door for the hard moment','Urge surfing with a fifteen-minute companion, guided breathing without breath holds, "let it pass" for a strong emotion, and a safety plan with your people and your region\'s helplines, two taps away.'),
                    ('03 / SEE','Without numbers','An emotional check-in with no scores, strategies grounded in DBT, CBT, ACT and self-compassion with their evidence in plain sight, and progress shown as the shape of your week — not a grade.')],
          privacy='Everything you enter stays on your device and in your own private iCloud. Apple Health is optional and read-only (sleep, activity), never weight or nutrition, and never leaves the phone. No analytics, no ads, no AI chat.',
          captions=['Home: the next routine, and «Now»','«What\'s going on?» routes to the right tool','Check-in without numbers','Strategies, with their evidence'],
          extra='Anchor is not a medical device and does not replace professional treatment. If you are in danger or your own thoughts scare you, please contact your local emergency number.'),
     dict(one='Apoyo diario en la recuperación de un trastorno alimentario: rutinas que sostienen y herramientas para el momento difícil, junto al tratamiento profesional, nunca en su lugar.',
          tags=['Recuperación','Rutinas','ES · EN'],
          lede='<strong>Anchor</strong> acompaña a personas que se recuperan de un trastorno de la conducta alimentaria. Rutinas que sostienen —comidas, descanso, movimiento— confirmadas con un toque; una sola puerta, <em>Ahora</em>, para el momento difícil: surfear el impulso, respirar con guía, dejar pasar una emoción o abrir tu plan de seguridad. Sin calorías, sin peso, sin rachas. Nunca.',
          meta=['iOS 17+','Live Activities','Apple Health (opcional, solo lectura)','Castellano · Inglés'],
          features=[('01 / SOSTENER','Rutinas, no reglas','Comidas, descanso y movimiento como bloques del día. Confirma con un toque; si un día no sale como estaba previsto, no pasa nada, y Anchor lo dice.'),
                    ('02 / AHORA','Una puerta para el momento difícil','Surf del impulso con un acompañante de quince minutos, respiración guiada sin retenciones, «déjalo pasar» para una emoción fuerte y un plan de seguridad con tu gente y los teléfonos de ayuda de tu región, a dos toques.'),
                    ('03 / VER','Sin números','Un registro emocional sin puntuaciones, estrategias basadas en DBT, TCC, ACT y autocompasión con su evidencia a la vista, y el progreso como la forma de tu semana, no como una nota.')],
          privacy='Todo lo que introduces se queda en tu dispositivo y en tu propio iCloud privado. Apple Health es opcional y de solo lectura (sueño, actividad), nunca peso ni nutrición, y nunca sale del teléfono. Sin analítica, sin anuncios, sin chat de IA.',
          captions=['Inicio: la siguiente rutina, y «Ahora»','«¿Qué está pasando?» lleva a la herramienta adecuada','Registro sin números','Estrategias, con su evidencia'],
          extra='Anchor no es un producto sanitario y no sustituye al tratamiento profesional. Si estás en peligro o tus propios pensamientos te asustan, llama al número de emergencias de tu zona.')),
 app('kover','Kover','kover.png','Sendoa Sola','kover',
     ['kover-01-products.jpg','kover-02-add.jpg','kover-03-seal.jpg','kover-04-detail.jpg'],
     dict(one='Snap the receipt, and Kover watches the warranty: what is covered, until when, and a nudge before it runs out.',
          tags=['Warranties','Receipts','ES · EN'],
          lede='Receipts fade, warranties expire quietly. <strong>Kover</strong> reads the date, store and amount from a photo or PDF of the receipt, works out the legal guarantee for your country, and keeps the photo, the serial number and the support contact in one place — with a reminder a month, a week and the day before it ends.',
          meta=['iOS 17+','Camera, Photos or PDF','English · Spanish'],
          features=[('01 / ADD','Three questions, then the seal','What did you buy, when and where, how much. Or let the receipt answer: camera, photo library or a PDF from your email, and the steps come prefilled. Saving ends on «Covered until».'),
                    ('02 / WATCH','Covered until, in plain words','Legal guarantee by country — 36 months in Spain — plus any extended warranty on top. «3 years left», not a countdown of days, on a seal that wears as time passes. Reminders at one month, one week and the day of.'),
                    ('03 / CLAIM','Everything for the day you need it','Serial number, support phone or website one tap away, the receipt photo, and a PDF to share. Claimed, replaced or gone: archive instead of delete.')],
          privacy='Kover keeps your products and receipt photos on your device and in your own iCloud account. Receipts are read on the phone with Apple\'s Vision framework — nothing is uploaded, no account, no analytics.',
          captions=['Next to expire, and the whole shelf','Three questions: what, when, how much','Saved and sealed: covered until 2029','The seal stays alive: covered until, on paper']),
     dict(one='Haz una foto al ticket y Kover vigila la garantía: qué está cubierto, hasta cuándo, y un aviso antes de que se acabe.',
          tags=['Garantías','Tickets','ES · EN'],
          lede='Los tickets se borran, las garantías caducan sin avisar. <strong>Kover</strong> lee la fecha, la tienda y el importe de una foto o un PDF del ticket, calcula la garantía legal de tu país y guarda la foto, el número de serie y el contacto de soporte en un mismo sitio, con un aviso un mes, una semana y el día antes de que termine.',
          meta=['iOS 17+','Cámara, Fotos o PDF','Castellano · Inglés'],
          features=[('01 / AÑADIR','Tres preguntas y el sello','Qué has comprado, cuándo y dónde, cuánto costó. O deja que responda el ticket: cámara, fototeca o un PDF del correo, y los pasos llegan rellenos. Guardar termina en «Cubierto hasta».'),
                    ('02 / VIGILAR','Cubierto hasta, en palabras','Garantía legal según el país —36 meses en España— más la extendida si la hay. «Quedan 3 años», no una cuenta atrás de días, en un sello que se gasta con el tiempo. Avisos un mes antes, una semana antes y el mismo día.'),
                    ('03 / RECLAMAR','Todo para el día que lo necesites','Número de serie, teléfono o web de soporte a un toque, la foto del ticket y un PDF para compartir. Reclamado, sustituido o ya no es tuyo: archivar en vez de borrar.')],
          privacy='Kover guarda tus productos y las fotos de los tickets en tu dispositivo y en tu propia cuenta de iCloud. Los tickets se leen en el propio teléfono con el framework Vision de Apple: no se sube nada, sin cuenta, sin analítica.',
          captions=['La próxima en caducar, y toda la estantería','Tres preguntas: qué, cuándo, cuánto','Guardado y sellado: cubierto hasta 2029','El sello sigue vivo: cubierto hasta, en papel']), appstore='6812714562'),
 app('tandem','Tandem','tandem.png','Sendoa Sola','tandem',
     ['tandem-01-dashboard.jpg','tandem-02-expenses.jpg','tandem-04-settle.jpg','tandem-03-reports.jpg'],
     dict(one='Fair expense splitting for couples: each pays in proportion to what they earn, and the month settles with one number.',
          tags=['Couples','Expenses','ES · EN'],
          lede='Fifty-fifty is only fair when you earn the same. <strong>Tandem</strong> takes two incomes and every shared expense — rent, groceries, the dinner out — and splits each one in proportion, so the month ends with a single transfer that both of you understand. One phone keeps the books for both.',
          meta=['iOS 17+','Widgets','English · Spanish'],
          features=[('01 / SPLIT','Proportional by default','Enter both incomes once. Every expense is split by that ratio — or 50/50, a custom share, or paid in full — and the ratio is frozen with the expense, so a raise next year never reopens last year\'s months.'),
                    ('02 / SETTLE','One number a month','Who paid what, who owes whom, and the transfer that squares it. Mark it settled; undo it if you were too quick.'),
                    ('03 / SEE','Where it goes','Recurring expenses that log themselves, reports by category, and a monthly bar of who actually paid.')],
          privacy='Tandem keeps names, incomes and expenses on your device and in your own iCloud account. Nothing is shared with anyone — not with us, and not with a server.',
          captions=['This month: shared, paid, to settle','Fixed and variable, by month','Settle up: the math, in the open','Who paid, month by month']),
     dict(one='Reparto justo de gastos en pareja: cada uno paga en proporción a lo que gana, y el mes se cierra con un solo número.',
          tags=['Pareja','Gastos','ES · EN'],
          lede='A medias solo es justo cuando ganáis lo mismo. <strong>Tandem</strong> toma los dos ingresos y cada gasto compartido —el alquiler, el súper, la cena fuera— y lo reparte en proporción, para que el mes termine con una única transferencia que los dos entendéis. Un solo móvil lleva las cuentas de los dos.',
          meta=['iOS 17+','Widgets','Castellano · Inglés'],
          features=[('01 / REPARTIR','Proporcional por defecto','Mete los dos ingresos una vez. Cada gasto se reparte con esa proporción —o a medias, con una parte propia, o lo paga uno entero— y la proporción se congela con el gasto, así una subida de sueldo el año que viene no reabre los meses del anterior.'),
                    ('02 / LIQUIDAR','Un número al mes','Quién pagó qué, quién debe a quién y la transferencia que lo cuadra. Márcalo como liquidado; deshazlo si te precipitaste.'),
                    ('03 / VER','A dónde va','Gastos recurrentes que se apuntan solos, informes por categoría y una barra mensual de quién pagó de verdad.')],
          privacy='Tandem guarda los nombres, los ingresos y los gastos en tu dispositivo y en tu propia cuenta de iCloud. No se comparte nada con nadie: ni con nosotros ni con un servidor.',
          captions=['Este mes: compartido, pagado, por liquidar','Fijos y variables, por mes','Liquidar: las cuentas, a la vista','Quién pagó, mes a mes'])),
 app('meso','Meso','meso.png','Sendoa Sola','meso',
     ['meso-01-today.jpg','meso-02-workout.jpg','meso-03-grid.jpg','meso-04-week.jpg'],
     dict(one='The gym version of your coach\'s spreadsheet: blocks of weeks, load and reps per set, effort as reps in reserve.',
          tags=['Strength','Blocks &amp; RIR','ES · EN'],
          lede='A programme is a block of weeks, not a list of workouts. <strong>Meso</strong> takes the sessions your coach wrote — or one of its templates — and turns them into a log that fills itself in: every set arrives with last time\'s load and reps, one tap confirms it, and effort is logged as reps in reserve. Then it shows whether the block is moving: tonnage per exercise week by week, sets per muscle against what the evidence says is enough.',
          meta=['iOS 17+','Apple Health','English · Spanish'],
          features=[('01 / LOG','One tap per set','Load, reps and RIR come pre-filled from the last time you did the exercise; the tick is the whole input when nothing changed. Steppers on real gym increments, a note per exercise, a warm-up ramp when you want one, and a substitute that lists the same muscle first.'),
                    ('02 / PROGRESS','Blocks, not days','A grid of tonnage per exercise across the weeks, sets per muscle against the 10–20 band, and the best set with its estimated 1RM as you go. No streaks, no confetti: the progression is measured in blocks.'),
                    ('03 / LEARN','Every rule with its source','Why RIR, why a deload, why the band — each principle in the app carries its evidence and how solid it is, with references you can check. Honest about what is settled and what is not.')],
          privacy='Meso keeps your programmes and sessions on your device and in your own iCloud account. Apple Health is written only if you switch it on, and never read. No account, no analytics.',
          captions=['Today: the session that is due, with last week next to it','A set is a tick; the rest is pre-filled','Tonnage per exercise, week by week','Sets per muscle against the evidence band']),
     dict(one='La versión de gimnasio del Excel de tu entrenador: bloques de semanas, carga y repeticiones por serie, esfuerzo en repeticiones en reserva.',
          tags=['Fuerza','Bloques y RIR','ES · EN'],
          lede='Un programa es un bloque de semanas, no una lista de entrenos. <strong>Meso</strong> toma las sesiones que te escribió el entrenador —o una de sus plantillas— y las convierte en un registro que se rellena solo: cada serie llega con la carga y las repeticiones de la última vez, un toque la confirma y el esfuerzo se apunta como repeticiones en reserva. Después enseña si el bloque avanza: tonelaje por ejercicio semana a semana y series por músculo frente a lo que la evidencia dice que basta.',
          meta=['iOS 17+','Apple Salud','Castellano · Inglés'],
          features=[('01 / APUNTAR','Un toque por serie','Carga, repeticiones y RIR vienen rellenos de la última vez que hiciste el ejercicio; el ✓ es toda la entrada cuando nada cambió. Incrementos reales de gimnasio, una nota por ejercicio, calentamiento en rampa si lo quieres y un sustituto que lista primero el mismo músculo.'),
                    ('02 / PROGRESAR','Bloques, no días','Una rejilla de tonelaje por ejercicio a lo largo de las semanas, series por músculo frente a la banda de 10–20 y la mejor serie con su 1RM estimado según avanzas. Sin rachas ni confeti: la progresión se mide en bloques.'),
                    ('03 / APRENDER','Cada regla con su fuente','Por qué RIR, por qué una descarga, por qué la banda: cada principio de la app lleva su evidencia y lo sólida que es, con referencias que puedes comprobar. Honesta con lo que está claro y lo que no.')],
          privacy='Meso guarda tus programas y sesiones en tu dispositivo y en tu propia cuenta de iCloud. Apple Salud solo se escribe si lo activas, y nunca se lee. Sin cuenta, sin analítica.',
          captions=['Hoy: la sesión que toca, con la semana pasada al lado','Una serie es un ✓; el resto viene relleno','Tonelaje por ejercicio, semana a semana','Series por músculo frente a la banda de la evidencia'])),
]

# ---------------------------------------------------------------- chrome
def other(lang): return 'es' if lang=='en' else 'en'
def prefix(lang): return 'es/' if lang=='es' else ''

def head(lang, title, desc, root, canonical, og_title=None):
    # canonical is the path inside the language tree (e.g. 'apps/kover.html' or '')
    en_url='https://seizeapps.com/'+canonical; es_url='https://seizeapps.com/es/'+canonical
    self_url=es_url if lang=='es' else en_url
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#060E1F">
<meta name="description" content="{desc}">
<link rel="canonical" href="{self_url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="es" href="{es_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Seize Apps">
<meta property="og:title" content="{og_title or title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{self_url}">
<meta property="og:image" content="https://seizeapps.com/assets/og.jpg">
<meta property="og:locale" content="{'es_ES' if lang=='es' else 'en_US'}">
<meta name="twitter:card" content="summary_large_image">
<title>{title}</title>
<link rel="icon" type="image/png" sizes="64x64" href="{root}favicon.png">
<link rel="icon" type="image/png" sizes="32x32" href="{root}favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="{root}favicon-16.png">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{root}assets/site.css?v={CSS_V}">
</head>
<body>
'''

def header(lang, root, canonical, current=None):
    t=UI[lang]; home=root+prefix(lang)
    switch=root+prefix(other(lang))+canonical
    def nav(href, label, key):
        cur=' aria-current="page"' if current==key else ''
        return f'<a href="{home}{href}"{cur}>{label}</a>'
    return f'''<header class="site-header shell">
  <a class="brand" href="{home}index.html" aria-label="Seize">
    <img class="brand-mark" src="{root}assets/seize-mark.png?v=1" alt="" width="36" height="36">
    <span class="wordmark">SEIZE</span>
  </a>
  <nav class="site-nav" aria-label="Main">
    {nav('index.html#apps',t['nav_apps'],'apps')}
    {nav('index.html#philosophy',t['nav_phil'],'philosophy')}
    {nav('index.html#work',t['nav_work'],'work')}
    {nav('index.html#studio',t['nav_studio'],'studio')}
    <a class="lang" href="{switch}" hreflang="{other(lang)}" lang="{other(lang)}" aria-label="{t['lang_switch_aria']}">{t['lang_switch']}</a>
    <a class="button small" href="mailto:hello@seizeapps.com">{t['nav_cta']}</a>
  </nav>
</header>
'''

def footer(lang, root):
    t=UI[lang]; home=root+prefix(lang)
    return f'''<footer class="site-footer">
  <div class="footer-inner shell">
    <div class="footer-brand">
      <img src="{root}assets/seize-mark.png?v=1" alt="" width="28" height="28">
      <div>
        <p class="footer-signoff">{t['footer_tag']}</p>
        <p class="copyright">{t['copyright']}</p>
      </div>
    </div>
    <nav class="footer-links" aria-label="Footer">
      <a href="{home}index.html#apps">{t['nav_apps']}</a>
      <a href="{home}privacy.html">{t['footer_privacy']}</a>
      <a href="{home}terms.html">{t['footer_terms']}</a>
      <a href="https://github.com/SeizeApps" rel="noopener">GitHub</a>
      <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>
    </nav>
  </div>
</footer>
</body>
</html>
'''

WAVE='''<svg class="wave" viewBox="0 0 1440 420" preserveAspectRatio="none" aria-hidden="true">
  <defs>
    <linearGradient id="wg" x1="0" x2="1" y1="0" y2="0">
      <stop offset="0" stop-color="#007AFF" stop-opacity="0"/>
      <stop offset=".45" stop-color="#007AFF" stop-opacity=".55"/>
      <stop offset=".75" stop-color="#22D3EE" stop-opacity=".7"/>
      <stop offset="1" stop-color="#22D3EE" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <path d="M0 300 C 240 200, 420 380, 700 260 S 1120 120, 1440 240" fill="none" stroke="url(#wg)" stroke-width="2"/>
  <path d="M0 340 C 260 240, 460 420, 760 300 S 1160 160, 1440 280" fill="none" stroke="url(#wg)" stroke-width="1.5" opacity=".6"/>
  <path d="M0 260 C 220 160, 400 340, 660 220 S 1080 80, 1440 200" fill="none" stroke="url(#wg)" stroke-width="1" opacity=".4"/>
</svg>'''

def write(path, html):
    full=os.path.join(SITE,path); os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full,'w').write(html)

# The app count and the app list in the copy come from APPS, so adding an
# app never leaves a «six apps» behind (it did, 20/09/2026).
NUMBERS={'en':['zero','one','two','three','four','five','six','seven','eight','nine','ten'],
         'es':['cero','una','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','diez']}
def fill_counts():
    n=len(APPS)
    for lang in LANGS:
        names=[a['name'] for a in APPS]
        joiner=' and ' if lang=='en' else ' y '
        apps=', '.join(names[:-1])+joiner+names[-1]
        word=NUMBERS[lang][n]
        UI[lang]['site_desc']=UI[lang]['site_desc'].format(apps=apps)
        UI[lang]['apps_h2']=UI[lang]['apps_h2'].format(Count=word.capitalize(), count=word)
fill_counts()

# ---------------------------------------------------------------- index
def build_index(lang):
    t=UI[lang]; root='../' if lang=='es' else ''; home=root+prefix(lang)
    cards=''.join(f'''
    <a class="app-card" href="{home}apps/{a['slug']}.html">
      <img src="{root}assets/icons/{a['icon']}" alt="" width="64" height="64">
      <h3>{a['name']}</h3>
      <p class="one-liner">{a['copy'][lang]['one']}</p>
      <div class="tags">{''.join(f'<span>{x}</span>' for x in a['copy'][lang]['tags'])}</div>
      <span class="card-more">{t['learn_more']} <span aria-hidden="true">→</span></span>
    </a>''' for a in APPS)
    values=''.join(f'<div class="value"><span class="num">0{i+1}</span><h3>{h}</h3><p>{p}</p></div>' for i,(h,p) in enumerate(t['values']))
    work=''.join(f'<div class="feature"><span class="num">0{i+1}</span><h3>{h}</h3><p>{p}</p></div>' for i,(h,p) in enumerate(t['work_items']))
    how=''.join(f'<div class="step"><h4>{h}</h4><p>{p}</p></div>' for h,p in t['work_how'])
    subject=t['work_subject'].replace(' ','%20')
    html=head(lang, t['site_title'], t['site_desc'], root, '', og_title=t['og_title'])+header(lang, root, 'index.html')+f'''<main>
  <section class="hero" aria-labelledby="hero-title">
    {WAVE}
    <div class="shell hero-grid">
      <div class="hero-copy">
        <p class="eyebrow">{t['hero_eyebrow']}</p>
        <h1 id="hero-title">{t['hero_h1']}</h1>
        <p class="lede">{t['hero_lede']}</p>
        <div class="cta-row">
          <a class="button" href="#apps">{t['hero_cta']}</a>
          <a class="button ghost" href="#work">{t['hero_cta2']}</a>
        </div>
      </div>
      <div class="hero-phone" aria-hidden="true">
        <div class="phone"><img src="{root}assets/shots/anchor-01-home.jpg" alt="" width="552" height="1200"></div>
      </div>
    </div>
  </section>

  <section class="section shell" id="apps" aria-labelledby="apps-title">
    <div class="section-head">
      <div><p class="eyebrow">{t['apps_eyebrow']}</p><h2 id="apps-title">{t['apps_h2']}</h2></div>
      <p>{t['apps_p']}</p>
    </div>
    <div class="app-grid">{cards}
    </div>
  </section>

  <section class="section shell" id="philosophy" aria-labelledby="philosophy-title">
    <div class="section-head">
      <div><p class="eyebrow">{t['phil_eyebrow']}</p><h2 id="philosophy-title">{t['phil_h2']}</h2></div>
      <p>{t['phil_p']}</p>
    </div>
    <div class="values">{values}</div>
  </section>

  <section class="section shell" id="work" aria-labelledby="work-title">
    <div class="section-head">
      <div><p class="eyebrow">{t['work_eyebrow']}</p><h2 id="work-title">{t['work_h2']}</h2></div>
      <p>{t['work_p']}</p>
    </div>
    <div class="features">{work}</div>
    <div class="work-how">
      <div class="work-how-head"><h3>{t['work_how_title']}</h3><a class="button" href="mailto:hello@seizeapps.com?subject={subject}">{t['work_cta']}</a></div>
      <div class="steps">{how}</div>
    </div>
  </section>

  <section class="section shell" id="studio" aria-labelledby="studio-title">
    <div class="section-head">
      <div><p class="eyebrow">{t['studio_eyebrow']}</p><h2 id="studio-title">{t['studio_h2']}</h2></div>
      <p>{t['studio_p']}</p>
    </div>
    <div class="studio">
      <div class="person">
        <div class="initials a" aria-hidden="true">IC</div>
        <div><h3>Izotz Cristobal Mota</h3><p class="role">{t['role']}</p><p class="bio">{t['bio_izotz']}</p></div>
      </div>
      <div class="person">
        <div class="initials b" aria-hidden="true">SS</div>
        <div><h3>Sendoa Sola</h3><p class="role">{t['role']}</p><p class="bio">{t['bio_sendoa']}</p></div>
      </div>
      <p class="studio-note">{t['studio_note']}</p>
    </div>
  </section>

  <section class="shell" id="contact" aria-labelledby="contact-title">
    <div class="contact">
      <div><p class="eyebrow">{t['contact_eyebrow']}</p><h2 id="contact-title">{t['contact_h2']}</h2><p class="note" style="margin-top:10px">{t['contact_p']}</p></div>
      <a class="button" href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>
    </div>
  </section>
</main>
'''+footer(lang, root)
    write(prefix(lang)+'index.html', html)

# ---------------------------------------------------------------- app pages
def build_app(lang, a):
    t=UI[lang]; c=a['copy'][lang]; root='../../' if lang=='es' else '../'; home=root+prefix(lang)
    shots=''.join(f'<figure><div class="phone"><img src="{root}assets/shots/{f}" alt="{t["shot_alt"].format(name=a["name"], cap=cap)}" loading="lazy" width="552" height="1200"></div><figcaption>{cap}</figcaption></figure>' for f,cap in zip(a['shots'], c['captions']))
    feats=''.join(f'<div class="feature"><span class="num">{n}</span><h3>{h}</h3><p>{p}</p></div>' for n,h,p in c['features'])
    extra=f'<p class="note" style="margin-top:20px">{c["extra"]}</p>' if c.get('extra') else ''
    # Sin id de App Store no hay badge: el sitio nunca enlaza a una ficha que
    # todavía no existe, ni menciona revisión, TestFlight ni fechas.
    # La URL va sin país a propósito: Apple redirige a la tienda del visitante.
    badge=(f'<a class="store-badge button" href="https://apps.apple.com/app/id{a["appstore"]}">{t["store_badge"]}</a>'
           if a.get('appstore') else '')
    html=head(lang, f'{a["name"]} — Seize Apps', c['one'].replace('"','&quot;'), root, f'apps/{a["slug"]}.html')+header(lang, root, f'apps/{a["slug"]}.html', 'apps')+f'''<main>
  <section class="app-hero shell" aria-labelledby="app-title">
    <div class="app-hero-copy">
      <img class="icon" src="{root}assets/icons/{a['icon']}" alt="" width="96" height="96">
      <p class="eyebrow">{t['app_eyebrow']}</p>
      <h1 id="app-title">{a['name']}</h1>
      <p class="lede">{c['lede']}</p>
      <div class="app-meta">{''.join(f'<span>{m}</span>' for m in c['meta'])}</div>
      {badge}
      {extra}
    </div>
  </section>
  <section class="shell" aria-label="{t['shots_aria']}"><div class="shots shots-{len(a['shots'])}">{shots}</div></section>

  <section class="section shell" aria-labelledby="what-title">
    <div class="section-head">
      <div><p class="eyebrow">{t['what_eyebrow']}</p><h2 id="what-title">{t['what_h2']}</h2></div>
    </div>
    <div class="features">{feats}</div>
  </section>

  <section class="shell" aria-labelledby="privacy-title">
    <div class="privacy-box">
      <div><p class="eyebrow">{t['privacy_eyebrow']}</p><h3 id="privacy-title" style="margin-bottom:10px">{t['privacy_h3']}</h3><p>{c['privacy']}</p><p class="note" style="margin-top:14px">{t['published_by'].format(lead=a['lead'])}</p></div>
      <div class="links"><a class="button ghost" href="{home}privacy.html#{a['privacy_id']}">{t['privacy_policy']}</a><a class="button ghost" href="mailto:hello@seizeapps.com?subject={a['name']}">{t['contact']}</a></div>
    </div>
  </section>
</main>
'''+footer(lang, root)
    write(prefix(lang)+f'apps/{a["slug"]}.html', html)

# ---------------------------------------------------------------- legal
from gen_legal_copy import LEGAL
def build_legal(lang, kind):
    t=UI[lang]; root='../' if lang=='es' else ''
    L=LEGAL[lang][kind]
    html=head(lang, L['title'], L['desc'], root, f'{kind}.html')+header(lang, root, f'{kind}.html')+f'<main class="shell legal">\n{L["body"]}\n</main>\n'+footer(lang, root)
    write(prefix(lang)+f'{kind}.html', html)

if __name__=='__main__':
    for lang in LANGS:
        build_index(lang)
        for a in APPS: build_app(lang, a)
        build_legal(lang,'privacy'); build_legal(lang,'terms')
    print('ok', len(APPS), 'apps ×', len(LANGS), 'languages')
