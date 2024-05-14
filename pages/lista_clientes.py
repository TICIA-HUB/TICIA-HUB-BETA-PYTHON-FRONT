import streamlit as st
import requests
import pandas as pd

API_URL = "https://ticiahub-6e8cd092033f.herokuapp.com"

def show(token):
    st.header("Lista de Clientes")

    headers = {"Authorization": f"Bearer {token}"}
    clientes = requests.get(f"{API_URL}/clientes", headers=headers)

    try:
        clientes = pd.DataFrame(clientes.json()['clientes'], columns=['nome', 'sobrenome', 'email', 'whatsapp', 'data_nascimento', 'cep'])
        st.table(clientes)
    except requests.exceptions.JSONDecodeError as e:
        st.error("Erro ao carregar clientes") 
    

#