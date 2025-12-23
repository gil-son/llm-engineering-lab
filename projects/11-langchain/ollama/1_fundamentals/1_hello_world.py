from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()

model = ChatOllama(
        model="llama3.2",
        temperature=0.5,
    )

message = model.invoke("Hello World")

print(message.content)