# import streamlit as st
# from src.main import search_similar_products, model
# from src.data_index import es  # Importing the necessary functions and objects
# from PIL import Image

# st.set_page_config(page_title="Product Recommendation", page_icon="🛍️", layout="wide")


# st.markdown("""
#     <style>
#         /* General layout styling */
#         .main { background-color: #f5f5f5; padding-top: 20px; }
#         h1, h3 { color: #FF6347; font-family: 'Arial', sans-serif; text-align: center; }
#         .result-card {
#             border-radius: 10px;
#             background-color: #ffffff;
#             padding: 20px;
#             margin-bottom: 20px;
#             box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
#             transition: transform 0.3s ease-in-out;
#         }
#         .result-card:hover {
#             transform: scale(1.02);
#         }
#         .stTextInput > div > div > input {
#             padding: 15px;
#             border-radius: 5px;
#             font-size: 16px;
#         }
#         footer {
#             margin-top: 50px;
#             text-align: center;
#             color: #808080;
#         }
#         /* Stylish sidebar */
#         [data-testid="stSidebar"] {
#             background-color: #f0f0f0;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Page Header
# st.title("🛍️ Product Recommendation System")
# st.write("Find the most relevant products for you. Simply describe what you're looking for!")

# # Sidebar for search settings
# with st.sidebar:
#     st.header("🔧 Search Settings")
#     st.write("Adjust your search criteria:")
    
#     # Slider for number of results
#     k = st.slider("Number of similar products to display:", min_value=1, max_value=10, value=5, step=1)
    
#     # Toggle dark/light mode for theme selection
#     theme = st.radio("Theme Selection", options=["Light", "Dark"], index=0)

#     # Provide a way to upload images if needed in future versions
#     st.markdown("---")
#     st.markdown("## 🌟 Upload Product Image (Coming Soon)")
#     uploaded_file = st.file_uploader("Choose an image...", type="jpg")

# # Apply selected theme
# if theme == "Dark":
#     st.markdown("""
#         <style>
#         body { background-color: #333; color: #fff; }
#         .stTextInput > div > div > input { color: #fff; background-color: #444; }
#         footer { color: #aaa; }
#         </style>
#     """, unsafe_allow_html=True)

# # Input box for the user to enter query
# st.markdown("## 🔍 Search for Products")
# user_input = st.text_input("Enter product description:", placeholder="e.g., Accessories for traditional men's wear", help="Describe the product you're searching for")

# # Show user progress and provide feedback
# if st.button("Search"):
#     if user_input:
#         with st.spinner('🔄 Searching for similar products...'):
#             results = search_similar_products(user_input, model, es, k=k)

#         if results:
#             st.success(f"🎉 Found {len(results)} similar products!")

#             # Display the results
#             cols = st.columns(2)  # Two-column layout for cards
#             for idx, result in enumerate(results):
#                 with cols[idx % 2]:
#                     st.markdown(f"""
#                         <div class='result-card'>
#                             <h3>{result['ProductName']}</h3>
#                             <p><b>Description:</b> {result['Description']}</p>
#                             <p><b>Score:</b> {result['Score']:.4f}</p>
#                         </div>
#                     """, unsafe_allow_html=True)

#                     # Optional: Add product image (placeholder for now)
#                     st.image("https://via.placeholder.com/200", caption="Product Image", use_column_width=True)
#                     st.markdown("---")
#         else:
#             st.warning("⚠️ No similar products found.")
#     else:
#         st.error("❗ Please enter a product description to search.")

# # Add a footer at the bottom
# st.markdown("""
#     <footer>
#         <p>Product Recommendation System © 2024 | Made with ❤️ by Your Team</p>
#     </footer>
# """, unsafe_allow_html=True)


import streamlit as st
from src.main import search_similar_products, model
from src.data_index import es  # Importing the necessary functions and objects
from PIL import Image

st.set_page_config(page_title="Product Recommendation", page_icon="🛍️", layout="wide")

# Custom CSS for styling the app
st.markdown("""
    <style>
        /* General layout styling */
        .main { background-color: #f5f5f5; padding-top: 20px; }
        h1, h3 { color: #FF6347; font-family: 'Arial', sans-serif; text-align: center; }
        .result-card {
            border-radius: 15px;
            background-color: #ffffff;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease-in-out;
            border-left: 5px solid #FF6347;
        }
        .result-card:hover {
            transform: scale(1.03);
            box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.15);
        }
        .stTextInput > div > div > input {
            padding: 15px;
            border-radius: 5px;
            font-size: 16px;
        }
        footer {
            margin-top: 50px;
            text-align: center;
            color: #808080;
        }
        /* Stylish sidebar */
        [data-testid="stSidebar"] {
            background-color: #f0f0f0;
        }
        /* Styling for price tag */
        .price-tag {
            font-size: 1.25em;
            color: #28a745;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Page Header
st.title("🛍️ Product Recommendation System")
st.write("Find the most relevant products for you. Simply describe what you're looking for!")

# Sidebar for search settings
with st.sidebar:
    st.header("🔧 Search Settings")
    st.write("Adjust your search criteria:")
    
    # Slider for number of results
    k = st.slider("Number of similar products to display:", min_value=1, max_value=10, value=5, step=1)
    
    # Toggle dark/light mode for theme selection
    theme = st.radio("Theme Selection", options=["Light", "Dark"], index=0)

    # Provide a way to upload images if needed in future versions
    st.markdown("---")
    st.markdown("## 🌟 Upload Product Image (Coming Soon)")
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

# Apply selected theme
if theme == "Dark":
    st.markdown("""
        <style>
        body { background-color: #333; color: #fff; }
        .stTextInput > div > div > input { color: #fff; background-color: #444; }
        footer { color: #aaa; }
        </style>
    """, unsafe_allow_html=True)

# Input box for the user to enter query
st.markdown("## 🔍 Search for Products")
user_input = st.text_input("Enter product description:", placeholder="e.g., Accessories for traditional men's wear", help="Describe the product you're searching for")

# Show user progress and provide feedback
if st.button("Search"):
    if user_input:
        with st.spinner('🔄 Searching for similar products...'):
            results = search_similar_products(user_input, model, es, k=k)

        if results:
            st.success(f"🎉 Found {len(results)} similar products!")

            # Display the results
            cols = st.columns(2)  # Two-column layout for cards
            for idx, result in enumerate(results):
                with cols[idx % 2]:
                    st.markdown(f"""
                        <div class='result-card'>
                            <h3>{result['ProductName']}</h3>
                            <p><b>Description:</b> {result['Description']}</p>
                            <p><b>Score:</b> {result['Score']:.4f}</p>
                            <p class='price-tag'>Price: ₹{result['Price']}</p>
                        </div>
                    """, unsafe_allow_html=True)

                    # Optional: Add product image (placeholder for now)
                    st.image("https://via.placeholder.com/200", caption="Product Image", use_column_width=True)
                    st.markdown("---")
        else:
            st.warning("⚠️ No similar products found.")
    else:
        st.error("❗ Please enter a product description to search.")

# Add a footer at the bottom
st.markdown("""
    <footer>
        <p>Product Recommendation System © 2024 | Made with ❤️ by Your Team</p>
    </footer>
""", unsafe_allow_html=True)
