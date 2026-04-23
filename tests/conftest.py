import pytest
from fastapi.testclient import TestClient
from copy import deepcopy
from src.app import app, activities


@pytest.fixture
def client():
    """
    Create a test client and reset activities before/after each test.
    This ensures test isolation and prevents cross-test contamination.
    """
    # Store original activities
    original = deepcopy(activities)
    
    yield TestClient(app)
    
    # Restore original activities after test
    activities.clear()
    activities.update(original)
