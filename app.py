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
# PESTAÑA 2: PORTAFOLIO DE MISIONES (CRONOLÓGICO Y CON CONCEPTOS INTEGRADOS)
# ==========================================
with tab2:
    st.header("🚀 Portafolio de Misiones: Ruta de Aprendizaje Progresiva")
    st.write("Demuestra tu progreso gerencial completando las misiones en orden para desbloquear las siguientes etapas del ciclo empresarial.")

    # 1. Inicializar la memoria de progreso si no existe
    if "nivel_progreso" not in st.session_state:
        st.session_state.nivel_progreso = 1  # Parte en la Misión 1

    # Barra de progreso visual según el nivel actual
    progreso_porcentaje = int((st.session_state.nivel_progreso - 1) / 5 * 100)
    st.progress(min(progreso_porcentaje, 100))
    st.write(f"**Tu Progreso Actual:** Nivel {st.session_state.nivel_progreso} de 6")
    st.markdown("---")

    # 2. Botones de navegación horizontal (Tu idea original intacta)
    col_m1, col_m2, col_m3, col_m4, col_m5, col_m7 = st.columns(6)
    
    with col_m1:
        m1_click = st.button("📦 Misión 1", use_container_width=True)
    with col_m2:
        m2_click = st.button("📊 Misión 2", disabled=(st.session_state.nivel_progreso < 2), use_container_width=True)
    with col_m3:
        m3_click = st.button("🔮 Misión 3", disabled=(st.session_state.nivel_progreso < 3), use_container_width=True)
    with col_m4:
        m4_click = st.button("🤝 Misión 4", disabled=(st.session_state.nivel_progreso < 4), use_container_width=True)
    with col_m5:
        m5_click = st.button("⚙️ Misión 5", disabled=(st.session_state.nivel_progreso < 5), use_container_width=True)
    with col_m7:
        m7_click = st.button("⚖️ Misión 7", disabled=(st.session_state.nivel_progreso < 6), use_container_width=True)

    # Definir qué misión mostrar en pantalla
    if "mision_activa" not in st.session_state:
        st.session_state.mision_activa = "Misión 1"

    if m1_click: st.session_state.mision_activa = "Misión 1"
    if m2_click: st.session_state.mision_activa = "Misión 2"
    if m3_click: st.session_state.mision_activa = "Misión 3"
    if m4_click: st.session_state.mision_activa = "Misión 4"
    if m5_click: st.session_state.mision_activa = "Misión 5"
    if m7_click: st.session_state.mision_activa = "Misión 7"

    st.markdown("---")

    # 3. Contenido de las misiones estructurado con los conceptos de la rúbrica
    if st.session_state.mision_activa == "Misión 1":
        st.subheader("📦 Misión 1: Gestión de Inventario y Kardex")
        
        # Ficha de Contexto con conceptos explícitos
        c1, c2, c3 = st.columns(3)
        c1.markdown("**🎯 Objetivo:** Determinar la velocidad con la que rota el **inventario** físico.")
        c2.markdown("**⚠️ Problema Trabajado:** Desbalance en bodega; convivencia de productos estancados junto con quiebres de stock.")
        c3.markdown("**🛠️ Herramientas:** Planillas de cálculo y análisis de **datos** históricos de movimientos.")
        
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🧠 Conceptos Aprendidos y Valor")
            st.write("Descubrimos que el **inventario** es capital inmovilizado. Aprendimos que el **abastecimiento** eficiente no se decide por intuición, sino analizando el historial operativo de la bodega para asegurar la continuidad del negocio.")
        with col2:
            st.markdown("### 🛠️ Dificultades, Aprendizaje Clave y Uso Futuro")
            st.error("**Dificultad:** Enfrentar bases de datos imperfectas y conciliar las presiones entre ventas y finanzas.")
            st.success("**Aprendizaje Clave y Uso Futuro:** Equilibrar el nivel de servicio con la inversión. En el futuro, usaremos estos **datos** para diseñar políticas óptimas de reposición de mercadería.")
        
        if st.session_state.nivel_progreso == 1:
            if st.button("✅ Comprender Diagnóstico y Desbloquear Misión 2 🔓"):
                st.session_state.nivel_progreso = 2
                st.session_state.mision_activa = "Misión 2"
                st.rerun()

    elif st.session_state.mision_activa == "Misión 2":
        st.subheader("📊 Misión 2: Clasificación ABC, Costos e Importaciones")
        
        # Ficha de Contexto
        c1, c2, c3 = st.columns(3)
        c1.markdown("**🎯 Objetivo:** Jerarquizar el catálogo analizando **costos** e **importaciones**.")
        c2.markdown("**⚠️ Problema Trabajado:** Pérdida de recursos al gestionar todos los productos con la misma prioridad operativa.")
        c3.markdown("**🛠️ Herramientas:** Clasificación de Pareto aplicada a la estructura de **costos** de adquisición.")
        
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🧠 Conceptos Aprendidos y Valor")
            st.write("Aprendimos que en la gestión de **importaciones**, los **costos** logísticos y de aduana impactan directamente en los **márgenes** de contribución de cada SKU. Clasificar los productos nos permite cuidar la rentabilidad.")
        with col2:
            st.markdown("### 🛠️ Dificultades, Aprendizaje Clave y Uso Futuro")
            st.error("**Dificultad:** Prorratear correctamente los gastos asociados a traer contenedores desde el extranjero.")
            st.success("**Aprendizaje Clave y Uso Futuro:** Proteger los **márgenes** del negocio. Utilizaremos esto para auditar y priorizar las compras de los artículos más valiosos para la empresa.")
        
        if st.session_state.nivel_progreso == 2:
            if st.button("✅ Definir Foco de Productos y Desbloquear Misión 3 🔓"):
                st.session_state.nivel_progreso = 3
                st.session_state.mision_activa = "Misión 3"
                st.rerun()

    elif st.session_state.mision_activa == "Misión 3":
        st.subheader("🔮 Misión 3: Planificación Integrada de la Demanda")
        
        # Ficha de Contexto
        c1, c2, c3 = st.columns(3)
        c1.markdown("**🎯 Objetivo:** Estimar la demanda futura mediante modelos de **planificación**.")
        c2.markdown("**⚠️ Problema Trabajado:** Incertidumbre comercial que causa compras excesivas o faltantes de stock.")
        c3.markdown("**🛠️ Herramientas:** Modelos de proyección matemática y presupuestos de **abastecimiento**.")
        
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🧠 Conceptos Aprendidos y Valor")
            st.write("El gran valor fue entender la **planificación** integrada. Sirve como el puente definitivo para alinear las metas de ventas de la empresa con el presupuesto asignado para el **abastecimiento** de productos.")
        with col2:
            st.markdown("### 🛠️ Dificultades, Aprendizaje Clave y Uso Futuro")
            st.error("**Dificultad:** Mitigar riesgos de quiebre sin inmovilizar el capital de trabajo de la firma.")
            st.success("**Aprendizaje Clave y Uso Futuro:** Sincronizar periódicamente las áreas operativas. En el futuro, aplicaremos esta **planificación** para optimizar la rotación y proteger la caja corporativa.")
        
        if st.session_state.nivel_progreso == 3:
            if st.button("✅ Validar Planificación de Compras y Desbloquear Misión 4 🔓"):
                st.session_state.nivel_progreso = 4
                st.session_state.mision_activa = "Misión 4"
                st.rerun()

    elif st.session_state.mision_activa == "Misión 4":
        st.subheader("🤝 Misión 4: Gestión de Clientes, Propuestas e IA")
        
        # Ficha de Contexto
        c1, c2, c3 = st.columns(3)
        c1.markdown("**🎯 Objetivo:** Clasificar la cartera y diseñar **propuestas** comerciales estratégicas.")
        c2.markdown("**⚠️ Problema Trabajado:** Dispersión del equipo de ventas al atender todas las cuentas con el mismo esfuerzo.")
        c3.markdown("**🛠️ Herramientas:** Modelos de segmentación y copilotos de Inteligencia Artificial (**IA**).")
        
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🧠 Conceptos Aprendidos y Valor")
            st.write("Utilizamos Inteligencia Artificial (**IA**) para acelerar el análisis y construir **propuestas** de valor personalizadas para clientes relacionales (B2B) y transaccionales (B2C), optimizando el tiempo comercial.")
        with col2:
            st.markdown("### 🛠️ Dificultades, Aprendizaje Clave y Uso Futuro")
            st.error("**Dificultad:** Mantener el criterio humano y ético al evaluar las ideas entregadas por la **IA**.")
            st.success("**Aprendizaje Clave y Uso Futuro:** La tecnología potencia la estrategia. Usaremos herramientas de **IA** en nuestro futuro profesional para formular **propuestas** competitivas en tiempo récord.")
        
        if st.session_state.nivel_progreso == 4:
            if st.button("✅ Segmentar Cartera Comercial y Desbloquear Misión 5 🔓"):
                st.session_state.nivel_progreso = 5
                st.session_state.mision_activa = "Misión 5"
                st.rerun()

    elif st.session_state.mision_activa == "Misión 5":
        st.subheader("⚙️ Misión 5: Costos, Sueldos y Cotizaciones")
        
        # Ficha de Contexto
        c1, c2, c3 = st.columns(3)
        c1.markdown("**🎯 Objetivo:** Auditar las planillas de **costos**, **sueldos** y gastos del periodo.")
        c2.markdown("**⚠️ Problema Trabajado:** Desfases e inconsistencias en la valorización contable de la operación.")
        c3.markdown("**🛠️ Herramientas:** Modelos de remuneraciones, libros de **sueldos** y retenciones legales.")
        
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🧠 Conceptos Aprendidos y Valor")
            st.write("Comprendimos el impacto financiero de los **sueldos** y sus respectivas **cotizaciones** previsionales sobre los **costos** operativos fijos. Validar estas planillas asegura que los márgenes reportados sean reales.")
        with col2:
            st.markdown("### 🛠️ Dificultades, Aprendizaje Clave y Uso Futuro")
            st.error("**Dificultad:** Aplicar con exactitud la normativa provisional y legal vigente de las **cotizaciones**.")
            st.success("**Aprendizaje Clave y Uso Futuro:** El control estricto de egresos. Usaremos este conocimiento para estructurar presupuestos de personal y controlar los **costos** reales de una organización.")
        
        if st.session_state.nivel_progreso == 5:
            if st.button("✅ Auditar Costos de Bodega y Desbloquear Misión FINAL 🔓"):
                st.session_state.nivel_progreso = 6
                st.session_state.mision_activa = "Misión 7"
                st.rerun()

    elif st.session_state.mision_activa == "Misión 7":
        st.subheader("⚖️ Misión 7: Estados Financieros y Visualización Ejecutiva")
        
        # Ficha de Contexto
        c1, c2, c3 = st.columns(3)
        c1.markdown("**🎯 Objetivo:** Traducir los registros en informes y herramientas de **visualización** gerencial.")
        c2.markdown("**⚠️ Problema Trabajado:** Libros contables dispersos que impiden ver la salud financiera global de la firma.")
        c3.markdown("**🛠️ Herramientas:** Balance, Estado de Resultados y diseño de dashboards para **visualización** de datos.")
        
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🧠 Conceptos Aprendidos y Valor")
            st.write("Aprendimos a conectar la operación con la estrategia financiera. Logramos estructurar informes claros combinando el análisis de **datos** con técnicas modernas de **visualización** para la toma de decisiones rápidas.")
        with col2:
            st.markdown("### 🛠️ Dificultades, Aprendizaje Clave y Uso Futuro")
            st.error("**Dificultad:** Presentar la información financiera de forma atractiva y legible para un Directorio.")
            st.success("**Aprendizaje Clave y Uso Futuro:** La transparencia directiva. En el futuro, utilizaremos la **visualización** interactiva de **datos** financieros para rendir cuentas claras ante inversionistas y gerentes.")
        
        if st.session_state.nivel_progreso == 6:
            st.balloons()
            st.success("🎉 ¡Felicidades! Has completado el ciclo completo del Pensamiento Gerencial. Estás listo para revisar la 'Reflexión Final'.")
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