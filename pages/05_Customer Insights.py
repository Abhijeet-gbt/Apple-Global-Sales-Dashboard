import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
import streamlit as st
from utils.data_loader import load_data

df = load_data()
country = st.selectbox("Select Country",sorted(df["country"].unique()))

product_sale_by_country = df[df["country"] == country].groupby(["category","country"])["units_sold"].sum().sort_values(ascending=False).reset_index()

relation_dis_units_sold = (
    df[df["country"] == country]
    .groupby("category")
    .agg(
        units_sold=("units_sold", "sum"),      # total units sold
        discount_pct=("discount_pct", "mean")  # avg discount %
    )
    .reset_index()
)

st.write(relation_dis_units_sold)


fig,ax = plt.subplots(1,2,figsize = (16,8))

sns.barplot(product_sale_by_country,x = "category",y = "units_sold",edgecolor = "black",ax=ax[0])
ax[0].set_title(f"Product Sales In {country} country")
ax[0].set_xlabel(f"Category")
ax[0].set_ylabel(f"Units Sold")

sns.scatterplot(relation_dis_units_sold,x="units_sold",y="discount_pct",ax=ax[1],hue="category")
ax[1].set_title(f"Relation Between Discount(%) and Units Sold(📦) of {country} country")
ax[1].set_xlabel(f"Units Sold")
ax[1].set_ylabel(f"Discount %")

for _,row in relation_dis_units_sold.iterrows():
    ax[1].annotate(
        row["category"],
        xy = (row["units_sold"],row["discount_pct"]),
        xytext = (5,5),
        textcoords= "offset points",
        fontsize = 8
    )

plt.tight_layout()

st.pyplot(fig)



