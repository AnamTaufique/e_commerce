import time

from allure_commons.model2 import Status

from pageObjects.Loginpage import Loginpage
from pageObjects.Add_customer import Add_customer
from pageObjects.search_candidate import searchcandidate
from Utilities.customlogger import LogGen
from Utilities.readproperties import ReadConfig


class Test_004_testcase:
    baseurl=ReadConfig.getapplicationurl()
    username=ReadConfig.getapplicationusername()
    password=ReadConfig.getapplicationpassword()

    logger = LogGen.loggen()


    def test_search_customer(self,setup):
        self.logger.info("******** test_004_testcase ******")
        self.logger.info("*******test_search_customer *********")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.logger.info("*******login process******")
        self.lp = Loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.loginbutton()

        self.addcust=Add_customer(self.driver)
        time.sleep(5)
        self.addcust.clickrecruitment()
        time.sleep(5)

        self.logger.info("****** search customer****")

        self.searchcand=searchcandidate(self.driver)
        time.sleep(5)

        self.searchcand.set_candidate_name("anam abdul khuddus")
        self.searchcand.search_butt()

        time.sleep(5)

        assert self.searchcand.search_customerby_name("anam abdul khuddus") is True

        self.logger.info("******** serach customer test execution id finished*****")



