# semantic_search_engine
- [semantic\_search\_engine](#semantic_search_engine)
  - [Overview](#overview)
  - [Key features:](#key-features)
  - [Project Structure](#project-structure)
  - [Getting started:](#getting-started)
    - [Prerequisites:](#prerequisites)
    - [Installation](#installation)
    - [|Running the Application](#running-the-application)
  - [Data Visualization](#data-visualization)

## Overview
This project implements a Semantic Search Engine that goes beyond traditional keyword matching by understanding the meaning of search queries using Natural Language Processing (NLP). It leverages advanced machine learning models to encode text into vector embeddings, enabling more accurate and relevant search results based on semantic similarity. The search engine is built using Elasticsearch and a Transformer-based model like Sentence-BERT.
## Key features:
- **Semantic Understanding**: instead of matching exact words, the engine interprets the meaning behind the query, improving search relevance.
- **Vector Search:** Text documents and search queries are encoded into high-dimensional vectors, allowing similarity-based retrieval using K-Nearest Neighbors (KNN) search.
- **Efficient Search with Elasticsearch:** The project integrates with Elasticsearch, a scalable search engine that supports vector indexing and querying.
- **Text Encoding:** Utilizes SentenceTransformer models to convert product descriptions or documents into vector embeddings.
-**KNN Search:** Enables finding the most semantically similar items by comparing the encoded query to indexed vectors.

## Project Structure
semantic_search_engine/  
├── Data  
│   └── myntra_products_catalog.csv  
├── index  
│   └── indexmapping.py  
├── index.ipynb  
├── project_structure.txt  
├── README.md  
├── src  
│   ├── data_index.py    
│   └── main.py  
└── utils  
│   └── preprocess.py   
## Getting started:
### Prerequisites:
### Installation
### |Running the Application
## Data Visualization