# LangChain for LLM Application Development

These notes are from the DeepLearning.ai course on [LangChain for LLM Application Development](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/)

The topics covered in the lectures are as follows:
- Introduction 
- Models, Prompts and parsers (18)
- Memory (17)
- Chains (13)
- Question and Answer (15)
- Evaluation (15)
- Agents (14)
- Conclusion

## 1. Introduction 
- LangChain is an open-scource development framework for LLM applications. 
- Python and Javascript (TypeScript) packages
- Focused on composition and modularity
- Key value adds:
    - Modular components
    - Use cases: Common ways to combine components

**Components of LangChain**
- **Models**
    - LLMS: 20+ integrations
    - Chat Models
    - Text Embedding Models: 10+ integrations
- **Prompts**
    - Prompt Templates
    - Output Parsers: 5+ implementations
        - Retry/fixing logic
    - Example Selectors: 5+ implementations
- **Indexes**
    - Document Loaders: 50+ implementations
    - Text Splitters: 10+ implementations
    - Vector stores: 10+ integrations
    - Retrievers: 5+ integrations/implementations
- **Chains**
    - Prompt + LLM + Output parsing
    - Can be used as building blocks for longer chains
    - More application specific chains: 20+ types
- **Agents**
    - Agent Types: 5+ types
        - Algorithms for getting LLMS to use tools
    - Agent Toolkits: 10+ implementations
        - Agents armed with specific tools for a specific application

## 2. Models, Prompts and parsers
- Direct API calls to OpenAI
- API calls through LangChain:
    - Models: the LLM model
    - Prompts
    - Output parsers: takes the output and parses it into a more structured format

## 3. Memory


## 4. Chains
## 5. Question and Answer
## 6. Evaluation
## 7. Agents
## 8. Conclusion

