import streamlit as st
import pandas as pd
import os
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns
import logging

logging.basicConfig(level=logging.INFO)

def save_uploaded_file(uploaded_file, folder="uploads"):
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def download_link(file_path, link_name):
    if not os.path.exists(file_path):
        st.warning(f"{file_path} not found. Please run the required process to generate it.")
        return
    with open(file_path, "rb") as f:
        file_bytes = BytesIO(f.read())
    return st.download_button(
        label=f"Download {link_name}",
        data=file_bytes,
        file_name=os.path.basename(file_path)
    )

def visualize_csv(file_path):
    if not os.path.exists(file_path):
        st.warning(f"{file_path} not found. Please run the required process to generate it.")
        return
    st.write(f"Visualizing {file_path}")
    data = pd.read_csv(file_path)
    st.dataframe(data.head())

    # Example visualization: histogram for numeric columns
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    if len(numeric_columns) > 0:
        fig, axes = plt.subplots(nrows=(len(numeric_columns) + 1) // 2, ncols=2, figsize=(12, len(numeric_columns) * 3))
        axes = axes.flatten()
        for i, col in enumerate(numeric_columns):
            sns.histplot(data[col], kde=True, ax=axes[i])
            axes[i].set_title(f"Distribution of {col}")
        for j in range(i + 1, len(axes)):
            axes[j].axis('off')  # Turn off unused subplots
        st.pyplot(fig)

# Streamlit UI
def main():
    st.title("Data Upload, Visualization, and Processing App")

    st.sidebar.header("Upload CSV Files")

    uploaded_files = {
        "OrderDetails": None,
        "CookingSessions": None,
        "UserDetails": None
    }

    for file_type in uploaded_files:
        uploaded_files[file_type] = st.sidebar.file_uploader(f"Upload {file_type}.csv", type="csv")

    if all(file is not None for file in uploaded_files.values()):
        st.success("All files uploaded successfully.")

        # Save files
        file_paths = {
            key: save_uploaded_file(file, folder="uploads") for key, file in uploaded_files.items()
        }

        # Buttons for processing
        if st.button("Run Data Cleaning"):
            import scripts.data_cleaning as data_cleaning  # Updated to reflect folder structure
            data_cleaning.clean_data()
            st.success("Data cleaning completed.")

        if st.button("Run Data Merging"):
            import scripts.data_merging as data_merging
            data_merging.merge_data()
            st.success("Data merging completed.")

        if st.button("Run Exploratory Analysis"):
            import scripts.exploratory_analysis as exploratory_analysis
            exploratory_analysis.exploratory_analysis()
            st.success("Exploratory analysis completed.")

        if st.button("Run Visualization"):
            visualize_csv('data/location_preferences.csv')
            visualize_csv('data/age_distribution.csv')
            visualize_csv('data/favorite_meal_orders.csv')
            visualize_csv('data/correlation.csv')  # Correlation
            visualize_csv('data/month_orders.csv')  # Monthly orders
            visualize_csv('data/recommendations.csv')  # Recommendations
            visualize_csv('data/predicted_orders.csv')  # Predictions
            visualize_csv('data/segmentation.csv')  # User segmentation
            visualize_csv('data/sentiment_analysis.csv')  # Sentiment analysis

        if st.button("Generate Report"):
            import scripts.report_generation as report_generation
            report_generation.generate_report()
            st.success("Report generated.")

        # Download processed files
        st.header("Download Processed Files")
        download_link('data/cleaned_UserDetails.csv', "Cleaned UserDetails")
        download_link('data/cleaned_CookingSessions.csv', "Cleaned CookingSessions")
        download_link('data/cleaned_OrderDetails.csv', "Cleaned OrderDetails")
        download_link('data/merged_data.csv', "Merged Data")
        download_link('data/location_preferences.csv', "Location Preferences")
        download_link('data/age_distribution.csv', "Age Distribution")
        download_link('data/favorite_meal_orders.csv', "Favorite Meal Orders")
        download_link('data/correlation.csv', "Correlation Data")
        download_link('data/month_orders.csv', "Monthly Orders")
        download_link('data/recommendations.csv', "Recommendations")
        download_link('data/predicted_orders.csv', "Predicted Orders")
        download_link('data/segmentation.csv', "User Segmentation")
        download_link('data/sentiment_analysis.csv', "Sentiment Analysis")
        download_link('reports/report.md', "Analysis Report")

if __name__ == "__main__":
    main()
