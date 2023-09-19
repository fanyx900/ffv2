def is_bullish_engulfing(candles):
    """
    Check if the latest candlestick pattern is a bullish engulfing.
    """
    last_candle = candles[-1]
    prev_candle = candles[-2]

    if last_candle['close'] > last_candle['open'] and prev_candle['close'] < prev_candle['open']:
        if last_candle['open'] < prev_candle['close'] and last_candle['close'] > prev_candle['open']:
            return True
    return False

def is_bearish_engulfing(candles):
    """
    Check if the latest candlestick pattern is a bearish engulfing.
    """
    last_candle = candles[-1]
    prev_candle = candles[-2]

    if last_candle['close'] < last_candle['open'] and prev_candle['close'] > prev_candle['open']:
        if last_candle['open'] > prev_candle['close'] and last_candle['close'] < prev_candle['open']:
            return True
    return False
