
from urllib.request import Request
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



def select_requests(emp_id):
        connection = get_connection()
        cursor = connection.cursor()

        #select requests from database

        qry = f"SELECT * FROM requests WHERE emp_id ='{emp_id}';"

        try:
            cursor.execute(qry)
        
            while True:
                record = cursor.fetchall()
                if record is None:
                    break
                print(record)
                return record


        except(psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if connection is not None:
                connection.close()



def select_all_requests():
        connection = get_connection()
        cursor = connection.cursor()

        #select all requests from database

        qry = f"SELECT * FROM requests;"

        try:
            cursor.execute(qry)
        
            while True:
                record = cursor.fetchall()
                if record is None:
                    break
                print(record)
                return record


        except(psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if connection is not None:
                connection.close()


def delete_requests(req_id):
        connection = get_connection()
        cursor = connection.cursor()

        #delete requests from database

        qry = f"DELETE FROM requests WHERE req_id ='{req_id}';"

        try:
            cursor.execute(qry)

            while True:
                # record = cursor.fetchone()
                connection.commit()
                record=cursor.rowcount
                if record is None:
                    break
                print(record)
                return record


        except(psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if connection is not None:
                connection.close()


def update_requests(req_id,status,comments):
        connection = get_connection()
        cursor = connection.cursor()

        #update requests from database

        qry = f"UPDATE requests SET status = '{status}', comments = '{comments}' WHERE req_id ='{req_id}';"

        try:
            cursor.execute(qry)

            while True:
                # record = cursor.fetchone()
                connection.commit()
                record=cursor.rowcount
                if record is None:
                    break
                print(record)
                return record


        except(psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if connection is not None:
                connection.close()