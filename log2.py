import streamlit as st
import hydralit_components as hc

# define what option labels and icons to display



with st.sidebar: 
    option_data= [
            {'icon': "bi bi-hand-thumbs-up", 'label':"Agree"},
            {'icon':"fa fa-question-circle",'label':"Unsure"},
            {'icon': "bi bi-hand-thumbs-down", 'label':"Disagree"},
    ]

    # substitua o tema, caso contrário, ele usará o tema aplicado Streamlit
    over_theme = {'txc_inactive': 'white','menu_background':'green','txc_active':'black','option_active':'blue'}
    font_fmt = {'font-class':'h2','font-size':'150%'}
    op= hc.option_bar(option_definition=option_data,
                  title='Leste Conecta',
                  key='PrimaryOption',
                  override_theme=over_theme,
                  font_styling=font_fmt,
                  horizontal_orientation=False)




