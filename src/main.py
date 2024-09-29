from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch
import numpy as np
from src.data_index import es  

model = SentenceTransformer("all-mpnet-base-v2")


def search_similar_products(input_text, model, es=es, index_name="daraz_products", field_name="DescriptionVector", k=5, num_candidates=500):
    """
    Search for products in Elasticsearch similar to the input description using KNN search.
    
    Args:
    input_text (str): The input description to search for similar products.
    model: The model used for encoding the input text into a vector.
    es (Elasticsearch): Elasticsearch client instance.
    index_name (str): Name of the Elasticsearch index.
    field_name (str): The field in the index containing the vectors (default is "DescriptionVector").
    k (int): Number of nearest neighbors to return (default is 5).
    num_candidates (int): Maximum number of candidates to consider (default is 500).
    
    Returns:
    list: List of search results (product names, links, and prices).
    """
    try:
        # Validate input
        if not input_text or not isinstance(input_text, str):
            raise ValueError("Invalid input text. Please provide a non-empty string.")
        
        print(f"Encoding input: {input_text}")
        vector_of_input = model.encode(input_text).tolist()  # Convert to list

        # Prepare the KNN search query
        query = {
            "field": field_name,
            "query_vector": vector_of_input,
            "k": k,
            "num_candidates": num_candidates,
        }

        # Check Elasticsearch connection
        if not es.ping():
            raise ConnectionError("Unable to connect to Elasticsearch cluster. Please check the connection.")

        print(f"Searching for similar products in index '{index_name}'...")
        res = es.knn_search(index=index_name, knn=query, _source=["link", "product_title", "price"])

        # Extract hits from the response
        hits = res.get("hits", {}).get("hits", [])
        if not hits:
            print(f"No similar products found for the input: {input_text}")
            return []

        # Process the search results
        results = [{
            "ProductName": hit["_source"].get("product_title", "Unknown"),
            "link": hit["_source"].get("link", "nolink"),
            "Score": hit.get("_score", 0),  # Score might not be available in _source
            "Price": hit["_source"].get("price", 0)
        } for hit in hits]

        print(f"Found {len(results)} similar products.")
        return results

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except ConnectionError as ce:
        print(f"ConnectionError: {ce}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return []

# # Search for similar products
# results = search_similar_products("laptops vivobook", model, es)

# if results:
#     print(f"Results found: {len(results)}")
#     for product in results:
#         print(f"Product Name: {product['ProductName']}, link: {product['link']}, Price: {product['Price']}")
# else:
#     print("No results found or an error occurred.")
