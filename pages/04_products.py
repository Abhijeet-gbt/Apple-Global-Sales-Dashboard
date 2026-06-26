import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt 
import seaborn as sns
from utils.data_loader import load_data

st.title("Product Sales Dashboard")
df = load_data()

region = st.selectbox("Select Region",sorted(df["region"].unique()))

filitered_df = df[df["region"] == region].groupby(["year","category"])["units_sold"].sum().sort_values(ascending = True).reset_index()

st.write("In almost every Year and Region ther Iphone is dominated by Units Sold but Mac also show a significant Growth ")
fig,ax = plt.subplots(figsize = (10,8))

sns.barplot(filitered_df,x="category",y="units_sold",hue="year",palette="Set2",edgecolor = "black")
ax.set_title(f"Product Sales of Each Year of {region} Region")
plt.xlabel(f"Category")
plt.ylabel(f"Units Sold")
plt.tight_layout()
st.pyplot(fig,ax)

st.write(filitered_df)