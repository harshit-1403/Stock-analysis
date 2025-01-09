import streamlit as st

# Set the initial page configuration (this must be at the top of the script)
st.set_page_config(page_title="Stock Analysis Dashboard", layout="wide")

# Define the pages
home_page = st.Page("pages/Home.py", title="Home", icon="🏠")
analytics_page = st.Page("pages/Analytics.py", title="Analytics", icon="📊")
dashboard_page = st.Page("pages/Dashboard.py", title="Dashboard", icon="📈")

# Set up navigation
pages = st.navigation([home_page, analytics_page, dashboard_page])

# Run the selected page
pages.run()
