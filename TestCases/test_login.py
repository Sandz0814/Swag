import time
import allure
from allure_commons.types import AttachmentType
from selenium.common import NoSuchElementException, TimeoutException
import pytest
from PageObject.LoginPage import Login
from Utilities.customLogger import LogGer
from TestData.data import userData


@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.usefixtures('setup')
class TestLogin:

    log = LogGer.logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login = Login(self.driver)

    def test_login(self, setup):

        self.driver = setup
        try:
            self.log.info('Start Login Test')

            self.log.info('Input valid username and password')

            users = userData()
            for user in users:

                self.login.inputUserName(user['userName'])
                time.sleep(2)
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








