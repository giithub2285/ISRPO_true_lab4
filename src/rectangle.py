def area(a, b):
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return a * b

def perimeter(a, b):
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return 2 * (a + b)

def is_square(a, b):
    return a == b