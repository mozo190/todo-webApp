import smtplib
import ssl

import streamlit as st


def send_email(message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"

    username = "mozo37@gmail.com"  # Enter your address
    something = "prvwzuwsgxjfubht"   # Enter your something

    receiver_email = "mozo37@gmail.com"  # Enter receiver address
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(username, something)
        server.sendmail(username, receiver_email, message)
