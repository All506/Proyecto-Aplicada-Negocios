import yfinance as yf
import streamlit as st
import pandas as pd
import altair as alt
import psycopg2
from sqlalchemy import create_engine

st.set_page_config(page_title="Productos Más Vendidos", page_icon="📈")

engine = create_engine("postgresql:///?user=odoo15&password=server&database=RizTech&host=172.23.84.89&port=5432")

st.subheader("Tipos de Producto más vendidos")

df = pd.read_sql("SELECT SUM(PT.list_price) AS \"Monto Compra\", CASE PT.detailed_type WHEN 'consu' THEN 'Consult' WHEN 'product' THEN 'Product' WHEN 'service' THEN 'Servicie' END \"Tipo Compra\" FROM product_template PT WHERE purchase_ok = true GROUP BY PT.detailed_type", engine)


bar_chart = alt.Chart(df, height=500, width=0).mark_bar().encode(
        x="Tipo Compra",
        y=alt.Y("Monto Compra", sort="-x"),
        #color=alt.condition(
            #alt.datum.presented_value > alt.datum.coloring_value,
            #alt.value('lightgreen'),
            #alt.value('lightgray')
        #)

    )
 
st.altair_chart(bar_chart, use_container_width=True)




# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.