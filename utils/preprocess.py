import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer

def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path)
    
def data_overview(df):
    """Get an overview of the dataset: head, info, and missing values."""
    print("First 5 rows of the dataset:")
    print(df.head())
    
    print("\nData types and missing values:")
    print(df.info())
    
    print("\nNumber of missing values per column:")
    print(df.isnull().sum())
    
    
def summary_statistics(df, numeric_columns):
    """Print summary statistics for numeric columns."""
    print("Summary statistics for numeric columns:")
    print(df[numeric_columns].describe())
    
    
def handle_missing_values(df, strategy='fill', fill_value='Unknown'):
    """Handle missing values by either filling or dropping."""
    if strategy == 'fill':
        df_filled = df.fillna(fill_value)
        return df_filled
    elif strategy == 'drop':
        df_dropped = df.dropna()
        return df_dropped
    else:
        print("Invalid strategy! Choose 'fill' or 'drop'.")

def unique_values(df, categorical_columns):
    """Print unique values in each categorical column."""
    for column in categorical_columns:
        print(f"Unique values in {column}:")
        print(df[column].unique())
        print("\n")


def plot_distribution(df, column_name, plot_type='hist'):
    """Plot the distribution of a numeric column."""
    plt.figure(figsize=(10, 6))
    if plot_type == 'hist':
        sns.histplot(df[column_name], kde=True)
        plt.title(f'Distribution of {column_name}')
    elif plot_type == 'count':
        sns.countplot(x=column_name, data=df)
        plt.title(f'Count of {column_name}')
    plt.show()
    
    
def correlation_matrix(df, numeric_columns):
    """Plot the correlation matrix for numeric columns."""
    corr_matrix = df[numeric_columns].corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()


def word_frequency_analysis(df, text_column, top_n=10):
    """Perform word frequency analysis on a text column."""
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df[text_column])
    
    # Summing up the occurrences of each word
    sum_words = X.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    
    print(f"Top {top_n} most frequent words:")
    for word, freq in words_freq[:top_n]:
        print(f"{word}: {freq}")


def plot_word_frequency(df, column, top_n=20):
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df[column])
    word_freq = X.sum(axis=0)
    words = [(word, word_freq[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
    words = sorted(words, key=lambda x: x[1], reverse=True)[:top_n]
    words, freqs = zip(*words)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=list(freqs), y=list(words))
    plt.title(f'Top {top_n} Words in {column}')
    plt.show()

        
def category_count_plot(df, column_name):
    """Plot the count of unique values in a categorical column."""
    plt.figure(figsize=(10, 6))
    sns.countplot(x=column_name, data=df, order=df[column_name].value_counts().index)
    plt.xticks(rotation=45)
    plt.title(f'Count of {column_name}')
    plt.show()


def perform_eda(file_path):
    """Perform EDA on the product data."""
    df = load_data(file_path)
    
    # Overview
    data_overview(df)
    
    # Summary statistics
    numeric_columns = ['Price (INR)', 'NumImages']
    summary_statistics(df, numeric_columns)
    
    # Handle missing values
    df_cleaned = handle_missing_values(df, strategy='fill', fill_value='Unknown')
    
    # Unique values in categorical columns
    categorical_columns = ['ProductBrand', 'Gender', 'PrimaryColor']
    unique_values(df_cleaned, categorical_columns)
    
    # Distribution of numeric columns
    plot_distribution(df_cleaned, 'Price (INR)', plot_type='hist')
    
    # Correlation matrix
    correlation_matrix(df_cleaned, numeric_columns)
    
    # Word frequency analysis in product descriptions
    word_frequency_analysis(df_cleaned, 'Description', top_n=10)
    plot_word_frequency(df_cleaned, 'Description', top_n=20)
    
    # Category count for Gender
    category_count_plot(df_cleaned, 'Gender')

# Example usage
perform_eda('Data/myntra_products_catalog.csv')
