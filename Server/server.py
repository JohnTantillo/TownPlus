import bottle

@bottle.route("/")
def home():
    return bottle.static_file("C:\Users\J_Dun\Documents\GitHub\TownPlus\htmlFiles\home.html", root="C:\\Users\\J_Dun\\Documents\\GitHub\\TownPlus")
