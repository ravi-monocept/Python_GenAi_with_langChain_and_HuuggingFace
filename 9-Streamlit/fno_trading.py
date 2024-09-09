import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime

# Set the title of the app
st.title("Indian Market Analysis and Prediction")

# Sidebar for user input
st.sidebar.header("Market Parameters")

# User input for stock ticker symbol
stock_symbol = st.sidebar.text_input(
    "Enter Stock Ticker Symbol (e.g., NIFTY, BANKNIFTY):", "NIFTY"
)

# Fetch today's market data
today = datetime.now().date()
data = yf.download(stock_symbol + ".NS", start=today, end=today)

# Display today's data
if not data.empty:
    st.subheader(f"Today's Market Data for {stock_symbol}")
    st.write(data)

    # Extract today's high and low
    today_high = data["High"][0]
    today_low = data["Low"][0]
    st.write(f"Today's High: {today_high}")
    st.write(f"Today's Low: {today_low}")

    # Plotting today's price action
    st.subheader("Price Action")
    st.line_chart(data["Close"])

    # Simple prediction based on today's high and low
    predicted_close = (today_high + today_low) / 2
    st.subheader("Predicted Close Price for Tomorrow")
    st.write(f"Predicted Close: {predicted_close:.2f}")

    # Display additional metrics
    st.subheader("Additional Market Information")
    st.write(f"Current Price: {data['Close'][0]}")
    st.write(f"Price Range: {today_low} - {today_high}")

else:
    st.write("No data available for the selected stock.")

# Footer
st.sidebar.markdown("## About")
st.sidebar.write(
    "This app provides an analysis of today's market data and a simple prediction for tomorrow's close."
)
