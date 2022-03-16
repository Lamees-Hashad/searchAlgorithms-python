# same as the uniform search function but we add the h value to the cumulative cost g
#add <,<= implementation,
# so if f value is same for 2 paths in the priorty queue take node smallest alphabetically

import queue

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

def A_Star(start, goal):
    visited = set()                  # set of visited nodes
    q = queue.PriorityQueue()        # we store vertices in the (priority) queue as tuples 
                                     # (f, g, n, path), with
                                     # f: the cumulative cost g + h,
                                     # n: the current node,
                                     # path: the path that led to the expansion of the current node
    q.put((start.h, 0, start, [start]))       # add the starting node and it's path contains only itself.

    while not q.empty():             # while the queue is nonempty
        f, g, current_node, path = q.get()
        visited.add(current_node)    # mark node visited on expansion,

        print("\n current node:\n",current_node.name, " path: ", [x.name for x in path])

        if current_node == goal:     # if the current node is a goal
            return path              # return its path
        else:
            print("edges: ")
            for edge in current_node.adj:
                child = edge[1]
                print(edge[1].name, ",f:", edge[0]+g+child.h, end="    ")
                if child not in visited:  #if child was not expanded before add path to it to the queue
                    q.put((g + edge[0] + child.h, g + edge[0], child, path + [child]))
#----------------------

print("A Star search path: ",[x.name for x in A_Star(m, r)])