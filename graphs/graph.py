class Graph: 
  def __init__(self): 
    self.graph = defaultdict(list)

  def add_edges(self, list_of_edges):
    # creates edges between two given nodes in your graph
    for origin, term in list_of_edges:
      self.graph[origin].append(term)
  
  def add_node(self, node):
    # adds vertices to your graph
    self.graph[node]

  def remove_node(self, node):
    # removes vertices from your graph
    pass

  def remove_edge(self, edge_tuple):
    # removes edges between two given vertices in your graph
    pass

  def contains(self, node):
    # checks if your graph contains a given node
    pass

  def has_edge(self, (edge_tuple)):
    # checks if a connection exists between two given nodes in your graph
    pass