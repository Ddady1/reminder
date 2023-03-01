from getpass import getpass
from mysql.connector import connect, Error
import json
import pymysql




class Mysql:
    def __init__(self):

        try:

            with connect(
                    host=config.get('aws_sql_address'),
                    user=config.get('db_username'),
                    # password=getpass("Enter password: "),
                    password=config.get('db_pass'),
                    # database=config.get('db_name')
            ) as connection:
                print('Connection with MySQL server was established')



        except Error as e:
                print(e)


    '''def menu(self, key):

        if key == 'sd':
            show_db(self)
        elif key == 'st':
            show_table(self)


    def show_db(self):
        # Show DB
        show_db_query = "SHOW DATABASES"
        with connection.cursor() as cursor:
            cursor.execute(show_db_query)
            for db in cursor:
                print(db)





        # Show Table

        ''show_table_query = 'DESCRIBE licenses'
        with connection.cursor() as cursor:
            cursor.execute(show_table_query)
            result = cursor.fetchall()
            for row in result:
                print(row)'''
            





if __name__ == '__main__':

    with open('secret.json', 'r') as f:
        config = json.load(f)

    mysql = Mysql()

