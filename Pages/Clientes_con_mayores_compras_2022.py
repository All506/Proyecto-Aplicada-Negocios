import streamlit as st
import pandas as pd
import altair as alt
from sqlalchemy import create_engine
import seaborn as sns
import numpy as np
import  matplotlib.pyplot as plt


#Subtitulo
st.subheader("Clientes con mayor volumen de compras de año 2022")

engine = create_engine("postgresql:///?user=odoo15&password=server&database=RizTech&host=172.23.84.89&port=5432")

df = pd.read_sql("SELECT RP.name AS Cliente, SUM(SOL.price_total) AS Total FROM sale_order_line SOL, sale_order SO, sale_order_line_invoice_rel SOLIR, account_move_line AML, res_partner RP WHERE SOL.order_id = SO.id AND SOL.id = SOLIR.order_line_id AND SOLIR.invoice_line_id = AML.id AND (extract(year from AML.date) = 2021) AND SO.partner_id = RP.id Group by Cliente Order by Total desc", engine)

df

chart = alt.Chart(df, height=500, width=0).mark_bar().encode(
        x=alt.X('cliente:O', sort=None),
        y=('sum(total):Q')
    )
 
st.altair_chart(chart, use_container_width=True)

