import pytest


@pytest.fixture(scope="session", autouse=True)
def run_stop_db():
    print("\n Running DB")

    yield

    print("\n Stopping DB")


@pytest.fixture()
def triangle_data():

    side_a, side_b, side_c = 3, 4, 5
    perimeter = side_a + side_b + side_c

    yield side_a, side_b, side_c, perimeter

    print("\n Down")


@pytest.fixture(params=[(1, 3.141592653589793),
                        (2, 12.566370614359172),
                        (3, 28.274333882308138),
                        (10, 314.1592653589793)
                        ])
def circle_data(request):
    radius, area = request.param

    yield radius, area


@pytest.fixture()
def rectangle_data():

    def _wrapper(data: str):
        if data == "integer":
            return 5, 8, 40
        if data == "float":
            return 2.5, 5.5, 13.75

    yield _wrapper

    print("\n wrapper used")
