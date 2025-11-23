# Introduction to the LLM Engineering Lab

<p align="center">
  <img src="https://gitlab.com/gil-son/useful-images-collection/-/raw/main/png/devs.png?ref_type=heads" width="40%">
</p>

Welcome to the **LLM Engineering Lab** – a structured repository designed to help you learn, explore, and experiment with Large Language Models (LLMs). This lab aims to guide you through the foundational concepts, practical applications, and orchestration of robust solutions using techniques like RAG, agents, and MLOps.

## <img src="https://cdn-icons-png.flaticon.com/512/6062/6062161.png" width="80"/> Learning Objectives

## By the End of This Lab, You Will Be Able To:

- **Understand** the core concepts and key terminology related to LLMs, and **build one from scratch**.  
- **Evaluate** different model architectures and fine-tuning techniques.  
- **Comprehend** the principles of **NLP**, **NLU**, and **NLG**, and how they relate to LLMs.  
- **Implement** Retrieval-Augmented Generation (**RAG**) pipelines using vector databases such as **FAISS** and **Weaviate**.  
- **Understand** how **MCP servers** work and how they integrate into LLM systems.  
- **Orchestrate** complex workflows using **LangChain**, **LangGraph**, **Semantic Kernel**, and other frameworks.  
- **Build** autonomous systems with **tool-using LLM agents**.  
- **Monitor**, **trace**, and **evaluate** model performance using **MLflow**, **LangSmith**, and **LangFuse**.  
- **Apply** all these concepts in hands-on projects and domain-specific scenarios such as **IVR systems**.  

<p align="center">
  <img src="https://gitlab.com/gil-son/useful-images-collection/-/raw/main/png/llm-lab.png?ref_type=heads">
</p>


## <img src="https://cdn-icons-png.flaticon.com/512/18310/18310876.png" width="80"/>  Repository Structure

The repository is organized into numbered folders to reflect a progressive learning path:

- **01-Concepts-and-Setup**: Core concepts and environment configuration.
- **02-NLP-NLU-NLG**: Foundations of natural language processing and understanding.
- **03-LLM-Fundamentals**: Architectures, fine-tuning, and evaluation of LLMs.
- **04-RAG-Pipeline**: Implementation of Retrieval-Augmented Generation techniques.
- **05-LLM-Orchestration**: Tools and frameworks to orchestrate LLM workflows.
- **06-Agentic-AI-Systems**: Building autonomous AI agents with tool usage.
- **07-Evaluation-and-Benchmarks**: Evaluation strategies, metrics, and observability.
- **08-MLOps-and-Tracking**: Applying MLOps practices to the LLM lifecycle.
- **09-AI-IVR-Specifics**: Applying LLMs to Interactive Voice Response (IVR) systems.
- **projects/**: Practical and applied hands-on projects.
- **notebooks/**: Jupyter notebooks for experiments and demonstrations.
- **scripts/**: Utility scripts and helper functions.

```

llm-engineering-lab/
│
├── README.md                                      # Introduction, objectives, repo overview, usage instructions
│
├── 01-LLM-Fundamentals/                           # Core LLM concepts, setup, and architectures
│   ├── 01-1-What-is-an-LLM.md                     # Intro: simple explanation of LLMs and their importance
│   ├── 01-2-Key-Terms.md                          # Glossary of essential terms (token, prompt, inference, etc.)
│   ├── 01-3-Environment-Setup.md                  # Setting up Python env, APIs, dependencies
│   ├── 01-4-LLM-Architectures.md                  # Transformer-based models like GPT, LLaMA
│   ├── 01-5-Pretraining-and-Objectives.md         # Pretraining tasks and objectives
│   ├── 01-6-Fine-tuning.md                        # Strategies for fine-tuning LLMs
│   ├── 01-7-Instruction-Tuning.md                 # Fine-tuning for following instructions
│   ├── 01-8-RLHF.md                               # Reinforcement learning with human feedback
│   └── 01-9-LLM-Evaluation.md                     # Metrics and best practices for evaluation
│
├── 02-NLP-NLU-NLG-Comprehension/
│   ├── 02-1_NLP_Processing_Language/              # Text preparation and transformation into machine-readable form
│   ├── 02-2_NLU_Understanding_Meaning/            # Extracting intent, entities, and semantic relationships
│   ├── 02-3_NLG_Generating_Text/                  # Producing coherent natural language output
│   └── 02-4_Evaluation_Refining_the_System/       # Measuring, optimizing, and improving model performance
│
├── 03-RAG-Pipeline/
│   ├── 03-1-Ingest-Documents/                     # Build the knowledge base: load, preprocessing, chunk, embed documents and vector
│   ├── 03-2-Retrieval/                            # Retrieve relevant context from the vector store
│   ├── 03-3-Generation/                           # Compose final answer combining LLM output with retrieved context
│   └── 03-4-Continuous-Improvement/               # Continuous improvement via evaluation and retraining
│
├── 04-LLM-Orchestration/                          # Orchestrating LLM workflows
│   ├── 04-1-Semantic-Kernel-Overview.md           # Microsoft’s Semantic Kernel
│   ├── 04-2-LangChain-Concepts.md                 # Chains, agents, retrievers, memory
│   ├── 04-3-LangGraph-Intro.md                    # Stateful workflows with LangGraph
│   ├── 04-4-LangSmith-Usage.md                    # Debugging, tracing, evaluation
│   ├── 04-5-LangFlow-UI-Builder.md                # Visual builder for LangChain workflows
│   └── 04-6-LangFuse-Observability.md             # Monitoring & analytics in production
│
├── 05-Agentic-AI-Systems/                         # Autonomous AI agents
│   ├── 05-1-Agentic-AI-Principles.md              # Fundamentals of AI agents
│   ├── 05-2-Tool-Integration-Examples.md          # Tool access: APIs, search, functions
│
├── 06-Evaluation-and-Benchmarks/                  # Testing and evaluating LLMs
│   ├── 06-1-Prompt-Evaluation.md                  # Assessing prompt quality
│   ├── 06-2-Metrics-and-Benchmarks.md             # Accuracy, BLEU, ROUGE, perplexity
│   ├── 06-3-Hallucination-Detection.md            # Detecting hallucinations
│   ├── 06-4-Latency-and-Cost.md                   # Runtime, token usage, cost tracking
│   └── 06-5-Tracing-with-LangSmith.md             # Traceability with LangSmith
│
├── 07-MLOps-and-Tracking/                         # Productionizing LLM workflows
│   ├── 07-1-MLflow-Basics.md                      # Logging and tracking experiments
│   ├── 07-2-Tracking-RAG-and-Prompts.md           # MLflow for prompt + retrieval stats
│   └── 07-3-Integration-with-LangChain.md         # MLflow integration with LangChain
│
├── 08-AI-IVR-Specifics/                           # LLMs in IVR systems
│   ├── 08-1-IVR-System-Overview.md                # Interactive Voice Response systems
│   ├── 08-2-Voice-to-Text-Text-to-Voice.md        # Speech-to-text and TTS integration
│   ├── 08-3-Dialogue-Management-in-IVR.md         # Managing conversations with LLMs
│   └── 08-4-Orchestration-Comparison.md           # LangChain vs Semantic Kernel in IVR
│
├── 09-LLM-Data-Engineering/                       # Dataset lifecycle for training
│   ├── 09-1-Dataset-Collection.md                 # Gathering high-quality training data
│   ├── 09-2-Data-Cleaning-and-Filtering.md        # Cleaning and filtering for consistency
│   └── 09-3-Dataset-Formatting.md                 # Formatting datasets for model training
│
├── 10-Prompt-Engineering/                         # Crafting effective prompts
│   ├── 10-1-Zero-Shot-One-Shot-Few-Shot.md        # Different prompting strategies
│   ├── 10-2-Chain-of-Thought.md                   # Step-by-step reasoning
│   └── 10-3-Prompt-Tuning-vs-Prefix-Tuning.md     # Lightweight tuning methods
│
├── projects/                                      # Hands-on projects
│   ├── 01-basic-rag/
│   ├── 02-weaviate-rag/
│   ├── 03-langchain-agent/
│   └── 04-semantic-kernel-bot/
│
├── notebooks/                              # Jupyter notebooks for experiments
│   ├── 01-LLM-Fundamentals/
│   │   ├── 01-mini-gpt-char.ipynb          # Minimal character-level GPT
│   │   ├── 02-genesis-transformer.ipynb    # More advanced Transformer LM
│   │   ├── README.md                       # Explains both steps
│   │   └── requirements.txt
│   ├── 02-NLP-NLU-NLG/                     # NLP (NLU and NLG) examples
│   ├── 03-RAG-Pipeline/                    # RAG examples
│   │   └──  rag_from_scratch_1_to_4
│   └── 04-LLM-Orchestration                # LLM Orchestration examples
│
└── scripts/                                # Utility scripts for loaders, embeddings, etc.
    ├── utils.py
    ├── loaders.py
    └── embeddings.py

```

<hr/>

<div align="center">
  <img src="https://i.ibb.co/kgNSnpv/git-support.png">
</div>
