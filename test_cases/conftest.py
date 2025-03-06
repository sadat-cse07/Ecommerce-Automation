# import allure
# import pytest
# from allure_commons.types import AttachmentType
# from pytest_metadata.plugin import metadata_key
# from selenium import webdriver
#
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser",
#         action="store",
#         default="chrome",
#         help="Specify the browser:Chrome or Firefox",
#     )
#
# @pytest.fixture()
# def log_on_failure(request):
#     yield
#     item=request.node
#     if item.rep_call.failed:
#         allure.attach(
#             driver.get_screenshot_as_png(),
#             name="Failed_Screen_Shot",
#             attachment_type=AttachmentType.PNG,
#         )
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
#
#
# @pytest.fixture
# def setup(browser):
#     global driver
#
#     if browser == "chrome":
#         driver = webdriver.Chrome()
#         driver.maximize_window()
#     elif browser == "firefox":
#         driver = webdriver.Firefox()
#         driver.maximize_window()
#     else:
#         raise ValueError("Unsupported browser")
#     return driver
#
#
# def pytest_configure(config):
#     config.stash[metadata_key]["Project Name"] = "Ecommerce Project Automation"
#     config.stash[metadata_key]["Test Module Name"] = "Login Page Test"
#     config.stash[metadata_key]["Tester Name"] = "Sadat"
#
#
# @pytest.hookimpl(optionalhook=True)
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)


import allure
import pytest
from allure_commons.types import AttachmentType
from pytest_metadata.plugin import metadata_key
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Specify the browser: Chrome or Firefox",
    )


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def setup(browser):
    global driver

    if browser == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
    else:
        raise ValueError("Unsupported browser")

    yield driver  # Ensure driver is yielded properly
    driver.quit()  # Quit driver after test execution


def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "Ecommerce Project Automation"
    config.stash[metadata_key]["Test Module Name"] = "Login Page Test"
    config.stash[metadata_key]["Tester Name"] = "Sadat"


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


# Corrected hook function
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    # Check if the test failed
    if result.failed:
        # Ensure the driver is accessible
        driver = item.funcargs.get("setup")  # Fetch the driver from the fixture
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Failed_Screen_Shot",
                attachment_type=AttachmentType.PNG,
            )
