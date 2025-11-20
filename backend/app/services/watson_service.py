from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

# 1. 인증 정보
creds = {
    "url": "https://us-south.ml.cloud.ibm.com", 
    "apikey": "tosW-FZuSPc1pj_BpJBQscRAyylL1PLVDXKA1_Lpcdp1"
}

# 2. 프로젝트 ID
my_project_id = "ac9ed1ee-d917-4b73-bee1-486fe3a733a8"

# 3. 모델 선택 (GPT-120B)
model_id = "openai/gpt-oss-120b"

# 4. 파라미터 (잡담 금지 설정)
params = {
    GenParams.DECODING_METHOD: "greedy",
    GenParams.MAX_NEW_TOKENS: 400,
    GenParams.MIN_NEW_TOKENS: 1,
    GenParams.REPETITION_PENALTY: 1.1,
    # "User:"가 나오면 멈추라는 뜻 (자기 혼자 1인 2역 하는 것 방지)
    GenParams.STOP_SEQUENCES: ["User:", "System:"] 
}

def get_diet_advice_from_watson(user_data: dict) -> str:
    print(f"🔍 [디버그] {model_id} 모델에게 강력한 명령 전송 중...")

    try:
        # 모델 초기화
        model = Model(
            model_id=model_id,
            params=params,
            credentials=creds,
            project_id=my_project_id
        )

        # [핵심 수정] 대화형 포맷 (Chat Format) 적용
        # System: 역할 부여 / User: 질문 / Assistant: 답변 시작
        prompt_input = f"""
System: You are a professional Korean Dietitian. You must answer in Korean only. Do not generate thoughts, just give the advice.

User: 
제 정보는 다음과 같습니다:
- 키: {user_data['height']}cm
- 몸무게: {user_data['weight']}kg
- BMI: {user_data['bmi']} ({user_data['bmi_status']})

이 정보를 바탕으로 건강 상태 분석, 한국식 식단 추천, 운동 추천, 응원 메시지를 한국어로 작성해주세요.

Assistant:
안녕하세요! 회원님의 건강 데이터를 분석해 드릴게요.
"""

        # 답변 요청
        generated_response = model.generate_text(prompt=prompt_input)
        
        # 우리가 적은 첫마디 + AI 답변
        full_response = "안녕하세요! 회원님의 건강 데이터를 분석해 드릴게요.\n" + generated_response.strip()
        return full_response

    except Exception as e:
        print(f"🚨 [치명적 에러] Watson API Error: {e}")
        return f"AI 연결 실패: {e}"