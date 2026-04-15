import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )


@pytest.fixture( scope="function" )
def browserInstance(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    options = Options()
    options.add_experimental_option("prefs",
                                    {"credentials_enable_service": False, "profile.password_manager_enabled": False})
    options.add_argument("--incognito")
    service_obj = Service()
    if browser_name == "chrome":  #firefox
        driver = webdriver.Chrome(service=service_obj, options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=service_obj)

    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    request.node.driver = driver

    yield driver  # Before test function execution
    driver.quit()  # post your test function execution


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == "call" and report.failed:

        project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
        reports_dir = os.path.join(project_root, "Reports")
        os.makedirs(reports_dir, exist_ok=True)

        file_name = report.nodeid.replace("::", "_") + ".png"
        file_path = os.path.join(reports_dir, file_name)

        _capture_screenshot(file_path)

        html = f'''
                    <div>
                        <img src="{file_name}" alt="screenshot"
                        style="width:304px;height:228px;"
                        onclick="window.open(this.src)" align="right"/>
                    </div>
                    '''

        extra.append(pytest_html.extras.html(html))

    report.extras = extra


def _capture_screenshot(file_path):
    driver.get_screenshot_as_file(file_path)

    success = driver.get_screenshot_as_file(file_path)
    print("Screenshot saved:", success)
    print("File path:", file_path)
    print("Exists:", os.path.exists(file_path))

