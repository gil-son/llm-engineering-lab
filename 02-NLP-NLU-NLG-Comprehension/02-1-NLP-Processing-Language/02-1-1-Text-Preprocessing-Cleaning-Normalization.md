# 02.1. NLP — Processing Language

<div align="center">
  <table>
    <tr>
      <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/1713/1713860.png" width="80"/></td>
      <td align="center"><img src="https://raw.githubusercontent.com/gil-son/experimental/refs/heads/main/matrizero/v001/src/assets/images/understating-meaning.png" width="80"/></td>
      <td align="center"><img src="https://raw.githubusercontent.com/gil-son/experimental/refs/heads/main/matrizero/v001/src/assets/images/generating-text.png" width="80"/></td>
      <td align="center"><img src="https://raw.githubusercontent.com/gil-son/experimental/refs/heads/main/matrizero/v001/src/assets/images/evaluating.png" width="80"/></td>
    </tr>
  </table>
</div>

## 02.1.1. Text Preprocessing / Cleaning / Normalization

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/7963/7963858.png" width="80"/> Introduction

---

Natural Language Processing (NLP) begins with **text preprocessing**, the stage where raw, unstructured text is cleaned and transformed into a consistent format suitable for computational models.

This process ensures that models receive standardized input and can focus on learning semantics rather than handling noise or inconsistencies.

Common preprocessing steps include:
- Text normalization (lowercasing, removing punctuation)
- Tokenization (splitting text into words or subwords)
- Lemmatization and stemming (reducing words to their base forms)
- Removing stop words and special characters
- Handling misspellings, URLs, and emojis

---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/5557/5557844.png" width="80"/> Why use it?
  
---

Text preprocessing ensures that the input to NLP or LLM systems is:
- **Clean** — free from noise, typos, and irrelevant symbols
- **Consistent** — unified in structure and format
- **Efficient** — reducing unnecessary complexity before vectorization
- **Meaningful** — preserving semantic value while removing redundancy

Without preprocessing, downstream tasks like tokenization, embedding, or model inference can suffer from **data drift**, **inconsistencies**, and **lower accuracy**.

---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/2299/2299623.png" width="80"/> Components

---

Core components of the text preprocessing pipeline include:

1. **Text Cleaning** — remove URLs, punctuation, HTML tags, and emojis  
2. **Normalization** — convert all text to lowercase, fix contractions, normalize whitespace  
3. **Tokenization** — split text into words, subwords, or characters  
4. **Stopword Removal** — eliminate frequent but low-information words like *“the”*, *“and”*, etc.  
5. **Lemmatization / Stemming** — reduce words to their root or canonical form  
6. **Vectorization** — transform text into numeric representations (TF-IDF, Word2Vec, embeddings)

---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/7527/7527144.png" width="80"/> How it works?

---

The text preprocessing pipeline transforms unstructured input into clean, tokenized data that can be embedded and processed by models.

#### Step-by-step Process

1. Collect raw text from a source (e.g., documents, user input, web scraping)  
2. Remove unwanted characters, links, and formatting  
3. Normalize case and expand contractions  
4. Tokenize into smaller units (words or subwords)  
5. Apply stemming or lemmatization to unify words  
6. Convert to numerical vectors or embeddings for use in downstream models

#### Simple Diagram

```mermaid
graph TD
    A[Raw Text] --> B[Text Cleaning]
    B --> C[Normalization]
    C --> D[Tokenization]
    D --> E[Lemmatization / Stemming]
    E --> F[Vectorization / Embedding]
    F --> G[Processed Data for NLP Model]
```

---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/6404/6404564.png" width="80"/> Use Cases

---

- Preprocessing text for **sentiment analysis**, **topic modeling**, and **text classification**  
- Preparing clean input for **LLM fine-tuning** or **RAG pipelines**  
- Building preprocessing modules for **chatbots** or **voice assistants**  
- Data preparation for **embedding-based retrieval systems** (e.g., ChromaDB, FAISS)

---

### <img src="https://cdn-icons-png.flaticon.com/512/6675/6675847.png" width="80"> Limitations

---

- Over-cleaning can **remove important context or meaning**  
- Lemmatization and stemming may **introduce errors** in some languages  
- Handling multilingual text adds **complexity** to preprocessing rules  
- Noise in input data can still propagate if not properly cleaned  

---

### <img src="https://cdn-icons-png.flaticon.com/512/2147/2147809.png" width="80"> Code/Notebook/Projects

[In the soon]

---

### <img src="https://cdn-icons-png.flaticon.com/512/2112/2112889.png" width="80"> Videos

A few recommended resources to visualize:

[In the soon]
