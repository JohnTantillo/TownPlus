import bottle
import requests
from pymongo import MongoClient


@bottle.route("/")
def home():
    return bottle.static_file("htmlFiles\\home.html", root="C:\\Users\\J_Dun\\Documents\\GitHub\\TownPlus")

@bottle.post("/sensorData")
def sensor():
    print("adding new server data")
    client = pymongo.MongoClient("mongodb+srv://johnduna:<password>@distances-mh9hl.mongodb.net/test?retryWrites=true&w=majority")
    db = client.Distances.dist
    posts = db.posts
    dist = bottle.request.forms.get('dist')
    posts.insert_one({"dist":float(dist)})


@bottle.route("/scala")
def toScala():
    print("scala pulled")
    return curDist[len(curDist)]

bottle.run(host="0.0.0.0",port="8080",debug=True)
