import locale

import cv2
from datetime import datetime
import streamlit as st

st.title("Simple Monitor Detection Web App")

video_button = st.button("Start Video")

locale.setlocale(locale.LC_TIME, 'hu_HU.UTF-8')

if video_button:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        if not check:
            st.error("Could not access the camera")
            break

        # Get dynamically the current date and time
        current_time = datetime.now()
        present_day = current_time.strftime("%A")
        present_date = current_time.strftime("%Y-%m-%d")
        present_time = current_time.strftime("%H:%M:%S")

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.putText(img=frame,
                    text=present_day,
                    org=(10, 20),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.5,
                    color=(20, 100, 250),
                    thickness=1,
                    lineType=cv2.LINE_AA
                    )
        cv2.putText(img=frame,
                    text=present_date,
                    org=(10, 40),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.6,
                    color=(20, 100, 200),
                    thickness=1,
                    lineType=cv2.LINE_AA
                    )
        cv2.putText(img=frame,
                    text=present_time,
                    org=(10, 60),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.6,
                    color=(20, 100, 200),
                    thickness=1,
                    lineType=cv2.LINE_AA)


        streamlit_image.image(frame)
