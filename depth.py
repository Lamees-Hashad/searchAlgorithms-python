import sys

# DFS algorithm
def dfs(graph, start, gaol, visited=None):
    if visited is None:
        visited = []
    visited.append(start)

    print(start)
    #print(visited)
    print(sorted(graph[start] - set(visited)))
    if start == gaol:
        return visited

    next = sorted(graph[start] - set(visited))[0]
    #print(next)
    dfs(graph, next, gaol, visited)
    return visited


""" graph = {'s': set(['a', 'b', 'c']),
         'a': set(['e', 'g1']),
         'b': set(['c', 'f']),
         'c': set(['g3']),
         'd': set(['s', 'b', 'g2']),
         'e': set(['g1']),
         'f': set(['d']),
         'g1': set([None]),
         'g2': set([None]),
         'g3': set(['f'])} """

graph = {'m': set(['a', 'b', 'd', 'e']),
         'a': set(['b', 'r']),
         'b': set(['a', 'c', 'd', 'e']),
         'c': set(['d', 'e']),
         'd': set(['e', 'r']),
         'e': set(['r']),
         'r': set([])}


depth_path = dfs(graph, 'm', 'r')

print(depth_path)