import streamlit as st
import pandas as pd

st.header("🧾 HSN Code Browser")

df = pd.read_csv("data/hsn_master_complete.csv")
search = st.text_input("Search product...")
if search:
    results = df[df['product_description'].str.contains(search, case=False)]
    st.dataframe(results)
else:
    st.dataframe(df)