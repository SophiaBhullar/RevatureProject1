

from flask import render_template,session
from repository.request_dao import delete_requests, select_requests
from service.request_service import create_request


def register_request(register_input):
  
    req_id = create_request(register_input)
        #return success
    if req_id is not None:
        session['req_id'] = req_id.req_id
        return render_template("empLogin.html")

    else:
        return "Failed"


def view_request():
    emp_id =int(session['emp_id']) 
    requests = select_requests(emp_id)
    print(requests)
    return render_template("viewRequests.html",allRequests=requests)


def delete_request(req_id):
    delete = delete_requests(req_id)
    return view_request()
     