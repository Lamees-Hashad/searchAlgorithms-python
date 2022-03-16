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

def greedy(start, goal, path=None):
    if start == None:   # if no node was passed the search faild to find a pass
        return "fail to find a path"
    if path == None:  # store path in a list
        path = []
    path.append(start.name)  #add current node to the path

    print("current node: ", start.name)

    if start == goal:  #return if goal was found
        return path

    #print edges and h values
    print("edges: ", [x[1].name for x in start.adj])
    print("    h: ", [x[1].h for x in start.adj])

    #next node is the node with smallest h value from the adj list
    next = start.adj[0][1]
    for temp in start.adj:
        if temp[1].name in path: #if node has beed visited already, skip and take second smallest
            continue
        if temp[1].h < next.h:
            next = temp[1]
    if next.name in path:
        next = None

    return greedy(next, goal, path)
#----------------------

gredySearch = greedy(m, r)
print("greedy search path:", gredySearch)
