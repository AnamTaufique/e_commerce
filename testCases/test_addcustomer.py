import string
import time

import pytest

from pageObjects.Loginpage import Loginpage
from Utilities.customlogger import LogGen
from Utilities.readproperties import ReadConfig
from testCases.conftest import setup
from pageObjects.Add_customer import Add_customer
import random


class Test_003_test_case:
    baseurl=ReadConfig.getapplicationurl()
    username=ReadConfig.getapplicationusername()
    password=ReadConfig.getapplicationpassword()

    logger=LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_add_customers(self,setup):
        self.logger.info("*******88test_003_test_case*******")
        self.logger.info(" *********test_add_customer*******")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp=Loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.loginbutton()
        self.logger.info("logging is sucessfull")

        self.logger.info("starting add customer ")


        self.addcus=Add_customer(self.driver)
        time.sleep(5)
        self.addcus.clickrecruitment()

        time.sleep(5)

        self.addcus.addcustomer()

        self.logger.info("adding customer infomation")

        self.addcus.add_firstname("sana")
        self.addcus.add_middlename("khan")
        self.addcus.add_lastname("pathan")

        #self.addcus.vacancy("Junior Account Assistant")
        time.sleep(5)

        self.email=random_generator()+"@gmail.com"
        self.addcus.email_txt(self.email)
        self.addcus.cont_num_txt("12345678")
        time.sleep(5)
        #self.addcus.browse_resume()
        self.addcus.key_words("selenium")
        time.sleep(5)
        self.addcus.date_enter()
        self.addcus.txt_notes("hello")
        self.addcus.rad_butt()
        self.addcus.butt_click()
        act_txt = self.addcus.alert_txt()

        if act_txt:
            act_txt_1 = act_txt.text
            print(f"Alert Text: {act_txt_1}")  # Debugging
            if act_txt_1 == "Successfully Saved":
                assert True
                self.logger.info("Add customer test is successful")
            else:
                self.driver.save_screenshot("./Screenshots/add_customer_test.png")
                self.logger.error("Add customer test failed")
                assert False
        else:
            print("Failed to locate alert text!")
            self.driver.save_screenshot("./Screenshots/alert_not_found.png")
            assert False

        self.driver.close()
        self.logger.info("end of add customer test")



def random_generator(size=8, char=string.ascii_lowercase + string.digits):
    return "".join(random.choice(char) for _ in range(size))






