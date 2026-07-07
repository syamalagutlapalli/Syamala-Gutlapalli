import streamlit as st

st.set_page_config(page_title="HDI Prediction", page_icon="🌍")

st.title("🌍 Human Development Index (HDI) Prediction")
st.write("Enter the country's development indicators to predict the HDI category.")

life = st.number_input("Life Expectancy at Birth (Years)", min_value=30.0, max_value=100.0, value=70.0)

expected = st.number_input("Expected Years of Schooling", min_value=0.0, max_value=25.0, value=12.0)

mean = st.number_input("Mean Years of Schooling", min_value=0.0, max_value=20.0, value=8.0)

gni = st.number_input("Gross National Income (GNI) per Capita (USD)", min_value=0.0, value=10000.0)

if st.button("Predict HDI"):

    score = 0

    if life >= 80:
        score += 1
    if expected >= 16:
        score += 1
    if mean >= 12:
        score += 1
    if gni >= 25000:
        score += 1

    if score == 4:
        category = "🟢 Very High Human Development"
    elif score == 3:
        category = "🔵 High Human Development"
    elif score == 2:
        category = "🟡 Medium Human Development"
    else:
        category = "🔴 Low Human Development"

    st.success(f"Predicted HDI Category: {category}")

st.markdown("---")
st.caption("Prototype developed for SmartBridge HDI Prediction Project.")
