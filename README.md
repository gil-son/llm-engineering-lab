# Introduction to the LLM Engineering Lab

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
├── README.md                                      # Introduction to the lab and learning objectives and repository overview and usage instructions
│
├── 01-Concepts-and-Setup/                         # Core LLM concepts and environment setup
│   ├── 01-1-What-is-an-LLM.md                     # Simple explanation of Large Language Models and their importance
│   ├── 01-2-Key-Terms.md                          # Glossary of essential LLM terms like token, prompt, inference
│   └── 01-3-Environment-Setup.md                  # Guide to setting up Python environment, APIs, and dependencies
│
├── 02-NLP-NLU-NLG/                                
│   ├── 02-1-Tokenization.md                       # Tokenization methods: BPE, WordPiece, SentencePiece
│   ├── 02-2-Embeddings.md                         # From one-hot to contextual: understanding word and token embeddings
│   ├── 02-3-NLP-Basics.md                         # Basic text preprocessing and normalization techniques
│   ├── 02-4-NLU-Intro.md                          # Introduction to intent detection and entity extraction
│   ├── 02-5-NLG-Overview.md                       # Overview of rule-based and neural language generation
│   └── 02-6-Applications-in-LLMs.md               # How LLMs perform NLP, NLU, and NLG tasks
│
├── 03-LLM-Fundamentals/                           # Understanding architectures and training of LLMs
│   ├── 03-1-LLM-Architectures.md                  # Overview of Transformer-based models like GPT and LLaMA
│   ├── 03-2-LLM-Fine-tuning.md                    # Techniques and strategies for fine-tuning LLMs
│   ├── 03-3-LLM-Evaluation.md                     # Metrics and best practices to evaluate LLM performance
│
├── 04-RAG-Pipeline/                               # Concepts and tools for retrieval-augmented generation
│   ├── 04-1-RAG-Concepts.md                       # Introduction to RAG and its practical benefits
│   ├── 04-2-Vector-Databases/                      # Integration with vector similarity databases
│   │   ├── Weaviate-Integration.md                # Setup, indexing, and querying with Weaviate
│   │   └── FAISS-Usage.md                         # Local similarity search using FAISS
│   ├── 04-3-Chunking-and-Embedding.md             # Best practices for text chunking and embeddings
│   └── 04-4-Retrieval-Strategies.md               # Dense, sparse, and hybrid retrieval methods explained
│
├── 05-LLM-Orchestration/                          # Frameworks and tools for orchestrating LLM workflows
│   ├── 05-1-Semantic-Kernel-Overview.md           # Overview of Microsoft’s Semantic Kernel framework
│   ├── 05-2-LangChain-Concepts.md                  # Core LangChain components: chains, agents, retrievers, memory
│   ├── 05-3-LangGraph-Intro.md                     # Introduction to LangGraph for stateful LLM workflows
│   ├── 05-4-LangSmith-Usage.md                     # Using LangSmith for debugging, tracing, and evaluation
│   ├── 05-5-LangFlow-UI-Builder.md                 # Visual UI builder for LangChain workflows
│   └── 05-6-LangFuse-Observability.md              # Monitoring and analytics with LangFuse in production
│
├── 06-Agentic-AI-Systems/                          # Autonomous agents and tool integrations
│   ├── 06-1-Agentic-AI-Principles.md               # Fundamentals of autonomous AI agents
│   ├── 06-2-Tool-Integration-Examples.md           # Examples of giving LLMs external tool access (APIs, search)
│
├── 07-Evaluation-and-Benchmarks/                   # Testing, evaluation metrics, and benchmarks for LLMs
│   ├── 07-1-Prompt-Evaluation.md                    # Methods to assess prompt quality and reliability
│   ├── 07-2-Metrics-and-Benchmarks.md               # Overview of accuracy, BLEU, ROUGE, perplexity metrics
│   ├── 07-3-Hallucination-Detection.md              # Techniques to detect hallucinations in LLM outputs
│   ├── 07-4-Latency-and-Cost.md                      # Measuring runtime, token consumption, and cost
│   └── 07-5-Tracing-with-LangSmith.md                # How to use LangSmith for traceability in evaluations
│
├── 08-MLOps-and-Tracking/                           # Production workflows for managing ML lifecycle
│   ├── 08-1-MLflow-Basics.md                         # Introduction to logging and tracking LLM experiments with MLflow
│   ├── 08-2-Tracking-RAG-and-Prompts.md              # Custom MLflow runs for prompt templates and retrieval stats
│   └── 08-3-Integration-with-LangChain.md            # Using MLflow integration with LangChain workflows
│
├── 09-AI-IVR-Specifics/                             # AI applications in IVR systems
│   ├── 09-1-IVR-System-Overview.md                   # Overview of Interactive Voice Response systems
│   ├── 09-2-Voice-to-Text-Text-to-Voice.md           # Techniques for speech-to-text and text-to-speech integration
│   ├── 09-3-Dialogue-Management-in-IVR.md            # Managing conversational flows with LLMs in IVR
│   └── 09-4-Orchestration-Comparison.md              # Comparing LangChain and Semantic Kernel for IVR orchestration
│
├── projects/                                        # Hands-on projects to apply concepts
│   ├── 01-basic-rag/
│   ├── 02-weaviate-rag/
│   ├── 03-langchain-agent/
│   └── 04-semantic-kernel-bot/
│
├── notebooks/                                       # Jupyter notebooks for experiments and demos
│   ├── langchain_intro.ipynb
│   ├── weaviate_faiss_comparison.ipynb
│   └── openai_agent_demo.ipynb
│
├── scripts/                                        # Utility scripts for loaders, embeddings, etc.
│   ├── utils.py
│   ├── loaders.py
│   └── embeddings.py
│
└── requirements.txt                                # Python dependencies list

```
