# Data-Driven Stock Analysis: Organizing, Cleaning, and Visualizing Market Trends

## Overview
This project provides a comprehensive analysis of Nifty 50 stocks' performance over the past year. It uses Python and Streamlit to analyze daily stock data and generate interactive dashboards, helping investors and analysts make data-driven decisions.

## Skills & Tools
- **Skills:** Data Analysis, Statistics, Data Cleaning, Visualization, Streamlit UI Development  
- **Technologies:** Python, Pandas, Streamlit, SQL  
- **Libraries:** Matplotlib, Seaborn, NumPy  

## Domain
Finance / Data Analytics  

## Problem Statement
The Stock Performance Dashboard visualizes the performance of Nifty 50 stocks by:  
- Analyzing daily stock data (open, close, high, low, volume)  
- Cleaning and processing data  
- Generating key metrics like top performers, volatility, and correlations  
- Offering interactive dashboards for better insights  

## Business Use Cases
1. **Stock Performance Ranking:** Identify the top 10 best-performing and worst-performing stocks over the past year.  
2. **Market Overview:** Analyze average stock performance and the percentage of green vs. red stocks.  
3. **Investment Insights:** Identify consistent growth stocks or those with significant declines.  
4. **Decision Support:** Visualize average prices, volatility, and trends for better trading decisions.  

## Features & Visualizations
1. **Volatility Analysis:**  
   - Calculate and plot the standard deviation of daily returns for each stock.  
   - Visualize the top 10 most volatile stocks.  
2. **Cumulative Return Over Time:**  
   - Compute cumulative returns for each stock.  
   - Plot a line chart for the top 5 performing stocks based on cumulative return.  
3. **Sector-wise Performance:**  
   - Analyze and visualize the average yearly return for each sector.  
   - Plot a bar chart for sector performance.  
4. **Stock Price Correlation:**  
   - Create a heatmap to show correlations between stock prices.  
   - Highlight stocks with high or low correlations.  
5. **Top Gainers and Losers (Monthly):**  
   - Identify and visualize the top 5 gainers and losers for each month.  

## Dataset
- Data is provided in YAML format, organized by months and symbols.  
- The data is transformed into CSV files for each symbol during preprocessing.  

### Required Packages
Ensure you have the following key libraries installed:
- streamlit
- pandas
- numpy
- matplotlib
- seaborn
- pyyaml
- pillow
## Results
- Interactive dashboards for stock performance trends.  
- Insights into top-performing and worst-performing stocks.  
- Market summaries and sector-wise performance analysis.  

## Installation
1. Clone the repository:  
   ```bash
   git clone https://github.com/harshit-1403/Stock-analysis.git
