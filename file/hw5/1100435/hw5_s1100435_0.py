def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if start == end: 
        return[-1, None]
    A = [] #matrix[i](a, b, c)  A[a][b]將儲存c的值
    path = []
    for i in range(0,total+1):
        A.append([float("inf")]*(total+1)) #建立一個(total+1)*(total+1)階的A矩陣並且每個數值都是無限大
        path.append([-1]*(total+1)) #建立一個(total+1)*(total+1)階的path矩陣且全部的值都是-1
    for i in range(1,total+1):
        A[i][i] = 0 #i到i的距離都是0
    for i in matrix:
        A[i[0]][i[1]] = i[2] #i = [2, 1, 6] = [a, b, c] -> a到b的值=c
    for k in range(1, total+1):
        for i in range(1, total+1):
             for j in range(1, total+1):
                if (A[i][k] + A[k][j] < A[i][j]): #如果(i到k) + (k到j)比(i直接到j)的路徑短
                    A[i][j] = A[i][k] + A[k][j] #(i->k) + (k->j)替換成最短路徑
                    path[i][j] = k #把需要經過的中轉點存入path

    ans = [A[start][end], ""] #ans[0]=start到end的最短距離 ans[1]=經過的全部路徑
    if ans[0] == float("inf"): #沒有這個路徑的話就直接回傳[-1, None] 
        return[-1, None] 

    ans[1] = str(start)
    def getpath(i, j): #尋找(i, j)之中的中轉點
        if (path[i][j] != -1): #如果中轉點k存在 
            getpath(i, path[i][j]) #尋找(i,k)之中的中轉點
            ans[1] +=str(path[i][j]) #紀錄經過的中轉點
            getpath(path[i][j], j) #尋找(k,j)之中的中轉點
    getpath(start, end) 
    ans[1] += str(end)
    
    return ans

if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,3],[2,1,2],[3,4,4]]
    start = 2 ;end = 4 ;total = 4
    print(homework_5(matrix, start, end, total))