import pandas as pd
import streamlit as st 

@st.cache_data() #cahce data so it doesn't reload every click 
def load_data():
    df = pd.read_csv("apple_global_sales_dataset.csv")
    df["sale_date"] = pd.to_datetime(df["sale_date"])
    df["customer_rating"].fillna(df["customer_rating"].median(), inplace=True)
    return df

