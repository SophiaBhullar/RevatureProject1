from flask import Flask, render_template,request
from controller.login_controller import check_cust_login, get_empLogin_page, get_managerLogin_page


app = Flask(__name__)


@app.route('/', methods=["GET"])
def landing_page():
    return render_template("home.html")

@app.route('/emplogin', methods=["GET"])
def empLogin_page():
    return get_empLogin_page()


@app.route('/emplogin/input', methods=["POST"])
def cust_empLogin():
    return check_cust_login(request.form)

@app.route('/managerLogin', methods=["GET"])
def login_page():
    return get_managerLogin_page()


@app.route('/managerLogin/input', methods=["POST"])
def cust_managerLogin():
    return check_cust_login(request.form)

if __name__ == "__main__":
    app.run(debug=True)