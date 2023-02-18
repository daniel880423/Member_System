def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    if start == end: 
        return[-1, None]
    ONE = [] 
    RODE = []
    for i in range(0,total+1):
        ONE.append([float("inf")]*(total+1)) 
        RODE.append([-1]*(total+1)) 
    for i in range(1,total+1):
        ONE[i][i] = 0 #節點到自己的距離都為0
    for i in matrix:
        ONE[i[0]][i[1]] = i[2] 
    for k in range(1, total+1):
        for i in range(1, total+1):
             for j in range(1, total+1):
                if (ONE[i][k] + ONE[k][j] < ONE[i][j]): 
                    ONE[i][j] = ONE[i][k] + ONE[k][j] 
                    RODE[i][j] = k 

    ans = [ONE[start][end], ""] 
    if ans[0] == float("inf"): 
        return[-1, None] 

    ans[1] = str(start)
    def getrode(i, j): #尋找(i, j)的中轉點
        if (RODE[i][j] != -1): 
            getrode(i, RODE[i][j]) 
            ans[1] +=str(RODE[i][j]) 
            getrode(RODE[i][j], j) 
    getrode(start, end) 
    ans[1] += str(end)
    
    return ans

if __name__ == '__main__':
    matrix =  [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    