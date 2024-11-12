import  math

from abc import ABC, abstractmethod


class Shape(ABC):
    """Абстрактный базовый класс для всех фигур.
    Использует абстрактный метод area, который должен быть реализован в дочерних классах"""


    @abstractmethod

    def area(self):
        """
        Абстрактный метод для вычисления площади фигуры.
        Должен быть реализован в каждом наследующем классе.
        """
        pass

class Circle(Shape):
    """Класс круг наследуется от Shape"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    """Класс прямоугольник наследуется от Shape"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Вычисление площади прямоугольника"""
        return self.width * self.height

class Triangle(Shape):
    """Класс треугольник наслед от Shape"""

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        """Вычисление площади треугольника"""

        return 0.5 * self.base * self.height


circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()

print("Плошадь круга: ", circle.area())
print("Плошадь прямоугольника: ", rectangle.area())
print("Плошадь треугольника: ", triangle.area())

try:
    shape = Shape()
except TypeError as e:
    print(f"Ошибка: {e}")

