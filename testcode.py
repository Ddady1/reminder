'''with connect(
                #host="localhost",
                host=config.get('aws_sql_address'),
                #user=input("Enter username: "),
                user=config.get('db_username'),
                #password=getpass("Enter password: "),
                #password='Aa1234',
                password=config.get('db_pass'),
                #database='test' # If data base exists
                #database=config.get('db_name')
            ) as connection:
                #print('Connection with database was established')
                print(connection)

                # Create DB

                db = connection.cursor()
                db.execute('show databases')
                lst = db.fetchall()
                print(len(lst)
                if dbname in lst:

                    print('Database already exists!!!')
                else:
                    create_db_query = 'CREATE DATABASE test'
                    with connection.cursor() as cursor:
                        cursor.execute(create_db_query)
                        print('Database was created')

                # Create Licenses Table
                create_licenses_table =
                            CREATE TABLE IF NOT EXISTS licenses(
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

                with connection.cursor() as cursor:
                    cursor.execute(create_licenses_table)
                    connection.commit()
                    print('Table was created')

____________________________________
Another way to connect with pymysql:
------------------------------------

        db = pymysql.connect(
                host=config.get('aws_sql_address'),
                user=config.get('db_username'),
                password=config.get('db_pass')
            )
            cursor = db.cursor()
            print(cursor)'''



import json

# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("assets/test.json", "w") as outfile:
    outfile.write(json_object)