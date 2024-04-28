import streamlit as st
import subprocess
import os




st.set_page_config(layout="wide", page_title="Leste conecta")
st.subheader(':green[LESTE CONECTA]', divider='rainbow')
st.markdown(
    '<h1 style="text-align: center; color: green;">TESTE DE ACESSO SUPERVSÃO</h1><br>', 
            
            unsafe_allow_html=True)

 

st.sidebar.link_button("Trancrição de Áudio", "https://transcriptionleste.streamlit.app/")