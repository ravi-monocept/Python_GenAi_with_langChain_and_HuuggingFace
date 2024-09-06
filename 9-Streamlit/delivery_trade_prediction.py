import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.linear_model import LinearRegression

# Title of the app
st.title("Indian Stock Market Analysis and Prediction")

# User input for stock symbol
stock_symbol = st.text_input("Enter Stock Symbol (e.g., INFY for Infosys):", "INFY")
from datetime import date

today = date.today()
# Fetch historical data from Yahoo Finance
data = yf.download(stock_symbol + ".NS", start="2020-01-01", end=today)

# Display the data
st.subheader(f"Historical Data for {stock_symbol}")
st.write(data)

# Plotting the closing price
st.subheader("Closing Price Over Time")
plt.figure(figsize=(10, 5))
plt.plot(data["Close"], label="Close Price", color="blue")
plt.title(f"{stock_symbol} Closing Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
st.pyplot(plt)

# Feature Engineering
data["Return"] = data["Close"].pct_change()
data["SMA_20"] = data["Close"].rolling(window=20).mean()
data["SMA_50"] = data["Close"].rolling(window=50).mean()

# Plotting the moving averages
st.subheader("Simple Moving Averages")
plt.figure(figsize=(10, 5))
plt.plot(data["Close"], label="Close Price", color="blue")
plt.plot(data["SMA_20"], label="20-Day SMA", color="orange")
plt.plot(data["SMA_50"], label="50-Day SMA", color="green")
plt.title(f"{stock_symbol} Price with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
st.pyplot(plt)

# Preparing data for prediction
data = data.dropna()
X = np.array(range(len(data))).reshape(-1, 1)  # Days as independent variable
y = data["Close"].values  # Closing price as dependent variable

# Train a linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict future prices
future_days = 30
future_X = np.array(range(len(data), len(data) + future_days)).reshape(-1, 1)
predictions = model.predict(future_X)

# Plotting predictions
st.subheader("Price Prediction for Next 30 Days")
plt.figure(figsize=(10, 5))
plt.plot(data["Close"], label="Historical Close Price", color="blue")
plt.plot(
    range(len(data), len(data) + future_days),
    predictions,
    label="Predicted Price",
    color="red",
)
plt.title(f"{stock_symbol} Price Prediction")
plt.xlabel("Days")
plt.ylabel("Price")
plt.legend()
st.pyplot(plt)
