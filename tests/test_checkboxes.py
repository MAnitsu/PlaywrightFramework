# tests/test_checkboxes.py

import allure
from pages.checkbox_page import CheckboxPage

@allure.feature("Checkboxes")
@allure.story("Check and Uncheck Boxes")
@allure.severity(allure.severity_level.NORMAL)
def test_checkboxes(page):
    checkbox_page = CheckboxPage(page)
    checkbox_page.navigate()
    
    with allure.step("Check checkbox 0"):
        checkbox_page.check(0)
    with allure.step("Ensure checkbox 0 is checked"):
        assert checkbox_page.is_checked(0) is True

    with allure.step("Uncheck checkbox 1"):
        checkbox_page.uncheck(1)
    with allure.step("Ensure checkbox 1 is unchecked"):
        assert checkbox_page.is_checked(1) is False
