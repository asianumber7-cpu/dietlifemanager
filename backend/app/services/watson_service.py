import re # <--- [추가] 문자열 필터링 도구
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

# 1. 인증 정보
creds = {
    "url": "https://us-south.ml.cloud.ibm.com", 
    "apikey": "tosW-FZuSPc1pj_BpJBQscRAyylL1PLVDXKA1_Lpcdp1"
}

# 2. 프로젝트 ID
my_project_id = "ac9ed1ee-d917-4b73-bee1-486fe3a733a8"

# 3. 모델 선택 (Llama 3.3)
model_id = "meta-llama/llama-3-3-70b-instruct"

# 4. 파라미터
params = {
    GenParams.DECODING_METHOD: "greedy",
    GenParams.MAX_NEW_TOKENS: 600,
    GenParams.MIN_NEW_TOKENS: 10,
    GenParams.REPETITION_PENALTY: 1.1,
    GenParams.STOP_SEQUENCES: ["```", "def ", "User:", "(Note:"] 
}

def get_diet_advice_from_watson(user_data: dict) -> str:
    print(f"🔍 [디버그] Llama 3.3({model_id})에게 '초등학생 눈높이' 요청 중...")

    try:
        # 모델 초기화
        model = Model(
            model_id=model_id,
            params=params,
            credentials=creds,
            project_id=my_project_id
        )

        # [수정] 대상을 '초등학생'으로 설정 -> 어려운 단어/한자 원천 봉쇄
        prompt_input = f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

You are a kind personal trainer for **Elementary School Students**.
Speak in very simple, pure Korean (Hangul).
**NEVER use Chinese characters (Hanja).**
If you want to say "運動", just say "운동".
Tone: Polite, warm, and easy to understand.

<|eot_id|><|start_header_id|>user<|end_header_id|>

Analyze my data and give advice in Korean.

[My Data]
- Height: {user_data['height']}cm
- Weight: {user_data['weight']}kg
- Age: {user_data['age']}
- Gender: {user_data['gender']}
- Activity: {user_data['activity_level']}
- BMI: {user_data['bmi']} ({user_data['bmi_status']})

[Request]
1. Analyze BMI (Easy explanation).
2. Recommend Korean diet menu.
3. Recommend exercises.
4. Cheering message.

<|eot_id|><|start_header_id|>assistant<|end_header_id|>
안녕하세요! 회원님의 건강 데이터를 알기 쉽게 설명해 드릴게요.
"""

        # 답변 요청
        generated_response = model.generate_text(prompt=prompt_input)
        
        # [핵심] 한자 강제 삭제 필터 (파이썬 코드로 후처리)
        # 정규식: 유니코드 한자 범위(\u4e00-\u9fff)에 해당하는 글자를 빈칸('')으로 바꿈
        clean_response = re.sub(r'[\u4e00-\u9fff]', '', generated_response)

        # 결과 반환
        full_response = "안녕하세요! 회원님의 건강 데이터를 알기 쉽게 설명해 드릴게요.\n" + clean_response.strip()
        return full_response

    except Exception as e:
        print(f"🚨 [치명적 에러] Watson API Error: {e}")
        return f"죄송합니다. AI 연결에 실패했습니다: {e}"