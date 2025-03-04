import time

from selenium.webdriver.common.by import By

from base_pages.Admin_Login_Page import Admin_Login_Page
from utilies import excel_utils
from utilies.custom_logger import Logger_Maker
from utilies.read_properties import Read_config


class Test_02_User_Login:
    page_url = Read_config.login_url()
    logger = Logger_Maker.log_gen()
    path = ".//test_data//login_data.xlsx"
    status_list = []

    def test_login_verification(self, setup):
        self.logger.info("****************login_verification***********************")
        self.driver = setup
        self.driver.implicitly_wait(35)
        self.driver.get(self.page_url)
        self.admin_lp = Admin_Login_Page(self.driver)

        self.rows = excel_utils.get_row_count(self.path, "Sheet1")
        print("Number of Rows Count:", self.rows)

        for r in range(2, self.rows + 1):
            self.username = excel_utils.read_data(self.path, "Sheet1", r, 1)
            self.password = excel_utils.read_data(self.path, "Sheet1", r, 2)
            self.expect_result = excel_utils.read_data(self.path, "Sheet1", r, 3)
            self.admin_lp.enter_username(self.username)
            self.admin_lp.enter_password(self.password)
            self.admin_lp.enter_login()

            time.sleep(35)
            act_title = self.driver.find_element(
                By.XPATH, "//span[@class='title']"
            ).text
            exp_title = "Products"

            if act_title == exp_title:
                if self.expect_result == "pass":
                    self.logger.info("Test should be Passed")
                    self.status_list.append("Passed")
                    self.driver.find_element(
                        By.XPATH, "//button[@id='react-burger-menu-btn']"
                    ).click()
                    self.admin_lp.enter_logout()
                elif self.expect_result == "failed":
                    self.logger.info("This test data not be passed")
                    self.status_list.append("Failed")
                    # self.driver.close()
            elif act_title != exp_title:
                if self.expect_result == "pass":
                    self.logger.info("This test data not be passed")
                    self.status_list.append("Failed")
                elif self.expect_result == "failed":
                    self.logger.info("Test should be Passed")
                    self.status_list.append("Passed")
        print("Status list is:", self.status_list)

        if "failed" in self.status_list:
            self.logger.info("test data driven is Fail")
            assert False
        else:
            self.logger.info("Test data driven is Pass")
            assert True
