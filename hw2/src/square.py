from rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Сторона должна быть больше 0")
        super().__init__(side_a, side_a)
