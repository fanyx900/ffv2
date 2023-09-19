def is_double_top(prices, tolerance=0.05):
    """
    Detectează dacă un model "double top" a fost format.

    :param prices: O listă de prețuri.
    :param tolerance: Toleranța pentru variația dintre cele două vârfuri. Implicit este 0.05 (5%).
    :return: True dacă un model "double top" este detectat, altfel False.
    """
    if len(prices) < 5:
        return False

    # Identifică vârfurile și văile
    top1 = max(prices[-5], prices[-3])
    bottom = min(prices[-4])
    top2 = max(prices[-2])

    # Verifică dacă cele două vârfuri sunt apropiate în valoare
    if abs(top1 - top2) <= tolerance * top1:
        if top1 == prices[-5] and top2 == prices[-2] and bottom == prices[-4]:
            return True

    return False
