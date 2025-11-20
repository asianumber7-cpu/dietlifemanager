import { useState } from 'react';
import client from '../api/client';

const DietForm = () => {
  // 1. 입력값 상태 관리 (변수들)
  const [formData, setFormData] = useState({
    height: '',
    weight: '',
    age: '',
    gender: 'male',
    activity_level: 'sedentary'
  });
  
  const [result, setResult] = useState(null); // 결과 저장용
  const [loading, setLoading] = useState(false); // 로딩 상태

  // 2. 입력값이 바뀔 때마다 변수에 저장
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  // 3. 버튼 눌렀을 때 백엔드로 전송
  const handleSubmit = async (e) => {
    e.preventDefault(); // 새로고침 방지
    setLoading(true);

    try {
      // 숫자로 변환해서 보내야 함 (안 그러면 문자열로 가서 에러 남)
      const payload = {
        ...formData,
        height: Number(formData.height),
        weight: Number(formData.weight),
        age: Number(formData.age),
      };

      // 백엔드 요청!
      const response = await client.post('/diets/calculate', payload);
      setResult(response.data); // 결과 받아서 저장
    } catch (error) {
      alert("입력값을 확인해주세요! (나이는 0보다 커야 합니다)");
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>📋 신체 정보 입력</h2>
      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <label>키 (cm)</label>
          <input type="number" name="height" value={formData.height} onChange={handleChange} required placeholder="예: 175" />
        </div>
        <div className="input-group">
          <label>몸무게 (kg)</label>
          <input type="number" name="weight" value={formData.weight} onChange={handleChange} required placeholder="예: 70" />
        </div>
        <div className="input-group">
          <label>나이</label>
          <input type="number" name="age" value={formData.age} onChange={handleChange} required placeholder="예: 30" />
        </div>
        <div className="input-group">
          <label>성별</label>
          <select name="gender" value={formData.gender} onChange={handleChange}>
            <option value="male">남성</option>
            <option value="female">여성</option>
          </select>
        </div>
        <div className="input-group">
          <label>활동량</label>
          <select name="activity_level" value={formData.activity_level} onChange={handleChange}>
            <option value="sedentary">운동 안 함 (사무직)</option>
            <option value="lightly">가벼운 활동 (주 1-3회)</option>
            <option value="moderate">보통 활동 (주 3-5회)</option>
            <option value="active">활발한 활동 (주 6-7회)</option>
            <option value="extra">매우 활발 (운동선수)</option>
          </select>
        </div>
        
        <button type="submit" disabled={loading}>
          {loading ? "AI 분석 중..." : "분석 시작 🚀"}
        </button>
      </form>

      {/* 결과가 있으면 보여주기 */}
      {result && (
        <div className="result-box">
          <h3>🎉 분석 결과</h3>
          <p>당신의 BMI는 <span className="highlight">{result.bmi}</span> ({result.bmi_status}) 입니다.</p>
          <p>기초대사량: <strong>{result.bmr} kcal</strong></p>
          <p>하루 권장 섭취량: <span className="highlight">{result.recommend_calories} kcal</span></p>
          <hr />
          <p><strong>💡 AI 조언:</strong><br/>{result.advice}</p>
        </div>
      )}
    </div>
  );
};

export default DietForm;