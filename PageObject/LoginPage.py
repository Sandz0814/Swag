from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Login:

    userNameFieldXpath = "//input[@id='user-name']"
    passwordID = "password"
    loginButtonID = "login-button"
    dashboardLogoXpath = "//div[@class='app_logo']"
    invalidUserErrorXpath = "//h3[contains(text(),'Username and password do not match')]"
    userNameRequiredErrorXpath = "//h3[normalize-space()='Epic sadface: Username is required']"
    passwordRequiredErrorXpath = "//h3[normalize-space()='Epic sadface: Password is required']"

    def __init__(self, driver):
        self.driver = driver

    def inputUserName(self, userName):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_element_located((By.XPATH, self.userNameFieldXpath)))
        element.clear()
        element.send_keys(userName)

    def inputPassword(self, password):
        self.driver.find_element(By.ID, self.passwordID).clear()
        self.driver.find_element(By.ID, self.passwordID).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.ID, self.loginButtonID).click()

    def assertDashboardLogo(self):
        return self.driver.find_element(By.XPATH, self.dashboardLogoXpath).text

    def invalidUserNamePassError(self):
        errorText = self.driver.find_element(By.XPATH, self.invalidUserErrorXpath).text
        return errorText

    def userNameRequiredError(self):
        return self.driver.find_element(By.XPATH, self.userNameRequiredErrorXpath).text

    def passwordRequiredError(self):
        return self.driver.find_element(By.XPATH, self.passwordRequiredErrorXpath).text

    def hmm(self):
        x = self.driver.find_element(By.XPATH, self.dashboardLogoXpath)
        assert x.is_displayed()

