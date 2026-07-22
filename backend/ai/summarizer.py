from ai.llm.gemini_client import gemini


class Summarizer:

    def summarize(
        self,
        text: str
    ):

        prompt = f"""
Summarize this industrial document.

Include:

1. Purpose
2. Important Equipment
3. Safety Notes
4. Maintenance Notes

{text[:8000]}
"""

        return gemini.generate(prompt)


summarizer = Summarizer()