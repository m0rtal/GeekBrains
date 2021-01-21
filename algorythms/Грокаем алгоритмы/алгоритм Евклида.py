def euclidius(width: int, height: int) -> int:
    """
    Алгоритм Эвклида - позволяет разбить прямоугольный участок на наибольшие квадратные участки
    :param width: ширина участка, целое число
    :param height: высота участка, целое число
    :return: размер стороны квадрата
    """
    if height == 0:
        return width
    else:
        new_height = width % height
        new_width = height
        print(new_width, new_height)
        return euclidius(new_width, new_height)

print(euclidius(1680, 640))
