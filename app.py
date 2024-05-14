import streamlit as st
import requests
from pages.adicionar_cliente import show as show_add_cliente
from pages.lista_clientes import show as show_lista_clientes
from utils.global_style import apply_global_styles
from PIL import Image

API_URL = "https://ticiahub-6e8cd092033f.herokuapp.com"

def render_sidebar():
    st.sidebar.title("Menu")
    page = st.sidebar.radio("Escolha a página:", ('Adicionar cliente', 'Lista de Clientes'), key='page_selection')
    return page

def login(username, password):
    response = requests.post(f"{API_URL}/login", json={"username": username, "password": password})
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        return None

def main():
    st.set_page_config(page_title="TiciaHub", page_icon=":bar_chart:", layout="wide")
    apply_global_styles()

    image_path = "pages\\images\\hub-logo (3).png"
    image = Image.open(image_path)
    st.image(image, width=360)

    if "token" not in st.session_state:
        username = st.sidebar.text_input("Usuario", key='username', help="Insira seu nome de usuário")
        password = st.sidebar.text_input("Senha", type="password", key='password', help="Insira sua senha")
        if st.sidebar.button("Login"):
            token = login(username, password)
            if token:
                st.session_state["token"] = token
                st.success("Login bem-sucedido!")
                st.experimental_rerun()
            else:
                st.error("Nome de usuário ou senha inválidos.")

    else:
        token = st.session_state["token"]
        page = render_sidebar()
        if page == 'Adicionar cliente':
            show_add_cliente(token)
        elif page == 'Lista de Clientes':
            show_lista_clientes(token)

if __name__ == "__main__":
    main()
