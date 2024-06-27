import sqlite3
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt





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


#datos interesantes 

col1, col2 = st.columns(2)

html1 = """
<div style="text-align: center;">
 <h2>PIB:</h2>
  <p> 2011: $2.421.443 millones (USD a precios corrientes).</p>
  <p> 2021: $1.849.473 millones (USD a precios corrientes)</p>
  <p> <strong>Caída:</strong> 24% </p>
</div>
"""


html2 = """
<div style="text-align: center;">
  <h2>Variación del Ingreso Per Cápita:</h2>
  <p>Caída: 23% entre 2011 y 2021</p>
  <p>Punto más alto: $13.230 en 2014</p>
</div>
"""





with col1:
    st.write(html1, unsafe_allow_html=True)

with col2:
    st.write(html2, unsafe_allow_html=True)








#Se agrega el apartado BRASIL-VENEZUELA


contenido = f"""
<div class="container">
    <h2 style="text-align: center;"><b>Brasil/</b></h2>
    <img src="https://img.goodfon.com/wallpaper/big/7/97/brasil-brazil-flag-flag-of-brazil-brazilian-flag.jpg" alt="Flag" width="50" > 
    <h2 style="text-align: center;"><b>Venezuela</b></h2>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Flag_of_Venezuela_%281930%E2%80%932006%29.svg/220px-Flag_of_Venezuela_%281930%E2%80%932006%29.svg.png" alt="Flag" width="50" > 
</div>
"""

st.markdown(contenido, unsafe_allow_html=True)


#Se agregan datos interesantes sobre Brasil y Venezuela
col1, col2, col3 = st.columns(3)

html1 = """
<div style="text-align: center;">
  <h2>PRODUCTO</h2>
  <p>$341MM | $270MM</p>
  <p>EXPORTACIONES | IMPORTACIÓN</p>
</div>
"""

html2 = """
<div style="text-align: center;">
 <h2>IMPORTACIÓN</h2>
  <p>2011: Venezuela era el 12º proveedor más importante de Brasil.</p>
  <p>2021: Venezuela ocupaba el puesto 60º entre los proveedores de Brasil.</p>
</div>
"""
html3 = """
<div style="text-align: center;">
 <h2>EXPORTACIÓN</h2>
  <p>2011: Venezuela era el 5º destino más importante de las exportaciones brasileñas.</p>
  <p>2021: Venezuela ocupaba el puesto 25º entre los destinos de las exportaciones brasileñas.</p>
</div>
"""

with col1:
    st.write(html1, unsafe_allow_html=True)

with col2:
    st.write(html2, unsafe_allow_html=True)

with col3:
    st.write(html3, unsafe_allow_html=True)



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

st.header("Acerca de las importaciones")


# Conecta a la base de datos
conn = sqlite3.connect('C:/Users/dan_n/Documents/Importaciones_Exportaciones BRA 2011-2021/database.db')


#Consulta SQL para obtener los datos para el gráfico
cursor = conn.cursor()
cursor.execute("""
    SELECT CO_ANO, NO_NCM_ESP, SUM(CO_UNID) AS cantidad_total, SUM(VL_FOB) AS valor_total
    FROM limpia_imp
    GROUP BY CO_ANO, NO_NCM_ESP
    ORDER BY CO_ANO, cantidad_total DESC;
""")
result = cursor.fetchall()

conn.close()

df = pd.DataFrame(result, columns=['Año', 'Producto', 'Cantidad Total', 'Valor Total'])

#Gráfico de barras para cada año y producto vendido
for year in df['Año'].unique():
    year_df = df[df['Año'] == year]
    top_5_products = year_df.nlargest(5, 'Cantidad Total')
    st.bar_chart(top_5_products, x='Producto', y='Cantidad Total', color='Valor Total')
    st.write(f"Productos más vendidos en {year}:")
    st.write(top_5_products)


# Crea un gráfico de mapa de Brasil y Venezuela
fig = px.choropleth_mapbox(None, geojson="https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/brazil-states.geojson",
                           locations=["SP", "RJ", "MG", "ES", "BA", "SE", "AL", "PE", "PB", "RN", "CE", "PI", "MA", "TO", "GO", "MT", "MS", "DF", "PR", "SC", "RS"],
                           color_discrete_sequence=["green"] * 20,
                           zoom=3, center={"lat": -15, "lon": -55},
                           mapbox_style="carto-positron",
                           title="Mapa de Brasil y Venezuela")

# Agrega Venezuela al mapa
venezuela_geojson = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/venezuela-states.geojson"
venezuela_locations = ["Amazonas", "Anzoátegui", "Apure", "Aragua", "Barinas", "Bolívar", "Carabobo", "Cojedes", "Delta Amacuro", "Falcón", "Guárico", "Lara", "Mérida", "Miranda", "Monagas", "Nueva Esparta", "Portuguesa", "Sucre", "Táchira", "Trujillo", "Vargas", "Yaracuy", "Zulia"]
fig.add_trace(px.choropleth_mapbox(None, geojson=venezuela_geojson,
                                   locations=venezuela_locations,
                                   color_discrete_sequence=["red"] * len(venezuela_locations),
                                   zoom=3, center={"lat": 8, "lon": -66},
                                   mapbox_style="carto-positron").data[0])

# Agrega ciudades importantes de Brasil
cities = pd.DataFrame({
    "City": ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador", "Belo Horizonte", "Curitiba", "Porto Alegre", "Recife", "Fortaleza", "Goiânia"],
    "Lat": [-23.5505, -22.9068, -15.7942, -12.9711, -19.9208, -25.4292, -30.0339, -8.0500, -3.7184, -16.6794],
    "Lon": [-46.6333, -43.1729, -47.8825, -38.5016, -43.9384, -49.2713, -51.2304, -34.8817, -38.4597, -47.8742]
})

fig.add_trace(px.scatter_mapbox(cities, lat="Lat", lon="Lon", hover_name="City", color_discrete_sequence=["red"] * len(cities)).data[0])

# Configura el layout del gráfico
fig.update_layout(margin=dict(l=0, r=0, t=30, b=0),
                  width=800, height=600)

# Muestra el gráfico en Streamlit
st.title("Mapa de Brasil y Venezuela")
st.plotly_chart(fig, use_container_width=True)