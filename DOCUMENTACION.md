# Documentación — Tutor Virtual del Curso

Guía de funcionamiento y mantenimiento del chatbot tutor del Curso-Taller de Posgrado
"Introducción a la IA Generativa para Docentes Universitarios" (UNLu, DCS).

Está pensada en dos capas: primero una **parte operativa** (cómo funciona y cómo
actualizarlo, sin necesidad de ser programador) y al final un **anexo técnico** para
quien tenga que meter mano en el código.

---

# PARTE 1 — Operativa

## 1. Qué es, en una frase

Es un asistente de chat que responde a los cursantes sobre el curso, basándose
**únicamente** en unos archivos de texto que nosotros controlamos (la "base de
conocimiento"). No inventa: si algo no está en esos archivos, avisa que no lo tiene y
deriva al equipo. Está embebido dentro del aula de Moodle.

## 2. Las piezas que lo componen

- **`app.py`** — el motor del bot (el programa en sí).
- **`conocimiento/`** — la carpeta con los textos que el bot "sabe". Es lo que más vas
  a tocar.
- **Gemini** (modelo de Google) — el "cerebro" que redacta las respuestas. Se conecta
  con una clave (API key).
- **Streamlit Community Cloud** — el servicio gratuito donde vive el bot online.
- **GitHub** — la copia en la nube del proyecto. Streamlit lee de ahí para publicar.

El circuito completo: editás archivos en tu computadora → los subís a GitHub (commit +
push) → Streamlit detecta el cambio y republica el bot → el bot se ve dentro de Moodle.

## 3. La base de conocimiento (`conocimiento/`)

Es una carpeta con subcarpetas:

```
conocimiento/
├── general/      → se carga SIEMPRE (info del curso, fechas, aula, FAQ, equipo…)
├── modulo_0/     → se carga cuando el curso llegó al Módulo 0 o más
├── modulo_1/     → se carga cuando el curso llegó al Módulo 1 o más
├── modulo_2/
├── modulo_3/
└── modulo_4/
```

**Cuatro reglas de oro para no romper nada:**

1. **El bot lee solo archivos `.md`** (texto en formato Markdown). Un PDF, un Word o una
   imagen dentro de estas carpetas los ignora. Si tenés material en otro formato, hay
   que pasarlo a texto `.md`.
2. **El bot lee TODOS los `.md` de cada carpeta que carga.** Todo lo que pongas ahí
   entra en la "cabeza" del bot. Por eso **no** metas archivos sueltos tipo plantillas,
   borradores o notas internas dentro de `general/` o `modulo_N/`: se los tomaría como
   contenido del curso.
3. **Nada de soluciones.** En las consignas de actividades va la *consigna*, nunca la
   *respuesta resuelta*. El bot acompaña, no resuelve (ver punto 6).
4. **Respetá el ritmo.** No pongas material de un módulo futuro en una carpeta que ya
   está activa. El bot solo debe conocer hasta donde va el curso.

## 4. `MODULO_ACTIVO` — el control del ritmo

Dentro de `app.py`, casi arriba de todo, hay una línea:

```python
MODULO_ACTIVO = 0
```

Ese número decide hasta qué módulo "ve" el bot. Con `0`, carga `general/` + `modulo_0/`.
Con `2`, carga `general/` + `modulo_0/` + `modulo_1/` + `modulo_2/`. Los módulos
superiores no existen para el bot, así que no puede adelantar temas.

**Cuando el curso avanza a un nuevo módulo, subís ese número.**

## 5. Cómo actualizar el bot (paso a paso)

### 5.a — Para corregir o agregar contenido
1. Editá o creá los archivos `.md` dentro de `conocimiento/` (con cualquier editor de
   texto; o pedímelo y lo hago yo).
2. Publicá los cambios (ver 5.c).

### 5.b — Para abrir un módulo nuevo (rutina completa)
1. Creá/completá los `.md` del módulo dentro de `conocimiento/modulo_N/` (podés partir
   del archivo `_PLANTILLA_modulo.md` que está en la carpeta borrador
   `conocimiento_actualizado/`).
2. Borrá el `_LEEME.md` de esa carpeta (era solo un recordatorio).
3. En `app.py`, subí `MODULO_ACTIVO` al número del módulo que abrís.
4. Publicá los cambios (ver 5.c) y forzá el refresco (ver 5.d).

### 5.c — Publicar los cambios (GitHub Desktop)
1. Abrí **GitHub Desktop**. Te muestra los archivos cambiados.
2. **Destildá** cualquier archivo de la carpeta `__pycache__` si aparece (es basura
   técnica, no va).
3. Escribí un resumen en "Summary" y apretá **"Commit to main"**.
4. Apretá **"Push origin"** (o "Publish branch" la primera vez).
5. En un par de minutos Streamlit republica solo.

### 5.d — Si no ves los cambios: la trampa de la caché
El bot guarda en memoria la base de conocimiento para responder más rápido. A veces,
después de publicar, sigue mostrando la versión vieja. Para forzar la actualización:

- Entrá a **share.streamlit.io**, buscá la app y elegí **"Reboot app"** (menú **⋮**).
- Esperá 1–2 minutos y hacé **Ctrl + F5** en el navegador.
- Alternativa rápida: dentro del bot, menú **⋮ → "Clear cache"** y luego **"Rerun"**.

Si tras un reboot limpio sigue sin verse el cambio, ahí sí hay que investigar.

## 6. La personalidad del bot (el "prompt")

Cómo se comporta el bot (su tono, qué responde y qué no) está definido en `app.py`, en
un texto largo llamado `system_instruction`. Hoy incluye: usar voseo cálido; responder
solo desde los materiales; **acompañar sin resolver** las actividades; respetar el ritmo
del curso; y, si no sabe, derivar al Foro de Consultas. Si querés cambiarle el tono o
alguna regla, se edita ahí (mejor pedímelo y lo ajustamos juntos).

## 7. La clave de Gemini (API key)

El bot necesita una clave para hablar con Gemini. Esa clave **no está en el código ni en
GitHub** (por seguridad): vive en los *Secrets* de Streamlit Cloud, bajo el nombre
`GEMINI_API_KEY`. Si alguna vez hay que cambiarla, se hace desde el panel de la app en
Streamlit (Settings → Secrets), no tocando el código.

## 8. Cómo está embebido en Moodle

El bot se publica en una URL de Streamlit (`tutor-curso-ia-sociales.streamlit.app`) y se
muestra dentro del aula mediante un `<iframe>` en la sección **Tutor Virtual**. Si algún
día cambia la URL del bot, hay que actualizar ese `<iframe>` en Moodle.

## 9. Checklist rápido de mantenimiento

- [ ] ¿El material nuevo está en `.md`?
- [ ] ¿Está en la carpeta correcta (`general/` o el `modulo_N/` que toca)?
- [ ] ¿No metí plantillas/borradores ni soluciones dentro de esas carpetas?
- [ ] Si abrí un módulo, ¿subí `MODULO_ACTIVO`?
- [ ] ¿Hice commit + push en GitHub Desktop (sin el `__pycache__`)?
- [ ] ¿Rebooteé la app y refresqué con Ctrl+F5 para ver el cambio?

---

# PARTE 2 — Anexo técnico

## Stack y dependencias

- **Lenguaje:** Python.
- **Framework de interfaz:** Streamlit.
- **Modelo:** Google Gemini `gemini-2.5-flash`, vía el SDK `google-genai`.
- **Hosting:** Streamlit Community Cloud (deploy automático desde la rama `main` del repo
  de GitHub `selajp-jps/TUTOR_CURSO_INTRO_IA_2026`).
- **`requirements.txt`:**
  ```
  streamlit
  google-genai
  ```

## Arquitectura: RAG "ingenuo"

Es una implementación de RAG (Retrieval-Augmented Generation) deliberadamente simple:
**no** usa embeddings ni base vectorial. En su lugar, concatena el texto completo de los
`.md` habilitados y lo inyecta entero en el `system_instruction` de cada consulta. Es
robusto y sin infraestructura, a costa de que **todo el corpus viaja en cada llamada**
(ver "Consideraciones de escala").

## Recorrido de `app.py` por bloques

1. **Configuración del curso (líneas ~6–23):** `MODULO_ACTIVO` y el diccionario
   `NOMBRES_MODULOS`. Es la única zona pensada para editar de forma rutinaria.
2. **UI base (25–31):** `st.set_page_config`, título, subtítulo y un `st.info` que
   muestra hasta qué módulo hay contenido.
3. **API key (33–38):** valida que exista `st.secrets["GEMINI_API_KEY"]` y crea el
   `genai.Client`. Usa `st.secrets` (propio de Streamlit Cloud); **no** usar
   `os.environ` acá.
4. **Carga de conocimiento (40–66):** `cargar_base_conocimiento(modulo_activo)`,
   decorada con `@st.cache_data`. Arma la lista de carpetas `["general", "modulo_0", …,
   f"modulo_{MODULO_ACTIVO}"]`, lee los `.md` ordenados alfabéticamente de cada una y los
   concatena con un encabezado `--- DOCUMENTO (carpeta): archivo ---` por archivo.
   Devuelve `(contexto, modulos_cargados)`.
5. **Memoria de conversación (68–74):** historial en `st.session_state.messages` (lista
   de dicts `{"role", "content"}`), re-renderizado en cada rerun.
6. **`system_instruction` (76–118):** el prompt de sistema. Bloques: rol, tono/estilo,
   qué responde, **acompañás-no-resolvés**, regla de ritmo (interpola
   `nombre_modulo_actual`), qué hacer si no sabe, y al final `DOCUMENTACIÓN DE
   REFERENCIA` con todo el `contexto_catedra`.
7. **Loop de chat (120–148):** `st.chat_input`; mapea el historial al formato de Gemini
   (`assistant` → `model`) construyendo `types.Content`/`types.Part`; llama a
   `client.models.generate_content` con `model="gemini-2.5-flash"`,
   `temperature=0.2` y el `system_instruction`; muestra y guarda la respuesta. Errores
   capturados con `try/except` y mostrados con `st.error`.

## `@st.cache_data`: por qué a veces no se ven los cambios

`cargar_base_conocimiento` está cacheada por sus argumentos (`MODULO_ACTIVO`). En un
reinicio completo del contenedor la caché se limpia y se releen los `.md`. Pero si
Streamlit reutiliza la instancia, puede servir el corpus viejo aunque el repo ya tenga
los `.md` nuevos. Solución operativa: **Reboot app** y/o **Clear cache** (ver 5.d).

## Parámetros del modelo

- `model="gemini-2.5-flash"` — rápido y económico, adecuado para Q&A sobre contexto.
- `temperature=0.2` — respuestas conservadoras y consistentes (poca "creatividad"),
  coherente con un tutor que no debe inventar.

## Consideraciones de escala y notas

- **Tamaño del contexto / costo:** como todo el corpus entra en cada consulta, a medida
  que se llenen los módulos el prompt crecerá. Con textos curados no debería ser
  problema, pero conviene evitar volcados crudos (transcripciones enteras, PDFs largos).
  Si algún día el volumen se dispara, el siguiente paso natural sería trocear el corpus
  e incorporar embeddings/recuperación selectiva.
- **`__pycache__/`:** Python genera esta carpeta al ejecutar. No debe subirse al repo;
  conviene agregar un `.gitignore` con `__pycache__/` y `*.pyc` para que deje de
  aparecer en GitHub Desktop.
- **Versiones sin fijar:** `requirements.txt` no fija versiones. Si en el futuro una
  actualización de Streamlit o del SDK rompiera algo, fijar versiones (`streamlit==x.y.z`)
  daría reproducibilidad.

---

*Última actualización de esta documentación: julio 2026. Mantener al día cuando cambien
el modelo, la estructura de `conocimiento/`, el hosting o el prompt.*
