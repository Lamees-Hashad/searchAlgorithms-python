#avoid loops using the path

from operator import itemgetter
from numpy import empty

class node:
    def __init__(self, name, h):
        self.name = name
        self.h = h
        self.adj = []
    
    def addadj(self, adj):
        self.adj = adj


m = node('m', 25)
a = node('a', 40)
b = node('b', 30)
c = node('c', 30)
d = node('d', 35)
e = node('e', 2)
r = node('r', 0)

m.addadj([(a, 5), (b, 8), (d, 4), (e, 5)])
a.addadj([(b, 2), (r, 30)])
b.addadj([(a, 1), (c, 12), (d, 3), (e, 3)])
c.addadj([(d, 6), (e, 2)])
d.addadj([(e, 5), (r, 21)])
e.addadj([(r, 40)])

def hillClimbing(start, end, path=None, potential_paths=set()):
    if path == None:
        path = []
    path.append(start)

    print(start.name)

    if start == end:
        return path

    print([x[0].name for x in start.adj])
    print([x[0].h for x in start.adj])

    next = start.adj[0][0]
    for temp in start.adj:
        potential_paths.add(tuple(path + [temp[0]]))
        if temp[0].h < next.h:
            next = temp[0]

    if next.h > start.h:
        path = list(potential_paths.pop())
        next = path[-1]

    return hillClimbing(next, end, path, potential_paths)

hillClimbingSearch = hillClimbing(m, r)
print("hill Climbing search path:", [x.name for x in hillClimbingSearch])
