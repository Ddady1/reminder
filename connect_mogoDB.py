from pymongo import MongoClient

con_string = 'mongodb+srv://myAtlasDBUser:<password>@myatlasclusteredu.vaenw0e.mongodb.net/?retryWrites=true&w=majority' #Replace password in string
client = MongoClient(con_string)

for db_name in client.list_database_names():
    print(db_name)

