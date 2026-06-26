import streamlit as st 

st.set_page_config(
    page_title="Apple Global Sales Dashboard",
    page_icon="🍎",
    layout="wide"
)

pg = st.navigation([
    st.Page("pages/01_overview.py",title="Overview",icon="🏡"),
    st.Page("pages/02_sales.py",title="Sales",icon="💰"),
    st.Page("pages/03_Trends_.py",title="Trend",icon="📊"),
    st.Page("pages/04_products.py",title="Products",icon="📦"),
    st.Page("pages/05_Customer Insights.py",title = "Customer Insights",icon = "🌌")
])

pg.run()

    