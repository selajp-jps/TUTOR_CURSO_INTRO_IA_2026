# Registro de cambios — Tutor Virtual del Curso

Anotar acá cada actualización de la base de conocimiento o del código, con fecha y motivo.
Sirve para saber, dentro de unos meses, por qué un archivo dice lo que dice.

---

## 08/09/2026 — Puesta al día de la base de conocimiento (Módulos 0, 1 y 2)

**Situación de partida.** El taller ya había dictado los Módulos 1 y 2, pero
`conocimiento/` solo tenía la carpeta `general/`: las cinco carpetas de módulo estaban
vacías, con su `_LEEME.md` de recordatorio. `MODULO_ACTIVO` estaba en `0` y, como
`modulo_0/` también estaba vacía, el bot respondía **únicamente** con la información
general del curso, sin nada de contenido de los módulos.

**Fuente de todo el contenido nuevo:** el aula Moodle del curso (id 3540), leída
directamente el 08/09/2026. Secciones consultadas: Info Esencial, Módulo 0, Módulo 1,
Módulo 2 y Baúl de Recursos.

### Archivos nuevos

Se creó la misma tríada en las tres carpetas de módulo:

- `conocimiento/modulo_0/01_contenidos.md`, `02_actividades.md`, `03_herramientas_y_faq.md`
- `conocimiento/modulo_1/01_contenidos.md`, `02_actividades.md`, `03_herramientas_y_faq.md`
- `conocimiento/modulo_2/01_contenidos.md`, `02_actividades.md`, `03_herramientas_y_faq.md`

Se borraron los `_LEEME.md` de `modulo_0/`, `modulo_1/` y `modulo_2/`. Los de `modulo_3/`
y `modulo_4/` siguen ahí, porque esas carpetas todavía están vacías.

### Cambios en `conocimiento/general/`

- **`02_cronograma_fechas.md`** — Se agregó una columna de estado a la tabla de
  encuentros; se documentó que el **Encuentro Sincrónico 2 (02/09/2026) no se realizó**
  por adhesión al paro docente del frente sindical universitario, que se reemplazó por un
  video de apertura y que no hubo corrimiento de fechas. Se agregó la tabla completa de
  fechas de entrega de las siete actividades obligatorias y la aclaración de la prórroga
  de la Actividad 2.
- **`04_evaluacion_certificacion.md`** — Se explicitó que el **75% de asistencia se
  calcula sobre cuatro encuentros**, no sobre cinco, por el encuentro no realizado. Se
  agregó qué actividades cuentan para el 75% de actividades asincrónicas, con sus fechas.
- **`06_faq_tecnica.md`** — Dos preguntas nuevas: los plazos de entrega por módulo y por
  qué no hubo Encuentro Sincrónico 2. Una tercera sobre qué contiene hoy el Baúl de
  Recursos.
- **`07_como_funciona_el_aula.md`** — Se corrigió la descripción de las secciones: los
  módulos son 0 a 4 y el Cierre no es una sección del menú sino una etapa del cronograma.
  Se detalló el contenido real del Baúl de Recursos.

**No se tocó** `01_programa_general.md`, `03_modulos_contenidos.md` ni
`05_equipo_organizacion.md`: siguen siendo correctos.

### Cambios en el código y la documentación

- **`app.py`** — `MODULO_ACTIVO` pasó de `0` a `2`. Ningún otro cambio: el bot ahora carga
  `general/` + `modulo_0/` + `modulo_1/` + `modulo_2/`.
- **`PLANTILLA_modulo.md`** (nuevo, en la raíz) — La plantilla real de los tres archivos
  por módulo, con la rutina para abrir un módulo nuevo y el checklist previo a publicar.
  La `DOCUMENTACION.md` remitía a un archivo `_PLANTILLA_modulo.md` dentro de una carpeta
  `conocimiento_actualizado/` que **nunca existió** en el repositorio.
- **`DOCUMENTACION.md`** — Se corrigió esa referencia al archivo inexistente y se agregó
  la estructura de tres archivos por módulo.
- **`CHANGELOG.md`** (nuevo) — Este archivo.

### Decisiones tomadas y por qué

- **Se redactó también el Módulo 0**, aunque sea optativo: estaba dictado y el bot no
  tenía nada de él.
- **Info Esencial no se modificó en el aula.** Su tabla de encuentros sigue mostrando el
  Encuentro 2 del 02/09 como estaba: esa sección cumplió su función al inicio del curso y
  se decidió no ajustarla con los cambios posteriores. La corrección vive en el banco de
  conocimiento, no en el aula.
- **El Baúl de Recursos se documentó por lo que efectivamente contiene hoy.** Varios
  bloques del Módulo 2 remiten al Baúl para materiales que todavía no están cargados
  (guía de iluminación avanzada, guía de edición en Google Flow, lista ampliada de
  herramientas de imagen, versión larga de dirección de escena para AI Studio). El banco
  de conocimiento **no** los menciona, para que el bot no prometa lo que no está.
- **Ningún passcode quedó escrito** en los archivos. El del Generador de Casos se nombra
  como algo que el equipo docente comparte por separado.

### Pendientes que quedaron fuera de este cambio

- Cargar en el aula las **fechas de entrega de las Actividades 5, 6 y 7**, que figuran
  como `[ COMPLETAR FECHA ]` a la vista de los cursantes. (Pablo lo ajusta manualmente.)
- Actualizar en el aula la fecha de la **Actividad 2**, que sigue mostrando el 31/08.
- Subir al Baúl de Recursos los materiales que el Módulo 2 promete.

---

## Cómo anotar el próximo cambio

Copiar el encabezado con la fecha nueva y responder tres cosas: **qué se cambió**, **de
dónde salió la información** y **qué decisiones se tomaron**. Lo tercero es lo que más
sirve dentro de seis meses.
