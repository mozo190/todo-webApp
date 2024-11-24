import streamlit as st

from send_email import send_email

st.header("Contact Us")

with st.form(key='contact_form'):
    name = st.text_input("Name")
    email = st.text_input("Your Email address")
    message = st.text_area("Your Message")

    message_to_you = f"""\
    Subject: New email from {name} ({email})
    
    From: {email}
    {message}
    
    Buy!
    """
    submit = st.form_submit_button("Submit")

    if submit:
        send_email(message_to_you)
        st.success("Your message has been sent!")
