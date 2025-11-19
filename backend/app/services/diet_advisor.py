from app.schemas.diet import DietInput, DietOutput, ActivityLevel

class DietAdvisorService:
    def calculate(self, data: DietInput) -> DietOutput:
        # 1. BMI 계산 (체질량 지수)
        height_m = data.height / 100
        bmi = round(data.weight / (height_m ** 2), 2)
        
        # BMI 상태 판별
        if bmi < 18.5: status = "저체중"
        elif bmi < 23: status = "정상"
        elif bmi < 25: status = "과체중"
        else: status = "비만"

        # 2. BMR 계산 (기초대사량 - 미플린-지어 공식)
        # 10 x 몸무게 + 6.25 x 키 - 5 x 나이 + (남자는 +5, 여자는 -161)
        base_bmr = (10 * data.weight) + (6.25 * data.height) - (5 * data.age)
        if data.gender.lower() == "male":
            bmr = base_bmr + 5
        else:
            bmr = base_bmr - 161

        # 3. TDEE 계산 (활동 대사량 - 하루 총 소비 칼로리)
        activity_multipliers = {
            ActivityLevel.SEDENTARY: 1.2,
            ActivityLevel.LIGHTLY_ACTIVE: 1.375,
            ActivityLevel.MODERATELY_ACTIVE: 1.55,
            ActivityLevel.VERY_ACTIVE: 1.725,
            ActivityLevel.EXTRA_ACTIVE: 1.9
        }
        multiplier = activity_multipliers.get(data.activity_level, 1.2)
        tdee = round(bmr * multiplier)

        # 4. 다이어트 추천 칼로리 (보통 유지 칼로리에서 500kcal를 뺍니다)
        target_calories = tdee - 500
        if target_calories < 1200: target_calories = 1200 # 최소 섭취량 보호

        # 5. 조언 생성
        advice = f"회원님은 현재 {status} 상태입니다. 기초대사량은 {int(bmr)}kcal이며, 현재 활동량을 고려했을 때 하루에 {int(tdee)}kcal를 소모하고 계십니다. 건강한 감량을 위해 하루 {int(target_calories)}kcal 섭취를 권장합니다."

        return DietOutput(
            bmi=bmi,
            bmi_status=status,
            bmr=round(bmr),
            tdee=tdee,
            recommend_calories=target_calories,
            advice=advice
        )

# 인스턴스 생성 (싱글톤처럼 사용)
diet_advisor = DietAdvisorService()