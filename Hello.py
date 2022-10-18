import streamlit as st
import pandas as pd
import altair as alt
from sqlalchemy import create_engine
import seaborn as sns
import numpy as np
import  matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(
    page_title="RyzAnalysis Main Page",
    page_icon="👋",
)

st.write("# Bienvenido a RyzAnalysis! 👋")

st.sidebar.success("Seleccione un gráfico para mostrar")

def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def Clientes_con_mayores_compras_2022():
    st.subheader("Clientes con mayor volumen de compras de año 2022")

    engine = create_engine("postgresql:///?user=odoo15&password=server&database=RizTech&host=172.23.84.89&port=5432")

    df = pd.read_sql("SELECT RP.name AS Cliente, SUM(SOL.price_total) AS Total FROM sale_order_line SOL, sale_order SO, sale_order_line_invoice_rel SOLIR, account_move_line AML, res_partner RP WHERE SOL.order_id = SO.id AND SOL.id = SOLIR.order_line_id AND SOLIR.invoice_line_id = AML.id AND (extract(year from AML.date) = 2021) AND SO.partner_id = RP.id Group by Cliente Order by Total desc", engine)

    df

    chart = alt.Chart(df, height=500, width=0).mark_bar().encode(
            x=alt.X('cliente:O', sort=None),
            y=('sum(total):Q')
        )
    
    st.altair_chart(chart, use_container_width=True)


def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": Clientes_con_mayores_compras_2022,
    "Page 3": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

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
