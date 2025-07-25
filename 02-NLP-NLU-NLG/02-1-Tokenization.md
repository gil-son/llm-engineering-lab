# 02-1-Tokenization

# What is Tokenization?

<div align="center">
  <img src="https://thumbs2.imgbox.com/32/19/hjPPYYNR_t.jpg" width="40%">
</div>
<br/>

**Tokenization** is the process of breaking down text into smaller units called **tokens**. These tokens are the building blocks that Large Language Models (LLMs) process and understand. Depending on the tokenizer used, tokens can be words, subwords, or even characters.

For LLMs, tokenization is a crucial first step that transforms raw human language into a numerical format that the model can process. Without tokenization, the model would not be able to comprehend the structure or meaning of input text.

---

<details><summary> <h3><a href="#"><img src="https://cdn-icons-png.flaticon.com/512/4133/4133589.png" width="5%"></a>Why is tokenization necessary?</h3></summary>

Tokenization is critical for several reasons:

- **Preprocessing**: Converts raw text into manageable units that a model can process.
- **Vocabulary Mapping**: Assigns each token an ID using a vocabulary.
- **Efficiency**: Subword-based tokenization reduces the vocabulary size and handles unknown words.
- **Consistency**: Ensures standardized input representation across different samples.

</details>

---

<details><summary><h3><a href="#"><img src="https://cdn-icons-png.flaticon.com/512/2833/2833807.png" width="5%"></a>How does tokenization work?</h3></summary>

Tokenization involves a few important steps:

1. **Input Text**
   - Example: `"Transformers are powerful."`

2. **Split into Tokens**
   - Tokenizer splits text into smaller parts.
   - Word-level: `["Transformers", "are", "powerful", "."]`
   - Subword-level (e.g., BPE): `["Transform", "ers", "are", "power", "ful", "."]`

3. **Map Tokens to IDs**
   - Each token is mapped to a unique ID in the vocabulary.
   - Example: `"Transformers"` → `37429`, `"are"` → `793`

4. **Feed into Model**
   - The sequence of token IDs is passed to the model for further processing.

---

### Visual Example

```text
Input Text:       "I love transformers!"
Tokens:           ["I", "love", "transform", "ers", "!"]
Token IDs:        [40, 567, 12098, 390, 0]
```

</details>

---

<details><summary><h3><a href="#"><img src="https://cdn-icons-png.flaticon.com/512/3588/3588592.png" width="5%"></a>Types of Tokenizers</h3></summary>

There are several types of tokenizers used in LLMs:

- **Whitespace Tokenizer**: Splits text based on spaces. Not robust for NLP tasks.
- **WordPiece**: Breaks down rare words into subword units. Used in BERT.
- **Byte Pair Encoding (BPE)**: Merges frequent character pairs. Used in GPT models.
- **Unigram**: Selects the most probable subword units based on a statistical model. Used in SentencePiece.
- **Character-Level**: Breaks text into single characters. Rare but useful for small vocabularies.

Each tokenizer balances vocabulary size, coverage, and efficiency.

</details>

---

<details><summary><h3><a href="#"><img src="https://cdn-icons-png.flaticon.com/512/1705/1705312.png" width="5%"></a>What are special tokens?</h3></summary>

Special tokens have specific purposes in LLMs:

- `<pad>`: Used to pad sequences to the same length.
- `<bos>` / `<s>`: Beginning of sentence token.
- `<eos>` / `</s>`: End of sentence token.
- `<unk>`: Unknown token for rare or out-of-vocabulary words.
- `<cls>`, `<sep>`: Used in BERT for classification and separating segments.

These tokens help guide the model's understanding of structure and context.

</details>

---


<details><summary><h3><a href="#"><img src="https://cdn-icons-png.flaticon.com/512/954/954591.png" width="5%"></a> How many tokens my input has?</h3></summary>

You can count tokens using tools like:

- **OpenAI Tokenizer**: [https://platform.openai.com/tokenizer](https://platform.openai.com/tokenizer)
- **Hugging Face Tokenizer**: Use `tokenizer.encode()` in Python
- **tiktoken** (OpenAI’s tokenizer library)

💡 **Tip**: The number of tokens is not equal to the number of words. For example:

```text
Text: "ChatGPT is amazing!"
Tokens: ["Chat", "G", "PT", " is", " amazing", "!"]
Token Count: 6
```

</details>

---

<details><summary><h3><a href="#"><img src="https://cdn-icons-png.flaticon.com/512/2965/2965363.png" width="5%"></a> Videos</h3></summary>
  <div align="center">
    <a href="https://www.youtube.com/watch?v=OjrGu0L5K7M" target="_blank">
        <img width="640" height="360" src="https://i.ytimg.com/vi_webp/OjrGu0L5K7M/maxresdefault.webp"/>
    </a>
    
  </div>
  <hr/>
  <div align="center">
    <a href="https://www.youtube.com/watch?v=zduSFxRajkE" target="_blank">
        <img width="640" height="360" src="https://i.ytimg.com/vi/zduSFxRajkE/maxresdefault.jpg"/>
    </a>
  </div>
  
  
</details>
