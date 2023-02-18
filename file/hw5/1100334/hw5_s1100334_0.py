def homework_5(matrix, start, end, total):

    path=[[-1 for i in range (total)]for j in range(total)]
    A=[[float("inf") for i in range (total)]for j in range(total)]

    for k in matrix:
        A[k[0]-1][k[1]-1]=k[2]
        
    for k in range (total):
        for i in range (total):
            for j in range (total):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
                    path[i][j] = k
    if A[start-1][end-1]==float("inf"):
        return[-1,None]

    
    global s
    s=''
    def getpath (i, j):
        if (path[i][j] != -1):
            global s            
            getpath(i, path[i][j])
            s+=str(path[i][j]+1)
            getpath(path[i][j], j)
            
    getpath(start-1,end-1)

    ans=[A[start-1][end-1],str(start)+s+str(end)] 
    return ans

if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    