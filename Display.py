import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from st_aggrid import AgGrid, GridOptionsBuilder
import plotly.express as px
# Set up the Streamlit application
st.title("Stock Analysis Dashboard")

@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date']).dt.date
    return df

# Load the stock data
stock_df = load_data("stock_analysis_results.csv")

# Sidebar for user inputs
st.sidebar.header("Filter Options")

# Dropdown for ticker symbol selection
ticker_names = stock_df["Ticker"].unique().tolist()
ticker_symbol = st.sidebar.selectbox("Select Ticker Symbol", ticker_names)

# Date range selection
min_date = stock_df['date'].min()
max_date = stock_df['date'].max()
start_date = st.sidebar.date_input("Start Date", value=min_date, min_value=min_date, max_value=max_date)
end_date = st.sidebar.date_input("End Date", value=max_date, min_value=min_date, max_value=max_date)
if st.sidebar.button("Go to analysis page"):
    st.write("hello")
# Filter data based on user inputs
if start_date > end_date:
    st.sidebar.error("Error: End date must fall after start date.")
else:
    filtered_df = stock_df[
        (stock_df["Ticker"] == ticker_symbol) &
        (stock_df["date"] >= start_date) &
        (stock_df["date"] <= end_date)
    ]
    filtered_df['date'] = pd.to_datetime(filtered_df['date']).dt.date
    
    price_tab, hist_tab, chart_tab = st.tabs(["Price Summary", "Historical Data", "Charts"])

    with price_tab:
        st.subheader(f"Price Summary for {ticker_symbol} from {start_date} to {end_date}")
        if not filtered_df.empty:
            st.write(filtered_df.describe())
        else:
            st.write("No data available for the selected date range and ticker symbol.")

    with hist_tab:
        st.subheader(f"Historical Data for {ticker_symbol} from {start_date} to {end_date}")
        if not filtered_df.empty:
            filtered_df = filtered_df.reset_index(drop=True)
            st.dataframe(filtered_df, hide_index=True)
        else:
            st.write("No data available for the selected date range and ticker symbol.")

    with chart_tab:
        st.subheader(f"Closing Prices Chart for {ticker_symbol} from {start_date} to {end_date}")
        if not filtered_df.empty:
            plt.figure(figsize=(10, 5))
            sns.lineplot(data=filtered_df, x="date", y="close", marker="o")
            plt.title(f"Closing Prices for {ticker_symbol}")
            plt.xlabel("Date")
            plt.ylabel("Closing Price")
            plt.xticks(rotation=45)
            st.pyplot(plt)
        else:
            st.write("No data available for the selected date range and ticker symbol.")




  

    
