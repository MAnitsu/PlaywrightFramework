# tests/test_dropdown.py

import allure
from pages.dropdown_page import DropdownPage

@allure.feature("Dropdowns")
@allure.story("Select Option from Dropdown")
@allure.severity(allure.severity_level.NORMAL)
def test_dropdown(page):
    dropdown_page = DropdownPage(page)
    dropdown_page.navigate()

    with allure.step("Select option from dropdown"):
        dropdown_page.select_option("2")

    with allure.step("Ensure option is correct"):
        assert dropdown_page.check_option("2") is True