from indicators.ema import ema
from indicators.rsi import rsi
from indicators.heikin_ashi import heikin_ashi_candles
from indicators.double_top import is_double_top
from indicators.double_bottom import is_double_bottom
from indicators.engulfing import is_bullish_engulfing, is_bearish_engulfing
from indicators.support_resistance import find_support_resistance


def momentum_strategy(data):
    # Calculează indicatorii
    data['EMA'] = ema(data['Close'], 50)
    data['RSI'] = rsi(data['Close'], 14)
    ha_data = heikin_ashi_candles(data)
    support, resistance = find_support_resistance(data['Close'])

    # Logica pentru cumpărare
    if (data['Close'].iloc[-1] > data['EMA'].iloc[-1] and
        is_double_bottom(data['Close'].iloc[-5:].tolist()) and
        is_bullish_engulfing(ha_data['Open'].iloc[-2], ha_data['Close'].iloc[-2], ha_data['Open'].iloc[-1], ha_data['Close'].iloc[-1]) and
        data['RSI'].iloc[-1] < 30 and
        data['Close'].iloc[-1] < support):
        return "BUY"

    # Logica pentru vânzare
    elif (data['Close'].iloc[-1] < data['EMA'].iloc[-1] and
          is_double_top(data['Close'].iloc[-5:].tolist()) and
          is_bearish_engulfing(ha_data['Open'].iloc[-2], ha_data['Close'].iloc[-2], ha_data['Open'].iloc[-1], ha_data['Close'].iloc[-1]) and
          data['RSI'].iloc[-1] > 70 and
          data['Close'].iloc[-1] > resistance):
        return "SELL"

    # Altfel, așteaptă
    else:
        return "HOLD"
