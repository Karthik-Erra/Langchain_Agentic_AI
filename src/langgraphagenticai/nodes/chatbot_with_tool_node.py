from src.langgraphagenticai.state.state import State
from langchain_core.messages import SystemMessage


class ChatbotWithToolNode:
    """
    Chatbot logic enhanced with tool integration.
    """

    def __init__(self, model):
        self.llm = model

    def create_chatbot(self, tools):
        """Returns a chatbot node function."""

        system_message = SystemMessage(
            content="You are an AI assistant. Use the tavily_search tool when the user asks about current events or real-time data."
        )

        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            """
            Chatbot logic for processing the input state and returning a response.
            """

            messages = [system_message] + state["messages"]

            response = llm_with_tools.invoke(messages)

            return {
                "messages": state["messages"] + [response]
            }

        return chatbot_node