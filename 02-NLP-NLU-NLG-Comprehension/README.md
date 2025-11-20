# NLP-NLU-NLG COMPREHENSION SUMMARY

This document provides a structured overview of the core components and steps involved in Natural Language Processing (NLP), Natural Language Understanding (NLU), and Natural Language Generation (NLG).

---

## <img src="https://cdn-icons-png.flaticon.com/512/1713/1713860.png" width="80"/> 2.1. NLP — Processing Language

| Step | Description |
| :--- | :--- |
| **2.1.1 Text Processing / Cleaning / Normalization** | The initial process of preparing raw text by removing noise (e.g., HTML tags, special characters), converting text to a standard case (e.g., lowercasing), and fixing inconsistencies. |
| **2.1.2 Text Splitting** | Dividing long documents into smaller, manageable chunks that respect context boundaries, typically for retrieval or processing by models with context length limits. |
| **2.1.3 Tokenization** | Breaking down the text into smaller units (tokens), which can be words, subwords, or characters, to be used as input for a model. |
| **2.1.4 Embeddings / Vectors** | Representing text tokens (words/subwords) as dense, numerical vectors (e.g., Word2Vec, BERT) that capture their semantic and contextual meaning. |
| **2.1.5 Ingestion (Vector Store)** | Storing the numerical text representations (embeddings) into a specialized database (Vector Store) for efficient search and retrieval operations (e.g., Pinecone, Chroma). |

---

## <img src="https://cdn-icons-png.flaticon.com/512/6062/6062503.png" width="80"/> 2.2 NLU — Understanding Meaning

| Step | Description |
| :--- | :--- |
| **2.2.1 Intent & Entity Recognition** | **Intent:** Identifying the user's overall goal or action (e.g., "book\_flight"). **Entity:** Extracting specific, structured pieces of information (e.g., "flight date," "destination city"). |
| **2.2.2 Semantic & Syntactic Analysis** | **Semantic:** Analyzing the meaning of the text to understand the relationships between words and concepts. **Syntactic:** Analyzing the grammatical structure of sentences (e.g., Part-of-Speech tagging, dependency parsing). |
| **2.2.3 Contextual Disambiguation** | Determining the correct meaning of words or phrases that have multiple interpretations (e.g., resolving the meaning of "bank" in a sentence based on the surrounding context). |
| **2.2.4 Similarity Search (Cosine)** | Using a numerical measure (like Cosine Similarity) on vector representations to find the documents or pieces of information most semantically similar to a user's query. |
| **2.2.5 Knowledge Retrieval** | Fetching relevant facts, documents, or data from a knowledge base (often a Vector Store or Graph Database) to provide comprehensive context for a response. |

---

## <img src="https://cdn-icons-png.flaticon.com/512/10087/10087719.png" width="80"/> 2.3. NLG — Generating Text

| Step | Description |
| :--- | :--- |
| **2.3.1 Content Planning** | Deciding what information should be included in the response, based on the NLU output (intent, entities, knowledge), and organizing the high-level message structure. |
| **2.3.2 Sentence Planning** | Determining the grammatical structure, lexical choices, and discourse features (e.g., coherence, tone) for each sentence that will be generated. |
| **2.3.3 Surface Realization** | The final step of turning the abstract sentence plan into a coherent, grammatically correct natural language string using a generation model (e.g., LLM or sequence-to-sequence model). |
| **2.3.4 Post-processing** | Applying final checks and formatting to the generated text, such as grammar correction, ensuring proper punctuation, and enforcing length or style constraints before delivery. |

---

## <img src="https://cdn-icons-png.flaticon.com/512/2550/2550820.png" width="80"/> 2.4. Evaluation — Refining the System

| Step | Description |
| :--- | :--- |
| **2.4.1 Metrics** | Quantifiable scores used to assess system performance. **Classification:** Accuracy, F1-Score. **Generation:** BLEU, ROUGE (for overlap), and Perplexity (for fluency). |
| **2.4.2 Feedback / RL** | Implementing a continuous learning loop where human feedback (e.g., thumbs up/down, corrections) is gathered and used to refine the model, often via Reinforcement Learning from Human Feedback (RLHF). |

---

## <img src="https://cdn-icons-png.flaticon.com/512/18310/18310876.png" width="80"/> NLP-NLU-NLG Structure 

```
02-NLP-NLU-NLG-COMPREHENSION/
├── 02-1-NLP-Processing-Language/
│   ├── 02-1-1-Text-Processing-Cleaning-Normalization.md
│   ├── 02-1-2-Text-Splitting.md
│   ├── 02-1-3-Tokenization.md
│   ├── 02-1-4-Embeddings-Vectors.md
│   └── 02-1-5-Ingestion-Vector-Store.md
│
├── 02-2-NLU-UNDERSTADING-MEANING/
│   ├── 02-2-1-Intent-Entity-Recognition.md
│   ├── 02-2-2-Semantic-Syntactic-Analysis.md
│   ├── 02-2-3-Contextual-Disambiguation.md
│   ├── 02-2-4-Similarity-Search.md
│   └── 02-2-5-Knowledge-Retrieval.md
│
├── 02-3-NLG-GENERATING-TEXT/
│   ├── 02-3-1-Content-Planning.md
│   ├── 02-3-2-Sentence-Planning.md
│   ├── 02-3-3-Surface-Realization.md
│   └── 02-3-4-Post-processing.md
│
└── 02-4-EVALUATION-REFINING-THE-SYSTEM/
        ├── 02-4-1-Metrics.md
        └── 02-4-2-Feedback_RL.md

```
