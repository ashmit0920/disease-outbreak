import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Epidemic Outbreak")

data = pd.read_csv("google_trends.csv")
emails = pd.read_csv("emails.csv")

st.header(":red[Epidemic] Outbreak Alerts")
st.write("The following plot shows the search interest for Covid during the past 5 years.")

st.line_chart(data, x='date', y='covid', y_label="Search Interest (0-100)")

st.write("Enter your Email-ID below to receive outbreak alerts!")
email = st.text_input("Your email:")

if email:
    emails.loc[len(emails)] = {'email_id': email}
    emails.to_csv("emails.csv", index = False)
    st.success("You will now receive outbreak alerts!")
