import streamlit as st
import os
from google import genai
from google.genai import types

# Configuración estética de la página web
st.set_page_config(page_title="Tutor IA - Módulo 0", page_icon="🤖", layout="centered")

st.title("🤖 Tutor Virtual de Cátedra")
st.subheader("Módulo 0: Introducción y Gestión de la Cursada")
st.caption("Departamento de Ciencias Sociales - Universidad Nacional de Luján")

# 1. Validar de forma segura que la API Key exista
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Falta la clave GEMINI_API_KEY en tu archivo .streamlit/secrets.toml")
    st.stop()

# Inicializar el cliente oficial de Gemini
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# 2. Función para leer de forma automática todos los archivos .md de la carpeta conocimiento
@st.cache_data
def cargar_base_conocimiento():
    contexto_completo = ""
    carpeta = "conocimiento"
    if os.path.exists(carpeta):
        for archivo in os.listdir(carpeta):
            if archivo.endswith(".md"):
                ruta_completa = os.path.join(carpeta, archivo)
                with open(ruta_completa, "r", encoding="utf-8") as f:
                    contexto_completo += f"\n\n--- DOCUMENTO DE REFERENCIA: {archivo} ---\n\n" + f.read()
    return contexto_completo

contexto_catedra = cargar_base_conocimiento()

if not contexto_catedra:
    st.warning("⚠️ No se encontraron archivos Markdown (.md) en la carpeta '/conocimiento'. Por favor, cargá el programa de la materia.")

# 3. Estructurar el Historial de Chat (Session State) para que tenga memoria
if "messages" not in st.session_state:
    st.session_state.messages = []

# Renderizar los mensajes que ya ocurrieron en la pantalla
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Instrucción estricta del sistema (System Prompt) inyectando el contexto de tus textos
system_instruction = (
    "Sos el Asistente Virtual del Módulo 0 del curso de posgrado 'Inteligencia Artificial en la Educación Superior: "
    "Herramientas básicas para la enseñanza de las Ciencias Sociales' de la UNLu. "
    "Respondé de forma empática, utilizando el voseo rioplatense (español de Argentina) de manera natural pero sumamente profesional. "
    "Tu objetivo es guiar a los docentes alumnos basándote EXCLUSIVAMENTE en el contexto institucional provisto abajo.\n\n"
    "REGLA DE ORO: Si la respuesta a la pregunta del usuario no se encuentra explicitada, sugerida o respaldada en los documentos de referencia, "
    "no inventes información bajo ningún concepto. Respondé textualmente: 'No dispongo de esa información específica en los registros del Módulo 0. "
    "Te sugiero consultarlo en el Foro de Avisos de Moodle o directamente con el Profesor Responsable del curso, Lic. Jorge Pablo Sela, o el equipo docente.'\n\n"
    f"DOCUMENTACIÓN OFICIAL DE CÁTEDRA PARA CONSULTAR:\n{contexto_catedra}"
)

# 4. El búcle de interacción del Chat
if prompt := st.chat_input("¿Qué duda tenés sobre el Módulo 0 o el programa?"):
    # Mostrar la pregunta del docente en la pantalla
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Solicitar la respuesta blindada a Gemini
    with st.chat_message("assistant"):
        with st.spinner("Consultando el programa de la cátedra..."):
            try:
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=0.2, # Temperatura baja para evitar creatividad/alucinación
                    )
                )
                respuesta_bot = response.text
                st.markdown(respuesta_bot)
                # Guardar la respuesta en el historial
                st.session_state.messages.append({"role": "assistant", "content": respuesta_bot})
            except Exception as e:
                st.error(f"Error de conexión con el modelo: {e}")