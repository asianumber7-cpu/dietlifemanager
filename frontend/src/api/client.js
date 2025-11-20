import axios from 'axios';

// 백엔드 주소를 미리 설정해둡니다.
const client = axios.create({
  baseURL: 'http://localhost:8000/api/v1', // 공통 주소
  headers: {
    'Content-Type': 'application/json',
  },
});

export default client;