# CareerPath AI (가칭)
> **공공데이터 기반 개인 맞춤형 AI 취업 내비게이션**  
> *"채용공고를 추천하는 AI가 아니라, 취업까지의 길을 찾아주는 AI"*

---

## 📌 1. 프로젝트 개요

**CareerPath AI**는 단순한 채용공고 나열이나 일회성 추천을 넘어, 구직자의 현재 상태(전공, 역량, 경력, 적성)와 실제 노동시장의 빅데이터(고용24 채용·직무·훈련정보, 국가기술자격정보, 기업 공공데이터)를 결합하여 **목표 직무까지 도달하는 개인별 최적 취업 준비 경로(Action Plan)를 내비게이션처럼 제시하는 AI 기반 고용서비스**입니다.

---

## 🚀 2. 핵심 기능

1. **사용자 프로파일링 & 적성 분석**
   - 전공, 학력, 보유 기술, 희망 조건 및 고용24 직업심리검사(흥미/적성/가치관) 연동
2. **AI 2-트랙 직무 추천**
   - 적성 적합도(Aptitude Match) & 현재 준비도(Readiness) 기반 다각적 직무 추천
3. **고용24 연계 채용공고 & 기업 매칭**
   - 채용공고 요구조건과 사용자 역량 간 일치도 및 구체적 추천 사유(Explainable AI) 제공
4. **정량적 노동시장 빅데이터 기반 Skill Gap 분석**
   - 실제 채용공고 출현 빈도와 사용자 역량을 비교하여 핵심 부족 역량 도출
5. **취업 경로 최적화 & 주차별 Action Plan**
   - 준비 가능 기간(예: 3개월, 6개월)과 시장 중요도를 고려한 단계별 취업 로드맵 생성
6. **고용24 훈련과정 및 국가기술자격 연계**
   - 부족 역량에 대한 K-디지털 트레이닝 과정 및 한국산업인력공단 자격증 자동 매칭
7. **What-if 취업 시뮬레이션**
   - 특정 프로젝트나 자격증 취득 시 목표 직무 취업 준비도 점수 변화 사전 예측
8. **대화형 AI Career Agent (Dynamic Re-planning)**
   - 기간 변경, 지역 확대 등 상황 변화에 따라 실시간으로 취업 경로를 유연하게 재설계
9. **8대 핵심 섹션 통합 AI 취업 전략 보고서 (Career Report)**

---

## 🏗️ 3. 디렉토리 구조

```
hire_contest/
├── backend/                       # FastAPI 기반 백엔드 서비스
│   ├── app/
│   │   ├── api/                   # REST API 엔드포인트
│   │   │   └── v1/
│   │   │       └── endpoints/     # auth, profile, jobs, recruitments, skill_gap, path, simulation, market, agent, reports
│   │   ├── core/                  # DB, 설정, 보안 모듈
│   │   ├── models/                # SQLAlchemy ORM 데이터베이스 모델
│   │   ├── schemas/               # Pydantic 요청/응답 스키마
│   │   ├── services/              # 핵심 비즈니스 로직
│   │   ├── ai/                    # Multi-Agent, RAG, LLM 프롬프트
│   │   │   ├── agents/            # Career, JobSearch, SkillAnalysis, Education, Company Agent
│   │   │   ├── rag/               # Vector Store, Embeddings, Retriever
│   │   │   └── llm/               # LLM 클라이언트 및 프롬프트
│   │   └── integrations/          # 공공데이터 API 클라이언트
│   │       ├── employment24/      # 고용24 (채용, 직무, 훈련, 심리검사)
│   │       ├── qnet/              # Q-Net 한국산업인력공단 국가기술자격
│   │       └── corporate/         # 기업 공공데이터
│   ├── requirements.txt
│   ├── Dockerfile
│   └── README.md
├── frontend/                      # Next.js / React / TypeScript 웹 프론트엔드
│   ├── src/
│   │   ├── components/            # 공통, 로드맵, 스킬갭, 시뮬레이션, 채팅 등
│   │   ├── pages/                 # 페이지 라우터
│   │   ├── services/              # API 연동 서비스
│   │   ├── types/                 # TypeScript 인터페이스
│   │   └── styles/                # Tailwind CSS
│   ├── package.json
│   ├── Dockerfile
│   └── README.md
├── data/                          # 공공데이터 수집 & RAG 임베딩 파이프라인
│   ├── collectors/                # 고용24/Q-Net 데이터 수집기
│   ├── processors/                # 스킬 추출 및 벡터 인덱싱
│   ├── raw/                       # 원본 데이터 저장소
│   └── processed/                 # 정제 데이터 저장소
├── docs/                          # 프로젝트 문서 및 아키텍처
│   ├── architecture/              # 시스템 아키텍처 다이어그램 및 설계서
│   └── api/                       # API 명세서
├── docker-compose.yml             # 전체 컨테이너 오케스트레이션
├── .gitignore
├── .env.example
├── plan.md                        # 서비스 기획서 원문
└── README.md
```

---

## 🛠️ 4. 시작 가이드 (Quick Start)

### Docker Compose로 전체 실행

```bash
# 환경변수 파일 복사 및 설정
cp .env.example .env

# 컨테이너 빌드 및 실행 (Frontend, Backend, PostgreSQL, Redis)
docker-compose up --build
```
- **Frontend**: [http://localhost:3000](http://localhost:3000)
- **Backend API Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📄 5. 라이선스 & 문서 링크

- [서비스 기획서 (plan.md)](plan.md)
- [시스템 아키텍처 (docs/architecture/system_architecture.md)](docs/architecture/system_architecture.md)
- [API 명세서 (docs/api/api_specification.md)](docs/api/api_specification.md)
