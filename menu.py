import streamlit as st
from auth import app_login, authenticate
from teste import teste


def set_role():
    # Função de retorno de chamada para salvar a seleção de função no estado da sessão
    st.session_state.role = st.session_state._role

def authenticated_menu():
    app_login()


def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    pass
    #st.sidebar.page_link("pages/home.py", label="Log in")


def menu():
    # Determine if a user is logged in or not, then show the correct
    # navigation menu
    
    if "role" not in st.session_state or st.session_state.role is None:

        authenticated_menu() 

        
        return unauthenticated_menu()
    





          
    

def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
      
        st.switch_page("app.py")
        
    menu()