## Live Demo

**Try NEXUS online:** [Launch NEXUS AI Business Intelligence](https://govardhana1891-nexus-ai-business-intelligence-app-hdf5r1.streamlit.app)

Explore sales analytics, business insights, machine learning model evaluation, and anomaly detection through the interactive dashboard.

# NEXUS — AI Multi-Agent Business Intelligence

NEXUS is a Python-based business intelligence application that combines data analysis, automated business insights, machine learning evaluation, and anomaly detection in an interactive Streamlit dashboard.

The project analyzes e-commerce transaction data and presents business metrics and visualizations to support data-driven decision-making.

## Features

- **Data Analysis Agent:** Calculates revenue, order, customer, category, regional, and operational metrics.
- **Business Insight Agent:** Generates findings from analyzed business data.
- **Revenue Prediction Agent:** Trains and evaluates a Random Forest regression model and compares it with a baseline.
- **Anomaly Detection Agent:** Uses Isolation Forest to flag unusual transactions for further investigation.
- **Interactive Dashboard:** Displays KPIs, category and regional revenue, monthly trends, business insights, model metrics, and anomaly results.
- **Transaction Filtering:** Filters sales records by product category and region.
- **CSV Export:** Downloads filtered transactions and detected anomaly records.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Pandas | Data processing and analysis |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning and anomaly detection |
| Plotly | Interactive charts |
| Streamlit | Interactive web dashboard |

## Project Structure

```text
AI-Multi-Agent-Business-Analyst/
├── agents/
│   ├── data_analyst_agent.py
│   ├── insight_agent.py
│   ├── prediction_agent.py
│   └── anomaly_detection_agent.py
├── data/
│   └── ecommerce_sales_analytics_5000.csv
├── outputs/
│   ├── anomaly_detection_results.csv
│   └── detected_anomalies.csv
├── app.py
├── test_agent.py
├── inspect_data.py
├── .gitignore
└── README.md
```

## Dataset

The application uses an e-commerce transaction dataset containing 5,000 records and 12 columns.

The fields include:

- Order ID and order date
- Customer ID
- Product category and region
- Quantity and unit price
- Discount and payment method
- Delivery duration and customer rating
- Revenue

## Dashboard Pages

### 1. Executive Overview
Summarizes revenue, orders, customers, customer ratings, delivery duration, top-performing categories, and regional performance. Includes a monthly revenue trend.

### 2. Sales Analytics
Compares category and regional revenue, supports interactive filters, and provides filtered transaction downloads.

### 3. Business Insights
Displays automatically generated findings and data quality indicators.

### 4. ML Model Evaluation
Reports Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R². It also compares the Random Forest model with a baseline predictor.

### 5. Anomaly Detection
Displays potentially unusual transactions identified using Isolation Forest, with a sortable results table and CSV export.

## Installation and Setup

### Prerequisites

- Python 3.10 or newer
- pip
- Visual Studio Code (recommended)

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AI-Multi-Agent-Business-Analyst
```

Replace the placeholder with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install pandas numpy scikit-learn matplotlib seaborn plotly streamlit
```

### 4. Run the dashboard

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal, normally:

```text
http://localhost:8501
```

### 5. Run the agent test script

```bash
python test_agent.py
```

## Machine Learning Notes

The revenue model is evaluated using a train/test split and compared against a simple mean-prediction baseline.

**Important limitation:** Revenue in this dataset is derived from quantity, unit price, and discount. Using these fields to predict revenue can produce deceptively strong evaluation results because the target is mathematically determined by the inputs.

Consequently, the reported R² should not be interpreted as evidence of real-world future forecasting performance. A more realistic forecasting task would predict future-period revenue using historical data and features available before the prediction period.

The anomaly detector identifies statistically unusual records; flagged records are candidates for investigation, not confirmed fraud or errors.

## Current Dataset Scope

The dashboard reports historical aggregates from the supplied dataset. The monthly trend reflects dates contained in the dataset and is not a forecast.

## Future Improvements

- Add date-range and aggregation filters.
- Improve automated insight prioritization.
- Add time-based revenue forecasting with appropriate validation.
- Expand model diagnostics and anomaly explanations.
- Add automated tests and stronger data validation.
- Deploy the dashboard to a public hosting platform.

## Author

Developed as an AI and machine learning portfolio project to demonstrate data analytics, machine learning, anomaly detection, and dashboard development.




## Dashboard Screenshots

### 1. Executive Overview — KPIs and Revenue
![Executive Overview](assets/Screenshot%202026-10-09%20103554.png)

### 2. Executive Overview — Monthly Revenue Trend
![Monthly Revenue Trend](assets/Screenshot%202026-10-09%20103752.png)

### 3. Executive Overview — Business Highlights
![Business Highlights](assets/Screenshot%202026-10-09%20103922.png)

### 4. Sales Analytics — Revenue by Category and Region
![Sales Analytics](assets/Screenshot%202026-10-09%20104014.png)

### 5. Sales Analytics — Transaction Explorer
![Transaction Explorer](assets/Screenshot%202026-10-09%20104051.png)

### 6. Business Insights — Key Findings
![Business Insights](assets/Screenshot%202026-10-09%20104155.png)

### 7. Business Insights — Additional Findings
![Additional Business Insights](assets/Screenshot%202026-10-09%20104219.png)

### 8. Machine Learning — Model Evaluation
![Model Evaluation](assets/Screenshot%202026-10-09%20104256.png)

### 9. Anomaly Detection — Flagged Transactions
![Anomaly Detection](assets/Screenshot%202026-10-09%20104402.png)

### 10. Anomaly Detection — Transaction Details
![Anomaly Transaction Details](assets/Screenshot%202026-10-09%20104430.png)

### 11. Dashboard Navigation
![Dashboard Navigation](assets/Screenshot%202026-10-09%20104456.png)
