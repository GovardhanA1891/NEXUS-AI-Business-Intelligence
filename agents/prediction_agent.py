
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.dummy import DummyRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


class PredictionAgent:

    def __init__(self, data_path):
        self.data_path = data_path
        self.df = pd.read_csv(data_path)

    def train_model(self):

        # Features used to predict revenue
        X = self.df[
            [
                "quantity",
                "unit_price",
                "discount",
                "product_category",
                "region",
                "payment_method",
                "delivery_days",
                "customer_rating"
            ]
        ]

        # Target variable
        y = self.df["revenue"]

        # Categorical features
        categorical_features = [
            "product_category",
            "region",
            "payment_method"
        ]

        # Preprocessing pipeline
        preprocessor = ColumnTransformer(
            transformers=[
                (
                    "categorical",
                    OneHotEncoder(handle_unknown="ignore"),
                    categorical_features
                )
            ],
            remainder="passthrough"
        )

        # Random Forest regression model
        model = RandomForestRegressor(
            n_estimators=100,
            random_state=42
        )

        pipeline = Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                ("model", model)
            ]
        )

        # Split into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        # Train Random Forest
        pipeline.fit(X_train, y_train)

        # Generate predictions
        predictions = pipeline.predict(X_test)

        # Baseline model predicts the training-set mean
        baseline = DummyRegressor(strategy="mean")
        baseline.fit(X_train, y_train)

        baseline_predictions = baseline.predict(X_test)

        # Evaluate Random Forest
        mae = mean_absolute_error(y_test, predictions)

        rmse = mean_squared_error(
            y_test,
            predictions
        ) ** 0.5

        r2 = r2_score(y_test, predictions)

        # Evaluate baseline
        baseline_mae = mean_absolute_error(
            y_test,
            baseline_predictions
        )

        baseline_rmse = mean_squared_error(
            y_test,
            baseline_predictions
        ) ** 0.5

        baseline_r2 = r2_score(
            y_test,
            baseline_predictions
        )

        # Validate the revenue formula
        calculated_revenue = (
            self.df["quantity"]
            * self.df["unit_price"]
            * (1 - self.df["discount"])
        )

        formula_match_percentage = (
            (
                self.df["revenue"].round(2)
                == calculated_revenue.round(2)
            ).mean() * 100
        )

        return {
            "model": pipeline,
            "mae": mae,
            "rmse": rmse,
            "r2": r2,
            "baseline_mae": baseline_mae,
            "baseline_rmse": baseline_rmse,
            "baseline_r2": baseline_r2,
            "formula_match_percentage": formula_match_percentage
        }
