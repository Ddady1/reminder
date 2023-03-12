from mysql.connector import connect, Error
import json


def connect_sql():

    with open('assets/secret.json') as f:
        config = json.load(f)

    try:
        with connect(
                host=config.get('sql_address'),
                user=config.get('db_username'),
                # password=getpass("Enter password: "),
                password=config.get('db_pass'),
                database=config.get('db_dbName')
        ) as connection:
            print('Connection with MySQL server was established')
            #time.sleep(3)
            #check_db_exists(config.get('db_name'), connection)

    except Error as e:
            print(e)