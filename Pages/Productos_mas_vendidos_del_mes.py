import yfinance as yf
import streamlit as st
import pandas as pd
import altair as alt
import psycopg2
from sqlalchemy import create_engine

#Subtitulo
st.subheader("Productos más vendidos en el último mes")

engine = create_engine("postgresql:///?user=odoo15&password=server&database=RizTech&host=172.23.84.89&port=5432")

df = pd.read_sql("select PT.name as \"Product name\" ,sum(product_uom_qty) as \"Unidades vendidas\" from sale_order_line SO, product_template PT where PT.id = SO.product_id and SO.write_date > now() - interval '1 month' group by PT.name ORDER BY \"Unidades vendidas\" DESC LIMIT 10 ", engine)

bar_chart = alt.Chart(df, height=500, width=0).mark_bar().encode(
        x="Unidades vendidas",
        y=alt.Y("Product name", sort="-x"),
    )
 
st.altair_chart(bar_chart, use_container_width=True)