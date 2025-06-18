from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

class LLM:
    def __init__(self):
        API_KEY=os.getenv('GROQ_API_KEY')
        self.llm = ChatGroq(
            model = "llama3-70b-8192",
            api_key=API_KEY,
            temperature=0.6,
        )

    def get_llm(self):
        return self.llm

