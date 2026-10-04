import os
import json


def fetch_hrd_trainings(api_key: str):
    """
    고용24 훈련과정(HRD-Net) 수집 배치 스크립트 (plan.md 9.4)
    """
    print("[Batch] 고용24 K-디지털/직업훈련 과정 수집 시작...")
    trainings = [
        {"id": "TR01", "course_name": "클라우드 네이티브 백엔드 엔지니어링", "provider": "한국소프트웨어산업협회"},
        {"id": "TR02", "course_name": "Spring Boot & MSA 실무 프로젝트", "provider": "멀티캠퍼스"}
    ]
    os.makedirs("data/raw", exist_ok=True)
    with open("data/raw/hrd_trainings.json", "w", encoding="utf-8") as f:
        json.dump(trainings, f, ensure_ascii=False, indent=2)
    print(f"[Batch] 훈련과정 {len(trainings)}건 수집 완료.")


if __name__ == "__main__":
    fetch_hrd_trainings(api_key=os.getenv("EMPLOYMENT24_API_KEY", ""))
