from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

API_KEY=os.getenv('GROQ_API_KEY')
llm = ChatGroq(
    model = "llama3-70b-8192",
    api_key=API_KEY,
    temperature=0.6,
)

response= llm.invoke("What is the most populated country in the world?")
print(response.content)