# import streamlit as st
# from pages import adicionar_cliente, lista_clientes

# def apply_global_styles():
#     st.markdown("""
#     <link rel="preconnect" href="https://fonts.googleapis.com">
#     <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
#     <link href="https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">            
#     <style>
#         body {
#             background-color: #ffffff;
#             color: #000000;
#             font-family: 'Raleway', sans-serif;
#             fontweight: medium;

#         }
        
#         h1 {
#                 font-family: 'Raleway', sans-serif;
#                 fontweight: bold;
#         }
        
#         h2 {
#                 font-family: 'Raleway', sans-serif;
#                 fontweight: medium;
        
#         }
        
#         h3 {
#                 font-family: 'Raleway', sans-serif;
#                 fontweight: medium;
#         }
        
#         input[type="text"], input[type="email"], input[type="password"], input[type="number"] {
#             font-family: 'Raleway', sans-serif;
#         }
        
#     </style>   
        
# """, unsafe_allow_html=True)

# def render_sidebar():
#     st.sidebar.title("Menu")
#     page = st.sidebar.radio("Escolha a página:", ('Adicionar cliente', 'Lista de Clientes'))
#     return page

# def main():
#     # Renderizar sidebar e obter a escolha da página
#     page = render_sidebar()

#     # Exibir a página escolhida
#     if page == 'Adicionar cliente':
#         adicionar_cliente.show()
#     elif page == 'Lista de Clientes':
#         lista_clientes.show()


# def render_sidebar():
#     st.sidebar.title("Menu")
#     page = st.sidebar.radio("Escolha a página:", ('Adicionar cliente', 'Lista de Clientes'))
#     return page

# if __name__ == "__main__":
#     main()


# import streamlit as st
# import requests

# # URL do endpoint de login
# LOGIN_URL = "http://127.0.0.1:5000/login"

# def login_user(username, password):
#     """ Envia uma solicitação POST para a API de login com o username e password """
#     response = requests.post(LOGIN_URL, json={"username": username, "password": password})
#     if response.status_code == 200:
#         return True, response.json()
#     return False, response.json()

# def login_page():
#     """ Página de login com verificação via API """
#     st.sidebar.title("Login")
#     username = st.sidebar.text_input("Username", key="login_username")
#     password = st.sidebar.text_input("Password", type="password", key="login_password")
#     if st.sidebar.button("Login", key="login_button"):
#         login_successful, response_data = login_user(username, password)
#         if login_successful:
#             st.session_state['logged_in'] = True
#             st.success("Login bem-sucedido!")
#         else:
#             st.error(response_data.get('message', 'Credenciais inválidas.'))

# def render_sidebar():
#     """ Renderiza a barra lateral com opções de navegação após login """
#     st.sidebar.title("Menu")
#     page = st.sidebar.radio("Escolha a página:", ('Adicionar cliente', 'Lista de Clientes'), key="page_selection")
#     return page

# def apply_global_styles():
#     """ Aplica estilos globais para a página usando CSS """
#     st.markdown("""
#     <style>
#         body {
#             background-color: #ffffff;
#             color: #000000;
#             font-family: 'Raleway', sans-serif;
#             font-weight: medium;
#         }
#         h1, h2, h3 {
#             font-family: 'Raleway', sans-serif;
#             font-weight: bold;
#         }
#         input[type="text"], input[type="email"], input[type="password"], input[type="number"] {
#             font-family: 'Raleway', sans-serif;
#         }
#     </style>   
#     """, unsafe_allow_html=True)

# def main():
#     """ Função principal que controla o fluxo da aplicação """
#     apply_global_styles()
#     # Verifica se o usuário está logado
#     if 'logged_in' not in st.session_state:
#         st.session_state['logged_in'] = False

#     if not st.session_state['logged_in']:
#         login_page()
#     else:
#         page = render_sidebar()
#         if page == 'Adicionar cliente':
#             adicionar_cliente.show()
#         elif page == 'Lista de Clientes':
#             lista_clientes.show()

import streamlit as st
from pages import adicionar_cliente, lista_clientes

def apply_global_styles():
    st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">            
    <style>
        body {
            background-color: #ffffff;
            color: #000000;
            font-family: 'Raleway', sans-serif;
            font-weight: medium;
        }
        
        h1 {
            font-family: 'Raleway', sans-serif;
            font-weight: bold;
        }
        
        h2, h3 {
            font-family: 'Raleway', sans-serif;
            font-weight: medium;
        }
        
    </style>   
    """, unsafe_allow_html=True)

def render_sidebar():
    st.sidebar.title("Menu")
    # Adicionando uma chave única para evitar conflitos
    page = st.sidebar.radio("Escolha a página:", ('Adicionar cliente', 'Lista de Clientes'), key='page_selection')
    return page

def main():
    # Renderizar sidebar e obter a escolha da página
    page = render_sidebar()

    # Exibir a página escolhida
    if page == 'Adicionar cliente':
        adicionar_cliente.show()
    elif page == 'Lista de Clientes':
        lista_clientes.show()


if __name__ == "__main__":
    main()
