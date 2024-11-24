import pandas as pd
import streamlit as st

st.set_page_config(page_title="The best company", page_icon="🧊", layout="wide")

st.title("The best company")

content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
"""
st.write(content)

st.subheader("Our Team")

col1, empty_col, col2, empty_col2, col3 = st.columns([1, 0.5, 1, 0.5, 1])

df = pd.read_csv('data.csv', sep=',')

with col1:
    for i, row in df[:4].iterrows():
        st.header(row['first name'].title() + " " + row['last name'].title())
        st.write(row['role'])
        st.image("images/" + row['image'])

with col2:
    for i, row in df[4:8].iterrows():
        st.header(row['first name'].title() + " " + row['last name'].title())
        st.write(row['role'])
        st.image("images/" + row['image'])

with col3:
    for i, row in df[8:].iterrows():
        st.header(row['first name'].title() + " " + row['last name'].title())
        st.write(row['role'])
        st.image("images/" + row['image'])
