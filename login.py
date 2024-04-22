import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

def app():
# Função para autenticar o usuário
    def authenticate(login, senha):
    # Autenticação com o Google Sheets
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('cred.json', scope)
        client = gspread.authorize(creds)
    
    # Abre a planilha e a folha
        sheet = client.open('LOGIN').sheet1
    
    # Obtém as credenciais da planilha
        credenciais = sheet.get_all_values()
    
    # Verifica se as credenciais estão corretas
        for credencial in credenciais:
            if len(credencial) >= 2 and credencial[0] == login and credencial[1] == senha:
                return True
        return False

# Configurações do Streamlit
    st.title("Digite seu login e senha")
    login = st.text_input("Login")
    senha = st.text_input("Senha", type="password")
    submit_button = st.button("Entrar")

# Verifica as credenciais quando o botão for clicado
    if submit_button:
        if authenticate(login, senha):
            st.success("Login bem-sucedido!")
            st.write("Redirecionando para a Homepage...")
        # Construa o caminho completo para o arquivo Homepage.py
            homepage_path = os.path.join(os.path.dirname(__file__), "Homepage.py")
        # Redireciona para a Homepage
            st.experimental_rerun(script_runner=homepage_path)
        else:
            st.error("Credenciais inválidas. Por favor, tente novamente.")
