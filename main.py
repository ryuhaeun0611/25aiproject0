import streamlit as st

# MBTI와 추천 국가, 국기 이모지, 국가 이미지 URL, 국가 정보
mbti_to_country = {
    "INTJ": {
        "country": "독일 🇩🇪",
        "flag": "🇩🇪",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Flag_of_Germany.svg/1920px-Flag_of_Germany.svg.png",
        "description": "독일은 효율성과 질서를 중요하게 여기는 나라로, INTJ의 전략적이고 체계적인 사고에 적합합니다.",
        "country_info": "독일은 기술 혁신과 교육의 강국으로, 고도로 발전된 산업 기반과 풍부한 역사적 유산을 자랑합니다."
    },
    "INTP": {
        "country": "네덜란드 🇳🇱",
        "flag": "🇳🇱",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/1920px-Flag_of_the_Netherlands.svg.png",
        "description": "네덜란드는 창의적이고 독립적인 사고를 장려하는 환경을 제공하며, INTP의 이론적이고 분석적인 성향에 잘 맞습니다.",
        "country_info": "네덜란드는 자유롭고 개방적인 사회로, 예술과 창의성을 중시하는 풍부한 문화적 환경을 제공합니다."
    },
    "ENTJ": {
        "country": "영국 🇬🇧",
        "flag": "🇬🇧",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Flag_of_the_United_Kingdom.svg/1920px-Flag_of_the_United_Kingdom.svg.png",
        "description": "영국은 정치적, 경제적 중심지로 ENTJ의 리더십을 발휘하기 좋은 국가입니다.",
        "country_info": "영국은 세계적인 금융 중심지와 풍부한 문화유산을 자랑하는 나라입니다."
    },
    "ENTP": {
        "country": "캐나다 🇨🇦",
        "flag": "🇨🇦",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_Canada.svg/1920px-Flag_of_Canada.svg.png",
        "description": "캐나다는 다양성과 창의성을 중요시하는 나라로, ENTP의 혁신적이고 개방적인 사고에 잘 맞습니다.",
        "country_info": "캐나다는 아름다운 자연과 다양한 문화가 공존하는 나라로, 친근하고 개방적인 사회입니다."
    },
    "INFJ": {
        "country": "스위스 🇨🇭",
        "flag": "🇨🇭",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Flag_of_Switzerland.svg/1920px-Flag_of_Switzerland.svg.png",
        "description": "스위스는 평화롭고 조용한 환경을 제공하며, INFJ의 내향적이고 이상주의적인 성격에 잘 맞습니다.",
        "country_info": "스위스는 고도의 정치적 중립성과 아름다운 자연경관으로 잘 알려져 있습니다."
    },
    "INFP": {
        "country": "뉴질랜드 🇳🇿",
        "flag": "🇳🇿",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Flag_of_New_Zealand.svg/1920px-Flag_of_New_Zealand.svg.png",
        "description": "뉴질랜드는 자연과 평화로운 환경을 중시하며, INFP의 이상주의적인 성향을 잘 반영하는 나라입니다.",
        "country_info": "뉴질랜드는 맑은 하늘과 아름다운 자연경관으로 유명하며, 탐험과 모험을 사랑하는 사람들에게 이상적인 장소입니다."
    },
    "ENFJ": {
        "country": "호주 🇦🇺",
        "flag": "🇦🇺",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Flag_of_Australia.svg/1920px-Flag_of_Australia.svg.png",
        "description": "호주는 ENFJ의 사람 중심적이고 사회적인 성격에 잘 맞는 나라로, 다양한 문화가 공존하는 사회입니다.",
        "country_info": "호주는 다양한 문화적 배경을 가진 사람들이 모여 사는 나라로, 아름다운 자연과 해변이 매력적입니다."
    },
    "ENFP": {
        "country": "덴마크 🇩🇰",
        "flag": "🇩🇰",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Flag_of_Denmark.svg/1920px-Flag_of_Denmark.svg.png",
        "description": "덴마크는 창의적이고 자유로운 사회로, ENFP의 열정적이고 개방적인 성격에 잘 맞는 곳입니다.",
        "country_info": "덴마크는 세계에서 가장 행복한 나라 중 하나로, 평등과 복지가 잘 이루어진 사회입니다."
    },
    "ISTJ": {
        "country": "일본 🇯🇵",
        "flag": "🇯🇵",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Japan.svg/1920px-Flag_of_Japan.svg.png",
        "description": "일본은 전통과 규율을 중요시하는 사회로, ISTJ의 성격에 잘 맞습니다.",
        "country_info": "일본은 기술 혁신과 독특한 문화로 세계적으로 유명한 나라입니다."
    }
}

# 페이지 레이아웃과 스타일 설정
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #e1f5fe;
    }
    .stSelectbox, .stButton {
        margin-bottom: 20px;
    }
    .emoji {
        font-size: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# 웹앱 제목
st.title("MBTI 기반 나라 추천 🌏")

# 사용자에게 MBTI 입력 받기
mbti = st.selectbox("당신의 MBTI 유형을 선택하세요 🧠", list(mbti_to_country.keys()))

# MBTI에 맞는 국가 정보
country_info = mbti_to_country.get(mbti)

# 추천된 국가 출력
if country_info:
    st.write(f"당신에게 추천하는 나라는 **{country_info['country']}** 입니다! 🌟")
    st.image(country_info["image"], caption=country_info["country"], use_column_width=True)
    st.write(country_info["description"])
    
    # 나라 선택 후 국가 정보 제공
    st.subheader("🌍 국가 정보:")
    st.write(country_info["country_info"])

    # 비행기 및 구름 이모지
    st.markdown("✈️ ☁️")
else:
    st.write("유효하지 않은 MBTI 유형입니다. 🤔")
