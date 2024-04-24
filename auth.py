import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from teste import teste




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


def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    
    st.sidebar.page_link("pages/home.py", label="HOME")
    st.sidebar.page_link("pages/comercial.py", label="COMERCIAL")
    st.sidebar.page_link("pages/financeiro.py", label="FINANCEIRO")
    st.sidebar.page_link("pages/suporte.py", label="SUPORTE")

def set_role():
    # Função de retorno de chamada para salvar a seleção de função no estado da sessão
    st.session_state.role = st.session_state._role

def app_login():

    st.subheader(':green[LESTE CONECTA]', divider='rainbow')
    st.title("Digite seu login e senha")
    login = st.text_input("Login")
    senha = st.text_input("Senha", type="password")
    submit_button = st.button("Entrar")
    

    # Verifica as credenciais quando o botão for clicado
    if submit_button:
        if authenticate(login, senha):

            unauthenticated_menu()
            st.success("Login bem-sucedido!")

           
            #st.selectbox(
            #"Escolha sua função:",
            #[None, "AGENTE", "SUPERVISÃO", "CORDENAÇÃO"],
            #key="_role",
            #on_change=set_role,
            #)
 
            
        else:
            st.error("Credenciais inválidas. Por favor, tente novamente.")



def app_login1():
    st.subheader(':green[LESTE CONECTA]', divider='rainbow')
    st.title("Digite seu login e senha")
    login = st.text_input("Login")
    senha = st.text_input("Senha", type="password")
    submit_button = st.button("Entrar")

    # Verifica as credenciais quando o botão for clicado
    if submit_button:
        if authenticate(login, senha):
            st.success("Login bem-sucedido!")
            
            return True
        else:
            st.error("Credenciais inválidas. Por favor, tente novamente.")

    return False 





