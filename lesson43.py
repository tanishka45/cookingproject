import streamlit as st
import pandas as pd
import numpy as np
data = pd.DataFrame({
    "Day": pd.date_range("2025-01-01", periods=7),
    "Sales": np.random.randint(100, 500, size=7),
    "Returns": np.random.randint(10, 50, size=7)
})


st.title("Weekly Sales & Returns")


# Plot area chart using st.area_chart
st.area_chart(data.set_index("Day"))




df = pd.DataFrame({
    "Day": pd.date_range("2025-01-01", periods=5),
    "Sales": np.random.randint(100, 500, 5),
    "Returns": np.random.randint(10, 100, 5)
})


st.area_chart(
    data=df,
    x="Day",
    y=["Sales", "Returns"],
    x_label="Date",
    y_label="Value",
    color=["#1f77b4", "#ff7f0e"],
    stack="normalize",
    use_container_width=True
)
data = pd.DataFrame({
    "Product": ["A", "B", "C", "D"],
    "Sales": [120, 340, 200, 150],
    "Profit": [30, 70, 50, 20]
})


st.title("Sales and Profit by Product")


st.bar_chart(
    data=data,
    x="Product",
    y=["Sales", "Profit"],
    stack="normalize",
    use_container_width=True
)

data = pd.DataFrame({
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Revenue": [5000, 7000, 6000, 6500]
})


st.bar_chart(data.set_index("Quarter"))
data = pd.DataFrame({
    "Month": pd.date_range("2025-01-01", periods=6, freq='ME'),
    "Revenue": np.random.randint(1000, 5000, 6),
    "Expenses": np.random.randint(500, 3000, 6)
})


st.title("Monthly Revenue vs Expenses")


st.line_chart(
    data=data,
    x="Month",
    y=["Revenue", "Expenses"],
    x_label="Month",
    y_label="USD",
    use_container_width=True
)
