from getpass import getpass
from mysql.connector import connect, Error
import json



class Mysql:
    def __init__(self):

        try:
            with connect(
                #host="localhost",
                host=secret.get('aws_sql_address'),
                user=input("Enter username: "),
                #password=getpass("Enter password: "),
                password='Aa1234',
                database='test' # If data base exists
            ) as connection:
                print('Connection with database was established')

                # Create DB

                db = connection.cursor()
                db.execute('show databases')
                lst = db.fetchall()
                print(len(lst))
                if dbname in lst:
                
                    print('Database already exists!!!')
                else:
                    create_db_query = 'CREATE DATABASE test'
                    with connection.cursor() as cursor:
                        cursor.execute(create_db_query)
                        print('Database was created')

                # Create Licenses Table
                create_licenses_table = '''
                            '''CREATE TABLE IF NOT EXISTS licenses(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            product_name VARCHAR(100),
                            issuer VARCHAR(100),
                            license_id VARCHAR(100),
                            purchase_date DATE,
                            start_date DATE,
                            end_date DATE,
                            invoice VARCHAR(50),
                            quantity INT(10),
                            authorization_id VARCHAR(100),
                            agreement_id VARCHAR(100)
                            )
                            '''
                with connection.cursor() as cursor:
                    cursor.execute(create_licenses_table)
                    connection.commit()
                    print('Table was created')



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

    mysql = Mysql()

