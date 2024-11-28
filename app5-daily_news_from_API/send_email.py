import smtplib
import ssl

from data import E_MAIL, PASS


def send_email(message, email):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    username = E_MAIL  # Enter your address
    password = PASS  # Enter your password
    receiver_email = E_MAIL  # Enter receiver address

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver_email, message)
        print('Email sent successfully')
