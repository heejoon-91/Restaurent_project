import streamlit as st
from domain.restaurant_reco import recommend_restaurant

st.set_page_config(page_title="맛집 추천", page_icon="🍽️")
st.title("🍽️ 약속 지역 맞춤 맛집 추천")

gender = st.selectbox("본인 성별", ["남성", "여성"])
partner_gender = st.selectbox("약속 상대 성별", ["동성", "이성"])
location = st.text_input("만남 지역")
food_pref = st.text_input("선호 음식")

st.caption(
    "선호 음식 5곳 + 다른 카테고리 추천 3곳을 함께 제공합니다."
)

if st.button("추천받기"):
    if not location:
        st.warning("만남 지역은 필수입니다.")
    else:
        info = f"{gender} / {location} / {partner_gender} / {food_pref}"

        with st.spinner("추천 중입니다..."):
            result = recommend_restaurant(info)

        st.write(result)
