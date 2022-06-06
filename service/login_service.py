
from repository.login_dao import select_user_by_designation

def check_login(login_input):
    print(login_input)
    user_dto = select_user_by_designation(login_input.get("designation"), login_input.get("emp_name"), login_input.get("emp_pass"))
    if user_dto is not None:
        return user_dto