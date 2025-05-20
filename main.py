import streamlit as st

# MBTI와 추천 국가 정보를 딕셔너리로 저장
country_recommendations = {
    'INTJ': ('독일', '논리적이고 체계적인 환경에서 효율적으로 일할 수 있어요. 🇩🇪'),
    'INTP': ('네덜란드', '개방적이고 자유로운 분위기에서 창의력을 발휘할 수 있어요. 🇳🇱'),
    'ENTJ': ('영국', '리더십과 전략적 사고를 발휘할 수 있는 환경이에요. 🇬🇧'),
    'ENTP': ('미국', '다양한 아이디어와 창의적인 논의가 자유로운 분위기에서 살아가세요. 🇺🇸'),
    'INFJ': ('스위스', '자연과 평화로운 환경에서 내면의 성장을 이룰 수 있어요. 🇨🇭'),
    'INFP': ('아이슬란드', '자연과 문화가 풍부하고 감성적이고 평화로운 분위기를 좋아해요. 🇮🇸'),
    'ENFJ': ('캐나다', '타인과의 관계를 중요시하며 다양한 문화적 배경이 융합된 곳이에요. 🇨🇦'),
    'ENFP': ('오스트레일리아', '자유롭고 다양한 사람들과의 교류가 활발한 곳이에요. 🇦🇺'),
    'ISFJ': ('일본', '조용하고 질서 정연한 환경에서 타인과의 관계를 소중히 여길 수 있어요. 🇯🇵'),
    'ISFP': ('뉴질랜드', '자연과의 조화 속에서 창조적인 활동을 즐기기 좋은 곳이에요. 🇳🇿'),
    'ESFJ': ('프랑스', '사회적이고 따뜻한 사람들과 함께 조화롭게 살아가기 좋아요. 🇫🇷'),
    'ESFP': ('이탈리아', '사람들과의 즐거운 만남과 활기찬 생활이 가득한 곳이에요. 🇮🇹'),
    'ISTJ': ('핀란드', '조용하고 질서 있는 환경에서 실용적이고 조직적인 생활을 할 수 있어요. 🇫🇮'),
    'ISTP': ('스웨덴', '자유롭고 창의적인 환경에서 실용적인 문제 해결을 할 수 있어요. 🇸🇪'),
    'ESTJ': ('싱가포르', '효율적이고 체계적인 생활을 선호하는 사람들에게 알맞은 곳이에요. 🇸🇬'),
    'ESTP': ('스페인', '활기차고 도전적인 환경에서 모험적인 생활을 즐길 수 있어요. 🇪🇸')
}

# Streamlit 앱 디자인
st.set_page_config(page_title="MBTI에 맞는 나라 추천", page_icon="🌍", layout="centered")

# 배경색 설정
st.markdown("""
    <style>
        body {
            background-color: #FFF9C4;
        }
    </style>
    """, unsafe_allow_html=True)

# 타이틀
st.title("MBTI에 맞는 나라 추천 🌏")

# MBTI 선택
mbti = st.selectbox("당신의 MBTI를 선택하세요!", list(country_recommendations.keys()))

# MBTI에 맞는 나라와 이유를 가져와서 표시
country, reason = country_recommendations[mbti]

st.subheader(f"추천하는 나라는 {country}입니다! {reason}")

# 이모티콘 출력
emoji = {
    'INTJ': '🧠',
    'INTP': '🔍',
    'ENTJ': '👑',
    'ENTP': '💡',
    'INFJ': '🌱',
    'INFP': '🌸',
    'ENFJ': '🤝',
    'ENFP': '🌈',
    'ISFJ': '🍃',
    'ISFP': '🎨',
    'ESFJ': '🎉',
    'ESFP': '🎭',
    'ISTJ': '📚',
    'ISTP': '🛠️',
    'ESTJ': '📊',
    'ESTP': '⚡'
}

st.markdown(f"이모티콘: {emoji[mbti]}")

