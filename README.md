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
1. Python 3.9+
2. Elasticsearch (Version 8.x recommended)
3. Virtual Environment (Optional, but recommended)
### Installation
1. Clone the repository:
    ```
    git clone https://github.com/swostika-048/semantic_search_engine.git
    cd semantic_search_engine

    ```
2. Create and activate a virtual environment (optional):
    ``` 
    python3 -m venv venv
    On linux:source venv/bin/activate  
    On Windows: venv\Scripts\activate

    ```
3. Install the dependencies:
   ``` 
   pip install -r requirements.txt
    ```
4. Set up environment variables in the .env file:
   ``` 
    ELASTICSEARCH_HOST=hostname      
    ELASTICSEARCH_PORT=portnumber
    ELASTICSEARCH_USER=username
    ELASTICSEARCH_PASSWORD=password

    # change hostname, portnumber,username,password with the elatiscsearch server hostname portnumber username and password
    ```
### |Running the Application
1. Start Elasticsearch: Ensure that Elasticsearch server is running.
2. run app.py
## Data Visualization