from pathlib import Path
import streamlit as st
import json
from streamlit_lottie import st_lottie
import base64
from streamlit_player import st_player





#3def carregar_arquivo_lottie(caminho_arquivo: str):
   # with open(caminho_arquivo, "r") as f:
    #    return json.load(f)

# Define o caminho relativo para a pasta pages
pasta_pages = Path("pages")

# Define o caminho do arquivo de animação de fundo
caminho_animation2 = pasta_pages / "animation2.json"

# Carrega o arquivo Lottie da animação de fundo
#animacao_fundo = carregar_arquivo_lottie(caminho_animation2)

# Define a configuração da página antes de fazer qualquer outra chamada do Streamlit
st.set_page_config(layout="wide", page_title="Leste conecta")







st.subheader(':green[LESTE CONECTA]', divider='rainbow')
st.markdown('<h1 style="text-align: ; color: green;">BEM VINDO A PÁGINA INICIAL</h1><br>', unsafe_allow_html=True)


st.sidebar.page_link("pages/comercial.py", label="🛒 COMERCIAL")
st.sidebar.page_link("pages/financeiro.py", label="💲 FINANCEIRO")
st.sidebar.page_link("pages/suporte.py", label="🛠️ SUPORTE")
st.sidebar.page_link("app.py", label="SAIR")
st.sidebar.divider()

col1, col2, col3, col4 = st.columns(4)
with col1:
    #st.header(":orange[CONSULTAR VIABILIDADE]")
    st.write('<h2 style="font-weight:bold; color:">VIABILIDADE</h2>', unsafe_allow_html=True)

    st.link_button("VIABILIDADE", "https://www.lestetelecom.com.br/viabilidade")

with col2:
    #st.header("CONSULTA FAQ")
    st.write('<h2 style="font-weight:bold; color:">FAQ</h2>', unsafe_allow_html=True)

    st.link_button("FAQ - LESTE", "https://www.lestetelecom.com.br/faq")

with col3:
    #st.header("LESTE MOVEL")
    st.write('<h2 style="font-weight:bold; color:">LESTE MÓVEL</h2>', unsafe_allow_html=True)

    st.link_button("IR", "https://www.lestemovel.com.br/")

with col4:
    st.write('<h2 style="font-weight:bold; color:">CHAT-TRANSCRIPTION</h2>', unsafe_allow_html=True)
    st.link_button("APP - Transcrição de Audio", "https://chat-audio.streamlit.app/")       

st.divider()


vd1, vd2, vd3, vd4 = st.columns(4)

with vd1:
   st_player("https://www.youtube.com/shorts/myWMoNbsdDY")

with vd2:
    st_player("https://www.youtube.com/watch?v=5aFnP22GpPI&pp=ygUNbGVzdGUgdGVsZWNvbQ%3D%3D")

with vd3:
    st_player("https://www.youtube.com/watch?v=7mftCZJ86oU&pp=ygUNbGVzdGUgdGVsZWNvbQ%3D%3D")

with vd4:  
    st_player("https://www.youtube.com/watch?v=kpv8CcdXfCc&pp=ygUNbGVzdGUgdGVsZWNvbQ%3D%3D")          
