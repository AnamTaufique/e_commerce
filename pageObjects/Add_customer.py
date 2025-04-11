from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Add_customer:
    link_recruitmwnt_menu_xpath=" //span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='Recruitment']"
    butt_add_customer_xpath="//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    txt_first_name_xpath="//input[@placeholder='First Name']"
    txt_middle_name_xpath="//input[@placeholder='Middle Name']"
    txt_last_name_xpath="//input[@placeholder='Last Name']"
    link_vacancy_xpath="//div[@class='oxd-select-text oxd-select-text--active']"


    link_menu_j_account_assis="//div[contains(text(),'Junior Account Assistant')]"

    link_menu_software_developer="//div[contains(text(),'Software Developer')]"
    txt_email_xpath="//div[3]//div[1]//div[1]//div[1]//div[2]//input[1]"
    txt_con_num_xpath="//body/div[@id='app']/div[@class='oxd-layout orangehrm-upgrade-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container orangehrm-save-candidate-page']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-3 orangehrm-full-width-grid']/div[2]/div[1]/div[2]/input[1]"
    upload_resume_xpath="//div[@class='oxd-file-button']"
    upload_file_button_xpath="//i[@class='oxd-icon bi-upload oxd-file-input-icon']"
    txt_keywords_xpath="//input[@placeholder='Enter comma seperated words...']"
    link_date_xpath="//i[@class='oxd-icon bi-calendar oxd-date-input-icon']"
    link_today_xpath="//div[@class='oxd-date-input-link --today']"
    link_month_xpath="//i[@class='oxd-icon bi-calendar oxd-date-input-icon']"
    txt_notes_xpath="//textarea[@placeholder='Type here']"
    rd_consent_xpath="//span[@class='oxd-checkbox-input oxd-checkbox-input--active --label-right oxd-checkbox-input']"
    but_save_xpath="//button[normalize-space()='Save']"
    alert_save_xpath="//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']"

    def __init__(self,driver):
        self.driver=driver

    def clickrecruitment(self):
        self.driver.find_element(By.XPATH,self.link_recruitmwnt_menu_xpath).click()

    def addcustomer(self):
        element =self. driver.find_element(By.XPATH,self.butt_add_customer_xpath)
        time.sleep(5)
        #self.driver.execute_script("arguments[0].scrollIntoView();", element)

        element.click()

        time.sleep(5)

    def add_firstname(self,fname):
        namef=self.driver.find_element(By.XPATH,self.txt_first_name_xpath).send_keys(fname)

    def add_middlename(self,mname):
        self.driver.find_element(By.XPATH,self.txt_middle_name_xpath).send_keys(mname)

    def add_lastname(self,lname):
        self.driver.find_element(By.XPATH,self.txt_last_name_xpath).send_keys(lname)

    def vacancy(self,menu):
        menu_bar=self.driver.find_element(By.XPATH,self.link_vacancy_xpath)
        menu_bar.click()
        menu_bar.send_keys(menu)
        time.sleep(5)





    def email_txt(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)

    def cont_num_txt(self,c_num):
        self.driver.find_element(By.XPATH,self.txt_con_num_xpath).send_keys(c_num)



    def browse_resume(self):
        # Wait for the file input element to be present in the DOM
        upload_r = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.upload_resume_xpath))
        )
        upload_r.click()
        time.sleep(5)
        upload_r.send_keys('/Users/anam/anam.pdf')
        upload_r.click()
        time.sleep(5)


    def key_words(self,words):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.txt_keywords_xpath))
        ).send_keys(words)

    def date_enter(self):
        self.driver.find_element(By.XPATH,self.link_date_xpath).click()
        self.driver.find_element(By.XPATH,self.link_today_xpath).click()

    def txt_notes(self,notes):
        self.driver.find_element(By.XPATH,self.txt_notes_xpath).send_keys(notes)

    def rad_butt(self):
        self.driver.find_element(By.XPATH,self.rd_consent_xpath).click()

    def butt_click(self):
        self.driver.find_element(By.XPATH,self.but_save_xpath).click()


    def alert_txt(self):
            try:
                alert_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "oxd-text--toast-message"))
                )
                return alert_element  # Return WebElement
            except:
                print("Alert element not found!")
                return None

