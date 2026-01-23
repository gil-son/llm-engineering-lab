from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])

chat_model = ChatOpenAI(model="gpt-5-nano", temperature=0.9)

chain = prompt | chat_model

session_store: dict[str, InMemoryChatMessageHistory] = {}

def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]

conversational_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

config = {"configurable": {"session_id": "demo-session"}}

# Interactions
response1 = conversational_chain.invoke({"input": "Hello, my name is Wesley. how are you?"}, config=config)
print("Assistant: ", response1.content)
print("-"*30)

response2 = conversational_chain.invoke({"input": "Can you repeat my name?"}, config=config)
print("Assistant: ", response2.content)
print("-"*30)

response3 = conversational_chain.invoke({"input": "Can you repeat my name in a motivation phrase?"}, config=config)
print("Assistant: ", response3.content)
print("-"*30)