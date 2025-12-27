from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv() # Load OPENAI_API_KEY from .env file

# 1. Initialize the model
model = init_chat_model(
        model="gpt-4.1-nano",
        model_provider="openai",
        temperature=0.5,
    )

# 2. Invoke the model
answer = model.invoke("Hello World")

# 3. Output
print(answer.content)