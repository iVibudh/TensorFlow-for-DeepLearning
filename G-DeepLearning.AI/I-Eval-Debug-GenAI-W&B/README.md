# Notes on Evaluating and Debugging Generative AI - Weights & Biases

[ref](https://learn.deeplearning.ai/courses/evaluating-debugging-generative-ai/lesson/1/introduction)

0. Introduction 
1. Instrument W&B
2. Training a Diffusion Model with W&B
3. Evaluating Diffusion Model
4. LLM Evaluationand Tracing with W&B
5. Finetuning a Language model
6. Conclusion
<hr />

### 0. Introduction 
![Course Intro](SS/1-intro.png)

### 1. Instrument W&B
![W&B Intro](SS/2-W&B-tool.png) <br>
![W&B Intro code](SS/2-1-W&B-code.png)

### 2. Training a Diffusion Model with W&B
![diffusion model intro](SS/3-Diffusion-model-intro.png) <br>
![diffusion model intro- 1](SS/3-1-Diffusion-model-intro.png) ![diffusion model intro- 1](SS/3-2-Diffusion-model-intro.png) <br>
For diffusion models, the loss flatens out very quickly. However, small improvement in the loss improves the quality of the image by a lot. So, we need to sample the images during training.

### 3. Evaluating Diffusion Model
![Managing Models](SS/4-Evaluating-diffusion-models.png) <br>
![W&B Tables](SS/4-1-Evaluating-diffusion-models-Tables.png) 

### 4. LLM Evaluationand Tracing with W&B
![Example 1 - Evaluating LLMs](SS/5-1-evaluating-LLMs.png) <br>
<br>
![Example 1- using API with tables](SS/5-2-evaluating-LLMs-ex1.png) <br>
**using API with tables** could be used for creating a table with system prompts, user prompt, response, and custom functions like cost, time, etc.
<br>
<br>

![Example 2 - LLM Tracer](SS/5-3-evaluating-LLMs-Tracer-ex2.png)
**LLM Tracer** It is a tool that allows you to trace a chain (from Langchain) with the help of TraceTimeline.
<br>
<br>

![Example 3 - Tracking Langchain Agents](SS/5-4-evaluating-LLMs-tracking-Langchain-Agent-ex3.png)
**Tracking LangChain Agents** It is a tool that allows you to trace an agent (from Langchain).

### 5. Finetuning a Language model
![Finetuning LLM](SS/6-1-finetuning-llm.png) <br>
This allows you to keep track of the training process and to see the results of the training in real time.
