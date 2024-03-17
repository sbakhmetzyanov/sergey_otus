from figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().__init__(name="Triangle")
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Стороны должны быть больше нуля")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        area = (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5
        return area

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Необходим класс должен быть figure")
        return self.get_area() + other_figure.get_area()
