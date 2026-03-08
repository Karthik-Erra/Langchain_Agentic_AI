from src.langgraphagenticai.state.state import State

class BasicChatbotNode:

    def __init__(self, llm):
        self.llm = llm

    def process(self, state):

        messages = state["messages"]

        response = self.llm.invoke(messages)

        return {
            "messages": [response]
        }