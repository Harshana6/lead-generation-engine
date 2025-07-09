import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.header("📈 Insights & Trends")

data = pd.read_csv("data/importyeti_mock_data.csv")
data['recency_days'] = (pd.Timestamp.today() - pd.to_datetime(data['last_shipment_date'])).dt.days

country_count = data['supplier_country'].value_counts()
st.subheader("Suppliers by Country")
st.bar_chart(country_count)

st.subheader("Shipment Volume vs Recency")
plt.scatter(data['shipment_count'], data['recency_days'], alpha=0.6)
plt.xlabel("Shipment Count")
plt.ylabel("Recency Days")
st.pyplot(plt)