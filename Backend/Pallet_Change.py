import json
from Backend.config import color_reload

file = open("Config.json", "r")
data = json.load(file)
file.close()

pallet = data["palettes"]

def color_change(chosen):
    pallet["current"] = pallet[chosen]

    file = open("Config.json", "w")
    json.dump(data, file, indent=4)
    file.close()
    color_reload()

color_change("default")