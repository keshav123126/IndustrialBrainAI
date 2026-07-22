from ai.llm.gemini_client import gemini

from ai.prompts.system_prompt import SYSTEM_PROMPT

from ai.prompts.maintenance_prompt import MAINTENANCE_PROMPT


class MaintenanceAgent:

    def answer(
        self,
        question,
        context
    ):

        prompt = f"""
{SYSTEM_PROMPT}

{MAINTENANCE_PROMPT}

Context:

{context}

Question:

{question}
"""

        return gemini.generate(prompt)


maintenance_agent = MaintenanceAgent()