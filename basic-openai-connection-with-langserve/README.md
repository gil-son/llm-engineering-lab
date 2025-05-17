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
python main.py
```

The API will be available at:

```
http://localhost:8000/translator
```

You can explore:

- LangServe Playground UI: [http://localhost:8000/translator/playground](http://localhost:8000/translator/playground)

---

## 🧠 How It Works

- Loads API key securely using `dotenv`
- Uses LangChain's `ChatPromptTemplate`, `ChatOpenAI`, and `StrOutputParser`
- Exposes the chain using LangServe’s `add_routes()` function
- Implements a FastAPI server to serve the translation chain

---

## 📄 Example Output

### Request

**POST** `/translator/invoke`

```json
{
  "input": {
    "idiom": "French",
    "text": "I love pizza!"
  }
}
```

### Response

```json
{
  "output": "J'adore la pizza !"
}
```

---

## 🛠️ Notes

- The example uses `gpt-4.1-nano` — you can change it as needed.
- Caching is disabled for development simplicity.
