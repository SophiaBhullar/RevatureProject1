from flask import render_template
from service.login_service import check_login 

def get_empLogin_page():
    return render_template("empLogin.html")


def get_managerLogin_page():
    return render_template("managerLogin.html")


def check_cust_login(login_input):
    user_login = check_login(login_input)
    if user_login is None:
        return "Failed Login"
    else:
        return "Success"