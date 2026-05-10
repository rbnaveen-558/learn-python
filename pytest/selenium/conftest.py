import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests with. Supported values: chrome, firefox",
    )


@pytest.fixture(scope="session")
def browser(request) -> WebDriver:
    browser_name = request.config.getoption("--browser").lower()

    if browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    else:
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1200,900")
        driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(5)
    yield driver
    driver.quit()
