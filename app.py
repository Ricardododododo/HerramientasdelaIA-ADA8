import streamlit as st

# Configuración de página
st.set_page_config(page_title="IA y Tipos de Apego", layout="wide")

# CSS para diseño creativo y coherencia visual
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, #1e293b 0%, #0f172a 100%);
        color: #f8fafc;
    }
    .main-title {
        background: -webkit-linear-gradient(#60a5fa, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 50px;
        font-weight: 900;
        text-align: center;
        margin-bottom: 0px;
    }
    .hero-subtitle {
        color: #94a3b8;
        font-size: 20px;
        text-align: center;
        font-style: italic;
        margin-bottom: 40px;
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 30px;
        border-radius: 24px;
        margin-bottom: 25px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }
    .section-header {
        color: #60a5fa;
        font-size: 26px;
        font-weight: 700;
        margin-bottom: 15px;
        border-left: 5px solid #3b82f6;
        padding-left: 15px;
    }
    .content-body {
        font-size: 17px;
        line-height: 1.8;
        text-align: justify;
        color: #cbd5e1;
    }
    .ref-container {
        background: rgba(59, 130, 246, 0.05);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid rgba(59, 130, 246, 0.2);
        margin-bottom: 20px;
    }
    .ref-title {
        color: #60a5fa;
        font-weight: bold;
        font-size: 16px;
        margin-bottom: 8px;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

# Encabezado principal
