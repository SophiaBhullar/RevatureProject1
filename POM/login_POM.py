from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Loginpage:
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def getEmpLoginPage(self):
        return self.driver.get("http://127.0.0.1:5000/emplogin")

    def getDesignation(self):
        return self.driver.find_element(By.XPATH,"//*[@id='designation']")
        
    def getUsername(self):
        return self.driver.find_element(By.XPATH,"//*[@id='emp_name']")

    def getPassword(self):
        return self.driver.find_element(By.XPATH,"//*[@id='emp_pass']")

    def getSubmitBtn(self):
        return self.driver.find_element(By.XPATH,"//*[@id='loginbtn']")

    def getPageTitle(self):
        return self.driver.title

    def getPageElement(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div/h2")