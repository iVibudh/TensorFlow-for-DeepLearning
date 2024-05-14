# Finetuning Large Language Models - Lamini

These notes are from the DeepLearning.ai course on [Finetuning Large Language Models](https://learn.deeplearning.ai/courses/finetuning-large-language-models/lesson/1/introduction)

The topics covered in the lectures are as follows:
1. Introduction 
2. Why Finetune
3. Where Finetune fits in
4. Instruction finetuning
5. Data preparation
6. Training Process
7. Evaluation and iteration
8. Consideration on getting started now
9. Conclusion


## 1. Introduction
Course Overview:
- This course will cover fine-tuning large language models (LLMs).
- Fine-tuning is a technique that allows you to specialize a large language model for your own specific use case - such as have a certain tone.
- The course will cover the following topics:
    - How fine-tuning fits in RAG applications
    - The difference between fine-tuning and other techniques such as prompt engineering and retrieval-augmented generation
    - A specific variant called instruction fine-tuning, which teaches an LLM to follow instructions similar to ChatGPT
    - How to implement fine-tuning, evaluate and iterate in code
Benefits of taking this course:
- You will gain a concrete understanding of fine-tuning LLMs.
- You will be able to get started using fine-tuning techniques for your own projects.
- Fine-tuning is a significant step up in capability compared to just prompting, and it is an important tool for people building applications using LLMs.

## 2. Why Finetune
- What is finetume?
    - Gneral purpose model to a specialized purpose model.
    (GPT-3 to ChatGPT) or (GPT4 to Github Copilot)
    Analagy (Doctor to a Cardiologist or Dermatologist)
- What does fientuning do for the model?
    - Gives the model new information
    - LLM gives more consistent output or behaviour
    - Reduces hallucination
    - Solves aspecific use case
    - process could be very similar to the model training
- Finetune Libraries
    - Pytorch (Meta)
    - Huggingface
    - Llama library (Lamini)
- Lab:
    - base llama-2 model 
    - base llama-2-chat model 

![finetuning](images\01-01-finetuning.jpg)
![prompting-vs-finetuning.jpg](images\01-02-prompting-vs-finetuning.jpg)
![finetuning-benefits.jpg](images\01-03-finetuning-benefits.jpg)

## 3. Where Finetune fits in
**Pretraining**
- Model at start has just the neural network
    - its objective is to predict the next word
    - trained on giant corpus of text - "unlabeled" SELF-SUPERVISED
    - Pretraining is Expensive and time consuming
- After Training 
    - Learns Language
    - Learns Knowledge 
- Open-source pretrained data - **"The Pile" by Luther**
    - intellectual text from different sources

**Finetuning after pretraining**
- Fine-tune refers to training further
    - Can also be self-supervised unlabeled data
    - Can be "labeled" data that you created
    - Less data needed

- Lab:
    - load large text dataset with streaming (one at at time)
    - load QA dataset from company specific data
    - apply qa template of your choice by string concatenation
    - Common way of storing your data will be jsonline - where each row is a json
    - So we prepare 2 datasets:
        - text only data - single string of QA
        - json data - json with question and answer

![finetuning-after-pretraining.jpg](images\03-01-finetuning-after-pretraining.jpg)

## 4. Instruction finetuning
- Instruction finetuning is a variant of finetuning
    - "instruction-tuned" or "instruction-following" LLM
    - Teaches model to behave like a chatbot
    - Better user interface for model interaction
        - Tuned GPT-3 into ChatGPT-3
- Intruction-following datasets
    - FAQs
    - Customer Support conversations
    - Slack messages
- Non-QA data (such as a readme file) can be converted into a QA dataset
    - Alpacha (uses ChatGPT, or open source LLM) to convert a data file into a QA dataset

- Overview of Finetuning:
    - Data preparation
    - Training
    - Evaluation 
    (iterate)

- Lab:
    - load instruction tuned dataset (alpaca)
    - prompt template with input and without input 
    - test response from non-instruction tuned LLM, instruction tuned LLM, and ChatGPT-3
    - run inference on instruction tuned LLM 

![finetuning-data-prep.jpg](images\04-01-finetuning-data-prep.jpg)

## 5. Data preparation
- What kind of data do you need for finetuning:
    - Higher Quality 
    - Diversity
    - Real 
    - More
- Steps to prepare your data:
    1. collect instruction-respnse pairs
    2. concatenate pairs - add prompt template, if needed
    3. Tokenize: pad, truncate
    4. Split into train, test
- Lab:
    - Padding - making the lengths of all the tokenized sentences same
    - truncate - left or right. you truncate the tokenized sentence to a the max_length
    - Pad and truncate all your QA data
    - Split the data into test and train
    - datasets: taylor_swift, bts, open_llms
    
![tokenize-data.jpg](images\05-01-tokenize-data.jpg)

## 6. Training Process
- Training an LLM: same as other neural networks
- Hyperparameters:
    - Learning rate
    - Learning rate scheduler
    - Optimize hyperparameter

- Lab:
    - training config
    - tokenize, train/test split
    - load base LLM model
    - base model on CPU or GPU device
    - Inference function
        - tokenize the text
        - generate tokens with prompt
        - decode generated tokens
        - return response
    - Training arguments
        - max_step - max no of trainig steps - No. of batches
        - trained_model at eaxh step
        - learning rate 
        - no. of epochs
        - Max steps
        - per device training batch size
        - output_directory, etc
     - Understand the number of floating point operations (Flops) and memory footprint
     - Run Trainer class

![training-process.jpg](images\06-01-training-process.jpg)

## 7. Evaluation and iteration

## 8. Consideration on getting started now

## 9. Conclusion