import streamlit as st
st.title("Jeremys streamlit text element guide")
st.header("A comprehensive guide to Streamlit's text elements")
st.text("developers new to stremlit can use this guide to understand the various text elements available in Streamlit and how to use them effectively.")
st.subheader("Plain text example")
st.text("This is a simple text element in Streamlit. It can be used to display plain text on the app.")
st.subheader("Markdown example")
st.markdown("Streamlit supports **Markdown** for rich text formatting. You can use Markdown to create headings, lists, links, and more.")
st.subheader("Code example")
st.code("import streamlit as st\nst.title('Hello, Streamlit!')\nst.write('This is a simple Streamlit app.')")
def great(name):
    return f"Hello, {name}! welcome to the streamlit text element guide."
