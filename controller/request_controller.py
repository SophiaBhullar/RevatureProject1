

from flask import render_template,session
from repository.request_dao import select_requests
from service.request_service import create_request


def register_request(register_input):
    #validate input
    """ input_dict={
        "description":register_input["description"],
        "amount":register_input["amount"],
        "status":register_input["status"],
        "comments":register_input["comments"],

    }

    if validate_request(input_dict): """

        #create new user
    #emp_id = create_login(register_input)
    global req_id 
    req_id = create_request(register_input)
        #return success
    if req_id is not None:
        return render_template("empLogin.html")

    else:
        return "Failed"


def view_request():
    emp_id =int(session['emp_id']) 
    requests = select_requests(emp_id)
    print(requests)
    return render_template("viewRequests.html",allRequests=requests)
    