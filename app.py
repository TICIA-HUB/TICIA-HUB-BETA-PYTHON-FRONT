import streamlit as st
from pages import adicionar_cliente, lista_clientes

def render_sidebar():
    st.sidebar.title("Menu")
    page = st.sidebar.radio("Escolha a página:", ('Adicionar cliente', 'Lista de Clientes'))
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