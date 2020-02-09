import bottle
import requests
import pymongo
from pymongo import MongoClient
import json
import sqlite3


@bottle.route("/")
def home():
    return bottle.static_file("htmlFiles\\home.html", root="C:\\Users\\J_Dun\\Documents\\GitHub\\TownPlus")


@bottle.post("/sensorData")
def sensor():
    client = pymongo.MongoClient("mongodb+srv://dbUser:100741Vcs@cluster0-cxegb.mongodb.net/test?retryWrites=true&w=majority")
    db = client.Distances
    posts = db.dist
    dist = bottle.request.forms.get('dist')
    posts.insert_one({"dist":float(dist)})
    client.close()


@bottle.route("/scala")
def toScala():
    client = pymongo.MongoClient("mongodb+srv://dbUser:100741Vcs@cluster0-cxegb.mongodb.net/test?retryWrites=true&w=majority")
    db = client.Distances
    posts = db.dist
    data = posts.find_one()
    print(data)
    if float(data["dist"]) <= 100:
        return json.dumps(True)
    else:
        return json.dumps(False)

    client.close()

@bottle.post("/fuckingPlease")
def fromScala():
    print("from scala")
    lotJson = bottle.request.forms.get('lot')
    lot = json.loads(lotJson)
    client = pymongo.MongoClient("mongodb+srv://dbUser:100741Vcs@cluster0-cxegb.mongodb.net/test?retryWrites=true&w=majority")
    db = client.ForFrontend
    posts = db.maps
    posts.insert_one({"maps":lot})
    client.close()


bottle.run(host="0.0.0.0",port="80",debug=True)
