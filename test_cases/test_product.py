import pytest

from base_pages.Add_Product import Add_Product
from base_pages.Admin_Login_Page import Admin_Login_Page
from utilies.custom_logger import Logger_Maker
from utilies.read_properties import Read_config


class Test_03_Product:
    page_url = Read_config.login_url()
    textbox_username = Read_config.get_username()
    textbox_password = Read_config.get_password()
    text = "Thank you for your order!"
    first_name = "sadat"
    last_name = "anwar"
    zip = "4000"
    logger = Logger_Maker.log_gen()

    @pytest.mark.regression
    def test_product_add_to_chart(self, setup):
        self.logger.info("**********User Login*************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.page_url)

        self.admin_lp = Admin_Login_Page(self.driver)
        self.admin_lp.enter_username(self.textbox_username)
        self.admin_lp.enter_password(self.textbox_password)
        self.admin_lp.enter_login()

        self.logger.info("********Start add product************")

        self.add_product = Add_Product(self.driver)
        self.add_product.product_add()
        self.add_product.shopping_cart()
        self.add_product.checkout()
        self.add_product.enter_first_name(self.first_name)
        self.add_product.enter_last_name(self.last_name)
        self.add_product.enter_zip_code(self.zip)
        self.add_product.continue_button()
        self.add_product.finish()

        self.logger.info("*****Validation checking********")

        expected_text = self.add_product.actual_text().text
        self.logger.info(f"Actual text found: {expected_text}")
        if expected_text == "Thank you for your order!":
            assert True
