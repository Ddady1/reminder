from getpass import getpass
from mysql.connector import connect, Error
import json
import time
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
                time.sleep(3)
                check_db_exists(config.get('db_name'), connection)


    except Error as e:
            print(e)


def create_db(dbname, connection):
    create_db_query = f'CREATE DATABASE {dbname}'

    try:
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
            print('Database was created successfully!')
    except Error as e:
        print(e)

def check_db_exists(dbname, connection):

    print("Checking Databases...")
    time.sleep(3)
    db = connection.cursor()
    db.execute('show databases')
    lst = db.fetchall()
    i = 0
    while i < len(lst):
        if dbname in lst[i]:
            print('Database is already exists')
            return
        else:
            i += 1

    print('Database doesn\'t exists. Creating DB...')
    create_db(config.get('db_name'), connection)



def manual():
    print('Manual')





    '''def show_db(self):
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

    x = input('Please choose 1 for Auto setup or 2 for Manual setup:')

    while True:
        if x != 1 or x != 2:
            print(type(x))
            x = input('Please choose 1 or 2:')

        elif x == '1':
            print(type(x))
            connect_sql()
            break

        elif x == '2':
            print(type(x))
            manual()
            break



    #connect_sql()


