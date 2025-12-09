# tests/test_failure_demo.py

import allure

@allure.title("Intentional Failure Demo")
@allure.severity(allure.severity_level.CRITICAL)
def test_intentional_failure(page):
    page.goto("https://example.com")
    assert page.locator("h1").inner_text() == "Non-Existent Text"
