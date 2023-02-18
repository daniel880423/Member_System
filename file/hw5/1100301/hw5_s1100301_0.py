def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if start == end: 
        return[-1, None]
    A = [] 
    path = []
    for i in range(0,total+1):
        A.append([float("inf")]*(total+1)) 
        path.append([-1]*(total+1)) 
    for i in range(1,total+1):
        A[i][i] = 0 
    for i in matrix:
        A[i[0]][i[1]] = i[2] 
    for k in range(1, total+1):
        for i in range(1, total+1):
             for j in range(1, total+1):
                if (A[i][k] + A[k][j] < A[i][j]): 
                    A[i][j] = A[i][k] + A[k][j] 
                    path[i][j] = k 

    ans = [A[start][end], ""] 
    if ans[0] == float("inf"): 
        return[-1, None] 

    ans[1] = str(start)
    def getpath(i, j):
        if (path[i][j] != -1): 
            getpath(i, path[i][j]) 
            ans[1] +=str(path[i][j]) 
            getpath(path[i][j], j) 
    getpath(start, end) 
    ans[1] += str(end)
    
    return ans

if __name__ == '__main__':
    matrix =  [[2, 1, 6], [2, 3, 8]]
    start = 2;end = 2; total = 3
    print(homework_5(matrix, start, end, total))
    