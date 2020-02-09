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
    print("adding new server data")
    client = pymongo.MongoClient("mongodb+srv://johnduna:100741Vcs@distances-mh9hl.mongodb.net/test?retryWrites=true&w=majority")
    db = client.Distances
    posts = db.dist
    dist = bottle.request.forms.get('dist')
    posts.insert_one({"dist":float(dist)})
    client.close()


@bottle.route("/scala")
def toScala():
    print("scala pulled")
    client = pymongo.MongoClient("mongodb+srv://johnduna:100741Vcs@distances-mh9hl.mongodb.net/test?retryWrites=true&w=majority")
    db = client.Distances
    posts = db.dist
    data = posts.find().sort("dist",-1)
    print(data)
    if float(data[0]) <= 100:
        return json.dumps(True)
    else:
        return json.dumps(False)

    client.close()


bottle.run(host="0.0.0.0",port="80",debug=True)
