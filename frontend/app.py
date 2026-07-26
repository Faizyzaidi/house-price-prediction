import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction")
st.write("Enter the details below to predict the house price.")

# Input fields
income = st.number_input(
    "Average Area Income",
    min_value=0.0,
    value=70000.0
)

house_age = st.number_input(
    "Average Area House Age",
    min_value=0.0,
    value=6.0
)

rooms = st.number_input(
    "Average Number of Rooms",
    min_value=0.0,
    value=7.0
)

bedrooms = st.number_input(
    "Average Number of Bedrooms",
    min_value=0.0,
    value=4.0
)

population = st.number_input(
    "Area Population",
    min_value=0.0,
    value=35000.0
)

# Predict button
if st.button("Predict House Price"):

    payload = {
        "avg_area_income": income,
        "avg_area_house_age": house_age,
        "avg_area_number_of_rooms": rooms,
        "avg_area_number_of_bedrooms": bedrooms,
        "area_population": population
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        if response.status_code == 200:
            result = response.json()

            st.success(
                f"🏡 Predicted House Price: ${result['Predicted Price']:,.2f}"
            )

        else:
            st.error("Prediction failed!")

    except Exception as e:
        st.error(f"Could not connect to FastAPI.\n\n{e}")