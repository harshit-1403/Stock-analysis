import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date']).dt.date
    return df

# Load stock data
stock_df = load_data("stock_analysis_results.csv")
st.header("Data Analysis and Visualization")

questions = [
    "1. Volatility Analysis",
    "2. Cumulative Return Over Time",
    "3. Sector-wise Performance",
    "4. Stock Price Correlation",
    "5. Top 5 Gainers and Losers (Month-wise)"
]
select_dashboard = st.selectbox("Choose the Dashboard", questions)

if select_dashboard == "1. Volatility Analysis":
    # Ensure the 'date' column is in datetime format and extract only the date
    stock_df['date'] = pd.to_datetime(stock_df['date']).dt.date
    # Sort the DataFrame by Ticker and Date
    stock_df = stock_df.sort_values(by=['Ticker', 'date'])
    # Calculate daily returns for each Ticker
    stock_df['daily_return'] = stock_df.groupby('Ticker')['close'].pct_change()
    # Compute standard deviation of daily returns (volatility) for each Ticker
    volatility = stock_df.groupby('Ticker')['daily_return'].std()
    # Sort volatility in descending order to get the top 10 most volatile stocks
    top_10_volatility = volatility.sort_values(ascending=False).head(10)
    
    # Plot a bar chart showing the volatility of the top 10 most volatile stocks
    plt.figure(figsize=(10, 6))
    top_10_volatility.plot(kind='bar', color='skyblue')
    plt.title('Top 10 Most Volatile Stocks')
    plt.xlabel('Ticker')
    plt.ylabel('Volatility (Standard Deviation of Daily Returns)')
    plt.xticks(rotation=90)
    plt.tight_layout()
    # Display the plot in the Streamlit app
    st.pyplot(plt)

elif select_dashboard == "2. Cumulative Return Over Time":
    # Sample code to handle a DataFrame with multiple tickers
    stocks_df = pd.read_csv("stock_analysis_results.csv")
    # Ensure the 'date' column is in datetime format and extract only the date
    stock_df['date'] = pd.to_datetime(stock_df['date'])
    stock_df['date'] = stock_df['date'].dt.date
    # Sort the DataFrame by Ticker and Date
    stock_df = stock_df.sort_values(by=['Ticker', 'date'])
    # Manually calculate daily returns using the formula
    stock_df['daily_return'] = stock_df.groupby('Ticker')['close'].pct_change()
    # Calculate cumulative returns for each stock by applying a running total
    stock_df['cumulative_return'] = (1 + stock_df['daily_return']).groupby(stock_df['Ticker']).cumprod() - 1
    # Find the cumulative return at the end of the year for each Ticker
    final_cumulative_returns = stock_df.groupby('Ticker')['cumulative_return'].last()
    # Sort the stocks by their final cumulative return and select the top 5
    top_5_stocks = final_cumulative_returns.sort_values(ascending=False).head(5)
    print(top_5_stocks)
    # Filter the DataFrame for the top 5 stocks
    top_5_df = stock_df[stock_df['Ticker'].isin(top_5_stocks.index)]
    # Plot a line chart for the top 5 performing stocks over the course of the year
    plt.figure(figsize=(10, 6))
    for ticker in top_5_stocks.index:
        # Filter the data for each stock
        stock_data = top_5_df[top_5_df['Ticker'] == ticker]
        plt.plot(stock_data['date'], stock_data['cumulative_return'], label=ticker)

    # Customize the plot
    plt.title('Top 5 Performing Stocks (Cumulative Return) Over the Year')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.legend(title='Ticker')
    plt.xticks(rotation=90)
    plt.tight_layout()
    st.pyplot(plt)


elif select_dashboard == "3. Sector-wise Performance":
    st.subheader("")
    stocks_df = pd.read_csv("stock_analysis_results.csv")
    sector_df = pd.read_csv("Sector_data - Sheet1.csv")
    # Extract the Ticker values and select relevant columns
    sector_df["Ticker"] = sector_df["Symbol"].str.split(": ").str[1]
    sector_df = sector_df[["sector", "Ticker"]]
    # Merge stocks and sector data
    stocks_df = stocks_df.merge(sector_df, how="left", on="Ticker")
    # Check for null sectors
    null_sectors = stocks_df[stocks_df["sector"].isnull()]
    print("Stocks with null sectors:\n", null_sectors)
    # Ensure the 'date' column is datetime and extract the year
    stocks_df['date'] = pd.to_datetime(stocks_df['date'])
    stocks_df['year'] = stocks_df['date'].dt.year
    # Calculate yearly returns for each stock
    stocks_df = stocks_df.sort_values(by=['Ticker', 'date'])
    stocks_df['yearly_return'] = stocks_df.groupby(['Ticker', 'year'])['close'].pct_change()
    # Calculate average yearly return by sector
    sector_avg_yearly_return = stocks_df.groupby('sector')['yearly_return'].mean()
    # Display the results
    # print("Sector-Wise Average Yearly Returns:")
    # print(sector_avg_yearly_return)
    plt.figure(figsize=(10, 6))
    sector_avg_yearly_return.sort_values(ascending=False).plot(kind='bar', color='lightcoral')
    plt.title('Average Yearly Return by Sector')
    plt.xlabel('Sector')
    plt.ylabel('Average Yearly Return')
    plt.xticks(rotation=90)
    plt.tight_layout()
    st.pyplot(plt)

elif select_dashboard == "4. Stock Price Correlation":
    stock_data = pd.read_csv("stock_analysis_results.csv")
    # Ensure 'date' column is in datetime format
    stock_data['date'] = pd.to_datetime(stock_data['date'])
    # Pivot the DataFrame to create a table with tickers as columns and dates as rows
    pivot_df = stock_data.pivot(index='date', columns='Ticker', values='close')
    # Calculate daily returns
    daily_returns = pivot_df.pct_change().dropna()
    # Compute the correlation matrix for daily returns
    correlation_matrix = daily_returns.corr()
    # Set the size of the plot
    plt.figure(figsize=(30, 30))
    # Create a heatmap of the correlation matrix
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, linewidths=0.5, fmt='.2f')
    # Add titles and labels
    plt.title('Stock Closing Price Correlation Matrix')
    plt.xlabel('Stock Ticker')
    plt.ylabel('Stock Ticker')
    # Display the plot
    plt.show()
    # Display the plot in Streamlit
    st.pyplot(plt)



