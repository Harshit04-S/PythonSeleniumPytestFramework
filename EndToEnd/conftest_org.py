import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from  selenium.webdriver.chrome.options import Options

# To register the options we are sending from command line during test run
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )


@pytest.fixture(scope="function")
def browserInstance(request):        # request: it will have hold of the whole command what we are requesting to run.
    # to get the option that we are passing from command line during testcase run
    browser_name = request.config.getoption("browser_name")
    #to handle the chrome ui popup
    options = Options()
    options.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False})
    options.add_argument("--incognito")

    # service_obj = ChromeService()
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(), options=options)
        driver.implicitly_wait(5)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService())
        driver.implicitly_wait(5)

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    yield driver
    driver.close()



