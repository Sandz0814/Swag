import time
import allure
from allure_commons.types import AttachmentType
from selenium.common import NoSuchElementException, TimeoutException
import pytest
from selenium.webdriver.common.by import By
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
                time.sleep(1)
                self.login.inputPassword(user['password'])
                self.login.clickLoginButton()

        except (AssertionError, TimeoutException, NoSuchElementException) as e:
            print(f'Error: {str(e)}')
            self.log.error(f'Error: {str(e)}')








