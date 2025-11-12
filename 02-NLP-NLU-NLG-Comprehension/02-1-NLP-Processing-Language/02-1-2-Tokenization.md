# 2.1. NLP — Processing Language

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

## 2.1.2. Tokenization 🧩

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/7963/7963858.png" width="80"/> Introduction

---

Tokenization is the process of breaking text into smaller units — called **tokens** — which can be words, subwords, or characters.  
These tokens are the foundation of any Natural Language Processing (NLP) or Large Language Model (LLM) pipeline.

---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/5557/5557844.png" width="80"/> Why use it?
  
- Models cannot directly understand raw text — they operate on numerical representations.  
- Tokenization creates a **bridge** between human-readable language and machine-readable data.  
- Efficient tokenization improves training and inference speed.

---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/2299/2299623.png" width="80"/> Components

- **Tokenizer type** (Word, Subword, Character, Byte-Pair Encoding, SentencePiece)
- **Vocabulary** — the set of all tokens the model recognizes
- **Special tokens** (e.g., `[PAD]`, `[CLS]`, `[SEP]`, `<s>`, `</s>`)
- **Token IDs** — numerical identifiers assigned to tokens

---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/7527/7527144.png" width="80"/> How it works?

1. Input text is read as a raw string.  
2. Tokenizer splits text into words or subwords.  
3. Each token is mapped to an ID from the vocabulary.  
4. The model uses these IDs for training or inference.

#### Step-by-step Process

1. Input: `"I love NLP!"`
2. Tokenization: `["I", "love", "NLP", "!"]`
3. IDs: `[101, 1045, 2293, 17953, 999, 102]`
4. Model processes IDs → outputs prediction

#### Simple Diagram

```mermaid
graph TD
    A[Raw Text] --> B[Tokenizer]
    B --> C[Tokens]
    C --> D[IDs / Embeddings]
    D --> E[Model Input]
```

---

### <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/6404/6404564.png" width="80"/> Use Cases

- Preparing datasets for fine-tuning LLMs  
- Building chatbots and assistants  
- Preprocessing for translation or summarization  
- Enabling token-efficient inference in production

---

### <img src="https://cdn-icons-png.flaticon.com/512/6675/6675847.png" width="80"> Limitations

- Tokenizers trained on limited data may struggle with rare or multilingual words.  
- Different tokenization methods lead to inconsistencies across models.  
- Subword-level tokenization may break linguistic coherence.

---

### <img src="https://cdn-icons-png.flaticon.com/512/2147/2147809.png" width="80"> Code/Notebook/Projects

- [Create an LLM from scratch](https://github.com/gil-son/llm-engineering-lab/tree/main/notebooks/01-transformer-lm)

---

### <img src="https://cdn-icons-png.flaticon.com/512/2112/2112889.png" width="80"> Videos

[In the soon]
