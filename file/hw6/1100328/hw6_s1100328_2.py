class Graph:
  def __init__(self, vertices):
    self.V = vertices 
    self.graph = []

  def addEdge(self, u, v, w):
    self.graph.append([u, v, w])
      
  def find(self, parent, i):
    if parent[i] != i:
      parent[i] = self.find(parent, parent[i])
    return parent[i]

  def union(self, parent, rank, x, y):
    if rank[x] < rank[y]:
      parent[x] = y
    elif rank[x] > rank[y]:
      parent[y] = x
    else:
      parent[y] = x
      rank[x] += 1

def homework_6(nodes):
  graph = Graph(len(nodes))
  for i in range(len(nodes)):
    for j in range(i):
      dis = abs(nodes[i][0]-nodes[j][0]) + abs(nodes[i][1]-nodes[j][1])
      graph.addEdge(i, j, dis)

  result = []  
  i = 0
  e = 0

  graph.graph = sorted(graph.graph,key=lambda item: item[2])

  parent = []
  rank = []

  for node in range(graph.V):
      parent.append(node)
      rank.append(0)

  while e < graph.V - 1:

      u, v, w = graph.graph[i]
      i = i + 1
      x = graph.find(parent, u)
      y = graph.find(parent, v)

      if x != y:
          e = e + 1
          result.append([u, v, w])
          graph.union(parent, rank, x, y)

  minimumCost = 0
  for u, v, weight in result:
      minimumCost += weight
  return minimumCost

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    # nodes = [[3,1],[2,7],[4,8],[7,4]]
    print(homework_6(nodes))
