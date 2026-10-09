
import os
import pandas as pd

from sklearn.ensemble import IsolationForest


class AnomalyDetectionAgent:

    def __init__(self, data_path):
        self.data_path = data_path
        self.df = pd.read_csv(data_path)

    def detect_anomalies(self, output_dir="outputs"):

        # Features used to identify unusual transactions
        features = [
            "quantity",
            "unit_price",
            "discount",
            "delivery_days",
            "customer_rating",
            "revenue"
        ]

        data = self.df[features].copy()

        # Configure Isolation Forest
        model = IsolationForest(
            n_estimators=100,
            contamination=0.05,
            random_state=42
        )

        # Fit model and classify transactions
        predictions = model.fit_predict(data)

        result = self.df.copy()

        # Isolation Forest: -1 = anomaly, 1 = normal
        result["anomaly_status"] = predictions
        result["anomaly_status"] = result["anomaly_status"].map({
            1: "Normal",
            -1: "Anomaly"
        })

        # Higher scores indicate more unusual observations
        result["anomaly_score"] = model.decision_function(data)

        # Keep anomalies first, most unusual at the top
        anomalies = (
            result[result["anomaly_status"] == "Anomaly"]
            .sort_values("anomaly_score", ascending=True)
        )

        # Save results
        os.makedirs(output_dir, exist_ok=True)

        all_results_path = os.path.join(
            output_dir,
            "anomaly_detection_results.csv"
        )

        anomalies_path = os.path.join(
            output_dir,
            "detected_anomalies.csv"
        )

        result.to_csv(all_results_path, index=False)
        anomalies.to_csv(anomalies_path, index=False)

        return {
            "total_transactions": len(result),
            "anomaly_count": len(anomalies),
            "normal_count": len(result) - len(anomalies),
            "anomaly_percentage": (
                len(anomalies) / len(result) * 100
            ),
            "all_results_path": all_results_path,
            "anomalies_path": anomalies_path,
            "anomalies": anomalies
        }
