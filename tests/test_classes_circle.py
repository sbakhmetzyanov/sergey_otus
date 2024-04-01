import pytest
from src.circle import Circle


class TestCircle:
    @pytest.mark.smoke
    @pytest.mark.otus
    def test_circle_area_positive(self, circle_data):

        radius, area = circle_data
        c = Circle(radius)
        assert c.get_area() == area, f"Circle area should be {c.get_area()}"

    @pytest.mark.parametrize("radius",
                             [
                                 (-3),
                                 (-5.5),
                                 0],
                             ids=["below zero int", "below zero float",
                                  "zero rad",])
    def test_circle_negative(self, radius):
        with pytest.raises(ValueError):
            Circle(radius)