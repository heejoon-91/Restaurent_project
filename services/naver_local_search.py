import requests
import streamlit as st

NAVER_LOCAL_SEARCH_URL = "https://openapi.naver.com/v1/search/local.json"


def search_restaurants(query: str, display: int = 5):
    headers = {
        "X-Naver-Client-Id": st.secrets["NAVER_API_ID"],
        "X-Naver-Client-Secret": st.secrets["NAVER_API_KEY"],
    }

    params = {
        "query": query,
        "display": display,
        "sort": "comment"  # 리뷰 많은 순
    }

    response = requests.get(
        NAVER_LOCAL_SEARCH_URL,
        headers=headers,
        params=params,
        timeout=5
    )

    response.raise_for_status()
    return response.json()["items"]
