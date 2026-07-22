from ai.llm.gemini_client import gemini

from ai.prompts.system_prompt import SYSTEM_PROMPT
from ai.prompts.document_prompt import DOCUMENT_PROMPT


class DocumentAgent:

    def answer(
        self,
        question,
        context
    ):

        prompt = f"""
{SYSTEM_PROMPT}

{DOCUMENT_PROMPT}

Context:

{context}

Question:

{question}
"""

        return gemini.generate(prompt)


document_agent = DocumentAgent()