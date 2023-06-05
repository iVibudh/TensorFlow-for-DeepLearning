# Notes

These notes are from the DeepLearning.ai course on [ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)

The topics covered in the lectures are as follows:
- Introduction
- Guidelines
- Iterative
- Summarization 
- Expanding
- Chatbot
- Conclusion

## 1. Introduction 
 
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

## 2. Guidelines 

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


## 3. Iterative Prompt development 
- Try something 
- analyse the results 
- clarify instructions 
- Refine prompts with a sample batch 
- Retry 

## 4. Summarizing 
- Text summarization 
- limit on words, sentence or character limit
- summarize with a specific context 
- try "extract" instead of summarize 

## 5. Inferring 
- extract sentiment 
- extract emotions 
- identify extremely angry messages 
- Extract names and entities 
- Multi class classification 

## 6. Transforming 
- Universal Language translation 
- Tone transformation - Formal to informal 
- Format Conversion 
- Spellcheck/Grammar check 

## 7. Expanding 
Use 'AI customer agent' to respond to a customer email. 

Temperature for a generative model 
- helps to a get a variety of responses for the same input or get the same response each time 
- degree of exploration or randomness of the model 
- higher temperature more unlikely choices might be taken too 
- temperature = 0 => more predictable response 
- Temperature = 0.9 => more creative 

## 8. Chatbot
- utilize the chat format to have extended conversations with chatbot personalized or specialized for specific tasks or behaviors.
- eg.  role of an AI customer service agent or an AI order taker for a restaurant
- We do this by adding the following components of the message 
    - System Message: sets the behaviour or persona of the assistance 
    (this is a high level guidance to the model)
    - User Message: the question asked by the user 
    - assistant message: the message from the language model 
- We can also provide the previous messages as context to help the chatbot understand the whole conversation 

## 9. Conclusion
- Principles:
    - Write clear and specific instructions 
    - Give the model time to think 
- Iterative prompt development 
- Capabilities: Summarizing, Infering, Transforming, Expanding 
- Build a custom chatbot
