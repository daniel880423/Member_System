def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal
    sum=0
    V=[0]
    W = [[float("inf") for i in range(len(nodes))] for j in range(len(nodes))]
    for i in range(len(W)-1):
        for j in range(i+1,len(W)):
            W[i][j]=abs(nodes[i][0]-nodes[j][0])+abs(nodes[i][1]-nodes[j][1])
            W[j][i]=W[i][j]
    while True:
        g=[]       
        for j in V:
            g.append([min(W[j]),j])
        g=sorted(g)
        for i in range(len(W)):
            if W[g[0][1]][i]==g[0][0]:
                V.append(i)
                sum+=g[0][0]
                W[j][i]=float("inf")
                W[i][j]=float("inf")
                break
        if len(V) == len(nodes):
            break
                
              
    return sum

if __name__ == '__main__':
    nodes = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(homework_6(nodes))
    # 22
    