from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
import os
import openai

api_key = os.environ['OPENAI_API_KEY']
openai.api_key=api_key

class CustomVectorstoreIndexCreator(VectorstoreIndexCreator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.engine = openai.Engine(api_key=api_key)

    def get_vectors(self, documents):
        vectors = []
        for document in documents:
            text = self.engine.encode(document)
            vectors.append(text)
        return vectors

index = CustomVectorstoreIndexCreator().from_loaders([TextLoader('test.txt')])
query = "What do whales like to eat?"
index.query_with_sources(query)
