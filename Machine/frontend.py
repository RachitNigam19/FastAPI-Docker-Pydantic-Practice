import requests 
import streamlit as st

# url of backend
api_url = "http://127.0.0.1:8000/predict"

# title of the site 
st.title("Insurance Premium Category Predictor")

st.markdown("Enter Your Details Below:")

# Input Fields
age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight(Kg)", min_value=1, max_value=300, value=80)
height = st.number_input("Height (m)", min_value=0.1, max_value=3.0, value=2.5)
income_lpa = st.number_input("Income (LPA)", min_value=1.0, value=10.0)
smoker = st.selectbox("Are you a smoker?" ,options=['Yes','No'])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox(
              "Occupation",
              ['retired','freelancer', 'student', 'goverment_job', 'buisness_owner', 'unemployed', 'private_job']
              )

if st.button("Predict Premium category"):
              input_data = {
                      "age": age,
                      "weight":weight,
                      "height":height,
                      "income_lpa":income_lpa,
                      "smoker":smoker,
                      "city":city,
                      "occupation":occupation
              }

              try:
                      response = requests.post(api_url, json=input_data)
                      if response.status_code == 200:
                              result = response.json()
                              st.success(f"Predicted Insurance Premium Category: **{result['predicted_category']}**")
                      else:
                              st.error(f"API Error: {response.status_code} - {response.text}")
              except requests.exceptions.ConnectionError:
                      st.error("Could not connect to the fast api server. Make sure its running on the port 8000.")
