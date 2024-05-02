import streamlit as st
import requests
    
def busca_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200 and response.json().get('erro') is None:
        return response.json()
    else:
        return None
    
