from ai.agents.supervisor import supervisor_agent
from ai.agents.maintenance_agent import maintenance_agent
from ai.agents.safety_agent import safety_agent
from ai.agents.document_agent import document_agent


class AgentManager:

    def answer(
        self,
        question,
        context
    ):

        route = supervisor_agent.route(question)

        answers = []

        for agent in route["agents"]:

            if agent == "maintenance":
                answers.append(
                    maintenance_agent.answer(
                        question,
                        context
                    )
                )

            elif agent == "safety":
                answers.append(
                    safety_agent.answer(
                        question,
                        context
                    )
                )

            elif agent == "document":
                answers.append(
                    document_agent.answer(
                        question,
                        context
                    )
                )

        from ai.reasoning.answer_fusion import answer_fusion

        return answer_fusion.merge(answers)


agent_manager = AgentManager()