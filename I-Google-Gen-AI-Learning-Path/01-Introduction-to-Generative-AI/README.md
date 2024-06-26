# 1. Introduction to Generative AI

This is an introductory level microlearning course aimed at explaining what Generative AI is, how it is used, and how it differs from traditional machine learning methods. It also covers Google Tools to help you develop your own Gen AI application. 

### Course Content
This course covers:
- Define Generative AI
- Explain how Generative AI works
- Describe Generative AI model types
- Describe Generative Applications

### Generative AI 
It is a type of AI technology thst can produce various types of content, including text, imagery, audio, and synthetic data. 

##### What is Artificial Intelligence (AI)? What is the difference between AI and Machine Learning(ML)?
- One way to think about it is that AI is a discipline. AI is a branch of computer science that deals with the creation of **intelligent agents, which are systems that can reason and learn and act autonomously.  Think and act like human intelligence.**
- In this discipline we have ML which is a subfield of AI it is a program or system that trains a model from input data. **ML gives the computer the ability to learn without explicit programming**
    - supervised models (labelled data)
    - unsupervised models 
- Deep learning (subset of ML) uses Artificial Neural Networks, allowing them to process more complex patterns than traditional Machine Learning. 
- In semi-supervised learning, a neural network is trained on a small amount of label data and a large amount of unlabelled data. Labelled data allows it learn the basic task. Unlabelled data allows the model to generalize the tasks. 
- **Gen AI** is a subset of deep learning. It uses artificial neural networks, can process labeled and unlabelled data using supervised, unsupervised, and semi-supervised methods.

- Deep Learning Model Types 
    - Discriminitive
    - Generative 

**Classical supervised or unsupervised learning VS Gen AI**
- Classical supervised or unsupervised learning can predict, classify or cluster something
- The Gen AI porocess can take training code, label data, and unlabeled data of all data types and build a foundation model. The foundation model can then generate new content - text, code, images, audio, video, etc. 
Eg. PaLM (Pathways Language Model), LAMBDA (Language Model for Dialogue Applications)

##### Generative AI based on Data 
- When input is Text - Output could be Text, Image, Audio, Decisions, etc. 
- When input is image - Output could be text, image, video (animation)

##### The power of Gen AI comes from Transformers
- Transformer's Encoder encodes the input prompt
- Then the transformer's decoder decodes this
- Further, a generative pretrained transformer model produces an appropriate response. 

##### Hallucinations 
Words or phrases that are generated by the model that are often nonsensical or grammatically incorrect. 

##### Propmt design
The quality of input determines the quality of the output. 

##### Model Types
- text-to-text
- text-to-image (diffusion)
- text-to-video or text-to-3D
- text-to-task (software agents, virtual assistants, automation)

- **Foundation Models** - It is trained to do a large variety of tasks. 
    - Input data could be text, image, speach, structured data, 3D, etc
    - Outout is more adaptive. 
    - Can perform tasks, such as, question answering, sentiment analysis, information extraction, image captioning, object recognition, instruction following, etc. 

##### Model Garden: Vertex AI Foundation Models
- Language 
    - Foundations: PaLM API for chat, PaLM API for text, BERT
- Vision
    - Foundations: Embeddings extractor, Stable Diffusion, BLIP image captioning, BLIP VQA, CLIP, OWL-ViT, ViT GPT2


#### GenAI Studio
    - Fine-tune models 
    - Deploy models to production 
    - Create Chatbots 
    - Image Generation 

#### Generative AI App Builder 
- It lets you create apps without writing any code. 
- Drag and drop interface to design and build apps. 
- Visual editor allows you to create and edit app content
- Built in search engine that allows you to search for information within apps
- It hasd a Converversational AI Engine that helps users to interact with the app using natural language. 
- You can create your own digital assistants, custom search engines, knowledge bases, training applications, etc.

#### PaLM API & MakerSuite simplifies Generative Development Cycles
- Palm API - simple entry point for Google's LLMs. Provide developer access to models that are optimized for use cases
- MakerSuite - An approchable way to start prototyping and building generative AI applications. Iterate on prompts, augment your dataset with synthetic data, tune custom models. 
    - Model training tool 
    - Model deployment tool 
    - Model monitoring tool





# All Readings: Introduction to Generative AI (G-GENAI-I)
Here are the assembled readings on generative AI:
- [Ask a Techspert: What is generative AI?](https://blog.google/inside-google/googlers/ask-a-techspert/what-is-generative-ai/)
- [Build new generative AI powered search & conversational experiences with Gen App Builder:](https://cloud.google.com/blog/products/ai-machine-learning/create-generative-apps-inminutes-with-gen-app-builder)
- [What is generative AI?](https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-generative-ai)
- [Google Research, 2022 & beyond: Generative models:](https://ai.googleblog.com/2023/01/google-research-2022-beyond-language.html#GenerativeModels)
- [Building the most open and innovative AI ecosystem:](https://cloud.google.com/blog/products/ai-machine-learning/building-an-open-generative-ai-partner-ecosystem)
- [Generative AI is here. Who Should Control It?](https://www.nytimes.com/2022/10/21/podcastshard-fork-generative-artificial-intelligence.html)
- [Stanford U & Google’s Generative Agents Produce Believable Proxies of Human Behaviors:](https://syncedreview.com/2023/04/12/stanford-u-googles-generative-agents-produce-believable-proxies-of-human-behaviours/)
- [Generative AI: Perspectives from Stanford HAI:](https://hai.stanford.edu/sites/default/files/2023-03/Generative_AI_HAI_Perspectives.pdf)
- [Generative AI at Work:](https://www.nber.org/system/files/working_papers/w31161/w31161.pdf)
- [The future of generative AI is niche, not generalized:](https://www.technologyreview.com/2023/04/27/1072102/the-future-of-generative-ai-isniche-not-generalized/)


Here are the assembled readings on large language models:
- [NLP's ImageNet moment has arrived: ](https://thegradient.pub/nlp-imagenet/)
- [Google Cloud supercharges NLP with large language models:](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-supercharges-nlp-with-large-language-models)
- [LaMDA: our breakthrough conversation technology:](https://blog.google/technology/ai/lamda/)
- [Language Models are Few-Shot Learners:](https://proceedings.neurips.cc/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64aPaper.pdf)
- [PaLM-E: An embodied multimodal language model:](https://ai.googleblog.com/2023/03/palm-e-embodied-multimodal-language.html)
- [Pathways Language Model (PaLM): Scaling to 540 Billion Parameters for Breakthrough Performance:](https://ai.googleblog.com/2022/04/pathways-language-model-palm-scaling-to.html)
- [PaLM API & MakerSuite: an approachable way to start prototyping and building generative AI applications:](https://developers.googleblog.com/2023/03/announcing-palm-api-and-makersuite.html)
- [The Power of Scale for Parameter-Efficient Prompt Tuning:](https://proceedings.neurips.cc/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64aPaper.pdf)
- [Google Research, 2022 & beyond: Language models:](https://ai.googleblog.com/2023/01/google-research-2022-beyond-language.html#LanguageModels)
- [Accelerating text generation with Confident Adaptive Language Modeling (CALM):](https://ai.googleblog.com/2022/12/accelerating-text-generation-with.html)
- [Solving a machine-learning mystery:](https://news.mit.edu/2023/large-language-models-in-context-learning-0207)

Additional Resources:
- [Attention is All You Need:](https://research.google/pubs/pub46201/)
- [Transformer: A Novel Neural Network Architecture for Language Understanding:](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html)
- [Transformer on Wikipedia:](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)#:~:text=Transformers%20were%20introduced%20in%202017,allowing%20training%20on%20larger%20datasets)
- [What is Temperature in NLP?](https://lukesalamone.github.io/posts/what-is-temperature/)
- [Bard now helps you code:](https://blog.google/technology/ai/code-with-bard/)
- [Model Garden:](https://cloud.google.com/model-garden)
- [Auto-generated Summaries in Google Docs:](https://ai.googleblog.com/2022/03/auto-generated-summaries-in-google-docs.html)
