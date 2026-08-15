import streamlit as st
import os
from google import genai
from google.genai import types

# =============================================================
# CONFIGURACIÓN DEL CURSO — editá esto a medida que avanza
# =============================================================
# Subí este número cuando el grupo llega a un nuevo módulo.
# El bot cargará el contenido de 'general/' + todos los módulos
# desde 0 hasta MODULO_ACTIVO (inclusive). Los módulos superiores
# NO se cargan: no existen para el bot, así que no puede adelantarlos.
MODULO_ACTIVO = 0

# Nombre "lindo" de cada módulo (para mensajes del bot y la interfaz)
NOMBRES_MODULOS = {
    0: "Módulo 0 — Introducción a la IA Generativa",
    1: "Módulo 1 — Laboratorio de Producción Textual",
    2: "Módulo 2 — Laboratorio de Imagen y Audio",
    3: "Módulo 3 — Laboratorio de Video y Lipsync",
    4: "Módulo 4 — Laboratorio de Actividades, Evaluaciones y Bots",
}
# =============================================================

# Configuración estética de la página
st.set_page_config(page_title="Tutor IA — Curso de Posgrado", page_icon="🎓", layout="centered")

st.title("🎓 Tutor Virtual del Curso")
st.subheader("Introducción a la IA Generativa para Docentes Universitarios")
st.caption("Departamento de Ciencias Sociales — Universidad Nacional de Luján")
st.info(f"📚 Contenido disponible hasta: **{NOMBRES_MODULOS.get(MODULO_ACTIVO, 'Módulo ' + str(MODULO_ACTIVO))}**")

# 1. Validar que la API Key exista
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Falta la clave GEMINI_API_KEY en los Secrets de Streamlit.")
    st.stop()

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# 2. Cargar la base de conocimiento SEGÚN el módulo activo
#    Lee 'conocimiento/general/' siempre + 'conocimiento/modulo_N/' hasta MODULO_ACTIVO.
@st.cache_data
def cargar_base_conocimiento(modulo_activo):
    contexto = ""
    modulos_cargados = []

    # Carpetas a leer: general + los módulos habilitados
    carpetas = ["general"] + [f"modulo_{i}" for i in range(modulo_activo + 1)]

    for nombre_carpeta in carpetas:
        ruta_carpeta = os.path.join("conocimiento", nombre_carpeta)
        if os.path.exists(ruta_carpeta):
            archivos_md = [a for a in sorted(os.listdir(ruta_carpeta)) if a.endswith(".md")]
            if archivos_md:
                modulos_cargados.append(nombre_carpeta)
            for archivo in archivos_md:
                ruta = os.path.join(ruta_carpeta, archivo)
                with open(ruta, "r", encoding="utf-8") as f:
                    contexto += f"\n\n--- DOCUMENTO ({nombre_carpeta}): {archivo} ---\n\n" + f.read()

    return contexto, modulos_cargados

contexto_catedra, modulos_cargados = cargar_base_conocimiento(MODULO_ACTIVO)

if not contexto_catedra:
    st.warning("⚠️ No se encontró contenido en la carpeta 'conocimiento/'. Cargá al menos la carpeta 'general/'.")

# 3. Memoria de la conversación (historial en session_state)
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. System prompt: TUTOR de contenidos que sigue el ritmo de la cursada
nombre_modulo_actual = NOMBRES_MODULOS.get(MODULO_ACTIVO, f"Módulo {MODULO_ACTIVO}")

system_instruction = (
    "Sos el Tutor Virtual del curso-taller de posgrado 'Introducción a la IA Generativa para "
    "Docentes Universitarios' de la Universidad Nacional de Luján (UNLu), Departamento de Ciencias Sociales. "
    "Tu rol es acompañar el aprendizaje de docentes universitarios que en su mayoría tienen poca o ninguna "
    "experiencia previa con IA generativa.\n\n"

    "TONO Y ESTILO:\n"
    "- Usá el voseo rioplatense (español de Argentina) de forma natural, cálida y profesional.\n"
    "- Explicá con claridad, sin jerga innecesaria. Si usás un término técnico, aclaralo.\n"
    "- Sé breve y concreto: docentes con poco tiempo. Ofrecé ampliar si hace falta.\n\n"

    "QUÉ RESPONDÉS:\n"
    "- Respondés sobre los CONTENIDOS del curso (conceptos de IA generativa, prompts, herramientas, "
    "producción de materiales, etc.) y también sobre cuestiones de cursada (fechas, requisitos, certificación).\n"
    "- Basás tus respuestas EXCLUSIVAMENTE en la documentación de referencia provista más abajo. "
    "No inventes datos, herramientas, funciones ni procedimientos que no estén en esos materiales.\n\n"

    "ACOMPAÑÁS, NO RESOLVÉS:\n"
    "- Tu función es acompañar el proceso de aprendizaje, no hacer el trabajo por el participante. "
    "Orientás, das pistas, sugerís cómo encarar una actividad o cómo mejorar un prompt, pero NO entregás "
    "la actividad resuelta ni la respuesta que el participante tiene que elaborar.\n"
    "- Si te piden que resuelvas una actividad por ellos o que hagas la tarea, respondé con calidez que "
    "tu rol es acompañarlos para que la hagan ellos. Ofrecé una orientación o un primer paso, e invitá a "
    "consultar al equipo docente en el Foro de Consultas si necesitan más ayuda.\n\n"

    "REGLA DE RITMO (muy importante):\n"
    f"- El curso va actualmente en: {nombre_modulo_actual}.\n"
    "- Solo tenés cargado el contenido hasta el módulo actual. Si te preguntan por algo que claramente "
    "corresponde a un módulo posterior y no está en tu documentación, NO lo inventes ni lo adelantes. "
    "Respondé con calidez que ese tema se va a ver más adelante en el curso, e invitá a enfocarse en lo "
    "que se está trabajando ahora. Ejemplo de tono: 'Eso lo vamos a ver más adelante en el curso. "
    "Por ahora estamos trabajando con [tema del módulo actual], ¿te ayudo con eso?'.\n\n"

    "SI NO SABÉS:\n"
    "- Si la respuesta no está en los materiales y no es un tema de un módulo futuro, respondé: "
    "'No dispongo de esa información en los materiales del curso. Te sugiero consultarlo en el Foro de "
    "Consultas del aula o con el equipo docente.'\n\n"

    f"DOCUMENTACIÓN DE REFERENCIA:\n{contexto_catedra}"
)

# 5. Bucle de interacción, ahora CON memoria conversacional
if prompt := st.chat_input("Escribí tu consulta sobre el curso..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Reconstruir el historial en el formato que espera Gemini.
    # (Gemini usa 'user' y 'model'; mapeamos 'assistant' -> 'model'.)
    contents = []
    for m in st.session_state.messages:
        rol = "user" if m["role"] == "user" else "model"
        contents.append(types.Content(role=rol, parts=[types.Part(text=m["content"])]))

    with st.chat_message("assistant"):
        with st.spinner("Consultando los materiales del curso..."):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=contents,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=0.2,
                    ),
                )
                respuesta_bot = response.text
                st.markdown(respuesta_bot)
                st.session_state.messages.append({"role": "assistant", "content": respuesta_bot})
            except Exception as e:
                st.error(f"Error de conexión con el modelo: {e}")
