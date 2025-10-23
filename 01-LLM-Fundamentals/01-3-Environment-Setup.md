# 1. Fundamentals

<div align="center">
  <img src="https://static.vecteezy.com/system/resources/previews/042/890/624/non_2x/llm-artificial-intelligence-blue-gradient-concept-icon-content-generation-chatbot-round-shape-line-illustration-abstract-idea-graphic-design-easy-to-use-infographic-presentation-vector.jpg" width="20%">
</div>
<br/>

## 1.3. Environments Setup

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/7963/7963858.png" width="80"/> Introduction

---

Before diving into model architectures and fine-tuning, it’s crucial to configure a reliable environment for working with Large Language Models (LLMs).

This setup ensures:

Reproducibility — everyone can run the same code under the same conditions.

Dependency management — models, frameworks, and libraries evolve rapidly.

Hardware optimization — environments differ depending on CPU, GPU, or cloud usage.

In this section, you’ll learn how to create and manage your Python environments using both venv and conda, install essential libraries, and connect to APIs like OpenAI or Hugging Face.

---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/5557/5557844.png" width="80"/> Why use it?
  
Setting up environments properly prevents the infamous “it works on my machine” problem.

For LLM projects, this is especially important because:

You’ll often switch between different frameworks (LangChain, LlamaIndex, Transformers, etc.).

You may work on GPU-enabled setups locally or in the cloud.

Environment reproducibility is key for collaboration and deployment.

---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/2299/2299623.png" width="80"/> Components

| Component              | Description                                          | Example                         |
| ---------------------- | ---------------------------------------------------- | ------------------------------- |
| **Python Environment** | Isolated workspace with specific dependencies        | `venv` or `conda`               |
| **Requirements File**  | Lists all Python dependencies                        | `requirements.txt`              |
| **Environment YAML**   | Conda-based specification of libraries and versions  | `environment.yml`               |
| **API Keys**           | Credentials to connect to OpenAI, Hugging Face, etc. | `.env` or environment variables |
| **Version Control**    | Ensures team reproducibility                         | `git`, `.gitignore`             |

---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/7527/7527144.png" width="80"/> How it works?

Each project can have its own virtual environment.
When activated, Python uses its local libraries, isolated from global installations.

Step-by-step Process

1. Clone the repository:
```
git clone https://github.com/gil-son/llm-engineering-lab.git
cd llm-engineering-lab
```
2. Access the desired notebook or project:
```
cd notebooks/03-RAG
```

OR

```
cd projects/04-langchain
```

3. Choose your environment manager conform the project OR notebook:

- Option 1: Using venv
```
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```
- Option 2: Using conda
```
conda env create -f environment.yml
conda activate <project-name-inside-of-environment>
jupyter lab
```
4. Configure API keys

- Option 1:Create a .env file in your root directory:
```
OPENAI_API_KEY=your_openai_key
HUGGINGFACEHUB_API_TOKEN=your_hf_token
```

- Option 2: Install a local LLM runtime, such as Ollama:

Install Ollama:
```
curl -fsSL https://ollama.com/install.sh | sh
```

Run a local model (e.g., Llama 3):
```
ollama run llama3
```


#### Simple Diagram

```mermaid
graph TD
    A[Branch] --> B[Clone OR Fork Repository]
    B --> C[Access the Project OR Notebook]
    C --> D[Create Environment venv OR conda]
    D --> E[Install Dependencies]
    E --> F[Configure API Keys OR one Local LLM]
    F --> G[Run]
```


---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/6404/6404564.png" width="80"/> Use Cases

- Running local experiments with small or open models (e.g., GPT-2, Mistral-7B, Llama 3 via Ollama)
- Building reproducible demos with LangChain or LlamaIndex
- Hosting notebooks on VSCode, Jupyter, or Colab
- Preparing isolated development environments for RAG, fine-tuning, or evaluation pipelines

---

### <img src="https://cdn-icons-png.flaticon.com/512/6675/6675847.png" width="80"> Limitations

- Virtual environments do not include GPU drivers or CUDA setup — these must be installed separately.
- Environment activation commands vary by operating system (Windows, macOS, Linux).
- API keys must be stored securely — **never commit** .env files or secrets to version control.

---

### <img src="https://cdn-icons-png.flaticon.com/512/2147/2147809.png" width="80"> Code/Notebook/Projects

- [requirements.txt](https://github.com/gil-son/llm-engineering-lab/blob/main/projects/04-langchain/basic-openai-connection-with-langserve-and-client/requirements.txt): this is an example file with necessaries labaries to be installed via venv
- [environment.yml](https://github.com/gil-son/llm-engineering-lab/blob/main/notebooks/03-RAG/environment.yml): this is an example file with necessaries labaries to be installed via conda (anaconda)

---

### <img src="https://cdn-icons-png.flaticon.com/512/2112/2112889.png" width="80"> Videos

A few recommended resources to visualize how environments and reproducibility work:

Create and activate environment with **venv** and manage it:
<div align="center">
  <a href="https://www.youtube.com/watch?v=Y21OR1OPC9A" target="_blank">
      <img width="640" height="360" src="https://i.ytimg.com/vi/Y21OR1OPC9A/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLAfGONINxti98sD3YBv_1BVBEqsnA"/>
  </a>
</div>
<hr/>

Create environment with **conda** and manage it:
<div align="center">
  <a href="https://www.youtube.com/shorts/EvkK3VhCloQ" target="_blank">
      <img width="360" height="540" src="https://i.ytimg.com/vi/EvkK3VhCloQ/oar2.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&rs=AOn4CLDwlC7RbGEQvLUUrXmV8usaiXtjCg"/>
  </a>
</div>
