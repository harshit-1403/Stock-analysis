import streamlit as st
from PIL import Image
import io

# Project Title
st.title("Data-Driven Stock Analysis: Organizing, Cleaning, and Visualizing Market Trends")

# Project Description
st.write("""
Welcome to the Stock Performance Dashboard! This project provides a comprehensive analysis of the Nifty 50 stocks' performance over the past year. The goal is to help investors, analysts, and stock enthusiasts make data-driven decisions based on various stock performance metrics.

With this interactive dashboard, you will be able to:
- Analyze daily stock data (open, close, high, low, volume).
- Visualize volatility, cumulative returns, and sector-wise performance.
- Identify top-performing and worst-performing stocks.
- Gain insights into stock price correlations and monthly performance trends.

The dashboard utilizes **Streamlit** and **Power BI** for real-time visualizations and insights, making it a valuable tool for investment decisions.

Explore the pages to get started!
""")
