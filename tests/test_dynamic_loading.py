# tests/test_dynamic_loading.py

import allure
from pages.dynamic_loading_page import DynamicLoadingPage

@allure.feature("Dynamic Loading")
@allure.story("Load Hidden Element")
@allure.severity(allure.severity_level.NORMAL)
def test_dynamic_loading(page):
    dynamic_loading_page = DynamicLoadingPage(page)
    dynamic_loading_page.navigate()

    with allure.step("Click the start button"):
        dynamic_loading_page.click_start()

    with allure.step("Wait 6 seconds for selector"):
        dynamic_loading_page.wait_loading(6000)

    with allure.step("Ensure final message is correct"):
        assert dynamic_loading_page.check_message("Hello World!") is True