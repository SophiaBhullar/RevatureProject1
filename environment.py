from behave.runner import Context
from selenium import webdriver
from POM.homepage import Homepage
from POM.login_POM import Loginpage
from POM.mngrLoginPOM import ManagerLoginpage
from POM.register_request import RegistrationPage

def before_all(context: Context):
    # We need to add a driver to the context
    context.driver = webdriver.Chrome("/Users/bhull/RevatureProject1/ERS/Drivers/chromedriver.exe")
    print(f'\n context driver here: {context.driver}\n')
    # We need to add all POMS to the context
    context.homepage = Homepage(context.driver)
    context.loginpage=Loginpage(context.driver)
    context.registrationpage = RegistrationPage(context.driver)
    context.mngrloginpage=ManagerLoginpage(context.driver)
    # We add an implicit wait to work with latency issues
    context.driver.implicitly_wait(1)

def after_all(context: Context):
    # This will make sure at the end of a behave test all the drivers are closed
    context.driver.quit()