import streamlit as st
import pandas as pd
import plotly.express as px

# Datos proporcionados
data_2023 = {
    'Canal': ['APP', 'CAR', 'IFI', 'INHOUSE', 'PORTAL DE PAGOS', 'REDES', 'Total'],
    'Enero': [42866, 200614, 871230, 233914, 0, 236816, 1585440],
    'Febrero': [35156, 179989, 776400, 217881, 0, 218798, 1428224],
    'Marzo': [36004, 206921, 899560, 252085, 0, 225047, 1619617],
    'Abril': [32414, 195246, 863006, 233037, 0, 225047, 1548750],
    'Mayo': [33573, 202014, 891736, 236766, 0, 193690, 1557779],
    'Junio': [31228, 191791, 877311, 238754, 0, 187170, 1526254],
    'Julio': [30773, 191887, 910114, 242479, 0, 198619, 1573872],
    'Agosto': [30369, 198217, 966361, 246328, 6, 206560, 1647835],
    'Septiembre': [28491, 191871, 920688, 239779, 13, 190323, 1571158],
    'Octubre': [29785, 196714, 913890, 239110, 25, 195866, 1575378],
    'Noviembre': [28344, 191537, 901452, 231107, 43, 181324, 1533789],
    'Diciembre': [27868, 184392, 922955, 233027, 43, 188728, 1557013]
}

data_2024 = {
    'Canal': ['APP', 'CAR', 'IFI', 'INHOUSE', 'PORTAL', 'REDES'],
    'Enero': [29613, 186913, 1020008, 222393, 132, 204555],
    'Febrero': [28235, 176177, 920377, 230555, 200, 196279],
    'Marzo': [29531, 186368, 966413, 236394, 274, 206491],
    'Abril': [33670, 183217, 925961, 226471, 386, 202160],
    'Mayo': [30349, 190890, 932369, 232625, 420, 218740],
    'Junio': [27434, 184099, 906495, 216070, 423, 194815],
    'Julio': [26144, 198499, 965177, 222723, 527, 221879],
    'Agosto': [26021, 194917, 946290, 223191, 527, 218107],
    'Septiembre': [26623, 186994, 902701, 210609, 526, 207311],
    'Octubre': [29061, 187269, 943883, 240412, 606, 210866],
    'Noviembre': [26129, 169688, 886073, 256438, 593, 211554],
    'Diciembre': [25692, 171453, 950733, 262935, 672, 235039]
}

# Convertir los datos a DataFrames
df_2023 = pd.DataFrame(data_2023)
df_2024 = pd.DataFrame(data_2024)

# Agregar columna "Año"
df_2023['Año'] = 2023
df_2024['Año'] = 2024

# Combinar ambos DataFrames
df = pd.concat([df_2023, df_2024])

# Transformar datos a formato largo para Plotly
df_largo = df.melt(id_vars=['Canal', 'Año'], var_name='Mes', value_name='Transacciones')

# Ordenar los meses correctamente
meses_ordenados = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                   'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
df_largo['Mes'] = pd.Categorical(df_largo['Mes'], categories=meses_ordenados, ordered=True)

# Crear la interfaz en Streamlit
st.title('Comparación de Transacciones')

# Filtro por canal
canal_seleccionado = st.selectbox('Selecciona el canal:', df_largo['Canal'].unique())

# Filtrar datos para el canal seleccionado
df_filtrado = df_largo[df_largo['Canal'] == canal_seleccionado]

# Crear gráfico
fig = px.line(
    df_filtrado,
    x='Mes',
    y='Transacciones',
    color='Año',
    title=f'Comparación de Transacciones ({canal_seleccionado})',
    labels={'Transacciones': 'Número de Transacciones'}
)

# Mostrar gráfico en Streamlit
st.plotly_chart(fig)
