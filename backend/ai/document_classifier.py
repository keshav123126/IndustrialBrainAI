from ai.llm.gemini_client import gemini


class DocumentClassifier:

    def classify(
        self,
        text: str
    ):

        prompt = f"""
Return ONLY JSON.

{{
"document_type":"",
"department":"",
"equipment":"",
"keywords":[]
}}

Document:

{text[:5000]}
"""

        return gemini.generate(prompt)


document_classifier = DocumentClassifier()