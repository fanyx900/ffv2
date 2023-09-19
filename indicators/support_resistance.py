def find_support_resistance(prices, window=20):
    """
    Find support and resistance levels for given prices.
    """
    resistance = []
    support = []

    for i in range(window, len(prices) - window):
        local_max = max(prices[i-window:i+window])
        local_min = min(prices[i-window:i+window])

        if prices[i] == local_max:
            resistance.append((i, prices[i]))
        elif prices[i] == local_min:
            support.append((i, prices[i]))

    return support, resistance
