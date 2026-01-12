from services.openai_client import get_openai_client
from services.naver_local_search import search_restaurants

SYSTEM_PROMPT = """
Role (페르소나):
너는 우리나라에서 맛집을 가장 많이 가본 맛잘알이다.
추천한 맛집에 대한 만족도가 매우 높다.

Context (맥락):
입력자는 약속이 있는 상황이며,
성별 조합과 만남 목적에 어울리는 음식점을 찾고 있다.

Task (지시 사항):
- 입력자의 성별
- 약속 상대의 성별 (동성/이성)
- 만남 지역
- 선호 음식 카테고리
를 종합적으로 고려하여 음식점을 추천하라.

추천 규칙:
1. 총 8개의 음식점을 추천한다.
2. 구성은 다음과 같이 한다.
   - 선호 음식 카테고리 기반 추천: 5곳
   - 선호하지 않은 다른 카테고리 추천: 3곳
3. 다른 카테고리 추천은 다음 기준을 따른다.
   - 데이트/모임 분위기 보완
   - 해당 지역에서 특히 평이 좋은 곳
   - 선호 카테고리를 싫어하더라도 무난한 선택
4. 추천 후보들을 웹에서 검색하여 실제로 있는 음식점일 경우에만 사용자에게 추천한다.

출력 형식:
- [선호 카테고리 추천]
- [다른 카테고리 추천]
으로 섹션을 나누어 명확히 구분한다.

각 음식점마다 반드시 포함할 정보:
- 음식점 이름
- 음식 국적
- 대표 메뉴
- 추천 메뉴
- 추천 이유
- 영업시간
- 휴무일
- 전화번호

실제로 존재하지 않을 가능성이 있는 음식점 이름은 생성하지 말고,
모호할 경우 체인점 또는 널리 알려진 상호를 우선하라.
"""

# def recommend_restaurant(
#     info: str,
#     model: str = "gpt-4.1-mini",
#     temperature: float = 1.0,
#     top_p: float = 1.0,
#     max_tokens: int = 2048,
# ) -> str:
#     client = get_openai_client()

#     response = client.chat.completions.create(
#         model=model,
#         messages=[
#             {"role": "system", "content": SYSTEM_PROMPT},
#             {"role": "user", "content": f"성별/만남 장소/동성자 성별 : {info}"}
#         ],
#         temperature=temperature,
#         top_p=top_p,
#         max_completion_tokens=max_tokens,
#     )

#     return response.choices[0].message.content

# from services.openai_client import get_openai_client


def recommend_restaurant(prompt: str):
    client = get_openai_client()

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "input_text",
                        "text": SYSTEM_PROMPT
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": prompt
                    }
                ]
            }
        ],
        tools=search_restaurants(),
        max_output_tokens=2048
    )

    return response.output_text


# from services.openai_client import get_openai_client
# from services.web_search_config import WEB_SEARCH_TOOL

# def recommend_restaurant(prompt):
#     client = get_openai_client()

#     response = client.responses.create(
#         model="gpt-4.1-mini",

#         input=prompt,
#         tools=WEB_SEARCH_TOOL,
#         max_output_tokens=2048
#     )
#     return response.output_text

