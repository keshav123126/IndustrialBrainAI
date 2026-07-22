from rag.embedder import embedder
from rag.vector_store import vector_store


class Retriever:

    def search(
        self,
        question,
        document_id,
        k=5
    ):

        embedding = embedder.generate(
            [question]
        )[0]

        return vector_store.search(
            embedding,
            document_id,
            k
        )


retriever = Retriever()