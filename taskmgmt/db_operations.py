import pymongo
import os
import polyhouse.settings as settings

class database:
    app_client = None
    db_conn = None
    collection = None
    
    def __init__(self) -> None:
        db = settings.DATABASES['default']
        db_name = db['NAME']
        host = db['HOST']
        coll_name = db['COLLECTION']

        self.app_client = pymongo.MongoClient(host)
        self.db_conn = self.app_client[db_name]
        self.collection = self.db_conn[coll_name]

    def create_task(self, name, age):
        myquery = { "address": "Valley 345" }
        newvalues = { "$set": { "address": "Canyon 123" } }
        data = {"name": name, "age": age}

        self.collection.insert_one(data)

        #print "customers" after the update:
        for x in self.collection.find():
            print(x)