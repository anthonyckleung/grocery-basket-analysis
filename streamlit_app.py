"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import plotly.express as px 
import pandas as pd
from pyvis.network import Network
from millify import prettify

st.set_page_config(layout="wide")

ar_df = pd.read_csv('data/ar_results.csv')

item_df = pd.read_csv('data/popular_product.csv')
item_df = item_df[:20]
# ar_df.head()

# Network Graph
HtmlFile = open(f'html/pyvis_graph.html', 'r', encoding='utf-8')
source_code = HtmlFile.read()

container_1 = st.container()
container_2 = st.container()
container_3 = st.container()



with container_1:
  st.title(':basket: Supermarket Basket Analysis Dashboard')
  col1, col2, col3 = st.columns(3)
  col1.metric(label='No. Transactions', value=prettify(1384617), delta='4% (Month-over-Month)')
  col2.metric(label='Avg. Basket Size per Transaction', value=31, delta='0.7% (Month-over-Month)')


with container_2:
  
  st_col1, st_col2 = st.columns([1,1])

  with st_col1:
    st.header('Basket Analysis Network')
    st.components.v1.html(source_code, height=500)
  
  with st_col2:
    st.header('Top 20 Popular Products')
    fig=px.bar(item_df,
      x='purchase_count',
      y='product_name', 
      orientation='h',
      height = 500,
    )
    fig.update_layout(yaxis=dict(autorange="reversed"))
    st.write(fig)




with container_3:
  st.header('Top 200 Association Results')
  st.dataframe(data =ar_df, height=500)