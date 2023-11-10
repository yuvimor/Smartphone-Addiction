import streamlit as st
import joblib
import numpy as np

# Load the trained model
model_path = "model.joblib"
model = joblib.load(model_path)

# Streamlit App
def main():
    st.title("Smartphone Addiction Prediction App")

    # Sidebar with user inputs
    st.sidebar.header("Please answer the following:")
    
    # Update this line to use radio button for single choice selection
    weekday_hours = st.sidebar.radio("Average Smartphone Use on Weekdays", ["<5 hours", ">5 hours"])
    
    compulsive_behavior = st.sidebar.slider("Compulsive Behavior", 9, 36, 18)
    functional_impairment = st.sidebar.slider("Functional Impairment", 8, 32, 16)
    withdrawal = st.sidebar.slider("Withdrawal Symptoms", 6, 24, 12)
    tolerance = st.sidebar.slider("Tolerance", 3, 12, 6)

    # Convert categorical inputs to numerical
    weekday_hours = 1 if weekday_hours == ">5 hours" else 0

    # Create a feature array
    features = np.array([weekday_hours, compulsive_behavior, functional_impairment, withdrawal, tolerance])

    # Make prediction
    if st.button("Predict"):
        prediction = model.predict(features.reshape(1, -1))
        st.success(f"The predicted addiction score is: {prediction[0]:.2f}")

if __name__ == "__main__":
    main()
