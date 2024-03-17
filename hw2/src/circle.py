import math
from figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        super().__init__(name="Circle")
        if radius <= 0:
            raise ValueError("Радиус должен быть больше нуля")
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius * self.radius

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Необходим класс должен быть Figure")
        return self.get_area() + other_figure.get_area()
