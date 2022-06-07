

from flask import render_template
from service.request_service import create_login, create_request


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
    req_id = create_request(register_input)
        #return success
    if req_id is not None:
        return render_template("empLogin.html")

    else:
        return "Failed"