import streamlit as st
from src.langgraphagenticai.UI.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.UI.streamlitui.display_result import DisplayResultStreamlit
import traceback

def load_langgraph_agenticai_app():

    """
    Loads and runs the langgraph ahenticai application with streamlit UI. This function initializes the UI,
    handles user input, configures the LLM model, sets up the graph based on the selected use case, and displays the output while
    implementing tbe exception handling for robustness.

    """

    ## Load UI
    ui = LoadStreamlitUI()

    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI Loader")
        return
    
    user_message = st.chat_input("Enter your message")

    if user_message:
        try:
            ## Configure the LLM
            obj_llm_config = GroqLLM(user_control_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model is not initialized")
                return 
            
            ## Initialize and set up the graph based on use case

            usecase = user_input.get('selected_usecase')

            if not usecase:
                st.error("Error: Usecase is not defined")
                return
            
            ## Graph Builder
            graph_builder = GraphBuilder(model)
            try:
                compiled_graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,compiled_graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Graph setup failed — {str(e)}")
                st.text(traceback.format_exc())
                return


        except Exception as e:
            raise ValueError(f"Error Occured with Exception : {e}")



