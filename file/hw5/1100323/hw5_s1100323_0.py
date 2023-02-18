def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    if start == end: 
        return[-1, None]
    D = [] #matrix[i](a, b, c)  A[a][b]將儲存c的值
    V = []
    for i in range(0,total+1):
        D.append([float("inf")]*(total+1)) #建立一個(total+1)*(total+1)階的A矩陣且全部的值都是無限大
        V.append([-1]*(total+1)) #建立一個(total+1)*(total+1)階的path矩陣且全部的值都是-1
    for i in range(1,total+1):
        D[i][i] = 0 #任何節點到自己所需的距離都為0
    for i in matrix:
        D[i[0]][i[1]] = i[2] #將matrix給予的值存入A
    for k in range(1, total+1):
        for i in range(1, total+1):
             for j in range(1, total+1):
                if (D[i][k] + D[k][j] < D[i][j]): #如果透過中轉點的距離比原路徑小
                    D[i][j] = D[i][k] + D[k][j] #替換最短路徑
                    V[i][j] = k #將此中轉點存入path

    ans = [D[start][end], ""] #ans[0]=start到end的最短距離 ans[1]=路徑
    if ans[0] == float("inf"): #ans[0]=inf 也就是並無start到end的路徑就直接回傳[-1, None] 
        return[-1, None] 

    ans[1] = str(start)
    def getpath(i, j): #尋找(i, j)之中的中轉點
        if (V[i][j] != -1): #中轉點!=-1 代表存在中轉點path[i][j]
            getpath(i, V[i][j]) #尋找(i, 中轉點path[i][j])之中的中轉點
            ans[1] +=str(V[i][j]) #路徑加上中轉點
            getpath(V[i][j], j) #尋找(中轉點path[i][j], j)之中的中轉點
    getpath(start, end) 
    ans[1] += str(end)
    
    return ans

if __name__ == '__main__':
    matrix =  [[1,2,2],[1,3,1],[1,4,5],[3,4,2],[4,5,1]]
    start = 2;end = 5; total = 5
    print(homework_5(matrix, start, end, total))