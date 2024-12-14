import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def merge_data():
    logging.info("Starting data merging process.")
    
    # Load cleaned data
    user_details = pd.read_csv('data/cleaned_UserDetails.csv')
    cooking_sessions = pd.read_csv('data/cleaned_CookingSessions.csv')
    order_details = pd.read_csv('data/cleaned_OrderDetails.csv')
    
    # Validate data consistency
    if not user_details['User ID'].is_unique:
        raise ValueError("Duplicate User IDs found in UserDetails.")
    if not cooking_sessions['Session ID'].is_unique:
        raise ValueError("Duplicate Session IDs found in CookingSessions.")
    if not order_details['Order ID'].is_unique:
        raise ValueError("Duplicate Order IDs found in OrderDetails.")
    
    # Merge data
    merged_user_sessions = pd.merge(user_details, cooking_sessions, on='User ID', how='inner')
    final_data = pd.merge(merged_user_sessions, order_details, on='Session ID', how='left')
    
    # Save merged data
    final_data.to_csv('data/merged_data.csv', index=False)
    
    logging.info("Data merging completed.")

if __name__ == "__main__":
    merge_data()