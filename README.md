# Sitemap RAG
SitemapRAG is an open-source tool designed to leverage your website's sitemap as a Retrieval-Augmented Generation (RAG) source. It empowers developers to build intelligent, context-aware applications by extracting, indexing, and querying content directly from a sitemap.

With SitemapRAG, you can seamlessly integrate structured website content into applications like chatbots, search tools, or recommendation engines, enhancing the relevance and accuracy of responses.

## Features
- Automated Sitemap Parsing: Effortlessly crawl and index all URLs in your sitemap.
- Content Retrieval: Extract key information or text from web pages to create a knowledge base.
- RAG Integration: Use the indexed content for Retrieval-Augmented Generation tasks.
- Flexible Storage: Choose between in-memory, file-based, or vector database storage for embeddings.
- Multilingual Support: Handle multilingual content with ease.
- Pluggable Models: Compatible with popular LLMs like GPT or custom fine-tuned models.
- Real-time Updates: Sync with sitemap changes to keep the knowledge base current.


## Installation
```bash
pip install -r requirements.txt
flask --app main run -p 8000 
```