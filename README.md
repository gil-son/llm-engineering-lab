# 🤖 LangChain

**LangChain** is a framework for developing applications powered by large language models (LLMs). LangChain provides building blocks to connect LLMs with tools like APIs, vector stores, memory, and more, enabling complex, intelligent applications like chatbots, agents, and search systems.

---

## 📚 What is LangChain?

LangChain is a Python (and JavaScript) framework designed to:

- Connect LLMs to external data (e.g., documents, databases).
- Enable LLMs to perform reasoning and decision-making.
- Build chains of prompts and actions.
- Create autonomous agents with memory and tools.

It simplifies building apps like:

- Chatbots with memory and context
- RAG (Retrieval-Augmented Generation) systems
- Document Q&A systems
- LLM-powered agents and workflows

## 🧭 Architecture Overview

A typical LangChain-based generative AI application flow can be visualized as follows:

```plaintext
[User]
   │
   ▼
[User Question]
   │
   ▼
[Generative AI Application]
   ├── Retrieves Context from → [Data Source]
   ├── Uses Prompt Template → [Template with Question + Context]
   │
   ▼
Sends to
   ▼
[LLM API (e.g., OpenAI, Anthropic)]
   │
   ▼
[Response/Answer]
   │
   ▼
[Returned to User]
```
### Key Steps:
- User submits a query.
- Application fetches relevant data and builds a prompt.
- Prompt includes user input + context (e.g., from a document or DB).
- LLM API processes the prompt and returns a response.
- Response is delivered to the user.

### This architecture is commonly used in:

- 🔁 **Retrieval-Augmented Generation (RAG) systems**: Enhance LLMs with relevant external data to improve response accuracy.
- 📄 **Document Q&A bots**: Answer user questions based on the content of documents.
- 💬 **Context-aware chat assistants**: Maintain memory and context to hold more natural conversations.
- 🔍 **ReAct**: Use reasoning and action steps to solve tasks step-by-step.
- 🛠 **Tool Calling**: Allow LLMs to invoke external tools like APIs or calculators.
- 🔗 **LangGraph (graph-based workflows)**: Structure complex tasks using nodes and edges for better control flow.
- 🤖 **Multi-agent systems**: Coordinate multiple LLM agents to collaborate on problem-solving.

It’s also possible to combine multiple approaches depending on your use case. LangChain supports a variety of patterns—from simple prompt chains to complex agents that interact with APIs and tools.

### Other Frameworks for Building Generative Applications:
- Semantic Kernel (Microsoft)
   - Focused on C#
- Llama Index
   - Focused on RAG (Retrieval-Augmented Generation)
- LangChain
   - General-purpose framework

## ⚙️ Features

<details>
  <summary>🔗 <strong>Chains</strong> – Compose sequences of calls (prompt + LLM + tool).</summary>
  <br/>
  Chains are workflows that involve multiple steps with an LLM. For example, you might format a user input, pass it to an LLM, then use the result in another tool or API. LangChain simplifies this chaining process.
  
  Example:
  - Prompt → LLM → Output Parser
  - User Question → Search Tool → LLM → Final Answer

  ```python
  from langchain.llms import OpenAI
  from langchain.prompts import PromptTemplate
  from langchain.chains import LLMChain

  prompt = PromptTemplate.from_template("Translate the following into Spanish: {text}")
  llm = OpenAI(temperature=0)
  chain = LLMChain(llm=llm, prompt=prompt)

  result = chain.run("Hello, how are you?")
  print(result)
```
</details>

<details>
  <summary>🧠 <strong>Memory</strong> – Add long- or short-term memory to your agents.</summary>
  <br/>
  Memory allows the LLM to remember past interactions and use context across multiple calls. This is essential for chatbots or assistants that need to maintain a conversation or recall previous steps.

  Types include:
  - ConversationBufferMemory
    ```python
      from langchain.memory import ConversationBufferMemory
      from langchain.chains import ConversationChain
      from langchain.llms import OpenAI
      
      memory = ConversationBufferMemory()
      convo = ConversationChain(llm=OpenAI(), memory=memory)
      
      print(convo.run("My name is John."))
      print(convo.run("What is my name?"))    
    ```
    📦 Output:
    ```
    Hi John!
    You just told me that your name is John.
    ```
  - ConversationSummaryMemory
    ```python
      from langchain.memory import ConversationSummaryMemory
      from langchain.chains import ConversationChain
      from langchain.llms import OpenAI
      
      llm = OpenAI(temperature=0)
      memory = ConversationSummaryMemory(llm=llm)
      conversation = ConversationChain(llm=llm, memory=memory, verbose=True)
      
      conversation.run("Hi, I'm planning a vacation to Japan.")
      conversation.run("I like food, history, and nature. Any tips?")
      conversation.run("Can you summarize what we've discussed?")
    ```
  - VectorStoreRetrieverMemory
    ```python
      from langchain.memory import VectorStoreRetrieverMemory
      from langchain.vectorstores import FAISS
      from langchain.embeddings import OpenAIEmbeddings
      from langchain.chains import ConversationChain
      from langchain.llms import OpenAI
      
      # Setup vector store
      embedding = OpenAIEmbeddings()
      faiss_db = FAISS.from_texts([], embedding)
      
      retriever_memory = VectorStoreRetrieverMemory(retriever=faiss_db.as_retriever())
      conversation = ConversationChain(llm=OpenAI(), memory=retriever_memory, verbose=True)
      
      conversation.run("My favorite color is blue.")
      conversation.run("Do you remember my favorite color?")
    ```
</details>

<details>
  <summary>📄 <strong>Document Loaders</strong> – Easily load and process PDFs, websites, docs.</summary>
  <br/>
  LangChain provides utilities to ingest and preprocess external documents, making them searchable and ready for LLM use. Useful for building RAG (Retrieval-Augmented Generation) applications.

  Loaders include:
  - PDFLoader, UnstructuredFileLoader
  - WebBaseLoader
  - Notion, Google Drive, GitHub loaders
</details>

<details>
  <summary>🧩 <strong>Embeddings & Vector Stores</strong> – Plug in OpenAI, FAISS, Pinecone, etc.</summary>
  <br/>
  Embeddings convert text into vector representations. Vector stores allow efficient similarity search across embedded documents. LangChain supports many vector DBs for semantic search.

  Popular integrations:
  - FAISS, Pinecone, Chroma, Weaviate, Qdrant
  - Embedding models: OpenAI, Hugging Face, Cohere
</details>

<details>
  <summary>🧠 <strong>Agents</strong> – Let LLMs make decisions using tools like calculators, APIs.</summary>
  <br/>
  Agents use an LLM to decide which tools to use and when. They are goal-driven and autonomous, handling tasks like browsing the web, searching, or calling APIs.

  Common use cases:
  - Autonomous customer support agents
  - AI assistants with multiple tools
  - Reasoning over multiple documents
</details>

<details>
  <summary>🌐 <strong>Tool Integration</strong> – Connect to APIs, web search, SQL databases, etc.</summary>
  <br/>
  Tools are external functions that an agent or chain can call. LangChain allows easy integration with:
  
  - Web scraping tools
  - SQL databases (with LangChain SQL)
  - Python functions
  - REST APIs
  - Search engines (e.g., SerpAPI)
</details>

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install langchain openai
