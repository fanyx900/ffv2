import numpy as np

def calculate_atr(highs, lows, closes, period=14):
    """
    Calculate Average True Range (ATR) for given high, low, and close prices.
    """
    tr = np.zeros(len(closes))
    atr = np.zeros(len(closes))

    for i in range(1, len(closes)):
        hl = highs[i] - lows[i]
        hc = abs(highs[i] - closes[i-1])
        lc = abs(lows[i] - closes[i-1])
        tr[i] = max(hl, hc, lc)

    atr[period-1] = np.mean(tr[1:period+1])

    for i in range(period, len(closes)):
        atr[i] = (atr[i-1] * (period-1) + tr[i]) / period

    return atr
