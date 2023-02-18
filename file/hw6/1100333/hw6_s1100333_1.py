def homework_6(nodes):
    s=len(nodes)
    K=[[float("inf") for i in range (s)]for j in range(s)]
    for k in range(s-1):
        K[k][k]=0
    for i in range (s):
        for j in range (i+1,s):
            x=nodes[i][0]-nodes[j][0]
            y=nodes[i][1]-nodes[j][1]
            l=abs(x)+abs(y)
            K[i][j],K[j][i]=l,l


    near=[0 for i in range (s-1)]    
    dist=[K[0][i] for i in range (1,s)]
    RES=0
    for t in range(1,s):
        min = float("inf")
        for i in range (s-1):
            if dist[i]>=0 and dist[i]<min:
                min=dist[i]
                vnear=i
    
        RES+=K[vnear+1][near[vnear]]
        dist[vnear]=-1       
        for i in range(1,s):
            if K[i][vnear+1]<dist[i-1]:
                dist[i-1]=K[i][vnear+1]
                near[i-1]=vnear+1    
        
    
    return RES

if __name__ == '__main__':
    nodes = nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    