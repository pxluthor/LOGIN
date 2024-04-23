import streamlit as st
from streamlit_option_menu import option_menu
#import streamlit_authenticator as stauth
import home, login, financeiro, suporte, comercial



#st.set_page_config(layout="wide", page_title="Leste Conecta")



class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='LESTE CONECTA ',
                options=['LOGIN','HOME','COMERCIAL','FINANCEIRO','SUPORTE'],
                icons=['person-circle','house-fill','trophy-fill','chat-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                
                 )   
                
            

        
        if app == "HOME":
            home.app()

        if app == "LOGIN":
            login.app()            

        if app == "SUPORTE":
            suporte.app()  

        if app == "FINANCEIRO":
            financeiro.app()        
      
        if app == 'COMERCIAL':
            comercial.app()    

        
      
    run()            
         