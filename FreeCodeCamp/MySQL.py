# importing libraries
import mysql.connector
from mysql.connector import Error


# connecting to MySQL server
def create_server_connection(host_name, user_name, user_password, db_user):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = db_user
        )
        print('MySQL Database connection succeeded')
    except Error:
        print(f"Error: '{err}'")

    return connection

pw = 'MySQL4python' # MySQL database password
connection = create_server_connection('localhost', 'root', pw, 'asiefrahman')

# Creating new database
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print('Database created successfully')
    except Error as err:
        print(f"Error: '{err}'")

# Define a query to create a database & call the function
create_database_query = "CREATE DATABASE school"
create_database(connection, create_database_query)

'''# Connecting to the Database
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = (
            host =host_name,
            user = user_name,
            password = user_password,
            database = db_user
        )
        print('MySQL Database connection successful')
    except Error as err:
        print(f"Error: '{err}'")
    return connection'''

