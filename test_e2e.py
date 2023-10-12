# test_e2e.py
import pytest
from selenium import webdriver


@pytest.fixture
def web_driver():
    driver = webdriver.Chrome()  # Replace with your preferred web driver
    yield driver
    driver.quit()


def test_create_user(web_driver):
    web_driver.get("http://localhost:8000")  # Replace with the actual URL
    # Interact with the web page to create a user
    # Verify the user is created
    # Close the browser


def test_read_users(web_driver):
    web_driver.get("http://localhost:8000")  # Replace with the actual URL
    # Interact with the web page to read users
    # Verify the list of users
    # Close the browser
