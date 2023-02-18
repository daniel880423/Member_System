

def homework_5(matrix, start, end, total): 
    
    path=list()
    i=j=1
    for i in range(total):
        l=list()
        for j in range(total):
            l.append(-1)
        path.append(l)
    

    V=list()
    i=j=1
    for i in range(total):
        l=list()
        for j in range(total):
            l.append(float('inf'))
        V.append(l)

    for i in range(total):
        for j in range(total):
            if i==j:
                V[i][j]=0
            
    for i in matrix:
        V[i[0]-1][i[1]-1]=i[-1]

    for k in range(total):
        for i in range(total):
           for j in range(total): 
            if(V[i][k]+V[k][j]<V[i][j]):
                V[i][j]=V[i][k]+V[k][j]
                path[i][j]=k+1  
    
    def getpath(i,j):
        
        global path1
        
        if path[i][j]!=-1:
            path1 = ""
            getpath(i,path[i][j]-1)
            path1+=str(path[i][j])
            getpath(path[i][j]-1,j)
            return path1
        
    ans = []
    if V[start-1][end-1] == float('inf') or V[start-1][end-1]==0:
        ans = [-1, None]
    else:
        ans.append(V[start-1][end-1])
        if path[start-1][end-1] == -1:
            ans.append(str(start)+str(end))
        else:
            ans.append(str(start)+getpath(start-1,end-1)+str(end))

        
    return ans
#path1=""

if __name__ == '__main__':
    matrix = [[2, 1, 6], [2, 3, 8]]
    start = 2;end = 2; total = 3
    print(homework_5(matrix, start, end, total))