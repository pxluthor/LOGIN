
import streamlit as st

def app():

    st.subheader(':green[LESTE CONECTA]', divider='rainbow')
    st.markdown('<h1 style="text-align: center; color: green;">PROCEDIMENTOS</h1><br>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("CONSULTAR VIABILIDADE")
        st.link_button("VIABILIDADE", "https://www.lestetelecom.com.br/viabilidade")

    with col2:
        st.header("CONSULTA FAQ")
        st.link_button("FAQ - LESTE", "https://www.lestetelecom.com.br/faq")

    with col3:
        st.header("LESTE MOVEL")
    st.link_button("IR", "https://www.lestemovel.com.br/")

    st.divider()