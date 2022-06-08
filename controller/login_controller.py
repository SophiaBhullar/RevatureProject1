from flask import render_template,session
from service.login_service import check_login 

def get_empLogin_page():
    return render_template("empLogin.html")


def get_managerLogin_page():
    return render_template("managerLogin.html")


def check_emp_login(login_input):
    user_login = check_login(login_input)
    if user_login is None:
        return "Failed Login"
    else:
        session['emp_id'] = user_login.emp_id
        return render_template("fillRequest.html")


def check_manager_login(login_input):
    user_login = check_login(login_input)
    if user_login is None:
        return "Failed Login"
    else:
        return "Success"