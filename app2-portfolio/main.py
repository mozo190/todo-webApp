import streamlit as st

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
