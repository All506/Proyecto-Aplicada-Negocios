from datetime import datetime
import yfinance as yf
import streamlit as st
import pandas as pd
import altair as alt
import psycopg2
from sqlalchemy import create_engine

st.set_page_config(page_title="Visitas del Mes", page_icon="📈")

st.subheader("Visitas de " + datetime.now().strftime("%B"))

engine = create_engine("postgresql:///?user=odoo15&password=server&database=RizTech&host=172.23.84.89&port=5432")

df = pd.read_sql("SELECT COUNT(*) AS \"Ingresos\", date_part('day',(wt.visit_datetime)) as \"Dia\", TO_CHAR(wt.visit_datetime,'Day') AS \"Día de la semana\" FROM website_track wt WHERE date_part('month',(wt.visit_datetime)) = date_part('month', (SELECT current_timestamp)) AND date_part('year', (SELECT current_timestamp)) = date_part('year',(wt.visit_datetime)) GROUP BY date_part('day',(wt.visit_datetime)), TO_CHAR(wt.visit_datetime,'Day')", engine)


bar_chart = alt.Chart(df, height=500, width=0).mark_bar().encode(
        x="Dia",
        y=alt.Y("Ingresos", sort="x"),
    )
 
st.altair_chart(bar_chart, use_container_width=True)

st.button("Re-run")