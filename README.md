# TUTOR_CURSO_INTRO_IA_2026

### Asistente Virtual del Módulo 0 (Introducción y Gestión de la Cursada)
**Curso-Taller de Posgrado:** *"Inteligencia Artificial en la Educación Superior: Herramientas básicas para la enseñanza de las Ciencias Sociales"*
**Institución:** Universidad Nacional de Luján (UNLu) - Departamento de Ciencias Sociales

---

## 📝 Descripción del Proyecto
Este repositorio contiene el código fuente de un chatbot tutor automatizado diseñado para acompañar a los docentes cursantes durante el Módulo 0 (Onboarding) del posgrado. 

El sistema utiliza una arquitectura **RAG (Generación Aumentada por Recuperación)** simple y local. El "motor" de la aplicación está desarrollado con **Streamlit**, y las respuestas son procesadas por el modelo **Gemini 2.5 Flash** de Google. 

El bot está blindado pedagógicamente: sus respuestas se basan exclusivamente en la documentación oficial de la cátedra (programas, cronogramas y guías cargadas en formato Markdown), evitando alucinaciones y garantizando el rigor institucional.

## 📂 Estructura del Repositorio
* `app.py`: Archivo principal de la aplicación web en Streamlit.
* `requirements.txt`: Dependencias y librerías de Python necesarias para el servidor.
* `conocimiento/`: Carpeta contenedora de la base de conocimiento de la cátedra (archivos `.md`).

## 🚀 Ejecución en Entorno Local
Para probar y ejecutar esta aplicación en tu computadora, seguí estos pasos:

1. Clonar el repositorio o descargar los archivos.
2. Asegurarte de tener instalado Python.
3. Instalar las dependencias ejecutando en la terminal:
   ```bash
   pip install -r requirements.txt
