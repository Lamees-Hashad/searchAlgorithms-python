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

def greedy(start, end):
    path = []
    path.append(start.name)

    next = min((x for x in start.adj),key=itemgetter(1), default="EMPTY")
    
    if (next == "EMPTY") or (next[0].name == end.name):
        path.append(next[0].name)

    greedy(next[0], end)

    #for e in start.adj:
        
        #print(e[0].name, end=" ")
        #print(e[1])

greedy(m, r)
