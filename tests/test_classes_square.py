import pytest
from src.square import Square

class TestSquare:

    @pytest.mark.parametrize(("side_a", "perimeter"),
                             [
                                 (5, 20),
                                 (5.3, 21.2)
                             ],
                             ids=['int', 'float'])
    def test_square_perimeter_positive(self, side_a, perimeter):
        s = Square(side_a)
        assert s.get_perimeter() == perimeter, f'Result equal {2 * (side_a + side_a)}'




    @pytest.mark.parametrize(("side_a"),
                             [
                                 (-3),
                                 (0)
                             ],
                             ids=["side < 0", "one of sides = 0"])
    @pytest.mark.otus
    def test_square_negative(self, side_a):
        with pytest.raises(ValueError):
            Square(side_a)