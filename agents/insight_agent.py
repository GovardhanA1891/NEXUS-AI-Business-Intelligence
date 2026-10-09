class InsightAgent:

    def generate_insights(self, analysis):

        insights = []

        total_revenue = analysis["total_revenue"]

        # 1. Category insight
        category_revenue = analysis["category_revenue"]
        top_category = analysis["top_category"]

        top_category_revenue = category_revenue[top_category]

        category_percentage = (
            top_category_revenue / total_revenue
        ) * 100

        insights.append(
            f"{top_category} is the top revenue-generating category, "
            f"contributing {category_percentage:.1f}% of total revenue."
        )

        # 2. Region insight
        region_revenue = analysis["region_revenue"]
        top_region = analysis["top_region"]

        top_region_revenue = region_revenue[top_region]

        insights.append(
            f"{top_region} is the highest-revenue region, "
            f"generating {top_region_revenue:,.2f} in revenue."
        )

        # 3. Customer satisfaction insight
        average_rating = analysis["average_customer_rating"]

        if average_rating < 3:
            insights.append(
                f"The average customer rating is {average_rating:.2f}/5, "
                "indicating a potential customer satisfaction issue."
            )
        else:
            insights.append(
                f"The average customer rating is {average_rating:.2f}/5, "
                "indicating relatively positive customer satisfaction."
            )

        # 4. Delivery insight
        average_delivery = analysis["average_delivery_days"]

        if average_delivery > 5:
            insights.append(
                f"Average delivery time is {average_delivery:.2f} days, "
                "which may require delivery-performance investigation."
            )
        else:
            insights.append(
                f"Average delivery time is {average_delivery:.2f} days, "
                "indicating relatively efficient delivery."
            )

        # 5. Payment insight
        payment_method = analysis["most_used_payment_method"]

        insights.append(
            f"{payment_method} is the most frequently used payment method."
        )

        # 6. Data quality insight
        if analysis["missing_values"] == 0:
            insights.append(
                "The dataset contains no missing values."
            )
        else:
            insights.append(
                f"The dataset contains "
                f"{analysis['missing_values']} missing values "
                "that should be investigated."
            )

        if analysis["duplicate_rows"] == 0:
            insights.append(
                "No duplicate rows were detected in the dataset."
            )
        else:
            insights.append(
                f"{analysis['duplicate_rows']} duplicate rows were detected."
            )

        return insights