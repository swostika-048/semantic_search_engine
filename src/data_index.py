
# import sys
# import os
# import pandas as pd
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from elasticsearch import Elasticsearch
# from utils.preprocess import perform_eda,load_data
# from dotenv import load_dotenv
# from index.indexmapping import indexmapping
# from elasticsearch.helpers import bulk

# load_dotenv()

# es_host = os.getenv('ELASTICSEARCH_HOST')  
# es_port = int(os.getenv('ELASTICSEARCH_PORT'))
# es_scheme = os.getenv('ELASTICSEARCH_SCHEME')  
# print(es_scheme)
# es_user = os.getenv('ELASTICSEARCH_USER', None)
# es_password = os.getenv('ELASTICSEARCH_PASSWORD', None)

# es = Elasticsearch(
#     hosts=[{
#         'host': es_host,
#         'port': es_port,
#         'scheme': es_scheme
#     }])

# if es.ping():
#     print("Connected to Elasticsearch")
# else:
#     print("Could not connect to Elasticsearch")
    

# df= load_data("Data/myntra_products_catalog.csv")


# def retrieve_indexed_data(index_name):
    
#     query = {
#         "query": {
#             "match_all": {}
#         }
#     }

    
#     response = es.search(index=index_name, body=query, size=10000)
#     hits = response['hits']['hits']
#     data = [hit['_source'] for hit in hits]

#     df = pd.DataFrame(data)

#     return df


# def bulk_index_data(es, index_name, record_list):
#     actions = [
#         {
#             "_index": index_name,
#             "_id": record.get("ProductID", None),  # Use ProductID as the document ID, or let ES generate one
#             "_source": record
#         }
#         for record in record_list
#     ]

#     try:
#         success, failed = bulk(es, actions)
#         print(f"Successfully indexed {success} documents, {failed} failures.")
#     except Exception as e:
#         print(f"Error during bulk indexing: {e}")
        
        
        
# def encode_description_vectors(df, model):
#     """
#     Encode the 'Description' column into vectors using the provided model.
#     If 'DescriptionVector' already exists, it will return the existing vector.
    
#     Args:
#     df (pd.DataFrame): DataFrame containing 'Description' and optionally 'DescriptionVector' columns.
#     model: The model used for encoding descriptions into vectors.
    
#     Returns:
#     pd.DataFrame: DataFrame with the 'DescriptionVector' column updated or created.
#     """
    
#     df['DescriptionVector'] = df.apply(
#         lambda row: row['DescriptionVector'] if pd.notnull(row.get('DescriptionVector')) else model.encode(row['Description']),
#         axis=1
#     )
    
#     return df

# def record_list(df):
#     return df.to_dict("records")

# index_name = 'all_products'
# indexed_df = retrieve_indexed_data(index_name)
# print(indexed_df.head())
# # perform_eda('Data/myntra_products_catalog.csv')
# record_list=record_list(indexed_df)
# for record in record_list:
#     try:
#         es.index(index="all_products",document=record, id= record["ProductID"])
#     except Exception as e:
#             print(e)
# print(record_list[0])


import sys
import os
import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from dotenv import load_dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.preprocess import perform_eda, load_data
from index.indexmapping import indexmapping

# Load environment variables
load_dotenv()

# Elasticsearch connection details
es_host = os.getenv('ELASTICSEARCH_HOST')  
es_port = int(os.getenv('ELASTICSEARCH_PORT'))
es_scheme = os.getenv('ELASTICSEARCH_SCHEME')  
es_user = os.getenv('ELASTICSEARCH_USER', None)
es_password = os.getenv('ELASTICSEARCH_PASSWORD', None)


es = Elasticsearch(
    hosts=[{
        'host': es_host,
        'port': es_port,
        'scheme': es_scheme
    }],
    http_auth=(es_user, es_password) if es_user and es_password else None
)

# Test connection
if es.ping():
    print("Connected to Elasticsearch")
else:
    print("Could not connect to Elasticsearch")


# Load data (assuming your data is stored in a CSV file)
# df = load_data("Data/myntra_products_catalog.csv")
df = load_data("Data/product_data.csv")


def retrieve_indexed_data(index_name):
    query = {
        "query": {
            "match_all": {}
        }
    }

    response = es.search(index=index_name, body=query, size=10000)
    hits = response['hits']['hits']
    data = [hit['_source'] for hit in hits]

    return pd.DataFrame(data)


def bulk_index_data(es, index_name, records):
    """
    Bulk index data into Elasticsearch.
    
    Args:
        es: Elasticsearch client object.
        index_name: Name of the Elasticsearch index.
        records: List of dictionaries (records) to index.
    """
    actions = [
        {
            "_index": index_name,
            "_id": int(record.get("productid", None)),  # Use ProductID as the document ID, if available
            "_source": record
        }
        for record in records
    ]

    try:
        success, failed = bulk(es, actions)
        print(f"Successfully indexed {success} documents, {failed} failures.")
    except Exception as e:
        print(f"Error during bulk indexing: {e}")


# def bulk_index_data(es, index_name, records):
#     """
#     Bulk index data into Elasticsearch.
    
#     Args:
#         es: Elasticsearch client object.
#         index_name: Name of the Elasticsearch index.
#         records: List of dictionaries (records) to index.
#     """
#     actions = []
    
#     for record in records:
#         product_id = record.get("productid", None)
        
#         # Check if product_id is a string and convert it to an integer if valid
#         if isinstance(product_id, str) and product_id.isdigit():
#             product_id = int(product_id)
#         elif product_id is None:
#             product_id = None  # Keep it as None if not available
            
#         actions.append({
#             "_index": index_name,
#             "_id": product_id,  # Use ProductID as the document ID
#             "_source": record
#         })

#     try:
#         success, failed = bulk(es, actions)
#         print(f"Successfully indexed {success} documents, {failed} failures.")
#     except Exception as e:
#         print(f"Error during bulk indexing: {e}")


def encode_description_vectors(df, model):
    """
    Encode the 'Description' column into vectors using the provided model.
    
    Args:
    df (pd.DataFrame): DataFrame containing 'Description' and optionally 'DescriptionVector' columns.
    model: The model used for encoding descriptions into vectors.
    
    Returns:
    pd.DataFrame: DataFrame with the 'DescriptionVector' column updated or created.
    """
    df['DescriptionVector'] = df.apply(
        lambda row: row['DescriptionVector'] if pd.notnull(row.get('DescriptionVector')) else model.encode(row['Description']),
        axis=1
    )
    
    return df


def convert_to_record_list(df):
    """
    Convert the DataFrame into a list of dictionaries (records) for Elasticsearch indexing.
    
    Args:
    df (pd.DataFrame): DataFrame to convert.
    
    Returns:
    List[Dict]: List of records (dictionaries) to index.
    """
    return df.to_dict(orient="records")


# # Index name for Elasticsearch
# index_name = 'daraz_products'
# records=load_data('cleaned_file.csv')
# # bulk_index_data(es, index_name, records)
# try:
#     if not es.indices.exists(index="daraz_products"):
#         es.indices.create(index="daraz_products", body=indexmapping)
#         print("Index created successfully.")
#     else:
#         print("Index already exists.")
# except Exception as e:
#     print(f"Error creating index: {e}")


# # Retrieve existing data from the index (if any)
# indexed_df = retrieve_indexed_data(index_name)
# print(indexed_df.head())

# # Convert DataFrame to list of dictionaries
# record_list = convert_to_record_list(indexed_df)

# # Bulk index data into Elasticsearch
# bulk_index_data(es, index_name, record_list)

# # Print the first record for confirmation
# print(record_list[0])
