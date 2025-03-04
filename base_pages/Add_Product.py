from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Add_Product:
    add_to_cart_btn = "//button[@id='add-to-cart-sauce-labs-backpack']"
    click_shopping_cart = "//a[@class='shopping_cart_link']"
    click_checkout = "//button[@id='checkout']"
    enter_f_name = "//input[@id='first-name']"
    enter_l_name = "//input[@id='last-name']"
    zip_code = "//input[@id='postal-code']"
    click_continue_btn = "//input[@id='continue']"
    finish_btn = "//button[@id='finish']"
    act_text = "//*[@id='checkout_complete_container']/h2"

    def __init__(self, driver):
        self.driver = driver

    def product_add(self):
        self.driver.find_element(By.XPATH, self.add_to_cart_btn).click()

    def shopping_cart(self):
        self.driver.find_element(By.XPATH, self.click_shopping_cart).click()

    def checkout(self):
        self.driver.find_element(By.XPATH, self.click_checkout).click()

    def enter_first_name(self, first_name):
        self.driver.find_element(By.XPATH, self.enter_f_name).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.XPATH, self.enter_l_name).send_keys(last_name)

    def enter_zip_code(self, code):
        self.driver.find_element(By.XPATH, self.zip_code).send_keys(code)

    def continue_button(self):
        self.driver.find_element(By.XPATH, self.click_continue_btn).click()

    def finish(self):
        self.driver.find_element(By.XPATH, self.finish_btn).click()

    def actual_text(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.act_text))
        )
