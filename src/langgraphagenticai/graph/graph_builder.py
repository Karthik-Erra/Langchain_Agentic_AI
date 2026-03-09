from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.tools.search_tool import get_tools, create_tool_node
from langgraph.prebuilt import tools_condition
from src.langgraphagenticai.nodes.chatbot_with_tool_node import ChatbotWithToolNode


class GraphBuilder:

    def __init__(self, model):
        self.llm = model

    def basic_chatbot_build_graph(self):

        graph_builder = StateGraph(State)

        basic_chat_bot_node = BasicChatbotNode(self.llm)

        graph_builder.add_node("chatbot", basic_chat_bot_node.process)

        graph_builder.add_edge(START, "chatbot")
        graph_builder.add_edge("chatbot", END)

        return graph_builder.compile()

    def chatbot_with_tools_build_graph(self):

        graph_builder = StateGraph(State)

        # Tools
        tools = get_tools()
        tool_node = create_tool_node(tools)

        # Chatbot
        obj_chatbot_with_tool_node = ChatbotWithToolNode(self.llm)
        chatbot_node = obj_chatbot_with_tool_node.create_chatbot(tools)

        # Nodes
        graph_builder.add_node("chatbot", chatbot_node)
        graph_builder.add_node("tools", tool_node)

        # Edges
        graph_builder.add_edge(START, "chatbot")

        graph_builder.add_conditional_edges(
            "chatbot",
            tools_condition,
            {
                "tools": "tools",
                "__end__": END
            }
        )

        graph_builder.add_edge("tools", "chatbot")

        return graph_builder.compile()

    def setup_graph(self, usecase: str):

        if usecase == "Basic Chatbot":
            return self.basic_chatbot_build_graph()

        elif usecase == "Chatbot with Web":
            return self.chatbot_with_tools_build_graph()

        else:
            raise ValueError(f"Unsupported usecase: {usecase}")