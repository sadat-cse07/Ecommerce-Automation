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
#         help="Specify the browser: Chrome or Firefox",
#     )
#
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
#
#     yield driver  # Ensure driver is yielded properly
#     driver.quit()  # Quit driver after test execution
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
#
#
# # Corrected hook function
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     result = outcome.get_result()
#
#     # Check if the test failed
#     if result.failed:
#         # Ensure the driver is accessible
#         driver = item.funcargs.get("setup")  # Fetch the driver from the fixture
#         if driver:
#             allure.attach(
#                 driver.get_screenshot_as_png(),
#                 name="Failed_Screen_Shot",
#                 attachment_type=AttachmentType.PNG,
#             )

# import allure
# import pytest
# from allure_commons.types import AttachmentType
# from pytest_metadata.plugin import metadata_key
# from selenium import webdriver
#
# # Configure logging
# # logging.basicConfig(
# #     level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
# # )
# # logger = logging.getLogger(__name__)
#
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser",
#         action="store",
#         default="chrome",
#         help="Specify the browser: chrome or firefox",
#     )
#
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
#
#
# @pytest.fixture
# def setup(browser):
#     # logger.info(f"Starting tests on {browser} browser")
#
#     selenium_grid_url = "http://localhost-hub:4444"  # Dockerfile Selenium Grid
#
#     options = None
#     if browser == "chrome":
#         options = webdriver.ChromeOptions()
#     elif browser == "firefox":
#         options = webdriver.FirefoxOptions()
#     else:
#         raise ValueError("Unsupported browser")
#
#     options.add_argument("--headless")  # Run headless in Dockerfile
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#
#     # driver = webdriver.Remote(command_executor=selenium_grid_url, options=options)
#     driver = webdriver.Remote(command_executor=selenium_grid_url, options=options)
#     driver.maximize_window()
#
#     yield driver
#     driver.quit()
#     # logger.info(f"Tests completed on {browser} browser")
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
#
#
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     result = outcome.get_result()
#
#     # Check if the test failed
#     if result.failed:
#         # Ensure the driver is accessible
#         driver = item.funcargs.get("setup")  # Fetch the driver from the fixture
#         if driver:
#             allure.attach(
#                 driver.get_screenshot_as_png(),
#                 name="Failed_Screen_Shot",
#                 attachment_type=AttachmentType.PNG,
#             )

import allure
import pytest
from allure_commons.types import AttachmentType
from pytest_metadata.plugin import metadata_key
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Specify the browser: chrome or firefox",
    )


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def setup(browser):
    options = None
    if browser == "chrome":
        options = Options()
        # Use the installed Chromium browser in the container
        options.binary_location = "/usr/bin/chromium"
        # Set up the Service object with chromedriver location
        service = Service("/usr/bin/chromedriver")
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        service = Service("/usr/bin/geckodriver")
    else:
        raise ValueError("Unsupported browser")

    options.add_argument("--headless")  # Run headless in Docker
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Initialize the driver with the Service and options
    if browser == "chrome":
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError("Unsupported browser")

    driver.maximize_window()

    yield driver
    driver.quit()


def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "Ecommerce Project Automation"
    config.stash[metadata_key]["Test Module Name"] = "Login Page Test"
    config.stash[metadata_key]["Tester Name"] = "Sadat"


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


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
