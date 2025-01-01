import os
import time
from flask import (
    Flask,
    request,
    jsonify
)
from langchain_community.document_loaders.sitemap import SitemapLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from chat import chat, embedding

SITEMAP_URL = os.environ.get("SITEMAP_URL")
if SITEMAP_URL is None:
    raise ValueError("SITEMAP_URL is not set")

app = Flask(__name__)

model_name = "llama3.2:1b"

def load_documents():
    if os.getenv("AVOID_SSL_VERIFY", False):
        sitemap_loader = SitemapLoader(SITEMAP_URL, verify_ssl=False)
    else:
        sitemap_loader = SitemapLoader(SITEMAP_URL)
    docs = sitemap_loader.load()
    return docs


def sentences_as_chunks(chunk_size=512):
    text_splitter = RecursiveCharacterTextSplitter(  # Set a really small chunk size, just to show.
        chunk_size=chunk_size,
        chunk_overlap=0,
        length_function=len,
        is_separator_regex=False)
    return text_splitter.split_documents(load_documents())


def retriever():
    return Chroma.from_documents(documents=sentences_as_chunks(), embedding=embedding)

prompt_template = """"Use the following pieces of context to answer the question at the end.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    Use three sentences maximum and keep the answer as concise as possible.
    {context}
    Question: {question}
    Helpful Answer:
"""

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=prompt_template,
)

print("Building QA chain...")
start_time = time.time()
qa_chain = RetrievalQA.from_chain_type(chat, retriever=retriever().as_retriever(), chain_type_kwargs={"prompt": prompt})
print(f"QA chain built in {time.time() - start_time} seconds.")

@app.route("/api/predict")
def predict():
    query = request.args.get('q', '')
    result = qa_chain.invoke({"query": query})
    return jsonify(result)
