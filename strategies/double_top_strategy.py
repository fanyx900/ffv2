from indicators.double_top import is_double_top
from indicators.engulfing import is_bearish_engulfing
from indicators.support_resistance import is_resistance_zone
from indicators.ema import ema
from indicators.rsi import rsi

def double_top_sell_signal(prices, tolerance=0.05):
    """
    Detectează un semnal de vânzare bazat pe strategia Double Top.

    :param prices: O listă de prețuri.
    :param tolerance: Toleranța pentru variația dintre cele două vârfuri. Implicit este 0.05 (5%).
    :return: True dacă un semnal de vânzare este detectat, altfel False.
    """
    if not is_double_top(prices, tolerance):
        return False

    if not is_bearish_engulfing(prices[-2:]):
        return False

    if not is_resistance_zone(prices[-1]):
        return False

    # Aici poți adăuga verificări suplimentare pentru RSI, EMA sau orice alt indicator dorești.

    return True
