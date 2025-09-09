from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriver
model= OllamaLLM(model="llama3.2")
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