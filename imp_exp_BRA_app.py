import sqlite3
import streamlit as st
import pandas as pd
import plotly.express as px
 

# Conectar a la base de datos
conn = sqlite3.connect("C:/Users/dan_n/Desktop/Practica/database.db")
cursor = conn.cursor()

# Cerrar conexión
conn.close()



st.title('Análisis del Flujo Comercial entre Venezuela y Brasil (2011-2021)')


def set_bg_hack_url():
    st.markdown( 
          f""" 
          <style> 
        .stApp {{ 
              background-color: rgba(0, 0, 0, 0.5); /* 50% opacidad */
              background-image: url("https://i.imgur.com/enoZJSV.png"); 
              background-size: cover; 
         }} 
          </style> 
          """, 
          unsafe_allow_html=True 
      ) 

set_bg_hack_url()


st.markdown(
    f"""
    <style>
   .container {{
        display: flex;
    }}
   .logo-img {{
        float: right;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

url_image = "https://img.goodfon.com/wallpaper/big/7/97/brasil-brazil-flag-flag-of-brazil-brazilian-flag.jpg"

st.markdown(
    f"""
    <style>
    .container {{
        display: flex;
    }}
    .logo-img {{
        float: right;
        margin-right: 20px;  /* agregar espacio entre la foto y el texto */
    }}
    .logo-text {{
        font-size: 30px;  /* ajustar tamaño del texto */
        font-weight: bold;  /* hacer que el texto sea negrita */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

url_image = "https://img.goodfon.com/wallpaper/big/7/97/brasil-brazil-flag-flag-of-brazil-brazilian-flag.jpg"

st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src={url_image} alt="Flag" width="80"> 
        <p class="logo-text">Brasil</p> 
    </div>
    """,
    unsafe_allow_html=True
)
