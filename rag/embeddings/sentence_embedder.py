from sentence_transformers import SentenceTransformer

from rag.embeddings.base_embedder import BaseEmbedder


class SentenceEmbedder(BaseEmbedder):

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def embed(self, texts):

        return self.model.encode(
            texts,
            convert_to_tensor=False
        )