from langserve import RemoteRunnable

remote_chain = RemoteRunnable("http://localhost:8000/translator")

text = remote_chain.invoke({"idiom": "Franch", "text": "I love pizza!"})

print(text)