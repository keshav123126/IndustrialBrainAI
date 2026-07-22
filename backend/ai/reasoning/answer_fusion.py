from ai.llm.gemini_client import gemini


class AnswerFusion:

    def merge(self, answers):

        prompt = f"""
Merge the following AI answers.

Remove duplicates.

Keep technical accuracy.

Return one professional answer.

Answers:

{answers}
"""

        return gemini.generate(prompt)


answer_fusion = AnswerFusion()