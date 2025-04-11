import pytest
from selenium import webdriver
from pageObjects.Loginpage import Loginpage
from testCases.conftest import setup
import time
from Utilities.readproperties import ReadConfig
from Utilities.customlogger import LogGen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Test_001_login:
    baseurl=ReadConfig.getapplicationurl()
    username=ReadConfig.getapplicationusername()
    password=ReadConfig.getapplicationpassword()

    logger=LogGen.loggen()
    @pytest.mark.regression
    def test_homepage_title(self,setup):
       self.logger.info("********** Test_001_login ********")
       self.logger.info("**********test_homepage_title ****")
       self.driver=setup
       self.driver.maximize_window()
       self.driver.get(self.baseurl)
       time.sleep(5)
       act_title=self.driver.title

       if act_title =="OrangeHRM":
           self.logger.info("********* Home_title test case is passed******")
           assert True

       else:
           self.driver.save_screenshot("./Screenshots/" + "test_homepage_title.png")
           self.logger.error("*********Home_title test case is Failed ********")
           assert False
           self.driver.close()
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("******** test_login *********")
        self.driver=setup
        self.driver.maximize_window()
        # Use WebDriverWait instead of sleep
        time.sleep(5)
        act_title = self.driver.title
        self.driver.get(self.baseurl)
        self.lp=Loginpage(self.driver)
        time.sleep(5)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        time.sleep(5)
        self.lp.loginbutton()
        time.sleep(5)
        act_title=self.driver.title
        time.sleep(5)

        if act_title=="OrangeHRM":
            self.logger.info("**********test_login is passed********")
            assert True

        else:
            self.logger.error("********* test_login is failed*****88")
            self.driver.save_screenshot("./Screenshots/" + "test_login.png")
            assert False


        self.lp.logoutbutton()


