import streamlit as st
from PIL import Image

with st.expander('Show webcam'):
    # Start the webcam
    camera_image = st.camera_input('Please take a picture')


if camera_image:
    # Display the image
    img = Image.open(camera_image)

    # Convert the image to grayscale
    gray_img = img.convert('L')
    st.image(gray_img)
