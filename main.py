from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 
model = OllamaLLM(model="llama3.1")
template = """
Answer the question below.
Here is the conversation history:
{context}

Question:
{question}

Answer:
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to the AI chatbot")
    print("You can type 'exit' to quit")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Exiting chat. Goodbye!")
            break

        result = chain.invoke({"context": context, "question": user_input})
        print(f"The bot said: {result}")
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()