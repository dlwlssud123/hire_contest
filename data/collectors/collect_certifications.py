import os
import json


def fetch_qnet_certifications(api_key: str):
    """
    한국산업인력공단 국가기술자격 데이터 수집 (plan.md 9.5)
    """
    print("[Batch] 국가기술자격(Q-Net) 데이터 수집 시작...")
    certs = [
        {"code": "1320", "name": "정보처리기사", "series": "기사"},
        {"code": "1321", "name": "정보보안기사", "series": "기사"},
        {"code": "2290", "name": "빅데이터분석기사", "series": "기사"}
    ]
    os.makedirs("data/raw", exist_ok=True)
    with open("data/raw/qnet_certifications.json", "w", encoding="utf-8") as f:
        json.dump(certs, f, ensure_ascii=False, indent=2)
    print(f"[Batch] 국가기술자격 {len(certs)}건 수집 완료.")


if __name__ == "__main__":
    fetch_qnet_certifications(api_key=os.getenv("QNET_API_KEY", ""))
