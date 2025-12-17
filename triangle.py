import math


def area(a: float, b: float, c: float) -> float:
    """
    Вычисляет площадь треугольника по формуле Герона.

    Args:
        a (float): длина первой стороны треугольника
        b (float): длина второй стороны треугольника
        c (float): длина третьей стороны треугольника

    Returns:
        area (float): площадь треугольника
    
    Raises:
        ValueError: если хотя бы одна сторона меньше или равна 0
    """

    if a < 0 or b < 0 or c < 0:
        raise ValueError("Сторона треугольника должна быть больше 0")

    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def perimeter(a: float, b: float, c: float) -> float:
    """
    Вычисляет периметр треугольника.

    Args:
        a (float): длина первой стороны треугольника
        b (float): длина второй стороны треугольника
        c (float): длина третьей стороны треугольника

    Returns:
        perimeter (float): периметр треугольника
    """

    
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Сторона треугольника должна быть больше 0")

    return a + b + c

