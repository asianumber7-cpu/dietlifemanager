import './App.css'
import DietForm from './components/DietForm'
import DietHistory from './components/DietHistory'

function App() {
  return (
    <div className="container">
      <div style={{ textAlign: 'center', marginBottom: '30px' }}>
        <h1>💪 Diet & Life Manager</h1>
        <p>AI가 당신에게 딱 맞는 다이어트 계획을 세워드립니다.</p>
      </div>
      
      {/* 입력 폼 컴포넌트 배치 */}
      <DietForm />

      {/* 2. 기록 리스트  */}
      <DietHistory />
      
    </div>
  )
}

export default App