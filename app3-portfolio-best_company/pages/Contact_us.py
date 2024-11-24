import streamlit as st
from email import send_email

st.set_page_config(page_title="Contact Us", page_icon="🧊", layout="wide")

st.title("Contact Us")

with st.form(key='my_form'):
    name = st.text_input("Name")
    select_subject = st.selectbox("Subject", ["Job Inquiry", "Proposal", "Other"])
    email = st.text_input("Email")
    message = st.text_area("Write your message here")
    submit = st.form_submit_button("Submit")

    message_to_you = f"""\
    Subject: {select_subject}
    
    From: {name} ({email})
    {message}
    Buy!
    """

    if submit:
        send_email(message_to_you)
        st.info("Your message has been sent!")
