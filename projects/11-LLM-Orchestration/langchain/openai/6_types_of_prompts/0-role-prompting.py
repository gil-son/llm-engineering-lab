
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from utils import print_llm_result
from dotenv import load_dotenv
load_dotenv()

system = ("system", 
"""You are a university professor of computer science who is very technical and explain 
concepts with formal definitions and pseudocode.""")

system2 = ("system", """You are a high school student that is starting learning coding. 
You are not very technical and you prefer to explain concepts with simple words and examples.""")

user = ("user", "Explain recursion in 50 words.")

chat_prompt = ChatPromptTemplate([system, user])
chat_prompt2 = ChatPromptTemplate([system2, user])
messages = chat_prompt.format_messages()

model = ChatOpenAI(model="gpt-4o")
result = model.invoke(messages)
print_llm_result(str(system), result)

result2 = model.invoke(chat_prompt2.format_messages())
print_llm_result(str(system2), result2)