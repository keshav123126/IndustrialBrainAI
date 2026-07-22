class CitationEngine:

    def create(
        self,
        metadata
    ):

        citations = []

        for item in metadata:

            citations.append({

                "document": item["document"],

                "page": item["page"]

            })

        return citations


citation_engine = CitationEngine()