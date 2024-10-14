# Web Application Automation Testing

## Project Overview
This project is designed to automate the login functionality for a web application using Selenium and Python.

## Table of Contents
- [Project Overview](#project-overview)
- [Pre-requisites](#pre-requisites)
- [Test Scenarios](#test-scenarios)
- [Test Steps](#test-steps)
- [Expected Results](#expected-results)
- [Sample Code](#sample-code)
- [Conclusion](#conclusion)

## Pre-requisites
- Python 3.8+
- Selenium WebDriver
- Web browser drivers (e.g., ChromeDriver)

## Test Scenarios
1. **Valid Login Test**  
   Test for successful login with valid credentials.

2. **Invalid Login Test**  
   Test for login rejection with invalid credentials.

3. **Empty Field Validation**  
   Test for proper validation when fields are left blank.

## Test Steps
### Scenario 1: Valid Login
1. Navigate to the login page.
2. Enter valid username and password.
3. Click "Login" and verify redirection to the dashboard.

### Scenario 2: Invalid Login
1. Navigate to the login page.
2. Enter invalid username or password.
3. Click "Login" and verify the error message.

### Scenario 3: Empty Fields
1. Navigate to the login page.
2. Leave username or password blank.
3. Click "Login" and verify validation message.

## Expected Results
- **Valid Login**: Redirects to the dashboard.
- **Invalid Login**: Shows an error message.
- **Empty Fields**: Prompts for missing fields.

## Sample Code

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

     def test_login(self, setup):

        self.driver = setup
        try:
            self.log.info('Start Login Test')

            self.log.info('Parse User test data from json file')
            users = userData()
            
            self.log.info('Iterate negative and positive test')
            for user in users:

                self.login.inputUserName(user['userName'])
                self.login.inputPassword(user['password'])
                self.login.clickLoginButton()

                if user['expResult'] == self.login.invalidUserNamePassError():
                    assert True, (f'Expected "Epic sadface: Username and password do not match any user in this service"'
                                  f'but got {self.login.invalidUserNamePassError()}')

                elif user['expResult'] == self.login.userNameRequiredError():
                    assert True, f'Expected "Epic sadface: Username is required" but got {self.login.userNameRequiredError()}'

                elif user['expResult'] == self.login.passwordRequiredError():
                    assert True, f'Expected "Epic sadface: Password is required" but got {self.login.passwordRequiredError()}'

                elif user['expResult'] == self.login.assertDashboardLogo():
                    assert True, f'Expected "Swag Labs" but got {self.login.assertDashboardLogo()}'

                else:
                    allure.attach(self.driver.get_screenshot_as_png(), name="Dashboard",
                                  attachment_type=AttachmentType.PNG)
                    assert False

        except (AssertionError, NoSuchElementException, TimeoutException) as e:
            print(f'Error: {str(e)}')
            self.log.error(f'Error: {str(e)}')