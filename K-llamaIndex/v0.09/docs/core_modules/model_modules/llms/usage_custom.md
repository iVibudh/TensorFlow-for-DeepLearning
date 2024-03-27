# Customizing LLMs within LlamaIndex Abstractions

You can plugin these LLM abstractions within our other modules in LlamaIndex (indexes, retrievers, query engines, agents) which allow you to build advanced workflows over your data.

By default, we use OpenAI's `text-davinci-003` model. But you may choose to customize
the underlying LLM being used.

Below we show a few examples of LLM customization. This includes

- changing the underlying LLM
- changing the number of output tokens (for OpenAI, Cohere, or AI21)
- having more fine-grained control over all parameters for any LLM, from context window to chunk overlap

## Example: Changing the underlying LLM

An example snippet of customizing the LLM being used is shown below.
In this example, we use `text-davinci-002` instead of `text-davinci-003`. Available models include `text-davinci-003`,`text-curie-001`,`text-babbage-001`,`text-ada-001`, `code-davinci-002`,`code-cushman-001`. 

Note that
you may also plug in any LLM shown on Langchain's
[LLM](https://python.langchain.com/en/latest/modules/models/llms/integrations.html) page.

```python

from llama_index import (
    KeywordTableIndex,
    SimpleDirectoryReader,
    LLMPredictor,
    ServiceContext
)
from llama_index.llms import OpenAI
# alternatively
# from langchain.llms import ...

documents = SimpleDirectoryReader('data').load_data()

# define LLM
llm = OpenAI(temperature=0, model="text-davinci-002")
service_context = ServiceContext.from_defaults(llm=llm)

# build index
index = KeywordTableIndex.from_documents(documents, service_context=service_context)

# get response from query
query_engine = index.as_query_engine()
response = query_engine.query("What did the author do after his time at Y Combinator?")

```

## Example: Changing the number of output tokens (for OpenAI, Cohere, AI21)

The number of output tokens is usually set to some low number by default (for instance,
with OpenAI the default is 256).

For OpenAI, Cohere, AI21, you just need to set the `max_tokens` parameter
(or maxTokens for AI21). We will handle text chunking/calculations under the hood.

```python

from llama_index import (
    KeywordTableIndex,
    SimpleDirectoryReader,
    ServiceContext
)
from llama_index.llms import OpenAI

documents = SimpleDirectoryReader('data').load_data()

# define LLM
llm = OpenAI(temperature=0, model="text-davinci-002", max_tokens=512)
service_context = ServiceContext.from_defaults(llm=llm)

```

## Example: Explicitly configure `context_window` and `num_output`

If you are using other LLM classes from langchain, you may need to explicitly configure the `context_window` and `num_output` via the `ServiceContext` since the information is not available by default.

```python

from llama_index import (
    KeywordTableIndex,
    SimpleDirectoryReader,
    ServiceContext
)
from llama_index.llms import OpenAI
# alternatively
# from langchain.llms import ...

documents = SimpleDirectoryReader('data').load_data()


# set context window
context_window = 4096
# set number of output tokens
num_output = 256

# define LLM
llm = OpenAI(
    temperature=0, 
    model="text-davinci-002", 
    max_tokens=num_output,
)

service_context = ServiceContext.from_defaults(
    llm=llm,
    context_window=context_window,
    num_output=num_output,
)

```

## Example: Using a HuggingFace LLM

LlamaIndex supports using LLMs from HuggingFace directly. Note that for a completely private experience, also setup a local embedding model (example [here](embeddings.md#custom-embeddings)).

Many open-source models from HuggingFace require either some preamble before before each prompt, which is a `system_prompt`. Additionally, queries themselves may need an additional wrapper around the `query_str` itself. All this information is usually available from the HuggingFace model card for the model you are using.

Below, this example uses both the `system_prompt` and `query_wrapper_prompt`, using specific prompts from the model card found [here](https://huggingface.co/stabilityai/stablelm-tuned-alpha-3b).

```python
from llama_index.prompts.prompts import SimpleInputPrompt

system_prompt = """<|SYSTEM|># StableLM Tuned (Alpha version)
- StableLM is a helpful and harmless open-source AI language model developed by StabilityAI.
- StableLM is excited to be able to help the user, but will refuse to do anything that could be considered harmful to the user.
- StableLM is more than just an information source, StableLM is also able to write poetry, short stories, and make jokes.
- StableLM will refuse to participate in anything that could harm a human.
"""

# This will wrap the default prompts that are internal to llama-index
query_wrapper_prompt = SimpleInputPrompt("<|USER|>{query_str}<|ASSISTANT|>")

import torch
from llama_index.llms import HuggingFaceLLM
llm = HuggingFaceLLM(
    context_window=4096, 
    max_new_tokens=256,
    generate_kwargs={"temperature": 0.7, "do_sample": False},
    system_prompt=system_prompt,
    query_wrapper_prompt=query_wrapper_prompt,
    tokenizer_name="StabilityAI/stablelm-tuned-alpha-3b",
    model_name="StabilityAI/stablelm-tuned-alpha-3b",
    device_map="auto",
    stopping_ids=[50278, 50279, 50277, 1, 0],
    tokenizer_kwargs={"max_length": 4096},
    # uncomment this if using CUDA to reduce memory usage
    # model_kwargs={"torch_dtype": torch.float16}
)
service_context = ServiceContext.from_defaults(
    chunk_size=1024, 
    llm=llm,
)
```

Some models will raise errors if all the keys from the tokenizer are passed to the model. A common tokenizer output that causes issues is `token_type_ids`. Below is an example of configuring the predictor to remove this before passing the inputs to the model:

```python
HuggingFaceLLM(
    ...
    tokenizer_outputs_to_remove=["token_type_ids"]
)
```

A full API reference can be found [here](../../reference/llm_predictor.rst).

Several example notebooks are also listed below:

- [StableLM](/examples/customization/llms/SimpleIndexDemo-Huggingface_stablelm.ipynb)
- [Camel](/examples/customization/llms/SimpleIndexDemo-Huggingface_camel.ipynb)

## Example: Using a Custom LLM Model - Advanced

To use a custom LLM model, you only need to implement the `LLM` class (or `CustomLLM` for a simpler interface)
You will be responsible for passing the text to the model and returning the newly generated tokens.

Note that for a completely private experience, also setup a local embedding model (example [here](embeddings.md#custom-embeddings)).

Here is a small example using locally running facebook/OPT model and Huggingface's pipeline abstraction:

```python
import torch
from transformers import pipeline
from typing import Optional, List, Mapping, Any

from llama_index import (
    ServiceContext, 
    SimpleDirectoryReader, 
    LangchainEmbedding, 
    ListIndex
)
from llama_index.llms import CustomLLM, CompletionResponse, LLMMetadata


# set context window size
context_window = 2048
# set number of output tokens
num_output = 256

# store the pipeline/model outisde of the LLM class to avoid memory issues
model_name = "facebook/opt-iml-max-30b"
pipeline = pipeline("text-generation", model=model_name, device="cuda:0", model_kwargs={"torch_dtype":torch.bfloat16})

class OurLLM(CustomLLM):

    @property
    def metadata(self) -> LLMMetadata:
        """Get LLM metadata."""
        return LLMMetadata(
            context_window=context_window, num_output=num_output
        )

    def complete(self, prompt: str, **kwargs: Any) -> CompletionResponse:
        prompt_length = len(prompt)
        response = pipeline(prompt, max_new_tokens=num_output)[0]["generated_text"]

        # only return newly generated tokens
        text = response[prompt_length:]
        return CompletionResponse(text=text)
    
    def stream_complete(self, prompt: str, **kwargs: Any) -> CompletionResponseGen:
        raise NotImplementedError()

# define our LLM
llm = OurLLM()

service_context = ServiceContext.from_defaults(
    llm=llm, 
    context_window=context_window, 
    num_output=num_output
)

# Load the your data
documents = SimpleDirectoryReader('./data').load_data()
index = ListIndex.from_documents(documents, service_context=service_context)

# Query and print response
query_engine = index.as_query_engine()
response = query_engine.query("<query_text>")
print(response)
```

Using this method, you can use any LLM. Maybe you have one running locally, or running on your own server. As long as the class is implemented and the generated tokens are returned, it should work out. Note that we need to use the prompt helper to customize the prompt sizes, since every model has a slightly different context length.

Note that you may have to adjust the internal prompts to get good performance. Even then, you should be using a sufficiently large LLM to ensure it's capable of handling the complex queries that LlamaIndex uses internally, so your mileage may vary.

A list of all default internal prompts is available [here](https://github.com/jerryjliu/llama_index/blob/main/llama_index/prompts/default_prompts.py), and chat-specific prompts are listed [here](https://github.com/jerryjliu/llama_index/blob/main/llama_index/prompts/chat_prompts.py). You can also implement your own custom prompts, as described [here](/core_modules/service_modules/prompts.md).

