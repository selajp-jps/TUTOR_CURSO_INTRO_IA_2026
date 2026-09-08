# Plantilla para cargar un módulo en la base de conocimiento

Este archivo **no lo lee el bot**: está en la raíz del repositorio, fuera de `conocimiento/`.
No lo muevas adentro de `conocimiento/general/` ni de ningún `conocimiento/modulo_N/`,
porque ahí el bot lo tomaría como contenido del curso.

Cada carpeta `conocimiento/modulo_N/` lleva **tres archivos**, siempre los mismos:

```
conocimiento/modulo_N/
├── 01_contenidos.md
├── 02_actividades.md
└── 03_herramientas_y_faq.md
```

Se llaman igual en todos los módulos a propósito: así, cuando dentro de seis meses haya
que actualizar algo, se sabe de antemano en qué archivo está.

---

## 01_contenidos.md — qué enseña el módulo

Es el archivo más largo. Contiene lo conceptual: es lo que le permite al bot conversar
sobre el tema, no solo sobre la cursada.

Estructura:

1. **Encabezado del módulo.** Cómo y cuándo se abrió (encuentro sincrónico, fecha), cuál
   es el sentido del módulo, cuántos bloques tiene y cuáles llevan actividad.
2. **Un apartado por bloque**, con el título real que tiene en el aula. Adentro:
   - la idea central del bloque, en prosa;
   - los autores y conceptos que se citan, con lo que efectivamente dicen;
   - los datos concretos que el bot va a necesitar (límites de herramientas, cifras,
     reglas de calidad);
   - las lecturas del bloque, indicando si son **obligatorias u optativas**.
3. **Referencias del módulo**, al final, en una lista.

## 02_actividades.md — qué tiene que entregar el cursante

Es el archivo que más consultas va a resolver. Estructura:

1. **Encabezado:** cuántas actividades obligatorias tiene el módulo, con qué números, y
   **la fecha de entrega, bien visible**.
2. **Un apartado por actividad**, con su número y su título tal como figura en el aula:
   - en qué bloque está y dónde se entrega (foro, Padlet, tarea);
   - los pasos de la consigna;
   - el apartado "En concreto": qué campos hay que completar y qué se adjunta;
   - los criterios de calidad que el aula explicita.
3. **Nota para el tutor**, al final: recordarle que acompaña y no resuelve.

**Regla que no se negocia:** acá va la *consigna*, nunca la *respuesta resuelta*. Si el
archivo contiene un ejemplo terminado de lo que el cursante tiene que producir, el bot se
lo va a entregar.

**Si una fecha cambia:** dejar registrada la fecha anterior y aclarar que se prorrogó. Los
cursantes ven fechas viejas en materiales descargados y preguntan.

## 03_herramientas_y_faq.md — con qué se trabaja y qué preguntan

1. **Herramientas del módulo.** Para cada una: para qué se usa, si pide cuenta, qué da
   gratis y cuál es su límite. Si hay una herramienta propia del taller, aclarar si pide
   passcode y que el passcode se comparte por separado (nunca escribirlo acá).
2. **Preguntas frecuentes**, en formato pregunta / respuesta corta. Sirven: los plazos, lo
   que se rompe seguido, los límites gratuitos, los formatos de archivo pedidos, y todo lo
   que ya haya aparecido en el Foro de Consultas.

---

## Rutina para abrir un módulo nuevo

1. Escribir los tres archivos en `conocimiento/modulo_N/`.
2. Borrar el `_LEEME.md` de esa carpeta.
3. Revisar si `conocimiento/general/` necesita actualizarse: cronograma, fechas de
   entrega, criterios de aprobación, canales de consulta.
4. Subir `MODULO_ACTIVO` en `app.py` al número del módulo que se abre.
5. Anotar el cambio en `CHANGELOG.md`.
6. Commit + push, y después reiniciar la app en Streamlit (ver `DOCUMENTACION.md`, 5.c y 5.d).

## Antes de publicar, chequear

- [ ] ¿Todos los archivos son `.md`?
- [ ] ¿No hay ninguna actividad resuelta?
- [ ] ¿No hay contenido de un módulo que todavía no se dictó?
- [ ] ¿Las fechas coinciden con las que ven los cursantes en el aula?
- [ ] ¿No quedó ningún passcode, contraseña ni clave escrito en un archivo?
- [ ] ¿El banco de conocimiento no promete materiales que todavía no están cargados en el aula?
