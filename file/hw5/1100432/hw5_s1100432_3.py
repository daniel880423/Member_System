def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    if start == end: 
        return[-1, None]
    M = [] 
    point = []
    for i in range(0,total+1):
        M.append([float("inf")]*(total+1)) 
        point.append([-1]*(total+1)) 
    for i in range(1,total+1):
        M[i][i] = 0 
    for i in matrix:
        M[i[0]][i[1]] = i[2] 
    for k in range(1, total+1):
        for i in range(1, total+1):
             for j in range(1, total+1):
                if (M[i][k] + M[k][j] < M[i][j]): 
                    M[i][j] = M[i][k] + M[k][j] 
                    point[i][j] = k 

    ans = [M[start][end], ""] 
    if ans[0] == float("inf"): 
        return[-1, None] 

    ans[1] = str(start)
    def getmyway(i, j): 
        if (point[i][j] != -1): 
            getmyway(i, point[i][j]) 
            ans[1] +=str(point[i][j]) 
            getmyway(point[i][j], j) 
    getmyway(start, end) 
    ans[1] += str(end)
    
    return ans

if __name__ == '__main__':
    matrix =  [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    