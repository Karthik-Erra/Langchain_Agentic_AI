from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode



class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using Langgraph, This method initializes a chatbot node using the 
        'BasicchatbotNode' class and interrates it into the graph. The chatbot node is set as both the entry and exit
        poit of the graph
        """
        self.basic_chat_bot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node('chatbot',self.basic_chat_bot_node.process)
        self.graph_builder.add_edge(START,'chatbot')
        self.graph_builder.add_edge('chatbot',END)

        return self.graph_builder.compile()

    def setup_graph(self, usecase: str):

        if usecase == "Basic Chatbot":
            return self.basic_chatbot_build_graph()

        else:
            raise ValueError(f"Unsupported usecase: {usecase}")

