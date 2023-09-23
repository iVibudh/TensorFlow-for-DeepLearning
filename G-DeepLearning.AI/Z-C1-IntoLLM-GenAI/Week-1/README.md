# Generative AI with Large Language Models

This course will take a deep dive with you into how LLM technology actually works including going through many of the technical details, like model training, instruction tuning, fine-tuning, etc.

- Week 1: examine the transformer architecture that powers large language models, explore how these models are trained, and understand the compute resources required to develop these powerful LLMs. You'll also learn about a technique called in-context learning. How to guide the model to output at inference time with prompt engineering, and how to tune the most important generation parameters of LLMs for tuning your model output. 
- Lab 1: construct a compare different prompts and inputs for a given generative task, in this case, dialogue summarization. You'll also explore different inference parameters and sampling strategies to gain intuition on how to further improve the generative model of responses.
- Week 2: explore options for adapting pre-trained models to specific tasks and datasets via a process called instruction fine tuning. 
- Lab 2: fine tune it existing large language model from Hugging Face, a popular open-source model hub. You'll play with both full fine-tuning and parameter efficient fine tuning or PEFT for short. You'll see how PEFT lets you make your workflow much more efficient.
- Week 3: to align the output of language models with human values in order to increase helpfulness and decrease potential harm and toxicity. 
- Lab 3: hands-on with reinforcement learning from human feedback or RLHF, you'll build a reward model classifier to label model responses as either toxic or non-toxic.

### Week 1

#### Introduction to LLMs and generative AI projects


###### Transformers
- **Architecture of a Encode/Decoder from a transformer model**
    - Words are **tokenized** - represent as vectors
    - Tokens are converted to **vector embedding**. These vectors learn to encode the meaning and context of individual vectors
    - You add the positional encoding of these vector embeddings for each word. This generates **positional embedding vectors.**
    - The model processes **each of the input tokens in parallel.** 
    - You pass it to the **self-attention layer**. Here, the model analyzes the relationships between the tokens in your input sequence. As you saw earlier, this allows the model to attend to different parts of the input sequence to better capture the contextual dependencies between the words.
        - The self-attention weights that are learned during **training** and stored in these layers reflect the importance of each word in that input sequence to all other words in the sequence.
        - But this does not happen just once, the transformer architecture actually has **multi-headed self-attention.** This means that multiple sets of self-attention weights or heads are learned in parallel independently of each other. (12 to 100 heads in a model)
        -  The intuition here is that each self-attention head will learn a different **aspect of language**. 
    -  All of the attention weights have been applied to your input data, the output is processed through a **fully-connected feed-forward network.**
        - The output of this layer is a vector of logits proportional to the **probability score** for each and every token in the tokenizer dictionary.
    - You can then pass these logits to a final **softmax layer**, where they are normalized into a probability score for each word.

<br> <br> <br>
Generating Text - **Decoder** role in translation (seq-to-seq)
    - Pass in through the encoder 
    - the data that leaves the encoder is a deep representation of the **structure and meaning** of the input sequence. This representation is inserted into the middle of the decoder to influence the decoder's self-attention mechanisms.
    - Then **input sequence token** is added to the input of the decoder.
    - The output of the decoder's self-attention layers gets passed through the decoder feed-forward network and through a final softmax output layer. To **generate first token**
    - Token to word

<br> <br> <br>
- Encoder only models: (seq to seq) less common
    -  the input sequence and the output sequence or the same length
    - add additional layers to the architecture, you can train encoder-only models to perform classification tasks. eg BERT, RoBERTA
    - Encoder-only models are also known as Autoencoding models, and they are pre-trained using masked language modeling. Here, tokens in the input sequence or randomly mask, and the training objective is to predict the mask tokens in order to reconstruct the original sentence. This is also called a denoising objective.
- Encoder-Decoder model: (seq to seq)
    - the input sequence and the output sequence can be of different lengths
    - You can also scale and train this type of model to perform general text generation tasks. eg. BART
- Decoder only: (seq to seq)) most popular
    - the input sequence and the output sequence can be of different lengths.
    - Popular decoder-only models include the GPT family of models, GPT, BLOOM, Jurassic, LLaMA, and many more.
    - Decoder-based autoregressive models, mask the input sequence and can only see the input tokens leading up to the token in question. The model has no knowledge of the end of the sentence. The model then iterates over the input sequence one by one to predict the following token. In contrast to the encoder architecture, this means that the context is unidirectional. By learning to predict the next token from a vast number of examples, the model builds up a statistical representation of language. Models of this type make use of the decoder component off the original architecture without the encoder. Decoder-only models are often used for text generation, although larger decoder-only models show strong zero-shot inference abilities, and can often perform a range of tasks well. 

<br> <br> <br>

Ref-> [Transformer paper](https://arxiv.org/abs/1706.03762) 

<br> <br> <br>
#### Generative configuration

- Configuration parameters influence model output during inference, including max new tokens, controlling output length.
- Large language models operate with greedy decoding by default, choosing the word with the highest probability.
Random sampling introduces variability, reducing the likelihood of word repetition.
- Top k and top p settings limit random sampling, promoting sensible output.
    - Top k restricts choices to k tokens with the highest probability, reducing randomness in text generation.
    - Top p limits sampling to predictions below a combined probability threshold, balancing variability and sensibility.
- Temperature parameter influences the probability distribution of the next token, controlling randomness in text generation.
- Higher temperature values increase randomness, while lower values concentrate probability on likely words, resulting in less randomness.
- Default temperature value of one maintains unaltered probability distribution for text generation.

<br> <br> <br>

## References
**Transformer Architecture**
- [Attention is all you need](https://arxiv.org/pdf/1706.03762.pdf)
- [BLOOM: BigScience 176B Model](https://arxiv.org/abs/2211.05100)
- Coursera's [Vector Space Models](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/home/week/3)

**Pre-training and scaling laws**
- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361)

**Model architectures and pre-training objectives**
- [What Language Model Architecture and Pretraining Objective Work Best for Zero-Shot Generalization?](https://arxiv.org/pdf/2204.05832.pdf) The paper examines modeling choices in large pre-trained language models and identifies the optimal approach for zero-shot generalization.
- [HuggingFace Tasks](https://huggingface.co/tasks) and [Model Hub](https://huggingface.co/models): Collection of resources to tackle varying machine learning tasks using the HuggingFace library.
- [LLaMA: Open and Efficient Foundation Language Models] (https://arxiv.org/pdf/2302.13971.pdf) Article from Meta AI proposing Efficient LLMs (their model with 13B parameters outperform GPT3 with 175B parameters on most benchmarks)
- [Llama 2: Open Foundation and Fine-Tuned Chat Models](https://arxiv.org/abs/2307.09288)

**Scaling laws and compute-optimal models**
- [Language Models are Few-Shot Learners](https://arxiv.org/pdf/2005.14165.pdf) - This paper investigates the potential of few-shot learning in Large Language Models.

- [Training Compute-Optimal Large Language Models](https://arxiv.org/pdf/2203.15556.pdf) - Study from DeepMind to evaluate the optimal model size and number of tokens for training LLMs. Also known as “Chinchilla Paper”.

- [BloombergGPT: A Large Language Model for Finance](https://arxiv.org/pdf/2303.17564.pdf) - LLM trained specifically for the finance domain, a good example that tried to follow chinchilla laws.


