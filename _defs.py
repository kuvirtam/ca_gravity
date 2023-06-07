import random as r
import os

# очищает экран консоли
def cls(): os.system("cls")

# возвращает цвет исходя из переменных
def getColor(d, dif, colors):
	color = 0
	if d == 0: color = colors[0]
	else:
		if d > 0:
			dt = d/dif[1]
			clrs = [colors[0], colors[1]]
		if d < 0:
			dt = abs(d)/abs(dif[0])
			clrs = [colors[0], colors[-1]]
		color = (
				int(clrs[0][0]+(clrs[1][0]-clrs[0][0])*dt),
				int(clrs[0][1]+(clrs[1][1]-clrs[0][1])*dt),
				int(clrs[0][2]+(clrs[1][2]-clrs[0][2])*dt),
				)
	return color

# возвращает максимальное число из матрицы
def getMax(box):
	lines = []
	for el in box:
		lines.append(max(el))
	return max(lines)

# возвращает максимальное число из матрицы
def getMin(box):
	lines = []
	for el in box:
		lines.append(min(el))
	return min(lines)

# возвращает количество элементов в матрице
def getNum(box):
	i = 0
	for line in box:
		for el in line:
			if el == 1: i += 1
	return i

# возвращает массив чисел по заданным правилам
def getRange(start, end, step):
	line = []
	t = 1 if end > start else -1
	i = start
	while i != end:
		line.append(i)
		i += t*step
	return line

# создает матрицу с заданным элементом
def makeBox(size, el):
	box = []
	i = 0
	while i < size[0]:
		box.append([])
		ii = 0
		while ii < size[1]:
			box[i].append(el)
			ii += 1
		i += 1
	return box

# заполняет матрицу заданным элементом с заданной вероятностью
def addDots(box, percent, el):
	i = 0
	while i < len(box):
		ii = 0
		while ii < len(box[i]):
			if r.random() < percent:
				box[i][ii] = 1
			ii += 1
		i += 1
	return box

# возвращает координаты окружения заданного расстояния
def getXYbyN(n, mode):
	coords = []
	line = range(-n, n+1, 1)

	if mode == "box":
		for i in line:
			if abs(i) == n:
				for ii in line: coords.append([i, ii])
			else:
				coords.append([i, -n])
				coords.append([i, n])

	if mode == "cross":
		for i in line:
			if abs(i) == n:
				coords.append([i, 0])
			else:
				c = n - abs(i)
				coords.append([i, -c])
				coords.append([i, c])

	return coords

# вычисляет поле гравитации из матрицы элементов
def calcG(petri, g, mode):
	size = [len(petri), len(petri[0])]
	grav = makeBox(size, 0)
	ix = 0
	while ix < size[0]:
		iy = 0
		while iy < size[1]:
			# --- !

			if petri[ix][iy] == 1:
				i = 0
				while i < len(g):
					coords = getXYbyN(i, mode)
					for xy in coords:
						try: 
							c = [ix+xy[0], iy+xy[1]]
							if (c[0]>=0) and (c[1]>=0): grav[c[0]][c[1]] += g[i]
						except IndexError:
							pass
					i += 1

			# --- !
			iy += 1
		ix += 1
	return grav

# передвигает элементы в сторону наибольшей гравитации
def move2G(petri, grav, mode):
	i = 0
	while i < len(petri):
		ii = 0
		while ii < len(petri[i]):
			# ---------- !

			if petri[i][ii] == 1:
				coords = getXYbyN(1, mode)
				coords.append([0,0])
				gs = []
				for xy in coords:
					try:
						gs.append(grav[i+xy[0]][ii+xy[1]])
					except IndexError:
						pass
				to = coords[gs.index(max(gs))]
				try:
					if petri[i+to[0]][ii+to[1]] == 0:
						petri[i][ii] = 0
						petri[i+to[0]][ii+to[1]] = 1
				except IndexError:
					pass

			# ---------- !
			ii += 1
		i += 1
	return petri