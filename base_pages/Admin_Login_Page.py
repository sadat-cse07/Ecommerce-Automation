from selenium.webdriver.common.by import By


class Admin_Login_Page:
    # Login Page Locator
    # user_name="Email"
    # password_text="Password"
    # login_btn="//button[@type='submit']"

    user_name = "//input[@id='user-name']"
    password_text = "//input[@id='password']"
    login_btn = "//input[@id='login-button']"
    logout = "//a[@id='logout_sidebar_link']"

    # Define Constructor
    def __init__(self, driver):
        self.driver = driver

    # Define Action for every element
    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.user_name).clear()
        self.driver.find_element(By.XPATH, self.user_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_text).clear()
        self.driver.find_element(By.XPATH, self.password_text).send_keys(password)

    def enter_login(self):
        self.driver.find_element(By.XPATH, self.login_btn).click()

    def enter_logout(self):
        self.driver.find_element(By.XPATH, self.logout).click()
