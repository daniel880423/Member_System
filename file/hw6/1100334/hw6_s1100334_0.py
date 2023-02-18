def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    n=len(nodes)
    W=[[float("inf") for i in range (n)]for j in range(n)]
    for k in range(n-1):
        W[k][k]=0
    for i in range (n):
        for j in range (i+1,n):
            x=nodes[i][0]-nodes[j][0]
            y=nodes[i][1]-nodes[j][1]
            l=abs(x)+abs(y)
            W[i][j],W[j][i]=l,l


    near=[0 for i in range (n-1)]    
    dist=[W[0][i] for i in range (1,n)]
    ans=0
    for t in range(1,n):
        min = float("inf")
        for i in range (n-1):
            if dist[i]>=0 and dist[i]<min:
                min=dist[i]
                vnear=i
    
        ans+=W[vnear+1][near[vnear]]
        dist[vnear]=-1
        
        for i in range(1,n):
            if W[i][vnear+1]<dist[i-1]:
                dist[i-1]=W[i][vnear+1]
                near[i-1]=vnear+1    
        
    
    return ans

if __name__ == '__main__':
    nodes = nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    