# 🌐 OpenAI Translation API with LangChain & FastAPI

This project demonstrates how to access the OpenAI API using LangChain and FastAPI. It sets up a simple translation pipeline that uses prompt templates, chains, and LangServe to expose the functionality as a RESTful API.

---

## 🚀 Features

- Uses `langchain` with OpenAI integration  
- FastAPI server to expose a translation API  
- Demonstrates LangChain's Runnable interface  
- API endpoint to translate text into any target language  
- Secure API key loading via `.env` or prompt

---

## 🧩 Requirements

Make sure you have Python 3.12 or higher installed.

### Install dependencies

```bash
pip install -qU "langchain[openai]" langserve fastapi uvicorn python-dotenv
```

Alternatively, use:

```bash
pip install -r requirements.txt
```

---

## 🔐 Setup

1. Create a `.env` file in the project root.
2. Add your OpenAI API key:

```env
OPENAI_API_KEY="your-api-key-here"
```

If the key is not found in the environment, the script will prompt you to enter it manually.

---

## 🚦 Running the API Server

Make sure you have a valid `chain` defined in `thecode.py`.

Then start the server:

```bash
python thelangserve.py
```

The API will be available at:

```
http://localhost:8000/translator
```

You can explore:

- LangServe Playground UI: [http://localhost:8000/translator/playground](http://localhost:8000/translator/playground)

📡 Running the Client
After starting the API server, you can run the client to invoke the translation chain remotely:

```
python client.py
```

## 🧠 How It Works

1. Environment Setup
  - Loads your OpenAI API key securely from a .env file using python-dotenv.
  - If the key is not found, prompts the user to input it manually.

2. LangChain Pipeline
  - Uses LangChain components:
  - ChatPromptTemplate to create dynamic prompts.
  - ChatOpenAI to interact with OpenAI's chat models (e.g., GPT-4.1-nano).
  - StrOutputParser to convert model output into a plain string.

3. API Server

  - A FastAPI app (thelangserve.py) wraps the LangChain pipeline.
  - LangServe's add_routes() exposes the translation chain at /translator.
  - The server runs on localhost:8000 and includes interactive docs and a playground:
    - LangServe Playground: http://localhost:8000/translator/playground

4. Remote Client
  - A separate script (client.py) uses RemoteRunnable from langserve to connect to the running FastAPI server.
  - Sends input data remotely and prints the translated result locally.

## 🛠️ Notes

- The example uses `gpt-4.1-nano` — you can change it as needed.
- Caching is disabled for development simplicity.
