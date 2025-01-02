import streamlit as st
import mailer
import csv

st.header("Contact Page", divider="gray")

with open("topics.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    lst_topics = [row['topic'] for row in csv_reader]
    print(lst_topics)

with st.form("frm_mail"):
    txt_email = st.text_input("Your Email Address")
    txt_option = st.selectbox("How would you like to be contacted?",
                              lst_topics,
                              placeholder="Choose an option")
    txt_message = st.text_area("Your Message:")
    btn_submit = st.form_submit_button("Submit")
    if btn_submit:
        mailer.send(txt_email, txt_option, txt_message)
        st.info("Successfully submitted")
