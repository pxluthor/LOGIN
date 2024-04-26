import json
import requests
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
caminho_animation2 = pasta_pages / "animation.json"

# Carrega o arquivo Lottie da animação de fundo
animacao_fundo = carregar_arquivo_lottie(caminho_animation2)

# Exibe a animação de fundo usando st_lottie com CSS personalizado
st.markdown(
    f"""
    <style>
        .stApp {{
            background-image: url('data:image/svg+xml;base64,{animacao_fundo}');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}
    </style>
    """,
    unsafe_allow_html=True
)


#st.set_page_config(layout="wide", page_title="Leste conecta")
st.subheader(':green[LESTE CONECTA]', divider='rainbow')
st.markdown('<h1 style="text-align: center; color: green;">PROCEDIMENTOS - COMERCIAL</h1><br>', unsafe_allow_html=True)

st.header('teste de acesso Gerência')
st.sidebar.page_link("app.py", label="DELOGAR")


# GitHub: https://github.com/andfanilo/streamlit-lottie
# Lottie Files: https://lottiefiles.com/




def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

# Function to load Lottie file from local path
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Define the relative path to the pages folder
pages_folder = Path("pages")

# Define a list of filenames for the Lottie animations
filenames = ["animation2.json"]

# Load each Lottie file and store them in a list
lottie_animations = []
for filename in filenames:
    filepath = pages_folder / filename
    lottie_animation = load_lottiefile(filepath)
    lottie_animations.append(lottie_animation)

# Now you can use st_lottie with the loaded animation
for i, animacao_lottie in enumerate(lottie_animations):
    st_lottie(
        animacao_lottie,
        speed=1,
        reverse=False,
        loop=True,
        quality="low", # medium ; high
        height=400,
        width=400,
        key=f"lottie_animations_{i}",
)