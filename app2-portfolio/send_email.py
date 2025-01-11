import smtplib
import ssl

import streamlit as st


def send_email(message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"

    username = st.secrets["app2-portfolio_USER_NAME"]  # Enter your address
    password = st.secrets["app2-portfolio_EMAIL_PASSWORD"]   # Enter your password

    receiver_email = "mozo37@gmail.com"  # Enter receiver address
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver_email, message)
