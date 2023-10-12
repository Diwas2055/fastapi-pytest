# test_integration.py
import pytest
from fastapi.testclient import TestClient
from main import app, users_db
from hypothesis import given
from hypothesis import strategies as st
from main import User

client = TestClient(app)


@pytest.fixture
def reset_users_db():
    users_db.clear()


# Define strategies to generate user data
user_strategy = st.builds(
    User,
    username=st.text(min_size=1, max_size=50),
    email=st.emails(),
    full_name=st.text(min_size=1, max_size=100).filter(lambda x: x is not None),
)


# Test create user
@given(user_strategy, reset_users_db)
def test_create_user(user, _):
    response = client.post("/users/", json=user.dict())
    assert response.status_code == 200
    assert response.json() == user.dict()


# Test read users
@given(st.lists(user_strategy, min_size=1), reset_users_db)
def test_read_users(users, _):
    for user in users:
        client.post("/users/", json=user.dict())

    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == [user.dict() for user in users]
