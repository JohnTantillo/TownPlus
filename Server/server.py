import bottle
import requests
import pymongo
from pymongo import MongoClient
import json
import sqlite3
import time


@bottle.route("/")
def home():
    return bottle.static_file("home.html", root="/root/projects/TownPlus/FrontEnd")

@bottle.route("/home.html")
def home():
    return bottle.static_file("home.html", root="/root/projects/TownPlus/FrontEnd")

@bottle.route("/parking.js")
def parkingjs():
    return bottle.static_file("parking.js", root="/root/projects/TownPlus/FrontEnd")

@bottle.route("/parking.css")
def parkingcss():
    return bottle.static_file("parking.css", root="/root/projects/TownPlus/FrontEnd")

@bottle.route("/logo.png")
def logo():
    return bottle.static_file("logo.png", root="/root/projects/TownPlus/FrontEnd")

@bottle.route("/empty.png")
def empty():
    return bottle.static_file("empty.png", root="/root/projects/TownPlus/FrontEnd")

@bottle.route("/map.css")
def parkingcss():
    return bottle.static_file("map.css", root="/root/projects/TownPlus/FrontEnd")

@bottle.route("/homeStyle.css")
def parkingcss():
    return bottle.static_file("homeStyle.css", root="/root/projects/TownPlus/FrontEnd")

@bottle.route("/map.html")
def parkingcss():
    return bottle.static_file("map.html", root="/root/projects/TownPlus/FrontEnd")

@bottle.route("/maps.png")
def parkingcss():
    return bottle.static_file("maps.png", root="/root/projects/TownPlus/FrontEnd")

@bottle.route("/park.png")
def parkingcss():
    return bottle.static_file("park.png", root="/root/projects/TownPlus/FrontEnd")

@bottle.route("/parking.html")
def parkingcss():
    return bottle.static_file("parking.html", root="/root/projects/TownPlus/FrontEnd")

@bottle.route("/car.jpg")
def parkingcss():
    return bottle.static_file("car.jpg", root="/root/projects/TownPlus/FrontEnd")

#################################################################################################################
@bottle.route("/parking.css")
def parkingcss():
    return bottle.static_file("parking.css", root="C:\\Users\\J_Dun\\Documents\\GitHub\\TownPlus\\FrontEnd")

@bottle.post("/sensorData")
def sensor():
    client = pymongo.MongoClient("mongodb+srv://dbUser:100741Vcs@cluster0-cxegb.mongodb.net/test?retryWrites=true&w=majority")
    db = client.Distances
    posts = db.dist
    dist = bottle.request.forms.get('dist')
    posts.insert_one({"dist":float(dist), "time": time.time()})
    client.close()


@bottle.route("/scala")
def toScala():
    client = pymongo.MongoClient("mongodb+srv://dbUser:100741Vcs@cluster0-cxegb.mongodb.net/test?retryWrites=true&w=majority")
    db = client.Distances
    posts = db.dist
    data = posts.find().sort([("time",-1)]).limit(1)
    print(data[0]["dist"])
    if float(data[0]["dist"]) != -1:
        return json.dumps(True)
    else:
        return json.dumps(False)

    client.close()

@bottle.post("/fuckingPlease")
def fromScala():
    print("from scala")
    lotJson = bottle.request.forms.get('data')
    lot = json.loads(lotJson)
    client = pymongo.MongoClient("mongodb+srv://dbUser:100741Vcs@cluster0-cxegb.mongodb.net/test?retryWrites=true&w=majority")
    db = client.ForFrontend
    posts = db.maps
    posts.insert_one({"maps":lot})
    client.close()


bottle.run(host="0.0.0.0",port="80",debug=True)
