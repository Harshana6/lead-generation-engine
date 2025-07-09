import streamlit as st
from utils.engine import predict_lead
import pandas as pd
import matplotlib.pyplot as plt
import os

st.header("🎯 Predict Lead Score")

company = st.text_input("Company Name")
country = st.selectbox("Supplier Country", ["India", "USA", "Germany", "China", "Other"])
product = st.text_input("Product Description")
shipments = st.slider("Number of Shipments", 0, 200, 50)
last_date = st.date_input("Last Shipment Date")

if st.button("Predict"):
    score = predict_lead(company, country, product, shipments, str(last_date))
    st.success(f"📈 Lead Score: {score:.2f}")

    # Log result
    df = pd.DataFrame([[company, country, product, shipments, last_date, round(score, 2)]],
                      columns=["Company", "Country", "Product", "Shipments", "Last Shipment", "Score"])
    df.to_csv("data/prediction_log.csv", mode='a', index=False, header=not os.path.exists("data/prediction_log.csv"))

    # Chart
    data = pd.read_csv("data/importyeti_mock_data.csv")
    data['recency_days'] = (pd.Timestamp.today() - pd.to_datetime(data['last_shipment_date'])).dt.days
    plt.scatter(data['shipment_count'], data['recency_days'], c='orange', alpha=0.6)
    plt.xlabel("Shipment Count")
    plt.ylabel("Recency Days")
    st.pyplot(plt)