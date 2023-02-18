def homework_5(matrix, start, end, total): 
    if start == end: 
        return[-1, None]
    A = [] 
    path = []
    for i in range(0,total+1):
        A.append([float("inf")]*(total+1)) #建立一個(total+1)*(total+1)階的A矩陣"inf"無限大
        path.append([-1]*(total+1)) 
    for i in range(1,total+1):
        A[i][i] = 0 #到自己所需的距離為0
    for i in matrix:
        A[i[0]][i[1]] = i[2] #將matrix值存入A
    for k in range(1, total+1):
        for i in range(1, total+1):
             for j in range(1, total+1):
                if (A[i][k] + A[k][j] < A[i][j]): #距離比原路徑小
                    A[i][j] = A[i][k] + A[k][j] 
                    path[i][j] = k #存入path

    ans = [A[start][end], ""] #ans[0]=start到end的最短距離 ans[1]=路徑
    if ans[0] == float("inf"): 
        return[-1, None] 

    ans[1] = str(start)
    def getpath(i, j): #尋找(i, j)之中的中轉點
        if (path[i][j] != -1): #中轉點!=-1 代表存在中轉點path[i][j]
            getpath(i, path[i][j]) #尋找(i, 中轉點path[i][j])之中的中轉點
            ans[1] +=str(path[i][j]) #路徑加上中轉點
            getpath(path[i][j], j) #尋找(中轉點path[i][j], j)之中的中轉點
    getpath(start, end) 
    ans[1] += str(end)
    
    return ans

if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))