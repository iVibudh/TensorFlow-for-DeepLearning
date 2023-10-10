# Week 3.2 - Applications - Agents

### Model optimization for deployment
Large language models present inference challenges in terms of computing and storage requirements, as well as ensuring low latency for consuming applications.
- Optimize and deeploy model for inference
    - So how fast do you need your model to generate completions? 
    - What compute budget do you have available? 
    - Model performance vs inference speed vs storage VRAM? 
- The second set of questions is tied to additional resources that your model may need. 
    - Do you intend for your model to interact with external data or other applications? 
    - And if so, how will you connect to those resources? 
- Lastly, there's the question of how your model will be consumed. 
    - What will the intended application or API interface that your model will be consumed through look like? 
<br>

**LLM optimization techniques**
- **Distillation (Knowledge Distillation Model)**: Teacher Model to a student model
    - Student mimics the prediction from the Teacher model just in the final layer,  OR
    - in the model's hidden layers as well
    - Steps: 
        - You start with your fine tune LLM as your teacher model and create a smaller LLM for your student model. 
        - You freeze the teacher model's weights and use it to generate completions for your training data. At the same time, you generate completions for the training data using your student model. 
        - tokens produced by the Teacher model is called Soft label. Tokens produced by the student model is called soft predictions. Difference between the 2 is called **Distillation Loss**
        - The knowledge distillation is achieved by minimizing distillation loss. 
        - distillation uses the probability distribution over tokens that is produced by the teacher model's softmax layer. Trick that we use is in this process we keep temperature high. So, the distribution of Teacher model is same as student model. 
        - In parallel, you train the student model to generate the correct predictions based on your ground truth training data. Here, you don't vary the temperature setting and instead use the standard softmax function. 
        - Difference between Hard predictions and hard labels is Called **Student Loss**
- **Quantization**: post training quantization transforms a model's weights to a lower precision representation, such as, 16 bit floating point, 8 bit integer, et. Reducing memory footprint of the model. 
    - can be applied to just the model weights or to both weights and activation layers.
- **Pruning**: removes redundant parameters that contribute little to model's performance
    - These are the weights with values very close to or equal to zero. Note that some pruning methods require full retraining of the model, 
    - while others fall into the category of parameter efficient fine tuning, such as LoRA.

### Gen AI project Lifecycle Lifecycle Cheat sheet

### Using the LLM in applications
- Knowledge cut off date 
- doing math 
- Hallucination 
- Solution 
    - access to external data sources (Retrieval Augmented Generation - RAG) or connecting to existing APIs of other applications
    - External Applications 
        - Trigger API calls 
        - Perform Calculations
- Requirements for using LLM to power applications
    - Plan actions
    - Format outputs 
    - Validate actions

### Helping LLMs reason and plan with chain-of-thought

### Program-aided Language Model (PAL)
The method makes use of chain of thought prompting to generate executable Python scripts. The scripts that the model generates are passed to an interpreter to execute.

### ReAct: Combining reasoning and action
LangChain
- Tools
- Prompt Templates
- Memory
- Agents: Agents can be incorporated into chains to take an action or plan and execute a series of actions.

### Resources:
- [ReAct paper](https://arxiv.org/abs/2210.03629)

**RLHF**
- 

### LLM application architecture
- [Training language models to follow instructions with human feedback](https://arxiv.org/pdf/2203.02155.pdf) Paper by OpenAI introducing a human-in-the-loop process to create a model that is better at following instructions (InstructGPT).
- [Learning to summarize from human feedback](https://arxiv.org/pdf/2009.01325.pdf) This paper presents a method for improving language model-generated summaries using a reward-based approach, surpassing human reference summaries.
<br>
<br>

**Proximal Policy Optimization (PPO)** 
- [Proximal Policy Optimization Algorithms](https://arxiv.org/pdf/1707.06347.pdf) The paper from researchers at OpenAI that first proposed the PPO algorithm. The paper discusses the performance of the algorithm on a number of benchmark tasks including robotic locomotion and game play.

- [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/pdf/2305.18290.pdf) This paper presents a simpler and effective method for precise control of large-scale unsupervised language models by aligning them with human preferences.
<br>
<br>

**Scaling human feedback**
- [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/pdf/2212.08073.pdf) This paper introduces a method for training a harmless AI assistant without human labels, allowing better control of AI behavior with minimal human input.

<br>
<br>

**Advanced Prompting Techniques**
- [Chain-of-thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/pdf/2201.11903.pdf) Paper by researchers at Google exploring how chain-of-thought prompting improves the ability of LLMs to perform complex reasoning.

- [PAL: Program-aided Language Models](https://arxiv.org/abs/2211.10435) This paper proposes an approach that uses the LLM to read natural language problems and generate programs as the intermediate reasoning steps.

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) This paper presents an advanced prompting technique that allows an LLM to make decisions about how to interact with external applications.

<br>
<br>

**LLM powered application architectures**
- [LangChain Library (GitHub)](https://github.com/langchain-ai/langchain) This library is aimed at assisting in the development of those types of applications, such as Question Answering, Chatbots and other Agents. You can read the documentation [here](https://docs.langchain.com/docs/)
- [Who Owns the Generative AI Platform?](https://a16z.com/who-owns-the-generative-ai-platform/) The article examines the market dynamics and business models of generative AI.

