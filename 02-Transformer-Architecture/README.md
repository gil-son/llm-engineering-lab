## 02. Transformer-Architecture

<div align="center">
  <table>
    <tr>
      <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/9722/9722973.png" width="80"/></td>
      <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/11149/11149936.png" width="80"/></td>
      <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/2351/2351559.png" width="80"/></td>
      <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/2582/2582078.png" width="80"/></td>
      <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/6062/6062146.png" width="80"/></td>
      <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/10817/10817413.png" width="80"/></td>
    </tr>
  </table>
</div>

---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/7963/7963858.png" width="80"/> Introduction
Transformers were originally created to solve problems where one sequence of information needs to be turned into another. A classic example is translating text from one language to another. Because they transform an input into an output, they are “Transformers”.

---

### What Are Transformer Models?

A Transformer is a type of artificial intelligence that learns how words relate to each other so it can understand and generate text that feels natural to humans.

In simple terms:

A Transformer reads a lot of text, learns patterns in how words are used together, and then uses that knowledge to create new text or understand existing text.

Transformers are the technology behind many modern AI systems, including chatbots and language models. They are an improvement over older approaches because they don’t read text word by word like a human reading a sentence from left to right. Instead, they look at the whole sentence at once.

**So how do they understand meaning without reading step by step?**

They focus on **relationships** between words. For example, they learn which words are important to each other and which ones provide context. This is done using a concept called **attention**, which simply means the model learns where to “pay attention” when trying to understand or generate text.

<div align="center">
<img src="https://github.com/user-attachments/assets/ab49b7e9-cf48-4544-a5e1-d1091291e3ac" width="60%" />
<p>Image by the Datacamp</p>
</div>

---

## <img src="https://cdn-icons-png.flaticon.com/512/8592/8592294.png" width="10%"/>  The Transformer Architecture Overview

Transformers were first created to solve tasks where one sequence is turned into another, such as translating text from one language to another.

You can think of a Transformer as a black box that takes a sentence as input and produces another sentence as output.

For example:

<div align="center">
<img src="https://media.datacamp.com/legacy/v1704797298/image_2edc8e19d7.png" width="60%" />
<p>Image by the Datacamp</p>
</div>

### Encoder

The **encoder** reads the input sentence and turns it into an internal representation that captures its meaning.

```
"How are you?"
```
and converts it into a form the model can understand.

### Decoder

The decoder takes this internal representation and uses it to generate the output sentence, one part at a time.
In our example, it generates:

```
"¿Cómo estás?"
```

### How They Work Together

```
Input sentence → Encoder → Decoder → Output sentence
```
- The encoder understands the input.
- The decoder produces the final result.

### Multiple Layers for Better Understanding

In practice, the encoder and decoder are not just single blocks. Each one is made of multiple layers stacked on top of each other.
- All encoder layers have the same structure
- All decoder layers have the same structure
- The output of one layer becomes the input to the next

The original Transformer used 6 encoder layers and 6 decoder layers, but modern models can use more or fewer layers depending on the problem.

You can imagine it like this:

<div align="center">
<img src="https://media.datacamp.com/legacy/v1704797298/image_199786868d.png" width="60%" />
<p>Image by the Datacamp</p>
</div>

Each layer helps the model understand the input and produce better output.

Now that we have a high-level idea of how Transformers are structured, we can look more closely at **what the encoder and decoder actually do** and how they process information.


---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/5557/5557844.png" width="80"/> Why use it?
Transformers are widely used because they:
- Scale efficiently with large datasets and model sizes  
- Enable parallel processing of tokens (unlike RNNs)  
- Capture long-term dependencies using self-attention  
- Generalize well across multiple modalities (text, images, audio)  
- Serve as a unified architecture for NLP, vision, and multimodal tasks  

---

## <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/7527/7527144.png" width="80"/> How it works?

This section explains how a Transformer works using two perspectives:
- a **high-level architectural view** (Encoder → Decoder)
- an **internal view** (what happens inside each part)

### High-Level View (Architecture)

A Transformer is made of three main ideas working together:

- Encoder → understands the input text
- Decoder → generates the output text
- Attention → connects words based on meaning and context

Together, these elements form the **Transformer model**.

```mermaid
graph LR
A[Input Text] --> B[Encoder]
B --> C[Encoded Meaning]
C --> D[Decoder]
D --> E[Output Text]

```

---

### Internal View (What Happens Inside Encoder & Decoder)


This is the inside view, which explains how the encoder and decoder work:

1. The input text is broken into smaller pieces called **tokens**  
2. Tokens are converted into numerical representations (**embeddings**) and combined with **positional information**  
3. **Attention** analyzes relationships between all tokens  
4. The results pass through **neural processing layers**  
5. Multiple layers refine the understanding step by step  
6. Final representations are used to generate outputs (for example, the next word)

```mermaid
graph LR
A[Input Tokens] --> B[Embeddings + Position Info]
B --> C[Self-Attention]
C --> D[Processing Layers]
D --> E[Final Output]
```

---

### Where does this happen?

- **Tokenization & Embeddings**  
  → Before and at the start of the **Encoder**

- **Attention & Processing Layers**  
  → Inside each **Encoder and Decoder layer**

- **Final Output Generation**  
  → Performed by the **Decoder**

---

### Putting Everything Together (Complete Mental Model)

```mermaid
graph LR
A[Input Text] --> B[Tokenization & Embeddings]
B --> C[Encoder - Attention + Layers]
C --> D[Decoder - Attention + Layers]
D --> E[Output Text]
```
---

#### Plain-Language Analogy

Think of a **human translator**:

- **Tokenization & Embeddings**  
  → Reading and recognizing words  

- **Encoder (Attention + Layers)**  
  → Understanding meaning and context  

- **Decoder (Attention + Layers)**  
  → Speaking or writing the translation  

- **Transformer**  
  → The complete translation system

---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/2299/2299623.png" width="80"/> Components
Key components of the Transformer architecture include:
- Token Embeddings  
- Positional Encoding  
- Multi-Head Self-Attention  
- Scaled Dot-Product Attention  
- Feed-Forward Neural Networks  
- Residual Connections  
- Layer Normalization  
- Encoder and Decoder Blocks  

---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/6404/6404564.png" width="80"/> Use Cases
Transformers are used in a wide range of applications, such as:
- Machine Translation  
- Text Summarization  
- Question Answering  
- Chatbots and Conversational AI  
- Code Generation  
- Speech Recognition  
- Image Captioning and Vision Transformers  

---

### <img src="https://cdn-icons-png.flaticon.com/512/2147/2147809.png" width="80"> Code/Notebook/Projects

- [Build transformer from Scratch](https://github.com/gil-son/language-ai-engineering-lab/tree/main/notebooks/02-Transformers)

---

### <img src="https://cdn-icons-png.flaticon.com/512/2956/2956457.png" width="80"> Contents
- [DataCamp - How Transformers Work](https://www.geeksforgeeks.org/nlp/natural-language-processing-overview)


---

### <img src="https://cdn-icons-png.flaticon.com/512/2112/2112889.png" width="80"> Videos

A few recommended resources to visualize:

<div align="center">
  <a href="https://www.youtube.com/watch?v=ZXiruGOCn9s&pp=ygUVaG93IHRyYW5zZm9ybWVycyB3b3Jr" target="_blank">
      <img width="640" height="360" src="https://i.ytimg.com/vi/ZXiruGOCn9s/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLCWjNC9IqYn1RlRNtOvomVTrl24IA"/>
  </a>
</div>

---

<div align="center">
  <a href="https://www.youtube.com/watch?v=zxQyTK8quyY" target="_blank">
      <img width="640" height="360" src="https://i.ytimg.com/vi/zxQyTK8quyY/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLAr1eNdTMk0XByj5tnHCuK969pG0w"/>
  </a>
</div>
