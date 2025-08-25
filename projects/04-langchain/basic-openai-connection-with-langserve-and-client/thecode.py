from dotenv import load_dotenv
import os
import langchain
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Disable LangChain cache
langchain.cache = None

# Load .env file
load_dotenv()

# Clear existing env var to ensure fresh logic (optional but useful for testing)
#os.environ.pop("OPENAI_API_KEY", None)

# Attempt to get API key
api_key = os.getenv("OPENAI_API_KEY")

# Prompt only if missing or blank
if not api_key or api_key.strip() == "":
    api_key = input("Enter API key for OpenAI: ").strip()
    os.environ["OPENAI_API_KEY"] = api_key
    print("API key was provided manually.")
else:
    print("API key was loaded from environment or .env file.")

# Debug output (shows first few characters only)
print("Using API key:", repr(os.environ.get("OPENAI_API_KEY")[:6]) + "...")

# Build message chain
messages = [
    SystemMessage("Translate the next text to english language"),
    HumanMessage("Se inscrevam no canal")
]

# Choose your model (change if needed)
the_model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.7)

parser = StrOutputParser()

chain = the_model | parser

"""
Runnables

Equivalent to the following sequential calls:
    1. output = the_model.invoke(messages)
    2. text = parser.invoke(output)
"""

message_template = ChatPromptTemplate.from_messages([
    ("system", "Translate the next text to {idiom}"),
    ("user", "{text}")
])

print(message_template.invoke({"idiom": "Franch", "text": "I love pizza!"}))

chain = message_template | the_model | parser
