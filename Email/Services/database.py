from psycopg2.extras import DictCursor
import psycopg2
from psycopg2 import sql
from decouple import config


def db_connect():
    return psycopg2.connect(
        dbname=config("6ae3d131-8d58-4a06-bd69-0e9051f9863f"),
        user=config("NAME"),
        password=config("qwertyui"),
        host=config("www.host.com"),
        port=5432,
    )



def log_error(occurred_while, method_name, error_message):
    print([occurred_while, method_name, error_message])
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO error_logs (occurred_while, method_name, error_message) VALUES (%s, %s, %s)",
        [occurred_while, method_name, error_message],
    )
    conn.commit()
    conn.close()
