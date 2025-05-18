import streamlit as st
import pandas as pd
import re

# CSV 파일 로드
df = pd.read_csv("astrology_zodiac_data_en_full.csv")

# 별자리 각도 시작점 매핑
sign_degrees = {
    "aries": 0, "taurus": 30, "gemini": 60, "cancer": 90,
    "leo": 120, "virgo": 150, "libra": 180, "scorpio": 210,
    "sagittarius": 240, "capricorn": 270, "aquarius": 300, "pisces": 330
}

# 입력값을 십진수 각도로 변환
def parse_degree_input(input_str):
    input_str = input_str.lower().replace("′", "'").replace("’", "'").strip()

    # 숫자 입력: 예) 157.34
    if re.match(r"^\d+(\.\d+)?$", input_str):
        return float(input_str)

    # 별자리 + 도수 입력: 예) Aries 20°34 또는 20°34 Aries
    match = re.match(r"(?:(\d+)°(\d+)\s*)?(aries|taurus|gemini|cancer|leo|virgo|libra|scorpio|sagittarius|capricorn|aquarius|pisces)", input_str)
    if not match:
        match = re.match(r"(aries|taurus|gemini|cancer|leo|virgo|libra|scorpio|sagittarius|capricorn|aquarius|pisces)\s*(\d+)°(\d+)", input_str)

    if match:
        if match.lastindex == 3:
            d1, d2, sign = match.groups()
        else:
            sign, d1, d2 = match.groups()
        base = sign_degrees[sign.lower()]
        deg = int(d1) + int(d2) / 60
        return base + deg

    return None

# 앱 UI
st.title("Zodiac Degree Analyzer")

input_str = st.text_input("Enter degree (e.g., 'Aries 20°34' or '157.56')")

if input_str:
    degree = parse_degree_input(input_str)
    if degree is not None:
        row = df[(df["Decimal Start"] <= degree) & (df["Decimal End"] > degree)]
        if not row.empty:
            st.subheader("Result:")
            for col in ["Sign", "Duad", "Decan", "Bound", "Numerology", "Sabian Text"]:
                st.write(f"**{col}:** {row.iloc[0][col]}")
        else:
            st.error("No matching range found.")
    else:
        st.error("Could not parse the input. Try formats like 'Aries 20°34' or '157.56'.")
