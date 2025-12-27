from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# 1. Define the prompt template with multiple messages
system = ("system", "you are an assistant that answers questions in a {style} style")
user = ("user", "{question}")

# 2. Create the chat prompt template
chat_prompt = ChatPromptTemplate([system, user])

# 3. Format the prompt with variables
messages = chat_prompt.format_messages(style="funny", question="Who is Alan Turing?")

# 4. Output formatted messages
for msg in messages:
    print(f"{msg.type}: {msg.content}")

# 5. Initialize the model
model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.5)

# 6. Invoke the model
result = model.invoke(messages)

# 7. Output
print(result.content)