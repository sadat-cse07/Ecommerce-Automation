import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from base_pages.Admin_Login_Page import Admin_Login_Page
from utilies.custom_logger import Logger_Maker
from utilies.read_properties import Read_config


class Test_01_Admin_Login:
    page_url = Read_config.login_url()
    textbox_username = Read_config.get_username()
    textbox_password = Read_config.get_password()
    invalid_user = Read_config.get_invalid_user()
    logger = Logger_Maker.log_gen()

    @pytest.mark.sanity
    def test_title_verification(self, setup):
        self.logger.info("****************Test_01_Admin_Login***********************")
        self.logger.info("****************title_verification***********************")
        self.driver = setup
        self.driver.get(self.page_url)
        act_title = self.driver.title
        exp_title = "Swag Labs"
        if act_title == exp_title:
            assert True
            self.driver.close()
        else:

            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_verification(self, setup):
        self.logger.info("****************login_verification***********************")
        self.driver = setup

        self.driver.get(self.page_url)

        self.admin_lp = Admin_Login_Page(self.driver)
        self.admin_lp.enter_username(self.textbox_username)
        self.admin_lp.enter_password(self.textbox_password)
        self.admin_lp.enter_login()

        time.sleep(5)

        act_dashboard_text = self.driver.find_element(
            By.XPATH, "//span[@class='title']"
        ).text

        if act_dashboard_text == "Products":
            self.logger.info("****************text_match***********************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\fail.png")

            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_invalid_verification(self, setup):
        self.logger.info("****************invalid_verification***********************")
        self.driver = setup

        self.driver.get(self.page_url)

        self.admin_lp = Admin_Login_Page(self.driver)

        self.admin_lp.enter_username(self.invalid_user)

        self.admin_lp.enter_password(self.textbox_password)

        self.admin_lp.enter_login()

        time.sleep(5)

        error_message = self.driver.find_element(
            By.XPATH, "//h3[@data-test='error']"
        ).text
        if (
            error_message
            == "Epic sadface: Username and password do not match any user in this service"
        ):
            self.logger.info("****************text_match***********************")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="VerificationFailed",
                attachment_type=AttachmentType.PNG,
            )
            assert True
            self.driver.close()
        else:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="VerificationFailed",
                attachment_type=AttachmentType.PNG,
            )
            self.driver.close()
            assert False
