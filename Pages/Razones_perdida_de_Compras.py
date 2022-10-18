import yfinance as yf
import streamlit as st
import pandas as pd
import altair as alt
import psycopg2
from sqlalchemy import create_engine

st.set_page_config(page_title="Principales motivos de perdida de compras", page_icon="📈")


engine = create_engine("postgresql:///?user=odoo15&password=server&database=RizTech&host=172.23.84.89&port=5432")

st.subheader("Principales motivos de perdida de compras")

df = pd.read_sql("SELECT count(CLL.id) AS \"Cantidad\", CLR.name AS \"Razon\" FROM crm_lead_lost CLL, crm_lost_reason CLR WHERE CLL.lost_reason_id = CLR.id GROUP BY CLR.name", engine)


bar_chart = alt.Chart(df, height=500, width=0).mark_bar().encode(
        x="Cantidad",
        y=alt.Y("Razon", sort="-x"),
    )
 
st.altair_chart(bar_chart, use_container_width=True)


