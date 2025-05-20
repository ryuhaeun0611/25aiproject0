import streamlit as st
import pandas as pd

# MBTI와 추천 국가 데이터
mbti_to_country = {
    "INTJ": "독일",
    "INTP": "네덜란드",
    "ENTJ": "영국",
    "ENTP": "캐나다",
    "INFJ": "스위스",
    "INFP": "뉴질랜드",
    "ENFJ": "호주",
    "ENFP": "덴마크",
    "ISTJ": "일본",
    "ISFJ": "핀란드",
    "ESTJ": "스웨덴",
    "ESFJ": "미국",
    "ISTP": "아이슬란드",
    "ISFP": "포르투갈",
    "ESTP": "스페인",
    "ESFP": "이탈리아"
}

# 웹앱 제목
st.title("MBTI 기반 나라 추천")

# 사용자에게 MBTI 입력 받기
mbti = st.selectbox("당신의 MBTI 유형을 선택하세요", list(mbti_to_country.keys()))

# MBTI에 맞는 국가 추천
recommended_country = mbti_to_country.get(mbti)

# 추천된 국가 출력
if recommended_country:
    st.write(f"당신에게 추천하는 나라는 **{recommended_country}** 입니다!")
else:
    st.write("유효하지 않은 MBTI 유형입니다.")

