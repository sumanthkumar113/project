import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def clean_data():
    logging.info("Starting data cleaning process.")
    
    # Load data
    user_details = pd.read_csv('data/UserDetails.csv')
    cooking_sessions = pd.read_csv('data/CookingSessions.csv')
    order_details = pd.read_csv('data/OrderDetails.csv')
    
    # Handle missing values
    user_details['Age'].fillna(user_details['Age'].median(), inplace=True)
    cooking_sessions['Duration (mins)'].fillna(cooking_sessions['Duration (mins)'].mean(), inplace=True)
    order_details['Rating'].fillna('N/A', inplace=True)
    
    # Remove duplicates
    user_details.drop_duplicates(inplace=True)
    cooking_sessions.drop_duplicates(inplace=True)
    order_details.drop_duplicates(inplace=True)
    
    # Save cleaned data
    user_details.to_csv('data/cleaned_UserDetails.csv', index=False)
    cooking_sessions.to_csv('data/cleaned_CookingSessions.csv', index=False)
    order_details.to_csv('data/cleaned_OrderDetails.csv', index=False)
    
    logging.info("Data cleaning completed.")

if __name__ == "__main__":
    clean_data()