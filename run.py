import pygame as pg; pg.init()

from _defs import *
from _sets import *

# выводит данные на консоль
def conswrite(petri, grav, scrmode, fps):
	cls()
	print("")
	print("/// {} \\\\\\".format(GUI["title"]))
	print("")
	print("--- GUI")
	print("size | {}x{}".format(GUI["pix"]*SD["size"][0], GUI["pix"]*SD["size"][1]))
	print(" pix | {}".format(GUI["pix"]))
	print(" fps | {}".format(fps))
	print("mode | {}".format(scrmode))
	print("")
	print("--- INFO")
	print("size | {}x{}".format(SD["size"][0], SD["size"][1]))
	print("mode | {}".format(SD["mode"]))
	print("difs | {} -> {}".format(getMin(grav), getMax(grav)))
	print("cell | {} /{} (~{})".format(
		getNum(petri),
		SD["size"][0]*SD["size"][1],
		SD["percent"]
		))
	print("   g | {}".format(SD["g"]))
	print("")
	print("")
	print("")
	print("controls")
	print("    [0] | show/hide elements")
	print("    [1] | turn mode \"click\"")
	print("    [2] | turn mode \"auto\"")
	print(" [LEFT] | refresh automata")
	print("[RIGHT] | next step (if mode==\"click\")")
	print("   [UP] | fps += 10")
	print(" [DOWN] | fps -= 10")

def drawScreen(petri, grav, drawDots):
	i = 0
	while i < len(petri):
		ii = 0
		while ii < len(petri[i]):
			color = getColor(grav[i][ii], [getMin(grav), getMax(grav)], GUI["grav_color"])
			xy1 = [GUI["pix"]*i, GUI["pix"]*ii, GUI["pix"], GUI["pix"]]
			pg.draw.rect(screen, color, xy1)
			if drawDots == True and petri[i][ii] == 1:
				border = int(GUI["pix"]*0.4)
				xy2 = [GUI["pix"]*i+border, GUI["pix"]*ii+border, GUI["pix"]-(border*2), GUI["pix"]-(border*2)]
				pg.draw.rect(screen, GUI["cell_color"], xy2)
			ii += 1
		i += 1

screen_size = (GUI["pix"]*SD["size"][0], GUI["pix"]*SD["size"][1])
screen = pg.display.set_mode(screen_size)
pg.display.set_caption(GUI["title"])
clock = pg.time.Clock()

# init
petri, grav = init()
scrmode = GUI["mode"]
fps = GUI["fps"]
drawDots = True

running = True
while running:
	clock.tick(fps)
	
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
		elif event.type == pg.KEYDOWN:
			if event.key == pg.K_0:
				drawDots = True if drawDots == False else False
			if event.key == pg.K_1:
				scrmode = "click"
			if event.key == pg.K_2:
				scrmode = "auto"
			if event.key == pg.K_UP:
				fps += 10
			if event.key == pg.K_DOWN:
				fps -= 10
			if event.key == pg.K_LEFT:
				petri, grav = init()
			if event.key == pg.K_RIGHT:
				if scrmode == "click": petri, grav = nextGen(petri, grav)

	if scrmode == "auto": petri, grav = nextGen(petri, grav)

	conswrite(petri, grav, scrmode, fps)
	drawScreen(petri, grav, drawDots)

	# screen.fill((0,0,0))
	pg.display.flip()