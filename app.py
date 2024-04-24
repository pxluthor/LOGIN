import streamlit as st
from menu import menu


#Inicialize st.session_state.role como  vazia
if "role" not in st.session_state:
    st.session_state.role = None

# Recupere a função do estado da sessão para inicializar o widget
st.session_state._role = st.session_state.role

def set_role():
    # Função de retorno de chamada para salvar a seleção de função no estado da sessão
    st.session_state.role = st.session_state._role







menu() # Renderiza o menu dinâmico!



