import numpy

class D(object):
	N, S, E, W = 1, 2, 4, 8
	DX = {E: 1, W: -1, N:  0, S: 0}
	DY = {E: 0, W:  0, N: -1, S: 1}
	OPP = {E: W, W: E, N: S, S: N}

class Graph(object):

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.grid = numpy.zeros((height, width), dtype=int)

	def __unicode__(self):
		res = " " + "_" * (self.width * 2 - 1) + "\n"
		for y, row in enumerate(self.grid):
			res += "|"
			for x, cell in enumerate(row):
				if cell == 0 and y+1 < self.height and self.grid[y+1][x] == 0:
					res += " "
				elif cell & D.S != 0:
					res += " "
				else:
					res += "_"

				if cell == 0 and x+1 < self.width and row[x+1] == 0:
					if y+1 < self.height and (self.grid[y+1][x] == 0 or self.grid[y+1][x+1] == 0):
						res += " "
					else:
						res += "_"
				elif cell & D.E != 0:
					if (cell | row[x+1]) & D.S != 0:
						res += " "
					else:
						res += "_"
				else:
					res += "|"
			res += "\n"
		return res

	def __getitem__(self, key):
		if type(key) == int:
			return self.grid[key]
		elif type(key) == tuple:
			y,x = key
			return self.grid[y][x]

	def __setitem__(self, key, val):
		if type(key) == tuple:
			y,x = key
			self.grid[y][x] = val

if __name__ == '__main__':
	g = Graph(15, 5)
	print g.__unicode__()