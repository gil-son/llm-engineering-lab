from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv() # Load OPENAI_API_KEY from .env file

model = ChatOpenAI(
        model="gpt-4.1-nano",
        temperature=0,
    )

message = model.invoke("Hello World")

print(message.content)