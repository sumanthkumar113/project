import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

logging.basicConfig(level=logging.INFO)

def visualize_data():
    logging.info("Starting visualization process.")
    
    # Load demographic analysis data
    location_preferences = pd.read_csv('data/location_preferences.csv')
    age_distribution = pd.read_csv('data/age_distribution.csv')
    favorite_meal_orders = pd.read_csv('data/favorite_meal_orders.csv')
    
    # Ensure location_preferences contains only numeric data
    location_preferences = location_preferences.apply(pd.to_numeric, errors='coerce')
    
    # Drop rows or columns with NaN values if necessary
    location_preferences = location_preferences.dropna()
    
    # Check if location_preferences is empty
    if location_preferences.empty:
        logging.error("Location preferences data is empty after processing.")
        return  # Exit the function if there's no data
    
    # 1. Location-based preferences heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(location_preferences, cmap='Blues', annot=True, fmt='g')
    plt.title('Location-wise Cooking Preferences')
    plt.xlabel('Dish Name')
    plt.ylabel('Location')
    plt.savefig('visualizations/location_preferences.png')
    plt.close()
    
    # 2. Age distribution histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(age_distribution['Age'], bins=10, kde=True)
    plt.title('Age Distribution of Users')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.savefig('visualizations/age_distribution.png')
    plt.close()
    
    # 3. Favorite meal vs number of orders bar chart
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Favorite Meal', y='Number of Orders', data=favorite_meal_orders)
    plt.title('Favorite Meal vs Number of Orders')
    plt.xlabel('Favorite Meal')
    plt.ylabel('Number of Orders')
    plt.savefig('visualizations/favorite_meal_orders.png')
    plt.close()
    
    logging.info("Visualization process completed.")

if __name__ == "__main__":
    visualize_data()