import pytest


@pytest.fixture(scope="session")
def url(request):

    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def expected_status_code(request):

    return request.config.getoption("--status_code")


def pytest_addoption(parser):

    parser.addoption("--url", action="store", default="https://ya.ru",
                     help="Url for test")
    parser.addoption("--status_code", action="store", default="200",
                     type=int, help="required status code")
