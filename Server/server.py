import bottle
import requests

scalaServer = "/parkingSpot"
curDist = list()

@bottle.route("/")
def home():
    return bottle.static_file("htmlFiles\\home.html", root="C:\\Users\\J_Dun\\Documents\\GitHub\\TownPlus")

@bottle.post("/sensorData")
def sensor():
    dist = request.forms.get('dist')
    curDist = curDist.append(float(dist))

@bottle.route("/scala")
def toScala():
    return curDist[len(curDist)]

bottle.run(host="0.0.0.0",port="8080",debug=True)
