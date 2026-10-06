import streamlit as st
import altair as alt
import pandas as pd


df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Revenue": [1000, 1200, 1800, 1600],
    "Profit": [300, 400, 600, 550]
})


chart = alt.Chart(df).mark_line(point=True).encode(
    x='Month',
    y='Revenue',
    tooltip=['Month', 'Revenue']
).properties(
    title='Monthly Revenue Trend'
)


st.altair_chart(chart, use_container_width=True)
import streamlit as st


# Title
st.title("📈 Simple Graphviz Binary Tree")


# Define the graph structure
graph = """
digraph G {
    A -> B
    A -> C
    B -> D
    B -> E
    C -> F
    C -> G
}
"""


# Render the graph
st.graphviz_chart(graph, use_container_width=True)
import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(y=[2, 3, 1]))


st.plotly_chart(fig)
st.title("Siennas simple binary tree visualization")
st.caption("Visualize a basic binary tree structure using Graphviz in Streamlit.")

binary_tree = """
digraph BinaryTree {
    node [shape=circle, style=filled, color=lightblue, fontname=Helvetica];
    A [label="A"];
    B [label="B"];
    C [label="C"];
    D [label="D];
    E [label="E"];
    F [label="F"];
    G [label="G"];
    A -> B;
    A -> C;
    B -> D;
    B -> E;
    C -> F;
    C -> G;
}
"""
st.graphviz_chart(binary_tree, use_container_width=True)
import streamlit as st


st.title("🌲 Sienne's Simple Binary Tree Visualizer")
st.caption("Visualize a basic binary tree structure using Graphviz in Streamlit.")


# Define the binary tree using Graphviz DOT language
binary_tree = """
digraph BinaryTree {
    node [shape=circle, style=filled, color=lightblue, fontname=Helvetica];


    A [label="A"]
    B [label="B"]
    C [label="C"]
    D [label="D"]
    E [label="E"]
    F [label="F"]
    G [label="G"]


    A -> B
    A -> C
    B -> D
    B -> E
    C -> F
    C -> G
}
"""


# Display the binary tree
st.graphviz_chart(binary_tree)
