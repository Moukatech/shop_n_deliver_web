import pytest
from selenium import webdriver
from Pages.login_page import LoginPage
from time import sleep
BASE_URL= "https://www.betika.com/en-ke/"

# used to initiate the browser
@pytest.fixture(scope='class')
def init_driver(request):
    browser_name = request.config.getoption("--browser-type", default="chrome")

    # Initialize the WebDriver based on the chosen browser
    if browser_name == "chrome":
        web_driver = webdriver.Chrome()
    elif browser_name == "firefox":
        web_driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    request.cls.driver = web_driver
    web_driver.get(BASE_URL)
    web_driver.maximize_window()
    web_driver.implicitly_wait(10)
    yield web_driver
    web_driver.quit()
    

@pytest.fixture
def login(init_driver):
    # Perform login actions using the LoginPage class
    sleep(4)
    login_page = LoginPage(init_driver)
    login_page.do_login("0729208685", "Test123")


def pytest_addoption(parser):
    parser.addoption("--browser-type", action="store", default="chrome", help="Specify the browser for the tests (default: chrome)")