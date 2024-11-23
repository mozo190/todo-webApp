import smtplib
import ssl


def send_email(message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = " [email protected]"  # Enter your address
    receiver_email = " [email protected]"  # Enter receiver address
    password = "your_password"  # Enter your password
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


send_email()
