from selenium.webdriver.common.by import By


class Login:

    userNameFieldId = "user-name"
    passwordID = "password"
    loginButtonID = "login-button"
    dashboardLogoXpath = "//div[@class='app_logo']"
    invalidUserErrorXpath = "//h3[contains(text(),'Epic sadface: Username and password do not match a')]"
    userNameRequiredErrorXpath = "//h3[normalize-space()='Epic sadface: Username is required']"
    passwordRequiredErrorXpath = "//h3[normalize-space()='Epic sadface: Password is required']"

    def __init__(self, driver):
        self.driver = driver

    def inputUserName(self, userName):
        self.driver.find_element(By.ID, self.userNameFieldId).clear()
        self.driver.find_element(By.ID, self.userNameFieldId).send_keys(userName)

    def inputPassword(self, password):
        self.driver.find_element(By.ID, self.passwordID).clear()
        self.driver.find_element(By.ID, self.passwordID).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.ID, self.loginButtonID).click()

    def assertDashboardLogo(self):
        return self.driver.find_element(By.XPATH, self.dashboardLogoXpath).text

    def invalidUserNamePassError(self):
        return self.driver.find_element(By.XPATH, self.invalidUserErrorXpath).text

    def userNameRequiredError(self):
        return self.driver.find_element(By.XPATH, self.userNameRequiredErrorXpath).text

    def passwordRequiredError(self):
        return self.driver.find_element(By.XPATH, self.passwordRequiredErrorXpath).text



