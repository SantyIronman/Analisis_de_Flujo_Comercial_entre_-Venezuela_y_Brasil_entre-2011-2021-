import sqlite3
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


# Base de datos

st.title('Análisis del Flujo Comercial entre Venezuela y Brasil (2011-2021)')

##Fondo agregado
def set_bg_hack_url():      
    st.markdown( 
          f""" 
          <style> 
          .stApp {{ 
              background: url("https://i.imgur.com/enoZJSV.png"); 
              background-size: cover 
          }} 
          </style> 
          """, 
          unsafe_allow_html=True 
      ) 

set_bg_hack_url()

####Se agrega la bandera de Brasil con un subtitulo
styles = """
<style>
  .container {
        display: flex;
        align-items: center; /* Alinear verticalmente el contenido */
    }
  .logo-img {
        width: 150px; /* Tamaño de la imagen de la bandera */
        height: 100px;
        margin: 10px; /* Agregar un margen para separar la imagen del borde */
    }
  .logo-text {
        font-size: 60px;  /* ajustar tamaño del texto */
        font-weight: bold;  /* hacer que el texto sea negrita */
        margin-left: 10px; /* Agregar un margen a la izquierda para separar del texto de la imagen */
    }
</style>
"""

st.markdown(styles, unsafe_allow_html=True)

bandera_brasil = "https://img.goodfon.com/wallpaper/big/7/97/brasil-brazil-flag-flag-of-brazil-brazilian-flag.jpg"

contenido = f"""
<div class="container">
    <img class="logo-img" src={bandera_brasil} alt="Flag" > 
    <span class="logo-text">Brasil</span>
</div>
"""

st.markdown(contenido, unsafe_allow_html=True)


# Contenido sobre el contexto histórico

st.title("Acerca de")

st.header("Objetivo")

st.write("El intercambio comercial entre Venezuela y Brasil ha tenido una larga y compleja historia, marcada por períodos de auge y declive, fuertemente influenciada por factores políticos, económicos y sociales. A continuación, se presenta un panorama general del contexto histórico de las importaciones y exportaciones entre ambos países desde principios del año 2011 hasta el año 2021.")

st.write("Para ello necesitamos identificar el contexto histórico que maneja la influencia de los acontecimientos políticos y económicos.")

st.header("Contexto Económico")

st.write("Aunque actualmente la crisis económica en Venezuela no es tan fácil de percibir como lo era durante su punto más alto cerca de los años 2013-2017 aún existe y ha logrado afectar el comercio internacional. Para relacionar la crisis económica de Venezuela con su comercio con Brasil debemos conocer los puntos críticos de la economía de Venezuela durante la última década tales como la hiperinflación y las sanciones económicas.")

# Se agrega el título para la próxima sección
st.title("Importaciones Brasil - Venezuela durante 2011 y 2021")

st.write("Las importaciones son un componente fundamental del PIB que contribuyen al crecimiento y bienestar de una economía, tanto a través del consumo como de la mejora de la productividad empresarial. En el caso de Brasil, las importaciones han sido un factor relevante, aunque las exportaciones han sido el principal motor del crecimiento económico en las últimas décadas")
st.markdown("""
<ol>
  <strong>Factores imprtantes: </strong>
  <li><strong>Precio del petróleo:</strong> El precio del petróleo fue el principal factor que determinó el volumen de las importaciones venezolanas desde Brasil. Cuando el precio del petróleo era alto, Venezuela tenía más ingresos para gastar en importaciones.</li>
  <li><strong>Tipo de cambio:</strong> El tipo de cambio entre el bolívar venezolano y el real brasileño también afectó las importaciones. Cuando el bolívar se debilitaba, las importaciones desde Brasil se volvían más caras.</li>
  <li><strong>Crecimiento económico:</strong> El crecimiento económico de Venezuela también influyó en las importaciones. Cuando la economía venezolana crecía, la demanda de productos importados también aumentaba.</li>
  <li><strong>Controles de importación:</strong> A partir del 2014, el gobierno venezolano implementó una serie de controles de importación, lo que dificultó la entrada de productos brasileños al país.</li>
  <li><strong>Sanciones:</strong> Las sanciones impuestas a Venezuela por Estados Unidos en 2019 también dificultaron el comercio con Brasil.</li>
</ol>
""", unsafe_allow_html=True)

st.header("Durante el 2011")


