import streamlit as st
import requests

# Use the local URL where your FastAPI server is running
API_URL = "http://127.0.0.1:8000/predict" 

st.set_page_config(page_title="Insurance Predictor", page_icon="🏥")

st.title("🏥 Insurance Premium Predictor")
st.markdown("Enter your details below to estimate your premium category.")

# Create two columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=119, value=30)
    weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
    height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
    income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)

with col2:
    smoker = st.selectbox("Are you a smoker?", options=[True, False])
    city = st.text_input("City", value="Mumbai")
    occupation = st.selectbox(
        "Occupation",
        ['private_job', 'government_job', 'business_owner', 'freelancer', 'student', 'retired', 'unemployed']
    )

st.divider()

if st.button("Calculate Premium Category", type="primary"):
    # 1. Prepare data (must match InsuranceData Pydantic model)
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    try:
        with st.spinner("Talking to API..."):
            response = requests.post(API_URL, json=input_data)
            
        if response.status_code == 200:
            result = response.json()
            
            # 2. Extract the key we defined in the FastAPI return statement
            prediction = result.get("predicted_insurance_premium")
            
            st.balloons()
            st.success(f"### Predicted Premium: **{prediction}**")
            
            # Show calculated metrics from the API for transparency
            with st.expander("See Calculated Metrics"):
                st.info("These values were calculated by the API logic:")
                # Note: These keys depend on if you return data.bmi etc. in your FastAPI response
                st.write(f"**BMI:** {weight / (height**2):.2f}")
        else:
            st.error(f"API Error: {response.status_code}")
            st.write(response.json())

    except requests.exceptions.ConnectionError:
        st.error("❌ Connection Refused. Ensure your FastAPI server is running at the same URL.")