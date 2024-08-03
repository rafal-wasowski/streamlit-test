import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(layout="wide")

# Mock Data
data = {
    "Actual": [28, 6, 5],
    "YTD": [22, 2, 6],
    "Vs LY": [-6, -4, 1],
    "Vs Budget": [-4, -3, 1]
}

forecast_data = {
    "YTD": [25, 2, 5],
    "Vs PFY": [-3, -4, 1],
    "Vs Budget": [-3, -3, 1]
}

branches_data = {
    "Branch": ["A", "B", "C", "D", "E"],
    "Sales": [100, 90, 80, 70, 60]
}

colleagues_data = {
    "Colleague": ["A", "B", "C", "D", "E"],
    "Sales": [50, 45, 40, 35, 30]
}

# Layout
st.title("NoChoc2Smore Ltd")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Churn Risk: Small")
    st.subheader("Predicted Lifetime: 5 years")
    st.text("Estimated Retirement: 15 year")
    st.text("Engagement Score: 85")
    st.text("Days Since Last Order: 3")

    st.header("Avg Orders p/w: 3")
    st.text("Avg Order Lines p/w: 23")
    st.text("Avg Order Value p/w: £3,700")
    st.text("Avg Cancelled Value p/w: £300")
    st.text("Avg Return Value p/w: £50")

    st.header("Open Orders: 2")
    st.text("Open Orders Value: £1,500")
    st.text("Oldest Open Order Days: 12")

    st.header("Open Quotes: 4")
    st.text("Open Quotes Value: £15,000")
    st.text("Quote Conversion Rate: 0.25")

with col2:
    st.header("Actual vs Forecast")
    df_actual = pd.DataFrame(data, index=["Sales", "Units", "Margin"])
    st.table(df_actual)

    st.header("Forecast")
    df_forecast = pd.DataFrame(forecast_data, index=["Sales", "Units", "Margin"])
    st.table(df_forecast)

    st.header("Credit Risk: Small")
    st.text("Avg Monthly Spend: £15,000")
    st.text("Credit Limit: £20,000")
    st.text("Credit Used: £18,500")
    st.text("Pay Due Date: 25/12/2024")
    st.text("Account Status: Live")

    st.line_chart([1, 2, 3, 2, 1, 2, 3])

with col3:
    st.header("Contact Information")
    st.text("Owner: Any Name - 077 777 7777")
    st.text("Buyer: Other Surname - 078 888 8888")
    st.text("123 Building, Only Road\nSmall Town, AB1 2CD")

    st.header("Top 5 Branches")
    df_branches = pd.DataFrame(branches_data)
    st.table(df_branches)

    st.header("Top 5 Sales Colleagues 12m rolling")
    df_colleagues = pd.DataFrame(colleagues_data)
    st.table(df_colleagues)
