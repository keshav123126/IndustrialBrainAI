import json

from ai.llm.gemini_client import gemini

from ai.prompts.router_prompt import ROUTER_PROMPT


class SupervisorAgent:

    def route(self, question):

        prompt = f"""
{ROUTER_PROMPT}

Question:

{question}
"""

        response = gemini.generate(prompt)

        try:
            return json.loads(response)
        except:
            return {
                "agents": ["document"]
            }


supervisor_agent = SupervisorAgent()