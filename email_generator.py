from llm_helper import llm

response=llm.invoke("What is the capital of India?")
print(response.content)