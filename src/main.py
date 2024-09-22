from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch
import numpy as np
from data_index import es  

model = SentenceTransformer("all-mpnet-base-v2")

def search_similar_products(input_text, model, es=es, index_name="all_products", field_name="DescriptionVector", k=5, num_candidates=500):
    """
    Search for products in Elasticsearch similar to the input description using KNN search.
    
    Args:
    input_text (str): The input description to search for similar products.
    model: The model used for encoding the input text into a vector.
    es (Elasticsearch): Elasticsearch client instance.
    index_name (str): Name of the Elasticsearch index.
    field_name (str): The field in the index containing the vectors (default is "DescriptionVector").
    k (int): Number of nearest neighbors to return (default is 2).
    num_candidates (int): Maximum number of candidates to consider (default is 500).
    
    Returns:
    list: List of search results (product names and descriptions).
    """
    
    try:
        
        if not input_text or not isinstance(input_text, str):
            raise ValueError("Invalid input text. Please provide a non-empty string.")
        
        
        print(f"Encoding input: {input_text}")
        vector_of_input = model.encode(input_text)

        
        query = {
            "field": field_name,
            "query_vector": vector_of_input,
            "k": k,
            "num_candidates": num_candidates
        }

        
        if not es.ping():
            raise ConnectionError("Unable to connect to Elasticsearch cluster. Please check the connection.")

        
        print(f"Searching for similar products in index '{index_name}'...")
        res = es.knn_search(index=index_name, knn=query, _source=["ProductName", "Description"])

        
        hits = res.get("hits", {}).get("hits", [])
        if not hits:
            print(f"No similar products found for the input: {input_text}")
            return []

        
        results = [{"ProductName": hit["_source"].get("ProductName", "Unknown"), 
                    "Description": hit["_source"].get("Description", "No Description")}
                   for hit in hits]
        print(f"Found {len(results)} similar products.")
        return results

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except ConnectionError as ce:
        print(f"ConnectionError: {ce}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    
    return []



results = search_similar_products("traditional kurties", model, es, "all_products")

if results:
    print(f"Results found: {len(results)}")
    for product in results:
        print(f"Product Name: {product['ProductName']}, Description: {product['Description']}")
else:
    print("No results found or an error occurred.")
