
import os
import pandas as pd
import streamlit as st
import plotly.express as px

from agents.data_analyst_agent import DataAnalystAgent
from agents.insight_agent import InsightAgent
from agents.prediction_agent import PredictionAgent
from agents.anomaly_detection_agent import AnomalyDetectionAgent


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="NEXUS | Business Intelligence",
    page_icon="N",
    layout="wide",
    initial_sidebar_state="expanded"
)

DATA_PATH = "data/ecommerce_sales_analytics_5000.csv"


# =========================================================
# PREMIUM UI STYLING
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
    --bg: #F4F6FB;
    --surface: #FFFFFF;
    --navy: #111B32;
    --primary: #4F46E5;
    --text: #172033;
    --muted: #68758A;
    --border: #E3E8F1;
    --shadow: 0 5px 20px rgba(24, 39, 75, 0.045);
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: var(--bg);
    color: var(--text);
}

[data-testid="stHeader"] {
    background: rgba(244, 246, 251, 0.94);
}

[data-testid="stAppViewContainer"] .main .block-container {
    max-width: 1700px;
    padding: 2.2rem 2.6rem 3rem;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111B32 0%, #172642 100%);
    border-right: 1px solid #263552;
}

[data-testid="stSidebar"] * {
    color: #E8EDF8;
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #AEBBD1;
    line-height: 1.65;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label {
    border-radius: 9px;
    padding: 0.5rem 0.65rem;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background: #273753;
}

.brand {
    font-family: 'Manrope', sans-serif;
    font-size: 1.8rem;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: #FFFFFF;
    margin: 0.4rem 0 0.2rem;
}

.brand span {
    color: #8FA2FF;
}

.brand-subtitle {
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 2px;
    color: #AEBBD1;
    margin-bottom: 1.8rem;
}

.page-eyebrow {
    font-size: 0.73rem;
    font-weight: 700;
    letter-spacing: 2px;
    color: var(--primary);
    margin-bottom: 0.55rem;
}

.page-title {
    font-family: 'Manrope', sans-serif;
    font-size: clamp(1.8rem, 2.6vw, 2.5rem);
    font-weight: 800;
    line-height: 1.2;
    letter-spacing: -0.8px;
    color: #121C30;
    margin-bottom: 0.65rem;
}

.page-description {
    color: var(--muted);
    font-size: 0.98rem;
    line-height: 1.7;
    margin-bottom: 2rem;
    max-width: 850px;
}

.section-heading {
    font-family: 'Manrope', sans-serif;
    color: #172033;
    font-size: 1.22rem;
    font-weight: 800;
    letter-spacing: -0.3px;
    margin: 1.9rem 0 1rem;
}

.kpi-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 15px;
    padding: 1.35rem 1.3rem;
    min-height: 142px;
    box-shadow: var(--shadow);
    transition: transform 0.18s ease, box-shadow 0.18s ease;
}

.kpi-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 9px 25px rgba(24, 39, 75, 0.085);
}

.kpi-label {
    color: var(--muted);
    font-size: 0.76rem;
    font-weight: 700;
    letter-spacing: 0.8px;
    margin-bottom: 0.8rem;
}

.kpi-value {
    color: #172033;
    font-family: 'Manrope', sans-serif;
    font-size: clamp(1.3rem, 1.8vw, 1.8rem);
    font-weight: 800;
    line-height: 1.3;
    overflow-wrap: anywhere;
}

.kpi-note {
    color: #8490A3;
    font-size: 0.79rem;
    line-height: 1.5;
    margin-top: 0.55rem;
}

.info-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 13px;
    padding: 1.25rem 1.4rem;
    margin-bottom: 0.85rem;
    box-shadow: var(--shadow);
}

.info-card-title {
    color: #172033;
    font-size: 1rem;
    font-weight: 700;
    margin-bottom: 0.55rem;
}

.info-card-text {
    color: #59677D;
    font-size: 0.91rem;
    line-height: 1.75;
}

div[data-testid="stPlotlyChart"] {
    background: #FFFFFF;
    border: 1px solid var(--border);
    border-radius: 15px;
    padding: 0.7rem;
    box-shadow: var(--shadow);
}

div[data-testid="stDataFrame"] {
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
    background: #FFFFFF;
}

.stButton > button,
.stDownloadButton > button {
    border-radius: 9px;
    min-height: 2.7rem;
    font-weight: 700;
    padding: 0.55rem 1rem;
    transition: all 0.18s ease;
}

.stDownloadButton > button[kind="primary"] {
    background: var(--primary);
    border-color: var(--primary);
}

.stDownloadButton > button:hover {
    filter: brightness(0.95);
    box-shadow: 0 4px 12px rgba(79, 70, 229, 0.16);
}

div[data-testid="stMetric"] {
    background: #FFFFFF;
    border: 1px solid var(--border);
    padding: 1rem;
    border-radius: 12px;
    box-shadow: var(--shadow);
}

div[data-testid="stMetricLabel"] {
    color: var(--muted);
}

hr {
    border-color: var(--border);
    margin: 1.5rem 0;
}

[data-testid="stCaptionContainer"] {
    color: #7C889C;
}

.footer {
    text-align: center;
    color: #8490A3;
    font-size: 0.8rem;
    line-height: 1.8;
    padding: 1.5rem 0 0.5rem;
}

@media (max-width: 900px) {
    [data-testid="stAppViewContainer"] .main .block-container {
        padding: 1.3rem 1rem 2rem;
    }

    .page-description {
        font-size: 0.9rem;
    }

    .kpi-card {
        padding: 1rem;
        min-height: 125px;
    }
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# DATA LOADING AND AGENT EXECUTION
# =========================================================

@st.cache_data
def load_data(path):
    return pd.read_csv(path)


@st.cache_resource
def run_analysis(path):

    data_agent = DataAnalystAgent(path)
    analysis = data_agent.analyze()

    insight_agent = InsightAgent()
    insights = insight_agent.generate_insights(analysis)

    prediction_agent = PredictionAgent(path)
    prediction_results = prediction_agent.train_model()

    anomaly_agent = AnomalyDetectionAgent(path)
    anomaly_results = anomaly_agent.detect_anomalies()

    return analysis, insights, prediction_results, anomaly_results


# =========================================================
# REUSABLE UI COMPONENTS
# =========================================================

def page_header(eyebrow, title, description):
    st.markdown(
        f"""
        <div class="page-eyebrow">{eyebrow}</div>
        <div class="page-title">{title}</div>
        <div class="page-description">{description}</div>
        """,
        unsafe_allow_html=True
    )


def section_title(title):
    st.markdown(
        f'<div class="section-heading">{title}</div>',
        unsafe_allow_html=True
    )


def kpi_card(label, value, note=""):
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
            <div class="kpi-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def info_card(title, description):
    st.markdown(
        f"""
        <div class="info-card">
            <div class="info-card-title">{title}</div>
            <div class="info-card-text">{description}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def style_chart(fig, height=350):
    fig.update_layout(
        template="plotly_white",
        height=height,
        margin=dict(l=18, r=28, t=55, b=30),
        font=dict(
            family="DM Sans, sans-serif",
            size=12,
            color="#344054"
        ),
        title=dict(
            font=dict(
                family="Manrope, sans-serif",
                size=15,
                color="#182230"
            ),
            x=0.03,
            xanchor="left"
        ),
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        legend=dict(
            bgcolor="rgba(255,255,255,0)",
            font=dict(size=11),
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    fig.update_xaxes(
        showgrid=False,
        linecolor="#E4E7EC",
        zeroline=False
    )

    fig.update_yaxes(
        gridcolor="#EEF0F5",
        zeroline=False
    )

    return fig


# =========================================================
# SIDEBAR NAVIGATION
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="brand">NEXUS<span>.</span></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="brand-subtitle">AI BUSINESS INTELLIGENCE</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    page = st.radio(
        "WORKSPACE",
        [
            "Executive Overview",
            "Sales Analytics",
            "Business Insights",
            "ML Model Evaluation",
            "Anomaly Detection"
        ],
        label_visibility="visible"
    )

    st.markdown("---")

    st.markdown("**PROJECT STATUS**")
    st.markdown("Dataset connected")
    st.markdown("Four agents configured")

    st.markdown("---")

    st.caption("DATA SOURCE")
    st.caption("E-commerce transactions")
    st.caption("5,000 records · 12 columns")

    st.markdown("---")
    st.caption("NEXUS Analytics · v1.0")


# =========================================================
# LOAD DATA AND ANALYSIS
# =========================================================

if not os.path.exists(DATA_PATH):
    st.error(
        f"Dataset not found: {DATA_PATH}. "
        "Run this app from the project root directory."
    )
    st.stop()

try:
    df = load_data(DATA_PATH)

    with st.spinner("Preparing your business intelligence workspace..."):
        (
            analysis,
            insights,
            prediction_results,
            anomaly_results
        ) = run_analysis(DATA_PATH)

except Exception as error:
    st.error(f"Unable to load the dashboard: {error}")
    st.stop()


# =========================================================
# PAGE 1: EXECUTIVE OVERVIEW
# =========================================================

if page == "Executive Overview":

    page_header(
        "OVERVIEW / 01",
        "Business at a glance",
        "A consolidated view of sales performance, customers and operations."
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        kpi_card(
            "TOTAL REVENUE",
            f"{analysis['total_revenue']:,.2f}",
            "Across all recorded orders"
        )

    with col2:
        kpi_card(
            "TOTAL ORDERS",
            f"{analysis['total_orders']:,}",
            "Transactions in the dataset"
        )

    with col3:
        kpi_card(
            "UNIQUE CUSTOMERS",
            f"{analysis['total_customers']:,}",
            "Distinct customer IDs"
        )

    with col4:
        kpi_card(
            "AVERAGE RATING",
            f"{analysis['average_customer_rating']:.2f}/5",
            "Customer satisfaction indicator"
        )

    st.write("")

    col5, col6, col7, col8 = st.columns(4)

    with col5:
        kpi_card(
            "AVERAGE DELIVERY",
            f"{analysis['average_delivery_days']:.2f} days",
            "Average delivery duration"
        )

    with col6:
        kpi_card(
            "TOP CATEGORY",
            analysis["top_category"],
            "Highest category revenue"
        )

    with col7:
        kpi_card(
            "TOP REGION",
            analysis["top_region"],
            "Highest regional revenue"
        )

    with col8:
        kpi_card(
            "FLAGGED RECORDS",
            f"{anomaly_results['anomaly_count']:,}",
            "Candidates for investigation"
        )

    # CATEGORY AND REGION REVENUE

    section_title("Revenue performance")

    left, right = st.columns([1.15, 1])

    with left:

        category_df = pd.DataFrame(
            list(analysis["category_revenue"].items()),
            columns=["Category", "Revenue"]
        ).sort_values("Revenue", ascending=False)

        fig = px.bar(
            category_df,
            x="Category",
            y="Revenue",
            title="Revenue by product category",
            text_auto=".3s",
            color="Revenue",
            color_continuous_scale=["#B7C6FF", "#4263EB"]
        )

        fig.update_layout(coloraxis_showscale=False)
        fig.update_traces(textposition="outside")

        st.plotly_chart(
            style_chart(fig, 370),
            use_container_width=True
        )

    with right:

        region_df = pd.DataFrame(
            list(analysis["region_revenue"].items()),
            columns=["Region", "Revenue"]
        ).sort_values("Revenue", ascending=False)

        fig = px.pie(
            region_df,
            names="Region",
            values="Revenue",
            title="Revenue distribution by region",
            hole=0.62,
            color_discrete_sequence=[
                "#4263EB", "#8298FF", "#35B8A5", "#F5A65B"
            ]
        )

        fig.update_traces(
            textposition="inside",
            textinfo="percent"
        )

        st.plotly_chart(
            style_chart(fig, 370),
            use_container_width=True
        )

    # MONTHLY REVENUE TREND

    section_title("Monthly revenue trend")

    trend_df = df.copy()
    trend_df["order_date"] = pd.to_datetime(
        trend_df["order_date"],
        errors="coerce"
    )

    trend_df = trend_df.dropna(subset=["order_date"])

    if not trend_df.empty:

        monthly_revenue = (
            trend_df
            .assign(
                month=trend_df["order_date"]
                .dt.to_period("M")
                .astype(str)
            )
            .groupby("month", as_index=False)["revenue"]
            .sum()
            .sort_values("month")
        )

        fig = px.line(
            monthly_revenue,
            x="month",
            y="revenue",
            markers=True,
            title="Revenue generated each month",
            labels={
                "month": "Month",
                "revenue": "Total revenue"
            }
        )

        fig.update_traces(
            line=dict(color="#4F46E5", width=3),
            marker=dict(size=7, color="#4F46E5"),
            fill="tozeroy",
            fillcolor="rgba(79, 70, 229, 0.08)",
            hovertemplate=(
                "Month: %{x}<br>"
                "Revenue: %{y:,.2f}"
                "<extra></extra>"
            )
        )

        fig.update_layout(
            hovermode="x unified",
            xaxis_title="Month",
            yaxis_title="Revenue"
        )

        st.plotly_chart(
            style_chart(fig, 380),
            use_container_width=True
        )

        if len(monthly_revenue) > 1:
            first_month = monthly_revenue.iloc[0]
            last_month = monthly_revenue.iloc[-1]

            st.caption(
                f"Showing {len(monthly_revenue)} months of recorded data, "
                f"from {first_month['month']} through {last_month['month']}. "
                "These values represent historical revenue, not forecasts."
            )

    else:
        st.info(
            "No valid order dates are available for the monthly trend chart."
        )

    # BUSINESS HIGHLIGHTS

    section_title("Business highlights")

    left, right = st.columns(2)

    with left:

        info_card(
            "Leading category",
            f"{analysis['top_category']} generated the highest "
            "category revenue in this dataset."
        )

        info_card(
            "Regional performance",
            f"{analysis['top_region']} is the highest-revenue region."
        )

    with right:

        info_card(
            "Customer experience",
            f"The average rating is "
            f"{analysis['average_customer_rating']:.2f}/5. "
            "Review customer feedback for potential improvements."
        )

        info_card(
            "Delivery performance",
            f"Average delivery time is "
            f"{analysis['average_delivery_days']:.2f} days."
        )

    section_title("Recent transactions")

    st.dataframe(
        df.head(10),
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# PAGE 2: SALES ANALYTICS
# =========================================================

elif page == "Sales Analytics":

    page_header(
        "ANALYTICS / 02",
        "Explore sales performance",
        "Compare category and regional revenue, then filter individual transactions."
    )

    left, right = st.columns(2)

    with left:

        category = (
            df.groupby("product_category", as_index=False)["revenue"]
            .sum()
            .sort_values("revenue", ascending=False)
        )

        fig = px.bar(
            category,
            x="product_category",
            y="revenue",
            title="Revenue by category",
            text_auto=".3s",
            color="product_category",
            color_discrete_sequence=[
                "#4263EB", "#8298FF", "#35B8A5", "#F5A65B"
            ]
        )

        fig.update_layout(showlegend=False)
        fig.update_traces(textposition="outside")

        st.plotly_chart(
            style_chart(fig, 360),
            use_container_width=True
        )

    with right:

        region = (
            df.groupby("region", as_index=False)["revenue"]
            .sum()
            .sort_values("revenue", ascending=False)
        )

        fig = px.bar(
            region,
            x="region",
            y="revenue",
            title="Revenue by region",
            text_auto=".3s",
            color="region",
            color_discrete_sequence=[
                "#4263EB", "#8298FF", "#35B8A5", "#F5A65B"
            ]
        )

        fig.update_layout(showlegend=False)
        fig.update_traces(textposition="outside")

        st.plotly_chart(
            style_chart(fig, 360),
            use_container_width=True
        )

    section_title("Transaction explorer")

    filter1, filter2 = st.columns(2)

    categories = sorted(df["product_category"].unique().tolist())
    regions = sorted(df["region"].unique().tolist())

    with filter1:
        selected_categories = st.multiselect(
            "Product categories",
            categories,
            default=categories
        )

    with filter2:
        selected_regions = st.multiselect(
            "Regions",
            regions,
            default=regions
        )

    filtered_df = df[
        df["product_category"].isin(selected_categories)
        & df["region"].isin(selected_regions)
    ]

    m1, m2, m3 = st.columns(3)

    with m1:
        kpi_card(
            "MATCHING ORDERS",
            f"{len(filtered_df):,}",
            "Based on current filters"
        )

    with m2:
        kpi_card(
            "FILTERED REVENUE",
            f"{filtered_df['revenue'].sum():,.2f}",
            "Sum of matching revenue"
        )

    with m3:
        average_revenue = (
            filtered_df["revenue"].mean()
            if not filtered_df.empty else 0
        )

        kpi_card(
            "AVERAGE ORDER REVENUE",
            f"{average_revenue:,.2f}",
            "For matching transactions"
        )

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )

    st.download_button(
        "Download filtered transactions",
        data=filtered_df.to_csv(index=False).encode("utf-8"),
        file_name="filtered_transactions.csv",
        mime="text/csv",
        type="primary"
    )


# =========================================================
# PAGE 3: BUSINESS INSIGHTS
# =========================================================

elif page == "Business Insights":

    page_header(
        "INTELLIGENCE / 03",
        "Business insights",
        "Findings generated from the data analyst and insight agents."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        kpi_card(
            "INSIGHTS GENERATED",
            f"{len(insights)}",
            "Automatically generated findings"
        )

    with col2:
        kpi_card(
            "MISSING VALUES",
            f"{analysis['missing_values']:,}",
            "Data quality check"
        )

    with col3:
        kpi_card(
            "DUPLICATE ROWS",
            f"{analysis['duplicate_rows']:,}",
            "Exact duplicate-row check"
        )

    section_title("Key findings")

    for index, insight in enumerate(insights, start=1):

        st.markdown(
            f"""
            <div class="info-card">
                <div class="info-card-title">
                    {index:02d} &nbsp; Business finding
                </div>
                <div class="info-card-text">{insight}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.info(
        "These findings are descriptive indicators. Validate business "
        "context and operational causes before taking action."
    )


# =========================================================
# PAGE 4: ML MODEL EVALUATION
# =========================================================

elif page == "ML Model Evaluation":

    page_header(
        "MACHINE LEARNING / 04",
        "Model evaluation",
        "Review regression metrics and compare the model with a simple baseline."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        kpi_card(
            "RANDOM FOREST MAE",
            f"{prediction_results['mae']:.2f}",
            "Mean absolute error"
        )

    with col2:
        kpi_card(
            "RANDOM FOREST RMSE",
            f"{prediction_results['rmse']:.2f}",
            "Root mean squared error"
        )

    with col3:
        kpi_card(
            "R² SCORE",
            f"{prediction_results['r2']:.4f}",
            "Coefficient of determination"
        )

    section_title("Random Forest vs. baseline")

    comparison_df = pd.DataFrame({
        "Model": ["Random Forest", "Mean Baseline"],
        "MAE": [
            prediction_results["mae"],
            prediction_results["baseline_mae"]
        ],
        "RMSE": [
            prediction_results["rmse"],
            prediction_results["baseline_rmse"]
        ]
    })

    left, right = st.columns([1, 1.2])

    with left:
        st.dataframe(
            comparison_df.round(3),
            use_container_width=True,
            hide_index=True
        )

    with right:

        metric_df = comparison_df.melt(
            id_vars="Model",
            value_vars=["MAE", "RMSE"],
            var_name="Metric",
            value_name="Error"
        )

        fig = px.bar(
            metric_df,
            x="Metric",
            y="Error",
            color="Model",
            barmode="group",
            title="Error metric comparison",
            color_discrete_sequence=["#4263EB", "#F5A65B"]
        )

        st.plotly_chart(
            style_chart(fig, 320),
            use_container_width=True
        )

    st.warning(
        "Important limitation: revenue matches quantity × unit price × "
        "(1 − discount) for 100% of the dataset to two decimal places. "
        "The model uses these inputs, so the high R² does not establish "
        "genuine future-revenue forecasting ability."
    )

    kpi_card(
        "REVENUE FORMULA MATCH",
        f"{prediction_results['formula_match_percentage']:.2f}%",
        "Rows matching the calculated revenue formula"
    )


# =========================================================
# PAGE 5: ANOMALY DETECTION
# =========================================================

elif page == "Anomaly Detection":

    page_header(
        "RISK EXPLORER / 05",
        "Unusual transactions",
        "Explore transactions flagged by the Isolation Forest anomaly detector."
    )

    anomalies = anomaly_results["anomalies"].copy()

    col1, col2, col3 = st.columns(3)

    with col1:
        kpi_card(
            "TOTAL TRANSACTIONS",
            f"{anomaly_results['total_transactions']:,}",
            "Records evaluated"
        )

    with col2:
        kpi_card(
            "FLAGGED RECORDS",
            f"{anomaly_results['anomaly_count']:,}",
            "Candidates for review"
        )

    with col3:
        kpi_card(
            "FLAGGED SHARE",
            f"{anomaly_results['anomaly_percentage']:.2f}%",
            "Configured anomaly proportion"
        )

    st.warning(
        "A flagged transaction is unusual relative to the data. It is not "
        "automatically fraud, an error, or a confirmed business problem."
    )

    section_title("Revenue distribution of flagged records")

    if not anomalies.empty:

        fig = px.histogram(
            anomalies,
            x="revenue",
            nbins=25,
            title="Revenue distribution",
            color_discrete_sequence=["#4263EB"]
        )

        st.plotly_chart(
            style_chart(fig, 350),
            use_container_width=True
        )

        section_title("Investigate flagged transactions")

        sort_option = st.selectbox(
            "Sort records by",
            [
                "Most unusual first",
                "Highest revenue",
                "Lowest revenue",
                "Longest delivery"
            ]
        )

        if sort_option == "Most unusual first":
            anomalies = anomalies.sort_values(
                "anomaly_score",
                ascending=True
            )

        elif sort_option == "Highest revenue":
            anomalies = anomalies.sort_values(
                "revenue",
                ascending=False
            )

        elif sort_option == "Lowest revenue":
            anomalies = anomalies.sort_values(
                "revenue",
                ascending=True
            )

        else:
            anomalies = anomalies.sort_values(
                "delivery_days",
                ascending=False
            )

        st.dataframe(
            anomalies,
            use_container_width=True,
            hide_index=True
        )

        st.download_button(
            "Download flagged transactions",
            data=anomalies.to_csv(index=False).encode("utf-8"),
            file_name="detected_anomalies.csv",
            mime="text/csv",
            type="primary"
        )

    else:
        st.info("No anomalies were detected.")


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div class="footer">
        NEXUS · AI Multi-Agent Business Intelligence<br>
        Python · Pandas · Scikit-learn · Plotly · Streamlit
    </div>
    """,
    unsafe_allow_html=True
)

#streamlit run app.py