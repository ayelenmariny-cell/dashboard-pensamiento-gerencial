import streamlit as st
import pandas as pd

# 1. Configuración general de la página (Debe ser la primera línea)
st.set_page_config(page_title="Guía de Supervivencia Gerencial", layout="wide", page_icon="📈")

# 2. Título principal
st.title("🎯 Guía de Supervivencia: Pensamiento Gerencial y el Ciclo de la Empresa")
st.markdown("---")

# 3. Creación de las pestañas
tab1, tab2, tab3 = st.tabs(["📖 Inicio: Guía de Supervivencia", "🚀 Misiones del Curso", "🧠 Reflexión Final"])

# ==========================================
# PESTAÑA 1: MARCO CONCEPTUAL (UNIFICADO Y PROFUNDIZADO)
# ==========================================
with tab1:
    st.header("🧠 Fundamentos Gerenciales: El Pensamiento y su Tablero de Juego")
    st.write("Antes de auditar los números, un gerente debe entender la naturaleza de su mente y la estructura de su entorno.")
    
    st.markdown("---")
    
    # SECCIÓN UNIFICADA: PENSAMIENTO GERENCIAL Y LA EMPRESA
    st.subheader("🌐 El Motor y el Tablero: Sincronizando la Mente Gerencial con la Empresa Real")
    
    col_izq, col_der = st.columns([1.2, 1])
    
    with col_izq:
        st.markdown("### 🧬 1. ¿Qué es el Pensamiento Gerencial?")
        st.write("""
        El **Pensamiento Gerencial** no es solo saber usar planillas o softwares; es el desarrollo de un **criterio analítico y crítico** para tomar decisiones bajo incertidumbre. 
        Un gerente no mira datos aislados. Su mente opera como un conector de puntos: entiende que un retraso en la bodega (Operaciones) destruye una promesa de venta (Comercial) y desangra la liquidez en el mediano plazo (Finanzas). 
        
        Desarrollar este pensamiento implica transicionar de un rol operativo (hacer la tarea) a un **rol estratégico** (entender el impacto sistémico de la tarea en el negocio).
        """)
    
    with col_der:
        st.markdown("### 🏢 2. La Empresa como Sistema Vivo")
        st.write("""
        La **Empresa** es el tablero de juego donde se aplica este pensamiento. No es una estructura estática, sino un **sistema vivo, interconectado y organizado** que combina recursos humanos, financieros y tecnológicos para resolver un problema en el mercado y generar valor económico.
        
        Ninguna de sus áreas puede operar como una isla: si el motor operativo falla, el impacto financiero es inmediato. El rol del gerente es mantener la homeostasis y el equilibrio de todo este sistema.
        """)

    st.markdown("---")
    
    # PROFUNDIZACIÓN: LA CLASIFICACIÓN INTERACTIVA DE LAS EMPRESAS
    st.markdown("### 📊 Clasificación Avanzada del Tablero de Juego")
    st.write("Para tomar decisiones correctas, un gerente debe clasificar y diagnosticar la naturaleza exacta de la empresa que lidera. En el mercado real, las empresas se estructuran bajo tres ejes críticos:")

    # Usamos métricas visuales para que sea estético y rápido de leer
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(label="🎯 Según su Actividad", value="Productivas o Comerciales", delta="B2B / B2C / Importadoras")
        st.markdown("""
        * **Industriales/Productivas:** Transforman materia prima en producto terminado.
        * **Comerciales/Distribuidores:** Com
# ==========================================
# PESTAÑA 2: PORTAFOLIO POR ÁREAS DE NEGOCIO (CORRECCIÓN CON ÁREAS EXACTAS)
# ==========================================
with tab2:
    st.header("🏢 Matriz de Madurez por Áreas Funcionales")
    st.write("Análisis del progreso del semestre organizado según las tres grandes áreas estratégicas de la empresa real.")

    # 1. Inicializar la memoria de área activa si no existe
    if "area_activa" not in st.session_state:
        st.session_state.area_activa = "📈 Área Comercial"

    # 2. Botones de Navegación Horizontal por las ÁREAS EXACTAS pedidas
    col_a1, col_a2, col_a3 = st.columns(3)
    
    with col_a1:
        a1_click = st.button("📈 Comercial", use_container_width=True)
    with col_a2:
        a2_click = st.button("📦 Operaciones", use_container_width=True)
    with col_a3:
        a3_click = st.button("💰 Finanzas de Contabilidad", use_container_width=True)

    # Controlar el clic de los botones
    if a1_click: st.session_state.area_activa = "📈 Área Comercial"
    if a2_click: st.session_state.area_activa = "📦 Área de Operaciones"
    if a3_click: st.session_state.area_activa = "💰 Área de Finanzas de Contabilidad"

    st.markdown("---")

    # ==========================================
    # ÁREA 1: COMERCIAL
    # ==========================================
    if st.session_state.area_activa == "📈 Área Comercial":
        st.subheader("📈 Área Comercial: Estrategia de Clientes y Propuestas de Valor")
        
        # Ficha Técnica
        c1, c2, c3 = st.columns(3)
        c1.markdown("**🎯 Objetivo del Área:** Maximizar la rentabilidad de la cartera diseñando ofertas a la medida del mercado.")
        c2.markdown("**⚠️ Problema Inicial:** Fuerza de ventas desgastada por atender con el mismo esfuerzo a clientes masivos y estratégicos.")
        c3.markdown("**🛠️ Herramientas Evolutivas:** Segmentación B2B/B2C, Ingeniería de Prompts e Inteligencia Artificial.")
        
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🔄 Evolución del Aprendizaje Gerencial")
            st.write("""
            Al principio del semestre, nuestra visión comercial consistía simplemente en empujar ventas sin una estrategia clara. A lo largo del proceso, entendimos que el éxito comercial requiere una **planificación** integrada. 
            
            Aprendimos a clasificar la cartera distinguiendo el comportamiento de clientes bajo lógicas transaccionales (B2C) y relacionales (B2B). El gran salto innovador ocurrió al integrar Inteligencia Artificial (**IA**) como copiloto, permitiéndonos formular **propuestas** comerciales competitivas y personalizadas en tiempo récord, optimizando el rendimiento de la fuerza de ventas.
            """)
        with col2:
            st.markdown("### 🛠️ Obstáculos y Criterio Profesional Futuro")
            st.error("**La Gran Dificultad superada:** Aprender a no depender ciegamente de las respuestas tecnológicas; validar y estructurar los entregables de la **IA** con un criterio humano riguroso.")
            st.success("**Uso en la Empresa Real:** Nos capacita para liderar equipos comerciales modernos, utilizando tecnologías emergentes para segmentar mercados y estructurar ofertas de alto valor corporativo.")

    # ==========================================
    # ÁREA 2: OPERACIONES
    # ==========================================
    elif st.session_state.area_activa == "📦 Área de Operaciones":
        st.subheader("📦 Área de Operaciones: Gestión de Bodega, Abastecimiento y Logística")
        
        # Ficha Técnica
        c1, c2, c3 = st.columns(3)
        c1.markdown("**🎯 Objetivo del Área:** Asegurar la continuidad operativa alineando el stock con la demanda.")
        c2.markdown("**⚠️ Problema Inicial:** Quiebres de stock continuos conviviendo con capital inmovilizado en productos estancados.")
        c3.markdown("**🛠️ Herramientas Evolutivas:** Historial de Kardex, Análisis de Pareto (ABC) y Prorrateo logístico.")
        
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🔄 Evolución del Aprendizaje Gerencial")
            st.write("""
            Comenzamos viendo la logística de forma aislada, creyendo que la bodega se manejaba de forma intuitiva. El análisis del **Kardex** físico nos abrió los ojos para entender la velocidad de rotación real del **inventario**. 
            
            Posteriormente, la clasificación ABC nos enseñó a priorizar esfuerzos en los SKU críticos para el negocio. La madurez del área se consolidó al enfrentar el proceso de **importaciones**, donde logramos conectar la operación de traer contenedores desde el extranjero con una estrategia de **abastecimiento** sincronizada con las proyecciones de venta de la empresa.
            """)
        with col2:
            st.markdown("### 🛠️ Obstáculos y Criterio Profesional Futuro")
            st.error("**La Gran Dificultad superada:** Conciliar bases de datos operativas imperfectas y balancear las presiones comerciales (stock infinito) con las restricciones financieras.")
            st.success("**Uso en la Empresa Real:** Diseñar e implementar políticas eficientes de inventario y compras internacionales en firmas comerciales, protegiendo el capital de trabajo de la organización.")

    # ==========================================
    # ÁREA 3: FINANZAS DE CONTABILIDAD
    # ==========================================
    elif st.session_state.area_activa == "💰 Área de Finanzas de Contabilidad":
        st.subheader("💰 Área de Finanzas de Contabilidad: Control de Gestión y Salud Financiera")
        
        # Ficha Técnica
        c1, c2, c3 = st.columns(3)
        c1.markdown("**🎯 Objetivo del Área:** Traducir los hechos económicos de la operación en información verídica para la toma de decisiones.")
        c2.markdown("**⚠️ Problema Inicial:** Inconsistencias en registros, desfases de costeo en ERP y datos dispersos sin estructura ejecutiva.")
        c3.markdown("**🛠️ Herramientas Evolutivas:** Libros de remuneraciones, Balance de 8 columnas y Dashboards de Control.")
        
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🔄 Evolución del Aprendizaje Gerencial")
            st.write("""
            En esta área descubrimos el verdadero lenguaje de los negocios. Comenzamos analizando **costos** básicos, pero avanzamos rápidamente a entender la complejidad de auditar planillas operativas, integrando el cálculo de **sueldos** junto con sus respectivas **cotizaciones** previsionales legales. 
            
            Todo este ecosistema de información contable maduró al transformar los libros diarios en Estados Financieros consolidados (Balance y Estado de Resultados). Esto nos permitió auditar los **márgenes** de contribución reales y utilizar técnicas modernas de **visualización** de **datos** para presentar la salud del negocio a nivel directivo.
            """)
        with col2:
            st.markdown("### 🛠️ Obstáculos y Criterio Profesional Futuro")
            st.error("**La Gran Dificultad superada:** Superar el simple cuadre numérico de celdas y balances para ser capaces de redactar conclusiones financieras estratégicas sobre la liquidez y el riesgo.")
            st.success("**Uso en la Empresa Real:** Nos faculta para estructurar presupuestos corporativos eficientes, auditar costos de importación reales y rendir cuentas transparentes ante un Directorio o inversionistas mediante tableros de control.")

    st.markdown("---")
    st.caption("💡 Consejo de la Dupla: Haz clic en cada una de las tres áreas de arriba para revisar el progreso contable, comercial y logístico exigido en la pauta.")
# ==========================================
# PESTAÑA 3: REFLEXIÓN FINAL (¡INTERACTIVA Y SEGÚN LA PREGUNTA CENTRAL!)
# ==========================================
with tab3:
    st.header("🧠 Reflexión Ejecutiva e Integración de Aprendizajes")
    st.write("Selecciona una situación empresarial real abajo para descubrir qué aprendimos, su valor y su aplicación futura.")
    
    st.markdown("---")
    
    # 1. Componente Interactivo: El Simulador de Decisiones Gerenciales
    st.subheader("🏢 Simulador de Criterio Gerencial")
    st.write("Imagina que eres el nuevo Gerente General de nuestra empresa importadora. ¿Qué problema crítico te gustaría resolver hoy?")
    
    opcion_reflexion = st.selectbox(
        "Elige un escenario crítico de negocio para analizar:",
        ["🚨 Escenario A: La bodega está colapsada, pero Comercial dice que faltan productos.",
         "📉 Escenario B: Las planillas de costos no cuadran y hay sospechas de pérdidas en el margen.",
         "🔮 Escenario C: El Directorio exige presentar el plan estratégico y financiero para el próximo año."]
    )
    
    st.markdown("---")
    
    # 2. Respuestas dinámicas que responden exactamente a la pregunta del examen
    if opcion_reflexion == "🚨 Escenario A: La bodega está colapsada, pero Comercial dice que faltan productos.":
        st.markdown("### 📦 Diagnóstico: Gestión de Inventario, Abastecimiento y Planificación")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("### 🧠 ¿Qué Aprendimos?")
            st.write("""
            En las **Misiones 1, 2 y 3** aprendimos que el inventario no es solo mercadería guardada, sino capital de trabajo congelado. 
            Aprendimos a usar el **Kardex** para calcular la rotación real, a aplicar la **Clasificación ABC** (Pareto) para priorizar el catálogo, y a usar modelos matemáticos de **planificación** de la demanda.
            """)
            
        with col2:
            st.success("### 💎 ¿Qué Valor tuvo?")
            st.write("""
            El valor fue entender el impacto de la **planificación integrada**. Nos enseñó a no operar por intuición. Descubrimos que el desbalance se soluciona creando un puente de **datos** entre las metas de Ventas y el presupuesto de Compras, logrando eficiencia sin ahogar las finanzas.
            """)
            
        with col3:
            st.warning("### 🔮 ¿Cómo usarlo en el Futuro?")
            st.write("""
            En una empresa real, utilizaremos esto para establecer políticas de stock de seguridad automatizadas y liderar comités de **abastecimiento** mensuales. Así evitaremos quiebres que ahuyenten clientes y sobrestocks que destruyan la liquidez.
            """)

    elif opcion_reflexion == "📉 Escenario B: Las planillas de costos no cuadran y hay sospechas de pérdidas en el margen.":
        st.markdown("### 💰 Diagnóstico: Auditoría de Costos, Sueldos y Márgenes de Importación")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("### 🧠 ¿Qué Aprendimos?")
            st.write("""
            En las **Misiones 2 and 5** aprendimos a auditar la estructura completa de **costos**, incluyendo el prorrateo de fletes en **importaciones**. También calculamos el impacto real de los **sueldos** y sus **cotizaciones** previsionales sobre la carga financiera fija de la empresa.
            """)
            
        with col2:
            st.success("### 💎 ¿Qué Valor tuvo?")
            st.write("""
            El valor fue desarrollar un ojo auditor y crítico. Entendimos que si el sistema arroja 'costos negativos' o ignora las leyes sociales, cualquier cálculo de **márgenes** o utilidades finales será una ilusión contable que puede llevar a la quiebra.
            """)
            
        with col3:
            st.warning("### 🔮 ¿Cómo usarlo en el Futuro?")
            st.write("""
            En el futuro, aplicaremos esto para visar las matrices de precios de productos importados y controlar los presupuestos de contratación de personal. Tomaremos decisiones basadas en **costos reales** y auditados, protegiendo la rentabilidad de la firma.
            """)

    else:
        st.markdown("### ⚖️ Diagnóstico: Estados Financieros, IA y Visualización Ejecutiva")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("### 🧠 ¿Qué Aprendimos?")
            st.write("""
            En las **Misiones 4 y 7** aprendimos a sintetizar miles de transacciones de libros diarios en Estados Financieros (Balance y Estado de Resultados). Además, aprendimos a usar Inteligencia Artificial (**IA**) como copiloto para diseñar **propuestas** comerciales y segmentar clientes.
            """)
            
        with col2:
            st.success("### 💎 ¿Qué Valor tuvo?")
            st.write("""
            El valor fue aprender a conectar la operación física con el lenguaje financiero directivo. Descubrimos el poder de la **visualización** de **datos** para transformar números áridos en un tablero ejecutivo claro, permitiendo evaluar la salud del negocio en un segundo.
            """)
            
        with col3:
            st.warning("### 🔮 ¿Cómo usarlo en el Futuro?")
            st.write("""
            En nuestra vida profesional, usaremos la **visualización** interactiva y la **IA** para presentar informes ante directorios o inversionistas. Nos permitirá defender decisiones estratégicas con argumentos financieros sólidos, evaluando riesgos y detectando oportunidades de crecimiento.
            """)

    st.markdown("---")
    
    # 3. Conclusión de cierre de la Dupla
    st.markdown("### 🤝 Conclusión de la Dupla Gerencial")
    st.markdown("""
    A lo largo de este taller, comprendimos que **las empresas son sistemas vivos e interconectados**. El verdadero valor del curso no radicó en dominar el software, sino en el **desarrollo del criterio gerencial**. Las herramientas nos entregan los datos, pero somos los profesionales quienes, con pensamiento crítico, debemos transformar esos datos en decisiones estratégicas. 
    
    **Nos llevamos el mapa completo de una organización: desde el movimiento en la bodega hasta el veredicto final de los Estados Financieros.**
    """)
    
    # Campo interactivo para feedback de los profesores
    st.text_area("✍️ Espacio para comentarios o notas del Profesor evaluador:", "Excelente propuesta interactiva para el cierre del portafolio...")
