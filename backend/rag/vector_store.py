import chromadb


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

    def add(
        self,
        ids,
        documents,
        embeddings,
        metadatas
    ):

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings.tolist(),
            metadatas=metadatas
        )

    def search(
        self,
        embedding,
        document_id,
        k=5
    ):

        return self.collection.query(
            query_embeddings=[
                embedding.tolist()
            ],
            n_results=k,
            where={
                "document_id": str(document_id)
            }
        )


vector_store = VectorStore()