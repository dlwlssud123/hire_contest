# CareerPath AI REST API 명세서 (API Specification)

기본 엔드포인트 URL: `http://localhost:8000/api/v1`

## 1. 인증 및 사용자 관리 (`/auth`)
- `POST /auth/register`: 회원가입
- `POST /auth/login`: 로그인 및 JWT 토큰 발급

## 2. 프로필 관리 (`/profile`)
- `GET /profile/{user_id}`: 사용자 프로필 및 심리검사 데이터 조회
- `POST /profile/{user_id}`: 사용자 프로필 등록 및 갱신

## 3. 직무 및 채용 추천 (`/jobs`, `/recruitments`)
- `GET /jobs/recommendations/{user_id}`: AI 2-트랙(적성 적합도 / 준비도) 직무 추천
- `GET /recruitments/search`: 고용24 연계 채용공고 검색 및 매칭 사유 조회

## 4. Skill Gap 분석 (`/skill-gap`)
- `GET /skill-gap/analyze`: 목표 직무와 보유 역량 간의 Skill Gap 및 출현 빈도 분석

## 5. 취업 경로 최적화 (`/path`)
- `POST /path/optimize`: 목표 직무 및 준비 기간(개월) 기반 주차별 Action Plan 생성

## 6. What-if 시뮬레이션 (`/simulation`)
- `POST /simulation/simulate`: 활동(프로젝트/자격증 등) 추가에 따른 취업 준비도 변화 시뮬레이션

## 7. 노동시장 분석 (`/market`)
- `GET /market/insights`: 직무별 요구 역량 통계 및 시장 트렌드 데이터 조회

## 8. 대화형 AI 커리어 에이전트 (`/agent`)
- `POST /agent/chat`: 대화형 조건 변경 및 취업 경로 동적 재설계

## 9. AI 취업 전략 보고서 (`/reports`)
- `GET /reports/generate`: 8대 핵심 섹션 통합 AI Career Report 생성
