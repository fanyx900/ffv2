def is_double_bottom(prices, tolerance=0.05):
    """
    Detectează dacă un model "double bottom" a fost format.

    :param prices: O listă de prețuri.
    :param tolerance: Toleranța pentru variația dintre cele două văi. Implicit este 0.05 (5%).
    :return: True dacă un model "double bottom" este detectat, altfel False.
    """
    if len(prices) < 5:
        return False

    # Identifică vârfurile și văile
    bottom1 = min(prices[-5], prices[-3])
    top = max(prices[-4])
    bottom2 = min(prices[-2])

    # Verifică dacă cele două văi sunt apropiate în valoare
    if abs(bottom1 - bottom2) <= tolerance * bottom1:
        if bottom1 == prices[-5] and bottom2 == prices[-2] and top == prices[-4]:
            return True

    return False
