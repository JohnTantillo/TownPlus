import bottle
import requests

nonMagicNumber = 100
scalaServer = "/parkingSpot"

@bottle.route("/")
def home():
    return bottle.static_file("htmlFiles\\home.html", root="C:\\Users\\J_Dun\\Documents\\GitHub\\TownPlus")

@bottle.post("/sensorData")
def sensor():
    dist = request.forms.get('dist')
    if dist != "Out Of Range":
        if float(dist) <= nonMagicNumber:
            r = requests.post(scalaServer, data = {'distance':float(dist)})

bottle.run(host="0.0.0.0",port="8080",debug=True)
