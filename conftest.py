import pytest
from api_client import APIClient

@pytest.fixture(scope="session")
def client():
    base_url = "https://reqres.in/api"
    headers = {
        "x-api-key": "reqres-free-v1"
    }
    return APIClient(base_url, headers=headers)
