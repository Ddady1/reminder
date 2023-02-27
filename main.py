from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        #password=getpass("Enter password: "),
        password='Aa1234',
        database='test' # If data base exists
    ) as connection:
        # Create DB
        '''create_db_query = 'CREATE DATABASE test'
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)'''

        # Show DB
        '''show_db_query = "SHOW DATABASES"
        with connection.cursor() as cursor:
            cursor.execute(show_db_query)
            for db in cursor:
                print(db)'''

        # Create Licenses Table

        create_licenses_table = '''
            CREATE TABLE licenses(
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
        '''with connection.cursor() as cursor:
            cursor.execute(create_licenses_table)
            connection.commit()'''


        # Show Table

        show_table_query = 'DESCRIBE licenses'
        with connection.cursor() as cursor:
            cursor.execute(show_table_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
            


except Error as e:
    print(e)