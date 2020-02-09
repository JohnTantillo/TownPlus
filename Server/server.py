import bottle
import requests
import pymongo
import datetime
from datetime import date
from pymongo import MongoClient
import json


lot = []


@bottle.route("/")
def home():
    return bottle.static_file("htmlFiles\\home.html", root="C:\\Users\\J_Dun\\Documents\\GitHub\\TownPlus")


@bottle.post("/sensorData")
def sensor():
    print("adding new server data")
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S")
    client = pymongo.MongoClient("mongodb+srv://johnduna:100741Vcs@distances-mh9hl.mongodb.net/test?retryWrites=true&w=majority")
    db = client.Distances
    posts = db.dist
    dist = bottle.request.forms.get('dist')
    posts.insert_one({"dist":float(dist)})


@bottle.route("/scala")
def toScala():
    print("scala pulled")
    client = pymongo.MongoClient("mongodb+srv://johnduna:100741Vcs@distances-mh9hl.mongodb.net/test?retryWrites=true&w=majority")
    db = client.Distances
    posts = db.dist
    data = posts.find().sort({_id:-1})
    if float(data[0]) <= 100:
        lot.append([1])
    else:
        lot.append([0])
    for i in lot:
        print(i)
    return json.dumps(lot)
        #return json.dumps(True)
    #else:
        #return json.dumps(False)


bottle.run(host="0.0.0.0",port="80",debug=True)
