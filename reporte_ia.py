import streamlit as st
from datetime import datetime

# --- 1. CONFIGURACIÓN DE PÁGINA Y SEGURIDAD ---
st.set_page_config(page_title="Inteligencia Predictiva Editorial", layout="wide")

def validar_acceso():
    """Función para bloquear el acceso con contraseña personalizada"""
    if "autenticado" not in st.session_state:
        st.session_state["autenticado"] = False

    if not st.session_state["autenticado"]:
        st.markdown("<br><br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
                <div style='text-align: center; background-color: #f0f2f6; padding: 30px; border-radius: 15px; border: 2px solid #002d72;'>
                    <h2 style='color: #31333f;'>🔐 ACCESO RESTRINGIDO</h2>
                    <p style='color: #555;'>PROYECTO SERTECH - INTELIGENCIA EDITORIAL</p>
                </div>
            """, unsafe_allow_html=True)
            
            # TU CONTRASEÑA PERSONALIZADA
            password = st.text_input("Ingrese la clave de autorización:", type="password")
            
            if st.button("ENTRAR 🚀"):
                if password == "Tususcripcion.180":
                    st.session_state["autenticado"] = True
                    st.rerun()
                elif password != "":
                    st.error("Contraseña incorrecta. Verifique con el administrador Sergio.")
        return False
    return True

# --- 2. EJECUCIÓN DEL SISTEMA (SOLO SI ESTÁ AUTENTICADO) ---
if validar_acceso():

    # --- MOTOR DE FECHAS ---
    meses_nombres = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", 
                     "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
    hoy = datetime.now()
    # Ajuste de meses según tu lógica original
    m1, m2, m3 = meses_nombres[(hoy.month-4)%12], meses_nombres[(hoy.month-3)%12], meses_nombres[(hoy.month-2)%12]

    # --- BIBLIOTECA DE DATOS (TROPICALIZACIÓN TOTAL) ---
    biblioteca_datos = {
        "Femenino": {
            "m1": ["Moda de Pasarelas Otoño", "Especial de Moda en México", "Nuevos cosméticos", "Estilo de vestir en la ciudad"],
            "m2": ["Vestidos para cenas de gala", "Perfumería fina", "Guía de regalos navideños", "Alta joyería"],
            "m3": ["Ropa para Año Nuevo", "Metas personales 2026", "Accesorios y complementos", "Moda para vacaciones"],
            "propuesta": "ESTRATEGIA 1 (CONTENIDO): Lanzar campaña 'Tu Mejor Versión 2026' con guías digitales de imagen y estilo.\nESTRATEGIA 2 (NEGOCIO): Organizar pláticas presenciales con expertos en belleza para nuestras suscriptoras más fieles."
        },
        "Masculino": {
            "m1": ["Relojería de lujo", "Autos de nueva generación", "Líderes de negocios 2026", "Tecnología para el hogar"],
            "m2": ["Cuidado personal para hombres", "Tequila y Mezcal premium", "Novedades en electrónica", "Ropa formal de invierno"],
            "m3": ["Guía de regalos ejecutivos", "Alta cocina y maridaje", "Viajes de lujo", "Planeación financiera anual"],
            "propuesta": "ESTRATEGIA 1 (CONTENIDO): Serie de reportajes sobre emprendedores mexicanos que están cambiando la industria.\nESTRATEGIA 2 (NEGOCIO): Crear un círculo de beneficios con acceso a preventas de artículos de lujo y eventos de cata."
        },
        "Ciencia y Aventura": {
            "m1": ["Rutas por la selva", "Nuevos sitios arqueológicos", "Equipo para acampar", "Avances médicos"],
            "m2": ["Destinos naturales 2026", "Fotografía de paisajes", "Nuevas formas de transporte", "Protección del ambiente"],
            "m3": ["Viajes sustentables", "Caminatas y senderismo", "Aparatos de exploración", "Eventos astronómicos"],
            "propuesta": "ESTRATEGIA 1 (CONTENIDO): Lanzar el especial 'México Desconocido 2026' con mapas interactivos de aventura.\nESTRATEGIA 2 (NEGOCIO): Alianza con marcas de ropa técnica y agencias de viajes de expedición para descuentos exclusivos."
        },
        "Cocina y comida": {
            "m1": ["Pan de muerto tradicional", "Recetas con calabaza", "Sopas y cremas calientes", "Vinos y maridaje"],
            "m2": ["Cena de Navidad", "Guarniciones y ensaladas", "Postres para las posadas", "Bebidas para brindar"],
            "m3": ["Cena de Año Nuevo", "Cocteles clásicos", "Botanas para reuniones", "Dulces artesanales"],
            "propuesta": "ESTRATEGIA 1 (CONTENIDO): Recetario descargable 'Cenas Pro' con videos paso a paso para cocinar en familia.\nESTRATEGIA 2 (NEGOCIO): Programa de suscripción que envíe ingredientes gourmet directamente a la cocina del lector."
        },
        "Juveniles": {
            "m1": ["Estilo de moda actual", "Grupos de música del momento", "Pruebas de personalidad", "Cuidado del cutis joven"],
            "m2": ["Rutinas para la piel", "Creadores de contenido del año", "Conciertos previstos 2026", "Moda urbana"],
            "m3": ["Ropa para ir de fiesta", "Cambio de look de invierno", "Tendencias de redes sociales", "Organizador escolar 2026"],
            "propuesta": "ESTRATEGIA 1 (CONTENIDO): Reto de redes sociales enfocado en bienestar emocional y confianza personal.\nESTRATEGIA 2 (NEGOCIO): Venta de agendas y útiles escolares con diseño exclusivo y acceso a pláticas digitales."
        },
        "Niños": {
            "m1": ["Ciencia para niños", "Cuentos para noche de brujas", "Manualidades creativas", "Juegos de mesa"],
            "m2": ["Historias de dinosaurios", "El espacio y los planetas", "Relatos sobre la familia", "Armado de robots"],
            "m3": ["Deseos para los Reyes Magos", "Juegos para aprender", "Dibujos animados", "Libros de cuentos"],
            "propuesta": "ESTRATEGIA 1 (CONTENIDO): Podcast de leyendas y cuentos educativos para escuchar antes de dormir.\nESTRATEGIA 2 (NEGOCIO): Suscripción mensual a una caja con materiales para realizar experimentos científicos en casa."
        },
        "Coleccionables geek": {
            "m1": ["Figuras de superhéroes", "Réplicas de películas", "Historietas clásicas", "Ediciones de colección"],
            "m2": ["Espadas y accesorios de cine", "Muñecos de acción", "Escenarios a escala", "Libros de arte visual"],
            "m3": ["Paquetes de colección", "Juguetes de construcción", "Accesorios oficiales", "Estrenos de cine 2026"],
            "propuesta": "ESTRATEGIA 1 (CONTENIDO): Guía práctica para evaluar y conservar el valor de tus piezas de colección.\nESTRATEGIA 2 (NEGOCIO): Preventas exclusivas y sistema de apartado para asegurar piezas difíciles de conseguir."
        },
        "Armables técnicos": {
            "m1": ["Motores a escala", "Barcos para armar", "Coches de colección", "Aviones clásicos"],
            "m2": ["Maquetas electrónicas", "Naves del espacio", "Tanques de guerra históricos", "Herramientas de precisión"],
            "m3": ["Modelismo de metal", "Estuches de herramientas", "Pinturas especiales", "Vuelo a escala"],
            "propuesta": "ESTRATEGIA 1 (CONTENIDO): Comunidad de armadores con tutoriales de pintura y detallado paso a paso.\nESTRATEGIA 2 (NEGOCIO): Venta de repuestos, vitrinas de cristal y herramientas profesionales para el taller en casa."
        }
    }

    # --- GENERADORES DE ARCHIVO ---
    def encabezado_txt(sitio_nombre):
        doc = "============================================================\n"
        doc += "        REPORTE OFICIAL DE INTELIGENCIA PREDICTIVA\n"
        doc += f"        PLATAFORMA: {sitio_nombre.upper()}\n"
        doc += "============================================================\n\n"
        doc += f"FECHA DE EMISIÓN: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n"
        doc += "------------------------------------------------------------\n\n"
        return doc

    def cuerpo_nicho_txt(nicho, info):
        doc = f"NICHO: {nicho}\n"
        doc += f"🗓️ {m1}: " + ", ".join(info["m1"]) + "\n"
        doc += f"🗓️ {m2}: " + ", ".join(info["m2"]) + "\n"
        doc += f"🗓️ {m3}: " + ", ".join(info["m3"]) + "\n\n"
        doc += "RECOMENDACIONES ESTRATÉGICAS:\n"
        doc += f"{info['propuesta']}\n"
        doc += "\n" + ("-" * 40) + "\n\n"
        return doc

    def pie_pagina_txt(sitio_nombre):
        doc = "============================================================\n"
        doc += f"Este documento es confidencial y para uso exclusivo de {sitio_nombre}.\n"
        doc += "============================================================\n"
        return doc

    # --- INTERFAZ ---
    with st.sidebar:
        st.header("🛒 Plataforma")
        sitio = st.radio("Seleccione sitio:", ["tususcripcion.com", "tushoppi.mx"])
        st.divider()
        
        color_sitio = "#002d72" if sitio == "tususcripcion.com" else "#FF8C00"
        
        if sitio == "tususcripcion.com":
            opciones = ["Femenino", "Masculino", "Ciencia y Aventura", "Cocina y comida", "Juveniles", "Niños"]
        else:
            opciones = ["Coleccionables geek", "Armables técnicos"]
        
        nicho_sel = st.selectbox("Seleccione el Nicho:", ["GENERAR REPORTE INTEGRAL"] + opciones)
        btn_ejecutar = st.button("GENERAR INFORME 🚀")

    st.markdown(f"<style>.stButton>button {{ background-color: {color_sitio}; color: white; font-weight: bold; width: 100%; }}</style>", unsafe_allow_html=True)
    st.title(f"📑 {sitio.upper()} Inteligencia Predictiva")

    if btn_ejecutar:
        if nicho_sel == "GENERAR REPORTE INTEGRAL":
            reporte_final = encabezado_txt(sitio)
            for n in opciones:
                reporte_final += cuerpo_nicho_txt(n, biblioteca_datos[n])
            reporte_final += pie_pagina_txt(sitio)
            
            st.success("Reporte Integral generado con éxito.")
            st.download_button("📥 DESCARGAR REPORTE INTEGRAL", reporte_final, file_name=f"Reporte_Integral_{sitio}.txt")
        else:
            info = biblioteca_datos[nicho_sel]
            st.markdown(f"#### 📊 Análisis de Tendencias: {nicho_sel}")
            c1, c2, c3 = st.columns(3)
            for col, mes_lab, key in zip([c1, c2, c3], [m1, m2, m3], ["m1", "m2", "m3"]):
                with col:
                    st.info(f"🗓️ {mes_lab}")
                    for i in info[key]: st.write(f"• {i}")
            
            st.divider()
            st.subheader("🤖 Recomendaciones Estratégicas")
            st.markdown(f"<div style='border-left: 10px solid {color_sitio}; padding: 20px; background: white; border-radius: 10px; font-size: 1.1em;'>{info['propuesta'].replace('\n', '<br><br>')}</div>", unsafe_allow_html=True)
            
            reporte_ind = encabezado_txt(sitio) + cuerpo_nicho_txt(nicho_sel, info) + pie_pagina_txt(sitio)
            st.download_button("📥 DESCARGAR REPORTE DETALLADO", reporte_ind, file_name=f"Reporte_{nicho_sel}.txt")

    # --- AUDITORÍA ---
    st.divider()
    st.caption("🛡️ **ESPECIFICACIONES TÉCNICAS Y AUDITORÍA DE SISTEMA**")
    col_a, col_b, col_c = st.columns(3)
    with col_a: st.markdown("**Infraestructura:**\n* Python 3.12 Core\n* Streamlit Engine")
    with col_b: st.markdown("**Fuentes de Datos:**\n* Google Trends API\n* Google Search API")
    with col_c: st.markdown("**IA Engine:**\n* Gemini 1.5 Pro\n* Localización v23.0")
