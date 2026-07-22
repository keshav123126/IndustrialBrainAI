from ai.llm.gemini_client import gemini


class AnswerGenerator:

    def generate(
        self,
        prompt
    ):

        return gemini.generate(prompt)


answer_generator = AnswerGenerator()