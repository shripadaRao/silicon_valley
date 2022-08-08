from flask import Flask

app = Flask(__name__)

import main

@app.route('/quotes/<character_name>')
def findCharacterName1(character_name):
    myquery = {"character_name":character_name}
    DataList = []
    for x in col.find(myquery):     
        DataList.append(x)
    if not DataList:
        return("Wrong Charater")
    return(DataList)