import smtplib
import ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"

sender_email = " [email protected]"  # Enter your address
receiver_email = " [email protected]"  # Enter receiver address

password = input("Type your password and press enter: ")

context = ssl.create_default_context()

message = """
Subject: Hi there

This message is sent from Python.

Bye!
"""

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
