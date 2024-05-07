import streamlit as st
import requests
from utils.func import busca_cep
from app import apply_global_styles


def show():

    logoHub = "pages\images\hub-logo-1.0.svg"

    apply_global_styles()
    st.image(logoHub)
    st.header("Adicionar nova cliente")
    st.write("Insira as informações da nova cliente abaixo:")

    with st.form("form_add_cliente"):
        nome_input = st.text_input("Nome")
        nome = nome_input.title() # Verifica se o nome está capitalizado

        sobrenome_input = st.text_input("Sobrenome")
        sobrenome = sobrenome_input.title()  # Verifica se o sobrenome está capitalizado

        email = st.text_input("Email")
        whatsapp = st.text_input("Whatsapp (apenas números)")
        data_nascimento = st.text_input("Data de Nascimento")
        cep = st.text_input("CEP (apenas números)")
        numero = st.text_input("Número")
        complemento = st.text_input("Complemento")

        # Verificação condicional do CEP
        if cep and len(cep) == 8 and cep.isdigit():
            dados_cep = busca_cep(cep)
            if dados_cep:
                st.success("CEP válido!")
                rua = dados_cep.get('logradouro', '')
                bairro = dados_cep.get('bairro', '')
            else:
                st.error("CEP inválido. Por favor, tente novamente.")
        elif cep and not (len(cep) == 8 and cep.isdigit()):
            st.error("CEP inválido. Por favor, insira um CEP válido.")

        submit_button = st.form_submit_button("Adicionar")

    if submit_button:
        try:
            whatsapp = int(whatsapp)  # Verifica se o WhatsApp é um número válido
        except ValueError:
            st.error("Número de WhatsApp inválido.")
            return

        if email == '':
            email = 'notemail@notemail.com'  # Atribui um email padrão se o campo estiver vazio

        if data_nascimento == '':
            data_nascimento = 'null'

        if cep == '':
            cep = '00000000'
            rua = 'null'
            bairro = 'null'
        
        if numero == '':
            numero = 'null'
        
        
        if complemento == '':
            complemento = 'null'

        info = {
            'nome': nome,
            'sobrenome': sobrenome,
            'email': email,
            'whatsapp': whatsapp,
            'data_nascimento': data_nascimento,
            'cep': cep,
            'rua': locals().get('rua', ''),  # Uso seguro com locals().get() para evitar referência antes da atribuição
            'bairro': locals().get('bairro', ''),
            'numero': numero,
            'complemento': complemento
        }

        
        response = requests.post("https://ticiahub-6e8cd092033f.herokuapp.com/cliente_add", json=info)
        if response.status_code == 201:
            st.success("Cliente adicionado com sucesso!")
        elif response.status_code == 400:
            st.error("Verifique as informações inseridas")
        elif response.status_code == 500:
            st.error("Erro no servidor")

        st.markdown("""
        <style>
                    .logo {
                        
                    }
        </style>
        """, unsafe_allow_html=True)
        
if __name__ == "__main__":
    show()