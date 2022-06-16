

from distutils.log import FATAL
from operator import truediv
import re

def validate_log(new_login : tuple) -> bool:
    return validate_designation(new_login[0]) and validate_emp_name(new_login[1]) and validate_emp_pass(new_login[2])


def validate_req(new_request : tuple) -> bool:
    return validate_emp_id(new_request[0]) and validate_description(new_request[1]) and validate_amount(new_request[2]) and validate_status(new_request[3]) and validate_comments(new_request[4])


def validate_emp_id(emp_id):
    if re.findall('^[1-9]+$',emp_id):
        return True
    else:
        return False


def validate_description(description):
    if re.findall('(\d*[a-zA-Z]+\d*)+', description) and len(description)<=100  and description == description.strip():
        return True
    else:
        return False

def validate_amount(amount):
    new_amount=amount.replace("$", "")
    if re.findall('\$\ ?[+-]?[0-9]{1,3}(?:,?[0-9])*(?:\.[0-9]{1,2})?', amount):
        if(int(new_amount)>0 and int(new_amount)<=1000):
            return True
        else:
            return False
    else:
        return False

def validate_status(status):
    pending="Pending"
    approved="Approved"
    declined="Declined"

    if pending in status or approved in status or declined in status and not " " in status:
        return True
    else:
        return False

def validate_comments(comments):
    if re.findall('(\d*[a-zA-Z]+\d*)+', comments) and len(comments)<=100 and comments == comments.strip():
        return True
    else:
        return False


def validate_designation(designation):
    employee="Employee"
    manager="Manager"
    
    if employee in designation or manager in designation and not " " in designation:
        return True
    else:
        return False


def validate_emp_name(emp_name):
    if re.findall('[A-Za-z]{2,15}', emp_name) and len(emp_name)<=15 and not " " in emp_name:
        return True
    else:
        return False


def validate_emp_pass(emp_pass):
    if re.findall('[A-Za-z]{0,9}', emp_pass) and len(emp_pass)<=10 and not " " in emp_pass:
        return True
    else:
        return False