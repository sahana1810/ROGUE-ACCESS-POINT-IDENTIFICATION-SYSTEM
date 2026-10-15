import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("D:\\project 2\\rogue_model.pkl")

# Session state for login
if "login_status" not in st.session_state:
    st.session_state.login_status = False


# ---------- LOGIN PAGE ----------
def login():

    st.title("Rogue Access Point Detection System")

    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "DSC" and password == "project2@":
            st.session_state.login_status = True
            st.success("Login Successful")
            st.rerun()

        else:
            st.error("Invalid Username or Password")


# ---------- PREDICTION PAGE ----------
def detection_page():

    st.title("Rogue Access Point Detection")

    st.write("Enter Wi-Fi parameters")
    ip_address = st.text_input("Enter IP Address")
    duplication = st.selectbox("Duplication", [0,1])
    distance = st.selectbox("Distance Level", [0,1,2])
    encryption = st.selectbox("Encryption Type", [0,1,2,3])
    channel = st.number_input("Channel", min_value=1, max_value=14)
    signal = st.number_input("Signal Strength")

    if st.button("Detect"):

        input_data = np.array([[duplication, distance, encryption, channel, signal]])

        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.error("⚠ Rogue Access Point Detected")

        else:
            st.success("✅ Legitimate Access Point")

    if st.button("Logout"):
        st.session_state.login_status = False
        st.rerun()


# ---------- PAGE CONTROL ----------
if st.session_state.login_status:
    detection_page()
else:
    login()