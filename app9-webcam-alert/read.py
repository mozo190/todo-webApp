import glob
import os
import time
from threading import Thread

import cv2

from emailing import send_email

video = cv2.VideoCapture(0)
time.sleep(1)

first_frame = None
status_list = []
count = 1


def clean_folder():
    images = glob.glob("images/*.png")
    for image in images:
        try:
            os.remove(image)
        except Exception as e:
            print(f"Error occurred: {e}")


while True:
    status = 0
    check, frame = video.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame_gau
        continue

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)

    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    cv2.imshow("Capturing", dil_frame)

    contours, check_ = cv2.findContours(dil_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        if rectangle.any():
            status = 1
            cv2.imwrite(f"images/{count}.png", frame)
            count += 1
            all_img = glob.glob("images/*.png")
            index = int(len(all_img) / 2)
            image_with_object = all_img[index]
            # send_email(image=var)

    status_list.append(status)
    status_list = status_list[-2:]  # Keep only the last two elements

    if status_list[-2:] == [0, 1]:
        email_thread = Thread(target=send_email, args=(image_with_object,))
        email_thread.daemon = True
        clean_thread = Thread(target=clean_folder())
        clean_thread.daemon = True

        email_thread.start()

    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
clean_thread.start()
