from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv() # Load OPENAI_API_KEY from .env file

model = init_chat_model(
        model="gpt-4.1-nano",
        model_provider="openai",
        temperature=0.5,
    )

answer = model.invoke("Hello World")

print(answer.content)