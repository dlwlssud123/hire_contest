# CareerPath AI - Data Pipeline

고용24 채용정보, 직무정보, 직업심리검사, 훈련과정 및 한국산업인력공단 국가기술자격 데이터 수집/정제/RAG 벡터 색인 파이프라인입니다.

## 폴더 구성

- **`collectors/`**: 공공데이터 API 및 크롤러 배치 스크립트
  - `collect_employment24.py`: 고용24 채용공고 및 직무 데이터 수집
  - `collect_trainings.py`: 고용24 K-디지털/직업훈련 과정 수집
  - `collect_certifications.py`: Q-Net 국가기술자격 데이터 수집
- **`processors/`**: 비정형 텍스트 정제, 역량 키워드 추출 및 벡터 임베딩 생성
  - `extract_skills.py`: 채용공고 텍스트 대상 스킬 엔티티 추출
  - `build_embeddings.py`: LLM RAG용 Vector DB 인덱싱
- **`raw/`**: 수집된 원본 데이터 파일 (JSON/CSV)
- **`processed/`**: 정제 및 임베딩 완료된 데이터 세트
