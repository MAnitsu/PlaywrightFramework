# tests/test_login.py

import allure
from pages.login_page import LoginPage

@allure.feature("Login")
@allure.story("Valid Login")
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_login(page, valid_credentials):
    login_page = LoginPage(page)
    username = valid_credentials["username"]
    password = valid_credentials["password"]

    with allure.step("Navigate to Login Page"):
        login_page.navigate()
    with allure.step("Enter valid credentials and submit"):
        login_page.login(username, password)
    with allure.step("Verify successful login message is visible"):
        assert login_page.success_message_visible()

@allure.feature("Login")
@allure.story("Invalid Login")
@allure.severity(allure.severity_level.NORMAL)
def test_invalid_login(page, invalid_credentials):
    login_page = LoginPage(page)
    username = invalid_credentials["username"]
    password = invalid_credentials["password"]

    with allure.step("Navigate to Login Page"):
        login_page.navigate()
    with allure.step("Enter invalid credentials and submit"):
        login_page.login(username, password)
    with allure.step("Verify error message is visible"):
        assert login_page.error_message_visible()
