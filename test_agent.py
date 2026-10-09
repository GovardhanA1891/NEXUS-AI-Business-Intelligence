
from agents.data_analyst_agent import DataAnalystAgent
from agents.insight_agent import InsightAgent
from agents.prediction_agent import PredictionAgent
from agents.anomaly_detection_agent import AnomalyDetectionAgent


DATA_PATH = "data/ecommerce_sales_analytics_5000.csv"


# ==========================================
# AGENT 1: DATA ANALYST
# ==========================================

data_agent = DataAnalystAgent(DATA_PATH)
analysis = data_agent.analyze()

print("\n===== AGENT 1: DATA ANALYST REPORT =====")

for key, value in analysis.items():
    print(f"{key}: {value}")


# ==========================================
# AGENT 2: BUSINESS INSIGHT AGENT
# ==========================================

insight_agent = InsightAgent()
insights = insight_agent.generate_insights(analysis)

print("\n===== AGENT 2: BUSINESS INSIGHTS =====")

for insight in insights:
    print("-", insight)


# ==========================================
# AGENT 3: PREDICTION AGENT
# ==========================================

prediction_agent = PredictionAgent(DATA_PATH)
prediction_results = prediction_agent.train_model()

print("\n===== AGENT 3: REVENUE PREDICTION =====")

print(f"Random Forest MAE: {prediction_results['mae']:.2f}")
print(f"Random Forest RMSE: {prediction_results['rmse']:.2f}")
print(f"Random Forest R²: {prediction_results['r2']:.4f}")

print("\n--- Baseline Comparison ---")

print(f"Baseline MAE: {prediction_results['baseline_mae']:.2f}")
print(f"Baseline RMSE: {prediction_results['baseline_rmse']:.2f}")
print(f"Baseline R²: {prediction_results['baseline_r2']:.4f}")

print("\n--- Revenue Formula Validation ---")

print(
    "Rows matching revenue formula: "
    f"{prediction_results['formula_match_percentage']:.2f}%"
)


# ==========================================
# AGENT 4: ANOMALY DETECTION
# ==========================================

anomaly_agent = AnomalyDetectionAgent(DATA_PATH)
anomaly_results = anomaly_agent.detect_anomalies()

print("\n===== AGENT 4: ANOMALY DETECTION =====")

print(
    f"Total transactions: "
    f"{anomaly_results['total_transactions']}"
)

print(
    f"Normal transactions: "
    f"{anomaly_results['normal_count']}"
)

print(
    f"Detected anomalies: "
    f"{anomaly_results['anomaly_count']}"
)

print(
    f"Anomaly percentage: "
    f"{anomaly_results['anomaly_percentage']:.2f}%"
)

print(
    f"All results saved to: "
    f"{anomaly_results['all_results_path']}"
)

print(
    f"Anomalies saved to: "
    f"{anomaly_results['anomalies_path']}"
)


print("\n===== ALL 4 AGENTS COMPLETED =====")
