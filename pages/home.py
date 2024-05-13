from pathlib import Path
import streamlit as st
import json
from streamlit_lottie import st_lottie
import base64

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




#bg = """
#<style> 
#[data-testid="stAppViewContainer"]{
#background-image: url('https://img.freepik.com/fotos-gratis/fone-de-ouvido-de-audio-usado-por-agentes-de-call-center-para-atender-clientes-e-fazer-telecomunicacoes-com-tecnologia-estacao-de-trabalho-de-atendimento-ao-cliente-vazia-com-fones-de-ouvido-computadores-e-aparelhos-modernos_482257-40834.jpg?size=626&ext=jpg&ga=GA1.1.2082370165.1711238400&semt=ais');
#background-size: cover;
#}
#</style>

#"""

#st.markdown(bg, unsafe_allow_html=True)

# ANIMAÇÕES

#def load_and_display_lottie(filepath):
#        lottie_data = carregar_arquivo_lottie(filepath)
 #       st_lottie(lottie_data, speed=1, reverse=False, loop=True, quality="low", height=400, width=400)

  #  # Exibe outras animações Lottie
   #     load_and_display_lottie(pasta_pages/"animation.json")
    #    load_and_display_lottie(pasta_pages / "animation2.json")


st.subheader(':green[LESTE CONECTA]', divider='rainbow')
st.markdown('<h1 style="text-align: ; color: green;">BEM VINDO A PÁGINA INICIAL</h1><br>', unsafe_allow_html=True)


st.sidebar.page_link("pages/comercial.py", label="🛒 COMERCIAL")
st.sidebar.page_link("pages/financeiro.py", label="💲 FINANCEIRO")
st.sidebar.page_link("pages/suporte.py", label="🛠️ SUPORTE")
st.sidebar.page_link("app.py", label="DELOGAR")
st.sidebar.divider()

col1, col2, col3 = st.columns(3)
with col1:
    #st.header(":orange[CONSULTAR VIABILIDADE]")
    st.write('<h1 style="font-weight:bold; color:">VIABILIDADE</h1>', unsafe_allow_html=True)

    st.link_button("VIABILIDADE", "https://www.lestetelecom.com.br/viabilidade")

with col2:
    #st.header("CONSULTA FAQ")
    st.write('<h1 style="font-weight:bold; color:">FAQ</h1>', unsafe_allow_html=True)

    st.link_button("FAQ - LESTE", "https://www.lestetelecom.com.br/faq")

with col3:
    #st.header("LESTE MOVEL")
    st.write('<h1 style="font-weight:bold; color:">LESTE MÓVEL</h1>', unsafe_allow_html=True)

    st.link_button("IR", "https://www.lestemovel.com.br/")

st.divider()

st.write('<h1 style="font-weight:bold; color:">APP- TRANSCRIPTION</h1>', unsafe_allow_html=True)
st.link_button("APP - Transcrição de Audio", "https://audiotranscription-i.streamlit.app/")
    
   
    
