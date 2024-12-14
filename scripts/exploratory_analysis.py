import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO)

def exploratory_analysis():
    logging.info("Starting exploratory analysis.")

    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)

    # Load merged data
    try:
        data = pd.read_csv('data/merged_data.csv')
    except FileNotFoundError:
        logging.error("Merged data not found. Ensure data merging is completed.")
        return

    # 1. Location-based preferences
    location_preferences = data.groupby('Location')['Dish Name_x'].value_counts().unstack().fillna(0)
    location_preferences.to_csv('data/location_preferences.csv')
    logging.info("Location preferences saved.")

    # 2. Age distribution
    age_distribution = data['Age'].value_counts().sort_index()
    age_distribution.to_csv('data/age_distribution.csv')
    logging.info("Age distribution saved.")

    # 3. Favorite meal orders
    favorite_meal_orders = data.groupby('Favorite Meal')['Order ID'].count().reset_index()
    favorite_meal_orders.rename(columns={'Order ID': 'Number of Orders'}, inplace=True)
    favorite_meal_orders.to_csv('data/favorite_meal_orders.csv', index=False)
    logging.info("Favorite meal orders saved.")

    # 4. Correlation data
    logging.info("Checking available columns for correlation analysis.")
    logging.info(f"Available columns: {data.columns.tolist()}")  # Log available columns

    # Check if required columns exist
    required_columns = ['Duration (mins)', 'Total Orders']
    if not all(col in data.columns for col in required_columns):
        logging.error(f"Missing columns for correlation: {required_columns}")
        return  # Exit if required columns are missing

    correlation = data[required_columns].corr()
    correlation.to_csv('data/correlation.csv')
    logging.info("Correlation data saved.")

    # 5. Monthly orders
    data['Order Month'] = pd.to_datetime(data['Order Date']).dt.to_period('M')
    month_orders = data.groupby('Order Month')['Order ID'].count().reset_index()
    month_orders.to_csv('data/month_orders.csv', index=False)
    logging.info("Monthly orders saved.")

    # 6. Recommendations
    recommendations = data.groupby('Dish Name_x')['Order ID'].count().sort_values(ascending=False).head(10)
    recommendations.to_csv('data/recommendations.csv')
    logging.info("Recommendations saved.")

    # 7. Predicted orders (placeholder)
    predicted_orders = pd.DataFrame({
        'Month': ['2023-12', '2024-01'],
        'Predicted Orders': [500, 520]
    })
    predicted_orders.to_csv('data/predicted_orders.csv', index=False)
    logging.info("Predicted orders saved.")

    # 8. User segmentation
    segmentation = data.groupby('User ID_x')['Age'].count().reset_index()
    segmentation.rename(columns={'Age': 'Count'}, inplace=True)
    segmentation.to_csv('data/segmentation.csv', index=False)
    logging.info("User segmentation saved.")

    # 9. Sentiment analysis (placeholder)
    sentiment_analysis = pd.DataFrame({
        'Review': ['Good', 'Bad'],
        'Sentiment': ['Positive', 'Negative']
    })
    sentiment_analysis.to_csv('data/sentiment_analysis.csv', index=False)
    logging.info("Sentiment analysis saved.")

    logging.info("Exploratory analysis completed.")

if __name__ == "__main__":
    exploratory_analysis()
