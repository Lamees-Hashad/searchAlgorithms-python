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

# DFS algorithm
def dfs(start, gaol, path=None):
    if path is None:
        path = []
    path.append(start)

    print("current node: ", start.name)
    print("       edges: ", sorted(set([x[1].name for x in start.adj]) - set(x.name for x in path)))
    if start == gaol:
        return path

    next = sorted(sorted(set([x[1] for x in start.adj]) - set(path)))[0]
    #print(next)
    dfs(next, gaol, path)
    return path
#----------------------

depth_path = dfs(m, r)

print("depth search path: ", [x.name for x in depth_path])