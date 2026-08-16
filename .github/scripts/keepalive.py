"""
Visitante robot para mantener despierta la app de Streamlit Community Cloud.

Abre la app con un navegador real (Chromium headless), y si la encuentra
dormida, hace clic en el botón de "despertar". Luego espera unos segundos
para que la sesión quede registrada y se reinicie el contador de inactividad.

Se ejecuta automáticamente desde GitHub Actions (ver .github/workflows/keepalive.yml).
"""

from playwright.sync_api import sync_playwright

# URL pública de la app. Si algún día cambia, actualizá esta línea.
URL = "https://tutor-curso-ia-sociales.streamlit.app/"


def main():
    with sync_playwright() as p:
        navegador = p.chromium.launch()
        pagina = navegador.new_page()
        print(f"Visitando {URL} ...")
        pagina.goto(URL, timeout=60000)

        # Si la app está dormida, aparece un botón para reactivarla.
        # Intentamos hacer clic; si no está (la app ya estaba despierta), seguimos.
        try:
            pagina.get_by_text("Yes, get this app back up").click(timeout=15000)
            print("La app estaba dormida: se hizo clic para despertarla.")
        except Exception:
            print("La app ya estaba despierta (no hizo falta despertarla).")

        # Esperar a que la app cargue de verdad y registre la sesión.
        pagina.wait_for_timeout(45000)  # 45 segundos
        print("Visita completada.")
        navegador.close()


if __name__ == "__main__":
    main()
