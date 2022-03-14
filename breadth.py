#add a visited list to avoid cycles
#complete the level

""" graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
} """
"""
graph = {'m': ['a', 'b', 'd', 'e'],
         'a': ['b', 'r'],
         'b': ['a', 'c', 'd', 'e'],
         'c': ['d', 'e'],
         'd': ['e', 'r'],
         'e': ['r'],
         'r': []}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    # function calling """

# graph is in adjacent list representation
"""graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '3': [],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '6': [],
        '7': ['11', '12'],
        '8': [],
        '9': [],
        '10': [],
        '11': [],
        '12': []
        }"""

graph = {'m': ['a', 'b', 'd', 'e'],
         'a': ['b', 'r'],
         'b': ['a', 'c', 'd', 'e'],
         'c': ['d', 'e'],
         'd': ['e', 'r'],
         'e': ['r'],
         'r': []}

def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []

    final_path = []
    l=0
    nextl = 0
    # push the first path into the queue
    queue.append([start])
    #print(start)
    #print("\n")
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path






        #print(graph.get(node, []), end = " ")
        #nextl+=len(graph.get(node, []))
        #if not l:
            #l = nextl - 1
            #nextl=0
            #print("\n")
        #else:
            #l -= 1

        
        # enumerate all adjacent nodes, construct a 
        # new path and push it into the queue
        for adjacent in graph.get(node, []):
            print(adjacent)
            new_path = list(path)
            new_path.append(adjacent)
            print(new_path)
            queue.append(new_path)
            print(queue)
            if adjacent == end:
                final_path = new_path
        
        """if final_path:
            print("\n")
            return final_path"""

print (bfs(graph, 'm', 'r'))