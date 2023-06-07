# Notes

These notes are from the DeepLearning.ai course on [Building Systems with the ChatGPT API](https://www.deeplearning.ai/short-courses/building-systems-with-chatgpt/)

The topics covered in the lectures are as follows:
- Introduction 
- Language Modles, the Chat Format and Tokens
- Classification (Evaluate Inputs)
- Moderation 
- Chain of Thought Reasoning 
- Chaining Prompts
- Check Outputs 
- Evaluation 
- Evaluation Part 1
- Evaluation Part 2
- Summary 

## 1. Introduction 
 Best practices for building a complex application in LLM. More internal steps than visible to a user. 
- Evaluate the input to check if there is any problematic content, such as, hateful speech 
- Next, it to process the input 
evaluate what type of querry is it - complaint, product inquiry, 
- Retrieve the relevant information 
- Use LLM to build a helpful response
- Check the optput to understand if the output is problematic, such as, inacurate or inappropriate
- Best practices for evaluating and improving your system over time

## 2. Language Modles, the Chat Format and Tokens
- How does LLM model work 
- Two types of LLM models 
    - Base LLM 
    - Instruction Tuned LLM 
- Getting from a Base LLM to an instruction tuned LLM:
    - Train a Base LLM on a lot of data.
    - Further train the model:
        - Fine-tune on examples of where the input/output data
        - Obtain human-ratings of the quality of different LLM outputs - helpful, honest and harmless
        - Tune LLM to increase probability that it generates the more highly rated outputs (using RLHF: Reinforcement Learning from Human Feedback)
- Limitations due to Tokens 
- Helper function - chat format 
    - usage of system messages
- Responsible use of Open AI API key in .env file


## 3. Classification (Evaluate Inputs)
- Evaluate inputs to ensure safety and security of the system.

- For tasks in which a lot of different sets of instructions are needed top handle different cases, it can be beneficial to first classify the type of querry and then determine the type of instructions to use. Use fixed categories and hard coded instructions for handling tasks

## 4. Moderation 
- If you are building a system where the users can input information. It is important to check if the users are using the system responsibly.

 -Commpon types of system abuse:
    - Hateful speech (Use Moderation API to avoid)
 - Prompt injections (usage of prompts to detect prompt injections)
 
## 5. Chain of Thought Reasoning 
## 6. Chaining Prompts
## 7. Check Outputs 
## 8. Evaluation 
## 9. Evaluation Part 1
## 10. Evaluation Part 2
## 11. Summary 
