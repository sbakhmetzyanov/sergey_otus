import json
import pytest
from jsonschema import validate


def validate_assert(data, schema_file):

    with open(schema_file, encoding="utf-8") as file_json:
        schema = json.load(file_json)
        return validate(instance=data, schema=schema)


@pytest.mark.parametrize("id", [1, 5, 7], ids=["1", "5", "7"])
def test_validate(base_url, session, id):

    response = session.get(f"{base_url}/posts/{id}")
    if response.status_code == 200:
        validate_assert(response.json(),
                        "../schemas/jsonplaceholder_schema.json")
