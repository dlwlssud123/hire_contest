import os
import json
import httpx


def fetch_employment24_jobs(api_key: str):
    """
    고용24 채용정보 수집 배치 스크립트 (plan.md 9.1)
    """
    print("[Batch] 고용24 채용공고 수집 시작...")
    # Mock collection logic
    data = [
        {"id": "EMP01", "title": "Java 백엔드 신입 개발자", "company": "ABC테크"},
        {"id": "EMP02", "title": "Spring Boot 웹 개발자", "company": "XYZ솔루션"}
    ]
    os.makedirs("data/raw", exist_ok=True)
    with open("data/raw/employment24_jobs.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[Batch] 수집 완료: {len(data)}건 저장됨.")


if __name__ == "__main__":
    fetch_employment24_jobs(api_key=os.getenv("EMPLOYMENT24_API_KEY", ""))
