import sys
from collections import defaultdict

def main():
	edges = []
	val_map = {}
	readFile(edges, val_map)
	G2 = Graph()
	G2.add_val_map(val_map)
	for edge in edges:
		G2.add_edge(*edge)
	G2.add_val_map(val_map)
	

	print("Edges:")
	for edge in sorted(edges):
		print(edge)
	print("Values:")	
	for number in sorted(val_map):
		print(number, val_map[number])	




def readFile(edges, val_map):
	readFile = open(sys.argv[1], "r")
	for line in readFile:
		dirAndVal = line.split(".")
		dirAndVal[1] = dirAndVal[1].strip()
		if (dirAndVal[0] != "0"):
			aTuple = (dirAndVal[0][:-1], dirAndVal[0])
			edges.append(aTuple)
		val_map[dirAndVal[0]] = dirAndVal[1]
	
class Graph:
	def __init__(self):
		self.edges = defaultdict(list)
		self.val_map = {}

	def add_edge(self, from_node, to_node):
		self.edges[from_node].append(to_node)

	def add_val_map(self, val_map):
		self.val_map = val_map

main()							
