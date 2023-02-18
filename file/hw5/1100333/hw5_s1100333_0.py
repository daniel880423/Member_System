def homework_5(matrix, start, end, total):#1100333

    path=[[-1 for i in range (total)]for j in range(total)]
    A=[[float("inf") for i in range (total)]for j in range(total)]

    for m in matrix:
        A[m[0]-1][m[1]-1]=m[2]
        
    for m in range (total):
        for n in range (total):
            for k in range (total):
                if A[n][m] + A[m][k] < A[n][k]:
                    A[n][k] = A[n][m] + A[m][k]
                    path[n][k] = m
    if A[start-1][end-1]==float("inf"):
        return[-1,None]

    print(A)
    print(path)
    global s
    s=''
    def getpath (m, n):
        if (path[m][n] != -1):
            global s            
            getpath(m, path[m][n])
            s+=str(path[m][n]+1)
            getpath(path[m][n], n)
            
    getpath(start-1,end-1)

    result=[A[start-1][end-1],str(start)+s+str(end)] 
    return result

if __name__ == '__main__':
    matrix =    [[1,2,1],[1,3,3],[2,1,2],[3,4,4]]
    start = 3;end = 1; total = 4
    print(homework_5(matrix, start, end, total))
    