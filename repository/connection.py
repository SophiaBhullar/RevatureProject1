import psycopg2


# define function for database connection

def get_connection():
        connection = psycopg2.connect(
            database="ERS_database",
            user="postgres",
            password="project1",
            host="ers-database.c9nrebfnqjzt.us-east-2.rds.amazonaws.com",
            port="5432"
    
    )
        return connection