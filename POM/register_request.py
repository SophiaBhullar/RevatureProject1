from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class RegistrationPage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def emp_id_input(self):
        return self.driver.find_element(By.ID, "emp_id")

    def description_input(self):
        return self.driver.find_element(By.ID, "description")

    def amount_input(self):
        return self.driver.find_element(By.ID, "amount")

    def status_input(self):
        return self.driver.find_element(By.ID, "status")

    def comments_input(self):
        return self.driver.find_element(By.ID, "comments")
    
    def register_request_button(self):
        return self.driver.find_element(By.ID, "submit_request")

    def requestGetTitile(self):
        return self.driver.title
