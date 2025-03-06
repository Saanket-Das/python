import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

# Sample dataset structure
data = {
    "Date": ["2024-03-01", "2024-03-02", "2024-03-03", "2024-03-04", "2024-03-05"],
    "Open": [150, 155, 160, 162, 158],
    "High": [155, 160, 165, 167, 163],
    "Low": [148, 153, 158, 160, 157],
    "Close": [153, 158, 163, 165, 160],
    "Volume": [1000, 1200, 1100, 1500, 1300]
}

# Create DataFrame
dataset = pd.DataFrame(data)

# Convert Date column to datetime format and set as index
dataset["Date"] = pd.to_datetime(dataset["Date"])
dataset.set_index("Date", inplace=True)

# Ensure required columns exist
required_cols = {"Open", "High", "Low", "Close", "Volume"}
if required_cols.issubset(dataset.columns):
    # Plot Candlestick Chart
    mpf.plot(dataset, type='candle', style='charles', volume=True, title="Stock Prices", show_nontrading=True)
    plt.show()  # Ensure the plot is displayed
else:
    print("Error: Missing required columns for candlestick chart!")
