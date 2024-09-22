
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '')))


from utils.preprocess import perform_eda


perform_eda('Data/myntra_products_catalog.csv')