
from repository.login_dao import select_user_by_designation
from service.validation_service import validate_log



def validate_login(input_dic):
    return validate_log((input_dic["designation"], input_dic["emp_name"],input_dic["emp_pass"]))

def check_login(login_input):
    print(login_input)
    user_dto = select_user_by_designation(login_input.get("designation"), login_input.get("emp_name"), login_input.get("emp_pass"))
    if user_dto is not None:
        return user_dto