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
- Fine-tuning on a single task