
import streamlit as st
import pandas as pd

# Load the CSV data
df = pd.read_csv("astrology_zodiac_data_en_full.csv")

# Sign degree start mapping
sign_degrees = {
    "Aries": 0, "Taurus": 30, "Gemini": 60, "Cancer": 90,
    "Leo": 120, "Virgo": 150, "Libra": 180, "Scorpio": 210,
    "Sagittarius": 240, "Capricorn": 270, "Aquarius": 300, "Pisces": 330
}

st.title("Zodiac Degree Analyzer (Dropdown Version)")

# Input method selection
input_mode = st.radio("Select input method:", ["Sign + Degree + Minute", "Decimal Degree (0–360)"])

if input_mode == "Sign + Degree + Minute":
    sign = st.selectbox("Sign", list(sign_degrees.keys()))
    degree = st.selectbox("Degree (°)", list(range(0, 30)))
    minute = st.selectbox("Minutes (′)", list(range(0, 60)))

    decimal_degree = sign_degrees[sign] + degree + minute / 60

else:
    decimal_degree = st.slider("Decimal Degree", 0.0, 359.9833, 0.0, step=0.0167)

# Match row in dataframe
row = df[(df["Decimal Start"] <= decimal_degree) & (df["Decimal End"] > decimal_degree)]

if not row.empty:
    st.subheader("Result:")
    for col in ["Sign", "Duad", "Decan", "Bound", "Numerology", "Sabian Text"]:
        st.write(f"**{col}:** {row.iloc[0][col]}")
else:
    st.error("No matching range found.")
