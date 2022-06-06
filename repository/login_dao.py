import psycopg2
from repository.connection import get_connection
from models.login_dto import Login

#DAO= Data Access Object
# All database interaction to this file
#like inserting queries and all

#create a user login
#read user login


def select_user_by_username(cust_name):
    connection = get_connection()
    cursor = connection.cursor()

    #select user from database

    qry = f"SELECT * FROM cust_login WHERE cust_name = '{cust_name}';"

    try:
        cursor.execute(qry)
        while True:
            record = cursor.fetchone()
            if record is None:
                break
        
            user_login = Login(record[0], record[1], record[2])
            return user_login
    
    except(psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if connection is not None:
            connection.close()


def select_user_by_designation(designation,emp_name,emp_pass):
    connection = get_connection()
    cursor = connection.cursor()

    #select user from database

    qry = f"SELECT * FROM employee WHERE designation = '{designation}' AND emp_name = '{emp_name}' AND emp_pass = '{emp_pass}';"

    try:
        cursor.execute(qry)
        while True:
            record = cursor.fetchone()
            if record is None:
                break
        
            user_login = Login(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7])
            return user_login
    
    except(psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if connection is not None:
            connection.close()





def select_user(emp_name,emp_pass):
    connection = get_connection()
    cursor = connection.cursor()

    #select user from database

    qry = f"SELECT * FROM employee WHERE emp_name = '{emp_name}' AND emp_pass = '{emp_pass}';"

    try:
        cursor.execute(qry)
        while True:
            record = cursor.fetchone()
            if record is None:
                break
        
            user_login = Login(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7])
            return user_login
    
    except(psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if connection is not None:
            connection.close()


def select_user_by_id(cust_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM cust_login where cust_id = {cust_id};"

    try:
        cursor.execute(qry)
        
        while True:
            record = cursor.fetchone()
            if record is None:
                break
            user_login = Login(record[0],record[1], record[2])
            return user_login

    

    except(psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()
