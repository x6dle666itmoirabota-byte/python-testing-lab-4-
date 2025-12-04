def rectangle_area(width, height):
    """
    Вычисляет площадь прямоугольника.
    Возвращает None, если входные данные некорректны (не положительные числа).
    """
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        return None
    if width <= 0 or height <= 0:
        return None
    return width * height

def rectangle_perimeter(width, height):
    """
    Вычисляет периметр прямоугольника.
    Возвращает None, если входные данные некорректны (не положительные числа).
    """
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        return None
    if width <= 0 or height <= 0:
        return None
    return 2 * (width + height)