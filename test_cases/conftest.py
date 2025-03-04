import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Specify the browser:Chrome or Firefox",
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
    return driver


def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "Ecommerce Project Automation"
    config.stash[metadata_key]["Test Module Name"] = "Login Page Test"
    config.stash[metadata_key]["Tester Name"] = "Sadat"


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
