# LLM Orchestration

## Requirements

- Python 11 or 13 installed locally
- Anaconda installed locally
- OpenAI_KEY or Ollam3.2 installed locally

## Environment Setup

1. Go to `notebooks/04-LLM-Orchestration/` folder:

```
cd notebooks/04-LLM-Orchestration/
```

2. Create the Conda environment:

```bash
conda env create -f environment.yml
```

3. Activate the environment:

```bash
conda activate llm-orchestration
```

4. Launch Jupyter Lab from the `notebooks/04-LLM-Orchestration/` folder:

```bash
jupyter lab
```

5. Open on your hots on  port 8888

```
http://localhost:8888/

```
6. Deactivate when done:

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