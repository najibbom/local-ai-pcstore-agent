# Import the Ollama LLM wrapper, prompt template, and the retriever from vector.py
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever


# Initialize the local LLM (change model name to use other Ollama models)
model = OllamaLLM(model='deepseek-r1:8b')


# Prompt template for the LLM, including reviews and the user's question
template = """
You are an expert in answering questions about a PC components store

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""


# Create a prompt object from the template
prompt = ChatPromptTemplate.from_template(template)


# Chain the prompt and model together for invocation
chain = prompt | model


# Main interactive loop for user Q&A
while True:
    print("\n\n==================================================")
    # Get user question
    question = input("Please enter your question (q to quit): ")
    print("\n\n")
    if question.lower() == 'q':
        break
    # Retrieve relevant reviews using vector search
    reviews = retriever.invoke(question)
    # Pass reviews and question to the LLM chain
    result = chain.invoke({"reviews": reviews, "question": question})
    # Print the model's answer
    print(result)
