import streamlit as st
import pickle

# Loading the pre-trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Giving a title to the app
st.title("Smartphone Addiction Prediction App")

# Inputting features from the user
st.write("Please provide the following information for the prediction:")

# Hours of smartphone use on weekdays
hrs_weekday_option = st.selectbox("Average Hours of Smartphone Use on Weekdays:", ["Less than 5 hours", "Greater than 5 hours"])
# Assign score based on selection
hrs_weekday_score = 1 if hrs_weekday_option == "Greater than 5 hours" else 0

# Compulsive Behavior
compulsive_behavior = st.slider("Compulsive Behavior (9-36):", 9, 36)

# Functional Impairment
functional_impairment = st.slider("Functional Impairment (8-32):", 8, 32)

# Withdrawal Symptoms
withdrawal = st.slider("Withdrawal Symptoms (6-24):", 6, 24)

# Tolerance
tolerance = st.slider("Tolerance (3-12):", 3, 12)

# Make predictions
if st.button("Predict Smartphone Addiction Score"):
    features = [hrs_weekday_score, compulsive_behavior, functional_impairment, withdrawal, tolerance]
    prediction = model.predict([features])
    st.write(f"Predicted Smartphone Addiction Score: {prediction[0]}")
