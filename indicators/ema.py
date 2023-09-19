import numpy as np

def calculate_ema(prices, period):
    """
    Calculate Exponential Moving Average (EMA) for a given price list and period.
    """
    prices = np.array(prices)
    ema = np.zeros_like(prices)
    multiplier = 2 / (period + 1)
    ema[period - 1] = np.mean(prices[:period])  # Starting with SMA for the first value

    for i in range(period, len(prices)):
        ema[i] = (prices[i] - ema[i - 1]) * multiplier + ema[i - 1]

    return ema
