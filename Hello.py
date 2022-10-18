import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="RyzAnalysis Main Page",
    page_icon="👋",
)

st.write("# Bienvenido a RyzAnalysis! 👋")

st.sidebar.success("Seleccione un gráfico para mostrar")

st.markdown(
    """
    RyzAnalysis es una herramienta personalizada
    para el análisis de la información recompilada
    a través del tiempo en el manejo del ERP de la compañia.
    Con RyzAnalysis, la empresa será capaz de visualizar
    de una forma sencilla toda la información importante
    relacionada al manejo de la empresa con el fin de tomar
    decisiones empresarial y eficientemente inteligentes.
"""
)

image = Image.open('./Resources/graph.webp')
st.image(image, caption='El análisis de información importante puede conducir al cumplimiento de las metas propuestas por su compañía')