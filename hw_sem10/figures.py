# Задание No1
# 📌 Создайте класс окружность.
# 📌 Класс должен принимать радиус окружности при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие длину окружности и её площадь.

import math


class Circle:
    """Класс окружность"""

    # __name__ - dunder - double underscore
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def calculate_area(self) -> float:
        # pi*r^2
        return math.pi * self.radius**2

    def calculate_length(self) -> float:
        return 2 * math.pi * self.radius


# Задание No2
# 📌 Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр и площадь.
# 📌 Если при создании экземпляра передаётся только одна сторона, 
#     считаем что у нас квадрат.


class Rectangle:
    def __init__(self, width, height=0) -> None:
        self.width = width
        self.height = height if height else width
        
    def calculate_area(self) -> float:
        return self.width * self.height
    
    def calculate_perimeter(self) -> float:
        return (self.width + self.height) * 2


