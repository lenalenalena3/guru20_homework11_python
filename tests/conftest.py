import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from demoga_tests.model.browser_settings import is_selenoid_enabled
from utils import attach


@pytest.fixture(scope="function")
def setup_browser():
    options = Options()
    options.page_load_strategy = 'eager'
    # Определяем, используется ли Selenoid
    use_selenoid = is_selenoid_enabled()
    print(f" selenoid: {use_selenoid}")
    if use_selenoid:
        # Конфигурация для Selenoid
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "128.0",
            "selenoid:options": {
                "enableLog": True,
                "enableVNC": True,
                "enableVideo": True
            },
            "goog:loggingPrefs": {"browser": "ALL"}
        }
        options.capabilities.update(selenoid_capabilities)

        driver = webdriver.Remote(
            command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
            options=options
        )
        browser.config.driver = driver
    else:
        # Локальная конфигурация
        driver_options = webdriver.ChromeOptions()
        driver_options.page_load_strategy = 'eager'
        browser.config.driver_options = driver_options

    browser.config.base_url = 'https://demoqa.com'

    yield browser
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    # attach.add_video(browser)
    browser.quit()
