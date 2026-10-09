import pandas as pd


class DataAnalystAgent:

    def __init__(self, data_path):
        self.data_path = data_path
        self.df = pd.read_csv(data_path)

    def analyze(self):

        analysis = {}

        # Basic dataset information
        analysis["total_orders"] = len(self.df)
        analysis["total_customers"] = self.df["customer_id"].nunique()

        # Revenue metrics
        analysis["total_revenue"] = self.df["revenue"].sum()
        analysis["average_revenue"] = self.df["revenue"].mean()
        analysis["highest_revenue"] = self.df["revenue"].max()
        analysis["lowest_revenue"] = self.df["revenue"].min()

        # Quantity and delivery metrics
        analysis["average_quantity"] = self.df["quantity"].mean()
        analysis["average_delivery_days"] = self.df["delivery_days"].mean()

        # Customer satisfaction
        analysis["average_customer_rating"] = self.df["customer_rating"].mean()

        # Data quality
        analysis["missing_values"] = self.df.isnull().sum().sum()
        analysis["duplicate_rows"] = self.df.duplicated().sum()

        # Best performing category
        category_revenue = (
            self.df.groupby("product_category")["revenue"]
            .sum()
            .sort_values(ascending=False)
        )

        analysis["top_category"] = category_revenue.index[0]
        analysis["category_revenue"] = category_revenue.to_dict()

        # Best performing region
        region_revenue = (
            self.df.groupby("region")["revenue"]
            .sum()
            .sort_values(ascending=False)
        )

        analysis["top_region"] = region_revenue.index[0]
        analysis["region_revenue"] = region_revenue.to_dict()

        # Payment method analysis
        payment_counts = self.df["payment_method"].value_counts()

        analysis["most_used_payment_method"] = payment_counts.index[0]
        analysis["payment_method_usage"] = payment_counts.to_dict()

        return analysis