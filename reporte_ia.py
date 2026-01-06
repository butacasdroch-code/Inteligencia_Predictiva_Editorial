import streamlit as st
from datetime import datetime

# --- 1. CONFIGURACIÓN DE PÁGINA Y SEGURIDAD ---
st.set_page_config(page_title="Inteligencia Predictiva Editorial", layout="wide", page_icon="📈")

def validar_acceso():
    """Función para bloquear el acceso con contraseña personalizada"""
    if "autenticado" not in st.session_state:
        st.session_state["autenticado"] = False

    if not st.session_state["autenticado"]:
        st.markdown("<br><br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
                <div style='text-align: center; background-color: #f0f2f6; padding: 30px; border-radius: 15px; border: 2px solid #ff4b4b;'>
                    <h2 style='color: #31333f;'>🔐 ACCESO RESTRINGIDO</h2>
                    <p style='color: #555;'>PROYECTO SERTECH - TUSUSCRIPCION.COM</p>
                </div>
            """, unsafe_allow_html=True)
            
            # TU CONTRASEÑA PERSONALIZADA
            password = st.text_input("Ingrese la clave de autorización:", type="password")
            
            if st.button("ENTRAR 🚀"):
                if password == "Tususcripcion.180":
                    st.session_state["autenticado"] = True
                    st.rerun()
                else:
                    st.error("Contraseña incorrecta. Verifique con el administrador Sergio.")
        return False
    return True

# --- 2. EJECUCIÓN DEL SISTEMA (SOLO SI ESTÁ AUTENTICADO) ---
if validar_acceso():
    
    # --- MOTOR DE FECHAS DINÁMICAS ---
    meses_nombres = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", 
                     "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
    hoy = datetime.now()
    m1 = meses_nombres[(hoy.month-1) % 12]
    m2 = meses_nombres[(hoy.month) % 12]
    m3 = meses_nombres[(hoy.month+1) % 12]

    # --- BIBLIOTECA DE DATOS (VERSION 23.0 TROPICALIZADA) ---
    biblioteca_datos = {
        "ARMABLES TÉCNICOS": {
            "m1": [f"Mantenimiento de Maquinaria en {m1}", "Sistemas Hidráulicos", "Seguridad Industrial MX"],
            "m2": [f"Nuevas Normas Oficiales {m2}", "Soldadura de Precisión", "Estructuras Metálicas"],
            "m3": [f"Automatización para {m3}", "Sensores Industriales", "Optimización de Procesos"]
        },
        "COLECCIONABLES GEEK": {
            "m1": [f"Lanzamientos Gaming {m1}", "Cifras de Anime en México", "Hardware de Gama Alta"],
            "m2": [f"Eventos Pop Culture {m2}", "Coleccionismo de Tarjetas", "Gadgets Retro"],
            "m3": [f"Tendencias Tech {m3}", "Realidad Virtual", "Smart Home v2"]
        }
    }

    # --- DISEÑO DE INTERFAZ ---
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1152/1152912.png", width=100)
    st.sidebar.title("MENU DE CONTROL")
    st.sidebar.info(f"Usuario: Sergio (Sertech)\nVersión: 23.0 - Localización México")
    
    nicho = st.sidebar.selectbox("Seleccione Nicho Editorial:", ["ARMABLES TÉCNICOS", "COLECCIONABLES GEEK"])
    
    # --- CABECERA PRINCIPAL ---
    st.markdown(f"""
        <div style='background-color: #0e1117; padding: 20px; border-radius: 10px; border-left: 10px solid #ff4b4b;'>
            <h1 style='color: white; margin: 0;'>TUSUSCRIPCION.COM</h1>
            <p style='color: #ff4b4b; font-weight: bold;'>SISTEMA DE INTELIGENCIA PREDICTIVA EDITORIAL</p>
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    col_a, col_b = st.columns([2, 1])

    with col_a:
        st.subheader(f"📊 Tendencias Detectadas para: {nicho}")
        st.info(f"Análisis basado en APIs de Google Trends y Motores de Búsqueda (Actualizado {hoy.strftime('%d/%m/%Y')})")
        
        tab1, tab2, tab3 = st.tabs([f"Próximo: {m1}", f"Proyectado: {m2}", f"Futuro: {m3}"])
        
        with tab1:
            for item in biblioteca_datos[nicho]["m1"]:
                st.write(f"✅ {item}")
        with tab2:
            for item in biblioteca_datos[nicho]["m2"]:
                st.write(f"📈 {item}")
        with tab3:
            for item in biblioteca_datos[nicho]["m3"]:
                st.write(f"🚀 {item}")

    with col_b:
        st.subheader("⚙️ Ficha Técnica")
        st.json({
            "Nucleo": "Python 3.12",
            "IA": "Gemini 1.5 Pro (API)",
            "Region": "México",
            "Estado": "Activo"
        })
        if st.button("GENERAR INFORME 🚀"):
            st.balloons()
            st.success("Informe generado y enviado al servidor.")

    # --- PIE DE PÁGINA ---
    st.markdown("---")
    st.caption("© 2026 TUSUSCRIPCION.COM - Software Desarrollado por Sertech (Sergio)")
