import streamlit as st

# Configuración de la página
st.set_page_config(page_title="IA y Tipos de Apego", layout="wide")

# Estilos personalizados para la paleta de azules y tipografía
st.markdown("""
    <style>
    .main-title {
        color: #1E3A8A;
        font-size: 45px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        color: #3B82F6;
        font-size: 22px;
        text-align: center;
        font-style: italic;
        margin-bottom: 30px;
    }
    .section-header {
        color: #1D4ED8;
        border-bottom: 2px solid #DBEAFE;
        padding-bottom: 5px;
        margin-top: 20px;
    }
    .content-text {
        font-size: 17px;
        line-height: 1.6;
        text-align: justify;
    }
    .highlight-box {
        background-color: #EFF6FF;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #3B82F6;
    }
    </style>
    """, unsafe_allow_html=True)

# Título Principal y Frase Motivadora
st.markdown('<h1 class="main-title">La Inteligencia Artificial y los Tipos de Apego: ¿Herramienta práctica o refugio emocional?</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">"Entender cómo nos vinculamos con la tecnología es también entender cómo nos vinculamos con nosotros mismos."</p>', unsafe_allow_html=True)

# Introducción
st.markdown('<h2 class="section-header">Introducción</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="content-text">
En la actualidad, la Inteligencia Artificial (IA) ha transformado profundamente la manera en que las personas interactúan con la tecnología. 
Lo que antes era una herramienta puramente funcional, hoy comienza a ocupar un lugar en la vida emocional de los usuarios, simulando compañía y apoyo psicológico. 
Este fenómeno permite comprender cómo establecemos vínculos no solo con otros individuos, sino también con entidades tecnológicas.
</div>
""", unsafe_allow_html=True)

st.write("---")

# Cuerpo del Dashboard en Columnas
col1, col2 = st.columns(2)

with col1:
    st.markdown('<h3 class="section-header">Teoría del Apego y la IA</h3>', unsafe_allow_html=True)
    st.markdown("""
    <div class="content-text">
    Los patrones de relación desarrollados desde la infancia (seguro, ansioso y evitativo) influyen en cómo manejamos la intimidad con sistemas de IA. 
    Estudios sugieren que los usuarios pueden desarrollar apego hacia agentes artificiales cuando estos presentan características humanas o responden de manera empática.
    </div>
    """, unsafe_allow_html=True)
    
    st.info("**Antropomorfización:** Es la tendencia a atribuir características humanas a las máquinas, lo que facilita la creación de vínculos afectivos unilaterales.")

with col2:
    st.markdown('<h3 class="section-header">Uso según Estilos de Apego</h3>', unsafe_allow_html=True)
    st.markdown('<div class="highlight-box">', unsafe_allow_html=True)
    st.markdown("""
    - **Apego Ansioso:** Suelen recurrir a la IA para validación o compañía.
    - **Apego Evitativo:** Prefieren la IA porque permite interactuar sin el riesgo de una conexión emocional profunda.
    - **Uso Predominante:** A pesar de las necesidades emocionales, la mayoría utiliza la IA para tareas académicas o laborales.
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Sección de Conclusión
st.markdown('<h2 class="section-header">¿Relaciones Auténticas o Simuladas?</h2>', unsafe_allow_html=True)
st.warning("La IA carece de una experiencia emocional real, lo que limita la autenticidad de la relación comparada con el vínculo humano basado en reciprocidad y procesos neuronales profundos.")

st.markdown("""
<div class="content-text">
La IA no reemplaza las relaciones humanas, pero sí redefine la manera en que las experimentamos, desdibujando la línea entre herramienta y vínculo.
</div>
""", unsafe_allow_html=True)

# Sidebar con Referencias Seleccionadas
st.sidebar.title("Referencias Clave")
st.sidebar.markdown("""
- **Bao, Z. (2025):** Apego y preferencias por la IA.
- **Hermann, E. (2022):** IA antropomorfizada y consumo.
- **Yang & Oshio (2025):** Marco teórico de la relación humano-IA.
""")
