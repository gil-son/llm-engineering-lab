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

## 02.1.2. Text Splitting 

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/7963/7963858.png" width="80"/> Introduction

Text splitting is the process of breaking large blocks of text into
smaller, manageable chunks.\
This is essential for NLP tasks, especially when working with LLMs that
operate on limited context windows.

---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/5557/5557844.png" width="80"/> Why use it?

Why use it?

-   Large texts exceed LLM context window limits
-   Efficient indexing for RAG pipelines
-   Enables parallel processing
-   Reduces noise and improves embedding quality
-   Allows chunk-level retrieval instead of retrieving entire documents

---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/2299/2299623.png" width="80"/> Components

-   **Chunk Size** --- max number of characters/tokens per split\
-   **Chunk Overlap** --- repeated text between chunks for context
    continuity\
-   **Splitting Strategy**
    -   by character\
    -   by sentences\
    -   by paragraphs\
    -   by semantic boundaries
---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/7527/7527144.png" width="80"/> How it works?

#### Step-by-step Process

1.  Load and normalize text\
2.  Choose splitting strategy\
3.  Define chunk size and overlap\
4.  Apply split algorithm\
5.  Validate semantic continuity\
6.  Output chunks for further processing (embeddings, indexing, etc.)

#### Simple Diagram

``` mermaid
graph TD
    A[Raw Text] --> B[Choose Splitter]
    B --> C[Define Chunk Size & Overlap]
    C --> D[Split Text]
    D --> E[Generate Chunks]
    E --> F[Used by LLM / Vector Store / Pipelines]
```

---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/6404/6404564.png" width="80"/> Use Cases

[In the soon]

### <img src="https://cdn-icons-png.flaticon.com/512/6675/6675847.png" width="80"> Limitations

-   Overlapping increases computational cost\
-   Very small chunks reduce semantic meaning\
-   Incorrect strategy harms retrieval quality\
-   Token-level splitting may cut sentences unnaturally

---


### <img src="https://cdn-icons-png.flaticon.com/512/2147/2147809.png" width="80"> Code/Notebook/Projects

[In the soon]

---

### <img src="https://cdn-icons-png.flaticon.com/512/2112/2112889.png" width="80"> Videos

A few recommended resources to visualize:

[In the soon]
