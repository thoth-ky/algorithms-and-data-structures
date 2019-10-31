 
from collections import defaultdict 

''' 
G = (V, E) where E is Edges, V vertices
DFS(G, node)
    # visited, array of size |V| if G = (V, E)
    # visited[i] == True if we have listed node I, otherwise FALSE
    # visited = CreateArray(|V|) exists outside algorithms
    visited[node] <— True

    foreach v in AdjacencyList(G, node) do
        if not visited[v] then
            DFS(G,v)
'''
class Graph: 
  def __init__(self): 
    self.graph = defaultdict(list)

  def add_edges(self, list_of_edges):
    for origin, term in list_of_edges:
      self.graph[origin].append(term)
  
  def recursive_dfs(self, node, visited):
    visited[node] = True

    print(node, end='\n')

    for i in self.graph[node]:
      if visited[i] == False:
        self.recursive_dfs(i, visited)


  def dfs(self, node):
    visited = [False] * len(self.graph)
    self.recursive_dfs(node, visited)


# TEST
g = Graph() 
g.add_edges([(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)])
  
print("DFS") 
g.dfs(1) 
