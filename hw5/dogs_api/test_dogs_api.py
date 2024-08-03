import pytest
import requests
from jsonschema import validate


def test_list_breeds(base_url):

    response = requests.get(f"{base_url}/breeds/list/all", timeout=10)
    assert response.status_code == 200
    print(response.json())

    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "object"},
            "status": {"type": "string"},
        },
        "required": ["message", "status"]
    }
    validate(instance=response.json(), schema=schema)


@pytest.mark.parametrize("number", [1, 3, 19, 11, 47,
                                    pytest.param(59,
                                                 marks=pytest.mark.xfail)])
def test_numbers_image(number, base_url, get_random_image):

    dogs_image = f"{base_url}/{get_random_image}/{number}"
    res_dogs = requests.get(dogs_image, timeout=10)
    assert len(res_dogs.json().get("message")) == number


@pytest.mark.parametrize("number", [50, 51, 345, 999,
                                    pytest.param(0,
                                                 marks=pytest.mark.skip)])
def test_limit_50(number, base_url, get_random_image):

    run_limit = f"{base_url}/{get_random_image}/{number}"
    dogs_limit = requests.get(run_limit, timeout=10)
    assert len(dogs_limit.json().get("message")) == 50


def test_breed_list(base_url):

    response = requests.get(f"{base_url}/breed/hound/images", timeout=10)
    assert response.status_code == 200

    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "array"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }
    validate(instance=response.json(), schema=schema)
