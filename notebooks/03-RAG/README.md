# RAG From Scratch

Large Language Models (LLMs) are trained on a large but fixed corpus of data, which limits their ability to reason about **private or recent information**. Fine-tuning is one approach to mitigate this, but it is often [not well-suited for factual recall](https://www.anyscale.com/blog/fine-tuning-is-for-form-not-facts) and [can be costly](https://www.glean.com/blog/how-to-build-an-ai-assistant-for-the-enterprise).

**Retrieval-Augmented Generation (RAG)** is a powerful mechanism to expand an LLM's knowledge base. It uses **documents retrieved from external sources** to ground the LLM’s generation via **in-context learning**.

These notebooks accompany a [video playlist](https://youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x&feature=shared) that guides you through RAG from scratch, starting with indexing, retrieval, and generation.  

![RAG Overview](https://github.com/langchain-ai/rag-from-scratch/assets/122662504/54a2d76c-b07e-49e7-b4ce-fc45667360a1)

[Watch the video playlist](https://www.youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x)

---

## Environment Setup

Create the Conda environment:

```bash
conda env create -f environment.yml
```

Activate the environment:

```bash
conda activate rags
```

Deactivate when done:

```bash
conda deactivate
```

Launch Jupyter Lab from the `rag_from_scratch_*` folder:

```bash
jupyter lab
```

---

## LLM Options

This notebook supports two LLM options for embeddings and generation:

1. **Ollama Llama3.2**  
   Run locally:

   ```bash
   ollama run llama3.2
   ```

2. **OpenAI ChatGPT (gpt-3.5-turbo)**  
   Requires your **OPENAI_API_KEY** set as an environment variable:

   ```bash
   export OPENAI_API_KEY="sk-..."
   ```

---

## Notebook Overview

The notebooks walk through:

1. **Indexing** – loading documents and splitting into chunks.  
2. **Embeddings** – converting text to high-dimensional vectors.  
3. **Retrieval** – searching for relevant documents using similarity.  
4. **Generation** – combining retrieval with LLMs to answer questions.  

You will also find sections on **cosine similarity**, **2D/3D PCA visualization**, and **illustrative examples** with both real and fake embeddings.