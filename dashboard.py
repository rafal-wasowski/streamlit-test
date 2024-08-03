import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title="NoChoc2Smore Ltd Dashboard", layout="wide")

# Mock Data
data = {
    "Metric": ["Sales", "Units", "Margin"],
    "Actual": [28, 6, 5],
    "YTD": [22, 2, 6],
    "Vs LY": [-6, -4, 1],
    "Vs Budget": [-4, -3, 1]
}

forecast_data = {
    "Metric": ["Sales", "Units", "Margin"],
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

# Styles
st.markdown("""
    <style>
        .main {background-color: #f5f5f5;}
        .title {font-size: 2em; font-weight: bold; margin-bottom: 0.5em;}
        .header {font-size: 1.5em; font-weight: bold; margin-bottom: 0.5em;}
        .subheader {font-size: 1.25em; font-weight: bold; margin-bottom: 0.5em;}
        .metric {font-size: 1.25em; margin-bottom: 0.5em;}
        .text {font-size: 1em; margin-bottom: 0.25em;}
    </style>
""", unsafe_allow_html=True)

# Layout
st.markdown('<div class="title">NoChoc2Smore Ltd Dashboard</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.markdown('<div class="header">Churn Risk: Small</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Predicted Lifetime: 5 years</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Estimated Retirement: 15 year</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Engagement Score: 85</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Days Since Last Order: 3</div>', unsafe_allow_html=True)

    st.markdown('<div class="header">Avg Orders p/w: 3</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Avg Order Lines p/w: 23</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Avg Order Value p/w: £3,700</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Avg Cancelled Value p/w: £300</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Avg Return Value p/w: £50</div>', unsafe_allow_html=True)

    st.markdown('<div class="header">Open Orders: 2</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Open Orders Value: £1,500</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Oldest Open Order Days: 12</div>', unsafe_allow_html=True)

    st.markdown('<div class="header">Open Quotes: 4</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Open Quotes Value: £15,000</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Quote Conversion Rate: 0.25</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="header">Actual vs Forecast</div>', unsafe_allow_html=True)
    df_actual = pd.DataFrame(data)
    st.table(df_actual)

    st.markdown('<div class="header">Forecast</div>', unsafe_allow_html=True)
    df_forecast = pd.DataFrame(forecast_data)
    st.table(df_forecast)

    st.markdown('<div class="header">Credit Risk: Small</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Avg Monthly Spend: £15,000</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Credit Limit: £20,000</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Credit Used: £18,500</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Pay Due Date: 25/12/2024</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Account Status: Live</div>', unsafe_allow_html=True)

    st.markdown('<div class="header">Credit Utilisation</div>', unsafe_allow_html=True)
    st.line_chart([1, 2, 3, 2, 1, 2, 3])

with col3:
    st.markdown('<div class="header">Contact Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Owner: Any Name - 077 777 7777</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Buyer: Other Surname - 078 888 8888</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">123 Building, Only Road\nSmall Town, AB1 2CD</div>', unsafe_allow_html=True)

    st.markdown('<div class="header">Top 5 Branches</div>', unsafe_allow_html=True)
    df_branches = pd.DataFrame(branches_data)
    st.table(df_branches)

    st.markdown('<div class="header">Top 5 Sales Colleagues 12m rolling</div>', unsafe_allow_html=True)
    df_colleagues = pd.DataFrame(colleagues_data)
    st.table(df_colleagues)
