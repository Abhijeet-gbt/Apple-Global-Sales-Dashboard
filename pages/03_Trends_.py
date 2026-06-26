import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt
import seaborn as sns 
from utils.data_loader import load_data

df = load_data()

st.title("Trends Analysis 📈")

month_order = ["January","February","March","April","May","June",
               "July","August","September","October","November","December"]



df["sale_date"] = pd.to_datetime(df["sale_date"])

country = st.selectbox("Select Country",sorted(df["country"].unique()))

filitered__df = (df[(df["country"] == country)].groupby(["month","year"])["revenue_usd"].sum().reset_index())

filitered__df["month"] = pd.Categorical(filitered__df["month"],
                                        categories= month_order,
                                        ordered=True)

st.write("In year by year there is significant growth in Revenue in the last Months of the year")

fig,ax = plt.subplots(figsize = (10,8))

sns.lineplot(filitered__df,x="month",y="revenue_usd",hue="year",palette="bright")
ax.set_title(f"Month Wise {country} Sales Trend")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue")
plt.tight_layout()
st.pyplot(fig,ax)

st.write(filitered__df)