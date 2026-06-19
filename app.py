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
# CONTENIDO DE LA PRIMERA PESTAÑA (INICIO)
# ==========================================
with tab1:
    
    # --- MENSAJE DE BIENVENIDA ---
    st.markdown("### Bienvenido al curso")
    st.info("""
    Antes de sumergirnos en números, planillas y reportes, necesitamos ajustar nuestra forma de ver los negocios. 
    Esta guía está diseñada para darte el contexto y ayudarte a conectar los puntos que a veces se pierden en el día a día de las clases. 
    **Aquí no aprenderás a "completar misiones", aprenderás a pensar como un gerente.**
    """)
    st.markdown("<br>", unsafe_allow_html=True) # Espacio en blanco

    # --- SECCIÓN 1: EL MOTOR PRINCIPAL ---
    st.header("1. El Motor Principal: ¿Qué es el Pensamiento Gerencial?")
    st.write("No se trata de 'ser el jefe' o dar órdenes. El pensamiento gerencial es un **modelo mental**. Es la capacidad de ver una organización como un todo interconectado. Es el arte de tomar decisiones, optimizar recursos limitados y guiar a un equipo hacia un objetivo.")
    
    st.write("#### Un buen gerente cambia de 'lentes' constantemente:")
    lente = st.radio(
        "Selecciona un lente para explorar su significado:",
        ["⚙️ Pensamiento Sistémico", "♟️ Pensamiento Estratégico", "🔍 Pensamiento Crítico"],
        horizontal=True
    )

    if lente == "⚙️ Pensamiento Sistémico":
        st.success("**Pensamiento Sistémico:** Entender que la empresa es como un reloj. Si modificas algo en Ventas, afectará a Finanzas y Producción. Nada ocurre en el vacío.")
    elif lente == "♟️ Pensamiento Estratégico":
        st.success("**Pensamiento Estratégico:** Mirar a largo plazo. Es anticipar los movimientos futuros en lugar de solo 'apagar incendios' diarios.")
    else:
        st.success("**Pensamiento Crítico:** Cuestionar suposiciones, analizar datos reales y encontrar la causa raíz antes de proponer una solución.")

    # Expander para las funciones clásicas
    with st.expander("Haz clic aquí para ver las 4 Funciones Clásicas (Tu ciclo de trabajo)"):
        col_f1, col_f2, col_f3, col_f4 = st.columns(4)
        col_f1.markdown("📝 **Planificar:**\nDefinir metas y la estrategia para alcanzarlas.")
        col_f2.markdown("🧩 **Organizar:**\nAsignar recursos y estructurar quién hace qué.")
        col_f3.markdown("🗣️ **Dirigir:**\nLiderar, motivar y comunicar al equipo.")
        col_f4.markdown("📊 **Controlar:**\nMedir los resultados y ajustar el rumbo si es necesario.")

    st.markdown("---")

    # --- SECCIÓN 2: EL TABLERO DE JUEGO ---
    st.header("2. El Tablero de Juego: ¿Qué es una Empresa y cómo se clasifica?")
    st.write("Más allá de los edificios corporativos o las marcas, una empresa es un **sistema vivo**. Es un conjunto de personas, recursos y procesos unidos con un objetivo claro: resolver un problema o satisfacer una necesidad del mercado a cambio de un beneficio.")
    st.write("🏥 *La empresa es como un cuerpo: las decisiones gerenciales son el cerebro que coordina que el corazón (finanzas), los músculos (operaciones) y los sentidos (marketing) trabajen juntos para sobrevivir.*")
    
    st.write("Dependiendo de dónde trabajes mañana, el tablero cambia:")
    
    # Tabla de sectores económicos
    datos_sectores = {
        "Sector": ["Primario", "Secundario", "Terciario"],
        "¿Qué hacen?": ["Extracción de materias primas.", "Manufactura y transformación.", "Servicios, comercio e intangibles."],
        "Ejemplo": ["Minería, Agricultura", "Fábrica de muebles", "Bancos, Retail"],
        "Impacto en tus decisiones": ["Fuerte enfoque en maquinaria e inventario físico.", "Su corazón está en los Costos de Producción y compras.", "Las ventas y la fidelización de clientes son su motor principal."]
    }
    df_sectores = pd.DataFrame(datos_sectores)
    st.dataframe(df_sectores, use_container_width=True, hide_index=True)

    st.markdown("---")

    # --- SECCIÓN 3: EL ESCENARIO ---
    st.header("3. El Escenario: Nuestra Empresa y sus Departamentos")
    st.write("Para entender el recorrido de este curso, simularemos trabajar en una **mediana empresa comercializadora e importadora (Sector Terciario)**. No fabricamos desde cero; compramos productos terminados, los almacenamos y los vendemos.")
    st.write("En una empresa así, el pensamiento gerencial requiere alinear tres grandes áreas que, si no se comunican, destruyen el negocio:")

    # Columnas de departamentos
    col_ventas, col_operaciones, col_finanzas = st.columns(3)
    
    with col_ventas:
        st.error("🛒 **El Área Comercial (Ventas)**")
        st.write("- **Su objetivo:** Vender al máximo.")
        st.write("- **Su peor pesadilla:** Prometer un producto y que no haya stock.")
        
    with col_operaciones:
        st.warning("📦 **Área de Operaciones (Bodega)**")
        st.write("- **Su objetivo:** Son los guardianes físicos.")
        st.write("- **Su peor pesadilla:** Comprar cosas que nadie quiere y colapsar la bodega.")
        
    with col_finanzas:
        st.success("💰 **Finanzas y Contabilidad**")
        st.write("- **Su objetivo:** Son los guardianes del dinero.")
        st.write("- **Su peor pesadilla:** Tener millones secuestrados en inventario muerto o gastar más de lo que ingresa.")

    st.markdown("---")

    # --- SECCIÓN 4: EL FLUJO (EFECTO DOMINÓ) ---
    st.header("4. Conectando los Puntos: El Flujo del Pensamiento Gerencial")
    st.write("En el mundo real, los problemas no vienen separados por capítulos de un libro. Todo está conectado mediante un efecto dominó. Así es como un gerente estructura su mente para hacer que las áreas trabajen en armonía:")

    # Slider temporal interactivo
    paso = st.select_slider(
        "Desliza para ver cómo avanza el ciclo de la empresa:",
        options=["Paso 1: Diagnóstico", "Paso 2: Foco", "Paso 3: Anticipar", "Paso 4: Traducción"]
    )

    if paso == "Paso 1: Diagnóstico":
        st.markdown("### 🔍 Paso 1: Diagnosticar la Realidad Física (Lo que tenemos y lo que cuesta)")
        st.write("Antes de tomar cualquier decisión de negocios, un gerente debe saber exactamente dónde está parado. Esto empieza en la bodega.")
        st.write("Si tienes productos acumulados por meses sin venderse, la empresa tiene dinero inmovilizado; por el contrario, si te quedas sin stock (quiebre), los clientes reclaman y se van a la competencia. Para arreglar esto, no usas la intuición, usas un historial llamado **Kardex** para entender cómo rota el inventario y crear una política clara.")
        st.write("Al mismo tiempo, debes calcular el **costo real** de ese inventario. El costo de un producto cambia constantemente por mermas, importaciones o errores en el sistema (incluso arrojando 'costos negativos'). Si el gerente de Operaciones no calcula bien cuánto cuesta lo que hay en bodega, cualquier cálculo de ganancias futuras será una mentira.")

    elif paso == "Paso 2: Foco":
        st.markdown("### 🎯 Paso 2: El Poder del Foco (Priorizar Productos y Clientes)")
        st.write("Los recursos de una empresa (tiempo, dinero, vendedores) son limitados. El pensamiento gerencial no consiste en tratar a todos por igual, sino en decidir a qué prestarle atención para maximizar el valor.")
        
        c_prod, c_cli = st.columns(2)
        
        with c_prod:
            st.info("**📦 En los Productos:**")
            st.write("¿Por qué es necesario clasificarlos? Porque no todos los SKU aportan la misma rentabilidad ni tienen la misma rotación.")
            st.write("El desafío gerencial es definir una lógica (como la metodología ABC) que te permita identificar cuáles son los productos 'A' (estratégicos, nunca pueden faltar) frente a los 'C' (posibles candidatos a liquidación para liberar espacio y capital).")
            
        with c_cli:
            st.info("**🤝 En los Clientes:**")
            st.write("¿Por qué clasificar a tus compradores? Porque tu fuerza de ventas y tu tiempo son escasos.")
            st.write("""
            * **B2B (Business-to-Business):** La empresa vende a otras empresas. Aquí la relación es **relacional y técnica**; el cliente busca un aliado a largo plazo, por lo que justifica una atención personalizada y visitas de venta.
            * **B2C (Business-to-Consumer):** La empresa vende directo al consumidor final. Aquí la relación es **transaccional y masiva**; el volumen es clave y la atención suele ser automatizada o digital.
            """)
            st.write("Debes razonar sobre el valor de cada uno: ¿Quién sostiene el flujo de caja hoy? ¿Quién tiene potencial de crecimiento? Esta segmentación permite definir qué clientes justifican una atención personalizada frente a cuáles se gestionan mediante canales digitales.")

    elif paso == "Paso 3: Anticipar":
        st.markdown("### 🔮 Paso 3: Anticipar el Futuro (Planificar para no quebrar)")
        st.write("Una vez que sabes qué productos rotan, cuánto cuestan, cuáles son prioritarios y quiénes son tus mejores clientes, dejas de mirar el pasado y empiezas a proyectar.")
        st.write("El puente entre Ventas y Operaciones se llama **Planificación de Compras**. Basándote en el historial, debes proyectar matemáticamente cuántas unidades vas a vender en los próximos meses. Esta proyección le permite al departamento de Compras invertir el dinero de forma inteligente, asegurando el stock exacto sin ahogar las finanzas de la empresa.")

    elif paso == "Paso 4: Traducción":
        st.markdown("### ⚖️ Paso 4: La Traducción Financiera (El veredicto final)")
        st.write("Todo el esfuerzo comercial y operativo termina en un solo lugar: la contabilidad gerencial.")
        st.write("La contabilidad no es solo para pagar impuestos; es el sistema de información definitivo. Todas tus decisiones de compras, la gestión de tus clientes y los costos de tu bodega se transforman en diarios contables y Estados Financieros.")
        st.write("Aquí, el gerente revisa el Balance, el Estado de Resultados y el Flujo de Efectivo para compararlos contra un presupuesto (por ejemplo, evaluando variaciones contra un escenario 15% menor). El objetivo final de conectar todos estos puntos es poder sentarse frente al directorio y responder con **conclusiones ejecutivas** a las preguntas más importantes: ¿Ganamos o perdimos plata? ¿Tenemos liquidez para sobrevivir? ¿Cuáles son nuestros riesgos?")

    st.markdown("---")

    # --- CIERRE: CONSEJO DE ORO ---
    st.warning("""
    💡 **El Consejo de Oro para este curso:**
    
    Los libros, las fórmulas de Excel o la Inteligencia Artificial pueden entregarte datos o marcos teóricos. Sin embargo, ninguna herramienta toma decisiones por una empresa real. En la vida profesional, los algoritmos no dirigen las compañías; las dirigen personas con **criterio gerencial** capaces de defender sus decisiones considerando el contexto y la realidad de su negocio.
    """)

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
