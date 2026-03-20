import streamlit as st

# Configuración de la página
st.set_config(page_title="IA & Apego", layout="wide")

# CSS Avanzado para un diseño creativo y moderno
st.markdown("""
    <style>
    /* Fondo con gradiente sutil */
    .stApp {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
        color: #e2e8f0;
    }

    /* Título con resplandor neón */
    .main-title {
        font-family: 'Helvetica Neue', sans-serif;
        color: #60a5fa;
        font-size: 50px;
        font-weight: 800;
        text-align: center;
        text-shadow: 0px 0px 15px rgba(96, 165, 250, 0.4);
        margin-bottom: 5px;
        line-height: 1.2;
    }

    .subtitle {
        color: #94a3b8;
        font-size: 22px;
        text-align: center;
        font-style: italic;
        margin-bottom: 50px;
        letter-spacing: 1px;
    }

    /* Tarjetas de contenido */
    .content-card {
        background-color: rgba(30, 41, 59, 0.7);
        border: 1px solid #334155;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
        margin-bottom: 30px;
        transition: transform 0.3s ease;
    }
    
    .content-card:hover {
        border-color: #3b82f6;
        transform: translateY(-5px);
    }

    .section-header {
        color: #3b82f6;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
    }

    .section-header::before {
        content: "◈";
        margin-right: 10px;
        color: #60a5fa;
    }

    .text-body {
        font-size: 17px;
        line-height: 1.8;
        text-align: justify;
        color: #cbd5e1;
    }

    /* Estilo para Referencias */
    .ref-container {
        border-left: 4px solid #3b82f6;
        background: rgba(59, 130, 246, 0.05);
        padding: 20px;
        margin-bottom: 20px;
        border-radius: 0 15px 15px 0;
    }

    .ref-text {
        font-size: 14px;
        color: #94a3b8;
    }

    .resumen-text {
        font-size: 15px;
        color: #f1f5f9;
        margin-top: 10px;
    }

    /* Badge creativo */
    .badge {
        background: #1e40af;
        color: #bfdbfe;
        padding: 4px 12px;
        border-radius: 50px;
        font-size: 12px;
        font-weight: bold;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# Encabezado Impactante
st.markdown('<h1 class="main-title">La Inteligencia Artificial y los Tipos de Apego</h1>', unsafe_allow_html=True)
st.markdown('<h1 style="color:#3b82f6; font-size:30px; text-align:center; margin-top:-20px;">¿Herramienta práctica o refugio emocional?</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">"Entender cómo nos vinculamos con la tecnología es también entender cómo nos vinculamos con nosotros mismos."</p>', unsafe_allow_html=True)

# Layout de columnas para métricas visuales rápidas
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div style="text-align:center; background:rgba(59,130,246,0.1); padding:20px; border-radius:15px; border:1px solid #3b82f6;">'
                '<h2 style="margin:0; color:#60a5fa;">Psicología</h2><p style="margin:0; color:#94a3b8;">Teoría del Apego</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div style="text-align:center; background:rgba(59,130,246,0.1); padding:20px; border-radius:15px; border:1px solid #3b82f6;">'
                '<h2 style="margin:0; color:#60a5fa;">Tecnología</h2><p style="margin:0; color:#94a3b8;">IA Generativa</p></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div style="text-align:center; background:rgba(59,130,246,0.1); padding:20px; border-radius:15px; border:1px solid #3b82f6;">'
                '<h2 style="margin:0; color:#60a5fa;">Vínculo</h2><p style="margin:0; color:#94a3b8;">Antropomorfización</p></div>', unsafe_allow_html=True)

st.write("---")

# Secciones del Artículo en Tarjetas
def create_card(title, content):
    st.markdown(f"""
    <div class="content-card">
        <div class="section-header">{title}</div>
        <div class="text-body">{content}</div>
    </div>
    """, unsafe_allow_html=True)

create_card("Artículo de divulgación científica", 
            "En la actualidad, la Inteligencia Artificial (IA) ha transformado profundamente la manera en que las personas interactúan con la tecnología. Lo que antes era una herramienta puramente funcional, hoy comienza a ocupar un lugar en la vida emocional de los usuarios. Desde asistentes virtuales hasta chatbots conversacionales, la IA no solo responde preguntas, sino que también simula compañía y apoyo psicológico (Xie & Pentina, 2022). Este fenómeno ha despertado el interés de la psicología, particularmente desde la teoría del apego, la cual permite comprender cómo las personas establecen vínculos no solo con otros individuos, sino también con entidades tecnológicas (Yang & Oshio, 2025).")

create_card("La teoría del apego: base para entender la relación humano-IA", 
            "La teoría del apego explica que los seres humanos desarrollan patrones de relación desde la infancia que influyen en su comportamiento emocional en la vida adulta (Levy et al., 2011). Estos estilos, como el apego seguro, ansioso y evitativo, determinan cómo las personas buscan cercanía, manejan la intimidad y regulan sus emociones (Ortiz et al., 2019). En el contexto actual, estos patrones no solo se reflejan en relaciones humanas, sino también en la interacción con sistemas de IA. De hecho, estudios recientes sugieren que los usuarios pueden desarrollar formas de apego hacia agentes artificiales, especialmente cuando estos presentan características humanas o responden de manera empática (Hermann, 2022).")

# Uso de columnas para equilibrar la lectura en la sección media
col_a, col_b = st.columns(2)
with col_a:
    create_card("Apego y uso de la IA", 
                "Las investigaciones muestran que los estilos de apego influyen directamente en la forma en que las personas utilizan la IA. En general, el uso de estas tecnologías puede dividirse en dos grandes categorías: como herramienta práctica o como apoyo emocional. Por un lado, la mayoría de los usuarios tiende a utilizar la IA para actividades funcionales, como resolver tareas académicas, laborales o informativas (Bao, 2025).")
with col_b:
    create_card("Construcción de vínculos", 
                "El desarrollo de relaciones con la IA está estrechamente relacionado con el fenómeno de la antropomorfización. Cuando un sistema parece “comprender” emociones o responder de forma empática, los usuarios pueden comenzar a percibirlo como un agente social (Hermann, 2022). Este proceso facilita la creación de vínculos afectivos, aunque estos sean unilaterales.")

create_card("¿Relaciones auténticas o simuladas?", 
            "A pesar de los avances tecnológicos, la IA aún no puede replicar completamente la complejidad del vínculo humano. Las relaciones humanas están construidas sobre experiencias compartidas, reciprocidad emocional y contexto, elementos que la IA no puede experimentar genuinamente (Berendzen, 2023). Desde la psicobiología del apego, el vínculo implica procesos neuronales y emocionales profundos que difícilmente pueden ser reemplazados por una interacción artificial (Lahousen et al., 2019).")

create_card("La relación mutua: importancia", 
            "La relación entre los tipos de apego y el uso de la Inteligencia Artificial revela que la tecnología no es neutral: interactúa con nuestras emociones, necesidades y formas de vincularnos. En este sentido, la IA no reemplaza las relaciones humanas, pero sí redefine la manera en que las experimentamos. Nos enfrenta a un escenario donde la línea entre herramienta y vínculo comienza a desdibujarse.")

# Sección de Referencias Creativa
st.markdown('<h2 style="color:#60a5fa; text-align:center; margin-top:50px;">📚 Repositorio de Referencias Académicas</h2>', unsafe_allow_html=True)

referencias = [
    ("Bao, Z. (2025)", "Attachment Styles and Preferences for AI: Practical Tool or Emotional Support?", "Análisis de cómo la ansiedad o evitación afectan el vínculo con la IA."),
    ("Berendzen, K. (2023)", "Understanding social attachment as a window into the neural basis of prosocial behavior.", "Explora el apego desde una perspectiva neurocientífica y procesos cerebrales."),
    ("Deng, S. et al. (2024)", "Exploring the impact of insecure attachment on AI service preference.", "Preferencia de servicios de IA en personas con apego inseguro por ser menos amenazantes."),
    ("Hermann, E. (2022)", "Anthropomorphized artificial intelligence, attachment, and consumer behavior.", "Impacto de la humanización de las máquinas en el comportamiento del consumidor.")
]

for autor, titulo, resumen in referencias:
    st.markdown(f"""
    <div class="ref-container">
        <span class="badge">Fuente Académica</span>
        <div style="font-weight:bold; color:#60a5fa; margin-top:10px;">{autor}</div>
        <div class="ref-text"><i>{titulo}</i></div>
        <div class="resumen-text">{resumen}</div>
    </div>
    """, unsafe_allow_html=True)
