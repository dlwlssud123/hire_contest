# CareerPath AI 시스템 아키텍처 (System Architecture)

본 문서는 `plan.md`를 바탕으로 설계된 CareerPath AI(공공데이터 기반 개인 맞춤형 AI 취업 내비게이션)의 전체 시스템 아키텍처를 정의합니다.

## 1. 아키텍처 다이어그램 (Architecture Diagram)

```text
                 ┌─────────────────────────────────────────┐
                 │       Frontend (Next.js / React)        │
                 │   - 대시보드 / Skill Gap / 로드맵 / 채팅  │
                 └────────────────────┬────────────────────┘
                                      │ REST API / WebSocket
                 ┌────────────────────▼────────────────────┐
                 │        Backend API (FastAPI)            │
                 │   - Auth, Profile, Recommend, Sim, Rep  │
                 └────────────────────┬────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────┐
        ▼                             ▼                             ▼
┌──────────────┐             ┌─────────────────┐           ┌─────────────────┐
│ AI & Agents  │             │ Data Pipeline   │           │ Integrations    │
│ - Career     │             │ - Collectors    │           │ - 고용24 (채용/직무)│
│ - JobSearch  │             │ - Extractors    │           │ - 고용24 (훈련/검사)│
│ - SkillGap   │             │ - Vector Embed  │           │ - Q-Net 국가자격 │
│ - Education  │             └────────┬────────┘           │ - 기업 공공데이터 │
│ - Company    │                      │                    └────────┬────────┘
└───────┬──────┘                      │                             │
        │                             ▼                             │
        │                    ┌─────────────────┐                    │
        └───────────────────►│ RAG Vector DB   │◄───────────────────┘
                             │ (Chroma/pgvector│
                             └─────────────────┘
```

## 2. 핵심 계층별 구성

### 2.1 Frontend
- **사용자 프로필 & 심리검사 연동**: 사용자의 학력, 전공, 보유 역량 및 심리검사 결과 입력
- **Skill Gap 시각화**: 목표 직무 시장 요구빈도 vs 보유 역량 비교 차트
- **취업 내비게이션 타임라인**: 단계별/주차별 최적화 Action Plan 인터페이스
- **What-if 시뮬레이터**: 활동 추가 시 준비도 점수 변화 실시간 시뮬레이션
- **대화형 커리어 에이전트**: 조건 변경 및 Dynamic Re-planning 챗봇

### 2.2 Backend & Services
- **ProfileService**: 사용자 정보 및 심리검사 프로파일링
- **JobMatchService**: 적성 적합도 & 현재 준비도 2-트랙 직무 매칭
- **SkillGapService**: 노동시장 빅데이터 기반 역량 차이 분석
- **PathOptimizerService**: 시간/상황 제약을 고려한 취업 경로 최적화
- **SimulationService**: 활동별 준비도 점수 변화 시뮬레이션
- **ReportService**: 8대 핵심 섹션 통합 AI Career Report 생성

### 2.3 AI & Multi-Agent Architecture
- **Career Agent**: 사용자와의 질의응답 및 로드맵 동적 재설계 총괄
- **Job Search Agent**: 고용24 실시간 채용공고 탐색 및 적합도 랭킹
- **Skill Analysis Agent**: 채용공고 텍스트에서 기술 엔티티 추출 및 시장 요구빈도 통계화
- **Education Agent**: 부족 역량을 해소할 수 있는 국비지원 훈련과정 및 자격증 연계
- **Company Agent**: 기업 규모, 재무/복지 정보 등 기업 특성 분석

### 2.4 Integrations & Public Data
- 고용24 (워크넷) 채용공고 및 직업/직무 정보 API
- 고용24 직업심리검사 (흥미/적성/가치관)
- 고용24 (HRD-Net) 직업훈련과정 API
- 한국산업인력공단 (Q-Net) 국가기술자격 API
- 공공데이터포털 기업 정보 API
