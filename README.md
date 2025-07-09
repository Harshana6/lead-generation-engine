# 🚀 Lead Generation Engine Using Market Databases

This project is an AI-powered lead generation engine built using supplier trade data (ImportYeti-style) and product classification (HSN codes). It predicts high-potential leads based on shipment activity and product relevance.

## 📊 Project Overview

This tool was developed for **Xenhester Innovation Pvt. Ltd.** as part of an industry-defined problem. It helps businesses identify strong B2B leads by analyzing:
- Number of shipments
- Recency of supplier activity
- Country priority score
- Product detail and match with HSN codes

## 🛠 Features

- ✅ Streamlit multi-page web application
- ✅ Predict lead score based on custom inputs
- ✅ Visualize supplier insights (scatter plot, bar charts)
- ✅ Browse HSN codes and match products
- ✅ Log each prediction to CSV
- ✅ Works 100% offline after setup

## 🧠 Tech Stack

- **Python 3.10+**
- **Streamlit** – frontend dashboard
- **scikit-learn** – machine learning model (RandomForestClassifier)
- **pandas, matplotlib** – data handling and charts

## 📁 Folder Structure

```
LeadGen_FinalDashboard/
├── Home.py
├── pages/
│   ├── 1_Predict_Lead.py
│   ├── 2_Insights.py
│   └── 3_HSN_Browser.py
├── utils/
│   └── engine.py
├── data/
│   ├── importyeti_mock_data.csv
│   └── hsn_master_complete.csv
├── requirements.txt
└── prediction_log.csv (auto-created)
```

## 🚀 How to Run

1. **Clone the repo** or [Download ZIP](https://github.com/Harshana6/lead-generation-engine)
2. Open terminal and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run Home.py
   ```
4. Open browser at `http://localhost:8501`

## 📈 Sample Prediction

| Input | Value |
|-------|-------|
| Company | AquaPure Exports |
| Country | Germany |
| Product | Water Filtration Units |
| Shipments | 72 |
| Last Date | 2025-03-12 |

> Predicted Lead Score: **0.84** ✅ Strong Lead

## 📦 Future Enhancements

- Live API integration with ImportYeti
- User login system
- Export report as Excel or PDF
- Online deployment (Streamlit Cloud / Render)

## 🧑‍💻 Author

**Harshana Gohil**  
Final Year B.E. (Artificial Intelligence)  
[GitHub Profile](https://github.com/Harshana6)

---

*Built with ❤️ for  internship submission.*
