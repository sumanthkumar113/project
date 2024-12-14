import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def generate_report():
    logging.info("Generating report.")
    
    # Read popular dishes
    popular_dishes = pd.read_csv('data/popular_dishes.csv')
    
    try:
        # Load correlation data
        correlation_data = pd.read_csv('data/correlation.csv')
        logging.info(f"Correlation data columns: {correlation_data.columns.tolist()}")  # Log available columns
        
        # Access the correlation value between 'Duration (mins)' and 'Total Orders'
        correlation = correlation_data.loc['Duration (mins)', 'Total Orders']  # Adjust as necessary
    except FileNotFoundError:
        print("Error: The file 'data/correlation.csv' was not found.")
        correlation = "N/A"
    except KeyError as e:
        logging.error(f"KeyError: {e}. Please check the column names in the correlation data.")
        correlation = "N/A"
    
    # Generate report content
    report_content = f"""
    # Data Analytics Report

    ## Key Findings

    - **Correlation between Cooking Sessions and Orders:** {correlation}
    - **Top 10 Popular Dishes:**
      {popular_dishes.to_markdown(index=False)}
    
    ## Visualizations

    - **Session vs Order Correlation:** ![Session vs Order](visualizations/session_order_correlation.png)
    - **Popular Dishes:** ![Popular Dishes](visualizations/popular_dishes.png)
    """
    
    # Save report
    with open('reports/report.md', 'w') as f:
        f.write(report_content)
    
    logging.info("Report generation completed.")

if __name__ == "__main__":
    generate_report()