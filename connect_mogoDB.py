from pymongo import MongoClient

con_string = 'mongodb+srv://myAtlasDBUser:myatlas-001@myatlasclusteredu.vaenw0e.mongodb.net/?retryWrites=true&w=majority' #Replace password in string
client = MongoClient(con_string)

'''for db_name in client.list_database_names():
    print(db_name)

    mydb = client[db_name]
    for coll in mydb.list_collection_names():
        print(coll)
        for doc in coll.find({}):
            print(doc)'''


