def is_even(n):
    """Dado un número entero n, retorna True si es par, False si es impar."""
    return n % 2 == 0
 
def is_positive(n):
    """Dado un número entero n, retorna True si es mayor a 0, False en caso contrario."""
    return n > 0
 
def classify_number(n):
    if n == 0:
        return "zero"
    elif is_positive(n) and is_even(n):
        return "positive even"
    elif is_positive(n) and not is_even(n):
        return "positive odd"
    elif not is_positive(n) and is_even(n):
        return "negative even"
    else:
        return "negative odd"
