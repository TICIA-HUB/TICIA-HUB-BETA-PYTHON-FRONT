# # import streamlit as st
# # import requests
# # from utils.func import busca_cep

# # def show():

# #     st.header("Adicionar nova cliente")
# #     st.write("Insira as informações da nova cliente abaixo:")


# #     with st.form("form_add_cliente"):
# #         nome = st.text_input("Nome")
# #         sobrenome = st.text_input("Sobrenome")
# #         email = st.text_input("Email")
# #         whatsapp = st.text_input("Whatsapp (apenas números)")
# #         data_nascimento = st.text_input("Data de Nascimento")
# #         cep = st.text_input("CEP (apenas números)")

# #         if cep and len(cep) == 8 and cep.isdigit():
# #             dados_cep = busca_cep(cep)
# #             if dados_cep:
# #                 st.sucess("CEP válido!")
# #                 rua = st.text_input("Rua", value=dados_cep.get('logradouro'))
# #                 bairro = st.text_input("Bairro", value=dados_cep.get('bairro'))
# #                 numero = st.text_input("Número")
# #                 complemento = st.text_input("Complemento")
# #             else:
# #                 st.error("CEP inválido. Por favor, tente novamente.")
# #         elif cep:
# #             st.error("CEP inválido. Por favor, insira um CEP válido.")

# #         submit_button = st.form_submit_button("Adicionar")

# #     if submit_button:
        
# #         # Verificações
# #         try:
# #             whatsapp = int(whatsapp)  
# #         except ValueError:
# #             st.error("Número de WhatsApp inválido.")

# #         if email == '':
# #             email = 'notemail@notemail.com'

# #         info = {
# #             'nome': nome,
# #             'sobrenome': sobrenome,
# #             'email': email,
# #             'whatsapp': whatsapp,
# #             'data_nascimento': data_nascimento,
# #             'cep': cep
# #         }

# #         if '' in info.values():
# #             st.error("Insira todas as informações necessárias")
# #         else:
# #             st.write(info)
# #             response = requests.post("http://127.0.0.1:5000/cliente_add", json=info)
# #             if response.status_code == 201:
# #                 st.success("Cliente adicionado com sucesso!")
# #             elif response.status_code == 400:
# #                 st.error("Verifique as informações inseridas")
# #             elif response.status_code == 500:
# #                 st.error("Erro no servidor")

# # if __name__ == "__main__":
# #     show()




# import streamlit as st
# import requests
# from utils.func import busca_cep

# def show():
#     st.header("Adicionar nova cliente")
#     st.write("Insira as informações da nova cliente abaixo:")

#     with st.form("form_add_cliente"):
#         nome = st.text_input("Nome")
#         sobrenome = st.text_input("Sobrenome")
#         email = st.text_input("Email")
#         whatsapp = st.text_input("Whatsapp (apenas números)")
#         data_nascimento = st.text_input("Data de Nascimento")
#         cep = st.text_input("CEP (apenas números)")

#         # Verificação de CEP após completar o preenchimento de 8 dígitos
#         if cep and len(cep) == 8 and cep.isdigit():
#             dados_cep = busca_cep(cep)
#             if dados_cep:
#                 st.success("CEP válido!")
#                 rua = st.text_input("Rua", value=dados_cep.get('logradouro', ''))
#                 bairro = st.text_input("Bairro", value=dados_cep.get('bairro', ''))
#                 numero = st.text_input("Número")
#                 complemento = st.text_input("Complemento")
#             else:
#                 st.error("CEP inválido. Por favor, tente novamente.")
#         elif cep:
#             st.error("O CEP deve conter 8 dígitos numéricos.")

#         submit_button = st.form_submit_button("Adicionar")

#     if submit_button:
#         # Verificações antes de submeter
#         try:
#             whatsapp = int(whatsapp)
#         except ValueError:
#             st.error("Número de WhatsApp inválido.")
#             return  # Encerra a execução aqui para não prosseguir

#         if email == '':
#             email = 'notemail@notemail.com'

#         info = {
#             'nome': nome,
#             'sobrenome': sobrenome,
#             'email': email,
#             'whatsapp': whatsapp,
#             'data_nascimento': data_nascimento,
#             'cep': cep,
#             'rua': rua if 'rua' in locals() else '',  # Uso de locals() para verificar se rua está definido
#             'bairro': bairro if 'bairro' in locals() else '',
#             'numero': numero if 'numero' in locals() else '',
#             'complemento': complemento if 'complemento' in locals() else ''
#         }

#         if '' in info.values():
#             st.error("Insira todas as informações necessárias")
#         else:
#             response = requests.post("http://127.0.0.1:5000/cliente_add", json=info)
#             if response.status_code == 201:
#                 st.success("Cliente adicionado com sucesso!")
#             elif response.status_code == 400:
#                 st.error("Verifique as informações inseridas")
#             elif response.status_code == 500:
#                 st.error("Erro no servidor")

# if __name__ == "__main__":
#     show()

import streamlit as st
import requests
from utils.func import busca_cep

def show():
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

        
        response = requests.post("http://127.0.0.1:5000/cliente_add", json=info)
        if response.status_code == 201:
            st.success("Cliente adicionado com sucesso!")
        elif response.status_code == 400:
            st.error("Verifique as informações inseridas")
        elif response.status_code == 500:
            st.error("Erro no servidor")

if __name__ == "__main__":
    show()