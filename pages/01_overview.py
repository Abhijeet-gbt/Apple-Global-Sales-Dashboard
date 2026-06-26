import pandas as pd 
import streamlit as st 
from utils.data_loader import load_data

load_data()
df = load_data()

total_revenue = df["revenue_usd"].sum()
total_units_sold = df["units_sold"].sum()

col1,col2 = st.columns(2)

with col1:
    st.metric(
        label= "💰 Total Revenue",
        value=f"${total_revenue:,.0f}"
    )
    
with col2:
    st.metric(
        label="📦 Units Sold",
        value=f"{total_units_sold:,}"
    )
    
st.write("There are $18,035,669 💵 Revenue is generated in Dollars from all over and",
         "\n 23,270 Units 📦 are sold of different Categories")


st.write(df)

st.write("Missing Values")
st.write(df.isnull().sum())

st.write("Statistical summary")
st.write(df.describe())

st.write("Dtypes")
st.write(df.dtypes)