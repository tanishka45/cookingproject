import streamlit as st
import pandas as pd


# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
    
}
df = pd.DataFrame(data)


# Display the DataFrame using st.dataframe
st.dataframe(df)
arguments = {
    "Argument": ["data", "width", "height", "use_container_width"],
    "Type": ["DataFrame or array-like", "int", "int", "bool"],
    "Default Value": ["*Required*", "None", "None", "False"],
    "Description": [
        "The data to be displayed (e.g., a Pandas DataFrame, list, etc.)",
        "Fixed width (in pixels) for the display.",
        "Fixed height (in pixels) for the display.",
        "If True, the DataFrame will expand to the container's width."
    ]
}
args_df = pd.DataFrame(arguments)
# Display the table using st.table
st.table(args_df)
# Create a sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)


st.markdown("## Editable Data Table using st.data_editor")
st.write("You can edit the table directly below:")


# Use st.data_editor to allow users to edit the DataFrame
edited_df = st.data_editor(df, num_rows="dynamic")


# Display the edited DataFrame
st.markdown("### Edited DataFrame")
st.dataframe(edited_df)


st.dataframe(df, column_config={
    "Text column": st.column_config.TextColumn("Text"),

})


