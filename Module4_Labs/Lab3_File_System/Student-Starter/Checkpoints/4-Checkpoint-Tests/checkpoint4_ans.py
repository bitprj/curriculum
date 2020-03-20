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
	G2.print_ordered_file_structure("0")
	


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

	def print_ordered_file_structure(self, start):
	 visited = defaultdict(bool)
	 stack = []
	 stack.append(start)
	 visited[start] = True
	 while stack:
	  start = stack.pop()
	  f = open("output.txt", "a")
	  f.write(start+'. ' +   self.val_map[start] + '\n')
	  f.close()
	  lst = self.edges[start]
	  lst.sort()
	  lst = lst[::-1]
	  for j in lst:
	    if visited[j] == False: 
	      stack.append(j)
	      visited[j] = True		

main()							
