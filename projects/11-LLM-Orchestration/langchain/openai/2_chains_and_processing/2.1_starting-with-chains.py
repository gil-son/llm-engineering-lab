from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

prompt = ChatPromptTemplate.from_template(
    "Hi, I'm {name}! Tell me a joke with my name!"
)

# 2. Initialize the model
model = ChatOpenAI(
    model="gpt-4.1-nano",
    temperature=0.5
)

# 3. Create the chain
chain = prompt | model

# 4. Invoke the chain with variables
result = chain.invoke({"name": "Goku"})

# 5. Output
print(result.content)