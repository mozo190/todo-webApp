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
    I am passionate to learn new things and I am always looking for new challenges.
    The programing gives me the opportunity to create something new and useful.
    It is like inventing something new every day.
    """
    st.info(content)

st.write("Below you can find some of the apps I have created in Python. Feel free to contact me.")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])  # 3 columns
df = pd.read_csv('data.csv', sep=';')

# Add images to the dataframe
df['image'] = df['image'].apply(lambda x: f"images/{x}")

for i, row in df.iterrows():
    if i % 2 == 0:
        with col3:
            st.header(f" {row['title']}")
            st.write(row['description'])
            st.image(row['image'], use_container_width=True)
            st.write(f"[Source code]({row['url']})")
    else:
        with col4:
            st.header(f" {row['title']}")
            st.write(row['description'])
            st.image(row['image'], use_container_width=True)
            st.write(f"[Source code]({row['url']})")
