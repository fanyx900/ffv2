import pandas as pd

def calculate_ema(data, period=50, column='Close'):
    return data[column].ewm(span=period, adjust=False).mean()
