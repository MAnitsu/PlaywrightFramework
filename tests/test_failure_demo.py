# tests/test_failure_demo.py
import pytest
import allure

@allure.title("Intentional Failure Demo")
@allure.severity(allure.severity_level.CRITICAL)
def test_intentional_failure(page):
    page.goto("https://example.com")
    allure.attach(page.screenshot(), name="before_assert", attachment_type=allure.attachment_type.PNG)
    assert page.locator("h1").inner_text() == "Non-Existent Text"
