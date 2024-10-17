import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Epidemic Outbreak")

data = pd.read_csv("malaria.csv")
emails = pd.read_csv("emails.csv")

st.header(":red[Epidemic] Outbreak Alerts")
st.write("The following plot shows the search interest for Malaria during the past 5 years. It is visible that spikes are formed when the search interest crosses 40.")

st.line_chart(data, x='date', y='malaria', y_label="Search Interest (0-100)")

st.write("Enter your Email-ID below to receive outbreak alerts!")
email = st.text_input("Your email:")

if email:
    emails.loc[len(emails)] = {'email_id': email}
    emails.to_csv("emails.csv", index = False)
    st.success("You will now receive outbreak alerts!")
