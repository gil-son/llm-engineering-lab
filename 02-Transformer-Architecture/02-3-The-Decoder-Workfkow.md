## 02. Transformer-Architecture

<div align="center">
  <table>
    <tr>
      <td align="center"><img src="https://gitlab.com/gil-son/useful-images-collection/-/raw/main/hi.png?ref_type=heads" width="80"/></td>
      <td align="center"><img src="https://gitlab.com/gil-son/useful-images-collection/-/raw/main/png/abc.png?ref_type=heads" width="80"/></td>
      <td align="center"><img src="https://gitlab.com/gil-son/useful-images-collection/-/raw/main/encode.png?ref_type=heads" width="80"/></td>
      <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/2582/2582078.png" width="80"/></td>
      <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/6062/6062146.png" width="80"/></td>
      <td align="center"><img src="https://cdn-icons-png.flaticon.com/512/10817/10817413.png" width="80"/></td>
    </tr>
  </table>
</div>

## 02.3 The Decoder Workflow

The decoder's role centers on crafting text sequences. Mirroring the encoder, the decoder is equipped with a similar set of sub-layers. It boasts two multi-headed attention layers, a pointwise feed-forward layer, and incorporates both residual connections and layer normalization after each sub-layer.

<div align="center">
<img src="https://media.datacamp.com/legacy/v1704797298/image_65c45ce7dc.png" width="60%" />
<p>Image by the Datacamp</p>
</div>

These components function in a way akin to the encoder's layers, yet with a twist: each multi-headed attention layer in the decoder has its unique mission.

The final of the decoder's process involves a linear layer, serving as a classifier, topped off with a softmax function to calculate the probabilities of different words.

The Transformer decoder has a structure specifically designed to generate this output by decoding the encoded information step by step.

It is important to notice that the decoder operates in an autoregressive manner, kickstarting its process with a start token. It cleverly uses a list of previously generated outputs as its inputs, in tandem with the outputs from the encoder that are rich with attention information from the initial input.

This sequential dance of decoding continues until the decoder reaches a pivotal moment: the generation of a token that signals the end of its output creation.

### STEP 1 - Output Embeddings

At the decoder's starting line, the process mirrors that of the encoder. Here, the input first passes through an embedding layer

### STEP 2 - Positional Encoding

Following the embedding, again just like the encoder, the input passes by the positional encoding layer. This sequence is designed to produce positional embeddings.

These positional embeddings are then channeled into the first multi-head attention layer of the decoder, where the attention scores specific to the decoder’s input are meticulously computed.

### STEP 3 - Stack of Decoder Layers

The decoder consists of a stack of identical layers (6 in the original Transformer model). Each layer has three main sub-components:


#### STEP 3.1 Masked Self-Attention Mechanism

This is similar to the self-attention mechanism in the encoder but with a crucial difference: it prevents positions from attending to subsequent positions, which means that each word in the sequence isn't influenced by future tokens.

For instance, when the attention scores for the word "are" are being computed, it's important that "are" doesn't get a peek at "you", which is a subsequent word in the sequence.

<div align="center">
<img src="https://media.datacamp.com/cms/google/be6yxuucrgpnfjvgi21jzqewdhhjnaok6imbc1jdoheihoowjyji0pl_maozswiujqy6pp-tssnq995ojj51q2zi_ruysl-abl89skblu4k89y54i5vhtcfwzryyhweobflq7hp7plr1myaybwai7ns.png" width="60%" />
<p>Image by the Datacamp</p>
</div>

This masking ensures that the predictions for a particular position can only depend on known outputs at positions before it.

#### STEP 3.2 - Encoder-Decoder Multi-Head Attention or Cross Attention

In the second multi-headed attention layer of the decoder, we see a unique interplay between the encoder and decoder's components. Here, the outputs from the encoder take on the roles of both queries and keys, while the outputs from the first multi-headed attention layer of the decoder serve as values.

This setup effectively aligns the encoder's input with the decoder's, empowering the decoder to identify and emphasize the most relevant parts of the encoder's input.

Following this, the output from this second layer of multi-headed attention is then refined through a pointwise feedforward layer, enhancing the processing further.

<div align="center">
<img src="https://media.datacamp.com/cms/google/82s2vzpkd8l-bvn5nzlyol98qr7yjcmieudlmn5qvgnofxo4eajw_vpvx-suwmitx4yiebkhyzztq6vmw15j_so_-xiwvc5_d76irx1hlhky4giknbx2pff9rxydcuv3akzvwhl-pvyn7b7eszul9n4.png" width="60%" />
<p>Image by the Datacamp</p>
</div>

In this sub-layer, the queries come from the previous decoder layer, and the keys and values come from the output of the encoder. This allows every position in the decoder to attend over all positions in the input sequence, effectively integrating information from the encoder with the information in the decoder.

#### STEP 3.3 Feed-Forward Neural Network

Similar to the encoder, each decoder layer includes a fully connected feed-forward network, applied to each position separately and identically.



### STEP 4 Linear Classifier and Softmax for Generating Output Probabilities

The journey of data through the transformer model culminates in its passage through a final linear layer, which functions as a classifier.

The size of this classifier corresponds to the total number of classes involved (number of words contained in the vocabulary). For instance, in a scenario with 1000 distinct classes representing 1000 different words, the classifier's output will be an array with 1000 elements.

This output is then introduced to a softmax layer, which transforms it into a range of probability scores, each lying between 0 and 1. The highest of these probability scores is key,its corresponding index directly points to the word that the model predicts as the next in the sequence.

<div align="center">
<img src="https://media.datacamp.com/legacy/v1704797298/image_b2142a5a0d.png" width="60%" />
<p>Image by the Datacamp</p>
</div>

#### Normalization and Residual Connections

Each sub-layer (masked self-attention, encoder-decoder attention, feed-forward network) is followed by a normalization step, and each also includes a residual connection around it.

#### Output of the Decoder

The final layer's output is transformed into a predicted sequence, typically through a linear layer followed by a softmax to generate probabilities over the vocabulary.

The decoder, in its operational flow, incorporates the freshly generated output into its growing list of inputs, and then proceeds with the decoding process. This cycle repeats until the model predicts a specific token, signaling completion.

The token predicted with the highest probability is assigned as the concluding class, often represented by the end token.

Again remember that the decoder isn't limited to a single layer. It can be structured with N layers, each one building upon the input received from the encoder and its preceding layers. This layered architecture allows the model to diversify its focus and extract varying attention patterns across its attention heads.

Such a multi-layered approach can significantly enhance the model’s ability to predict, as it develops a more nuanced understanding of different attention combinations.

And the final architecture is something similar like this (form the original paper)


<div align="center">
<img src="https://media.datacamp.com/legacy/v1704797298/image_7b08f474e7.png" width="60%" />
<p>Image by the Datacamp</p>
</div>

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
