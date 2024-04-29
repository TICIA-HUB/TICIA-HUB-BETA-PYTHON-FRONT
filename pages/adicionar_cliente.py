import streamlit as st
import requests

def show():

    st.header("Adicionar nova Cliente")
    st.write("Insira as informações da nova cliente abaixo:")


    with st.form("form_add_cliente"):
        nome = st.text_input("Nome")
        sobrenome = st.text_input("Sobrenome")
        email = st.text_input("Email")
        whatsapp = st.text_input("Whatsapp")
        data_nascimento = st.text_input("Data de Nascimento")
        cep = st.text_input("CEP")

        submit_button = st.form_submit_button("Adicionar")

    if submit_button:
        
        try:
            whatsapp = int(whatsapp)  
        except ValueError:
            st.error("Número de WhatsApp inválido.")

        if email == '':
            email = 'notemail@notemail.com'

        info = {
            'nome': nome,
            'sobrenome': sobrenome,
            'email': email,
            'whatsapp': whatsapp,
            'data_nascimento': data_nascimento,
            'cep': cep
        }

        if '' in info.values():
            st.error("Insira todas as informações necessárias")
        else:
            st.write(info)
            response = requests.post("http://127.0.0.1:5000/cliente_add", json=info)
            if response.status_code == 201:
                st.success("Cliente adicionado com sucesso!")
            elif response.status_code == 400:
                st.error("Verifique as informações inseridas")
            elif response.status_code == 500:
                st.error("Erro no servidor")