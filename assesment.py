import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Williams brewery inspections")
def load_data():
    return pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=';')
df=load_data()
st.sidebar.title("Filter Options")
selected_quality = st.sidebar.multiselect("Select wine quality:", df['quality'].unique(), default=df['quality'].unique())
filtered_df=df[df['quality'].isin(selected_quality)]
st.write()
tab1, tab2, tab3,tab4,tab5,tab6 = st.tabs(["Distribution","Scatter plot","box plot","line plot","bar plot","correlation"])
with tab1:
    st.subheader("feature distribution")
    feature = st.selectbox("Select a feature to visualize its distribution:", df.columns[:-1])
    plt.figure(figsize=(10, 6))
    sns.histplot(data=filtered_df, x=feature, kde=True, bins=30)
    plt.title(f"Distribution of {feature}")
    st.pyplot(plt)
with tab2:
    st.subheader("Scatter plot")
    x_feature = st.selectbox("Select X-axis feature:", df.columns[:-1])
    y_feature = st.selectbox("Select Y-axis feature:", df.columns[:-1])
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=filtered_df, x=x_feature, y=y_feature, hue='quality', palette='viridis')
    plt.title(f"Scatter plot of {y_feature} vs {x_feature}")
    st.pyplot(plt)
with tab3:
    st.subheader("Box plot")
    feature = st.selectbox("Select a feature to visualize its box plot:", df.columns[:-1])
    feature_box = st.selection("Select a feature to visualize its box plots", df.columns[:1])
    fig, ax =plt.subplots(figsize=(10,6))
    sns.boxplot(data=filtered_df, x=feature_box, y=feature, ax=ax)
    plt.title(f"Box plot of {feature} by {feature_box}")
    st.pyplot(fig=plt)

