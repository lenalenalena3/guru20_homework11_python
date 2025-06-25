import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="session")
def setup_options():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options


@pytest.fixture(scope="function")
def open_page_demoqa(setup_options):
    browser.config.base_url = 'https://demoqa.com'
    yield
    browser.quit()