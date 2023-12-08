import pytest
from selenium import webdriver
from Pages.login_page import LoginPage
from time import sleep
from selenium.webdriver.chrome.options import Options
BASE_URL= "https://www.betika.com/en-ke/"

# used to initiate the browser
# def pytest_setup_options():
#     chrome_options = Options()
    
#     # Read the headless option from pytest.ini
#     headless_option = pytest.config.getini('addopts').count('--headless') > 0
    
#     if headless_option:
#         chrome_options.add_argument('--headless')
    
#     return chrome_options


@pytest.fixture(scope='class')
def init_driver(request):
    options = Options()
    options.add_argument('--headless=new')
    # chrome_options = pytest_setup_options()
    browser_name = request.config.getoption("--browser-type", default="chrome")

    # Initialize the WebDriver based on the chosen browser
    if browser_name == "chrome":
        web_driver = webdriver.Chrome(options=options)
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
    login_page.do_login("0735638271", "2020")
    yield
    login_page.logout()


def pytest_addoption(parser):
    parser.addoption("--browser-type", action="store", default="chrome", help="Specify the browser for the tests (default: chrome)")