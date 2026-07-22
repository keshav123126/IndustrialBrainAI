from sentence_transformers import SentenceTransformer


class Embedder:

    def __init__(self):

        SentenceTransformer(
    "BAAI/bge-small-en-v1.5",
    device="cpu"
)

    def generate(self, chunks):

        return self.model.encode(
            chunks,
            convert_to_numpy=True
        )


embedder = Embedder()