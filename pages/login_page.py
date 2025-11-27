# pages/login_page.py

from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.flash_success = page.locator("#flash.success")
        self.flash_error = page.locator("#flash.error")

    def navigate(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, user: str, pwd: str):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_button.click()

    def success_message_visible(self) -> bool:
        return self.flash_success.is_visible()

    def error_message_visible(self) -> bool:
        return self.flash_error.is_visible()
