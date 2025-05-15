import mysql.connector

def create_connection():
    return mysql.connector.connect(

        host="bjq6jnnrgqow5kow7aun-mysql.services.clever-cloud.com",
        user="u7vzjvegga6selmp",
        password="ABG6HjxyKzbqUPEsrict",
        database="bjq6jnnrgqow5kow7aun",
        ssl_disabled=False
    )