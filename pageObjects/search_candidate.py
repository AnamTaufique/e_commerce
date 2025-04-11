from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class searchcandidate:
    candidate_txt_xpath="//input[@placeholder='Type for hints...']"
    drop_down_xpath="//div[@role='option']"
    search_butt_xpath="//button[normalize-space()='Search']"


    table_xpath="//div[@class='oxd-table']"
    table_row_xpath="/div[@class='oxd-table-row oxd-table-row--with-border']"
    table_column_xpath="//div[@class='oxd-table-card']//div[@role='cell']"

    def __init__(self, driver):
        self.driver = driver

    def set_candidate_name(self, name):
        wait = WebDriverWait(self.driver, 10)

        # Type into the candidate input box
        candidate_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']")
        candidate_input.clear()
        candidate_input.send_keys(name)

        # Wait for the dropdown option to appear (not just "Searching...")
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='option' and not(contains(text(), 'Searching'))]")))

        # Optionally press arrow down and enter to select the first match
        candidate_input.send_keys(Keys.ARROW_DOWN)
        candidate_input.send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, self.drop_down_xpath).click()

    def search_butt(self):
        self.driver.find_element(By.XPATH,self.search_butt_xpath).click()

    def getno_rows(self):
        return len(self.driver.find_elements(By.XPATH,self.table_row_xpath))

    def getno_colu(self):
        return len(self.driver.find_elements(By.XPATH,self.table_column_xpath))

    def search_customerby_name(self, name):
        flag = False
        for r in range(1, self.getno_rows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            cust_name = table.find_element(By.XPATH,
                                           f"(//div[@class='oxd-table-card']//div[@role='cell'][3])[{r}]").text
            if cust_name == name:
                flag = True
                break
        return flag
