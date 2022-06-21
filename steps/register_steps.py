from time import time
from unittest import result
from behave import given,when,then
import random
import string

def get_random_string(length):
    letters= string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


@given(u'I am on submit request page')
def titlespage(context):
    context.registrationpage.requestGetTitile()=="Reimbursement Form"

@when(u'I input in a valid employee ID')
def step_user_entered_valid_emp_id(context):
    context.registrationpage.emp_id_input().send_keys("1")


@when(u'I input in a valid description')
def step_user_entered_valid_description(context):
    valid_description = get_random_string(random.randint(1,100))
    context.registrationpage.description_input().send_keys("valid description")


@when(u'I input in a valid amount')
def step_user_entered_valid_amount(context):
    context.registrationpage.amount_input().send_keys("$400")


@when(u'I input in a valid status')
def step_user_entered_valid_status(context):
    context.registrationpage.status_input().send_keys("Pending")



@when(u'I input in a valid comments')
def step_user_entered_valid_comments(context):
    valid_comments = get_random_string(random.randint(1,100))
    context.registrationpage.comments_input().send_keys("Awaiting Approval")
    
@when(u'I click on sumit button')
def step_user_click_submit_button(context):
    context.registrationpage.register_request_button().click()

@then(u'I should have a success response')
def step_user_get_success_response(context):
    assert context.registrationpage.requestGetTitile() == "Reimbursement Form"