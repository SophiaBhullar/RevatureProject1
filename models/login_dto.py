class Login:
    def __init__(self, emp_id, emp_name, emp_pass, designation, emp_firstname, emp_lastname, emp_email, emp_contact):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_pass = emp_pass
        self.designation = designation
        self.emp_firstname = emp_firstname
        self.emp_lastname = emp_lastname
        self.emp_email = emp_email
        self.emp_contact = emp_contact


    def __repr__(self) -> str:
        return f"User Login: id - {self.emp_id} emp_name - {self.emp_name} emp_pass - {self.emp_pass} designation -{self.designation} emp_firstname - {self.emp_firstname} emp_lastname - {self.emp_lastname} emp_email - {self.emp_email} emp_contact - {self.emp_contact}"
