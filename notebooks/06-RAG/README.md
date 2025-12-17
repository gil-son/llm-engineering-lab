# RAG From Scratch

Large Language Models (LLMs) are trained on a large but fixed corpus of data, which limits their ability to reason about **private or recent information**. Fine-tuning is one approach to mitigate this, but it is often [not well-suited for factual recall](https://www.anyscale.com/blog/fine-tuning-is-for-form-not-facts) and [can be costly](https://www.glean.com/blog/how-to-build-an-ai-assistant-for-the-enterprise).

**Retrieval-Augmented Generation (RAG)** is a powerful mechanism to expand an LLM's knowledge base. It uses **documents retrieved from external sources** to ground the LLM’s generation via **in-context learning**.

These notebooks accompany a [video playlist](https://youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x&feature=shared) that guides you through RAG from scratch, starting with indexing, retrieval, and generation.  

![RAG Overview](https://github.com/langchain-ai/rag-from-scratch/assets/122662504/54a2d76c-b07e-49e7-b4ce-fc45667360a1)

[Watch the video playlist](https://www.youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x)


✅ But in **llm-engineering-lab** repository, I created more steps to analisys and study it

---

## Environment Setup

1. Create the Conda environment:

```bash
conda env create -f environment.yml
```

2. Activate the environment:

```bash
conda activate rags
```

3. Launch Jupyter Lab from the `03-RAG/` folder:

```bash
jupyter lab
```

4. Open on your hots on  port 8888

```
http://localhost:8888/

```

5. Deactivate when done:

```bash
conda deactivate
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