# Introduction to the LLM Engineering Lab

<p align="center">
  <img src="https://github.com/gil-son/experimental/blob/main/matrizero/v002/src/assets/images/devs.png" width="40%">
</p>

Welcome to the **LLM Engineering Lab** – a structured repository designed to help you learn, explore, and experiment with Large Language Models (LLMs). This lab aims to guide you through the foundational concepts, practical applications, and orchestration of robust solutions using techniques like RAG, agents, and MLOps.

## <img src="https://cdn-icons-png.flaticon.com/512/6062/6062161.png" width="80"/> Learning Objectives

By the end of this lab, you will be able to:

- Understand the core concepts and key terminology related to LLMs.
- Set up a proper development environment for working with LLM APIs.
- Explain the principles of NLP, NLU, and NLG and how they relate to LLMs.
- Evaluate different model architectures and fine-tuning techniques.
- Implement Retrieval-Augmented Generation (RAG) pipelines using vector databases like FAISS and Weaviate.
- Orchestrate complex workflows using LangChain, LangGraph, Semantic Kernel, and others.
- Build autonomous systems with tool-using LLM agents.
- Monitor, trace, and evaluate model performance with MLflow, LangSmith, and LangFuse.
- Apply all concepts in hands-on projects and domain-specific scenarios like IVR.


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
├── 02-NLP-NLU-NLG/                                # NLP foundations and connections with LLMs
│   ├── 02-1-Tokenization.md                       # Tokenization methods: BPE, WordPiece, SentencePiece
│   ├── 02-2-Vector/
│   │   ├── 02-2-1-Vectors.md                     # Vector spaces, cosine similarity, distance metrics
│   │   ├── 02-2-2-Embeddings.md                  # One-hot, word2vec, transformer-based embeddings
│   │   ├── 02-2-3-Positional-Encoding.md         # Encoding word order in embeddings
│   │   ├── 02-2-4-Ingesting-Documents.md         # Preparing raw docs for embedding pipelines
│   │   ├── 02-2-5-Text-Splitting.md              # Chunking, sliding windows, recursive splitting
│   │   └── 02-2-6-Similarity-Search.md           # Nearest neighbor search in vector DBs
│   ├── 02-3-NLP-Basics.md                        # Text preprocessing and normalization
│   ├── 02-4-NLU-Intro.md                         # Intent detection, entity extraction
│   ├── 02-5-NLG-Overview.md                      # Rule-based vs neural language generation
│   ├── 02-6-Applications-in-LLMs.md              # Practical applications of LLMs
│   └── 02-7-NLP-with-NLU-and-NLG.md              # NLP vs NLU vs NLG
│
├── 03-RAG-Pipeline/                               # Retrieval-augmented generation
│   ├── 03-1-RAG-Concepts.md                       # What is RAG and why it matters
│   ├── 03-2-Vector-Databases/
│   │   ├── Weaviate-Integration.md                # Setup, indexing, querying with Weaviate
│   │   └── FAISS-Usage.md                         # Local similarity search with FAISS
│   ├── 03-3-Chunking-and-Embedding.md             # Best practices for chunking and embeddings
│   └── 03-4-Retrieval-Strategies.md               # Dense, sparse, hybrid retrieval methods
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
├── notebooks/                                     # Jupyter notebooks for experiments
│   ├── 01-transformer-lm/
│   │   ├── 01-mini-gpt-char.ipynb          # Minimal character-level GPT
│   │   ├── 02-genesis-transformer.ipynb    # More advanced Transformer LM
│   │   ├── README.md                       # Explains both steps
│   │   └── requirements.txt
│   └── 03-rag/
│       └──  rag_from_scratch_1_to_4
│
└── scripts/                                        # Utility scripts for loaders, embeddings, etc.
    ├── utils.py
    ├── loaders.py
    └── embeddings.py

```

<hr/>

<div align="center">
  <img src="https://i.ibb.co/kgNSnpv/git-support.png">
</div>
