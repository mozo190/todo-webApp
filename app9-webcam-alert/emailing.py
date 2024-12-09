import imghdr
import smtplib
from email.message import EmailMessage

PASSWORD = "prvwzuwsgxjfubht "
EMAIL_ = "mozo37@gmail.com"
to_email = "mozo37@gmail.com"


# def send_email(image=None):
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#     server.login(email, password)
#     subject = "Security Alert"
#     body = "Intruder detected"
#     msg = f"Subject: {subject}\n\n{body}"
#     server.sendmail(email, to_email, msg)
#     server.quit()

def send_email(image=None):
    email_message = EmailMessage()
    email_message["Subject"] = "Security Alert"
    email_message.set_content("Intruder detected")

    with open(image, "rb") as f:
        file_data = f.read()
        file_name = f.name
        email_message.add_attachment(file_data,
                                     maintype="image",
                                     subtype=imghdr.what(None, file_data),
                                     filename=file_name)
        gmail = smtplib.SMTP("smtp.gmail.com", 587)
        gmail.starttls()
        gmail.login(EMAIL_, PASSWORD)
        gmail.sendmail(EMAIL_, to_email, email_message.as_string())
        gmail.quit()


if __name__ == "__main__":
    send_email(image="images/1.png")
