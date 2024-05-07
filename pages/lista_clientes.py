import streamlit as st
import requests
import pandas as pd

def show():
    st.header("Lista de Clientes")

    clientes = requests.get("https://ticiahub-6e8cd092033f.herokuapp.com/clientes")

    try:
        clientes = pd.DataFrame(clientes.json()['clientes'], columns=['id', 'nome', 'sobrenome', 'email', 'whatsapp', 'data_nascimento', 'cep'])
        st.table(clientes)
    except requests.exceptions.JSONDecodeError as e:
        st.error("Erro ao carregar clientes") 
    