import streamlit as st

# Configuración inicial
st.set_page_config(page_title="IA & Apego Emocional", layout="wide")

# CSS para un diseño creativo, coherente y fácil de leer
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, #1e293b 0%, #0f172a 100%);
        color: #f8fafc;
    }
    .hero-title {
        background: -webkit-linear-gradient(#60a5fa, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 48px;
        font-weight: 900;
        text-align: center;
        margin-bottom: 0px;
    }
    .hero-subtitle {
        color: #94a3b8;
        font-size: 19px;
        text-align: center;
        font-style: italic;
        margin-bottom: 40px;
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 30px;
        border-radius: 20px;
        margin-bottom: 25px;
    }
    .section-title {
        color: #60a5fa;
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 15px;
        border-left: 4px solid #3b82f6;
        padding-left: 15px;
    }
    .text-body {
        font-size: 17px;
        line-height: 1.8;
        text-align: justify;
        color: #cbd5e1;
    }
    .ref-box {
        background: rgba(59, 130, 246, 0.05);
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 15px;
        border: 1px solid rgba(59, 130, 246, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# Título y subtítulo
st.markdown('<h1 class="hero-title">La Inteligencia Artificial y los Tipos de Apego</h1>', unsafe_allow_html=True)
st.markdown('<h2 style="color:#3b82f6; text-align:center; font-size:28px;">¿Herramienta práctica o refugio emocional?</h2>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Entender cómo nos vinculamos con la tecnología es también entender cómo nos vinculamos con nosotros mismos.</p>', unsafe_allow_html=True)

# Contenido del Artículo (Copia
