# test_main.py (with Hypothesis)
import pytest
from fastapi.testclient import TestClient
from main import app
from hypothesis import given
from hypothesis import strategies as st
from main import User

client = TestClient(app)

# Define strategies to generate user data
user_strategy = st.builds(
    User,
    username=st.text(min_size=1, max_size=50),
    email=st.emails(),
    full_name=st.text(min_size=1, max_size=100).filter(lambda x: x is not None),
)


# Test create user
@given(user_strategy)
def test_create_user(user):
    response = client.post("/users/", json=user.dict())
    assert response.status_code == 200
    assert response.json() == user.dict()


# Test read users
@given(st.lists(user_strategy, min_size=1))
def test_read_users(users):
    for user in users:
        client.post("/users/", json=user.dict())

    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == [user.dict() for user in users]


# Test read user
@given(user_strategy)
def test_read_user(user):
    client.post("/users/", json=user.dict())

    response = client.get("/users/0")
    assert response.status_code == 200
    assert response.json() == user.dict()


# Test update user
@given(user_strategy, user_strategy)
def test_update_user(original_user, updated_user):
    client.post("/users/", json=original_user.dict())

    response = client.put("/users/0", json=updated_user.dict())
    assert response.status_code == 200
    assert response.json() == updated_user.dict()


# Test delete user
@given(user_strategy)
def test_delete_user(user):
    client.post("/users/", json=user.dict())

    response = client.delete("/users/0")
    assert response.status_code == 200
    assert response.json() == user.dict()
