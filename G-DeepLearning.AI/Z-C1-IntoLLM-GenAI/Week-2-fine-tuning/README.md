# Generative AI with Large Language Models



### Week 2 - Fine-tuning LLMs with instruction

#### Instruction fine-tuning (or Fine-tuning)
(Fine-tuning an LLM with instruction prompts)
fine-tuning is a supervised learning process where you use a data set of labeled examples to update the weights of the LLM.

There are three ways to improve model response:
- In-context learning(ICL) - zero shot inference
- One-shot or Few-shot inference
    - Drawbacks
        - may not work for smaller LLM models
        - examples take up space in the context window
- **Fine tuning**
    - fine-tuning with labeled examples to update the weights of the LLM.
    - The labeled examples are prompt completion pairs, the fine-tuning process extends the training of the model to improve its ability to generate good completions for a specific task.
    -  Instruction fine-tuning, where all of the model's weights are updated is known as **full fine-tuning.**
    
Steps to perform fine tuning:
    - Prepare the dataset:
        - convert the data (usually tabular) and turn them into **instruction prompt datasets**. 
        - You may use different Prompt template libraries for different tasks (eg. Classification, Text generation, and summarization)
    - Training Splits:
        - Divind the dataset into training, validation and test splits. 
    - Fine-tuning:
        - Select prompts from your training data set and pass them to the LLM to generate completions. (y-predicted)
        - compare LLM response with the label data (y-true)
        - compare the distribution of the completion (y-predicted) and that of the training label (y-true) and use the standard **crossentropy function to calculate loss between the two token distribution**
        - then use the calculated loss to update your model weights in standard backpropagation. 
        - You'll do this for many batches of prompt completion pairs and over several epochs, update the weights so that the model's performance on the task improves.
        -  you can define separate evaluation steps to measure your LLM performance using the holdout validation data set. **(Validation accuracy)**
    - Evaluation 
        -  after you've completed your fine tuning, you can perform a final performance evaluation using the holdout test data set.**(Test accuracy)**
    - Result
        - The fine-tuning process results in **a new version of the base model**, often called an instruct model that is better at the tasks you are interested in. 

#### Fine-tuning on a single task
- Fine-tuning on a single task.  Often just **500-1,000 examples** can result in good performance in contrast to the billions of pieces of texts that the model saw during pre-training. 
- **Catastrophic forgetting**
    - Catastrophic forgetting happens because the full fine-tuning process modifies the weights of the original LLM. While this leads to great performance on the single fine-tuning task, it can degrade performance on other tasks.
- How to avoid Catastrophic forgetting?
    - First of all, it's important to decide whether catastrophic forgetting actually impacts your use case or not.
    - First, if you do want or need the model to maintain its multitask generalized capabilities, you can **perform fine-tuning on multiple tasks at one time**.
    - Second, perform **Parameter Efficient Fine-tuning (or PEFT)**. Instead of full fine-tuning, PEFT is a set of techniques that preserves the weights of the original LLM and trains only a small number of task-specific adapter layers and parameters. PEFT shows greater robustness to catastrophic forgetting since most of the pre-trained weights are left unchanged. PEFT is an exciting and active area of research that we will cover later this week. 
- Quiz:
    - [True] Catastrophic forgetting is a common problem in machine learning, especially in deep learning models.
    - [True] One way to mitigate catastrophic forgetting is by using regularization techniques to limit the amount of change that can be made to the weights of the model during training.
    - [True] Catastrophic forgetting occurs when a machine learning model forgets previously learned information as it learns new information.
    - [False] Catastrophic forgetting only occurs in supervised learning tasks and is not a problem in unsupervised learning.


#### Multi-task instruction fine-tuning
- the training dataset is comprised of example inputs and outputs for a variety of tasks (such as summarization, rating, translation, entity recognition, etc.)
- You train the model on this mixed dataset so that you can improve the performance of the model on all the tasks simultaneously, thus avoiding the issue of catastrophic forgetting. 
- One drawback to multitask fine-tuning is that it **requires a lot of data (50,000 - 100,000 examples)** <br><br><br>

- Let's take a look at one family of models that have been trained using multitask instruction fine-tuning. Instruct model variance differ based on the datasets and tasks used during fine-tuning. **Fine-tuned language net (or FLAN) family**.  
- Because they're FLAN fine-tuning is the last step of the training process the authors of the original paper called it the metaphorical dessert to the main course of pre-training.
    - FLAN-T5
    - FLAN-PALM 
- FLAN-T5 is a great general purpose instruct model. In total, it's been fine tuned on 473 datasets across 146 task categories. 
    - a prompt dataset used for summarization tasks in FLAN-T5 is SAMSum. It's part of the muffin collection of tasks and datasets. (summarize dialogues)
    - dialogsum - This is a support chat that is typical of the examples in the dialogsum dataset. The conversation is between a customer and a staff member at a hotel check-in desk. The chat has had a template applied so that the instruction to summarize the conversation is included at the start of the text.

#### Evaluation Metrics 

- Exploring metrics to assess model performance in large language models.

- Challenges in Language Model Evaluation:
    - non-deterministic output and language nuances.
    - Difficulty in measuring similarity and meaning in sentences.
<br><br>
Key Evaluation Metrics 

- **ROUGE (Recall-Oriented Understudy for Gisting Evaluation)** for Summary:
    - Measures quality of automatically generated summaries compared to human-generated reference summaries.
    - ROUGE-1 focuses on individual words (unigrams).
    - ROUGE-2 considers pairs of words (bigrams).
    - ROUGE-L considers longest common subsequences. 
    - Challenges in ROUGE: simple metrics can lead to deceptive scores. 
    - Calculate recall, precision, and F1 score for unigrams and bigrams.
    - Addressing limitations and ways to counter them, such as using clipping functions.
- **BLEU (Bilingual Evaluation Understudy)** for Translation:
    - Evaluates machine-translated text by comparing it to human-generated translations.
    - Scores calculated for a range of n-gram sizes (unigrams, bigrams, etc.).
    - BLEU score closer to 1 indicates better translation quality.
- Comparison and Usage
    - ROUGE and BLEU are widely used and relatively low-cost metrics.
    - ROUGE for summarization tasks, BLEU for translation tasks.
    - Use caution when interpreting scores; consider the context and task-specific relevance.
    - These metrics are useful but should be supplemented with comprehensive evaluation benchmarks for a thorough model performance assessment.

#### Benchmarks
Evaluating LLMs beyond simple metrics like rouge and blur scores
- Use existing benchmark datasets and leaderboards
    - Select datasets that isolate specific skills (e.g. reasoning) and risks (e.g. toxicity)
    - Use data the model hasn't seen during training
- Examples of benchmark suites
    - GLUE (General Language Understanding Evaluation)
        - Tasks like sentiment analysis and QA
    - SuperGLUE
        - More challenging versions of GLUE tasks
        - New tasks like multi-sentence reasoning
    - MMLU (Massive Multitask Language Understanding)
        - Tests world knowledge and problem solving
        - Wide range of subjects like math, law, etc.
    - BIG-bench
        - 204 diverse tasks testing capabilities
        - Multiple sizes to control compute costs
    - HELM (Holistic Evaluation of Language Models)
        - Multimetric approach with 7 metrics
        - Assesses beyond just accuracy
            - Fairness, bias, toxicity
        - Evolving benchmark
- Importance of comprehensive evaluation
    - Matching human performance on benchmarks ≠ human level intelligence
    - Ongoing "arms race" between benchmarks and model capabilities
    - Need transparency on model strengths and weaknesses
    - Enable selection of right model for specific tasks

# Parameter efficient fine-tuning (PEFT)

#### PEFT
- Full fine tuning 
    - Model weights for the LLMs can be 12-20 times larger that the Model Training Weights. 
    - Additional Memory allocation is needed for optimizer states, gradients, forward activations, and temporary memory during training.
    -  Full fine-tuning results in a new version of the model for every task you train on. Each of these is the same size as the original model, so it can create an expensive storage and deploymenmt problem if you're fine-tuning for multiple tasks. 
- In contrast to full fine-tuning where every model weight is updated during supervised learning, parameter efficient fine tuning methods only update a small subset of parameters.
    - With PEFT, most if not all of the LLM weights are kept frozen. As a result, the number of trained parameters is much smaller than the number of parameters in the original LLM. In some cases, just 15-20% of the original LLM weights. This makes the memory requirements for training much more manageable.
    - Also, less prone to catastrophic forgetting problems of full fine-tuning.
    - The PEFT weights are trained for each task and can be easily swapped out for inference, allowing efficient adaptation of the original model to multiple tasks. Less Storage footprint. 
- **PEFT Methods**
There are several methods you can use for parameter efficient fine-tuning, each with trade-offs on parameter efficiency, memory efficiency, training speed, model quality, and inference costs.
    - **1. Selective**: 
        - fine-tune only a subset of the original LLM parameters. 
        - There are several approaches that you can take to identify which parameters you want to update. You have the option to train only certain components of the model or specific layers, or even individual parameter types. 
        - Researchers have found mixed performance and there are significant trade-offs between parameter efficiency and compute efficiency. 
    - **2. Reparameterization** :
        - It also work with the original LLM parameters, but reduce the number of parameters to train by creating new low rank transformations of the original network weights. 
        - A commonly used technique of this type is **LoRA**
    - **3. Additive Methods** : 
        - additive methods carry out fine-tuning by keeping all of the original LLM weights frozen and introducing new trainable components. 
        - Here there are two main approaches:
            - **Adapter methods** add new trainable layers to the architecture of the model, typically inside the encoder or decoder components after the attention or feed-forward layers. 
            - **Soft prompt methods**, on the other hand, keep the model architecture fixed and frozen, and focus on manipulating the input to achieve better performance. 
                - **Prompt Tuning** This can be done by adding trainable parameters to the prompt embeddings or keeping the input fixed and retraining the embedding weights. 

#### PEFT techniques 1: LoRA (Low-rank Adaptation)
It is a parameter-efficient fine-tuning technique that falls into the re-parameterization category.
- Transformers recap: 
    - The input prompt is turned into tokens, which are then converted to embedding vectors and passed into the encoder and/or decoder parts of the transformer. In both of these components, there are two kinds of neural networks; self-attention and feedforward networks. The weights of these networks are learned during pre-training. 
    - After the embedding vectors are created, they're fed into the self-attention layers where a series of weights are applied to calculate the attention scores. During full fine-tuning, every parameter in these layers is updated.
- LoRA is a strategy that reduces the number of parameters to be trained during fine-tuning by freezing all of the original model parameters and then injecting a pair of rank decomposition matrices alongside the original weights.
- The dimensions of the smaller matrices are set so that their product is a matrix with the same dimensions as the weights they're modifying. 
- You then keep the original weights of the LLM frozen and train the smaller matrices using the same supervised learning process you saw earlier this week.
- For inference, the two low-rank matrices are multiplied together to create a matrix with the same dimensions as the frozen weights. You then add this to the original weights and replace them in the model with these updated values. You now have a LoRA fine-tuned model that can carry out your specific task.
- You then add this to the original weights and replace them in the model with these updated values. 
- You now have a LoRA fine-tuned model that can carry out your specific task.
- Researchers have found that applying LoRA to just the self-attention layers of the model is often enough to fine-tune for a task and achieve performance gains. 
- **How to choose the LoRA rank?** 
    - ranks in the range of 4-32 can provide you with a good trade-off between reducing trainable parameters and preserving performance.
    - Optimizing the choice of rank is an ongoing area of research and best practices may evolve as more practitioners like you make use of LoRA.

#### PEFT techniques 2: Soft prompts
**Prompt tuning is NOT prompt engineering!**

- With **prompt tuning**, you add additional trainable tokens to your prompt and leave it up to the supervised learning process to determine their optimal values. 
- The set of trainable tokens is called a soft prompt, and it gets prepended to embedding vectors that represent your input text. 
- The soft prompt vectors have the same length as the embedding vectors of the language tokens. And including somewhere between 20 and 100 virtual tokens can be sufficient for good performance. 
- The tokens that represent natural language are hard in the sense that they each correspond to a fixed location in the embedding vector space. However, the soft prompts are not fixed discrete words of natural language. Instead, you can think of them as virtual tokens that can take on any value within the continuous multidimensional embedding space.
-  with prompt tuning, the weights of the large language model are frozen and the underlying model does not get updated. Instead, the embedding vectors of the soft prompt gets updated over time to optimize the model's completion of the prompt. 
- Prompt tuning is a very parameter efficient strategy because only a few parameters are being trained. In contrast with the millions to billions of parameters in full fine tuning, similar to what you saw with LoRA.
- You can train a different set of soft prompts for each task and then easily swap them out at inference time.
- And once models have around 10 billion parameters, prompt tuning can be as effective as full fine tuning and offers a significant boost in performance over prompt engineering alone.
- **Explainability of Soft Prompts** Because the soft prompt tokens can take any value within the continuous embedding vector space. The trained tokens don't correspond to any known token, word, or phrase in the vocabulary of the LLM. However, an analysis of the nearest neighbor tokens to the soft prompt location shows that they form tight semantic clusters. However, the words closest to the soft prompt tokens have similar meanings.
- you can also combine LoRA with the quantization techniques you learned about in week 1 to further reduce your memory footprint. This is known as QLoRA in practice, PEFT is used heavily to minimize compute and memory resources.

# Readings
##### Multi-task, instruction fine-tuning
- [Scaling Instruction-Finetuned Language Models](https://arxiv.org/pdf/2210.11416.pdf) Scaling fine-tuning with a focus on task, model size and chain-of-thought data.

- [Introducing FLAN: More generalizable Language Models with Instruction Fine-Tuning](https://blog.research.google/2021/10/introducing-flan-more-generalizable.html) This blog (and article) explores instruction fine-tuning, which aims to make language models better at performing NLP tasks with zero-shot inference.

##### Model Evaluation Metrics
- [HELM - Holistic Evaluation of Language Models](https://crfm.stanford.edu/helm/latest/) HELM is a living benchmark to evaluate Language Models more transparently. 

- [General Language Understanding Evaluation (GLUE) benchmark](https://openreview.net/pdf?id=rJ4km2R5t7) This paper introduces GLUE, a benchmark for evaluating models on diverse natural language understanding (NLU) tasks and emphasizing the importance of improved general NLU systems.

- [SuperGLUE](https://super.gluebenchmark.com/) This paper introduces SuperGLUE, a benchmark designed to evaluate the performance of various NLP models on a range of challenging language understanding tasks.

- [ROUGE: A Package for Automatic Evaluation of Summaries](https://aclanthology.org/W04-1013.pdf) This paper introduces and evaluates four different measures (ROUGE-N, ROUGE-L, ROUGE-W, and ROUGE-S) in the ROUGE summarization evaluation package, which assess the quality of summaries by comparing them to ideal human-generated summaries.

- [Measuring Massive Multitask Language Understanding (MMLU)](https://arxiv.org/pdf/2009.03300.pdf) This paper presents a new test to measure multitask accuracy in text models, highlighting the need for substantial improvements in achieving expert-level accuracy and addressing lopsided performance and low accuracy on socially important subjects.

- [BigBench-Hard - Beyond the Imitation Game: Quantifying and Extrapolating the Capabilities of Language Models](https://arxiv.org/pdf/2206.04615.pdf) The paper introduces BIG-bench, a benchmark for evaluating language models on challenging tasks, providing insights on scale, calibration, and social bias.

##### Parameter- efficient fine tuning (PEFT)
- [Scaling Down to Scale Up: A Guide to Parameter-Efficient Fine-Tuning](https://arxiv.org/pdf/2303.15647.pdf) This paper provides a systematic overview of Parameter-Efficient Fine-tuning (PEFT) Methods in all three categories discussed in the lecture videos.

- [On the Effectiveness of Parameter-Efficient Fine-Tuning](https://arxiv.org/pdf/2303.15647.pdf) The paper analyzes sparse fine-tuning methods for pre-trained models in NLP.

##### LoRA
- [LoRA Low-Rank Adaptation of Large Language Models](https://arxiv.org/pdf/2106.09685.pdf) This paper proposes a parameter-efficient fine-tuning method that makes use of low-rank decomposition matrices to reduce the number of trainable parameters needed for fine-tuning language models.

- [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/pdf/2305.14314.pdf) This paper introduces an efficient method for fine-tuning large language models on a single GPU, based on quantization, achieving impressive results on benchmark tests.

##### Prompt tuning with soft prompts
- [The Power of Scale for Parameter-Efficient Prompt Tuning](https://arxiv.org/pdf/2104.08691.pdf) The paper explores "prompt tuning," a method for conditioning language models with learned soft prompts, achieving competitive performance compared to full fine-tuning and enabling model reuse for many tasks.