from sentence_transformers import SentenceTransformer


class Embedder:

    def __init__(self):
        self.model = None

    def load_model(self):
        if self.model is None:
            self.model = SentenceTransformer(
                "BAAI/bge-small-en-v1.5",
                device="cpu"
            )

    def generate(self, chunks):
        self.load_model()

        return self.model.encode(
            chunks,
            convert_to_numpy=True
        )


embedder = Embedder()