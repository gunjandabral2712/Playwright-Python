import pytest

from pages.login_page import LoginPage


@pytest.mark.ui
def test_login_success(page, base_url):
    login = LoginPage(page, base_url=base_url)
    login.goto()
    login.login("tomsmith", "SuperSecretPassword!")
    assert login.has_success_message()


@pytest.mark.ui
def test_login_failure(page, base_url):
    login = LoginPage(page, base_url=base_url)
    login.goto()
    login.login("wrong", "credentials")
    assert login.has_error_message()
