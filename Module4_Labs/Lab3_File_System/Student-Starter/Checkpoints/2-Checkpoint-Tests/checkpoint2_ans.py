import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

# part 2 - create your own graph object
class Graph:
	def __init__(self):
		self.edges = defaultdict(list)
		self.val_map = {}

	def add_edge(self, from_node, to_node):
		self.edges[from_node].append(to_node)

	def add_val_map(self, val_map):
		self.val_map = val_map

            

#provided method
#will help in displaying with networkx
#Param: G = networkx graph
#Param: root = "top" of the data structure
def hierarchy_pos(G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):
    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.
    Licensed under Creative Commons Attribution-Share Alike
    If the graph is a tree this will return the positions to plot this in a
    hierarchical layout.
    G: the graph (must be a tree)
    root: the root node of current branch
    - if the tree is directed and this is not given,
      the root will be found and used
    - if the tree is directed and this is given, then
      the positions will be just for the descendants of this node.
    - if the tree is undirected and not given,
      then a random choice will be used.
    width: horizontal space allocated for this branch - avoids overlap with other branches
    vert_gap: gap between levels of hierarchy
    vert_loc: vertical location of root
    xcenter: horizontal location of root
    '''
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')
    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  #allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))
    def _hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
        '''
        see hierarchy_pos docstring for most arguments
        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed
        '''
        if pos is None:
            pos = {root:(xcenter,vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children)!=0:
            dx = width/len(children)
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G,child, width = dx, vert_gap = vert_gap,
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
        return pos
    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)
        
def main():
	# initialize a list for the edges and a dictionary for values
	edges = []
	val_map = {}

	# read the file
	readFile(edges, val_map)

	# create the Graph
	G2 = Graph()

	# add all the edges
	for edge in edges:
		G2.add_edge(*edge)

	# add your val_map	
	G2.add_val_map(val_map)

	# for testing
	print("Edges:")
	for edge in sorted(edges):
		print(edge)
	print("Values:")	
	for number in sorted(val_map):
		print(number, val_map[number])	

	#TODO for part 3
	#display the graph using networkx and matplotlib
	#HINT: the activity on directed graphs
	#may be helpful ;)
	#note: you don't have to do this in the
	#main method

	#TODO for part 4
	#print the file structure in order
	#beware that the input file may not
	#be in numerical order.
	#reminder: the format is ###.some name
	#hint: use DFS
	#note: you don't have to do this in the
	#main method


# part 1 function
def readFile(edges, val_map):
	readFile = open("input.txt", "r")
	for line in readFile:
		dirAndVal = line.split(".")
		dirAndVal[1] = dirAndVal[1].strip()
		if (dirAndVal[0] != "0"):
			aTuple = (dirAndVal[0][:-1], dirAndVal[0])
			edges.append(aTuple)
		val_map[dirAndVal[0]] = dirAndVal[1]  

main()
