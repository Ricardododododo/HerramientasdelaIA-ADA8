import streamlit as st

# 1. CORRECCIÓN: El nombre correcto es set_page_config
st.set_page_config(page_title="IA & Apego Emocional", layout="wide")

# Diseño CSS Avanzado y Creativo
st.markdown("""
    <style>
    /* Fondo General Profundo */
    .stApp {
        background: radial-gradient(circle, #1e293b 0%, #0f172a 100%);
        color: #f8fafc;
    }

    /* Título con Degradado Moderno */
    .hero-title {
        background: -webkit-linear-gradient(#60a5fa, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 55px;
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

    /* Tarjetas de Vidrio (Glassmorphism) */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 30px;
        border-radius: 24px;
        margin-bottom: 25px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
    }

    .section-label {
        color: #60a5fa;
        text-transform: uppercase;
        font-weight: bold;
        font-size: 13px;
        letter-spacing: 2px;
        margin-bottom: 10px;
        display: block;
    }

    .section-title {
        color: #ffffff;
        font-size: 26px;
        font-weight: 700;
        margin-bottom: 15px;
    }

    .text-body {
        font-size: 17px;
        line-height: 1.8;
        text-align: justify;
        color: #cbd5e1;
    }

    /* Estilo de Referencias */
    .ref-box {
        border-left: 3px solid #3b82f6;
        padding-left: 20px;
        margin-bottom: 30px;
    }
    
    .ref-meta {
        color: #60a5fa;
        font-weight: 600;
        font-size: 14px;
    }

    /* Animación simple */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .animate { animation: fadeIn 0.8s ease-out; }
    </style>
    """, unsafe_allow_html=True)

# Barra Lateral de Navegación
with st.sidebar:
    st.markdown("<h2 style='color:#60a5fa;'>Navegación</h2>", unsafe_allow_html=True)
    menu = st.radio("Ir a la sección:", [
        "Inicio
