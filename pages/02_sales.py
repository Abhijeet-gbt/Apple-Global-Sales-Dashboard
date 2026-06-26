import streamlit as st 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
from utils.data_loader import load_data

df = load_data()

st.title("Sales Analysis 🔥")

country = st.selectbox("Select Country",sorted(df["country"].unique()))

filtered_df = (
    df[df["country"] == country].groupby("city")["revenue_usd"].sum().sort_values(ascending = False).head(5).reset_index()
)

fig,ax = plt.subplots(figsize = (10,8))

sns.barplot(data=filtered_df,y = "revenue_usd",
            x = "city",
            ax = ax,edgecolor = "black"
            )
plt.xlabel(f"City")
plt.ylabel(f"USD Revenue")
ax.set_title(f"Top 5 Cities by USD Revenue of {country} country")
plt.xticks(rotation = 45)
plt.tight_layout()
st.pyplot(fig,ax)

st.write(filtered_df)