
def homework_5(martix,start,end,total):
  inf = 99999
  V = 100
  p = [[ [] for j in range(V)] for i in range(V)]
  graph = [[(lambda x: 0 if x[0] == x[1] else inf)([i, j]) for j in range(V)] for i in range(V)]
  for u, v, c in martix:
    graph[u][v] = c 
  path = ''
  dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
  for k in range(V):
    for i in range(V):
      for j in range(V):
        temp = dist[i][j]
        dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
        if(temp != dist[i][j]):
          if(p[k][j] == []):
            p[k][j].append([k,j])
          if(p[i][k] == []):
            p[i][k].append([i,k])
          p[i][j] = p[i][k] + p[k][j]
  if p[start][end] == []:
    return [-1,None]
  for idx,item in enumerate(p[start][end]):
    path += str(item[0])
  path+= str(p[start][end][-1][-1])
  return [int(dist[start][end]),path]
 
if __name__ == "__main__":
  martix = [[[1, 2, 5], [2, 3, 1], [2, 5, 4], [3, 4, 3], [4, 6, 5], [6, 7, 2], [2, 6, 8], [5, 7, 5], [6, 8, 2], [7, 9, 4], [8, 9, 12], [9, 10, 10], [9, 11, 2], [10, 11, 2], [11, 12, 2]], 6, 12, 12]
  start = martix[-3]
  end = martix[-2]
  total = martix[-1]
  martix = martix[0]
  # Function call
  print(homework_5(martix,start,end,total))
