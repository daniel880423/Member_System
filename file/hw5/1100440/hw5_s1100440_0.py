def homework_5(matrix, start, end, total):                      # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
                                                                # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。

    path = []                                                   # P矩陣
    checkpoint = []                                             # 
    total += 1
    ans = ""                                                    # 總路徑
    for i in range(0, total):                                   
        tempPath = []                                           # path的暫存點
        tempCheckpoint = []                                     # checkpoint的暫存點
        for j in range(0, total):
            tempPath.append(101)                                # 初始化tempPath
            tempCheckpoint.append(j)                            # 初始化tempCheckpoint
        path.append(tempPath)                                   # 初始化path
        checkpoint.append(tempCheckpoint)                       # 初始化checkpoint
    for vec in matrix:                                          # 讀取題目matrix
        path[vec[0]][vec[1]] = vec[2]                           
    for k in range(0, total):                                   
        for i in range(0, total):                               
            for j in range(0, total):                           
                if (path[i][k]+path[k][j] < path[i][j]):        
                    path[i][j] = path[i][k]+path[k][j]          
                    checkpoint[i][j] = checkpoint[i][k]         

    if checkpoint[i][j] == None:                                # 專門給沒有路徑抵達的特例
        endless = (-1, None)                                    
        return endless                                          

    def find_path(ans, s, e):                                   # 輸出路徑
        ans += str(s)
        if (s != e):
            return find_path(ans, checkpoint[s][e], e)
        else:
            return ans
    ans = find_path(ans, start, end)
    if path[start][end] == 101:
        return [-1,None]
    else:
        return [path[start][end], ans]


if __name__ == '__main__':
    matrix = [[1, 2, 2], [1, 3, 1], [1, 4, 5], [3, 4, 2], [4, 5, 1]]
    start = 1
    end = 5
    total = 5
    print(homework_5(matrix, start, end, total))
