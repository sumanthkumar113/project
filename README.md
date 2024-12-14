

https://github.com/user-attachments/assets/a27aca0a-05b9-43f2-981d-e4442c9cb329



https://github.com/user-attachments/assets/564cd0a7-35fc-4edb-889a-52302bd231d5

# Data Analytics and Visualization App

## Project Overview

This Streamlit-based application is designed to facilitate comprehensive data analytics, visualization, and reporting. It provides a user-friendly interface for uploading, processing, and analyzing CSV data with advanced features for insights generation.

## 🌟 Key Features

- **File Upload**: Easy upload of multiple CSV files
- **Data Cleaning**: Robust data preprocessing
- **Data Merging**: Combine multiple datasets seamlessly
- **Exploratory Analysis**: Generate in-depth insights including:
  - Location-based preferences
  - Age distribution analysis
  - Favorite meals and order trends
  - User segmentation
  - Sentiment analysis
  - Correlation studies

- **Advanced Visualizations**: Comprehensive graphical representations
- **Report Generation**: Markdown reports summarizing key findings
- **Data Export**: Download processed datasets and reports
- 
- **PLEASE CHECK OUT THE VIDEO FOR COMPLETE DEMO
- 
## 📂 Project Structure

```
project-root/
|-- data/
|   |-- OrderDetails.csv          # Original order details file
|   |-- CookingSessions.csv       # Original cooking sessions file
|   |-- UserDetails.csv           # Original user details file
|   |-- cleaned_UserDetails.csv   # Cleaned user details file
|   |-- cleaned_CookingSessions.csv   # Cleaned cooking sessions file
|   |-- cleaned_OrderDetails.csv  # Cleaned order details file
|   |-- merged_data.csv           # Final merged dataset
|   |-- location_preferences.csv  # Generated location preferences data
|   |-- age_distribution.csv      # Generated age distribution data
|   |-- favorite_meal_orders.csv  # Generated favorite meal orders data
|   |-- correlation.csv           # Correlation data
|   |-- month_orders.csv          # Monthly order trends data
|   |-- recommendations.csv       # Recommendations data
|   |-- predicted_orders.csv      # Predicted orders data
|   |-- segmentation.csv          # User segmentation data
|   |-- sentiment_analysis.csv    # Sentiment analysis data
|
|-- reports/
|   |-- report.md                 # Markdown report summarizing findings
|
|-- scripts/
|   |-- data_cleaning.py          # Script for cleaning data
|   |-- data_merging.py           # Script for merging datasets
|   |-- exploratory_analysis.py   # Script for exploratory analysis
|   |-- report_generation.py      # Script for generating reports
|   |-- app.py                    # Main Streamlit application script
|
|-- uploads/                      # Folder for user-uploaded files
|
|-- visualizations/               # Folder for generated visualizations
|   |-- location_preferences.png
|   |-- age_distribution.png
|   |-- favorite_meal_orders.png
|   |-- correlation.png
|   |-- month_orders.png
|   |-- recommendations.png
|   |-- predicted_orders.png
|   |-- segmentation.png
|   |-- sentiment_analysis.png
|
|-- .streamlit/                   # Streamlit configuration files
|-- README.md                     # Project documentation
```

## 🛠 Prerequisites

- Python 3.8+
- pip (Python package manager)

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/data-analytics-app.git
   cd data-analytics-app
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install numpy pandas seaborn plotly matplotlib scikit-learn
   ```

## 💡 Usage

1. Upload required files:
   - `OrderDetails.csv`
   - `CookingSessions.csv`
   - `UserDetails.csv`

2. Use sidebar buttons to:
   - Clean data
   - Merge datasets
   - Perform exploratory analysis
   - Visualize results
   - Generate reports

3. Download processed data or reports as needed

## 🔧 Customization

Extend functionality by modifying:
- `scripts/data_cleaning.py`: Add custom cleaning rules
- `scripts/exploratory_analysis.py`: Add new insights or visualizations
- `scripts/report_generation.py`: Customize report content

## 📊 Sample Outputs

- Cleaned datasets
- Merged data
- Visualization charts
- Markdown reports with insights

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## 📧 Contact

Sumanth Kumar - [sumanthk1313@gmail.com](mailto:sumanthk1313@gmail.com)
