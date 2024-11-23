import streamlit as st

st.header("Contact Us")

with st.form(key='contact_form'):
    name = st.text_input("Name")
    email = st.text_input("Your Email address")
    message = st.text_area("Message")
    submit = st.form_submit_button("Submit")

    if submit:
        st.write(f"Thank you {name} for your message. We will contact you soon.")
        st.stop()

