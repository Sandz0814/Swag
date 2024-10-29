import configparser
import os
from selenium import webdriver
import pytest

file = os.path.join(os.path.dirname(__file__), 'config.ini')
config = configparser.ConfigParser()
config.read(file)
url = config['website']['url']


@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Edge()
    driver.implicitly_wait(10)
    driver.maximize_window()

    driver.get(url)

    request.cls.driver = driver
    yield driver

    driver.close()
    driver.quit()


# Hook to capture test failures and take screenshots
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute the test and capture the result
    outcome = yield
    report = outcome.get_result()

    # Check if the test failed during the "call" phase
    if report.when == "call" and report.failed:
        # Get the WebDriver instance from the test (from the 'setup' fixture)
        driver = item.cls.driver if hasattr(item.cls, 'driver') else None

        if driver:
            # Create the Report directory if it doesn't exist
            report_dir = "./Report"
            if not os.path.exists(report_dir):
                os.makedirs(report_dir)

            # Save the screenshot in the Report directory
            screenshot_name = os.path.join(report_dir, f"Failed {item.name}.png")
            driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved: {screenshot_name}")


