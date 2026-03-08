import streamlit as st
import os
from src.langgraphagenticai.UI.streamlitui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls ={}


    def load_streamlit_ui(self):
        st.set_page_config(page_title = self.config.get_page_title(),layout="wide")
        st.header(self.config.get_page_title())

        with st.sidebar:
            # Get Options from Config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            self.user_controls["selected_llm"] = st.selectbox("Select LLM",llm_options)
            
            if self.user_controls["selected_llm"] == "Groq":
                #Model Selections
                model_options = self.config.get_groq_model_options()
                self.user_controls['selected_groq_model'] = st.selectbox("select Model", model_options)

                self.user_controls["GROQ_API_KEY"] = st.text_input(
                                                "API Key",
                                                type="password",
                                                key="GROQ_API_KEY"
                                                                )

                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please Enter your Groq API Key to Continue Further -- Please Refer Groq Website to learn more about creating API Key")

            ## Usecase Selection

            self.user_controls['selected_usecase'] = st.selectbox("Select Usecase",usecase_options)

            return self.user_controls
        