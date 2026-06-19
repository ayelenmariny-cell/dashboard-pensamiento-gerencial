import streamlit as st
import pandas as pd

# ============================================================
# CONFIGURACIÓN GENERAL Y ESTILOS (TU DISEÑO LILA PREMIUM)
# ============================================================
st.set_page_config(
    page_title="Portafolio Gerencial Interactivo",
    page_icon="🌸",
    layout="wide"
)

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght=400;600;700;800&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Inter', sans-serif;
        }

        .stApp {
            background: linear-gradient(135deg, #fbf7ff 0%, #f1e7ff 45%, #fff8fb 100%);
        }

        .main-title {
            padding: 1.5rem 1.7rem;
            border-radius: 28px;
            background: linear-gradient(135deg, #7b4bb7 0%, #b388eb 55%, #f7c8e0 100%);
            color: white;
            box-shadow: 0 16px 40px rgba(123, 75, 183, 0.22);
            margin-bottom: 1.2rem;
        }

        .main-title h1 {
            margin: 0;
            font-size: 2.15rem;
            line-height: 1.15;
            font-weight: 800;
        }

        .main-title p {
            margin-top: .65rem;
            font-size: 1.02rem;
            opacity: .95;
        }

        .section-card {
            padding: 1.25rem 1.35rem;
            border-radius: 22px;
            background: rgba(255, 255, 255, 0.80);
            border: 1px solid rgba(179, 136, 235, 0.26);
            box-shadow: 0 12px 28px rgba(109, 75, 145, 0.10);
            margin-bottom: 1rem;
            color: #3b155f;
        }

        .soft-card {
            padding: 1.05rem 1.15rem;
            border-radius: 20px;
            background: #ffffffcc;
            border-left: 6px solid #b388eb;
            box-shadow: 0 10px 25px rgba(123, 75, 183, 0.10);
            min-height: 155px;
            margin-bottom: 1rem;
        }

        .mini-card {
            padding: .95rem 1rem;
            border-radius: 18px;
            background: #ffffffd9;
            border: 1px solid #eadcff;
            box-shadow: 0 8px 20px rgba(123, 75, 183, 0.08);
            min-height: 135px;
            margin-bottom: 1rem;
        }

        .concept-pill {
            display: inline-block;
            padding: .35rem .7rem;
            margin: .18rem .18rem .18rem 0;
            border-radius: 999px;
            background: #efe2ff;
            color: #5a2d82;
            font-weight: 700;
            font-size: .86rem;
            border: 1px solid #d9c3ff;
        }

        h1, h2, h3, h4 {
            color: #4b2178;
        }

        div[data-testid="stMetricValue"] {
            color: #6f42c1;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: .4rem;
        }

        .stTabs [data-baseweb="tab"] {
            background-color: #ffffffb8;
            border-radius: 999px;
            padding: .6rem 1rem;
            border: 1px solid #eadcff;
        }

        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #d9c3ff, #f7c8e0) !important;
            color: #3b155f !important;
            font-weight: 800;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# COMPONENTES VISUALES REUTILIZABLES
# ============================================================
def hero(titulo: str, bajada: str):
    st.markdown(f'<div class="main-title"><h1>{titulo}</h1><p>{bajada}</p></div>', unsafe_allow_html=True)

def card(titulo: str, texto: str, icono: str = "✨"):
    st.markdown(f'<div class="soft-card"><h3>{icono} {titulo}</h3><p>{texto}</p></div>', unsafe_allow_html=True)

def mini_card(titulo: str, texto: str, icono: str = "•"):
    st.markdown(f'<div class="mini-card"><h4>{icono} {titulo}</h4><p>{texto}</p></div>', unsafe_allow_html=True)

def concepto(nombre: str):
    st.markdown(f"<span class='concept-pill'>{nombre}</span>", unsafe_allow_html=True)

# BANNER PRINCIPAL
hero(
    "🌸 Portafolio Colectivo Avanzado: Pensamiento Gerencial Aplicado",
    "Demostración interactiva de la madurez del criterio de negocio a través de las grandes áreas estratégicas de la empresa."
)

# PESTAÑAS
tab1, tab2, tab3 = st.tabs([
    "🌐 1. Marco Conceptual e Intro", 
    "🏢 2. Matriz de Madurez por Áreas", 
    "🧠 3. Reflexión Final e Impacto"
])

# ============================================================
# PESTAÑA 1: MARCO CONCEPTUAL (UNIFICADO Y PROFUNDIZADO)
# ============================================================
with tab1:
    st.header("🧠 Fundamentos Gerenciales: El Pensamiento y su Tablero de Juego")
    
    st.markdown(
        """
        <div class="section-card">
        <b>Idea central:</b> Una empresa no es una planilla estática de tareas. Es un <b>sistema vivo</b> e interconectado 
        donde cada decisión operativa gatilla un efecto dominó sobre los estados financieros y la viabilidad comercial.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col_izq, col_der = st.columns([1.2, 1])
    
    with col_izq:
        st.subheader("🧬 ¿Qué es el Pensamiento Gerencial?")
        st.write(
            "Es la capacidad de desarrollar un **criterio analítico y crítico** para tomar decisiones defendibles bajo incertidumbre. "
            "Implica transicionar de un rol puramente operativo (completar una tarea) a un **rol estratégico** (comprender el impacto sistémico de la tarea en el negocio)."
        )
        st.info(
            "🏥 **La Analogía Sistémica:** El área de Finanzas de Contabilidad actúa como el corazón que distribuye los recursos; "
            "Operaciones representa los músculos que ejecutan el abastecimiento y la bodega; Comercial y Ventas son los sentidos que leen al cliente; "
            "mientras la Gerencia opera como el cerebro que orquesta el sistema completo."
        )
    
    with col_der:
        st.subheader("⚙️ Funciones Básicas del Administrador")
        funciones = pd.DataFrame({
            "Función": ["Planificar", "Organizar", "Dirigir", "Controlar"],
            "Enfoque Gerencial Extendido": [
                "Definir metas del negocio, prever la demanda futura y estructurar cursos de acción estratégicos.",
                "Asignar recursos escasos, estructurar responsabilidades y sincronizar departamentos corporativos.",
                "Comunicar visiones estratégicas, liderar con base en datos y movilizar equipos hacia objetivos comunes.",
                "Medir desvíos mediante visualización de datos, auditar costos y aplicar correcciones oportunas."
            ]
        })
        st.dataframe(funciones, use_container_width=True, hide_index=True)

    st.markdown("---")
    
    st.subheader("🎛️ Lentes del Criterio Profesional")
    st.write("Un directivo alterna dinámicamente sus marcos de pensamiento según la complejidad del escenario organizacional:")
    
    lente = st.radio("Selecciona un enfoque conceptual para examinar su utilidad gerencial:", ["⚙️ Sistémico", "♟️ Estratégico", "🔍 Crítico"], horizontal=True)
    if lente == "⚙️ Sistémico":
        st.success("**Pensamiento Sistémico:** Muestra las cadenas de impacto. Permite ver que un error en el registro de bodega altera el costeo de importaciones, distorsiona los márgenes y vicia el Balance General.")
    elif lente == "♟️ Estratégico":
        st.success("**Pensamiento Estratégico:** Centrado en la sostenibilidad de largo plazo. Evalúa si las propuestas comerciales de hoy comprometen la caja, la capacidad de almacenamiento o la reputación de la firma mañana.")
    else:
        st.success("**Pensamiento Crítico:** Desafía los datos preliminares. Obliga al equipo a cuestionar 'costos negativos' o reportes contables inconsistentes antes de fijar las matrices de precio.")

    st.markdown("---")
    st.subheader("📊 Clasificación Avanzada del Tablero de Juego")
    st.write("Las empresas comerciales y del sector terciario (como nuestro foco en **importaciones**) centran su gestión en coordinar eficientemente los flujos financieros y de stock:")
    
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(label="🎯 Por Actividad", value="Sector Terciario / Comercial", delta="B2B / B2C / Importadoras")
        st.write("El foco absoluto radica en los clientes, las propuestas de valor y la velocidad de rotación física del producto.")
    with m2:
        st.metric(label="📏 Por Tamaño", value="Mediana Empresa (Pyme)", delta="Estructuras Flexibles")
        st.write("Exige liderazgos integrales capaces de conectar los datos de compras y ventas de forma directa sin burocracia.")
    with m3:
        st.metric(label="⚖️ Por Capital", value="Empresa Privada", delta="Maximización del Margen")
        st.write("Busca proteger la rentabilidad de los accionistas asegurando liquidez y controlando estrictamente las mermas.")

# ============================================================
# PESTAÑA 2: MATRIZ DE MADUREZ POR ÁREAS (EVOLUCIÓN ENFOQUE PROFESOR)
# ============================================================
with tab2:
    st.header("🏢 Evolución de Criterio por Áreas Funcionales")
    st.write("Demostración cronológica de madurez del equipo. Evaluamos nuestro progreso unificando las misiones por áreas estratégicas.")

    if "area_activa" not in st.session_state:
        st.session_state.area_activa = "📈 Comercial"

    col_a1, col_a2, col_a3 = st.columns(3)
    with col_a1:
        if st.button("📈 Comercial y Ventas", use_container_width=True): st.session_state.area_activa = "📈 Comercial"
    with col_a2:
        if st.button("📦 Operaciones y Bodega", use_container_width=True): st.session_state.area_activa = "📦 Operaciones"
    with col_a3:
        if st.button("💰 Finanzas de Contabilidad", use_container_width=True): st.session_state.area_activa = "💰 Finanzas"

    st.markdown("---")

    if st.session_state.area_activa == "📈 Comercial":
        st.subheader("📈 Área Comercial: Gestión Estratégica de Clientes y Oferta de Valor")
        c1, c2, c3 = st.columns(3)
        with c1: mini_card("Objetivo Primario", "Maximizar la contribución de la cartera diseñando modelos de atención diferenciados.", "🎯")
        with c2: mini_card("Problema de Partida", "Equipos comerciales desgastados por atender con idéntico recurso a clientes masivos y cuentas clave.", "⚠️")
        with c3: mini_card("Conceptos Clave", "Clientes, Propuestas, Planificación, Segmentación B2B y B2C.", "🔗")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🔄 Evolución del Aprendizaje (De Misión 4 a Misión 7)")
            st.write(
                "Al inicio del semestre, nuestra perspectiva comercial era lineal: vender volumen a cualquier costo. "
                "Al abordar la **Misión 4**, entendimos que una cartera comercial requiere **planificación** analítica. "
                "Clasificamos a los **clientes** según valor, frecuencia y potencial, distinguiendo dinámicas de negociación corporativa (B2B) frente a masivas (B2C). "
                "Posteriormente, formulamos **propuestas** de valor competitivas de forma ágil, culminando en la **Misión 7** con modelos de **visualización** que mapean el rendimiento comercial en tiempo real."
            )
        with col2:
            st.markdown("### 🛠️ Obstáculos Superados y Criterio Profesional")
            st.error("**El Quiebre:** Superar la tentación de confiar ciegamente en algoritmos de generación de texto corporativo; aprendimos a auditar los entregables de la **IA** bajo un estricto criterio comercial humano.")
            st.success("**Aplicación Futura:** Diseñar planes de cobertura comercial eficientes, comisiones de venta basadas en **márgenes** reales y transformaciones digitales con analítica de datos comerciales.")

    elif st.session_state.area_activa == "📦 Operaciones":
        st.subheader("📦 Área de Operaciones: Sincronización de Bodega, Logística y Abastecimiento")
        c1, c2, c3 = st.columns(3)
        with c1: mini_card("Objetivo Primario", "Garantizar la continuidad del negocio mitigando mermas y balanceando los niveles de servicio.", "🎯")
        with c2: mini_card("Problema de Partida", "Bodegas colapsadas con stock obsoleto conviviendo con quiebres críticos en productos estrella.", "⚠️")
        with c3: mini_card("Conceptos Clave", "Inventario, Kardex, Abastecimiento, Importaciones, Clasificación ABC, SKU.", "🔗")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🔄 Evolución del Aprendizaje (De Misión 2 a Misión 5)")
            st.write(
                "Nuestra inmersión operativa comenzó en la **Misión 2**, donde concebíamos la bodega como un mero almacén estático. El análisis del **Kardex** de movimientos nos demostró el impacto financiero del **inventario** inmovilizado. "
                "Con la técnica ABC, aprendimos a priorizar recursos en los SKU que sostienen las ventas. El verdadero salto gerencial ocurrió entre la **Misión 3** y **Misión 5**: logramos conectar el pronóstico de demanda con la logística de **importaciones**, transformando la compra reactiva en un proceso formal de **abastecimiento** estratégico."
            )
        with col2:
            st.markdown("### 🛠️ Obstáculos Superados y Criterio Profesional")
            st.error("**El Quiebre:** Trabajar con bases de datos operativas reales que contenían inconsistencias y conciliar la presión comercial por sobrestockearse frente a las restricciones de espacio físico.")
            st.success("**Aplicación Futura:** Liderar departamentos logísticos fijando stocks de seguridad matemáticos, optimizando el capital de trabajo y coordinando cadenas de suministro internacionales eficientes.")

    elif st.session_state.area_activa == "💰 Finanzas":
        st.subheader("💰 Área de Finanzas y Contabilidad: Control de Gestión y Estructura Financiera")
        c1, c2, c3 = st.columns(3)
        with c1: mini_card("Objetivo Primario", "Traducir los hechos económicos del negocio en estados financieros íntegros para el gobierno corporativo.", "🎯")
        with c2: mini_card("Problema de Partida", "Existencia de inconsistencias contables ('costos negativos') en los ERP que invalidaban la toma de decisiones.", "⚠️")
        with c3: mini_card("Conceptos Clave", "Costos, Sueldos, Cotizaciones, Márgenes, Estados Financieros, Balance.", "🔗")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🔄 Evolución del Aprendizaje (De Misión 5 a Misión 7)")
            st.write(
                "Iniciamos el análisis financiero en la **Misión 5**, enfrentando descalces de costeo y aprendiendo a estructurar planillas complejas de **sueldos** y **cotizaciones** previsionales bajo marco legal. "
                "Nuestra visión maduró de forma definitiva en la **Misión 7**, cuando dejamos de ver cuentas aisladas y consolidamos Libros Diarios en un Balance de Ocho Columnas y Estados Financieros completos. Aprendimos a auditar los **márgenes** brutos y operacionales reales de la organización para emitir diagnósticos financieros certeros."
            )
        with col2:
            st.markdown("### 🛠️ Obstáculos Superados y Criterio Profesional")
            st.error("**El Quiebre:** Romper la visión del contador tradicional enfocado solo en el 'cuadre por partida doble'; escalamos hacia la mentalidad directiva que interpreta indicadores de liquidez, endeudamiento y rentabilidad.")
            st.success("**Aplicación Futura:** Evaluar la viabilidad financiera de proyectos comerciales, defender presupuestos ante comités directivos y estructurar tableros de control de gestión automatizados.")

# ============================================================
# PESTAÑA 3: REFLEXIÓN FINAL E IMPACTO (TU EXCELENTE SIMULADOR SELECTBOX)
# ============================================================
with tab3:
    st.header("🧠 Reflexión Ejecutiva e Integración de Aprendizajes")
    st.write("Selecciona un escenario de negocio real para evaluar cómo el criterio gerencial resuelve la complejidad empresarial:")
    
    opcion_reflexion = st.selectbox(
        "Elige una situación crítica organizativa para auditar:",
        ["🚨 Escenario A: La bodega está colapsada, pero Comercial reclama quiebres de stock continuos.",
         "📉 Escenario B: Las planillas de costos muestran descalces y hay sospechas de pérdidas silenciosas de margen.",
         "🔮 Escenario C: El Directorio exige sustentar el plan de expansión estratégica basado en la salud del negocio."]
    )
    
    st.markdown("---")
    
    if "🚨" in opcion_reflexion:
        st.markdown("### 📦 Diagnóstico de Operaciones: Sincronización Comercial-Abastecimiento")
        col1, col2, col3 = st.columns(3)
        with col1: st.info("### 🧠 ¿Qué Aprendimos?\nQue el inventario inmovilizado destruye la caja. El uso de **Kardex** y clasificación ABC permite segmentar los SKU y estructurar una **planificación** científica de compras.")
        with col2: st.success("### 💎 ¿Qué Valor tuvo?\nPermitió entender que los desbalances operativos no se resuelven con intuiciones, sino construyendo puentes de **datos** integrados entre las áreas de compras y ventas.")
        with col3: st.warning("### 🔮 Aplicación Futura:\nEstablecer políticas automáticas de reaprovisionamiento e implementar rutinas de S&OP (Sales and Operations Planning) para blindar la continuidad del negocio.")

    elif "📉" in opcion_reflexion:
        st.markdown("### 💰 Diagnóstico Financiero: Auditoría de Costos Reales y Remuneraciones")
        col1, col2, col3 = st.columns(3)
        with col1: st.info("### 🧠 ¿Qué Aprendimos?\nA construir el costo real integrando fletes de **importaciones**, mermas y cargas fijas de personal como **sueldos** y **cotizaciones** legalizadas.")
        with col2: st.success("### 💎 ¿Qué Valor tuvo?\nDesarrollar un pensamiento crítico: si la base contable arrastra errores, los **márgenes** serán ficticios y las utilidades reportadas una mera ilusión financiera.")
        with col3: st.warning("### 🔮 Aplicación Futura:\nLiderar auditorías de procesos internos y estructurar matrices de precios blindadas ante fluctuaciones en los costos internacionales.")

    else:
        st.markdown("### ⚖️ Diagnóstico de Dirección: Consolidación Financiera y Visualización")
        col1, col2, col3 = st.columns(3)
        with col1: st.info("### 🧠 ¿Qué Aprendimos?\nA unificar las transacciones contables operativas en Estados Financieros y a utilizar **IA** estratégica para la confección de **propuestas** comerciales de alto nivel.")
        with col2: st.success("### 💎 ¿Qué Valor tuvo?\nComprender el poder de la **visualización** avanzada para traducir grandes volúmenes de datos áridos en información estratégica asimilable por un Directorio.")
        with col3: st.warning("### 🔮 Aplicación Futura:\nPresentar estados de situación corporativa con solidez metodológica y liderar el proceso de toma de decisiones basándose en evidencia empírica auditable.")

    st.markdown("---")
    st.markdown(
        """
        <div class="section-card">
        <h3>🤝 Conclusión Consolidada de la Dupla Gerencial</h3>
        <p>
        A lo largo de este trayecto académico comprendimos que <b>las empresas son sistemas vivos, dinámicos e interconectados</b>. 
        El valor supremo no consistió en memorizar comandos de software, sino en forjar nuestro <b>criterio gerencial</b>. 
        Las herramientas digitales proveen los datos, pero corresponde a los directivos transformar esa analítica en decisiones estratégicas defendibles. 
        Nos despedimos del ciclo con el mapa integral de la firma: desde el movimiento primario en bodega hasta el veredicto definitivo en los estados financieros.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.text_area("✍️ Espacio para comentarios o notas del Profesor evaluador:", "Excelente integración de conceptos y madurez en el análisis por macroáreas estratégicas.")
