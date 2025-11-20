import { useEffect, useState } from 'react';
import client from '../api/client';

const DietHistory = () => {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);

  // 기록 가져오는 함수
  const fetchHistory = async () => {
    setLoading(true);
    try {
      const response = await client.get('/diets/history');
      setHistory(response.data);
    } catch (error) {
      console.error("기록 로딩 실패:", error);
    } finally {
      setLoading(false);
    }
  };

  // 화면이 켜지자마자 실행
  useEffect(() => {
    fetchHistory();
  }, []);

  return (
    <div className="card">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
        <h2>📅 지난 기록 (History)</h2>
        <button 
          onClick={fetchHistory} 
          style={{ width: 'auto', padding: '8px 15px', fontSize: '14px', backgroundColor: '#2196F3' }}
        >
          새로고침 🔄
        </button>
      </div>

      {loading ? (
        <p>데이터를 불러오는 중...</p>
      ) : (
        <div className="history-list">
          {history.length === 0 ? (
            <p style={{ color: '#999' }}>아직 기록이 없습니다. 위에서 분석을 시작해보세요!</p>
          ) : (
            history.map((item) => (
              <div key={item.id} className="history-item">
                <div className="date-badge">
                  {new Date(item.created_at).toLocaleDateString()} <br/>
                  <small>{new Date(item.created_at).toLocaleTimeString()}</small>
                </div>
                <div className="info">
                  <h4>{item.height}cm / {item.weight}kg ({item.bmi_status})</h4>
                  <p>권장 섭취량: <strong>{item.recommend_calories} kcal</strong></p>
                </div>
              </div>
            ))
          )}
        </div>
      )}
    </div>
  );
};

export default DietHistory;