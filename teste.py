
import streamlit as st

def teste():
    #st.sidebar.page_link("app.py", label="Switch accounts")
    st.sidebar.page_link("pages/comercial.py", label="COMERCIAL")
    st.sidebar.page_link("pages/financeiro.py", label="FINANCEIRO")
    st.sidebar.page_link("pages/suporte.py", label="SUPORTE")


    #st.sidebar.page_link("app.py", label="Switch accounts")
    #if st.session_state.role in ["financeiro", "suporte"]:
        #st.sidebar.page_link("pages/suporte.py", label="GERENCIA")
        #st.sidebar.page_link(
            #"pages/financeiro.py",
            #label="Acesso coordenação",
            #disabled=st.session_state.role != "financeiro",   
             #       )