# Week 3.2 - Applications - Agents

# Model optimization for deployment
Large language models present inference challenges in terms of computing and storage requirements, as well as ensuring low latency for consuming applications.
- Optimize and deeploy model for inference
    - So how fast do you need your model to generate completions? 
    - What compute budget do you have available? 
    - And are you willing to trade off model performance for improved inference speed or lower storage? 
- The second set of questions is tied to additional resources that your model may need. 
    - Do you intend for your model to interact with external data or other applications? 
    - And if so, how will you connect to those resources? 
- Lastly, there's the question of how your model will be consumed. 
    - What will the intended application or API interface that your model will be consumed through look like? 
<br>

**LLM optimization techniques**
- Distillation (Knowledge Model): Teacher Model to a student model
    - Student mimics the prediction from the Teacher model just in the final layer,  OR
    - in the model's hidden layers as well
    - Steps: 
        - You start with your fine tune LLM as your teacher model and create a smaller LLM for your student model. 
        - You freeze the teacher model's weights and use it to generate completions for your training data. At the same time, you generate completions for the training data using your student model. - The knowledge distillation is achieved by minimizing distillation loss. 
        -  distillation uses the probability distribution over tokens that is produced by the teacher model's softmax layer.
- Quantization: 16bit, 8bit, 4bit
- Pruning: removes redundant parameters that contribute little to model's performance

