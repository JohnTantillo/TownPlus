import bottle

@bottle.route("/")
def home():
    return bottle.static_file("htmlFiles\\home.html", root="C:\\Users\\J_Dun\\Documents\\GitHub\\TownPlus")

@bottle.route("/sensorData")
def sensor():
    

bottle.run(host="0.0.0.0",port="8080",debug=True)
