from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode
from dotenv import load_dotenv
import os


load_dotenv()

## print("Tavily key:", os.getenv("TAVILY_API_KEY"))

def get_tools():
    """
    Returns the list of tools to be used in the chatbot
    """

    tools = [TavilySearch(max_results=2)]
    return tools

def create_tool_node(tools):
    """
    Create and return a tool node for the graph"""

    return ToolNode(tools=tools)