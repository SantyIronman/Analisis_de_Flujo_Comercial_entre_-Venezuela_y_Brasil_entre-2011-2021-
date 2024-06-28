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
        align-items: center; 
    }
  .logo-img {
        width: 150px; 
        height: 100px;
        margin: 10px; 
    }
  .logo-text {
        font-size: 60px;  
        font-weight: bold;  
        margin-left: 10px; 
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
    <h2 style="text-align: center;"><b>Brasil</b></h2>
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


# Acerca de las importaciones
st.header("Acerca de las importaciones")

col1 = st.columns(1)

html1 = """
<div style="text-align: center;">
 <h2>IMPORTACIONES</h2>
  <p> Valor de las importaciones 2021 $361 MM </p>
  <p> Valor de las importaciones 2011 $884 MM </p>
  <p> <strong>Crecimiento de </strong> $523MM</p>
  <p> <strong>Crecimiento del valor de las exportacione</strong> -59,2% </p>
</div>
"""

html1 = """
<p style="text-align: center;">
  <strong>PIB:</strong> Valor de las exportaciones 2021 $1,33MM,
   <br>Valor de las exportaciones 2011 $5,33MM
   <br>Crecimiento del valor de las exportacione -74,6%
</p>
"""

st.write(html1, unsafe_allow_html=True)

#graficos

conn = sqlite3.connect('C:/Users/dan_n/Documents/Importaciones_Exportaciones BRA 2011-2021/database.db')
cursor = conn.cursor()  

# consulta
cursor.execute("""
    SELECT CO_ANO, NO_NCM_ESP, SUM(CO_UNID) AS cantidad_total, SUM(VL_FOB) AS valor_total
    FROM limpia_imp
    GROUP BY CO_ANO, NO_NCM_ESP
    ORDER BY CO_ANO, cantidad_total DESC;
""")

result = cursor.fetchall()
df = pd.DataFrame(result, columns=['Año', 'Producto', 'Cantidad Total', 'Valor Total'])
df['Producto'] = df['Producto'].apply(lambda x: x[:5] + '...' if len(x) > 5 else x)
df_grouped = df.groupby(['Año', 'Producto'])['Cantidad Total'].sum().reset_index()
df_grouped = df_grouped.sort_values(['Año', 'Cantidad Total'], ascending=[True, False]).groupby('Año').head(4).reset_index(drop=True)
fig = px.bar(df_grouped, x='Producto', y='Cantidad Total', color='Cantidad Total', 
             animation_frame='Año', hover_name='Producto', 
             color_continuous_scale='greens')
fig.update_layout(title='Productos más importados por año',
                  xaxis_title='Producto',
                  xaxis_title_font_size=18,
                  yaxis_title='Cantidad Total',
                  xaxis_tickfont=dict(size=14),  # Aumenta el tamaño de los tick labels
                  updatemenus=[])

# Configura el slider
fig.update_layout(sliders=[dict(
    currentvalue=dict(font=dict(size=16)),
    pad={'t': 10},
    steps=[]
)])

# Muestra el gráfico en Streamlit
st.plotly_chart(fig, use_container_width=True)


#Exportaciones apartado

st.header("Acerca de las exportaciones")

html1 = """
<p style="text-align: center;">
  <br>Valor de las exportaciones 2021 $1,33MM
  <br>Valor de las exportaciones 2011 $5,33MM
  <br><strong>Crecimiento del valor de las exportacione</strong> -74,6%
</p>
"""

st.write(html1, unsafe_allow_html=True)

# gráfico exportaciones

# consulta
cursor.execute("""
    SELECT CO_ANO, NO_NCM_ESP, SUM(CO_UNID) AS cantidad_total, SUM(VL_FOB) AS valor_total
    FROM limpia_exp
    GROUP BY CO_ANO, NO_NCM_ESP
    ORDER BY CO_ANO, cantidad_total DESC;
""")

result = cursor.fetchall()
df = pd.DataFrame(result, columns=['Año', 'Producto', 'Cantidad Total', 'Valor Total'])
df['Producto'] = df['Producto'].apply(lambda x: x[:5] + '...' if len(x) > 5 else x)
df_grouped = df.groupby(['Año', 'Producto'])['Cantidad Total'].sum().reset_index()
df_grouped = df_grouped.sort_values(['Año', 'Cantidad Total'], ascending=[True, False]).groupby('Año').head(4).reset_index(drop=True)
fig = px.bar(df_grouped, x='Producto', y='Cantidad Total', color='Cantidad Total', 
             animation_frame='Año', hover_name='Producto', 
             color_continuous_scale='greens')
fig.update_layout(title='Productos más exportados por año',
                  xaxis_title='Producto',
                  yaxis_title='Cantidad Total',
                  updatemenus=[])

#slider
fig.update_layout(sliders=[dict(
    currentvalue=dict(font=dict(size=16)),
    pad={'t': 10},
    steps=[]
)])
st.plotly_chart(fig, use_container_width=True)


fig = px.scatter(df, x="no_ncm_pais", y="Cantidad Total", color="Producto", hover_name="Producto")
fig.update_layout(title="Dispersión de productos vendidos por país",
                  xaxis_title="País",
                  yaxis_title="Cantidad Total",
                  legend_title="Producto")
st.plotly_chart(fig, use_container_width=True)



st.header("Referencias bibliográficas")

st.write("Exportaciones, importaciones y socios comerciales. (2022). OEC. https://oec.world/es/profile/country/bra?subnationalFlowSelector=flow0&flowSelector1=flow1")
st.write("Instituto Brasileiro de Geografía y Estadística (2020). IBGE. https://www.ibge.gov.br/")