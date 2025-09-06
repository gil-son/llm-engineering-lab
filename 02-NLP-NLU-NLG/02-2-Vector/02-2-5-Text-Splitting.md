# 02-2-5-Text-Splitting

# What is Text Splitting?

<div align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxEyD52aYxB5vOd6y1ANVmeL6NUtF4UReX72UbgJIzEj7X9F4_z-fVXphlbwtKHxTHQHo&usqp=CAU" width="20%">
</div>  
<br/>

**Text Splitting** is the process of dividing long documents into smaller, more manageable chunks before embedding or processing with Large Language Models (LLMs).  

Because LLMs have a **context window limit** (a maximum number of tokens they can handle), text splitting ensures that large documents can be broken down into overlapping or structured parts while preserving semantic meaning.  

This step is critical in **Retrieval-Augmented Generation (RAG)**, document search, and summarization pipelines.  

---

<details><summary><h3><a href="#"><img src="https://cdn-icons-png.flaticon.com/512/4133/4133589.png" width="5%"></a>Why is text splitting necessary?</h3></summary>  

Text splitting solves key challenges:  

- **Context Window Limits**: Prevents exceeding the model’s token limit.  
- **Efficient Retrieval**: Smaller chunks improve the accuracy of similarity search in vector databases.  
- **Semantic Preservation**: Splitting ensures chunks retain meaningful context.  
- **Overlap Handling**: Maintains context flow across sections of text.  

</details>  

---

<details><summary><h3><a href="#"><img src="https://cdn-icons-png.flaticon.com/512/2833/2833807.png" width="5%"></a>How does text splitting work?</h3></summary>  

Text splitting can be performed in multiple ways:  

1. **Chunking**  
   - Breaks text into fixed-size pieces (e.g., 500 tokens each).
       <div align="center"><img src="https://baoyu.io/images/rag/5-levels-of-text-splitting/ChunkVizCharacter34_4_w_overlap.png" width="70%"></div><hr/>
        - Breaks text into fixed-size pieces. Often used with overlap.
        - Example:
            - Text length ≈ 1100 tokens, chunk size ≈ 470, overlap = 45
            
        <div align="center"><img src="https://baoyu.io/images/rag/5-levels-of-text-splitting/ChunkVizCharacterRecursive.png" width="70%"></div><hr/>
   
     
   - May include **overlap** (e.g., 500 tokens with 30/40/50-token overlap) to preserve context.


3. **Sliding Window**  
   - A moving window of tokens is applied, sliding by a fixed step.  
   - Example: Window size = 400, step size = 100 → creates overlapping chunks.

4. **Recursive Character Splitting**  
   - Splits text hierarchically: paragraphs → sentences → words → characters.  
   - Useful for documents with irregular structure (e.g., legal texts, logs).  
   - Example Process:
        - Split by paragraph (\n\n)
        - If too long, split by sentence (.)
        - If still long, split by words or characters
---

### Step-by-step Process  

1. **Input Document**  
   - Example: A research paper of 10,000 tokens.  

2. **Define Chunking Strategy**  
   - Fixed-size chunks: 500 tokens.  
   - Overlap: 50 tokens between chunks.  

3. **Split into Chunks**  
   - Document → `[Chunk 1, Chunk 2, Chunk 3, …]`.  

4. **Optional Recursive Splitting**  
   - Large chunk → split by sentences → fallback to words if too long.  

5. **Pass Chunks to Embedding / RAG**  
   - Each chunk is vectorized for similarity search.  

---

### Simple Diagram  

```mermaid
graph TD
    A[Long Document] --> B[Define Chunking Strategy]
    B --> C[Chunking / Sliding Window / Recursive Split]
    C --> D[Overlapping Chunks]
    D --> E[Embedding or Vector Database]
    E --> F[Search & Retrieval]
```  

</details>  

---

<details><summary><h3><a href="#"><img src="https://cdn-icons-png.flaticon.com/512/3588/3588592.png" width="5%"></a>Common splitting techniques</h3></summary>  

- **Fixed-size Chunking**: Simple, fast, but may cut sentences in half.  
- **Overlapping Chunking**: Preserves semantic flow between chunks.
    - One way to prevent AI from hallucinating is to use "chunk overlap." This means reserving a certain number of tokens from the current chunk with those from the previous chunk, ensuring that the context of the chunks is related to each other.
    - <div align="center"><img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/0*rldz9gxQPzzbqCv5" width="50%"></div><hr/>
    - <div align="center"><img src="https://miro.medium.com/v2/resize:fit:720/format:webp/0*jkuQgGbrxGookb88.png" width="50%"></div>
    <div align="center">Tip: on average, a good overlap rate for document indexing is around 20%, for every 1000 tokens, 200 tokens will be overlapping</div>
    
- **Recursive Splitting**: Smart fallback that keeps chunks semantically valid.  
- **Sliding Windows**: Great for maintaining sequential context.  

</details>  

---

<details><summary><h3><a href="#"><img src="https://cdn-icons-png.flaticon.com/512/1705/1705312.png" width="5%"></a>Best practices</h3></summary>  

- Match chunk size to the **embedding model’s max token length**.
- Use **overlap (10–20%)** to avoid losing context between chunks.  
- Apply **recursive splitting** for structured or irregular data.  
- Test different chunk sizes for performance vs accuracy tradeoffs.  

</details>  

---

<details><summary><h3><a href="#"><img src="https://cdn-icons-png.flaticon.com/512/2965/2965363.png" width="5%"></a>Videos</h3></summary>  

<div align="center">  
  <a href="https://www.youtube.com/watch?v=gnLBEUyk3hg" target="_blank">  
      <img width="640" height="360" src="https://i.ytimg.com/vi/gnLBEUyk3hg/maxresdefault.jpg"/>  
  </a>  
</div>  
<hr/>  
<div align="center">  
  <a href="https://www.youtube.com/watch?v=Uqz9lNQyPeY" target="_blank">  
      <img width="640" height="360" src="https://i.ytimg.com/vi/Uqz9lNQyPeY/maxresdefault.jpg"/>  
  </a>  
</div>  

</details>  
