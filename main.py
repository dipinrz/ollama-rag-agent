from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from vector import retriver
import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyA8bLpkN-jw81TVXW3-n3spPx0nz-F0bB0"

# model= OllamaLLM(model="llama3.2")
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

template= """
you are an expert in answering questions about the pizza restaurant
here are some relevent reviews :{reviews}
based on the reviews, answer the question : {question}
"""

prompt= ChatPromptTemplate.from_template(template)
chain= prompt | model
while True:
    print("\n\n==================================================\n\n")
    question=input("Ask a question about the pizza restaurant: (q to quit)")
    print("\n\n==================================================\n\n")

    if question.lower()=="q":

        break
    reviews=retriver.invoke(question)

    results=chain.invoke({"reviews":reviews,"question":question})
    print(results)