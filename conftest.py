# conftest.py
import pytest
import allure
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

def attach_network_logs(page, test_name):
    requests = []
    page.on("request", lambda req: requests.append(f"➡️ {req.method} {req.url}"))
    page.on("response", lambda res: requests.append(f"⬅️ {res.status} {res.url}"))

    if requests:
        allure.attach(
            "\n".join(requests),
            name=f"{test_name}_network",
            attachment_type=allure.attachment_type.TEXT
        )
        
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        page = item.funcargs.get("page", None)
        if page:
            # Screenshot
            screenshot = page.screenshot(full_page=True)
            allure.attach(
                screenshot,
                name=f"{item.name}_failure",
                attachment_type=allure.attachment_type.PNG
            )

            # Console logs
            logs = []
            page.on("console", lambda msg: logs.append(f"[{msg.type}] {msg.text}"))
            if logs:
                allure.attach(
                    "\n".join(logs),
                    name=f"{item.name}_console_logs",
                    attachment_type=allure.attachment_type.TEXT
                )

            # Network logs
            attach_network_logs(page, item.name)
