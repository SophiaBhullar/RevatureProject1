

from flask import render_template,session
from repository.request_dao import delete_requests, select_all_requests, select_requests, update_requests
from service.request_service import create_request, validate_requests


def register_request(register_input):

    #validate input
    input_dict={
        "emp_id":register_input["emp_id"],
        "description":register_input["description"],
        "amount":register_input["amount"],
        "status":register_input["status"],
        "comments":register_input["comments"]
    }

    if validate_requests(input_dict):

        req_id = create_request(register_input)
        #return success
        if req_id is not None:
            return render_template("fillRequest.html")

    else:
        return "Failed"


def view_request():
    emp_id =int(session['emp_id']) 
    requests = select_requests(emp_id)
    print(requests)
    return render_template("viewRequests.html",allRequests=requests)


def mngrViewRequests():
    req = select_all_requests()
    print(req)
    return render_template("mngrViewrequests.html",allRequests=req)


def delete_request(req_id):
    delete = delete_requests(req_id)
    return view_request()
     

def accept_request(req_id):
    accept = update_requests(req_id,"Approved","Payment made")
    return mngrViewRequests()
    

def decline_request(req_id):
    decline = update_requests(req_id,"Declined","Payment Refused")
    return mngrViewRequests()