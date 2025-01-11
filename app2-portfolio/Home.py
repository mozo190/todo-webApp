import os.path

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Zoltan Molnar", page_icon="🧊", layout="wide")
col1, col2 = st.columns(2)

content = """
    I am a developer and a data scientist. I have a passion for data and I love to work with it.
    I have experience in Python, Java, SQL, and I am familiar with machine learning and deep learning.
    I am passionate to learn new things and I am always looking for new challenges.
    The programing gives me the opportunity to create something new and useful.
    It is like inventing something new every day.<br><hr style="border: 1px solid lightgrey; margin: 30px 20px;">
    Below you can find some of the apps I have created in Python.
    Feel free to contact me if you have any questions or suggestions.
    """

# Add spacing between the cards
card_style = (
    "border: 0 solid black; border-radius: 10px; padding: 10px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.8);"
    "margin: 10px;"
)

with col1:
    st.image(os.path.join(os.getcwd(), 'images/mozo480.png'))

with col2:
    with st.container():
        st.markdown(
            f"<div style='{card_style}'>"
            f"<h1 style='text-align: center;'>Zoltan Molnar</h1>"
            f"<p>{content}</p>",
            unsafe_allow_html=True,
        )

st.write("")

# Create columns for the cards
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])  # 3 columns
df = pd.read_csv('data.csv', sep=';', encoding='utf-8')

# Add images to the dataframe
df['image'] = df['image'].apply(lambda x: f"images/{x}")

for i, row in df.iterrows():
    if i % 2 == 0:
        with col3:
            st.markdown(f"<h3>{row['title']}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p>{row['description']}</p>", unsafe_allow_html=True)
            st.image(row['image'], use_container_width=True, caption=row['title'])
            st.markdown(
                f"<a href='{row['url']}' target='_blank' style='display: inline-block; "
                f"margin-top: 10px;'>Source code</a>",
                unsafe_allow_html=True)
            st.markdown("<hr style='border: 1px solid lightgrey; margin: 30px 20px;'>", unsafe_allow_html=True)

    else:
        with col4:
            st.markdown(f"<h3>{row['title']}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p>{row['description']}</p>", unsafe_allow_html=True)
            st.image(row['image'], use_container_width=True, caption=row['title'])
            st.markdown(
                f"<a href='{row['url']}' target='_blank' style='display: inline-block;"
                f" margin-top: 10px;'>Source code</a>",
                unsafe_allow_html=True)
            st.markdown("<hr style='border: 1px solid lightgrey; margin: 30px 20px;'>", unsafe_allow_html=True)
