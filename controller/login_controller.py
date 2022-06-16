from flask import render_template,session
from controller.request_controller import mngrViewRequests
from repository.request_dao import select_all_requests
from service.login_service import check_login, validate_login 

def get_empLogin_page():
    return render_template("empLogin.html")


def get_managerLogin_page():
    return render_template("managerLogin.html")


def check_emp_login(login_input):

    #validate input
    input_dic={
        "designation":login_input["designation"],
        "emp_name":login_input["emp_name"],
        "emp_pass":login_input["emp_pass"]
    }
    if validate_login(input_dic):

        user_login = check_login(login_input)
        if user_login is None:
            return "Failed Login"
        else:
            session['emp_id'] = user_login.emp_id
            return render_template("fillRequest.html")


def check_manager_login(login_input):
    input_dic={
        "designation":login_input["designation"],
        "emp_name":login_input["emp_name"],
        "emp_pass":login_input["emp_pass"]
    }
    if validate_login(input_dic):
        user_login = check_login(login_input)
        if user_login is None:
            return "Failed Login"
        else:
            return mngrViewRequests()