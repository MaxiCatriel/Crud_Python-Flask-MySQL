import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='python_flask',
    port='3306')

print(database)