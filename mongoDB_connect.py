from pymongo import MongoClient
import json

with open('assets/secret.json') as f:
    config = json.load(f)

db_address = config.get('mongoDB_address')
db_user = config.get('mongoDB_user')
password = config.get('mongoDB_pass')

#con_string = f'mongodb+srv://{db_user}:{password}@{db_address}' #Replace password in string
con_string = db_address.replace('<password>', password)
print(con_string)
#client = MongoClient(con_string)

'''for db_name in client.list_database_names():
    print(db_name)

    mydb = client[db_name]
    for coll in mydb.list_collection_names():
        print(coll)
        for doc in coll.find({}):
            print(doc)'''


