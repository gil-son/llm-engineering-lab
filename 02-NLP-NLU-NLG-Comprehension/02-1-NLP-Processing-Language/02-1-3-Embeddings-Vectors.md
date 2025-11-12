# 2.1.3. Embeddings Vectors

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

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/7963/7963858.png" width="80"/> Introduction

---

Embeddings are numerical vector representations of text (words, sentences, or documents) that capture their **semantic meaning**. They allow machines to understand relationships between words — like similarity, context, and meaning — in a **continuous vector space**.

For example:
- “King” - “Man” + “Woman” ≈ “Queen”  
- Similar sentences will have similar embedding vectors.

---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/5557/5557844.png" width="80"/> Why use it?
  
- To represent text numerically for ML/LLM models.  
- To capture **semantic similarity** rather than surface-level similarity.  
- To enable efficient search, clustering, and reasoning over language.  
- Essential for **RAG pipelines**, **semantic search**, and **recommendation systems**.

---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/2299/2299623.png" width="80"/> Components

1. **Tokenization** – break text into tokens.  
2. **Embedding model** – transform tokens into dense vectors.  
3. **Vector space** – multidimensional space where meaning is encoded.  
4. **Similarity metric** – measure relationships (e.g., cosine similarity).  

---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/7527/7527144.png" width="80"/> How it works?

#### Step-by-step Process

1. Input text is tokenized.  
2. Each token is mapped to an embedding vector (learned during training).  
3. These vectors are combined to represent sentences or documents.  
4. Similar meanings → similar vectors in high-dimensional space.

#### Simple Diagram

```mermaid
graph TD
    A[Text Input] --> B[Tokenizer]
    B --> C[Embedding Model]
    C --> D[Vector Representation]
    D --> E[Similarity or Downstream Task]
```

---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/6404/6404564.png" width="80"/> Use Cases

- **Semantic Search** (find text with similar meaning)  
- **Recommendation Systems**  
- **RAG Pipelines** (Retrieve relevant documents by vector similarity)  
- **Clustering or Visualization of text**  
- **Intent Detection or Classification**  

---

### <img src="https://cdn-icons-png.flaticon.com/512/6675/6675847.png" width="80"> Limitations

- Embeddings depend on the **training corpus** → bias risk.  
- High-dimensional vectors can be **computationally expensive**.  
- Semantic similarity ≠ logical reasoning.  
- May fail for **rare words or domain-specific jargon**.

---

### <img src="https://cdn-icons-png.flaticon.com/512/2147/2147809.png" width="80"> Code/Notebook/Projects

- [Create an LLM from scratch](https://github.com/gil-son/llm-engineering-lab/tree/main/notebooks/01-transformer-lm)


---

### <img src="https://cdn-icons-png.flaticon.com/512/2112/2112889.png" width="80"> Videos

A few recommended resources to visualize:

<div align="center">
  <a href="https://www.youtube.com/watch?v=izbifbq3-eI" target="_blank">
      <img width="640" height="360" src="https://i.ytimg.com/vi/izbifbq3-eI/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLB7eYOYt31W_QwtEHOhRbTKJm0tcg"/>
  </a>
</div>
<hr/>
<div align="center">
  <a href="https://www.youtube.com/watch?v=wgfSDrqYMJ4" target="_blank">
      <img width="640" height="360" src="https://i.ytimg.com/vi/wgfSDrqYMJ4/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLB4JQaAFm37tOg6cy7IM1CgJFCIQg"/>
  </a>
</div>
