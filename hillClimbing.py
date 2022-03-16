#avoid loops using the path
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

def hillClimbing(start, goal, path=None, potential_paths=set()):
    if path == None:
        path = []
    path.append(start)

    if tuple(path) in potential_paths:
        potential_paths.remove(tuple(path))

    print("current node: ", start.name)
    print("current path: ", [x.name for x in path])

    if start == goal:
        return path

    print("edges: ", [x[1].name for x in start.adj])
    print("    h: ", [x[1].h for x in start.adj])

    next = start.adj[0][1]
    for temp in start.adj:
        if temp[1] in path: #if node has beed visited already, skip and take second smallest
            print(temp[1].name, " is visited")
            continue
        if temp[1].h < start.h:
            potential_paths.add(tuple(path + [temp[1]])) #if h increases don't add to potential paths
        if temp[1].h < next.h:  #get nod with smallest h
            next = temp[1]

    if next.h > start.h:                   #if h increases we pop a path from potential_paths
        path = list(potential_paths.pop()) #potential_paths is a set so pop gets a random path
        print("change path to: ", [x.name for x in path])
        next = path[-1]
        path = path[0:-1]

    print("list of potential paths:")
    for i in potential_paths:
        print([x.name for x in i], end=' ')
    print("\n")

    return hillClimbing(next, goal, path, potential_paths)
#----------------------

hillClimbingSearch = hillClimbing(m, r)
print("hill Climbing search path:", [x.name for x in hillClimbingSearch])
