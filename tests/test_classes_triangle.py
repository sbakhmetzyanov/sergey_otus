import pytest
from src.triange import Triangle


class TestTriangle:

    def test_triangle_perimeter_positive(self, triangle_data):
        side_a, side_b, side_c, perimeter = triangle_data
        t = Triangle(side_a, side_b, side_c)
        assert t.get_perimeter() == perimeter, f'Result equal {t.get_perimeter()}'

    @pytest.mark.parametrize(('side_a', 'side_b', 'side_c'),
                             [(-3, 5, 7),
                              (1, 0, 7.5),
                              ],
                             ids=['side a < 0',
                                  'side a + side b < side c'])
    def test_triangle_perimeter_negative(self, side_a, side_b, side_c):
        with pytest.raises(ValueError):
            Triangle(side_a, side_b, side_c)
