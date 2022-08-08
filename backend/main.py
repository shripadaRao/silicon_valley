from http import client
from flask import Flask
from flask_pymongo import pymongo
from flask import jsonify

app = Flask(__name__)

conn = "mongodb+srv://shripad_rao:MfAPwUqXG9IpHXJa@cluster0.cqtw61h.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(conn)
db = client["SiliconValley"]
col = db['Quotes']


@app.route('/')
def flask_mongo_db():
    return("hello, this is homepage")

@app.route('/quotes/<character_name>')
def findCharacterName1(character_name):
    myquery = {"character_name":character_name}
    DataList = []
    for x in col.find(myquery):     
        DataList.append(x)
    if not DataList:
        return("Wrong Charater")
    return(DataList)

@app.route('/quotes/all')
def findAll():
    DataList = []
    for x in col.find({}):
        DataList.append(x)
    return(DataList)
    
if __name__ == '__main__':
    app.run(port=8000)