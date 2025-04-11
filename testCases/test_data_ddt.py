import pytest

from pageObjects.Loginpage import Loginpage
from testCases.conftest import setup
import time
from Utilities.readproperties import ReadConfig
from Utilities.customlogger import LogGen
from Utilities import Excelutils

class Test_001_login:
    baseurl = ReadConfig.getapplicationurl()
    path = "./TestData/login_data.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("****** Test_001_login *******")
        self.logger.info("******** test_login *********")
        self.driver = setup
        self.driver.maximize_window()
        time.sleep(5)  # Avoid sleep; use WebDriverWait

        self.driver.get(self.baseurl)
        self.lp = Loginpage(self.driver)


        self.row = Excelutils.getRowCount(self.path, 'Sheet1')
        print(f"Number of rows: {self.row}")

        self.status = []  # Corrected list reference
        for r in range(2, self.row + 1):  # Fixed loop range
            self.user = Excelutils.readData(self.path, 'Sheet1', r, 1)
            self.password = Excelutils.readData(self.path, 'Sheet1', r, 2)
            self.exp = Excelutils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setusername(self.user)  # Fixed variable name
            self.lp.setpassword(self.password)
            self.lp.loginbutton()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "OrangeHRM"

            if act_title == exp_title:
                if self.exp.lower() == "pass":
                    self.logger.info("Test Passed")
                    self.lp.logoutbutton()
                    self.status.append("pass")
                    assert True
                elif self.exp.lower() == "Fail": # Expected fail but passed
                    self.driver.save_screenshot("./Screenshots/"+"test_login_fail.png")
                    self.logger.error("Unexpected Pass (Should Fail)")
                    self.lp.logoutbutton()
                    self.status.append("Fail")
                    assert False
            elif act_title != exp_title:  # Login failed # Login failed
                if self.exp.lower() == "pass":
                    self.driver.save_screenshot("./Screenshots/"+"test_login_fail.png")
                    self.logger.info("Test Failed (Expected Pass)")
                    self.driver.close()
                    self.status.append("Fail")
                    assert False
                elif self.exp.lower() == "Fail":
                    self.logger.error("Expected Fail (Correct Behavior)")
                    self.status.append("pass")
                    self.driver.close()
                    assert True

        if "Fail" not in self.status:
            self.logger.info("DDT Login test case passed")
            self.driver.close()
            assert True
        else:
            self.logger.error("DDT Login test case failed")
            self.driver.close()
            assert False

        self.logger.info("End of DDT test")









