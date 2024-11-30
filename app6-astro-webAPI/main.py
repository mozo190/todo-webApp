import requests
import streamlit as st

from data import URL

st.set_page_config(page_title="Astronaut picture", page_icon="🚀", layout="wide")

response = requests.get(URL)
if response.status_code == 200:
    content = response.json()
    image_url = content.get("url")
    description = content.get("explanation", "No description available")
else:
    st.error("Failed to load data")
    image_url = None
    description = "No description available"

st.title("Astronaut picture")
if image_url:
    st.image(image_url, use_container_width=True, caption="Astronaut Image of the Day")
else:
    st.error("No image available")

st.write(description)
