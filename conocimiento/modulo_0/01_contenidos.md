# Módulo 0 — Introducción a la IA Generativa (contenidos)

**Carácter:** optativo y asincrónico. No tiene encuentro sincrónico ni actividades obligatorias. Se abrió el 19/08/2026 como entrada en calor, antes del primer encuentro.

**Sentido del módulo:** nivelar el punto de partida. Está pensado para quien nunca usó una herramienta de IA generativa. Quien ya tiene experiencia puede recorrerlo rápido o saltearlo: no afecta la aprobación.

**Bloques:** son cinco.

---

## Bloque 1 — ¿Qué es la IA generativa?

La IA generativa es un tipo de programa capaz de producir contenido nuevo —texto, imágenes, audio, video— a partir de una indicación que le damos. La palabra clave es **generar**: no busca una respuesta guardada para copiarla, como haría un buscador, sino que arma una respuesta en el momento combinando lo que aprendió durante su entrenamiento.

Cómo aprendió: se entrena a estos sistemas mostrándoles enormes cantidades de textos, imágenes y otros materiales hasta que reconocen patrones —qué palabra suele seguir a otra, qué formas y colores componen la foto de un gato, cómo se estructura una explicación—. Cuando se le pide algo, el sistema usa esos patrones para armar una respuesta coherente y probable. Por eso se lo describe como un sistema que predice, con mucha destreza, "qué sigue".

**Por qué se equivoca.** Como arma respuestas a partir de patrones, no siempre acierta: puede sonar segura y estar equivocada, mezclar datos o inventar una cita que no existe. No lo hace de mala fe: es una consecuencia de cómo funciona. Sirve como asistente al que hay que saber pedirle las cosas y cuyo resultado siempre conviene revisar, nunca como fuente que se dé por cierta sin más.

**Distinción de términos.** La inteligencia artificial es un campo enorme, con varias décadas de historia: incluye desde los sistemas que recomiendan qué serie ver hasta los que detectan fraudes bancarios. La IA generativa es una parte de ese campo —la que produce contenido nuevo— y se volvió masiva a fines de 2022, cuando estas herramientas quedaron al alcance de cualquiera con un navegador.

Hoy conviven muchas herramientas de orígenes distintos: las más conocidas son las de OpenAI, Google o Anthropic, y también hay desarrollos de otros países, incluidos varios modelos chinos menos difundidos por estos lados, que funcionan con la misma lógica.

**Lectura optativa del bloque:** un reporte del BID (Banco Interamericano de Desarrollo), en lenguaje accesible y escrito desde América Latina. Presenta las grandes "familias" de la IA —aprendizaje automático, reconocimiento de voz, visión por computadora— y muestra que la IA generativa es solo una de ellas. Cierra con uso responsable, privacidad y sesgos. Es lectura de panorama: no hace falta leerla entera.

---

## Bloque 2 — ¿De qué herramientas dispongo?

El bloque no propone memorizar una lista de herramientas, sino entender **en qué familias se agrupan** y **con qué criterio elegir** una cuando haga falta.

**Las cinco familias:**

- **Chats o asistentes de texto.** Se les escribe y responden, explican, resumen, corrigen, sugieren. Ejemplos gratuitos: ChatGPT, Gemini, Claude. Es la puerta de entrada más simple.
- **Generadores de imagen.** A partir de una descripción en palabras crean una ilustración, un afiche, un ícono. Ejemplos: Gemini (función de imágenes), Bing Image Creator, Canva con IA integrada.
- **Herramientas de audio.** Convierten texto en voz narrada o generan música de fondo. Ejemplos: ElevenLabs (plan gratuito acotado), la narración por voz de Canva.
- **Herramientas de video.** Generan clips cortos, animan una imagen o agregan subtítulos automáticos. Ejemplos: CapCut, Canva Video, Google Vids.
- **Agentes o asistentes que hacen tareas.** La familia más nueva: en lugar de responder, ejecutan una serie de pasos. Se menciona para que se sepa que existe; se mira más adelante en el curso.

**Las cuatro preguntas para evaluar una herramienta nueva:**

1. **¿Es gratis de verdad, o "gratis por ahora"?** Conviene usarla un par de veces y ver si el límite gratuito alcanza antes de armar una actividad entera alrededor de ella.
2. **¿Me pide la tarjeta para "verificar mi identidad"?** Es cada vez más común, incluso en planes que después no cobran. No es automáticamente una estafa, pero sí una señal de alerta: conviene leer bien y buscar la herramienta en internet antes de cargar un medio de pago.
3. **¿Tiene un límite, y cuál es?** Casi todas las versiones gratuitas lo tienen: usos por día, tiempo de espera, menor calidad. Para uso docente puntual suele alcanzar; lo importante es conocerlo antes de depender de la herramienta.
4. **¿La puede usar cualquier docente, sin ser "de tecnología"?** Todo lo que se usa en este taller funciona desde el navegador, con una cuenta gratuita y sin instalar nada. Si una herramienta pide "clonar un repositorio", "usar una terminal" o "conectar una API", no es para este contexto.

**Sobre los datos:** evitar cargar información sensible de estudiantes (notas, datos personales, trabajos con nombre y apellido) en herramientas gratuitas hasta no conocer bien su política de privacidad. Para explorar y aprender, usar ejemplos ficticios o materiales propios.

---

## Bloque 3 — Texto, imagen, audio y video

Qué se puede producir concretamente: materiales para la clase en cuatro formatos que hasta hace poco requerían tiempo, equipo o conocimientos que la mayoría no tiene.

**El dato que ordena todo el bloque.** Guo, Kim y Rubin analizaron 6,9 millones de sesiones de visualización en cursos universitarios en línea y encontraron que la participación cae abruptamente pasados los **seis minutos**. La recomendación es segmentar los materiales en fragmentos de menos de seis minutos. Lo valioso no es producir más material, sino piezas más chicas y más precisas: en lugar de grabar la clase entera, tres cápsulas de cuatro minutos sobre los tres conceptos donde los estudiantes siempre se traban.

Otras conclusiones del mismo estudio: los videos con estilo personal e informal resultan más atractivos que las producciones de estudio costosas; alternar el rostro con las diapositivas funciona mejor que solo diapositivas; hablar con entusiasmo y a ritmo natural rinde más que hablar artificialmente despacio. Y una idea general que atraviesa el curso: cada vez que aparece un medio nuevo, al principio lo usamos como al anterior —las primeras clases en video eran clases presenciales filmadas— y recién con el tiempo encontramos qué le sienta bien al medio nuevo.

**Un mismo tema, cuatro caminos** (ejemplo del aula: la diferencia entre eficacia y eficiencia):

- **Texto.** Pedirle a un chat la distinción con tres ejemplos cotidianos para alguien que recién empieza la carrera, más una versión corta para el apunte y una situación problemática para discutir en clase. No se usa tal cual: se lee, se corrige lo que no encaja y se conserva lo que sirve.
- **Imagen.** Con esa misma explicación, generar un esquema comparativo simple. No reemplaza al texto: le da anclaje visual a quien necesita ver la idea.
- **Audio.** Hay herramientas que toman los materiales propios y generan un audio de ocho a quince minutos donde dos voces conversan sobre el tema, con formato de podcast. Funciona bien en español y sirve para el estudiante que viaja o repasa caminando.
- **Video.** Con el guion ya escrito, una cápsula de tres o cuatro minutos: voz propia sobre diapositivas, narración generada o grabación con subtítulos automáticos. Los subtítulos mejoran la accesibilidad.

**La lógica que se repite en todo el curso:** primero está el texto —la explicación bien pensada— y de ahí se derivan la imagen, el audio y el video. No son cuatro trabajos distintos: es un trabajo que se transforma.

**Qué formato para qué.** El texto es imbatible cuando hace falta precisión conceptual y es lo que el estudiante puede citar y releer. La imagen funciona para mostrar una estructura, una comparación o un proceso con etapas. El audio gana cuando el material se consume en movimiento. El video es el más costoso de producir y conviene reservarlo para lo que hay que ver ocurrir. Regla práctica: preguntarse primero qué le está costando a los estudiantes y recién después elegir el formato.

**Sobre los costos.** Casi todo lo del curso se resuelve con herramientas gratuitas. En algunos casos puntuales una erogación pequeña ahorra mucho tiempo; cuando aparezca una de esas situaciones se dice con claridad qué se puede hacer gratis, dónde está el límite y qué se destraba pagando. Existen además programas y descuentos académicos en varias plataformas, que suelen verificar la condición docente con el correo institucional; **todavía no se verificó cuáles funcionan efectivamente con un correo de la UNLu**, así que queda anotado como posibilidad a explorar, no como promesa.

**Lectura optativa del bloque:** una síntesis en español del estudio de Guo, Kim y Rubin — una tabla con siete hallazgos, cada uno con su recomendación práctica, y la conclusión de los autores.

---

## Bloque 4 — Primer contacto con un LLM

**LLM** son las siglas en inglés de "modelo grande de lenguaje": los asistentes de texto de la familia 1 del Bloque 2 (ChatGPT, Gemini, Claude y otros). Lo que se encuentra al abrir uno es una caja de texto: se escribe lo que se necesita y responde. No hay menúes que aprender ni nada que instalar.

La idea central del bloque: **lo que se obtiene depende mucho de cómo se pide**. La misma consulta, formulada de dos maneras distintas, puede devolver algo genérico e inservible o algo casi listo para usar. Esa diferencia se ve mejor probando que leyendo; por eso el bloque termina en una actividad.

No hay forma de arruinar nada: no se rompe, no queda registro de los errores y se puede probar todas las veces que haga falta.

El texto que se usa como material de la actividad es un fragmento sobre semiótica social multimodal, de Flores Solano, C. (2021), *Introducción a la semiótica social multimodal y sus aplicaciones para el análisis de contextos escolares*, Revista Educación, 45(1), Universidad de Costa Rica. Es deliberadamente difícil.

---

## Bloque 5 — ¿Dónde estoy parado hoy?

Cierre del módulo. No es una evaluación ni un test: es un momento para pensar dónde está parado cada uno con todo esto, anclado en la propia asignatura. No hay respuesta correcta.

La idea para llevarse: **la herramienta propone, vos decidís**. El criterio pedagógico —qué enseñar, cómo y para qué— sigue siendo del docente.

Lo que se identifique en este bloque (el tema que se les traba a los estudiantes, el material que nunca se llegó a hacer) es el punto de partida de la producción de los módulos siguientes: conviene guardarlo a mano.

---

## Referencias del módulo

- Guo, P. J., Kim, J. y Rubin, R. (2014). *How video production affects student engagement: An empirical study of MOOC videos*. Proceedings of the First ACM Conference on Learning at Scale (L@S 2014). https://doi.org/10.1145/2556325.2566239
- Flores Solano, C. (2021). *Introducción a la semiótica social multimodal y sus aplicaciones para el análisis de contextos escolares*. Revista Educación, 45(1). Universidad de Costa Rica.
- Reporte del BID sobre inteligencia artificial (lectura optativa del Bloque 1).
