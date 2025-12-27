from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv() # Load OPENAI_API_KEY from .env file

# 1. Initialize the model
model = ChatOpenAI(
        model="gpt-4.1-nano",
        temperature=0,
    )

# 2. Invoke the model
message = model.invoke("Hello World")

# 3. Output
print(message.content)