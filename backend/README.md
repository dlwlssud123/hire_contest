# CareerPath AI - Backend

공공데이터 기반 개인 맞춤형 AI 취업 내비게이션 백엔드 API 서비스입니다.

## 주요 기능 및 모듈 구조

- **`app/api/v1/endpoints/`**: REST API 라우터
  - `profile.py`: 사용자 프로필 등록/조회 및 직업심리검사 연동
  - `job_recommend.py`: 적성 및 역량 기반 AI 직무 추천
  - `recruitments.py`: 고용24 기반 채용공고 및 기업 추천
  - `skill_gap.py`: 보유 역량 vs 채용 요구역량 Skill Gap 분석
  - `path_optimization.py`: 취업 경로 최적화 및 주차별 Action Plan 생성
  - `simulation.py`: What-if 취업 시뮬레이션
  - `market_analysis.py`: 노동시장 통계 및 채용 트렌드 분석
  - `agent.py`: 대화형 AI Career Agent
  - `reports.py`: 종합 AI 취업 전략 보고서 생성 및 관리
- **`app/ai/`**: AI / LLM / RAG / Multi-Agent 엔진
  - `agents/`: 목적별 전문 에이전트 (Career, JobSearch, SkillAnalysis, Education, Company)
  - `rag/`: Vector DB, 임베딩, 검색기 (Retriever)
  - `llm/`: 프롬프트 템플릿 및 LLM 인터페이스
- **`app/integrations/`**: 공공데이터 API 클라이언트
  - `employment24/`: 고용24 (채용공고, 직무정보, 훈련과정, 심리검사)
  - `qnet/`: 한국산업인력공단 국가기술자격 정보
  - `corporate/`: 기업 공공데이터 정보

## 로컬 실행 방법

```bash
# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt

# 환경변수 설정
cp ../.env.example .env

# 서버 실행
uvicorn app.main:app --reload --port 8000
```
