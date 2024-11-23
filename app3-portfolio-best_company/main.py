import streamlit as st

st.set_page_config(page_title="The best company", page_icon="🧊", layout="wide")

st.title("The best company")
content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
"""

st.subheader("Our Team")

col1, empty_col, col2, empty_col2, col3 = st.columns([1, 0.5, 1, 0.5, 1])

with col1:
    st.header
