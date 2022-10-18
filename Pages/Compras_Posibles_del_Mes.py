import yfinance as yf
import streamlit as st
import pandas as pd
import altair as alt
import psycopg2
from sqlalchemy import create_engine

st.set_page_config(page_title="Productos Más Vendidos", page_icon="📈")
engine = create_engine("postgresql:///?user=odoo15&password=server&database=RizTech&host=172.23.84.89&port=5432")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Posibles compras del mes actual")

    df = pd.read_sql("SELECT COUNT(CLead.id) AS \"Cantidad\", TO_CHAR(CLead.create_date,'Month') as \"Mes\" FROM crm_lead CLead WHERE date_part('month',(CLead.create_date)) = date_part('month', (SELECT current_timestamp)) and date_part('year', (SELECT current_timestamp)) = date_part('year',(CLead.create_date)) AND CLead.stage_id = 4 AND CLead.active = true GROUP BY TO_CHAR(CLead.create_date,'Month')", engine)
    
    chart_data = alt.Chart(df, height=500, width=0).mark_bar().encode(
            x="Mes",
            y=alt.Y("Cantidad", sort="x"),
        )
    
    st.altair_chart(chart_data, use_container_width=True)

with col2:

    st.subheader("Posibles compras perdidas del mes actual")

    df = pd.read_sql("SELECT COUNT(CLead.id) AS \"Cantidad\", TO_CHAR(CLead.create_date,'Month') as \"Mes\" FROM crm_lead_lost CLead, crm_lead CLead2 WHERE date_part('month',(CLead.create_date)) = date_part('month', (SELECT current_timestamp)) and date_part('year', (SELECT current_timestamp)) = date_part('year',(CLead.create_date)) AND CLead2.active = false GROUP BY TO_CHAR(CLead.create_date,'Month')", engine)
    
    chart_data = alt.Chart(df, height=500, width=0).mark_bar().encode(
            x="Mes",
            y=alt.Y("Cantidad", sort="-x"),
        )
    
    st.altair_chart(chart_data, use_container_width=True)
    
st.button("Re-run")
