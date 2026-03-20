import streamlit as st

# Configuración de la página
st.set_page_config(page_title="IA y Tipos de Apego", layout="wide")

# Estilos visuales optimizados (Paleta Azul Marino, Gris y Blanco Suave)
st.markdown("""
    <style>
    /* Fondo principal y color de texto base */
    .stApp {
        background-color: #111827; /* Gris muy oscuro (near-black) */
        color: #F3F4F6; /* Blanco suave */
    }

    /* Título Principal */
    .main-title { 
        color: #60A5FA; /* Azul cielo brillante pero suave */
        font-size: 42px; 
        font-weight: bold; 
        text-align: center; 
        margin-bottom: 5px; 
    }

    /* Frase Subtítulo */
    .subtitle { 
        color: #9CA3AF; /* Gris medio */
        font-size: 20px; 
        text-align: center; 
        font-style: italic; 
        margin-bottom: 40px; 
    }

    /* Cabeceras de Sección */
    .section-header { 
        color: #3B82F6; /* Azul brillante pero saturado */
        border-bottom: 2px solid #1F2937; /* Gris oscuro para separación sutil */
        padding-bottom: 10px; 
        margin-top: 30px; 
        margin-bottom: 20px; 
        font-weight: bold; 
        font-size: 24px; 
    }

    /* Texto de Contenido */
    .content-text { 
        font-size: 17px; 
        line-height: 1.7; 
        text-align: justify; 
        color: #E5E7EB; /* Gris muy claro */
        margin-bottom: 25px; 
    }

    /* Sección de Referencias */
    .ref-section { 
        background-color: #1F2937; /* Gris azulado oscuro (tarjeta) */
        padding: 25px; 
        border-radius: 12px; 
        border: 1px solid #374151; /* Gris medio-oscuro */
        margin-top: 50px; 
    }

    /* Título de Referencias */
    .ref-title { 
        color: #60A5FA; /* Mismo azul que el título principal */
        font-size: 26px; 
        font-weight: bold; 
        margin-bottom: 20px; 
    }
    
    /* Separador Horizontal personalizado */
    hr {
        border-color: #374151;
    }

    /* Color para las negritas dentro de las referencias */
    strong {
        color: #BFDBFE; /* Azul muy pálido */
    }

    </style>
    """, unsafe_allow_html=True)

# Título y Frase (Textual del documento, con los nuevos colores)
st.markdown('<h1 class="main-title">La Inteligencia Artificial y los Tipos de Apego: ¿Herramienta práctica o refugio emocional?</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Entender cómo nos vinculamos con la tecnología es también entender cómo nos vinculamos con nosotros mismos.</p>', unsafe_allow_html=True)

# --- CUERPO DEL ARTÍCULO (TEXTUAL) ---

st.markdown('<div class="section-header">Artículo de divulgación científica</div>', unsafe_allow_html=True)
st.markdown('<div class="content-text">En la actualidad, la Inteligencia Artificial (IA) ha transformado profundamente la manera en que las personas interactúan con la tecnología. Lo que antes era una herramienta puramente funcional, hoy comienza a ocupar un lugar en la vida emocional de los usuarios. Desde asistentes virtuales hasta chatbots conversacionales, la IA no solo responde preguntas, sino que también simula compañía y apoyo psicológico (Xie & Pentina, 2022). Este fenómeno ha despertado el interés de la psicología, particularmente desde la teoría del apego, la cual permite comprender cómo las personas establecen vínculos no solo con otros individuos, sino también con entidades tecnológicas (Yang & Oshio, 2025).</div>', unsafe_allow_html=True)

st.markdown('<div class="section-header">La teoría del apego: base para entender la relación humano-IA</div>', unsafe_allow_html=True)
st.markdown('<div class="content-text">La teoría del apego explica que los seres humanos desarrollan patrones de relación desde la infancia que influyen en su comportamiento emocional en la vida adulta (Levy et al., 2011). Estos estilos, como el apego seguro, ansioso y evitativo, determinan cómo las personas buscan cercanía, manejan la intimidad y regulan sus emociones (Ortiz et al., 2019). En el contexto actual, estos patrones no solo se reflejan en relaciones humanas, sino también en la interacción con sistemas de IA. De hecho, estudios recientes sugieren que los usuarios pueden desarrollar formas de apego hacia agentes artificiales, especialmente cuando estos presentan características humanas o responden de manera empática (Hermann, 2022).</div>', unsafe_allow_html=True)

st.markdown('<div class="section-header">Apego y uso de la IA: entre funcionalidad y necesidad emocional</div>', unsafe_allow_html=True)
st.markdown('<div class="content-text">Las investigaciones muestran que los estilos de apego influyen directamente en la forma en que las personas utilizan la IA. En general, el uso de estas tecnologías puede dividirse en dos grandes categorías: como herramienta práctica o como apoyo emocional. Por un lado, la mayoría de los usuarios tiende a utilizar la IA para actividades funcionales, como resolver tareas académicas, laborales o informativas (Bao, 2025). Este uso práctico predomina incluso en personas que presentan necesidades emocionales. Por otro lado, algunos individuos, especialmente aquellos con apego ansioso, pueden recurrir a la IA como una forma de validación o compañía, desarrollando vínculos emocionales con sistemas conversacionales (Heng & Zhang, 2025). En contraste, las personas con apego evitativo suelen preferir la IA precisamente porque les permite interactuar sin el riesgo de una conexión emocional profunda (Deng et al., 2024).</div>', unsafe_allow_html=True)

st.markdown('<div class="section-header">La construcción de vínculos con la IA</div>', unsafe_allow_html=True)
st.markdown('<div class="content-text">El desarrollo de relaciones con la IA está estrechamente relacionado con el fenómeno de la antropomorfización, es decir, la tendencia a atribuir características humanas a las máquinas. Cuando un sistema parece “comprender” emociones o responder de forma empática, los usuarios pueden comenzar a percibirlo como un agente social (Hermann, 2022). Este proceso facilita la creación de vínculos afectivos, aunque estos sean unilaterales. Estudios han demostrado que algunas personas llegan a experimentar apego emocional hacia chatbots, compartiendo información personal y estableciendo dinámicas similares a las relaciones humanas (Pentina et al., 2023). Sin embargo, estos vínculos presentan una paradoja: aunque la IA puede simular cercanía, carece de una experiencia emocional real, lo que limita la autenticidad de la relación.</div>', unsafe_allow_html=True)

st.markdown('<div class="section-header">¿Relaciones auténticas o simuladas?</div>', unsafe_allow_html=True)
st.markdown('<div class="content-text">A pesar de los avances tecnológicos, la IA aún no puede replicar completamente la complejidad del vínculo humano. Las relaciones humanas están construidas sobre experiencias compartidas, reciprocidad emocional y contexto, elementos que la IA no puede experimentar genuinamente (Berendzen, 2023). Desde la psicobiología del apego, el vínculo implica procesos neuronales y emocionales profundos que difícilmente pueden ser reemplazados por una interacción artificial (Lahousen et al., 2019). Por ello, aunque la IA puede funcionar como un apoyo complementario, especialmente en momentos de soledad o estrés, no sustituye la necesidad de relaciones humanas auténticas.</div>', unsafe_allow_html=True)

st.markdown('<div class="section-header">La relación mutua: importancia</div>', unsafe_allow_html=True)
st.markdown('<div class="content-text">La relación entre los tipos de apego y el uso de la Inteligencia Artificial revela que la tecnología no es neutral: interactúa con nuestras emociones, necesidades y formas de vincularnos. La evidencia sugiere que, aunque la IA tiene el potencial de convertirse en un recurso emocional, su uso sigue siendo predominantemente práctico (Bao, 2025). Sin embargo, ciertos perfiles, especialmente aquellos con inseguridad en el apego, pueden desarrollar vínculos más profundos con estas tecnologías. En este sentido, la IA no reemplaza las relaciones humanas, pero sí redefine la manera en que las experimentamos. Nos enfrenta a un escenario donde la línea entre herramienta y vínculo comienza a desdibujarse, obligándonos a cuestionar qué significa realmente conectar en la era digital.</div>', unsafe_allow_html=True)

# --- APARTADO DE REFERENCIAS (Con fondo y texto optimizado) ---

st.markdown('<div class="ref-section">', unsafe_allow_html=True)
st.markdown('<p class="ref-title">REFERENCIAS Y RESÚMENES</p>', unsafe_allow_html=True)

referencias_data = [
    ["Bao, Z. (2025). Attachment Styles and Preferences for AI: Practical Tool or Emotional Support? Journal of Global Research in Education and Social Science. 19(2), 71-80.", "El artículo analiza cómo los estilos de apego influyen en el uso de la inteligencia artificial como herramienta emocional. Con un enfoque mixto (encuestas y entrevistas a 100 participantes), se evaluó el uso práctico y el apoyo emocional mediante escalas específicas. Además, se busca entender si factores como la ansiedad o la evitación en las relaciones humanas afectan la forma en que los usuarios se vinculan con la IA y qué tipo de asistencia buscan en ella."],
    ["Berendzen, K. (2023). Understanding social attachment as a window into the neural basis of prosocial behavior. Frontiers in Neurology. 14.", "El potencial de las conductas de apego para servir como indicadores en otras especies de los componentes de las conductas basadas desde el desarrollo temprano en la niñez. El artículo explora el apego desde una perspectiva neurocientífica, explicando cómo los vínculos sociales están relacionados con procesos cerebrales que promueven conductas prosociales. Destaca la importancia del apego en la regulación emocional y en la formación de relaciones significativas."],
    ["Deng, S., Zhang, J., Lin, Z., y Li, X. (2024). Service staff makes me nervous: Exploring the impact of insecure attachment on AI service preference. Technological Forecasting and Social Change. 198.", "Investiga cómo el apego inseguro influye en la preferencia por servicios de IA en lugar de interacción humana. Los resultados muestran que las personas con apego evitativo o ansioso pueden sentirse incómodas con humanos y prefieren interactuar con IA por percibirla como menos amenazante."],
    ["Hermann, E. (2022). Anthropomorphized artificial intelligence, attachment, and consumer behavior. 33(1). Marketing Letters. 157-162.", "Estudia el impacto de la antropomorfización en la IA, es decir, cuando las máquinas parecen humanas. Concluye que esto facilita la formación de apego emocional y puede influir en el comportamiento del consumidor. Sostiene que la creciente humanización y capacidad emocional de las aplicaciones de inteligencia artificial puede fomentar el apego de los consumidores hacia la IA, transformando la interacción en algo similar a una relación humano-humano."],
    ["Lahousen, T., Unterrainer, H., y Kapfhammer, H. (2019). Frontiers in Psychiatry. 10", "Aborda la psicobiología del apego y el trauma desde una perspectiva clínica. Explica cómo los patrones de apego afectan la regulación emocional y la salud mental, aportando bases teóricas para entender relaciones humanas y tecnológicas. El patrón de apego adquirido está íntimamente ligado a la capacidad de empatía y mentalización del niño en crecimiento, ambas habilidades psicológicas que determinarán sus futuras relaciones."],
    ["Levy, K., Ellison, W., Scott, L., y Bernecker, S. (2011). Attachment Style. 67(2). Journal of Clinical Psychology. 193-203.", "Proporciona una revisión general del concepto de estilos de apego en adultos, explicando sus características y cómo influyen en la personalidad, las relaciones y la psicopatología. Análisis de estudios y experimentos realizados para encontrar relación entre los tipos de apego entre géneros y edad."],
    ["Ortiz, D., Acosta, P., Rubio, D., Martínez, N,. Del Valle, M., Caden, D., López, E., Hinojosa, F., y Ramos, C. (2019). Consideraciones teóricas acerca del apego en adultos. Avances en Psicología. 27(2). 135-152.", "investiga cómo los estilos de apego de las personas influyen en si utilizan la Inteligencia Artificial (IA) como una herramienta práctica o como apoyo emocional. Los hallazgos principales indican que la mayoría de los usuarios prefieren la IA para tareas funcionales, como la recuperación de información y asistencia en el trabajo o estudio, por encima del soporte emocional. determina con qué frecuencia se utiliza la tecnología. Finalmente, el autor sugiere que la falta de empatía auténtica en las herramientas actuales (como ChatGPT y Siri) limita su capacidad para satisfacer necesidades psicológicas profundas, reforzando su rol como asistentes utilitarios-"],
    ["Pentina, I., Hancock, T., y Xie, T. (2023). Exploring relationship development with social chatbots: A mixed-method study of replica. Computers in Human Behavior. 140.", "Estudia cómo las personas desarrollan relaciones con chatbots sociales como Replika. Encuentra que los usuarios pueden generar vínculos emocionales reales, incluyendo confianza y auto-revelación. Propone y prueba un modelo de desarrollo de la relación humano-IA en chatbots sociales. Integra teorías de interacción humano-computadora —como Computers Are Social Actors , presencia social percibida e interacción parasocial— con teorías interpersonales como la penetración social y el apego."],
    ["Pentina, I., y Xie, T. (2022). Attachment Theory as a Framework to Understand Relationships with Social Chatbots: A Case Study of Replika.", "Explora cómo se forman vínculos con chatbots sociales como Replika, especialmente durante los confinamientos por la pandemia. A partir de entrevistas en profundidad y desde la teoría del apego, se encontró que, en contextos de soledad y malestar emocional, las personas pueden desarrollar apego hacia estos agentes si perciben apoyo, seguridad y contención emocional. Aplica la teoría del apego para explicar las relaciones con chatbots sociales. Sugiere que las personas pueden desarrollar vínculos similares a los humanos con estos sistemas."],
    ["Yang, F., y Oshio, A. (2025). Using attachment theory to conceptualize and measure the experiences in human-AI relationships. Current Psychology. 44(11). 10658-10669.", "El artículo examina si la teoría del apego puede aplicarse a las relaciones entre personas e inteligencia artificial generativa. A través de varios estudios, propone que estas interacciones pueden entenderse mediante dos dimensiones: ansiedad de apego (búsqueda de reafirmación y miedo a respuestas insuficientes) y evitación (incomodidad con la cercanía emocional). Propone un marco teórico para medir experiencias en relaciones humano-IA desde la teoría del apego, destacando la relevancia de estos vínculos en la era digital."]
]

for ref, res in referencias_data:
    st.markdown(f"**Referencia:** {ref}")
    st.markdown(f"**Resumen:** {res}")
    st.markdown("---")

st.markdown('</div>', unsafe_allow_html=True)
