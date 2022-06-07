

import psycopg2
from models.login_dto import Login
from repository.connection import get_connection


def insert_request_info(emp_id:int, description:str, amount:float, status:str, comments:str):
    connection = get_connection()
    cursor = connection.cursor()
    
    #create a user
    qry = "INSERT INTO requests VALUES (default, %s , %s, %s, %s, %s) RETURNING req_id;"

    try:
        cursor.execute(qry, (emp_id, description, amount, status, comments))
        id = cursor.fetchone()[0]
        connection.commit()
        return id

    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()

    finally:
        if connection is not None:
            connection.close()