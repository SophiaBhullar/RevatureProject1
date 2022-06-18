from behave import given,when,then
import time


@given(u'user is on login page')
def loginPage(context):
    context.loginpage.getEmpLoginPage()


@when(u'user enter designation as "Employee"')
def designation(context):
    context.loginpage.getDesignation().send_keys("Employee")


@when(u'user enter Username as "Sophia"')
def username(context):
    context.loginpage.getUsername().send_keys("Sophia")


@when(u'user enter Password as "Sophia1234"')
def password(context):
    context.loginpage.getPassword().send_keys("Sophia1234")

@when(u'user click on LOGIN button')
def clickLogin(context):
    context.loginpage.getSubmitBtn().click()


@then(u'User can see fill request page')
def titlespage(context):
    assert context.loginpage.getPageTitle()=="Reimbursement Form"


