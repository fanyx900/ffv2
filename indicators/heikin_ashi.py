def calculate_heikin_ashi(candles):
    """
    Calculate Heikin Ashi candles from regular candles.
    """
    ha_candles = []

    for i, candle in enumerate(candles):
        if i == 0:
            ha_open = (candle['open'] + candle['close']) / 2
        else:
            ha_open = (ha_candles[-1]['open'] + ha_candles[-1]['close']) / 2

        ha_close = (candle['open'] + candle['close'] + candle['high'] + candle['low']) / 4
        ha_high = max(candle['high'], ha_open, ha_close)
        ha_low = min(candle['low'], ha_open, ha_close)

        ha_candles.append({
            'open': ha_open,
            'close': ha_close,
            'high': ha_high,
            'low': ha_low
        })

    return ha_candles
