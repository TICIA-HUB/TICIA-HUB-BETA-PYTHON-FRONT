import streamlit as st

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