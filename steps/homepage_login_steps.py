from behave import given,when, then

@given(u'I am on the homepage')
def step_user_is_on_homepage(context):
    print(" get homepage")
    context.homepage.getHomepage()

@when(u'I click on the login link')
def step_user_clicks_on_login_link(context):
    context.homepage.login_emp().click()

@then(u'I should be routed to the login page')
def step_user_is_routed_to_login_page(context):
    assert context.driver.title == "Employee Login"
  
