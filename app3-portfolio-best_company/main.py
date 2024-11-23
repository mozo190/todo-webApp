import streamlit as st
import pandas as pd

st.set_page_config(page_title="The best company", page_icon="🧊", layout="wide")

st.title("The best company")
content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
"""

st.subheader("Our Team")

col1, empty_col, col2, empty_col2, col3 = st.columns([1, 0.5, 1, 0.5, 1])

df = pd.read_csv('data.csv', sep=',')

with col1:
    for i, row in df[:2].iterrows():
        st.header(row['first name'] + " " + row['last name'])
        st.write(df['role'])
        st.image("images/" + df['image'])

