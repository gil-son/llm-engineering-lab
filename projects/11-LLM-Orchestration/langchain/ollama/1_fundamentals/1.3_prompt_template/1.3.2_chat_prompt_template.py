from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

system = ("system", "you are an assistant that answers questions in a {style} style")
user = ("user", "{question}")

chat_prompt = ChatPromptTemplate([system, user])

messages = chat_prompt.format_messages(style="funny", question="Who is Alan Turing?")

for msg in messages:
    print(f"{msg.type}: {msg.content}")

model = ChatOllama(model="llama3.2", temperature=0.5)
result = model.invoke(messages)
print(result.content)