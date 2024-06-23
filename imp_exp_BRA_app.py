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

# Definir estilos CSS
styles = """
<style>
  .cp-section-inner {
    padding: 20px;
  }
  .cp-multi-column-section-inner {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .cp-about-section-inner {
    background-color: #f7f7f7;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  .mantine-Text-root {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
  }
  .cp-section-content {
    padding: 20px;
    display: flex;
    flex-wrap: wrap;
  }
  .cp-multi-column-section-caption {
    font-size: 18px;
    color: #666;
    width: 50%;
  }
  .cp-section-paragraph {
    margin-bottom: 20px;
  }
  strong {
    font-weight: bold;
  }
  a {
    text-decoration: none;
    color: #337ab7;
  }
  a:hover {
    color: #23527c;
  }
</style>
"""

# Aplicar estilos CSS
st.markdown(styles, unsafe_allow_html=True)

# Contenido sobre el contexto histórico
contenido = """
<div class="cp-section-inner cp-multi-column-section-inner cp-about-section-inner">
  <h2 id="about">Acerca de</h2>
  <div class="cp-section-content">
    <div class="cp-multi-column-section-caption" style="display: inline-block; width: 50%;">
      <p class="cp-section-paragraph">
        <strong>Objetivo:</strong>
        El intercambio comercial entre Venezuela y Brasil ha tenido una larga y compleja historia, marcada por períodos de auge y declive,  fuertemente influenciada por factores políticos, económicos y sociales. A continuación, se presenta un panorama general del contexto histórico de las importaciones y exportaciones entre ambos países desde principios del año 2011 hasta el año 2021.  Para ello necesitamos identificar el contexto histórico que maneja la influencia de los acontecimientos políticos y económicos. 
      </p>
    </div>
    <div class="cp-multi-column-section-caption" style="display: inline-block; width: 50%;">
      <p class="cp-section-paragraph">
        <ol>
          <strong>Importaciones: </strong> 
          <li><strong>Precio del petróleo:</strong> El precio del petróleo fue el principal factor que determinó el volumen de las importaciones venezolanas desde Brasil. Cuando el precio del petróleo era alto, Venezuela tenía más ingresos para gastar en importaciones.</li>
          <li><strong>Tipo de cambio:</strong> El tipo de cambio entre el bolívar venezolano y el real brasileño también afectó las importaciones. Cuando el bolívar se debilitaba, las importaciones desde Brasil se volvían más caras.</li>
          <li><strong>Crecimiento económico:</strong> El crecimiento económico de Venezuela también influyó en las importaciones. Cuando la economía venezolana crecía, la demanda de productos importados también aumentaba.</li>
          <li><strong>Controles de importación:</strong> A partir del 2014, el gobierno venezolano implementó una serie de controles de importación, lo que dificultó la entrada de productos brasileños al país.</li>
          <li><strong>Sanciones:</strong> Las sanciones impuestas a Venezuela por Estados Unidos en 2019 también dificultaron el comercio con Brasil.</li>
        </ol>
        <ol>
          <strong>Exportaciones:</strong>
          <li><strong> El precio del petróleo:</strong>fue el principal factor que determinó el volumen de las exportaciones venezolanas a Brasil. Cuando el precio del petróleo era alto, Venezuela obtenía más ingresos por sus exportaciones.</li>
          <li><strong>Demanda de Brasil:</strong> La demanda de petróleo por parte de Brasil también influyó en las exportaciones venezolanas. Cuando la economía brasileña crecía, la demanda de petróleo aumentaba, lo que beneficiaba a Venezuela.</li>
          <li><strong>Relaciones políticas:</strong> Las relaciones políticas entre Venezuela y Brasil también jugaron un papel importante. Durante el período de gobierno del presidente Chávez, las relaciones entre ambos países eran estrechas, lo que facilitó el comercio bilateral.</li>
          <li><strong>Infraestructura:</strong> La infraestructura logística para el transporte de petróleo desde Venezuela a Brasil también fue un factor importante. La construcción de nuevos oleoductos y gasoductos aumentó la capacidad de exportación de Venezuela.</li>
        </ol>
      </p>
    </div>
  </div>
</div>
"""
# Mostrar contenido
st.markdown(contenido, unsafe_allow_html=True)


