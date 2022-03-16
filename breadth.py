#definition of node class
class node:
    def __init__(self, name, h):
        self.name = name
        self.h = h
        self.adj = []
    
    def addadj(self, adj):
        self.adj = adj

    #implement comparison operators for node
    def __lt__(self, other):
        if self.name < other.name:
            return True
        else:
            return False

    def __le__(self, other):
        if self.name <= other.name:
            return True
        else:
            return False

    #implement print for node
    def __str__(self):
      return self.name

########## graph ##########
m = node('m', 25)
a = node('a', 40)
b = node('b', 30)
c = node('c', 30)
d = node('d', 35)
e = node('e', 2)
r = node('r', 0)

m.addadj([(5, a), (8, b), (4, d), (1, e)])
a.addadj([(2, b), (30, r)])
b.addadj([(1, a), (12, c), (3, d), (3, e)])
c.addadj([(6, d), (2, e)])
d.addadj([(5, e), (21, r)])
e.addadj([(40, r)])
#--------------------------------------------


def bfs(start, goal):
    # maintain a queue of paths
    queue = []
    visited = []  #to avoid loops, expanded nodes are stored in a list

    # push the first path into the queue
    queue.append([start])
    print("start node:", start)
    
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == goal:
            return path

        if node in visited:   #check if adj node expanded before
          continue
        visited.append(node)
        
        print("current path: ", [x.name for x in path])
        print("current node: ", node)
        print("edges: ", [x[1].name for x in node.adj])

        # for all adjacent nodes, construct a 
        # new path and push it into the queue
        for adjacent in node.adj:
            print("current child: ", adjacent[1])
            new_path = list(path)
            new_path.append(adjacent[1])
            print("path to child: ", [x.name for x in new_path])
            queue.append(new_path)
            #print queue
            print("queue of paths: ")
            for i in queue:
              print([x.name for x in i], end=' ')
            print("\n")
#----------------------
        
print ("breadth search path: ", [x.name for x in bfs(m, r)])