import streamlit as st
import subprocess
import os




st.set_page_config(layout="wide", page_title="Leste conecta")
st.subheader(':green[LESTE CONECTA]', divider='rainbow')
st.markdown(
    '<h1 style="text-align: center; color: green;">TESTE DE ACESSO SUPERVIÃO</h1><br>', 
            
            unsafe_allow_html=True)

 

st.sidebar.link_button("Trancrição de Áudio", "https://transcriptionleste.streamlit.app/")

st.title('Testando vídeo')
st.sidebar.page_link("app.py", label="DESLOGAR")

container = st.container(border=True)
VIDEO_URL = "https://youtu.be/5aFnP22GpPI"


#st.video(f'<iframe width="800" height="400" src="{st.video(VIDEO_URL)}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

st.video(VIDEO_URL, format="video/mp4")
#st.markdown(f'<iframe width="800" height="400" src="{st.video(VIDEO_URL)}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
#st.markdown(f'<iframe width="400" height="225" src="{teste1}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
