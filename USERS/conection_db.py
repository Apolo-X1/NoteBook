import mysql.connector

def conection():
    database = mysql.connector.connect(

        host = "localhost",
        user = "root",
        passwd = "",
        database = "first_app_notebook",
        port = 3306
    )

    cursor = database.cursor(buffered = True)

    return[database, cursor]
