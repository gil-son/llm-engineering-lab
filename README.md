# Introduction to the LLM Engineering Lab

<p align="center">
  <img src="https://gitlab.com/gil-son/useful-images-collection/-/raw/main/png/devs.png?ref_type=heads" width="40%">
</p>

Welcome to the **LLM Engineering Lab**  – a comprehensive, structured repository designed to take you from LLM fundamentals to production-ready applications. Whether you're just starting with Large Language Models or looking to build sophisticated AI systems, this lab provides hands-on learning paths, practical implementations, and real-world projects to master the entire LLM engineering lifecycle.

## <img src="https://cdn-icons-png.flaticon.com/512/4681/4681450.png" width="80"/>  Repository Summary


It is important to understand the meaning and purpose of each section:

- **01-LLM-Fundamentals**: Core LLM concepts, architectures, training strategies (fine-tuning, RLHF), and evaluation metrics. Understanding transformer models, pretraining objectives, and instruction tuning.
- **02-NLP-NLU-NLG-Comprehension**: Foundations of natural language processing (tokenization, embeddings), understanding (intent extraction, entity recognition), and generation (coherent text output, decoding strategies).
- **03-Prompt-Engineering:**: Advanced prompting strategies including zero-shot/one-shot/few-shot learning, chain-of-thought reasoning, prompt templates, optimization techniques, and comparison of prompt tuning vs prefix tuning methods.
- **04-RAG Pipeline:**: Implementation of Retrieval-Augmented Generation techniques for context: Ingestion, Retrieval, Generation, Continuous Improvement.
- **05-Context-Management:**: LLM context management, often referred to as context engineering, is the practice of strategically curating, organizing, and optimizing the information (context) provided to a Large Language Model within its limited "context window" to ensure relevant, accurate, and cost-effective responses.
- **06-Model-Context-Protocol:**: Deep dive into Anthropic's Model Context Protocol (MCP) - the universal standard for connecting AI applications to data sources and tools. Covers MCP architecture, building custom servers (Python/TypeScript), security practices, and integration with orchestration frameworks.
- **07-LLM-Orchestration:**: Tools and frameworks for orchestrating complex LLM workflows, including Model Context Protocol (MCP), Semantic Kernel, LangChain, LangGraph, LangSmith, LangFlow, and LangFuse for debugging and observability.
- **08-Agentic-AI-Systems:**: Building autonomous AI agents with reasoning capabilities, tool integration (APIs, search, functions), planning strategies, and multi-agent collaboration patterns.
- **09-Evaluation-and-Benchmarks:**: Comprehensive evaluation strategies including prompt testing, performance metrics (BLEU, ROUGE, perplexity), hallucination detection, latency/cost tracking, and distributed tracing with LangSmith.
- **10-MLOps-and-Production:**: Productionizing LLM systems with MLOps best practices including experiment tracking with MLflow, model versioning and registry, continuous integration/deployment (CI/CD) pipelines, monitoring and logging in production, performance optimization, cost management, and integration with orchestration frameworks for robust, scalable deployments.
- **11-LLM-Data-Engineering:**: Dataset lifecycle management including collection strategies, data cleaning and filtering techniques, formatting for model training, and synthetic data generation.
- **12-AI-IVR-Specifics:**: Applying LLMs to Interactive Voice Response (IVR) systems, including speech-to-text/text-to-speech integration, dialogue management, and orchestration framework comparisons for voice applications.
- **projects/**: Practical and applied hands-on projects.
- **notebooks/**: Jupyter notebooks for experiments and demonstrations.
- **scripts/**: Utility scripts and helper functions.

## <img src="https://cdn-icons-png.flaticon.com/512/6062/6062161.png" width="80"/> Learning Objectives

By the End of This Lab, You Will Be Able To:

- **Foundation & Core Concepts**
    - **Understand** the architecture and mechanics of Large Language Models, from transformers to attention mechanisms
    - **Build** a miniature GPT model from scratch to deeply understand the underlying principles
    - **Master** key terminology and concepts that form the language of modern LLM engineering
- **Natural Language Processing**
    - **Apply** foundational NLP, NLU, and NLG techniques to process, understand, and generate human language
    - **Implement** tokenization, embeddings, intent extraction, and entity recognition pipelines
    - **Evaluate** different model architectures and select appropriate fine-tuning strategies (supervised, RLHF, instruction tuning)
- **Retrieval-Augmented Generation (RAG)**
    - **Implement** end-to-end RAG pipelines from document ingestion to context-aware generation
    - **Work with** vector databases including FAISS and Weaviate for efficient semantic search
    - **Evaluate and improve** retrieval quality through continuous iteration and testing
- **Context Management**
    - **Optimize** context windows to maximize information density within token limits
    - **Track** conversation state and history for coherent multi-turn dialogues
    - **Implement** memory systems for long-term information retention across sessions
    - **Structure** outputs in specific formats (JSON, XML, function calls) for downstream processing
- **Model Context Protocol (MCP)**
    - **Understand** MCP as the universal standard for connecting AI applications to external tools and data
    - **Build** custom MCP servers in Python and TypeScript for your specific use cases
    - **Integrate** MCP with orchestration frameworks to create flexible, modular AI systems
- **Orchestration & Workflows**
    - **Orchestrate** complex LLM workflows using LangChain, LangGraph, and Semantic Kernel
    - **Debug and trace** applications with LangSmith for complete observability
    - **Visualize** workflows with LangFlow and monitor production systems with LangFuse
- **Agentic Systems**
    - **Build** autonomous AI agents with reasoning, planning, and tool-use capabilities
    - **Integrate** external APIs, search engines, and custom functions as agent tools
    - **Design** multi-agent systems with collaboration patterns and shared objectives
- **Evaluation & Quality Assurance**
    - **Monitor** model performance using industry-standard metrics (BLEU, ROUGE, perplexity)
    - **Detect** hallucinations and implement quality gates in your pipelines
    - **Track** latency, cost, and resource utilization for production optimization
    - **Trace** distributed systems with comprehensive logging and debugging tools
- **Production & MLOps**
    - **Deploy** LLM systems to production with CI/CD pipelines and automated testing
    - **Track** experiments and manage model versions using MLflow
    - **Monitor** production systems with logging, alerts, and performance dashboards
    - **Optimize** costs and performance for scalable, enterprise-grade deployments
- **Data Engineering**
    - **Collect** and curate high-quality datasets for training and fine-tuning
    - **Clean** and filter data to ensure consistency and relevance
    - **Generate** synthetic data for scenarios where real data is scarce or sensitive
- **Dataset lifecycle management**
  - **Collect** and curate high-quality datasets from diverse sources for training and fine-tuning
  - **Clean** and filter data to ensure consistency, remove duplicates, and maintain quality standards
  - **Format** datasets according to specific model requirements and training objectives
  - **Generate** synthetic data to augment training sets and address data scarcity challenges
- **Domain Applications**
    - **Apply** LLM techniques to specialized domains like Interactive Voice Response (IVR) systems
    - **Integrates** speech-to-text and text-to-speech for voice-enabled applications
    - **Manage** complex dialogues in real-time conversational systems

<p align="center">
  <img src="https://gitlab.com/gil-son/useful-images-collection/-/raw/main/png/llm-lab.png?ref_type=heads">
</p>


## <img src="https://cdn-icons-png.flaticon.com/512/18310/18310876.png" width="80"/>  Learning Path

This is a recommended progressive learning path::

```
START HERE
    ↓
[01] LLM Fundamentals ← Must understand basics first
    ↓
[02] NLP/NLU/NLG ← Language processing concepts
    ↓
[03] Prompt Engineering ← How to talk to LLMs
    ↓
[04] RAG Pipeline ← Connecting LLMs to knowledge
    ↓
[05] Context Management ← Managing conversations
    ↓
[06] MCP ← Universal tool/data layer
    ↓
[07] Orchestration ← Using MCP with frameworks
    ↓
[08] Agentic Systems ← Building autonomous agents
    ↓
[09] Evaluation ← Testing everything
    ↓
[10] MLOps ← Production deployment
    ↓
[11] Data Engineering ← Training data pipelines
    ↓
[12] IVR Specifics ← Domain application
```

---

## <img src="https://cdn-icons-png.flaticon.com/512/1797/1797536.png" width="80"/>  Repository Structure


The repository is organized into numbered folders to reflect a progressive learning path:

```
llm-engineering-lab/
│
├── README.md                                      # Introduction, objectives, repo overview, usage instructions
│
├── 01-LLM-Fundamentals/                           # LLM Path
│   ├── README.md                                  # Overview LLM
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
├── 02-NLP-NLU-NLG-Comprehension/                  # NLP-NLU-NLG Path
│   ├── README.md                                  # NLP-NLU-NLG Overview
│   ├── 02-1_NLP_Processing_Language/              # Text preparation and transformation into machine-readable form
│   ├── 02-2_NLU_Understanding_Meaning/            # Extracting intent, entities, and semantic relationships
│   ├── 02-3_NLG_Generating_Text/                  # Producing coherent natural language output
│   └── 02-4_Evaluation_Refining_the_System/       # Measuring, optimizing, and improving model performance
│
├── 03-Prompt-Engineering/                         # Crafting effective prompts
│   ├── README.md                                  # Prompt Engineering Overview
│   ├── 03-1-Zero-Shot-One-Shot-Few-Shot.md        # Different prompting strategies
│   ├── 03-2-Chain-of-Thought.md                   # Step-by-step reasoning
│   ├── 03-3-Prompt-Templates.md                   # Reusable patterns
│   ├── 03-4-Prompt-Optimization.md                # Testing & iteration
│   └── 03-5-Prompt-Tuning-vs-Prefix-Tuning.md     # Lightweight tuning methods
│
├── 04-RAG-Pipeline/                               # Retrieval-Augmented Generation
│   ├── README.md                                  # RAG Overview
│   ├── 04-1-Document-Ingestion.md                 # Loading, preprocessing, chunking documents
│   ├── 04-2-Retrieval-Strategies.md               # Semantic search, vector databases
│   ├── 04-3-Generation-and-Synthesis.md           # Combining retrieval with generation
│   └── 04-4-RAG-Evaluation.md                     # Continuous improvement and metrics
│
├── 05-Context-Management/                         # Managing LLM context
│   ├── README.md                                  # Context Management Overview
│   ├── 05-1-Context-Window-Management.md          # Token limits, truncation strategies
│   ├── 05-2-State-and-History.md                  # Conversation state tracking
│   ├── 05-3-Memory-Systems.md                     # Long-term memory patterns
│   └── 05-4-Structured-Outputs.md                 # JSON, XML, function call formatting
│
├── 06-Model-Context-Protocol/                     # Universal AI integration standard
│   ├── README.md                                  # MCP Overview
│   ├── 06-1-MCP-Introduction.md                   # What is MCP, why it matters
│   ├── 06-2-MCP-Architecture.md                   # Hosts, clients, servers, transports
│   ├── 06-3-Using-MCP-Servers.md                  # Installing & configuring existing servers
│   ├── 06-4-Building-MCP-Servers-Python.md        # Complete Python tutorial
│   ├── 06-5-Building-MCP-Servers-TypeScript.md    # TypeScript/Node.js version
│   ├── 06-6-MCP-Security-Best-Practices.md        # Security, sandboxing, validation
│   └── 06-7-MCP-Advanced-Patterns.md              # Code execution, optimization
│
├── 07-LLM-Orchestration/                          # Orchestrating LLM workflows
│   ├── README.md                                  # LLM Orchestration Overview
│   ├── 07-1-Orchestration-Overview.md             # When & why to orchestrate
│   ├── 07-2-MCP-in-Orchestration.md               # How MCP fits in
│   ├── 07-3-Semantic-Kernel.md                    # Microsoft's Semantic Kernel
│   ├── 07-4-LangChain-Concepts.md                 # Chains, agents, retrievers, memory
│   ├── 07-5-LangGraph-Workflows.md                # Stateful workflows with LangGraph
│   ├── 07-6-LangSmith-Debugging.md                # Debugging, tracing, evaluation
│   ├── 07-7-LangFlow-Visual-Builder.md            # Visual builder for LangChain workflows
│   ├── 07-8-LangFuse-Observability.md             # Monitoring & analytics in production
│   └── 07-9-Orchestration-Comparison.md           # When to use each tool
│
├── 08-Agentic-AI-Systems/                         # Autonomous AI agents
│   ├── README.md                                  # Agentic AI Systems Overview
│   ├── 08-1-What-Are-AI-Agents.md                 # Clear definition and concepts
│   ├── 08-2-Agent-Architectures.md                # ReAct, Plan-Execute, etc.
│   ├── 08-3-Tool-Integration.md                   # APIs, search, databases, functions
│   ├── 08-4-MCP-Tools-in-Agents.md                # MCP as tool layer
│   ├── 08-5-Agent-Memory-and-Planning.md          # Long-term memory and reasoning
│   └── 08-6-Multi-Agent-Systems.md                # Agent collaboration patterns
│
├── 09-Evaluation-and-Benchmarks/                  # Testing and evaluating LLMs
│   ├── README.md                                  # Evaluation Overview
│   ├── 09-1-Evaluation-Overview.md                # Testing philosophy and strategies
│   ├── 09-2-Prompt-Evaluation.md                  # Assessing prompt quality
│   ├── 09-3-Metrics-and-Benchmarks.md             # Accuracy, BLEU, ROUGE, perplexity
│   ├── 09-4-Hallucination-Detection.md            # Detecting and preventing hallucinations
│   ├── 09-5-Latency-and-Cost-Tracking.md          # Runtime, token usage, cost tracking
│   └── 09-6-LangSmith-Tracing.md                  # Distributed tracing with LangSmith
│
├── 10-MLOps-and-Production/                       # Productionizing LLM systems
│   ├── README.md                                  # MLOps and Production Overview
│   ├── 10-1-Production-Readiness.md               # Deployment considerations
│   ├── 10-2-MLflow-Basics.md                      # Logging and tracking experiments
│   ├── 10-3-Experiment-Tracking.md                # MLflow for prompt + retrieval stats
│   ├── 10-4-LangChain-MLflow-Integration.md       # MLflow integration with LangChain
│   ├── 10-5-Monitoring-and-Logging.md             # Production monitoring and alerts
│   └── 10-6-CI-CD-for-LLM-Systems.md              # Deployment pipelines
│
├── 11-LLM-Data-Engineering/                       # Dataset lifecycle for training
│   ├── README.md                                  # LLM Data Engineering Overview
│   ├── 11-1-Data-Engineering-Overview.md          # Data lifecycle and principles
│   ├── 11-2-Dataset-Collection.md                 # Gathering high-quality training data
│   ├── 11-3-Data-Cleaning-and-Filtering.md        # Cleaning and filtering for consistency
│   ├── 11-4-Dataset-Formatting.md                 # Formatting datasets for model training
│   └── 11-5-Synthetic-Data-Generation.md          # Creating training data
│
├── 12-AI-IVR-Specifics/                           # LLMs in IVR systems
│   ├── README.md                                  # AI-IVR-Specifics Overview
│   ├── 12-1-IVR-System-Overview.md                # Interactive Voice Response systems
│   ├── 12-2-Speech-to-Text-and-TTS.md             # Speech-to-text and TTS integration
│   ├── 12-3-Dialogue-Management.md                # Managing conversations with LLMs
│   ├── 12-4-MCP-in-IVR-Systems.md                 # MCP for telephony integration
│   └── 12-5-Orchestration-for-IVR.md              # LangChain vs Semantic Kernel in IVR
│
├── projects/                                      # Hands-on projects
│   ├── 01-basic-rag/                              # Simple RAG implementation
│   ├── 02-weaviate-rag/                           # RAG with Weaviate vector DB
│   ├── 03-weather-mcp-server/                     # Custom MCP server example
│   ├── 04-langchain-agent/                        # Agent with LangChain
│   ├── 05-semantic-kernel-bot/                    # Bot with Semantic Kernel
│   └── 06-multi-agent-system/                     # Multi-agent collaboration
│
├── notebooks/                                     # Jupyter notebooks for experiments
│   ├── 01-LLM-Fundamentals/
│   │   ├── 01-mini-gpt-char.ipynb                 # Minimal character-level GPT
│   │   ├── 02-genesis-transformer.ipynb           # More advanced Transformer LM
│   │   ├── README.md                              # Explains both steps
│   │   └── requirements.txt
│   ├── 02-NLP-NLU-NLG/                            # NLP (NLU and NLG) examples
│   ├── 03-Prompt-Engineering/                     # Prompt engineering experiments
│   ├── 04-RAG-Pipeline/                           # RAG examples
│   │   └── rag_from_scratch_1_to_4/
│   ├── 05-Context-Management/                     # Context management examples
│   ├── 06-MCP/                                    # MCP experiments
│   │   ├── 01-mcp-basics.ipynb
│   │   ├── 02-build-simple-server.ipynb
│   │   └── 03-mcp-with-langchain.ipynb
│   ├── 07-LLM-Orchestration/                      # LLM Orchestration examples
│   └── 08-Agentic-Systems/                        # Agent building examples
│
└── scripts/                                       # Utility scripts for loaders, embeddings, etc.
    ├── utils.py                                   # General utility functions
    ├── loaders.py                                 # Document loaders
    ├── embeddings.py                              # Embedding generators
    └── mcp_utils.py                               # MCP helper functions
```

<hr/>

<div align="center">
  <img src="https://i.ibb.co/kgNSnpv/git-support.png">
</div>