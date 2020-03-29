# This file is used to output the edges and values of various graphs based on COMMAND-LINE Input of a file and DFS run on that input.
# Note that this file outputs the answer to an "output.txt" file
# Even though at this point of the lab they will have completed the networkx algorithms, we will not be testing this. This will ONLY test the DFS function (i.e. print_ordered_file_structure)
import sys
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

	# part 3 - DFS Traversal of Graph	
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
        
# part 1 function
def readFile(edges, val_map):
	readFile = open(sys.argv[1], "r")
	for line in readFile:
		dirAndVal = line.split(".")
		dirAndVal[1] = dirAndVal[1].strip()
		if (dirAndVal[0] != "0"):
			aTuple = (dirAndVal[0][:-1], dirAndVal[0])
			edges.append(aTuple)
		val_map[dirAndVal[0]] = dirAndVal[1]

def main():
	# initialize a list for the edges and a dictionary for values
	edges = []
	val_map = {}

	# read the file
	readFile(edges, val_map)

	# create the Graph
	G = Graph()

	# add all the edges
	for edge in edges:
		G.add_edge(*edge)

	# add your val_map	
	G.add_val_map(val_map)

	# part 3 - DFS Traversal of Graph
	G.print_ordered_file_structure("0")

	# part 4 - use networkx
	# G2 will be equivalent to our original graph G, but will be a networkx graph so that we can use the networkx functions
	G2 = nx.Graph()
	G2.add_edges_from(edges)

	# use hierarchy_pos with root = "0"
	pos = hierarchy_pos(G2,"0") 
	
	# networkx functions to draw graph. Notice that for draw_networkx_labels we pass in the val_map as the labels for the nodes
	nx.draw(G2, pos = pos, with_labels = False) 
	nx.draw_networkx_labels(G2, pos, val_map, 8)
	plt.show()
	 

main()
