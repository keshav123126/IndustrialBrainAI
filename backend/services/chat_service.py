from rag.retriever import retriever

from ai.reasoning.context_builder import context_builder
from ai.reasoning.prompt_builder import prompt_builder
from ai.reasoning.answer_generator import answer_generator
from ai.reasoning.confidence_engine import confidence_engine


class ChatService:

    def ask(
        self,
        question,
        document_id
    ):

        results = retriever.search(
            question,
            document_id
        )

        context = context_builder.build(
            results
        )

        if len(context.strip()) == 0:

            return {

                "answer": (
                    "No relevant information was found in the selected document."
                ),

                "confidence": 0,

                "citations": []

            }

        prompt = prompt_builder.build(
            question,
            context
        )

        answer = answer_generator.generate(
            prompt
        )

        confidence = confidence_engine.calculate(
            results["distances"][0]
        )

        return {

            "answer": answer,

            "confidence": confidence,

            "citations": []

        }


chat_service = ChatService()