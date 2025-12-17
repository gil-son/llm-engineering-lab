# 🌐 OpenAI Translation Example with LangChain

This project demonstrates how to access the OpenAI API using an API key and LangChain. It sets up a simple translation pipeline that uses prompt templates and the LangChain framework to call an OpenAI language model.

---

## 🚀 Features

- Uses `langchain` with `openai` integration  
- Loads API key from a `.env` file or via user prompt  
- Demonstrates message templating and chaining using LangChain  
- Basic translation example from any language to English (or another target idiom)

---

## 🧩 Requirements

Make sure you have Python 3.8 or higher installed.

### Install dependencies

```bash
pip install -qU "langchain[openai]" python-dotenv
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

## 🧠 How It Works

- Loads API key securely via `dotenv`
- Builds a prompt using `ChatPromptTemplate`
- Sends a chat message chain to OpenAI's model (e.g., GPT-4.1-nano)
- Parses and prints the result

---

## 📄 Example Output

Input:
```
Text: I love pizza!
Target Idiom: French
```

Output:
```
J'adore la pizza !
```

---

## 🛠️ Notes

- This example uses `gpt-4.1-nano`. You can change the model to suit your needs.
- Caching is disabled for easier testing and debugging.
