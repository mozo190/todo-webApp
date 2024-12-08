import cv2

import streamlit as st

st.title("Simple Monitor Detection Web App")

video_button = st.button("Start Video")

if video_button:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.putText(img=frame, text="Press 'q' to quit",
                    org=(10, 20),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.5,
                    color=(20, 100, 200),
                    thickness=1,
                    lineType=cv2.LINE_AA)

        streamlit_image.image(frame)
