## Notes

These notes are from the DeepLearning.ai course on [ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)

The topics covered in the lectures are as follows:
- Introduction
- Guidelines
- Iterative
- Summarization 
- Expanding
- Chatbot
- Conclusion

#### 1. Introduction 
 
Prompting best Practices for 
- summarizing
- inferring 
- transforming 
- expanding 

There are 2 types of Large Language Models (LLMs)
- Base LLM (good at predicting the next word based on text training data)
- Instruction Tuned LLM (tries to follow instructions)

The way you want to train the **Instruction Tuned LLM** is that you start off with a base LLM that has been traiined on huge amount of text data and then further fine-tuned with inputs and outputs (i.e. instructions and good attempts to follow those instructions). The outputs are further refined using **RLHF** (Reinforcement Learning from Human Feedback) to make the system better able to be helpful and follow instructions. 

Helpful, Honest and Harmless  - They are less likely to give problematic text (toxic output) compared to base LLMs. Best practices for instruction tuned LLMs.

#### 2. Guidelines 

Principles of Prompting 
1. Write clear and specific instructions 
    - Use """, ''', ---, <>, XML tags <tag></tag>
    - Ask for a structured output
    - check whether conditions are satisfied
    - Few-shot prompting
2. Give the model time to think
    - specify the steps needed to complete a task
    - instruct the model to work out its own solution before rushing to a complusion 
3. Model Limitation - Hallucination 
    - Resolve this by: first find relevant information then answer the question based on the relevant information. 


#### 3. Iterative Prompt development 
- Try something 
- analyse the results 
- clarify instructions 
- Refine prompts with a sample batch 
- Retry 

#### 4. Summarizing 
- Text summarization 
- limit on words, sentence or character limit
- summarize with a specific context 
- try "extract" instead of summarize 

#### 5. 


