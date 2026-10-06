# Generates seizeapps.com in English (root), Spanish (/es/) and French (/fr/):
#   index.html · apps/<slug>.html · privacy.html · terms.html   (+ the same under es/ and fr/)
# The French copy lives in gen_site_fr.py (UI_FR, APPS_FR) and gen_legal_fr.py.
# Run from anywhere: python3 tools/gen_site.py
# Identity: SEIZE 2026 (brand/design-tokens.json v2.1, brand/sheets/02-web-ui-system.png).
import os, re, sys, unicodedata
SITE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
CSS_V='2026-10-05.2'
LANGS=['en','es','fr']
# Language switch: short label and the link's accessible name, in the target language.
LANG_LINK={'en':('EN','Read in English'),'es':('ES','Leer en castellano'),'fr':('FR','Lire en français')}
OG_LOCALE={'en':'en_US','es':'es_ES','fr':'fr_FR'}
# Language on arrival (05/10/2026). GitHub Pages can't negotiate on the server, so the English pages (the
# x-default) carry a tiny script in <head>: if the visitor never picked a language with the switch, it goes
# to the first of the browser's languages that the page has an alternate for (read from its own hreflang
# links, so Garum's legal pages work too), keeping the #anchor. Spanish and French URLs are never
# redirected: someone who lands there asked for that language. A click on the switch is remembered
# (localStorage) and wins over the browser. No IP geolocation: a country is not a language.
LANG_PICK='''<script>(function(){try{var k='seize-lang',c=localStorage.getItem(k);var alt={};document.querySelectorAll('link[rel=alternate][hreflang]').forEach(function(l){alt[l.hreflang]=l.href});var want=null;if(c){want=c}else{var ls=navigator.languages||[navigator.language||''];for(var i=0;i<ls.length;i++){var b=(ls[i]||'').toLowerCase().split('-')[0];if(alt[b]){want=b;break}}}if(want&&want!=='en'&&alt[want]&&!/bot|crawl|spider/i.test(navigator.userAgent)){location.replace(alt[want]+location.hash)}}catch(e){}})();</script>
'''

# ---------------------------------------------------------------- UI strings
UI={
 'en': dict(
   nav_apps='Apps', nav_phil='Philosophy', nav_work='Work with us', nav_studio='Studio', nav_cta='Get in touch',
   footer_tag='Apps for a brighter tomorrow.', footer_privacy='Privacy', footer_terms='Terms',
   copyright='© 2026 Seize Apps · Izotz Cristobal Mota &amp; Sendoa Sola · Basque Country, Spain',
   site_title='Seize Apps — Extraordinary iOS apps for everyday life',
   site_desc='Seize designs and builds exceptional iOS apps that make life better: {apps}. An independent studio from the Basque Country that also builds apps and websites for clients.',
   og_title='Seize — Ideas into extraordinary.',
   hero_eyebrow='Apps for a brighter tomorrow', hero_h1='Ideas into <span>extraordinary.</span>',
   hero_lede='We design and build exceptional iOS apps that make life better. Small, native and private by design — each one does a single job, beautifully. And we build the same way for others.',
   hero_cta='Explore our apps', hero_cta2='Work with us',
   apps_eyebrow='Apps', apps_h2='{Count} apps, <span>{count} jobs.</span>',
   apps_p='Household rhythms, the working day, recurring money, recovery, warranties, the bills a couple shares, the training block, the macros you eat and the places worth the trip. Different problems, one way of building: a screen you understand at a glance, only the data the job needs, Spanish and English from day one.',
   learn_more='Learn more',
   phil_eyebrow='Philosophy', phil_h2='Beautiful. Useful. <span>Human. Possible.</span>',
   phil_p='Four words we hold every screen against. If a feature fails one of them, it doesn\'t ship — however clever it is.',
   values=[('Beautiful','Design with an opinion: one dominant colour, weight before size, motion that means something. The kind of care you notice without being told.'),
           ('Useful','Every app answers one real question people ask every day, and answers it on the first screen. No dashboards for their own sake.'),
           ('Human','No analytics, no advertising, no dark patterns. No accounts either, except where the app is a community — Garum is the only one. Everything else lives on your iPhone and in your own iCloud, and we never see it. Copy written for people, in two languages.'),
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
   privacy_policy='Privacy policy', contact='Contact', store_badge='Download on the App Store', store_icon='{name} on the App Store',
   shot_alt='{name} screenshot: {cap}',
   skip='Skip to content', lang_label='Language', soon='Coming soon', live_title='On the App Store', more_apps='More from Seize', toc_title='On this page',
   hero_proof='{n} apps · {live} on the App Store · Made in the Basque Country',
 ),
 'es': dict(
   nav_apps='Apps', nav_phil='Filosofía', nav_work='Trabaja con nosotros', nav_studio='Estudio', nav_cta='Escríbenos',
   footer_tag='Apps para un mañana mejor.', footer_privacy='Privacidad', footer_terms='Términos',
   copyright='© 2026 Seize Apps · Izotz Cristobal Mota y Sendoa Sola · País Vasco',
   site_title='Seize Apps — Apps iOS extraordinarias para el día a día',
   site_desc='Seize diseña y construye apps iOS excepcionales que mejoran la vida: {apps}. Un estudio independiente del País Vasco que también desarrolla apps y webs para clientes.',
   og_title='Seize — Ideas hechas extraordinarias.',
   hero_eyebrow='Apps para un mañana mejor', hero_h1='Ideas hechas <span>extraordinarias.</span>',
   hero_lede='Diseñamos y construimos apps iOS excepcionales que mejoran la vida. Pequeñas, nativas y privadas por diseño: cada una hace una sola cosa, y la hace bien. Y construimos igual para otros.',
   hero_cta='Ver las apps', hero_cta2='Trabaja con nosotros',
   apps_eyebrow='Apps', apps_h2='{Count} apps, <span>{count} tareas.</span>',
   apps_p='Los ritmos de casa, la jornada de trabajo, el dinero que se va cada mes, la recuperación, las garantías, las cuentas de una pareja, el bloque de entrenamiento, los macros de lo que comes y los sitios que merecen la pena. Problemas distintos, una sola forma de construir: una pantalla que se entiende de un vistazo, solo los datos que hacen falta, castellano e inglés desde el primer día.',
   learn_more='Ver más',
   phil_eyebrow='Filosofía', phil_h2='Bonito. Útil. <span>Humano. Posible.</span>',
   phil_p='Cuatro palabras contra las que medimos cada pantalla. Si una función falla en una de ellas, no sale, por ingeniosa que sea.',
   values=[('Bonito','Diseño con criterio: un color dominante, peso antes que tamaño, movimiento que significa algo. Ese cuidado que se nota sin que nadie te lo diga.'),
           ('Útil','Cada app responde a una pregunta real que la gente se hace a diario, y la responde en la primera pantalla. Nada de paneles por el gusto de tenerlos.'),
           ('Humano','Sin analítica, sin publicidad, sin trucos. Tampoco cuentas, salvo donde la app es una comunidad: Garum es la única. Todo lo demás vive en tu iPhone y en tu propio iCloud, y nosotros nunca lo vemos. Textos escritos para personas, en dos idiomas.'),
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
   privacy_policy='Política de privacidad', contact='Contacto', store_badge='Descargar en la App Store', store_icon='{name} en la App Store',
   shot_alt='Captura de {name}: {cap}',
   skip='Saltar al contenido', lang_label='Idioma', soon='Próximamente', live_title='En la App Store', more_apps='Más de Seize', toc_title='En esta página',
   hero_proof='{n} apps · {live} en la App Store · Hechas en el País Vasco',
 ),
}

# ---------------------------------------------------------------- apps
def app(slug, name, icon, lead, privacy_id, shots, en, es, appstore=None, privacy_path=None):
    # The French block comes from gen_site_fr.APPS_FR[slug] (added after APPS).
    # `appstore`: el id numérico de App Store Connect, solo cuando la app está
    # publicada de verdad. Si está, la página saca el badge; si no, no hay
    # badge. Nunca se escribe el href a mano en el HTML.
    # `privacy_path`: {'en': ..., 'es': ...} relativo a la raíz, para una app con
    # política propia (Garum), relativo a la portada de cada idioma (la de es está en /es/).
    return dict(slug=slug, name=name, icon=icon, lead=lead, privacy_id=privacy_id,
                shots=shots, appstore=appstore, privacy_path=privacy_path, copy={'en':en,'es':es})

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
          captions=['Seis anillos, un vistazo','Un temporizador es un nombre, un icono y un ciclo']), appstore='6796827400'),
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
          captions=['Tu jornada, recordada','Hoy: tiempo trabajado frente a tu objetivo','Un mes de días, coloreados según cómo fueron']), appstore='6761499275'),
 app('drip','Drip','drip.png','Sendoa Sola','drip',
     ['drip-01-dashboard.jpg','drip-03-services.jpg','drip-05-categories.jpg','drip-06-recap.jpg'],
     dict(one='See exactly where your money drips: every subscription, bill and membership shown as what it really costs a year.',
          tags=['Subscriptions','Budget','ES · EN · FR'],
          lede='Monthly hides the pain. <strong>Drip</strong> tracks every recurring service — subscriptions, bills, memberships — and puts the true yearly cost next to what you pay each month. Free for everyday use; Drip Pro is a one-time purchase, with a free 30-day trial. No account, no ads, no subscription: just the number, and what to do about it.',
          meta=['iOS 17+','Free · Pro, one-time purchase','Widgets &amp; Siri (Pro)','English · Spanish · French'],
          features=[('01 / REVEAL','Annual cost, always','That "just €9.99 a month" is €120 a year. Drip shows both, for every service, all the time, with the total by month, quarter and year. Drip Pro adds the deeper look: the twelve-month trend, seasonal patterns and the split by category, your own included.'),
                    ('02 / CONTROL','Know what\'s next','The next 14 days of charges at a glance, free-trial alerts and a swipe to mark a charge as paid. Pause a service instead of deleting it. With Drip Pro, a monthly budget and a yearly recap of what you spent.'),
                    ('03 / KEEP','Yours, not ours','No account and no tracking. Your services live on your device and in your own iCloud — never on a server of ours.')],
          privacy='Drip stores your services on your device, in a private container shared only with its widgets and Siri shortcuts, and in your own iCloud account — never anywhere we can see.',
          captions=['Dashboard: the yearly figure first','Every service, monthly and yearly','Where it drips most, and by category','The yearly recap (Pro)']),
     dict(one='Ve exactamente por dónde se te va el dinero: cada suscripción, recibo y cuota, con lo que cuesta de verdad al año.',
          tags=['Suscripciones','Presupuesto','ES · EN · FR'],
          lede='Lo mensual esconde el daño. <strong>Drip</strong> lleva la cuenta de cada servicio recurrente —suscripciones, recibos, cuotas— y pone el coste anual real al lado de lo que pagas cada mes. Gratis para el día a día; Drip Pro es una compra única, con 30 días de prueba gratis. Sin cuenta, sin anuncios, sin suscripción: solo el número, y qué hacer con él.',
          meta=['iOS 17+','Gratis · Pro, pago único','Widgets y Siri (Pro)','Castellano · Inglés · Francés'],
          features=[('01 / VER','El coste anual, siempre','Ese «solo 9,99 € al mes» son 120 € al año. Drip enseña las dos cifras, para cada servicio, todo el tiempo, con el total por mes, trimestre y año. Drip Pro añade el análisis a fondo: la tendencia a doce meses, los patrones estacionales y el reparto por categoría, también las tuyas.'),
                    ('02 / CONTROLAR','Saber qué viene','Los cobros de los próximos 14 días de un vistazo, avisos de fin de prueba y un gesto para marcar un cobro como pagado. Pausa un servicio en vez de borrarlo. Con Drip Pro, un presupuesto mensual y el resumen anual de lo que has gastado.'),
                    ('03 / GUARDAR','Tuyo, no nuestro','Sin cuenta y sin rastreo. Tus servicios viven en tu dispositivo y en tu propio iCloud, nunca en un servidor nuestro.')],
          privacy='Drip guarda tus servicios en tu dispositivo, en un contenedor privado compartido solo con sus widgets y atajos de Siri, y en tu propia cuenta de iCloud; nunca en ningún sitio que podamos ver.',
          captions=['Panel: la cifra anual primero','Cada servicio, al mes y al año','Por dónde se va más, y por categoría','El resumen anual (Pro)']), appstore='6812332005'),
 app('anchor','Anchor','anchor.png','Sendoa Sola','anchor',
     ['anchor-01-home.jpg','anchor-02-now.jpg','anchor-05-checkin.jpg','anchor-06-strategies.jpg'],
     dict(one='Daily support for eating-disorder recovery: routines that hold you and tools for the hard moment — alongside professional treatment, never instead of it.',
          tags=['Recovery','Routines','ES · EN · FR'],
          lede='<strong>Anchor</strong> accompanies people recovering from an eating disorder. Routines that hold you — meals, rest, movement — confirmed with a tap; a single door, <em>Now</em>, for the hard moment: ride the urge, breathe with guidance, let an emotion pass, or open your safety plan. No calories, no weight, no streaks. Ever.',
          meta=['iOS 17+','Free','Live Activities','Apple Health (optional, read-only)','English · Spanish · French'],
          features=[('01 / HOLD','Routines, not rules','Meals, rest and movement as daily blocks. Confirm with a tap; if a day doesn\'t go to plan, that\'s okay — Anchor says so.'),
                    ('02 / NOW','One door for the hard moment','Urge surfing with a fifteen-minute companion, guided breathing without breath holds, "let it pass" for a strong emotion, and a safety plan with your people and your region\'s helplines, two taps away.'),
                    ('03 / SEE','Without numbers','An emotional check-in with no scores, strategies grounded in DBT, CBT, ACT and self-compassion with their evidence in plain sight, and progress shown as the shape of your week — not a grade.')],
          privacy='Everything you enter stays on your device and in your own private iCloud. Apple Health is optional and read-only (sleep, activity), never weight or nutrition, and never leaves the phone. No analytics, no ads, no AI chat.',
          captions=['Home: the next routine, and «Now»','«What\'s going on?» routes to the right tool','Check-in without numbers','Strategies, with their evidence'],
          extra='Anchor is not a medical device and does not replace professional treatment. If you are in danger or your own thoughts scare you, please contact your local emergency number.'),
     dict(one='Apoyo diario en la recuperación de un trastorno alimentario: rutinas que sostienen y herramientas para el momento difícil, junto al tratamiento profesional, nunca en su lugar.',
          tags=['Recuperación','Rutinas','ES · EN · FR'],
          lede='<strong>Anchor</strong> acompaña a personas que se recuperan de un trastorno de la conducta alimentaria. Rutinas que sostienen —comidas, descanso, movimiento— confirmadas con un toque; una sola puerta, <em>Ahora</em>, para el momento difícil: surfear el impulso, respirar con guía, dejar pasar una emoción o abrir tu plan de seguridad. Sin calorías, sin peso, sin rachas. Nunca.',
          meta=['iOS 17+','Gratis','Live Activities','Apple Salud (opcional, solo lectura)','Castellano · Inglés · Francés'],
          features=[('01 / SOSTENER','Rutinas, no reglas','Comidas, descanso y movimiento como bloques del día. Confirma con un toque; si un día no sale como estaba previsto, no pasa nada, y Anchor lo dice.'),
                    ('02 / AHORA','Una puerta para el momento difícil','Surf del impulso con un acompañante de quince minutos, respiración guiada sin retenciones, «déjalo pasar» para una emoción fuerte y un plan de seguridad con tu gente y los teléfonos de ayuda de tu región, a dos toques.'),
                    ('03 / VER','Sin números','Un registro emocional sin puntuaciones, estrategias basadas en DBT, TCC, ACT y autocompasión con su evidencia a la vista, y el progreso como la forma de tu semana, no como una nota.')],
          privacy='Todo lo que introduces se queda en tu dispositivo y en tu propio iCloud privado. Apple Salud es opcional y de solo lectura (sueño, actividad), nunca peso ni nutrición, y nunca sale del teléfono. Sin analítica, sin anuncios, sin chat de IA.',
          captions=['Inicio: la siguiente rutina, y «Ahora»','«¿Qué está pasando?» lleva a la herramienta adecuada','Registro sin números','Estrategias, con su evidencia'],
          extra='Anchor no es un producto sanitario y no sustituye al tratamiento profesional. Si estás en peligro o tus propios pensamientos te asustan, llama al número de emergencias de tu zona.'), appstore='6812615752'),
 app('kover','Kover','kover.png','Sendoa Sola','kover',
     ['kover-01-products.jpg','kover-02-add.jpg','kover-04-detail.jpg','kover-05-alerts.jpg'],
     dict(one='Snap the receipt, and Kover watches the warranty: what is covered, until when, and a nudge before it runs out.',
          tags=['Warranties','Receipts','ES · EN · FR'],
          lede='Receipts fade, warranties expire quietly. <strong>Kover</strong> reads the date, store and amount from a photo or PDF of the receipt, works out the legal guarantee for your country, and keeps the photo, the serial number and the support contact in one place — with a reminder a month before, a week before and on the day it ends.',
          meta=['iOS 17+','Free · Pro, one-time purchase','Camera, Photos or PDF','English · Spanish · French'],
          features=[('01 / ADD','Three questions, then the seal','What did you buy, when and where, how much. Or let the receipt answer: camera, photo library or a PDF from your email, and the steps come prefilled. Saving ends on «Covered until».'),
                    ('02 / WATCH','Covered until, in plain words','Legal guarantee by country — 36 months in Spain — plus any extended warranty on top. «3 years left», not a countdown of days, on a seal that wears as time passes. Reminders at one month, one week and the day of.'),
                    ('03 / CLAIM','Everything for the day you need it','Serial number, support phone or website one tap away, and the receipt photo. Claimed, replaced or gone: archive instead of delete. Kover Pro adds more documents per product, a claim PDF, a CSV export and Siri — a one-time purchase, with a free 30-day trial.')],
          privacy='Kover keeps your products and receipt photos on your device and in your own iCloud account. Receipts are read on the phone with Apple\'s Vision framework — nothing is uploaded, no account, no analytics.',
          captions=['Next to expire, and the whole shelf','Three questions: what, when, how much — or the receipt','Covered until 2029, on its seal','Reminders before it runs out']),
     dict(one='Haz una foto al ticket y Kover vigila la garantía: qué está cubierto, hasta cuándo, y un aviso antes de que se acabe.',
          tags=['Garantías','Tickets','ES · EN · FR'],
          lede='Los tickets se borran, las garantías caducan sin avisar. <strong>Kover</strong> lee la fecha, la tienda y el importe de una foto o un PDF del ticket, calcula la garantía legal de tu país y guarda la foto, el número de serie y el contacto de soporte en un mismo sitio, con un aviso un mes antes, una semana antes y el mismo día en que termina.',
          meta=['iOS 17+','Gratis · Pro, pago único','Cámara, Fotos o PDF','Castellano · Inglés · Francés'],
          features=[('01 / AÑADIR','Tres preguntas y el sello','Qué has comprado, cuándo y dónde, cuánto costó. O deja que responda el ticket: cámara, fototeca o un PDF del correo, y los pasos llegan rellenos. Guardar termina en «Cubierto hasta».'),
                    ('02 / VIGILAR','Cubierto hasta, en palabras','Garantía legal según el país —36 meses en España— más la extendida si la hay. «Quedan 3 años», no una cuenta atrás de días, en un sello que se gasta con el tiempo. Avisos un mes antes, una semana antes y el mismo día.'),
                    ('03 / RECLAMAR','Todo para el día que lo necesites','Número de serie, teléfono o web de soporte a un toque, y la foto del ticket. Reclamado, sustituido o ya no es tuyo: archivar en vez de borrar. Kover Pro añade más documentos por producto, un PDF de reclamación, exportar a CSV y Siri: una compra única, con 30 días de prueba gratis.')],
          privacy='Kover guarda tus productos y las fotos de los tickets en tu dispositivo y en tu propia cuenta de iCloud. Los tickets se leen en el propio teléfono con el framework Vision de Apple: no se sube nada, sin cuenta, sin analítica.',
          captions=['La próxima en caducar, y toda la estantería','Tres preguntas: qué, cuándo, cuánto, o el ticket','Cubierto hasta 2029, en su sello','Avisos antes de que se acabe']), appstore='6812714562'),
 app('tandem','Tandem','tandem.png','Sendoa Sola','tandem',
     ['tandem-01-dashboard.jpg','tandem-02-expenses.jpg','tandem-04-settle.jpg','tandem-03-reports.jpg'],
     dict(one='Fair expense splitting for couples: each pays in proportion to what they earn, and the month settles with one number.',
          tags=['Couples','Expenses','ES · EN · FR'],
          lede='Fifty-fifty is only fair when you earn the same. <strong>Tandem</strong> takes two incomes and every shared expense — rent, groceries, the dinner out — and splits each one in proportion, so the month ends with a single transfer that both of you understand. One phone keeps the books for both.',
          meta=['iOS 17+','Free · Pro, one-time purchase','Widgets (Pro)','English · Spanish · French'],
          features=[('01 / SPLIT','Proportional by default','Enter both incomes once. Every expense is split by that ratio — or 50/50, or paid in full by one of you, or, with Tandem Pro, any share you agree on — and the ratio is frozen with the expense, so a raise next year never reopens last year\'s months.'),
                    ('02 / SETTLE','One number a month','Who paid what, who owes whom, and the transfer that squares it. Mark it settled; undo it if you were too quick.'),
                    ('03 / SEE','Where it goes','Recurring expenses that log themselves. Tandem Pro adds reports by category and month, reminders to log and to settle, and widgets — a one-time purchase, with a free 30-day trial.')],
          privacy='Tandem keeps names, incomes and expenses on your device and in your own iCloud account. Nothing is shared with anyone — not with us, and not with a server.',
          captions=['This month: shared, paid, to settle','Fixed and variable, by month','Settle up: the math, in the open','Reports: who paid, month by month (Pro)']),
     dict(one='Reparto justo de gastos en pareja: cada uno paga en proporción a lo que gana, y el mes se cierra con un solo número.',
          tags=['Pareja','Gastos','ES · EN · FR'],
          lede='A medias solo es justo cuando ganáis lo mismo. <strong>Tandem</strong> toma los dos ingresos y cada gasto compartido —el alquiler, el súper, la cena fuera— y lo reparte en proporción, para que el mes termine con una única transferencia que los dos entendéis. Un solo móvil lleva las cuentas de los dos.',
          meta=['iOS 17+','Gratis · Pro, pago único','Widgets (Pro)','Castellano · Inglés · Francés'],
          features=[('01 / REPARTIR','Proporcional por defecto','Mete los dos ingresos una vez. Cada gasto se reparte con esa proporción —o a medias, o lo paga uno entero, o, con Tandem Pro, la parte que acordéis— y la proporción se congela con el gasto, así una subida de sueldo el año que viene no reabre los meses del anterior.'),
                    ('02 / LIQUIDAR','Un número al mes','Quién pagó qué, quién debe a quién y la transferencia que lo cuadra. Márcalo como liquidado; deshazlo si te precipitaste.'),
                    ('03 / VER','A dónde va','Gastos recurrentes que se apuntan solos. Tandem Pro añade informes por categoría y por mes, recordatorios para apuntar y para liquidar, y widgets: una compra única, con 30 días de prueba gratis.')],
          privacy='Tandem guarda los nombres, los ingresos y los gastos en tu dispositivo y en tu propia cuenta de iCloud. No se comparte nada con nadie: ni con nosotros ni con un servidor.',
          captions=['Este mes: compartido, pagado, por liquidar','Fijos y variables, por mes','Liquidar: las cuentas, a la vista','Informes: quién pagó, mes a mes (Pro)']), appstore='6812734713'),
 app('meso','Meso','meso.png','Sendoa Sola','meso',
     ['meso-01-today.jpg','meso-02-workout.jpg','meso-03-grid.jpg','meso-04-week.jpg'],
     dict(one='The gym version of your coach\'s spreadsheet: blocks of weeks, load and reps per set, effort as reps in reserve.',
          tags=['Strength','Blocks &amp; RIR','ES · EN · FR'],
          lede='A programme is a block of weeks, not a list of workouts. <strong>Meso</strong> takes the sessions your coach wrote — or one of its templates — and turns them into a log that fills itself in: every set arrives pre-filled from your best recent session, the ones left follow each set you confirm, one tap confirms it, and effort is logged as reps in reserve. Then it shows whether the block is moving: tonnage per exercise week by week and, with Meso Pro, sets per muscle against what the evidence says is enough.',
          meta=['iOS 17+','Free · Pro, one-time purchase','Apple Health (Pro)','English · Spanish · French'],
          features=[('01 / LOG','One tap per set','Load, reps and RIR come pre-filled from your best recent session, and every set you confirm re-plans the ones left at their own reps and RIR; the tick is the whole input when nothing changed. A note per exercise, a warm-up ramp when you want one, and the next set on the Lock Screen.'),
                    ('02 / PROGRESS','Blocks, not days','A grid of tonnage per exercise across the weeks. Meso Pro adds sets per muscle against the 10–20 band, each exercise\'s estimated 1RM across blocks, the next step before your first set, and your gyms with their bar and plates — a one-time purchase, with a free 30-day trial. No streaks, no confetti: the progression is measured in blocks.'),
                    ('03 / LEARN','Every rule with its source','Why RIR, why a deload, why the band — each principle in the app carries its evidence and how solid it is, with references you can check. Honest about what is settled and what is not.')],
          privacy='Meso keeps your programmes and sessions on your device and in your own iCloud account. Apple Health is written only if you switch it on, and never read. No account, no analytics.',
          captions=['Today: the session that is due','A set is a tick; the rest is pre-filled','Tonnage per exercise, week by week','Sets per muscle against the evidence band (Pro)']),
     dict(one='La versión de gimnasio del Excel de tu entrenador: bloques de semanas, carga y repeticiones por serie, esfuerzo en repeticiones en reserva.',
          tags=['Fuerza','Bloques y RIR','ES · EN · FR'],
          lede='Un programa es un bloque de semanas, no una lista de entrenos. <strong>Meso</strong> toma las sesiones que te escribió el entrenador —o una de sus plantillas— y las convierte en un registro que se rellena solo: cada serie llega rellena con tu mejor sesión reciente, las que quedan siguen a cada serie que confirmas, un toque la confirma y el esfuerzo se apunta como repeticiones en reserva. Después enseña si el bloque avanza: tonelaje por ejercicio semana a semana y, con Meso Pro, series por músculo frente a lo que la evidencia dice que basta.',
          meta=['iOS 17+','Gratis · Pro, pago único','Apple Salud (Pro)','Castellano · Inglés · Francés'],
          features=[('01 / APUNTAR','Un toque por serie','Carga, repeticiones y RIR vienen rellenos de tu mejor sesión reciente, y cada serie que confirmas replanifica las que quedan a sus repeticiones y su RIR; el ✓ es toda la entrada cuando nada cambió. Una nota por ejercicio, series de aproximación si las quieres y la siguiente serie en la pantalla de bloqueo.'),
                    ('02 / PROGRESAR','Bloques, no días','Una rejilla de tonelaje por ejercicio a lo largo de las semanas. Meso Pro añade las series por músculo frente a la banda de 10–20, el 1RM estimado de cada ejercicio a lo largo de los bloques, el siguiente paso antes de la primera serie y tus gimnasios con su barra y sus discos: una compra única, con 30 días de prueba gratis. Sin rachas ni confeti: la progresión se mide en bloques.'),
                    ('03 / APRENDER','Cada regla con su fuente','Por qué RIR, por qué una descarga, por qué la banda: cada principio de la app lleva su evidencia y lo sólida que es, con referencias que puedes comprobar. Honesta con lo que está claro y lo que no.')],
          privacy='Meso guarda tus programas y sesiones en tu dispositivo y en tu propia cuenta de iCloud. Apple Salud solo se escribe si lo activas, y nunca se lee. Sin cuenta, sin analítica.',
          captions=['Hoy: la sesión que toca','Una serie es un ✓; el resto viene relleno','Tonelaje por ejercicio, semana a semana','Series por músculo frente a la banda de la evidencia (Pro)']), appstore='6813842295'),
 app('grain','Grain','grain.png','Sendoa Sola','grain',
     ['grain-01-today.jpg','grain-02-meal.jpg','grain-03-label.jpg','grain-04-history.jpg'],
     dict(one='A macro diary with no diet talk: energy, protein, carbs and fat against the targets you set, and what is left.',
          tags=['Nutrition','Macros','ES · EN · FR'],
          lede='Building muscle, losing fat or following your dietitian\'s numbers: <strong>Grain</strong> works the same for all of them. You set the targets; Grain logs what you eat and compares, without suggesting or judging. Going over is not painted red and hitting it is not green — the bar fills in its colour and the figure says "+12 g". Over 4,000 foods from the CIQUAL and BEDCA tables ship inside the app and work offline.',
          meta=['iOS 26+','Free · Pro, one-time purchase','Apple Health (Pro)','English · Spanish · French'],
          features=[('01 / LOG','The way you would say it','Type "2 eggs, 60 g toast, 10 g olive oil" and Grain splits the foods and suggests the grams, with the values from the tables; you check it before it is logged. Or search, scan a barcode (Open Food Facts), build a recipe and log it by its cooked weight, or add the macros by hand. Usual servings are already set, and any food that does not match its pack can be corrected.'),
                    ('02 / READ','The label, on your iPhone','With Grain Pro, point the camera at the nutrition table, or pick a photo, and the per-100 g values fill themselves in. It is read on the device; nothing leaves the phone.'),
                    ('03 / REVIEW','How your weeks add up','Each meal adds up next to its name, and the day shows what is left of the energy and each macro. Grain Pro adds history over seven, thirty or ninety days, averaging only the days you logged — and saying so — plus widgets and Apple Health; a one-time purchase, with a free 30-day trial. No streaks, no weight.')],
          privacy='Grain keeps your diary on your device and in your own iCloud account. From a barcode only the number leaves, to Open Food Facts, unless you choose to send a product to it. Apple Health is written only if you switch it on, and never read. No account, no analytics.',
          captions=['Today: what you ate against your targets, and what is left','Write a meal the way you would say it','A nutrition label, read on the iPhone (Pro)','How the weeks add up, by macro (Pro)']),
     dict(one='Un diario de macros sin tono de dieta: energía, proteína, hidratos y grasa frente a las metas que pones tú, y lo que queda.',
          tags=['Nutrición','Macros','ES · EN · FR'],
          lede='Ganar músculo, perder grasa o seguir lo que te ha pautado tu nutricionista: <strong>Grain</strong> sirve igual para todo. Las metas las pones tú; Grain anota lo que comes y lo compara, sin proponer ni juzgar. Pasarte no se pinta de rojo ni cumplir de verde: la barra se llena en su color y la cifra dice «+12 g». Más de 4.000 alimentos de las tablas CIQUAL y BEDCA van dentro de la app y funcionan sin conexión.',
          meta=['iOS 26+','Gratis · Pro, pago único','Apple Salud (Pro)','Castellano · Inglés · Francés'],
          features=[('01 / ANOTAR','Como lo dirías','Escribe «2 huevos, 60 g de pan tostado, 10 g de aceite» y Grain separa los alimentos y propone los gramos, con los valores de las tablas; tú lo revisas antes de anotar. O busca, escanea un código de barras (Open Food Facts), crea una receta y apúntala por su peso ya cocinado, o mete los macros a mano. Las raciones habituales ya vienen puestas, y cualquier alimento que no cuadre con su envase se puede corregir.'),
                    ('02 / LEER','La etiqueta, en tu iPhone','Con Grain Pro, apunta la cámara a la tabla nutricional, o elige una foto, y los valores por 100 g se rellenan solos. Se lee en el dispositivo; nada sale del teléfono.'),
                    ('03 / REPASAR','Cómo suman tus semanas','Cada comida suma junto a su nombre y el día enseña lo que queda de energía y de cada macro. Grain Pro añade el historial de siete, treinta o noventa días, con la media de los días anotados (y diciéndolo), además de widgets y Apple Salud: una compra única, con 30 días de prueba gratis. Sin rachas, sin peso.')],
          privacy='Grain guarda tu diario en tu dispositivo y en tu propia cuenta de iCloud. Del código de barras solo sale el número, a Open Food Facts, salvo que elijas enviarle un producto. Apple Salud solo se escribe si lo activas, y nunca se lee. Sin cuenta, sin analítica.',
          captions=['Hoy: lo que has comido frente a tus metas, y lo que queda','Escribe una comida como lo dirías','Una etiqueta nutricional, leída en el iPhone (Pro)','Cómo suman las semanas, por macro (Pro)']), appstore='6816346843'),
 app('garum','Garum','garum.png','Sendoa Sola','garum',
     ['garum-01-map.jpg','garum-02-why.jpg','garum-03-detail.jpg','garum-04-signed.jpg'],
     dict(one='A map of places that are there for a reason: classics, established places and new ones with a point of view, each with its why, everything signed.',
          tags=['Food &amp; drink','Curated map','ES · EN · FR'],
          lede='<strong>Garum</strong> is a map where places get in on merit, not on stars or ads. Three lists by age — classics open for more than 25 years, established places between 3 and 25, and new ones under 3 with a point of view — and places move from one to the next on their own as the years go by. Each one carries the reasons it is there and notes signed by whoever stands behind it. Anyone can propose a place; it gets in when a Curator signs it or enough trusted people back it.',
          meta=['iOS 26+','Free','Apple Maps','English · Spanish · French'],
          features=[('01 / WHY','Every place, with its why','A closed list of reasons — a classic, the product, the price, the room — and signed notes, never a score. Opening hours, phone and directions come live from Apple Maps.'),
                    ('02 / FIND','What you fancy, now','Filter by list, kind of place, food, price and moment, or by what fits right now. What to order and whether to book are on the card.'),
                    ('03 / SIGNED','Everything is signed','See who backs each place and follow people with your taste. Propose what is missing; if it does not get in, you are told why. Curators can also suggest removing a place that has closed or lost its way, and moderation decides, with its reason.')],
          privacy='Browsing the map needs no account. To see why each place is there and to contribute, you sign in with Apple, without giving your email: you appear with the name you share with Apple (or one you set later) and a username, and what you contribute is published, on a server in the EU. No ads, no analytics. Garum has its own privacy policy and terms.',
          captions=['The map: classics, established places and new ones','Each place with its reasons and signed notes','What to order, when to go, whether to book','Everything signed: who backs what']),
     dict(one='Un mapa de sitios que están por algo: clásicos, establecidos y nuevos con criterio, cada uno con su porqué, todo firmado.',
          tags=['Comer y beber','Mapa con criterio','ES · EN · FR'],
          lede='<strong>Garum</strong> es un mapa donde los sitios entran por mérito, no por estrellas ni anuncios. Tres listas por antigüedad —clásicos con más de 25 años abiertos, establecidos entre 3 y 25 y nuevos de menos de 3 con criterio—, y los sitios pasan de una a la siguiente solos con los años. Cada uno lleva los motivos por los que está y notas firmadas por quien lo respalda. Cualquiera puede proponer un sitio; entra cuando lo firma un Curator o lo respaldan suficientes personas de confianza.',
          meta=['iOS 26+','Gratis','Apple Maps','Castellano · Inglés · Francés'],
          features=[('01 / PORQUÉ','Cada sitio, con su porqué','Una lista cerrada de motivos —un clásico, el producto, el precio, el local— y notas firmadas, nunca una puntuación. Horario, teléfono y cómo llegar, en vivo desde Apple Maps.'),
                    ('02 / ENCONTRAR','Lo que te apetece, ahora','Filtra por lista, tipo de sitio, cocina, precio y momento, o por lo que encaja ahora mismo. Qué pedir y si hay que reservar, en la ficha.'),
                    ('03 / FIRMADO','Todo va firmado','Mira quién respalda cada sitio y sigue a gente con tu gusto. Propón lo que falta; si no entra, te decimos por qué. Los Curators también pueden sugerir quitar un sitio que ha cerrado o ya no es lo que era, y la moderación decide, con su motivo.')],
          privacy='Mirar el mapa no necesita cuenta. Para ver por qué está cada sitio y para aportar, entras con Apple, sin dar tu correo: apareces con el nombre que compartes con Apple (o el que pongas después) y un nombre de usuario, y lo que aportas se publica, en un servidor en la UE. Sin anuncios ni analítica. Garum tiene su propia política de privacidad y sus condiciones.',
          captions=['El mapa: clásicos, establecidos y nuevos','Cada sitio con sus motivos y notas firmadas','Qué pedir, cuándo ir, si hay que reservar','Todo firmado: quién respalda qué']),
     privacy_path={'en': 'garum/privacy/', 'es': '../garum/privacidad/', 'fr': '../garum/confidentialite/'}, appstore='6816385891'),
 # Sacapuntas (Kids, 02/10/2026): solo en castellano y solo en España; su propia política, con versión para niños.
 app('sacapuntas','Sacapuntas','sacapuntas.png','Sendoa Sola','sacapuntas',
     ['sacapuntas-01-shelf.jpg','sacapuntas-02-sum.jpg','sacapuntas-03-village.jpg','sacapuntas-04-report.jpg'],
     dict(one='Primary-school workbooks, from age 6 to 12, in Spanish and Basque: arithmetic, times tables, accents, grammar and reading comprehension, with a village that grows with every page done well.',
          tags=['Education','Primary school','ES · EU'],
          lede='The workbooks every Spanish child knows, made digital and with a sense of humour. <strong>Sacapuntas</strong> ("pencil sharpener") covers column arithmetic with carrying and borrowing, long multiplication and division in the Spanish layout, number facts and times tables, Spanish syllables and accentuation by the RAE rules, grammar and reading comprehension. Each child studies in their own language: there is a Basque path too. Short pages with a clear end; every page done well earns shavings to build the child\'s own village. For the Spanish school system, in Spanish and Basque.',
          meta=['iOS 26+','iPhone &amp; iPad','Free · Pro, lifetime or subscription','Spanish · Basque'],
          features=[('01 / COLUMNS','Digit by digit','Each digit in its box and each carry where it goes. A mistake marks the box and the hint says which column to look at; a repeated slip is recognised and explained. A correct answer is never marked wrong for using another method.'),
                    ('02 / ACCENTS','Agudas, llanas, esdrújulas','The stressed syllable, the three classes and "does it take an accent?", by the 2010 Spanish spelling rules, with real words of the child\'s year.'),
                    ('03 / FAMILIES','Behind the family code','Profiles, a weekly report with what is hard and an activity to do together, the school year and what the class has covered, the school\'s methods, printable worksheets with answers, and Sacapuntas Pro: once and for good or by subscription, with a free trial that ends on its own. The child never sees a price.')],
          privacy='Sacapuntas collects no data from the child: no account, no ads, no analytics, no notifications. Progress stays on the device and, if the family leaves it on, in its own iCloud.',
          captions=['The shelf: what to do next','Column sums, digit by digit','The village built with shavings','For the family: the weekly report']),
     dict(one='Cuadernillos para toda la primaria, de 6 a 12 años, en castellano y en euskera: cuentas, tablas, tildes, gramática y comprensión lectora, con un pueblo que crece con cada página bien terminada.',
          tags=['Educación','Primaria','ES · EU'],
          lede='Los cuadernillos de toda la vida, digitales y con gracia. <strong>Sacapuntas</strong> trae las cuentas en columna con sus llevadas, multiplicar por dos cifras y dividir en la caja de siempre, sumas y tablas, numeración, sílabas, tildes con las reglas de la RAE, gramática y comprensión lectora. Cada niño estudia en su idioma: también hay un camino de Euskara. Páginas cortas con un final claro; cada página bien terminada da virutas para construir su propio pueblo. Para mentes afiladas.',
          meta=['iOS 26+','iPhone y iPad','Gratis · Pro, de por vida o por suscripción','Castellano · Euskera'],
          features=[('01 / CUENTAS','Cifra a cifra','Cada cifra en su casilla y cada llevada en su sitio. Un fallo marca la casilla y la pista dice qué columna mirar; si el mismo error se repite, se reconoce y se explica. Nunca se da por mal una cuenta bien hecha por otro método.'),
                    ('02 / TILDES','Agudas, llanas y esdrújulas','La sílaba tónica, las tres clases y «¿lleva tilde?», con la Ortografía de 2010 y palabras de su curso.'),
                    ('03 / FAMILIAS','Tras el código de familia','Perfiles, el informe de la semana con lo que le cuesta y una actividad para hacer juntos, el curso y lo visto en clase, los métodos de su colegio, fichas para imprimir con solucionario y Sacapuntas Pro: de una vez y para siempre o por suscripción, con una prueba gratis que acaba sola. El niño nunca ve un precio.')],
          privacy='Sacapuntas no recoge ningún dato del niño: sin cuenta, sin anuncios, sin analítica y sin notificaciones. El progreso se queda en el dispositivo y, si la familia lo deja activado, en su propio iCloud.',
          captions=['La estantería: lo que toca','Sumas en columna, cifra a cifra','El pueblo hecho con virutas','Para la familia: el informe de la semana']),
     privacy_path={'en': 'sacapuntas/privacidad/', 'es': '../sacapuntas/privacidad/', 'fr': '../sacapuntas/privacidad/'}),
 # GamingHub (0.5.0, aún sin publicar en la Store): sin appstore hasta que `lookup` devuelva 1.
 app('gaminghub','GamingHub','gaminghub.png','Izotz Cristobal Mota','gaminghub',
     ['gaminghub-01-home.jpg','gaminghub-02-impostor.jpg','gaminghub-03-unison.jpg'],
     dict(one='Party games for a game night, each friend on their own phone: create a room, share the code and play. Each device shows only what you are allowed to see.',
          tags=['Games','Multiplayer','EN · ES'],
          lede='Turn any evening into a game night. With <strong>GamingHub</strong> you create a room, share the code or the QR, and every friend joins from their own phone. Each device shows only what you are meant to see: your role, your word, your cards. Impostor at a masquerade ball, Vault, Unison, Rewind, Spot On and Fishbowl are original games built on classic mechanics, played live in the room.',
          meta=['iOS 17+','iPhone','Unison free · the rest, one-time purchases','English · Spanish'],
          features=[('01 / ROOM','One code, one table','Create a room, share a four-letter code or a QR, and friends appear in the lobby as they join. Resume your table after a call, a lock screen or a restart.'),
                    ('02 / SECRET','Each phone knows its own secret','Your role, your word and your cards are sent only to your device. The room sees the game; nobody sees your hand.'),
                    ('03 / PLAY','Free to try, yours to keep','Unison is free for everyone. The other games are one-time purchases, and your whole table plays free whenever the host owns the game; otherwise each player gets three free plays of each game. Purchases are shared with your family.')],
          privacy='GamingHub has no account, no email and no password. To run a room it sends a display name you choose, an avatar, an anonymous identifier and the game state to our server (Supabase), where the other players in the room see it; rooms are deleted when they empty and purged after 12 hours. No ads, no analytics, no tracking.',
          captions=['Home: create a room, join with a code or scan a QR','Impostor: break the seal to read your invitation','Unison: play your cards in order, in silence']),
     dict(one='Juegos para una noche de juegos, cada uno con su móvil: crea una sala, comparte el código y a jugar. Cada dispositivo enseña solo lo que te toca ver.',
          tags=['Juegos','Multijugador','EN · ES'],
          lede='Convierte cualquier tarde en una noche de juegos. Con <strong>GamingHub</strong> creas una sala, compartes el código o el QR y cada amigo entra desde su móvil. Cada dispositivo enseña solo lo que te toca ver: tu rol, tu palabra, tus cartas. Impostor en un baile de máscaras, Bóveda, Sintonía, Rebobina, Diana y La Pecera son juegos originales sobre mecánicas clásicas, jugados en directo en la sala.',
          meta=['iOS 17+','iPhone','Sintonía gratis · el resto, compras únicas','Castellano · Inglés'],
          features=[('01 / SALA','Un código, una mesa','Crea una sala, comparte un código de cuatro letras o un QR y tus amigos aparecen en la sala de espera según entran. Retoma tu mesa tras una llamada, el bloqueo de pantalla o un reinicio.'),
                    ('02 / SECRETO','Cada móvil guarda su secreto','Tu rol, tu palabra y tus cartas se envían solo a tu dispositivo. La sala ve la partida; nadie ve tu mano.'),
                    ('03 / JUGAR','Gratis para probar, tuyo para quedártelo','Sintonía es gratis para todos. Los demás juegos son compras únicas, y toda tu mesa juega gratis siempre que el anfitrión tenga el juego; si no, cada jugador tiene tres partidas gratis de cada uno. Las compras se comparten con tu familia.')],
          privacy='GamingHub no tiene cuenta, ni correo, ni contraseña. Para llevar una sala envía a nuestro servidor (Supabase) un nombre que eliges, un avatar, un identificador anónimo y el estado de la partida, que ven los demás jugadores de la sala; las salas se borran al vaciarse y se purgan a las 12 horas. Sin anuncios, sin analítica y sin seguimiento.',
          captions=['Inicio: crea una sala, entra con un código o escanea un QR','Impostor: rompe el sello para leer tu invitación','Sintonía: jugad las cartas en orden y en silencio'])),
 # Atino (0.1.0, aún sin publicar en la Store): sin appstore hasta que `lookup` devuelva 1. Política propia en /atino/.
 app('atino','Atino','atino.png','Izotz Cristobal Mota','atino',
     ['atino-01-matches.jpg','atino-02-job.jpg','atino-03-filters.jpg'],
     dict(one='Import your CV and see current job ads across Europe ranked by how well they fit, each with a short reason. Your name and contact details are removed on your iPhone first.',
          tags=['Jobs','Europe','CV'],
          lede='<strong>Atino</strong> reads your CV on your iPhone, takes out your name and contact details and, with your permission, has an AI model score each job against what is left. More than 100,000 current job ads from public company career pages and open employment data come with the app and update every day. Every result shows a fit percent and a short reason; the percent is an estimate, not a promise, and Apply takes you to the employer\'s own page.',
          meta=['iOS 26+','iPhone','Free · Pro, subscription','24 languages'],
          features=[('01 / IMPORT','Your CV stays yours','Import a PDF; scans work too. Atino removes your name, email, phone, address, date of birth and ID number on the phone, then shows you the exact text it would send. You can edit it, and nothing is sent until you allow it.'),
                    ('02 / RANK','Best fit first','Choose where you want to work and how, then search. Jobs come back ranked, each with a fit percent and a breakdown of the work, skills, level and requirements. One search a day and your top 10 are free.'),
                    ('03 / WATCH','Pro keeps watching','Atino Pro adds every match, all the filters, saved searches and as many searches as you need within fair use, plus one alert a day, at the time you pick, when a saved search has something new.')],
          privacy='Your CV, results and saved searches stay on your iPhone. With your permission, the redacted CV text goes through the Seize relay to Command Code and TypeSafe AI (Jev) to rank jobs; they may keep it under their own terms. No account, no analytics, no tracking. Atino has its own privacy policy.',
          captions=['Matches: current jobs ranked by fit','A job: why it fits, and where to apply','Filters: where and how you want to work']),
     dict(one='Importa tu CV y mira las ofertas de empleo de toda Europa ordenadas por lo bien que encajan, con un motivo breve en cada una. Tu nombre y tus datos de contacto se quitan antes, en tu iPhone.',
          tags=['Empleo','Europa','CV'],
          lede='<strong>Atino</strong> lee tu CV en el iPhone, quita tu nombre y tus datos de contacto y, con tu permiso, pide a un modelo de IA que puntúe cada oferta con lo que queda. Más de 100.000 ofertas vigentes, de páginas de empleo públicas de empresas y de datos abiertos de empleo, vienen con la app y se actualizan cada día. Cada resultado trae un porcentaje de encaje y un motivo breve; el porcentaje es una estimación, no una promesa, y el botón para solicitar te lleva a la página del propio empleador.',
          meta=['iOS 26+','iPhone','Gratis · Pro, suscripción','24 idiomas'],
          features=[('01 / IMPORTAR','Tu CV sigue siendo tuyo','Importa un PDF; los escaneados también valen. Atino quita en el teléfono tu nombre, correo, teléfono, dirección, fecha de nacimiento y documento de identidad, y te enseña el texto exacto que enviaría. Puedes editarlo, y no se envía nada hasta que lo permitas.'),
                    ('02 / ORDENAR','Primero, lo que mejor encaja','Elige dónde quieres trabajar y cómo, y busca. Las ofertas vuelven ordenadas, cada una con su porcentaje de encaje y un desglose de trabajo, habilidades, nivel y requisitos. Una búsqueda al día y tus 10 mejores resultados son gratis.'),
                    ('03 / VIGILAR','Pro sigue buscando por ti','Atino Pro suma todos los resultados, todos los filtros, búsquedas guardadas y todas las búsquedas que necesites dentro de un uso razonable, además de un aviso al día, a la hora que elijas, cuando una búsqueda guardada tiene algo nuevo.')],
          privacy='Tu CV, tus resultados y tus búsquedas guardadas se quedan en tu iPhone. Con tu permiso, el texto redactado del CV pasa por la pasarela de Seize hasta Command Code y TypeSafe AI (Jev) para ordenar las ofertas; pueden conservarlo según sus propias condiciones. Sin cuenta, sin analítica, sin seguimiento. Atino tiene su propia política de privacidad.',
          captions=['Resultados: ofertas vigentes ordenadas por encaje','Una oferta: por qué encaja y dónde solicitarla','Filtros: dónde y cómo quieres trabajar']),
     privacy_path={'en': 'atino/privacy/', 'es': '../atino/privacidad/', 'fr': '../atino/privacy/'}),
 # Roomy (0.0.2, aún sin publicar en la Store): sin appstore hasta que `lookup` devuelva 1 (sin id de ASC en SIGNING.yml). Privacidad: /roomy/privacy/ (solo inglés).
 app('roomy','Roomy','roomy.png','Izotz Cristobal Mota','roomy',
     ['roomy-01-home.jpg','roomy-02-swipe.jpg','roomy-03-similar.jpg'],
     dict(one='Swipe left to delete, right to keep. Roomy also finds duplicates, similar shots and huge videos, all on your iPhone.',
          tags=['Utilities','Photos','9 languages'],
          lede='A full camera roll is a chore until it becomes a game. <strong>Roomy</strong> shows your photos one at a time: swipe left to delete, right to keep, undo any swipe, and nothing is deleted until you confirm in the Trash. Smart Cleanup finds exact duplicates, bursts and near-identical shots (with the best one picked for you), screenshots and the large videos that really eat your storage, which Roomy can compress while keeping the date and location.',
          meta=['iOS 17+','iPhone','Free · Pro, subscription or lifetime','9 languages'],
          features=[('01 / SWIPE','Clean a month in minutes','Swipe through your library month by month, by On This Day memories or at random. Every swipe is undoable, and deleted items wait in the Trash until you confirm. Free: 50 swipes a day.'),
                    ('02 / FIND','The clutter, found for you','Duplicates, similar shots, screenshots and large videos each get their own queue. Similar photos arrive grouped with the best one marked, and what you swiped Keep is never pre-selected for deletion.'),
                    ('03 / FREE UP','See what you got back','Roomy Pro adds unlimited swipes, one-tap cleanup of duplicates and similar shots, and video compression that saves up to 80% of the space. Track the storage you freed and keep a daily streak.')],
          privacy='Roomy analyses your library on your iPhone only. Your photos, videos and metadata are never uploaded. No account, no analytics, no ads, no tracking: nothing leaves the phone. Purchases go through Apple.',
          captions=['Home: free space, and the clutter Roomy found','Swipe left to delete, right to keep','Similar shots grouped, with the best one marked']),
     dict(one='Desliza a la izquierda para borrar, a la derecha para quedarte. Roomy también encuentra duplicados, fotos parecidas y vídeos enormes, todo en tu iPhone.',
          tags=['Utilidades','Fotos','9 idiomas'],
          lede='Un carrete lleno es una tarea pesada hasta que se convierte en un juego. <strong>Roomy</strong> te enseña tus fotos de una en una: izquierda para borrar, derecha para quedarte, cada gesto se puede deshacer y no se borra nada hasta que lo confirmas en la Papelera. La limpieza inteligente encuentra duplicados exactos, ráfagas y fotos casi idénticas (con la mejor ya marcada), capturas de pantalla y los vídeos grandes que de verdad llenan el espacio, que Roomy puede comprimir conservando la fecha y la ubicación.',
          meta=['iOS 17+','iPhone','Gratis · Pro, suscripción o de por vida','9 idiomas'],
          features=[('01 / DESLIZAR','Un mes limpio en minutos','Recorre tu biblioteca mes a mes, por los recuerdos de «Tal día como hoy» o al azar. Cada gesto se puede deshacer y lo borrado espera en la Papelera hasta que confirmas. Gratis: 50 gestos al día.'),
                    ('02 / ENCONTRAR','El desorden, encontrado por ti','Duplicados, fotos parecidas, capturas de pantalla y vídeos grandes tienen cada uno su cola. Las parecidas llegan agrupadas con la mejor marcada, y lo que marcaste como «quedarme» nunca se preselecciona para borrar.'),
                    ('03 / LIBERAR','Mira lo que has recuperado','Roomy Pro suma gestos ilimitados, borrado de duplicados y parecidas con un toque y compresión de vídeo que ahorra hasta un 80 % del espacio. Sigue el espacio liberado y mantén una racha diaria.')],
          privacy='Roomy analiza tu biblioteca solo en tu iPhone. Tus fotos, vídeos y metadatos nunca se suben. Sin cuenta, sin analítica, sin anuncios y sin seguimiento: nada sale del teléfono. Las compras pasan por Apple.',
          captions=['Inicio: espacio libre y el desorden que ha encontrado Roomy','Izquierda para borrar, derecha para quedarte','Fotos parecidas agrupadas, con la mejor marcada']),
     privacy_path={'en': 'roomy/privacy/', 'es': '../roomy/privacy/', 'fr': '../roomy/privacy/'}),
]

from gen_site_fr import UI_FR, APPS_FR
UI['fr']=UI_FR
for a in APPS: a['copy']['fr']=APPS_FR[a['slug']]

# ---------------------------------------------------------------- chrome
def prefix(lang): return '' if lang=='en' else lang+'/'
def up(lang, depth=1): return '../'*(depth + (lang!='en'))   # from a page `depth` folders deep in its language tree to the site root

def jpeg_size(path):
    # (width, height) from the JPEG's SOF marker, so every screenshot reserves its real box (most are
    # 552×1304, a few 552×1200): no layout shift while they load.
    d=open(path,'rb').read(); i=2
    while i < len(d):
        while d[i]!=0xFF: i+=1
        while d[i]==0xFF: i+=1
        marker=d[i]; seg=int.from_bytes(d[i+1:i+3],'big')
        if marker in (0xC0,0xC1,0xC2): return int.from_bytes(d[i+6:i+8],'big'), int.from_bytes(d[i+4:i+6],'big')
        i+=1+seg
    raise ValueError(f'no SOF marker in {path}')

def shot(root, f, alt='', lazy=True, priority=False):
    w,h=jpeg_size(os.path.join(SITE,'assets','shots',f))
    load=' loading="lazy"' if lazy else ''
    prio=' fetchpriority="high"' if priority else ''
    return f'<img src="{root}assets/shots/{f}" alt="{alt}" width="{w}" height="{h}"{load}{prio} decoding="async">'

def head(lang, title, desc, root, canonical, og_title=None, alts=None, preload=()):
    # canonical is the path inside the language tree (e.g. 'apps/kover.html' or '').
    # `alts`: {lang: absolute URL} for pages outside the language trees (Garum, Sacapuntas legal);
    # a page with a single language gets no hreflang.
    alts=alts or {L: 'https://seizeapps.com/'+prefix(L)+canonical for L in LANGS}
    self_url=alts[lang]
    hreflang=''.join(f'<link rel="alternate" hreflang="{L}" href="{u}">\n' for L,u in alts.items())
    if len(alts)>1: hreflang+=f'<link rel="alternate" hreflang="x-default" href="{alts.get("en", self_url)}">\n'
    else: hreflang=''
    preloads=''.join(f'<link rel="preload" as="image" href="{u}" fetchpriority="high">\n' for u in preload)
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#060E1F">
<meta name="color-scheme" content="dark">
<meta name="description" content="{desc}">
<link rel="canonical" href="{self_url}">
{hreflang}<meta property="og:type" content="website">
<meta property="og:site_name" content="Seize Apps">
<meta property="og:title" content="{og_title or title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{self_url}">
<meta property="og:image" content="https://seizeapps.com/assets/og.jpg">
<meta property="og:locale" content="{OG_LOCALE[lang]}">
{LANG_PICK if lang=='en' and hreflang else ''}
<meta name="twitter:card" content="summary_large_image">
<title>{title}</title>
<link rel="icon" type="image/png" sizes="64x64" href="{root}favicon.png">
<link rel="icon" type="image/png" sizes="32x32" href="{root}favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="{root}favicon-16.png">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
{preloads}<link rel="stylesheet" href="{root}assets/site.css?v={CSS_V}">
<script src="{root}assets/site.js?v={CSS_V}" defer></script>
</head>
<body>
'''

def header(lang, root, canonical, current=None, switch=None):
    # `switch`: {lang: href} for the language links; default, the same page in each language tree.
    t=UI[lang]; home=root+prefix(lang)
    switch=switch or {L: root+prefix(L)+canonical for L in LANGS}
    langs=''.join(f'<span aria-current="true">{LANG_LINK[L][0]}</span>' if L==lang else
                  f'<a href="{switch[L]}" hreflang="{L}" lang="{L}" aria-label="{LANG_LINK[L][1]}">{LANG_LINK[L][0]}</a>'
                  for L in LANGS if L==lang or L in switch)
    def nav(href, label, key):
        cur=' aria-current="page"' if current==key else ''
        return f'<a href="{home}{href}"{cur}>{label}</a>'
    return f'''<a class="skip" href="#main">{t['skip']}</a>
<header class="site-header">
  <div class="shell header-inner">
    <a class="brand" href="{home}index.html" aria-label="Seize">
      <img class="brand-mark" src="{root}assets/seize-mark.png?v=1" alt="" width="32" height="32">
      <span class="wordmark">SEIZE</span>
    </a>
    <nav class="site-nav" aria-label="Main">
      {nav('index.html#apps',t['nav_apps'],'apps')}
      {nav('index.html#philosophy',t['nav_phil'],'philosophy')}
      {nav('index.html#work',t['nav_work'],'work')}
      {nav('index.html#studio',t['nav_studio'],'studio')}
    </nav>
    <div class="header-tools">
      <div class="lang" role="group" aria-label="{t['lang_label']}">{langs}</div>
      <a class="button small" href="mailto:hello@seizeapps.com">{t['nav_cta']}</a>
    </div>
  </div>
</header>
'''

def footer(lang, root):
    t=UI[lang]; home=root+prefix(lang)
    return f'''<footer class="site-footer">
  <div class="footer-inner shell">
    <div class="footer-brand">
      <img src="{root}assets/seize-mark.png?v=1" alt="" width="32" height="32" loading="lazy" decoding="async">
      <div>
        <p class="footer-signoff">{t['footer_tag']}</p>
        <p class="copyright">{t['copyright']}</p>
      </div>
    </div>
    <nav class="footer-links" aria-label="Footer">
      <a href="{home}index.html#apps">{t['nav_apps']}</a>
      <a href="{home}index.html#studio">{t['nav_studio']}</a>
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


def write(path, html):
    full=os.path.join(SITE,path); os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full,'w').write(html)

# URL viejas → nuevas (absolutas). Ver el final del fichero.
REDIRECTS=[
    ('criba/privacidad/index.html', 'https://seizeapps.com/garum/privacidad/'),
    ('criba/condiciones/index.html', 'https://seizeapps.com/garum/condiciones/'),
    ('criba/privacy/index.html', 'https://seizeapps.com/garum/privacy/'),
    ('criba/terms/index.html', 'https://seizeapps.com/garum/terms/'),
    ('apps/criba.html', 'https://seizeapps.com/apps/garum.html'),
    ('es/apps/criba.html', 'https://seizeapps.com/es/apps/garum.html'),
]

def redirect_page(url):
    return ('<!doctype html>\n<html><head><meta charset="utf-8">\n'
            f'<title>Garum</title>\n<link rel="canonical" href="{url}">\n'
            f'<meta http-equiv="refresh" content="0; url={url}">\n<meta name="robots" content="noindex">\n'
            f'</head><body><p>Criba se llama ahora Garum · Criba is now Garum: <a href="{url}">{url}</a></p></body></html>\n')

# The app count and the app list in the copy come from APPS, so adding an
# app never leaves a «six apps» behind (it did, 20/09/2026).
NUMBERS={'en':['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen'],
         'es':['cero','una','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','diez','once','doce','trece'],
         'fr':['zéro','une','deux','trois','quatre','cinq','six','sept','huit','neuf','dix','onze','douze','treize']}
def fill_counts():
    n=len(APPS)
    for lang in LANGS:
        names=[a['name'] for a in APPS]
        joiner={'en':' and ','es':' y ','fr':' et '}[lang]
        apps=', '.join(names[:-1])+joiner+names[-1]
        word=NUMBERS[lang][n]
        UI[lang]['site_desc']=UI[lang]['site_desc'].format(apps=apps)
        UI[lang]['apps_h2']=UI[lang]['apps_h2'].format(Count=word.capitalize(), count=word)
        UI[lang]['hero_proof']=UI[lang]['hero_proof'].format(n=n, live=sum(1 for a in APPS if a.get('appstore')))
fill_counts()

APPLE_GLYPH='<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path fill="currentColor" d="M16.37 12.72c-.02-2.3 1.88-3.41 1.97-3.46-1.07-1.57-2.74-1.79-3.34-1.81-1.42-.14-2.77.84-3.49.84-.72 0-1.83-.82-3.01-.8-1.55.02-2.98.9-3.77 2.29-1.61 2.79-.41 6.92 1.16 9.18.77 1.11 1.68 2.35 2.87 2.31 1.15-.05 1.59-.75 2.98-.75 1.39 0 1.78.75 3 .72 1.24-.02 2.03-1.13 2.79-2.24.88-1.29 1.24-2.53 1.26-2.6-.03-.01-2.41-.93-2.42-3.68zM14.07 5.94c.63-.77 1.06-1.83.94-2.9-.91.04-2.02.61-2.67 1.37-.58.67-1.1 1.76-.96 2.8 1.02.08 2.05-.52 2.69-1.27z"/></svg>'

def store_status(a, t):
    # Live apps carry an «App Store» pill that links straight to the listing (a sibling of the card's link:
    # a link can't sit inside another); the rest say «Coming soon». Both come from `appstore`, never by hand.
    if not a.get('appstore'): return f'<span class="status soon">{t["soon"]}</span>'
    label=t['store_icon'].format(name=a['name'])
    return (f'<a class="status live" href="https://apps.apple.com/app/id{a["appstore"]}" '
            f'aria-label="{label}" title="{label}">{APPLE_GLYPH}<span>App Store</span></a>')

def icon_vt(a):
    # Same name on the home card's icon and the app page's hero icon: the cross-page View Transition morphs one into the other.
    return f'style="view-transition-name:icon-{a["slug"]}"'

# ---------------------------------------------------------------- index
HERO_SHOTS=(('left','drip-01-dashboard.jpg'),('right','garum-01-map.jpg'),('front','tempo-01-welcome.jpg'))
SHIELD='<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" d="M12 3 4.5 6v5.5c0 4.6 3.1 8.3 7.5 9.5 4.4-1.2 7.5-4.9 7.5-9.5V6L12 3Z"/><path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" d="m8.8 12.2 2.3 2.3 4.3-4.6"/></svg>'

def build_index(lang):
    t=UI[lang]; root=up(lang,0); home=root+prefix(lang)
    def cards(apps):
        return ''.join(f'''
        <li class="app-card-wrap reveal" style="--i:{k%3}">
          <a class="app-card" href="{home}apps/{a['slug']}.html">
            <img class="app-icon" src="{root}assets/icons/{a['icon']}" alt="" width="64" height="64" loading="lazy" decoding="async" {icon_vt(a)}>
            <h3>{a['name']}</h3>
            <p class="one-liner">{a['copy'][lang]['one']}</p>
            <div class="tags">{''.join(f'<span>{x}</span>' for x in a['copy'][lang]['tags'])}</div>
            <span class="card-more">{t['learn_more']} <span aria-hidden="true">→</span></span>
          </a>{store_status(a, t) if a.get('appstore') else ''}
        </li>''' for k,a in enumerate(apps))
    # Live apps first, then the ones without an App Store id under «Coming soon»: the group says it, so their cards carry no pill.
    groups=''.join(f'''
    <p class="group-label" id="apps-{key}">{label}</p>
    <ul class="app-grid app-grid-{key}" role="list" aria-labelledby="apps-{key}">{cards(apps)}
    </ul>''' for key,label,apps in (('live', t['live_title'], [a for a in APPS if a.get('appstore')]),
                                       ('soon', t['soon'], [a for a in APPS if not a.get('appstore')])) if apps)
    strip=''.join(f'<li><img src="{root}assets/icons/{a["icon"]}" alt="" width="56" height="56" decoding="async"><span>{a["name"]}</span></li>' for a in APPS)
    stage=''.join(f'<div class="device device-{pos}"><div class="phone">{shot(root, f, lazy=False, priority=(pos=="front"))}</div></div>' for pos,f in HERO_SHOTS)
    values=''.join(f'<li class="value reveal" style="--i:{i}"><span class="num">0{i+1}</span><h3>{h}</h3><p>{p}</p></li>' for i,(h,p) in enumerate(t['values']))
    work=''.join(f'<li class="feature reveal" style="--i:{i}"><span class="num">0{i+1}</span><h3>{h}</h3><p>{p}</p></li>' for i,(h,p) in enumerate(t['work_items']))
    how=''.join(f'<li class="step"><span class="step-dot" aria-hidden="true"></span><h4>{h}</h4><p>{p}</p></li>' for h,p in t['work_how'])
    subject=t['work_subject'].replace(' ','%20')
    front=dict(HERO_SHOTS)['front']
    html=head(lang, t['site_title'], t['site_desc'], root, '', og_title=t['og_title'], preload=[f'{root}assets/shots/{front}'])+header(lang, root, 'index.html')+f'''<main id="main">
  <section class="hero" aria-labelledby="hero-title" data-tilt>
    <div class="shell hero-grid">
      <div class="hero-copy">
        <p class="eyebrow" style="--i:0">{t['hero_eyebrow']}</p>
        <h1 id="hero-title" style="--i:1">{t['hero_h1']}</h1>
        <p class="lede" style="--i:2">{t['hero_lede']}</p>
        <div class="cta-row" style="--i:3">
          <a class="button" href="#apps">{t['hero_cta']}</a>
          <a class="button ghost" href="#work">{t['hero_cta2']}</a>
        </div>
        <p class="hero-proof" style="--i:4">{t['hero_proof']}</p>
      </div>
      <div class="hero-stage" aria-hidden="true">{stage}</div>
    </div>
    <div class="marquee" aria-hidden="true"><div class="marquee-inner"><ul>{strip}</ul><ul>{strip}</ul></div></div>
  </section>

  <section class="section shell" id="apps" aria-labelledby="apps-title">
    <div class="section-head reveal">
      <div><p class="eyebrow">{t['apps_eyebrow']}</p><h2 id="apps-title">{t['apps_h2']}</h2></div>
      <p>{t['apps_p']}</p>
    </div>
{groups}
  </section>

  <section class="section shell" id="philosophy" aria-labelledby="philosophy-title">
    <div class="section-head reveal">
      <div><p class="eyebrow">{t['phil_eyebrow']}</p><h2 id="philosophy-title">{t['phil_h2']}</h2></div>
      <p>{t['phil_p']}</p>
    </div>
    <ol class="values" role="list">{values}</ol>
  </section>

  <section class="section shell" id="work" aria-labelledby="work-title">
    <div class="section-head reveal">
      <div><p class="eyebrow">{t['work_eyebrow']}</p><h2 id="work-title">{t['work_h2']}</h2></div>
      <p>{t['work_p']}</p>
    </div>
    <ul class="features" role="list">{work}</ul>
    <div class="work-how reveal">
      <div class="work-how-head"><h3>{t['work_how_title']}</h3><a class="button" href="mailto:hello@seizeapps.com?subject={subject}">{t['work_cta']}</a></div>
      <ol class="steps" role="list">{how}</ol>
    </div>
  </section>

  <section class="section shell" id="studio" aria-labelledby="studio-title">
    <div class="section-head reveal">
      <div><p class="eyebrow">{t['studio_eyebrow']}</p><h2 id="studio-title">{t['studio_h2']}</h2></div>
      <p>{t['studio_p']}</p>
    </div>
    <div class="studio">
      <div class="person reveal" style="--i:0">
        <div class="initials" aria-hidden="true">IC</div>
        <div><h3>Izotz Cristobal Mota</h3><p class="role">{t['role']}</p><p class="bio">{t['bio_izotz']}</p></div>
      </div>
      <div class="person reveal" style="--i:1">
        <div class="initials" aria-hidden="true">SS</div>
        <div><h3>Sendoa Sola</h3><p class="role">{t['role']}</p><p class="bio">{t['bio_sendoa']}</p></div>
      </div>
      <p class="studio-note reveal">{t['studio_note']}</p>
    </div>
  </section>

  <section class="section shell" id="contact" aria-labelledby="contact-title">
    <div class="contact reveal">
      <div><p class="eyebrow">{t['contact_eyebrow']}</p><h2 id="contact-title">{t['contact_h2']}</h2><p class="contact-p">{t['contact_p']}</p></div>
      <a class="button large" href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>
    </div>
  </section>
</main>
'''+footer(lang, root)
    write(prefix(lang)+'index.html', html)

# ---------------------------------------------------------------- app pages
def build_app(lang, a):
    t=UI[lang]; c=a['copy'][lang]; root=up(lang); home=root+prefix(lang)
    shots=''.join(f'''
      <li class="shot reveal" style="--i:{k}"><figure><div class="phone" data-tilt>{shot(root, f, t["shot_alt"].format(name=a["name"], cap=cap))}</div><figcaption>{cap}</figcaption></figure></li>'''
                  for k,(f,cap) in enumerate(zip(a['shots'], c['captions'])))
    feats=''.join(f'<li class="feature reveal" style="--i:{k}"><span class="num">{n}</span><h3>{h}</h3><p>{p}</p></li>' for k,(n,h,p) in enumerate(c['features']))
    extra=f'<p class="note app-extra">{c["extra"]}</p>' if c.get('extra') else ''
    # Sin id de App Store no hay badge: el sitio nunca enlaza a una ficha que
    # todavía no existe, ni menciona revisión, TestFlight ni fechas.
    # La URL va sin país a propósito: Apple redirige a la tienda del visitante.
    badge=(f'<a class="store-badge button" href="https://apps.apple.com/app/id{a["appstore"]}">{APPLE_GLYPH}<span>{t["store_badge"]}</span></a>'
           if a.get('appstore') else f'<span class="status soon">{t["soon"]}</span>')
    more=''.join(f'<li><a href="{home}apps/{b["slug"]}.html"><img src="{root}assets/icons/{b["icon"]}" alt="" width="56" height="56" loading="lazy" decoding="async"><span>{b["name"]}</span></a></li>'
                 for b in APPS if b is not a)
    privacy_href=home+(a['privacy_path'][lang] if a.get('privacy_path') else 'privacy.html#'+a['privacy_id'])
    html=head(lang, f'{a["name"]} — Seize Apps', c['one'].replace('"','&quot;'), root, f'apps/{a["slug"]}.html')+header(lang, root, f'apps/{a["slug"]}.html', 'apps')+f'''<main id="main">
  <section class="app-hero shell" aria-labelledby="app-title">
    <div class="app-hero-head">
      <img class="icon" src="{root}assets/icons/{a['icon']}" alt="" width="128" height="128" fetchpriority="high" {icon_vt(a)}>
      <div><p class="eyebrow">{t['app_eyebrow']}</p><h1 id="app-title">{a['name']}</h1></div>
    </div>
    <div class="app-hero-body">
      <p class="lede">{c['lede']}</p>
      <div class="app-meta">{''.join(f'<span>{m}</span>' for m in c['meta'])}</div>
      <div class="cta-row">{badge}</div>
      {extra}
    </div>
  </section>

  <section class="gallery" aria-label="{t['shots_aria']}">
    <ul class="shots-rail" role="list">{shots}
    </ul>
  </section>

  <section class="section shell" aria-labelledby="what-title">
    <div class="section-head reveal">
      <div><p class="eyebrow">{t['what_eyebrow']}</p><h2 id="what-title">{t['what_h2']}</h2></div>
    </div>
    <ul class="features" role="list">{feats}</ul>
  </section>

  <section class="section shell" aria-labelledby="privacy-title">
    <div class="privacy-box reveal">
      <div class="privacy-glyph" aria-hidden="true">{SHIELD}</div>
      <div><p class="eyebrow">{t['privacy_eyebrow']}</p><h2 id="privacy-title">{t['privacy_h3']}</h2><p>{c['privacy']}</p><p class="note">{t['published_by'].format(lead=a['lead'])}</p></div>
      <div class="links"><a class="button ghost" href="{privacy_href}">{t['privacy_policy']}</a><a class="button ghost" href="mailto:hello@seizeapps.com?subject={a['name']}">{t['contact']}</a></div>
    </div>
  </section>

  <section class="section shell more-apps" aria-labelledby="more-title">
    <h2 id="more-title" class="more-title">{t['more_apps']}</h2>
    <ul class="more-list" role="list">{more}</ul>
  </section>
</main>
'''+footer(lang, root)
    write(prefix(lang)+f'apps/{a["slug"]}.html', html)

# ---------------------------------------------------------------- legal
from gen_legal_copy import LEGAL
LEGAL_H2=re.compile(r'<h2>(.*?)</h2>')
LEGAL_TOC=re.compile(r'<nav class="toc" aria-label="([^"]*)">(.*?)</nav>', re.S)
def plain(s): return re.sub(r'<[^>]+>','',s)
def anchor(s):
    s=unicodedata.normalize('NFKD', plain(s)).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+','-',s).strip('-') or 'section'

def legal_main(lang, body):
    # Every legal page goes through here (studio-wide, Garum, Sacapuntas, Atino, Roomy). The text is never
    # touched: each bare <h2> gets an id, and on wide screens those headings (plus the app list, if the page
    # has one) become a sticky table of contents beside a ~68ch column. Narrow screens keep the inline pills.
    used=set(re.findall(r'\bid="([^"]+)"', body)); heads=[]
    def add_id(m):
        base=anchor(m.group(1)); s=base; k=2
        while s in used: s=f'{base}-{k}'; k+=1
        used.add(s); heads.append((s, plain(m.group(1))))
        return f'<h2 id="{s}">{m.group(1)}</h2>'
    body=LEGAL_H2.sub(add_id, body)
    aside=''
    if heads:
        title=UI[lang]['toc_title']
        links=''.join(f'<li><a href="#{s}">{h}</a></li>' for s,h in heads)
        m=LEGAL_TOC.search(body)
        apps=f'<p class="toc-label">{m.group(1)}</p><div class="toc-apps">{m.group(2).strip()}</div>' if m else ''
        aside=f'<aside class="legal-aside"><nav aria-label="{title}"><p class="toc-label">{title}</p><ol role="list">{links}</ol>{apps}</nav></aside>'
    return f'<main id="main" class="shell legal-page">\n<article class="legal">\n{body}\n</article>\n{aside}\n</main>\n'

def build_legal(lang, kind):
    t=UI[lang]; root=up(lang,0)
    L=LEGAL[lang][kind]
    html=head(lang, L['title'], L['desc'], root, f'{kind}.html')+header(lang, root, f'{kind}.html')+legal_main(lang, L['body'])+footer(lang, root)
    write(prefix(lang)+f'{kind}.html', html)


if __name__=='__main__':
    for lang in LANGS:
        build_index(lang)
        for a in APPS: build_app(lang, a)
        build_legal(lang,'privacy'); build_legal(lang,'terms')
    from gen_legal_criba import build_criba
    build_criba()
    # Sacapuntas (Kids, 01/10/2026): su propia política, en castellano, con versión para niños.
    from gen_legal_sacapuntas import build_sacapuntas
    build_sacapuntas()
    # Atino (05/10/2026): su propia política, en inglés y castellano.
    from gen_legal_atino import build_atino
    build_atino()
    # Roomy (05/10/2026): su página de privacidad, en inglés como la app.
    from gen_legal_roomy import build_roomy
    build_roomy()
    # Garum's share links (0.0.26): /garum/c/ and /garum/p/, and the Universal Links file.
    from gen_garum_share import build_garum_share
    build_garum_share()
    # Criba pasó a llamarse Garum (28/09/2026). Sus URL viejas siguen vivas (van dentro de builds ya
    # subidas y de fichas de la Store): GitHub Pages no redirige en el servidor, así que cada una es una
    # página mínima con meta refresh y canonical a la nueva.
    for old, new in REDIRECTS:
        write(old, redirect_page(new))
    print('ok', len(APPS), 'apps ×', len(LANGS), 'languages · Garum legal and share pages ·', len(REDIRECTS), 'redirecciones')
