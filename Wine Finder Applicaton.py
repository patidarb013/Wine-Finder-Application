import streamlit as st
import re
import pandas as pd

# Load the merged dataset
merged_df = pd.read_csv('/Users/bhaveshpatidar/Desktop/merged_data.csv')  

# Remove non-numeric characters from 'weight' column and convert to float
merged_df['weight'] = merged_df['weight'].replace('[^\d.]', '', regex=True).astype(float)

# Set page title
st.set_page_config(page_title="Wine Emporium")

# Create navigation between pages
page = st.sidebar.radio("Navigation", ["Home", "Filtered Wine List"])

# Render selected page
if page == "Home":
    # Display application name and tagline in cursive font
    st.markdown(
        """
        <div style="background-color:#f63366;padding:10px;border-radius:10px">
            <h1 style="font-family:cursive;color:white;text-align:center;">Wine Emporium</h1>
            <h2 style="font-family:cursive;color:white;text-align:right;font-size:18px;">~Right Type of Wine For You</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    # Display wine photo on the front page
    st.image('/Users/bhaveshpatidar/Desktop/wine photo.jpg', use_column_width=True)
elif page == "Filtered Wine List":
    # Page 2: Filtered Wine List
    st.write("# Filtered Wine List")
    
    # Sidebar title and description
    st.sidebar.title("Wine Finder")
    st.sidebar.write("Find the right wine for you!")

    # Sidebar filters
    min_rating = st.sidebar.slider("Minimum Rating", min_value=0.0, max_value=5.0, value=0.0, step=0.1)
    max_weight = st.sidebar.number_input("Maximum Weight (lbs)", min_value=0.0)

    # Filter the dataset based on user inputs
    filtered_df = merged_df[(merged_df['reviews.rating'] >= min_rating) & (merged_df['weight'] <= max_weight)]
    
    st.write(filtered_df)
