from behave import given,when,then
import time


@given(u'user is on manager login page')
def mngrloginpage(context):
    context.mngrloginpage.getMngrLoginPage()


@when(u'user enter designation as "Manager"')
def designation(context):
    context.mngrloginpage.getDesignation().send_keys("Manager")


@when(u'user enter Username as "Ajay"')
def username(context):
    context.mngrloginpage.getUsername().send_keys("Ajay")


@when(u'user enter Password as "Ajay1234"')
def password(context):
    context.mngrloginpage.getPassword().send_keys("Ajay1234")

@when(u'user click on manager LOGIN button')
def clickLogin(context):
    context.mngrloginpage.getSubmitBtn().click()


@then(u'User can see view request page')
def titlespage(context):
    assert context.mngrloginpage.getPageTitle()=="Manager View Requests"


