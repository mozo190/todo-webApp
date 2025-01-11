import streamlit as st

from send_email import send_email

st.header("Contact Us")

with st.form(key='contact_form'):
    name = st.text_input("Name")
    email = st.text_input("Your Email address")
    message = st.text_area("Your Message")

    submit = st.form_submit_button("Submit")

    if submit:
        if not name.strip():
            st.error("Please enter your name.")
        elif not email.strip():
            st.error("Please enter your email address.")
        elif not message.strip():
            st.error("Please enter your message.")
        else:

            message_to_you = f"""\
            Subject: New email from {name} ({email})

            From: {email}
            {message}

            Buy!
            """

            try:
                send_email(message_to_you)
                st.success("Your message has been sent!")
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.write(f"Please try again later or contact me directly at zoltan.molnar069@yahoo.com")
