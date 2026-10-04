import json
from typing import List, Dict, Any


def extract_skill_entities(text: str) -> List[str]:
    """
    채용공고 비정형 텍스트로부터 스킬 엔티티 추출 규칙/모델 (plan.md 15.1)
    """
    known_skills = [
        "Java", "Spring", "Spring Boot", "Python", "Django", "FastAPI",
        "SQL", "MySQL", "PostgreSQL", "Redis", "AWS", "Docker",
        "Kubernetes", "Git", "React", "TypeScript", "Next.js"
    ]
    found = [skill for skill in known_skills if skill.lower() in text.lower()]
    return list(set(found))


if __name__ == "__main__":
    sample_text = "Java 기반 Spring Boot 백엔드 개발 및 AWS 클라우드 배포 경험자 우대. Docker 및 SQL 능숙자."
    print("추출된 기술 스택:", extract_skill_entities(sample_text))
