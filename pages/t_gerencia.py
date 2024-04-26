import json
import streamlit as st
from streamlit_lottie import st_lottie
from pathlib import Path

# Função para carregar o arquivo Lottie do caminho local
def carregar_arquivo_lottie(caminho_arquivo: str):
    with open(caminho_arquivo, "r") as f:
        return json.load(f)

# Define o caminho relativo para a pasta pages
pasta_pages = Path("pages")

# Define o caminho do arquivo de animação de fundo
caminho_animation2 = pasta_pages / "animation2.json"

# Carrega o arquivo Lottie da animação de fundo
animacao_fundo = carregar_arquivo_lottie(caminho_animation2)

# Define a configuração da página antes de fazer qualquer outra chamada do Streamlit
st.set_page_config(layout="wide", page_title="Leste conecta")

# Adiciona o estilo CSS para aplicar a animação como plano de fundo
st.markdown(
    f"""
    <style>
        .background-container {{
            background-image: url('data:image/svg+xml;base64,{animacao_fundo}');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
        }}
    </style>
    """
    ,unsafe_allow_html=True
)

# Define o conteúdo da página dentro do elemento de contêiner
with st.container() as conteudo:
    # Seu conteúdo Streamlit normal aqui...
    st.subheader(':green[LESTE CONECTA]', divider='rainbow')
    st.markdown('<h1 style="text-align: center; color: green;">PROCEDIMENTOS - COMERCIAL</h1><br>', unsafe_allow_html=True)
    
    st.header('teste de acesso Gerência')
    st.sidebar.page_link("app.py", label="DELOGAR")

    # Carrega e exibe outras animações Lottie
    def load_and_display_lottie(filepath):
        lottie_data = carregar_arquivo_lottie(filepath)
        st_lottie(lottie_data, speed=1, reverse=False, loop=True, quality="low", height=400, width=400)

    # Exibe outras animações Lottie
    load_and_display_lottie(pasta_pages / "animation.json")
    load_and_display_lottie(pasta_pages / "animation2.json")
