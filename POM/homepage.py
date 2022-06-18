from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Homepage:
    def __init__(self,driver:WebDriver):
        self.driver = driver
    
    def getHomepage(self):
        print("homepage get homepage")
        return self.driver.get('http://127.0.0.1:5000/')


    def login_emp(self):
        return self.driver.find_element(By.ID, "emp_login")