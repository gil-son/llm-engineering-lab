from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["name"],
    template="Hi, I'm {name}! Tell me a history with my name!"
)

text = template.format(name="Jesus")
print(text)