class ContextBuilder:

    def build(self, results):

        docs = results["documents"][0]

        context = []

        seen = set()

        for doc in docs:

            text = doc.strip()

            if text in seen:
                continue

            seen.add(text)

            context.append(text)

        return "\n\n".join(context)


context_builder = ContextBuilder()