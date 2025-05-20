import streamlit as st

# MBTI와 추천 국가, 국기 이모지, 국가 이미지 URL 데이터
mbti_to_country = {
    "INTJ": {
        "country": "독일 🇩🇪",
        "flag": "🇩🇪",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Flag_of_Germany.svg/1920px-Flag_of_Germany.svg.png",
        "description": "독일은 효율성, 혁신성, 그리고 질서 정연한 삶을 중요하게 여깁니다. INTJ 타입에게 매우 잘 맞는 나라입니다."
    },
    "INTP": {
        "country": "네덜란드 🇳🇱",
        "flag": "🇳🇱",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/1920px-Flag_of_the_Netherlands.svg.png",
        "description": "네덜란드는 창의적이고 독립적인 사고를 중요시하는 나라로, INTP와 잘 맞는 환경을 제공합니다."
    },
    "ENTJ": {
        "country": "영국 🇬🇧",
        "flag": "🇬🇧",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Flag_of_the_United_Kingdom.svg/1920px-Flag_of_the_United_Kingdom.svg.png",
        "description": "영국은 정치적, 경제적으로 중요한 국가로, ENTJ의 리더십을 발휘하기 좋은 곳입니다."
    },
    "ENTP": {
        "country": "캐나다 🇨🇦",
        "flag": "🇨🇦",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_Canada.svg/1920px-Flag_of_Canada.svg.png",
        "description": "캐나다는 다양성과 개방성을 중요시하는 나라로, ENTP의 창의적이고 개방적인 성격과 잘 맞습니다."
    },
    "INFJ": {
        "country": "스위스 🇨🇭",
        "flag": "🇨🇭",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Flag_of_Switzerland.svg/1920px-Flag_of_Switzerland.svg.png",
        "description": "스위스는 평화롭고 안정적인 환경을 제공하며, INFJ의 내향적이고 이상주의적인 성격에 적합한 국가입니다."
    },
    "INFP": {
        "country": "뉴질랜드 🇳🇿",
        "flag": "🇳🇿",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Flag_of_New_Zealand.svg/1920px-Flag_of_New_Zealand.svg.png",
        "description": "자연과 평화로운 환경을 중시하는 뉴질랜드는 INFP의 이상주의적인 성향을 잘 반영합니다."
    },
    "ENFJ": {
        "country": "호주 🇦🇺",
        "flag": "🇦🇺",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Flag_of_Australia.svg/1920px-Flag_of_Australia.svg.png",
        "description": "호주는 ENFJ의 사람 중심적이고 사회적인 성격에 잘 맞는 나라로, 다양한 문화가 공존합니다."
    },
    "ENFP": {
        "country": "덴마크 🇩🇰",
        "flag": "🇩🇰",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Flag_of_Denmark.svg/1920px-Flag_of_Denmark.svg.png",
        "description": "덴마크는 창의적이고 자유로운 사회로, ENFP의 열정적이고 에너지 넘치는 성격과 잘 어울립니다."
    },
    "ISTJ": {
        "country": "일본 🇯🇵",
        "flag": "🇯🇵",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Japan.svg/1920px-Flag_of_Japan.svg.png",
        "description": "일본은 전통과 규율을 중요시하는 사회로, ISTJ의 성격에 잘 맞습니다."
    },
    "ISFJ": {
        "country": "핀란드 🇫🇮",
        "flag": "🇫🇮",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Flag_of_Finland.svg/1920px-Flag_of_Finland.svg.png",
        "description": "핀란드는 조용하고 안정적인 환경을 제공하며, ISFJ의 보호자 성향과 잘 맞습니다."
    },
    "ESTJ": {
        "country": "스웨덴 🇸🇪",
        "flag": "🇸🇪",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Flag_of_Sweden.svg/1920px-Flag_of_Sweden.svg.png",
        "description": "스웨덴은 효율적이고 실용적인 나라로, ESTJ의 관리 능력을 발휘하기 좋은 국가입니다."
    },
    "ESFJ": {
        "country": "미국 🇺🇸",
        "flag": "🇺🇸",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Flag_of_the_United_States.svg/1920px-Flag_of_the_United_States.svg.png",
        "description": "미국은 활발하고 사람 중심적인 사회로, ESFJ의 사회적인 성격과 잘 맞습니다."
    },
    "ISTP": {
        "country": "아이슬란드 🇮🇸",
        "flag": "🇮🇸",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Flag_of_Iceland.svg/1920px-Flag_of_Iceland.svg.png",
        "description": "아이슬란드는 자연과 모험을 중시하는 나라로, ISTP의 탐험적인 성향과 잘 맞습니다."
    },
    "ISFP": {
        "country": "포르투갈 🇵🇹",
        "flag": "🇵🇹",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/1920px-Flag_of_Portugal.svg.png",
        "description": "포르투갈은 예술적이고 자연을 사랑하는 사람들에게 적합한 환경을 제공합니다."
    },
    "ESTP": {
        "country": "스페인 🇪🇸",
        "flag": "🇪🇸",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/a9/Flag_of_Spain.svg/1920px-Flag_of_Spain.svg.png",
        "description": "스페인은 활발하고 역동적인 문화로 ESTP의 에너지 넘치는 성격과 잘 맞습니다."
    },
    "ESFP": {
        "country": "이탈리아 🇮🇹",
        "flag": "🇮🇹",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/1920px-Flag_of_Italy.svg.png",
        "description": "이탈리아는 예술적이고 감각적인 삶을 중시하는 나라로, ESFP의 자유롭고 외향적인 성격에 잘 어울립니다."
    }
}

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
else:
    st.write("유효하지 않은 MBTI 유형입니다. 🤔")


