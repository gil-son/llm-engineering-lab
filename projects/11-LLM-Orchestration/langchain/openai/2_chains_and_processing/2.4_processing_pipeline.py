from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

template_translate = ChatPromptTemplate.from_template(
    template="Translate the following text to English:\n ```{initial_text}````"
)

template_summary = ChatPromptTemplate.from_template(
    template="Summarize the following text in 4 words:\n ```{text}```"
)

llm_en = ChatOpenAI(model="gpt-4.1-nano", temperature=0)

translate = template_translate | llm_en | StrOutputParser()
pipeline = {"text": translate} | template_summary | llm_en | StrOutputParser()

result = pipeline.invoke({"initial_text": "LangChain é um framework para desenvolvimento de aplicações de IA"})
print(result)