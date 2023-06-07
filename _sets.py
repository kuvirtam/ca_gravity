from _defs import *

# отрисовка
GUI = {
	"title": "gravity",
	"pix": 8,
	"fps": 30,
	"grav_color": [(0,0,0),(0,255,255),(255,0,0)],
	"cell_color": (255, 255, 255),
	"mode": "auto"
}

# параметры автомата
SD = {
	"size": [64, 64],
	"g": getRange(10, 0, 1),
	"mode": "cross",
	"percent": 0.5,
}

# ---------- init
def init():
	petri = makeBox(SD["size"], 0)
	petri = addDots(petri, SD["percent"], 1)
	grav = calcG(petri, SD["g"], SD["mode"])
	return petri, grav

# ---------- loop
def nextGen(petri, grav):
	petri = move2G(petri, grav, SD["mode"])
	grav = calcG(petri, SD["g"], SD["mode"])
	return petri, grav