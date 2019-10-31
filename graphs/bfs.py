 
from collections import defaultdict 

'''
# G = (V, E) where E is Edges, V vertices

BFS(G, node) -> visited
  Q - CreateQueue()
  Visited <— CreateArray(|V|)
  Inqueue <— CreateArray(|V|)
  
  for i <— 0 |V| do
    Visited[i] <— False
    Inqueue[i] <— False

  Enqueue(Q, node)
  inqueue[node] <- True
  While not isQueueEmpty(Q) do
    C <— Dequeue(Q)
    inqueue[c] <— False
    Visited[c] <— True
      
  Foreach v in AdjacencyList(G,C) do
    If not visited[v] and not inqueue[v] then
      Enqueue(Q,v)
      Inqueue[v] <— True
  Return visited

'''


class Graph: 
  def __init__(self): 
    self.graph = defaultdict(list)

  def add_edges(self, list_of_edges):
    for origin, term in list_of_edges:
      self.graph[origin].append(term)
  


  def bfs(self, node):
    queue = []
    visited = [False] * len(self.graph)  
    inqueue = [False] * len(self.graph)

    queue.append(node)
    inqueue[node] =  True
    
    while queue:
      el = queue.pop()
      print(el, end='\n')
      
      inqueue[el] =  False
      visited[el] =  True
      for neighbor in self.graph[el]:
        print(f'n: {el} -> {neighbor}')
        if not visited[neighbor] and not inqueue[neighbor]:
          queue.append(neighbor)
          inqueue[neighbor] = True
    return visited 

# TEST

g = Graph() 
g.add_edges([(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)])
  
print("BFS") 
v = g.bfs(1) 
print(v)