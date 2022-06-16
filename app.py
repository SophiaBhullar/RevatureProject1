from flask import Flask, render_template,request
from controller.login_controller import check_manager_login, get_empLogin_page, get_managerLogin_page,check_emp_login
from controller.request_controller import accept_request, decline_request, delete_request, register_request, view_request


app = Flask(__name__)
app.secret_key="XYZ"

@app.route('/', methods=["GET"])
def landing_page():
    return render_template("home.html")

@app.route('/emplogin', methods=["GET"])
def empLogin_page():
    return get_empLogin_page()


@app.route('/emplogin/input', methods=["POST"])
def cust_empLogin():
    return check_emp_login(request.form)

@app.route('/managerLogin', methods=["GET"])
def login_page():
    return get_managerLogin_page()


@app.route('/managerLogin/input', methods=["POST"])
def cust_managerLogin():
    return check_manager_login(request.form)


@app.route('/fillrequest/request', methods=["POST"])
def register_new_user():
    return register_request(request.form)

@app.route('/viewRequests', methods=["GET"])
def view_requests():
    return view_request()

@app.route('/viewRequests/delete', methods=["POST"])
def request_delete():
    req_id=request.form['req_to_delete']
    print(req_id)
    return delete_request(req_id)

@app.route('/managerLogin/input/accept', methods=["POST"])
def request_accept():
    req_id = request.form['req_to_accept']
    print(req_id)
    return accept_request(req_id)


@app.route('/managerLogin/input/decline', methods=["POST"])
def request_decline():
    req_id = request.form['req_to_decline']
    return decline_request(req_id)


if __name__ == "__main__":
    app.run(debug=True)