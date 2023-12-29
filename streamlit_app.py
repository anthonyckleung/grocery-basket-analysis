"""
# Supermarket Basket Analysis Streamlit App
# Created by: Anthony Leung 
# github repo: https://github.com/anthonyckleung/grocery-basket-analysis
"""

import streamlit as st
import plotly.express as px 
import pandas as pd
from millify import prettify

st.set_page_config(layout="wide")

ar_df = pd.read_csv('data/ar_results.csv')

item_df = pd.read_csv('data/popular_product.csv')
aisle_df = pd.read_csv('data/popular_aisle.csv')
department_df = pd.read_csv('data/popular_department.csv')

# Truncate data to top 20
item_df = item_df[:20]
aisle_df = aisle_df[:20]
department_df= department_df[:20]


# Load Network Graph
HtmlFile = open(f'html/pyvis_graph.html', 'r', encoding='utf-8')
source_code = HtmlFile.read()

container_1 = st.container()
container_2 = st.container()
container_3 = st.container()


# Container 1: Metrics
with container_1:
  st.header(':basket: Supermarket Basket Analysis Dashboard', divider='gray')
  col1, col2, col3 = st.columns(3)
  col1.metric(label='No. Order', value=prettify(1384617), delta='4% (Month-over-Month)')
  col2.metric(label='Avg. Basket Size per Order', value=31, delta='0.7% (Month-over-Month)')
  st.divider()


# Container 2: Order Statistics
with container_2:
  st_col1, st_col2, st_col3 = st.columns(3)

  with st_col1:
    st.header('Top 20 Orders by Product')
    fig=px.bar(item_df,
      x='purchase_count',
      y='product_name', 
      orientation='h',
      labels={
        'purchase_count': 'No. of Orders',
        'product_name': 'Product Name'
      },
      height = 500,
    )
    fig.update_layout(yaxis=dict(autorange="reversed"))
    st.write(fig)

  with st_col2:
    st.header('Top 20 Orders by Aisle')
    fig=px.bar(aisle_df,
      x='purchase_count',
      y='aisle', 
      orientation='h',
      labels={
        'purchase_count': 'No. of Orders',
        'aisle': 'Aisle'
      },
      height = 500,
    )
    fig.update_layout(yaxis=dict(autorange="reversed"))
    st.write(fig)

  with st_col3:
    st.header('Top 20 Orders by Department')
    fig=px.bar(department_df,
      x='purchase_count',
      y='department', 
      orientation='h',
      labels={
        'purchase_count': 'No. of Orders',
        'department': 'Department'
      },
      height = 500,
    )
    fig.update_layout(yaxis=dict(autorange="reversed"))
    st.write(fig)
  st.divider()


# Container 3: Network Analysis
with container_3:
  
  st_col1, st_col2 = st.columns([2,1])

  with st_col1:
    st.header('Basket Analysis Network')
    st.components.v1.html(source_code, height=500)
  
  with st_col2:
    st.header('Top 200 Association Results')
    st.dataframe(data =ar_df, height=500)


