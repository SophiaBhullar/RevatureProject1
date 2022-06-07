class Request:
    def __init__(self, req_id:int, emp_id:int, description:str, amount:float, status:str, comments:str):
        self.req_id = req_id
        self.emp_id = emp_id
        self.description = description
        self.amount = amount
        self.status = status
        self.comments = comments


    def __repr__(self) -> str:
        return f"Request Details: {self.req_id} + {self.emp_id} + {self.description} + {self.amount} + {self.status} + {self.comments}"
