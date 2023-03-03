from getpass import getpass
from mysql.connector import connect, Error
import json
#import pymysql





def connect_sql():
    try:
        with connect(
            host=config.get('aws_sql_address'),
            user=config.get('db_username'),
            # password=getpass("Enter password: "),
            password=config.get('db_pass'),
            #database=config.get('db_name')
            ) as connection:
                print('Connection with MySQL server was established')
                check_db_exists(config.get('db_name'), connection)


    except Error as e:
            print(e)

def create_db(dbname, connection):
    create_db_query = f'CREATE DATABASE {dbname}'
    with connection.cursor() as cursor:
        cursor.execute(create_db_query)
        print('Database was created')

def check_db_exists(dbname, connection):

    db = connection.cursor()
    db.execute('show databases')
    lst = db.fetchall()
    print(lst)
    if dbname in lst:
        print('Database is already exists')
        print(lst)
    else:
        print('Database doesn\'t exists. Creating DB...')
        try:
            create_db(config.get('db_name'), connection)
            print('Database was created successfully')

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

    with open('secret.json') as f:
        config = json.load(f)


    connect_sql()


