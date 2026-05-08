from abc import ABC, abstractmethod


class BaseVectorStore(ABC):

    @abstractmethod
    def add(self, embeddings, metadata):
        pass

    @abstractmethod
    def search(self, embedding, top_k=5):
        pass