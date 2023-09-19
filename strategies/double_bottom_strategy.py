from indicators.double_bottom import is_double_bottom
from indicators.engulfing import is_bullish_engulfing
from indicators.support_resistance import is_support_zone
from indicators.ema import ema
from indicators.rsi import rsi

def double_bottom_buy_signal(prices, tolerance=0.05):
    """
    Detectează un semnal de cumpărare bazat pe strategia Double Bottom.

    :param prices: O listă de prețuri.
    :param tolerance: Toleranța pentru variația dintre cele două văi. Implicit este 0.05 (5%).
    :return: True dacă un semnal de cumpărare este detectat, altfel False.
    """
    if not is_double_bottom(prices, tolerance):
        return False

    if not is_bullish_engulfing(prices[-2:]):
        return False

    if not is_support_zone(prices[-1]):
        return False

    # Aici poți adăuga verificări suplimentare pentru RSI, EMA sau orice alt indicator dorești.

    return True
