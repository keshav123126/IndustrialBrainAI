from ai.llm.gemini_client import gemini

from ai.prompts.system_prompt import SYSTEM_PROMPT
from ai.prompts.safety_prompt import SAFETY_PROMPT


class SafetyAgent:

    def answer(
        self,
        question,
        context
    ):

        prompt = f"""
{SYSTEM_PROMPT}

{SAFETY_PROMPT}

Context:

{context}

Question:

{question}
"""

        return gemini.generate(prompt)


safety_agent = SafetyAgent()