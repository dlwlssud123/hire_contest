from typing import List


class EmbeddingService:
    def __init__(self):
        self.model = "text-embedding-3-small"

    async def get_embedding(self, text: str) -> List[float]:
        # Return mock embedding vector for setup
        return [0.0] * 1536


embedding_service = EmbeddingService()
