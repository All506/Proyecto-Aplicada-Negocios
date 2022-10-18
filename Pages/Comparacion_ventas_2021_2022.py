import streamlit as st
import pandas as pd
import altair as alt
from sqlalchemy import create_engine
import seaborn as sns
import numpy as np
import  matplotlib.pyplot as plt


#Subtitulo
st.subheader("Comparación de las ventas de 2021 y 2022")

engine = create_engine("postgresql:///?user=odoo15&password=server&database=RizTech&host=172.23.84.89&port=5432")

df = pd.read_sql("SELECT extract(year from AML.date) AS Anho, TO_CHAR(AML.date, 'MONTH') AS Mes, extract(month from AML.date) AS Mesnum, SUM(SOL.price_total) AS Total  FROM sale_order_line SOL, sale_order SO, sale_order_line_invoice_rel SOLIR, account_move_line AML WHERE SOL.order_id = SO.id AND SOL.id = SOLIR.order_line_id AND SOLIR.invoice_line_id = AML.id AND (extract(year from AML.date) = 2021 OR extract(year from AML.date) = 2022) GROUP BY Mes, MESNUM, Anho ORDER BY MESNUM", engine)

df

chart=alt.Chart(df, height=500, width=38).mark_bar().encode(
        x=alt.X('anho:O', sort=None),
        y=alt.Y('total:Q', sort=None),
        color='anho:N',
        column = alt.Column("mes", sort=["JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SETEMBER","OCTOBER","NOVEMBER","DECEMBER"])
    )
 
st.altair_chart(chart, use_container_width=False)
