# LLM Orchestration – LangChain

<div align="center">
  <table>
    <tr>
      <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/7527/7527144.png" width="80"/></td>
      <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/4380/4380939.png" width="80"/></td>
      <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/6231/6231228.png" width="80"/></td>
      <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/4380/4380939.png" width="80"/></td>
      <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/9431/9431523.png" width="80"/></td>
    </tr>
  </table>
</div>

LangChain is a framework for **LLM orchestration**, allowing you to compose prompts, models, chains, tools, and agents into reliable and reusable AI-powered applications.

---

## Instructions

You have **two ways** to practice this project:

### 1. OpenAI (Cloud-based)
- Requires an API key from your personal OpenAI account.
- Add the key to the `.env-example` file and rename it to `.env`.

### 2. Ollama (Local & Free)
- Runs LLMs locally on your machine.
- No API key is required.
- Recommended for learning and experimentation.

More details:
👉 https://github.com/gil-son/language-ai-engineering-lab/blob/main/projects/11-LLM-Orchestration/langchain/ollama/README.md

---

## Requirements

- Python **3.11** (recommended)
- Anaconda installed locally
- One of the following:
  - `OPENAI_API_KEY`
  - Ollama installed with a model (e.g. `llama3.2`)

---

## LangChain Learning Path

### Fundamentals
- Initialize a Chat Model
- Prompt Templates

---

### Chains and Processing

#### Starting with Chains
Chains allow you to connect prompts, models, and outputs into a single execution flow.

#### Chains with Decorators
Decorators help simplify chain definitions and improve readability.

#### RunnableLambda
`RunnableLambda` lets you inject custom Python logic into a LangChain pipeline.

#### Processing Pipelines
Pipelines combine multiple runnables into structured workflows.

---

### Summarization

LLMs are **stateless**. As conversations or documents grow, they may exceed the model’s **context window**, causing earlier information to be lost.

For this reason, **summarization is crucial**.

#### Why Summarization?
- Reduces token usage and cost
- Preserves essential information
- Enables long-document processing

#### Chunking

Large texts are split into smaller pieces (chunks):

**Original text**
```
I was at the supermarket and a salesman offered chocolate. But I don't like pure chocolate.
```

**Chunks**
```
Chunk 1: I was at the supermarket and a salesman offered chocolate. But I don't
Chunk 2: like pure chocolate.
```

If we process only Chunk 2, important context is lost.

#### Chunk Overlap

Chunk overlap helps recover context by reusing part of the previous chunk.

Example (overlap = 10 characters):
```
Previous overlap + Chunk 2 → I don't like pure chocolate.
```

---

### Summarization Strategies

#### STUFF
- Combines all chunks and summarizes them at once.

**Pros**
- Simple
- Fast

**Cons**
- Limited by context window

#### MAP-REDUCE
- Summarizes each chunk individually (Map)
- Combines summaries into a final summary (Reduce)

**Pros**
- Scales to large documents

**Cons**
- More complex
- Slightly higher cost

---

### Pipeline Summarization
You can build a **custom summarization pipeline** using chains and runnables tailored to your data and constraints.

---

## AI Agents

Key concepts:
- LLM is the core reasoning engine
- Agents can decide **what to do next**
- Agents require **tools and resources**

### Tools & Resources
- MCP (Model Context Protocol) provides structured access to external tools and data.

---

### ReAct Pattern

ReAct = **Reason + Act**

The agent iterates until it finds a solution.

Example:

```
--- Cycle 1 ---
Thought: I need more information
Action: Search documentation
Observation: Relevant API found

--- Cycle 2 ---
Thought: I can now call the API
Action: Execute API request
Observation: Response received

--- Cycle 3 ---
Thought: I have enough data
Action: Generate final answer
Observation: Task completed
```