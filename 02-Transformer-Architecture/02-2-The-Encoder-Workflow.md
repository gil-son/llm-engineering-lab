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

## 02.2 The Encoder Workflow

The encoder is a fundamental component of the Transformer architecture. Its primary role is to transform a sequence of input tokens into contextualized representations. Unlike earlier NLP models that processed words mostly in isolation, the Transformer encoder allows each token to be interpreted in relation to every other token in the sequence.

A Transformer encoder does not treat a word as a fixed dictionary entry. Instead, it converts each token into a context-aware meaning vector — a numerical representation that reflects not only the word itself, but also how it is being used in the sentence.

Consider the sentence:

> “The bank raised interest rates.”

The token **“bank”** is ambiguous when viewed alone. It could refer to:

- a financial institution
- the side of a river

At the embedding level, the token "bank" starts with a generic vector that represents all of its possible meanings.

| Token      | How it influences “bank” |
| ---------- | ------------------------ |
| *the*      | signals a noun           |
| *raised*   | implies an actor         |
| *interest* | strongly financial       |
| *rates*    | confirms finance domain  |


Its structure composition consists as follows:


<div align="center">
<img src="https://media.datacamp.com/legacy/v1704797298/image_3aa5aef3db.png" width="60%" />
<p>Image by the Datacamp</p>
</div>

So let’s break its workflow into its most basic steps:

### STEP 1 - Input Embeddings

The embedding only happens in the bottom-most encoder. The encoder begins by converting input tokens - words or subwords - into vectors using embedding layers. These embeddings capture the semantic meaning of the tokens and convert them into numerical vectors.

All the encoders receive a list of vectors, each of size 512 (fixed-sized). In the bottom encoder, that would be the word embeddings, but in other encoders, it would be the output of the encoder that’s directly below them.

<div align="center">
<img src="https://media.datacamp.com/cms/google/bxt-22k9uk5i0y0deewtnedhcteoppv0uzng7cbp47gtukb5gnomnbw_jl7ll9012twgpdsgfkb0peouhad_c3ku9yxlczuq6z_eo2miiagvdhaph_5_zxs4nib2j6saa9d0if7r8qw9s_qi1mxooxu.png" width="60%" />
<p>Image by the Datacamp</p>
</div>

### STEP 2 - Positional Encoding

Since Transformers do not have a recurrence mechanism like RNNs, they use positional encodings added to the input embeddings to provide information about the position of each token in the sequence. This allows them to understand the position of each word within the sentence.

To do so, the researchers suggested employing a combination of various sine and cosine functions to create positional vectors, enabling the use of this positional encoder for sentences of any length.

In this approach, each dimension is represented by unique frequencies and offsets of the wave, with the values ranging from -1 to 1, effectively representing each position.

<div align="center">
<img src="https://media.datacamp.com/cms/google/aa6uuy3t-iknfuwcguorfwsud60oza4ptjuotfmk0ce1p1pp_o-dr0k8dxqubp4xfk7yme8vx3tlliorja-afownqyoeggkxey3nv0arqyrwnwpeqzyx0dsyavjdodgysmonaxryhwcqf0b-in1zkki.png" width="60%" />
<p>Image by the Datacamp</p>
</div>

### STEP 3 - Stack of Encoder Layers

The Transformer encoder consists of a stack of identical layers (6 in the original Transformer model).

The encoder layer serves to transform all input sequences into a continuous, abstract representation that encapsulates the learned information from the entire sequence. This layer comprises two sub-modules:

A multi-headed attention mechanism.
A fully connected network.
Additionally, it incorporates residual connections around each sublayer, which are then followed by layer normalization.

<div align="center">
<img src="https://media.datacamp.com/cms/google/up1zbwza3irkfxqsidxaeovuq7wruaxbfne0z6orvezle0hkvwrs59nf7zoxj-anzmzkpiuc9hodoc7vwq8z7w14x7fvbaiki_oqqla4viortfyrap3tf9tpp41x4ucim1wi2lfg_wefzg4v5qk-ma4.png" width="60%" />
<p>Image by the Datacamp</p>
</div>



#### 3.1 Multi-Headed Self-Attention Mechanism


In the encoder, the multi-headed attention utilizes a specialized attention mechanism known as **self-attention**. This approach enables the models to relate each word in the input with other words. For instance, in a given example, the model might learn to connect the word “are” with “you”.


This mechanism allows the encoder to focus on different parts of the input sequence as it processes each token. It computes attention scores based on:

- A **query is a vector that represents a specific word or token** from the input sequence in the attention mechanism.

- A **key is also a vector in the attention mechanism**, corresponding to each word or token in the input sequence.

- Each value is associated with a key and is used to construct the output of the attention layer. **When a query and a key match well, which basically means that they have a high attention score**, the corresponding value is emphasized in the output.

This **first Self-Attention** module **enables the model to capture contextual information** from the **entire sequence**. Instead of performing a single attention function, queries, keys and values are **linearly projected h times**. On each of these projected **versions of queries**, keys and values the **attention mechanism is performed in parallel**, yielding h-dimensional output values.

The detailed architecture goes as follows:


<div align="center">
<img src="https://media.datacamp.com/legacy/v1704797299/image_542a27c68b.png" width="60%" />
<p>Image by the Datacamp</p>
</div>

##### Matrix Multiplication (MatMul) - Dot Product of Query and Key

Once the query, key, and value vectors are passed through a linear layer, a dot product matrix multiplication is performed between the queries and keys, resulting in the creation of a score matrix.

The score matrix establishes the degree of emphasis each word should place on other words. Therefore, each word is assigned a score in relation to other words within the same time step. A higher score indicates greater focus.

This process effectively maps the queries to their corresponding keys.

<div align="center">
<img src="https://media.datacamp.com/legacy/v1704797298/image_381d380e59.png" width="60%" />
<p>Image by the Datacamp</p>
</div>

##### Reducing the Magnitude of attention scores

The scores are then scaled down by dividing them by the square root of the dimension of the query and key vectors. This step is implemented to ensure more stable gradients, as the multiplication of values can lead to excessively large effects.


<div align="center">
<img src="https://media.datacamp.com/legacy/v1704797298/image_0ad7c66d5f.png" width="60%" />
<p>Image by the Datacamp</p>
</div>

##### Applying Softmax to the Adjusted Scores

Subsequently, a softmax function is applied to the adjusted scores to obtain the attention weights. This results in probability values ranging from 0 to 1. The softmax function emphasizes higher scores while diminishing lower scores, thereby enhancing the model's ability to effectively determine which words should receive more attention.

<div align="center">
<img src="https://media.datacamp.com/legacy/v1704797298/image_d992490cc2.png" width="60%" />
<p>Image by the Datacamp</p>
</div>

##### Combining Softmax Results with the Value Vector

The following step of the attention mechanism is that weights derived from the softmax function are multiplied by the value vector, resulting in an output vector.

In this process, only the words that present high softmax scores are preserved. Finally, this output vector is fed into a linear layer for further processing.


<div align="center">
<img src="https://media.datacamp.com/legacy/v1704797297/image_205dd62af2.png" width="60%" />
<p>Image by the Datacamp</p>
</div>


And we finally get the output of the Attention mechanism!

So, you might be wondering why it’s called Multi-Head Attention?

Remember that before all the process starts, we break our queries, keys and values h times. This process, known as self-attention, happens separately in each of these smaller stages or 'heads'. Each head works its magic independently, conjuring up an output vector.

This ensemble passes through a final linear layer, much like a filter that fine-tunes their collective performance. The beauty here lies in the diversity of learning across each head, enriching the encoder model with a robust and multifaceted understanding.


#### 3.2 Normalization and Residual Connections

Each sub-layer in an encoder layer is followed by a normalization step. Also, each sub-layer output is added to its input (residual connection) to help mitigate the vanishing gradient problem, allowing deeper models. This process will be repeated after the Feed-Forward Neural Network too.

<div align="center">
<img src="https://media.datacamp.com/legacy/v1704797297/image_c4cd3b7050.png" width="60%" />
<p>Image by the Datacamp</p>
</div>


#### 3.3 Feed-Forward Neural Network

The journey of the normalized residual output continues as it navigates through a pointwise feed-forward network, a crucial phase for additional refinement.

Picture this network as a duo of linear layers, with a ReLU activation nestled in between them, acting as a bridge. Once processed, the output embarks on a familiar path: it loops back and merges with the input of the pointwise feed-forward network.

This reunion is followed by another round of normalization, ensuring everything is well-adjusted and in sync for the next steps.


<div align="center">
<img src="https://media.datacamp.com/cms/google/vlhrn8ils_st_zi2idnmbnilodyakp_cgknbhacy_b-pscedygvsghbfpjbcfmsubjqapd2jnzyfickxqlix8p-omrzlmbdqujvpjc-filrllkj7e4yng0kijtrtm2cey9vouyk1p_lqbjjdgtxrpx4.png" width="60%" />
<p>Image by the Datacamp</p>
</div>

#### STEP 4 - Output of the Encoder

The output of the final encoder layer is a set of vectors, each representing the input sequence with a rich contextual understanding. This output is then used as the input for the decoder in a Transformer model.

This careful encoding paves the way for the decoder, guiding it to pay attention to the right words in the input when it's time to decode.

Think of it like building a tower, where you can stack up N encoder layers. Each layer in this stack gets a chance to explore and learn different facets of attention, much like layers of knowledge. This not only diversifies the understanding but could significantly amplify the predictive capabilities of the transformer network.

---

### <img src="https://cdn-icons-png.flaticon.com/512/2147/2147809.png" width="80"> Code/Notebook/Projects

- [Build transformer from Scratch](https://github.com/gil-son/language-ai-engineering-lab/tree/main/notebooks/02-Transformers)
- [Building a transformer with Pytorch](https://www.datacamp.com/tutorial/building-a-transformer-with-py-torch)

---

### <img src="https://cdn-icons-png.flaticon.com/512/2956/2956457.png" width="80"> Contents
- [DataCamp - How Transformers Work](https://www.datacamp.com/tutorial/how-transformers-work)


---

### <img src="https://cdn-icons-png.flaticon.com/512/2112/2112889.png" width="80"> Videos

A few recommended resources to visualize:

<div align="center">
  <a href="https://www.youtube.com/watch?v=zxQyTK8quyY" target="_blank">
      <img width="640" height="360" src="https://i.ytimg.com/vi/zxQyTK8quyY/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLAr1eNdTMk0XByj5tnHCuK969pG0w"/>
  </a>
</div>


