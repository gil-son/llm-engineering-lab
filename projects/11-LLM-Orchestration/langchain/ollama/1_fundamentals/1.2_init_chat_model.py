from langchain.chat_models import init_chat_model

model = init_chat_model(
        model="llama3.2",
        model_provider="ollama",
        temperature=0.5,
    )

answer = model.invoke("Hello World")

print(answer.content)