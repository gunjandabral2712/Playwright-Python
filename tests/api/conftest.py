import os
import pytest
import requests


@pytest.fixture(scope="session")
def api_base_url():
    """Base URL for API tests. Can be overridden with `API_BASE_URL` env var."""
    return os.getenv("API_BASE_URL") or "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def http_session():
    """Provide a requests.Session for API tests (session-scoped)."""
    s = requests.Session()
    yield s
    s.close()
