import numpy as np
def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    N = len(nodes)
    A = np.zeros((N,N)).astype(int)

    for i in range(N):
        for j in range(i,N):
            if i == j:
                continue
            d = abs(nodes[i][0]-nodes[j][0]) + abs(nodes[i][1]-nodes[j][1])
            A[i][j] = d
            A[j][i] = A[i][j]
      
    selected_node = [0 for i in range(N)]
    no_edge = 0
    selected_node[0] = True
    INF = 99999
    sum = 0
    while (no_edge < N - 1):
    
        minimum = INF
        a = 0
        b = 0
        for m in range(N):
            if selected_node[m]:
                for n in range(N):
                    if ((not selected_node[n]) and A[m][n]):  
                        # not in selected and there is an edge
                        if minimum > A[m][n]:
                            minimum = A[m][n]
                            a = m
                            b = n
        sum += A[a][b]
        selected_node[b] = True
        no_edge += 1
    return sum






    

if __name__ == '__main__':
    nodes = [[-1, 18], [11, 19], [-13, -18], [-17, 0]]
    print(homework_6(nodes))
    # 22
    