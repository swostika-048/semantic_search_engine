

indexmapping={
  "mappings": {
    "properties": {
      "productid": {
        "type": "long"
      },
      "product_title": {
        "type": "text"
      },
      "link": {
        "type": "keyword"
      },
      # "ProductBrand": {
      #   "type": "text"
      # },
      "price": {
        "type": "long"
      },
      "actualprice": {
        "type": "long",
        "null_value": 0
      },
      "ratings": {
        "type": "integer"
      },
      "color": {
        "type": "text"
      },
      "DescriptionVector": {
        "type": "dense_vector",
        "dims": 768,
        "index": True,
        "similarity": "l2_norm"
      }
    }
  }
}
