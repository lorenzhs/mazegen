from random import randrange, shuffle
import os
import time

from common import Graph, D

class GrowingTree(object):
	def __init__(self, width, height, strategy):
		self.width = width
		self.height = height
		self.strategy = strategy
		self.graph = Graph(width, height)

	def run(self, verbose=False):
		cells = [(randrange(self.width), randrange(self.height)),]
		while len(cells) > 0:
			if verbose:
				os.system('clear')
				print self.graph.__unicode__()
				time.sleep(0.01)
			index = self.strategy(len(cells))
			x, y = cells[index]
			dirs = [D.N, D.S, D.E, D.W]
			shuffle(dirs)
			for dir in dirs:
				# find neighbour
				nx, ny = x + D.DX[dir], y + D.DY[dir]
				# in bounds and neighbour unvisited?
				if 0 <= nx < self.width and 0 <= ny < self.height and self.graph[ny,nx] == 0:
					self.graph[y,x] |= dir
					self.graph[ny][nx] |= D.OPP[dir]
					index = -1
					cells.append((nx, ny),)
			if index >= 0:
				cells.pop(index)



def random(num):
	return randrange(num)

def newest(num):
	return num - 1

def oldest(num):
	return 0

def middle(num):
	return num // 2

def mix(s1, s2, p1=50):
	def run(num):
		if randrange(100) < p1:
			return s1(num)
		else:
			return s2(num)
	return run

STRATEGIES = {"random": random, "newest": newest, "oldest": oldest, "middle": middle, "ran_new": mix(random, newest, 75)}

if __name__ == '__main__':
	import sys
	if len(sys.argv) > 1:
		width = int(sys.argv[1])
	else:
		width = 15

	if len(sys.argv) > 2:
		height = int(sys.argv[2])
	else:
		height = 10

	if len(sys.argv) > 3:
		strategyname = sys.argv[3]
	else:
		strategyname = "random"

	strategy = STRATEGIES[strategyname]

	verbose = len(sys.argv) > 4

	alg = GrowingTree(width, height, strategy)
	alg.run(verbose)
	if not verbose:
		print alg.graph.__unicode__()