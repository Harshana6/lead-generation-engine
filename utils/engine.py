import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def predict_lead(company, country, product, shipments, last_date):
    hot_markets = ['India', 'USA', 'Germany']
    imp = pd.read_csv("data/importyeti_mock_data.csv")
    hsn = pd.read_csv("data/hsn_master_complete.csv")
    df = imp.merge(hsn, on="product_description", how="left")
    df['last_shipment_date'] = pd.to_datetime(df['last_shipment_date'])
    df['recency_days'] = (pd.Timestamp.today() - df['last_shipment_date']).dt.days
    df['country_score'] = df['supplier_country'].isin(hot_markets).astype(int)
    df['product_score'] = df['product_description'].str.len()
    df['lead_quality'] = ((df['shipment_count'] > 50) & (df['recency_days'] < 180)).astype(int)

    X = df[['shipment_count', 'recency_days', 'country_score', 'product_score']]
    y = df['lead_quality']
    model = RandomForestClassifier()
    model.fit(X, y)

    country_score = 1 if country in hot_markets else 0
    recency_days = (pd.Timestamp.today() - pd.to_datetime(last_date)).days
    product_score = len(product)
    features = pd.DataFrame([[shipments, recency_days, country_score, product_score]],
                            columns=X.columns)
    proba = model.predict_proba(features)[0]
    return proba[1] if len(proba) > 1 else proba[0]