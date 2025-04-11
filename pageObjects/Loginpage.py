from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Loginpage:
    textbox_username_cssselector="input[placeholder='Username']"
    textbox_password_cssselector="input[placeholder='Password']"
    login_xpath="//button[normalize-space()='Login']"
    logout_button_xpath="//p[@class='oxd-userdropdown-name']"
    logout_sel_xpath="//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Wait object to be used across methods

    def setusername(self, username):  # Debugging: Print the page source
        username_field = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.textbox_username_cssselector)))
        #username_field.clear()
        username_field.send_keys(username)

    def setpassword(self, password):
        password_field = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.textbox_password_cssselector)))
        #password_field.clear()
        password_field.send_keys(password)

    def loginbutton(self):
        login_btn = self.driver.find_element(By.XPATH, self.login_xpath)
        login_btn.click()

    def logoutbutton(self):
        # Click the dropdown first
        user_dropdown = self.driver.find_element(By.XPATH, self.logout_button_xpath)
        user_dropdown.click()

        # Wait for logout button to appear and click it
        logout_btn = self.driver.find_element(By.XPATH, self.logout_sel_xpath)
        logout_btn.click()