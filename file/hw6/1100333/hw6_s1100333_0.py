def homework_6(nodes):
    k=len(nodes)
    s=[[float("inf") for i in range (k)]for j in range(k)]
    for k in range(k-1):
        s[k][k]=0
    for i in range (k):
        for j in range (i+1,k):
            x=nodes[i][0]-nodes[j][0]
            y=nodes[i][1]-nodes[j][1]
            l=abs(x)+abs(y)
            s[i][j],s[j][i]=l,l

    dist=[s[0][i] for i in range (1,k)]
    neighbouring=[0 for i in range (k-1)]    
    result=0
    for t in range(1,k):
        min = float("inf")
        for i in range (k-1):
            if dist[i]>=0 and dist[i]<min:
                min=dist[i]
                vnear=i
    
        result+=s[vnear+1][neighbouring[vnear]]
        dist[vnear]=-1
        
        for i in range(1,k):
            if s[i][vnear+1]<dist[i-1]:
                dist[i-1]=s[i][vnear+1]
                neighbouring[i-1]=vnear+1    
        
    
    return result

if __name__ == '__main__':
    nodes = nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    