
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("security_model.pkl")

st.set_page_config(
    page_title="Security Incident Prediction",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 Security Incident Prediction")
st.write("Machine Learning Based Security Monitoring System")

st.subheader("Enter Security Details")

login_attempts = st.number_input(
    "Login Attempts", min_value=0, value=5
)

failed_logins = st.number_input(
    "Failed Logins", min_value=0, value=2
)

unusual_activity = st.selectbox(
    "Unusual Activity", [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

if st.button("Predict Security Incident"):

    input_data = pd.DataFrame({
        "login_attempts": [login_attempts],
        "failed_logins": [failed_logins],
        "unusual_activity": [unusual_activity]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("Potential Security Incident Predicted")
    else:
        st.success("No Incident Predicted")

    st.caption(
        "Demo prediction only. Not a validated real-world security alert."
    )
