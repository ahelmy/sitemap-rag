import os
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama

LANGCHAIN_SERVER = os.environ.get("LANGCHAIN_SERVER")
if LANGCHAIN_SERVER is None:
    raise ValueError("LANGCHAIN_SERVER is not set")

MODEL_NAME = 'llama3.2:1b'
embedding = OllamaEmbeddings(model=MODEL_NAME, base_url=LANGCHAIN_SERVER)   
chat = ChatOllama(model=MODEL_NAME, base_url=LANGCHAIN_SERVER)