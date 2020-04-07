
"""
Test Case1: check function fileReader
def main():
    graph = fileReader("case1.csv")
    print("Graph:",graph)
if __name__ == "__main__":
    main()
"""
"""
Test Case 1 - Results
Graph: [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]
"""



"""
Test Case2: check the Vertices of the graph and function initColors
n = 2
def main():
    graph = fileReader("case1.csv")
    print("Graph:",graph) # check function fileReader
    numVertices = len(graph)
    print("Number of vertices: ",numVertices)
    n = int(input("Enter n: "))
    colors = initColors(numVertices)  
    print("Initial colors: ", colors) 
if __name__ == "__main__":
    main()
"""
"""
Test Case 2 - Results
Graph: [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]
Number of vertices:  4
Enter n: 2
Initial colors:  [0, 0, 0, 0] 
"""



"""
Test Case 3: check color not enough condition
n = 0
def main():
    graph = fileReader("case1.csv")
    print("Graph:",graph) # check function fileReader
    numVertices = len(graph)
    print("Number of vertices: ",numVertices) # check the Vertices of the graph
    n = int(input("Enter n: "))
    colors = initColors(numVertices)   # initalizes colors to all 0s
    print("Initial colors: ", colors) # check function initColors
    if graphColoring(graph, n, colors, 0, numVertices) == False:
        print("Graph cannot be colored")
if __name__ == "__main__":
    main()
“”“
”“”
Test Case 3 - Results
Graph: [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]
Number of vertices:  4
Enter n: 0
Initial colors:  [0, 0, 0, 0] 
Graph cannot be colored
“”“


”“”
Test Case 4: checkVertex and graphColoring function
n = 1
def main():
    graph = fileReader("case1.csv")
    print("Graph:",graph) # check function fileReader
    numVertices = len(graph)
    print("Number of vertices: ",numVertices) # check the Vertices of the graph
    n = int(input("Enter n: "))
    colors = initColors(numVertices)   # initalizes colors to all 0s
    print("Initial colors: ", colors,"\n") # check function initColors
    if graphColoring(graph, n, colors, 0, numVertices) == False:
        print("Graph cannot be colored")
if __name__ == "__main__":
    main()
“”“
”“”
Test Case 4 - Results
Graph: [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]
Number of vertices:  4
Enter n: 1
Initial colors:  [0, 0, 0, 0] 

vertex 0 can have color 1
vertex 0 can have color 1
vertex 0 can have color 1
vertex 0 can have color 1
Assign color 1  to vertex 0 

vertex 1 can't have color 1
Graph cannot be colored
“”“

”“”
Test Case 5:
Enter n: 2 # return the same result for n>=2
def main():
    graph = fileReader("case1.csv")
    print("Graph:",graph) # check function fileReader
    numVertices = len(graph)
    print("Number of vertices: ",numVertices) # check the Vertices of the graph
    n = int(input("Enter n: "))
    colors = initColors(numVertices)   # initalizes colors to all 0s
    print("Initial colors: ", colors,"\n") # check function initColors
    if graphColoring(graph, n, colors, 0, numVertices) == False:
        print("Graph cannot be colored")
    else:
        print("The color assignments are: ")
        for color in colors:
            print(color)


if __name__ == "__main__":
    main()
"""

"""
Test Case 5 - Results
Graph: [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]
Number of vertices:  4
Enter n: 2 # return the same result for n>=2
Initial colors:  [0, 0, 0, 0] 

vertex 0 can have color 1
vertex 0 can have color 1
vertex 0 can have color 1
vertex 0 can have color 1
Assign color 1  to vertex 0 

vertex 1 can't have color 1
vertex 1 can have color 2
vertex 1 can have color 2
vertex 1 can have color 2
vertex 1 can have color 2
Assign color 2  to vertex 1 

vertex 2 can't have color 1
vertex 2 can have color 2
vertex 2 can have color 2
vertex 2 can have color 2
vertex 2 can have color 2
Assign color 2  to vertex 2 

vertex 3 can have color 1
vertex 3 can have color 1
vertex 3 can have color 1
vertex 3 can have color 1
Assign color 1  to vertex 3 

The color assignments are: 
1
2
2
1
"""
