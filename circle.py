import math


def area(r: float) -> float:
    """
    Вычисляет площадь круга.

    Args:
        r (float): радиус круга

    Returns:
        area (float): площадь круга
    """
    return math.pi * r * r


def perimeter(r: float) -> float:
    """
    Вычисляет периметр круга.

    Args:
        r (float): радиус круга

    Returns:
        perimeter (float): периметр круга
    """
    return 2 * math.pi * r

