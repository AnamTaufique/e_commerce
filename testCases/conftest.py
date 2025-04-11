import pytest
from selenium import webdriver

# Command-line option to specify browser type
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
@pytest.fixture()
def setup(browser):  # Accepts browser fixture
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    elif browser.lower() == "edge":
        driver = webdriver.Edge()
        print("Launching Edge browser")
    else:
        raise ValueError(f"Unsupported browser: {browser}")
        print("Unsupported browser")

    driver.maximize_window()
    yield driver  # Provide WebDriver instance to test functions
    driver.quit()  # Close driver after test execution

#### html report
def pytest_configure(config):
    if hasattr(config, "_metadata"):  # ✅ This prevents the error
        config._metadata['Project Name'] = 'nop commerce'
        config.metadata['module_name']='CUSTOMER'
        config.metadata['Tester']='ANAM'

##### it is a hook to delete/edit environment info in html report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)





