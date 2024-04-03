from datetime import datetime
import pytest
from src.rectangle import Rectangle


class TestRectangle:

    @pytest.mark.smoke
    @pytest.mark.otus
    @pytest.mark.parametrize(("side_a", "side_b", "area"),
                             [
                                 (5, 8, 40),
                                 (2.5, 5.5, 13.75)
                             ],
                             ids=["integer check", "float check"])
    @pytest.mark.skipif(condition=datetime.now().day == 13,
                        reason="Bad day especially if it's Friday")
    def test_rectangle_area_positive(self, side_a, side_b, area):

        r = Rectangle(side_a, side_b)
        assert r.get_area() == area, \
            f'Result area not equal {side_a * side_b}'

    @pytest.mark.smoke
    @pytest.mark.otus
    @pytest.mark.skipif(condition=datetime.now().day == 13,
                        reason="Bad day especially if it's Friday")
    @pytest.mark.parametrize("rectangle_params", ["integer", "float"])
    def test_rectangle_area_positive_data_from_fixture(self, rectangle_data,
                                                       rectangle_params):

        side_a, side_b, area = rectangle_data(data=rectangle_params)
        r = Rectangle(side_a, side_b)
        assert r.get_area() == area, \
            f"Calculated rectangle area should be equal {side_a * side_b}"

    @pytest.mark.parametrize(("side_a", "side_b"),
                             [
                                 (-3, 6),
                                 (3.5, -6.5),
                                 (0, 1)
                             ],
                             ids=["side a < 0",
                                  "side b < 0",
                                  "one of sides = 0"])
    @pytest.mark.otus
    def test_rectangle_negative(self, side_a, side_b):
        with pytest.raises(ValueError):
            Rectangle(side_a, side_b)
