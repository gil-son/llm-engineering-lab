from thecode import chain
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(
    title="LangChain Server - Translate text to any language",
    description="A simple api server using Langchain's Runnable interfaces",
)

add_routes(
    app,
    chain,
    path="/translator",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)