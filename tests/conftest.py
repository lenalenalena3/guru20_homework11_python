import os

import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver
    yield browser

    browser.quit()


@pytest.fixture(scope="function")
def setup_browser():
    options = Options()
    options.page_load_strategy = 'eager'

    # Определяем, используется ли Selenoid
    use_selenoid = os.getenv('USE_SELENOID', 'false').lower() == 'true'

    if use_selenoid:
        # Конфигурация для Selenoid
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "100.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        options.capabilities.update(selenoid_capabilities)

        driver = webdriver.Remote(
            command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
            options=options
        )
    else:
        # Локальная конфигурация
        driver_options = webdriver.ChromeOptions()
        driver_options.page_load_strategy = 'eager'
        browser.config.driver_options = driver_options

    browser.config.driver = driver
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 10.0

    yield browser

    browser.quit()