from typing import List, Dict, Any


class VectorStoreManager:
    """
    ChromaDB / pgvector 기반 벡터 스토어 관리자
    """
    def __init__(self):
        self.collection_name = "career_knowledge_base"

    async def add_documents(self, documents: List[Dict[str, Any]]):
        pass

    async def similarity_search(self, query: str, k: int = 5) -> List[Dict[str, Any]]:
        return []


vector_store_manager = VectorStoreManager()
