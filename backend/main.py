from http import client
from flask import Flask
from flask_pymongo import pymongo
from markupsafe import escape
from flask import jsonify

app = Flask(__name__)

def col():
    conn = open("env.txt", 'r').read()
    print(conn)
    client = pymongo.MongoClient(conn)
    db = client["SiliconValley"]
    col = db['QuotesFinal']
    return col

###-------------------------------------------------------------------------------------------###

@app.route('/')
def flask_mongo_db():
    return("hello, this is homepage")

@app.route('/quotes/<character_name>')              #Print all quotes from the given character. 
def findCharacterName(character_name):
    myquery = {"character_name":character_name}
    DataList = []
    contentList = []
    for x in col().find(myquery):     
        DataList.append(x)
        contentList.append(x["quote"])
    if not DataList:
        return("Wrong Character")
    return(jsonify(contentList))

@app.route('/quotes/all')
def findAll():
    DataList = []
    for x in col().find({}):
        DataList.append(x)
    return(jsonify(DataList))

@app.route('/quotes/character-names') #Print all character names
def findCharacterNames():
    c_names = []
    for x in col().find({},{"character_name":1}):
        c_names.append(x["character_name"])
    
    character_names = set(c_names)
    return((list(character_names)))
    
if __name__ == '__main__':
    app.run(port=8000, debug=True)