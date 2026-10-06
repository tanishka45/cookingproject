"""import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import time
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
c = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.write(c)"""
import streamlit as st
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




_LOREM_IPSUM = """
Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""




def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)


    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )
    


    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)




if st.button("Stream data"):
    st.write_stream(stream_data)

# Draw a title and some text to the app:
'''
# This is the document title


This is some _markdown_.
'''
df = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 Draw the dataframe


x = 10
'x', x  # 👈 Draw the string 'x' and then the value of x


# Also works with most supported chart types




arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)


fig  # 👈 Draw a Matplotlib chart



# Title, header, and subheader
st.title("Streamlit Text Elements")
st.header("This is a header")
st.subheader("This is a subheader")


# Plain text output
st.text("This is plain text output using st.text()")


# Markdown formatted text
st.markdown("**This is bold markdown text using st.markdown()**")


# Caption text
st.caption("This is a caption for an image or a figure.")


# Display a code block with syntax highlighting
code_snippet = '''
def hello_world():
    print("Hello, Streamlit!")
'''
st.code(code_snippet, language='python')


# Display a LaTeX formatted mathematical expression
st.latex(r'''
a^2 + b^2 = c^2
''')


# Using st.write to display generic content
st.write("This is an example of st.write, which can display different types of content.")


# Message functions for different statuses
st.success("This is a success message!")
st.error("This is an error message!")
st.warning("This is a warning message!")
st.info("This is an info message!")


# Example of displaying an exception with st.exception
try:
    1 / 0
except Exception as e:
    st.exception(e)
