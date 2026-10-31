import mysql.connector
from fastapi import FastAPI

def connect():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "employee_db"
    )

