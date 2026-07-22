class ConfidenceEngine:

    def calculate(
        self,
        distances
    ):

        if not distances:

            return 0

        avg = sum(distances) / len(distances)

        score = 100 / (
            1 + avg
        )

        return round(
            min(
                100,
                max(
                    0,
                    score
                )
            ),
            2
        )


confidence_engine = ConfidenceEngine()