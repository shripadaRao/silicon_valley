"""THIS FILE GETS DATA FROM data_transformation.py & PUSHES RECORDS INTO MONGODB"""

import data_transform
from pymongo import MongoClient

with open('env.txt','r') as f:
    MONGO_URI = f.read()

client = MongoClient(MONGO_URI)
db = client["SiliconValley"]
col = db["QuotesFinal"]

DataModel = {"_id":1, "character_name":"", "quote":""}         

def make_record(i):
    DataModel["_id"] = i
    DataModel["character_name"] = data_transform.character_name_list[i]
    DataModel["quote"] = data_transform.quotes_list[i]
    i+=1
    return DataModel

def push_record(data):
    col.insert_one(data)

def main():
    for i in range(len(data_transform.character_name_list)):
        make_record(i)
        push_record(DataModel)
        print("Pushing record!!")
    print("Done")

main()