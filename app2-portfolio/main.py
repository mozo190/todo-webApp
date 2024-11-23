import streamlit as st
import pandas as pd

st.set_page_config(page_title="Zoltan Molnar", page_icon="🧊", layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image('images/mo-zo-480.png')

with col2:
    st.title("Zoltan Molnar")
    content = """
    I am a developer and a data scientist. I have a passion for data and I love to work with it.
    I have experience in Python, Java, SQL, and I am familiar with machine learning and deep learning.
    I have a strong background in mathematics and statistics.
    """
    st.info(content)

st.write("Below you can find some of the apps I have created in Python. Feel free to contact me.")


col3, col4 = st.columns(2)
df = pd.read_csv('data.csv', sep=';')

# Add images to the dataframe
df['image'] = df['image'].apply(lambda x: f"images/{x}")

with col3:
    for i, row in df[:10].iterrows():
        st.header(f" {row['title']}")
        st.write(row['description'])
        st.image(row['image'])
        st.write(f"[Source code]({row['url']})")

with col4:
    for i, row in df[10:].iterrows():
        st.header(f" {row['title']}")
        st.write(row['description'])
        st.image(row['image'])
        st.write(f"[Source code]({row['url']})")
