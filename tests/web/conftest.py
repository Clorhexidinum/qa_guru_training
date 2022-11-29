import os
import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from asos.utils.allure import attach


# @pytest.fixture(scope='session', autouse=True)
# def browser_management():
#     browser.config.base_url = os.getenv('selene.base_url', 'https://asos.com')
#     browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
#     browser.config.window_width = 1920
#     browser.config.window_height = 1080
#     browser.config.hold_browser_open = (
#             os.getenv('selene.hold_browser_open', 'false').lower() == 'true'
#     )
#     browser.config.timeout = float(os.getenv('selene.timeout', '15'))
#     browser.open('')


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0',

    )
    parser.addoption(
        '--browser_name',
        default='chrome',

    )
    parser.addoption(
        '--window_size',
        default='1920x1080',

    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def setup_browser(request):
    browser_name = request.config.getoption('--browser_name')
    browser_version = request.config.getoption('--browser_version')
    window_size = str(request.config.getoption('--window_size')).split('x')

    options = Options()
    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": browser_version,
        "pageLoadStrategy": 'eager',
        "se"
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        # command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.base_url = 'https://asos.com'
    driver.set_window_size(window_size[0], window_size[1])
    browser.config.timeout = 20.0
    browser.open('')

    yield browser

    attach.screenshot()
    attach.logs()
    attach.html_dump()
    attach.video(browser)
    browser.close()
