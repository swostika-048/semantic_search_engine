# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.feature_extraction.text import CountVectorizer

# def load_data(file_path):
#     """Load the dataset from a CSV file."""
#     return pd.read_csv(file_path)
    
# def data_overview(df):
#     """Get an overview of the dataset: head, info, and missing values."""
#     print("First 5 rows of the dataset:")
#     print(df.head())
    
#     print("\nData types and missing values:")
#     print(df.info())
    
#     print("\nNumber of missing values per column:")
#     print(df.isnull().sum())
    
    
# def summary_statistics(df, numeric_columns):
#     """Print summary statistics for numeric columns."""
#     print("Summary statistics for numeric columns:")
#     print(df[numeric_columns].describe())
    
    
# def handle_missing_values(df, strategy='fill', fill_value='Unknown'):
#     """Handle missing values by either filling or dropping."""
#     if strategy == 'fill':
#         df_filled = df.fillna(fill_value)
#         return df_filled
#     elif strategy == 'drop':
#         df_dropped = df.dropna()
#         return df_dropped
#     else:
#         print("Invalid strategy! Choose 'fill' or 'drop'.")

# def unique_values(df, categorical_columns):
#     """Print unique values in each categorical column."""
#     for column in categorical_columns:
#         print(f"Unique values in {column}:")
#         print(df[column].unique())
#         print("\n")


# def plot_distribution(df, column_name, plot_type='hist'):
#     """Plot the distribution of a numeric column."""
#     plt.figure(figsize=(10, 6))
#     if plot_type == 'hist':
#         sns.histplot(df[column_name], kde=True)
#         plt.title(f'Distribution of {column_name}')
#     elif plot_type == 'count':
#         sns.countplot(x=column_name, data=df)
#         plt.title(f'Count of {column_name}')
#     plt.show()
    
    
# def correlation_matrix(df, numeric_columns):
#     """Plot the correlation matrix for numeric columns."""
#     corr_matrix = df[numeric_columns].corr()
#     plt.figure(figsize=(10, 6))
#     sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
#     plt.title('Correlation Matrix')
#     plt.show()


# def word_frequency_analysis(df, text_column, top_n=10):
#     """Perform word frequency analysis on a text column."""
#     vectorizer = CountVectorizer(stop_words='english')
#     X = vectorizer.fit_transform(df[text_column])
    
#     # Summing up the occurrences of each word
#     sum_words = X.sum(axis=0)
#     words_freq = [(word, sum_words[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
#     words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    
#     print(f"Top {top_n} most frequent words:")
#     for word, freq in words_freq[:top_n]:
#         print(f"{word}: {freq}")


# def plot_word_frequency(df, column, top_n=20):
#     vectorizer = CountVectorizer(stop_words='english')
#     X = vectorizer.fit_transform(df[column])
#     word_freq = X.sum(axis=0)
#     words = [(word, word_freq[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
#     words = sorted(words, key=lambda x: x[1], reverse=True)[:top_n]
#     words, freqs = zip(*words)
    
#     plt.figure(figsize=(10, 6))
#     sns.barplot(x=list(freqs), y=list(words))
#     plt.title(f'Top {top_n} Words in {column}')
#     plt.show()

        
# def category_count_plot(df, column_name):
#     """Plot the count of unique values in a categorical column."""
#     plt.figure(figsize=(10, 6))
#     sns.countplot(x=column_name, data=df, order=df[column_name].value_counts().index)
#     plt.xticks(rotation=45)
#     plt.title(f'Count of {column_name}')
#     plt.show()


# def perform_eda(file_path):
#     """Perform EDA on the product data."""
#     df = load_data(file_path)
    
#     print("====================data overview===========================")
#     data_overview(df)
    
#     print("===================summary statistics=======================")
#     numeric_columns = ['price', 'actual_price']
#     summary_statistics(df, numeric_columns)
    
#     # Handle missing values
#     df_cleaned = handle_missing_values(df, strategy='fill', fill_value='Unknown')
    
#     # Unique values in categorical columns
#     categorical_columns = ['Product_title', 'ratins', 'color']
#     unique_values(df_cleaned, categorical_columns)
    
#     # Distribution of numeric columns
#     plot_distribution(df_cleaned, 'price', plot_type='hist')
    
#     # Correlation matrix
#     correlation_matrix(df_cleaned, numeric_columns)
    
#     # Word frequency analysis in product descriptions
#     word_frequency_analysis(df_cleaned, 'product_title', top_n=10)
#     plot_word_frequency(df_cleaned, 'product_title', top_n=20)
    
#     # Category count for Gender
#     category_count_plot(df_cleaned, 'ratings')


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
        df_filled.index.name = 'productid'
        df_filled.to_csv('cleaned_file.csv', index=True)
        return df_filled
    elif strategy == 'drop':
        df_dropped = df.dropna()
        df_dropped.index.name = 'productid'
        df_dropped.to_csv('cleaned_file.csv', index=True)
        return df_dropped
    else:
        print("Invalid strategy! Choose 'fill' or 'drop'.")

def unique_values(df, categorical_columns):
    """Print unique values in each categorical column."""
    for column in categorical_columns:
        print(f"Unique values in {column}:")
        print(df[column].unique())
        print("\n")

# def plot_distribution(df, column_name, plot_type='hist', save=False, file_name='distribution_plot.png'):
#     """Plot the distribution of a numeric column and save if required."""
#     plt.figure(figsize=(10, 6))
#     if plot_type == 'hist':
#         sns.histplot(df[column_name], kde=True)
#         plt.title(f'Distribution of {column_name}')
#     elif plot_type == 'count':
#         sns.countplot(x=column_name, data=df)
#         plt.title(f'Count of {column_name}')
    
#     if save:
#         plt.savefig(file_name)
#         print(f"Plot saved as {file_name}")
    
#     plt.show()

def clean_price_column(df, column_name):
    """Clean the price column by removing currency symbols and commas, and convert to numeric."""
    df[column_name] = df[column_name].replace({'Rs. ': '', ',': ''}, regex=True)
    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
    return df


def plot_distribution(df, column_name, plot_type='hist', save=False, file_name='distribution_plot.png', bin_count=10):
    """
    Plot the distribution of a numeric column, divide values into bins, and save if required.
    
    Parameters:
    - df: DataFrame containing the data.
    - column_name: The name of the column to plot.
    - plot_type: The type of plot ('hist' for histogram or 'count' for count plot).
    - save: Whether to save the plot as a file (default is False).
    - file_name: The name of the file to save the plot (default is 'distribution_plot.png').
    - bin_count: Number of bins for the histogram (default is 10).
    """
    plt.figure(figsize=(10, 6))
    
    # Get the min and max of the column for binning
    min_value = df[column_name].min()
    max_value = df[column_name].max()
    
    # Create bins based on the range and specified bin count
    bins = list(range(int(min_value), int(max_value) + (int((max_value - min_value) / bin_count)), int((max_value - min_value) / bin_count)))
    
    if plot_type == 'hist':
        sns.histplot(df[column_name], bins=bins, kde=True)
        plt.title(f'Distribution of {column_name}')
        plt.xlabel(f'{column_name} (Binned)')
        plt.ylabel('Count')
    elif plot_type == 'count':
        sns.countplot(x=column_name, data=df)
        plt.title(f'Count of {column_name}')
    
    # Optionally save the plot
    if save:
        plt.savefig(file_name)
        print(f"Plot saved as {file_name}")
    
    # Show the plot
    plt.show()



def correlation_matrix(df, numeric_columns, save=False, file_name='correlation_matrix.png'):
    """Plot the correlation matrix for numeric columns and save if required."""
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')  
    corr_matrix = df[numeric_columns].corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    
    if save:
        plt.savefig(file_name)
        print(f"Correlation matrix saved as {file_name}")
    
    plt.show()

def plot_word_frequency(df, column, top_n=20, save=False, file_name='word_frequency.png'):
    """Plot the word frequency for a text column and save if required."""
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df[column].astype(str))
    word_freq = X.sum(axis=0)
    words = [(word, word_freq[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
    words = sorted(words, key=lambda x: x[1], reverse=True)[:top_n]
    words, freqs = zip(*words)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=list(freqs), y=list(words))
    plt.title(f'Top {top_n} Words in {column}')
    
    if save:
        plt.savefig(file_name)
        print(f"Word frequency plot saved as {file_name}")
    
    plt.show()



def category_count_plot(df, column_name, save=False, file_name='category_count_plot.png'):
    """Plot the count of unique values in a categorical column and save if required."""
    
    # Check if the column is ratings and process accordingly
    if column_name == 'ratings':
        # Extract numeric ratings from the string format
        df[column_name] = df[column_name].str.extract('(\d+)')[0]
        
        # Fill NaN values with 0
        df[column_name] = df[column_name].fillna(0).astype(int)
    
    # Set up the plot
    plt.figure(figsize=(10, 6))
    
    # Create count plot with ratings sorted in ascending order
    sns.countplot(x=column_name, data=df, order=sorted(df[column_name].unique()))
    plt.xticks(rotation=45)
    plt.title(f'Count of {column_name}')
    
    # Save the plot if required
    if save:
        plt.savefig(file_name)
        print(f"Category count plot saved as {file_name}")
    
    plt.show()

def perform_eda(file_path):
    """Perform EDA on the product data and save plots as needed."""
    df = load_data(file_path)
    
    print("==================== Data Overview ===========================")
    data_overview(df)
    
    print("=================== Summary Statistics =======================")
    numeric_columns = ['price', 'actual_price']
    summary_statistics(df, numeric_columns)
    
    print("=================== Handling Missing Values ==================")
    df_cleaned = handle_missing_values(df, strategy='drop', fill_value='Unknown')
    print(df_cleaned)
    # print(df_cleaned.isna().value_counts())
    df_cleaned=clean_price_column(df=df_cleaned, column_name='price')
    print(df_cleaned)
    
    print("=================== Unique Categorical Values =================")
    categorical_columns = ['product_title', 'ratings', 'color']
    unique_values(df_cleaned, categorical_columns)
    
    print("=================== Distribution Plots ========================")
    plot_distribution(df_cleaned, 'price', plot_type='hist', save=True, file_name='price_distribution.png')
   
    
    print("=================== Correlation Matrix ========================")
    correlation_matrix(df_cleaned, numeric_columns, save=True, file_name='correlation_matrix.png')
    
    print("=================== Word Frequency Analysis ===================")
    plot_word_frequency(df_cleaned, 'product_title', top_n=20, save=True, file_name='word_frequency_plot.png')
    
    print("=================== Category Count Plot =======================")
    category_count_plot(df_cleaned, 'ratings', save=True, file_name='ratings_count_plot.png')



# perform_eda('Data/product_data.csv')


