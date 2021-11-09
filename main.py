import psycopg2
from Controller import menu

try:
    connection = psycopg2.connect(
        database="Labs",
        user="postgres",
        password="4214",
        host="127.0.0.1")
    connection.autocommit = True

    menu(connection)

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
