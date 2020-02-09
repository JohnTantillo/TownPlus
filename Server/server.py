import bottle
import requests
import pymongo
import datetime
from datetime import date
from pymongo import MongoClient


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
    posts.insert_one({"dist":float(dist), "id":dt_string})


@bottle.route("/scala")
def toScala():
    print("scala pulled")
    return curDist[len(curDist)]

bottle.run(host="0.0.0.0",port="8080",debug=True)
