def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    if start == end: 
        return[-1, None]
    A = []                                           #建立一個matrix對應A[a][b]存入需要走的步數c
    path = []                                        #建立一個matrix存入中轉點
    for i in range(0,total+1):
        A.append([float("inf")]*(total+1))           #建立一個(total+1)*(total+1)階的A矩陣且全部的值預設為inf
        path.append([-1]*(total+1))                  #建立一個(total+1)*(total+1)階的path矩陣且全部的值預設為-1
    for i in range(1,total+1):                       #利用for迴圈將matrix對角線的值依序存入A
        A[i][i] = 0                                  #任何節點到自己所需的距離都為0 
    for i in matrix:                                 #利用for迴圈將matrix給予的值依序存入A
        A[i[0]][i[1]] = i[2]                         
    for k in range(1, total+1):
        for i in range(1, total+1):
            for j in range(1, total+1):
                if (A[i][k] + A[k][j] < A[i][j]):    #如果透過中轉點的距離比原路徑小
                    A[i][j] = A[i][k] + A[k][j]      #替換最短路徑
                    path[i][j] = k                   #將此中轉點存入path

    ans = [A[start][end], ""]                        #ans[0]存入start到end的最短距離 ans[1]存入路徑
    if ans[0] == float("inf"):                       #ans[0]=inf 也就是並無start到end的路徑就直接回傳[-1, None] 
        return[-1, None] 

    ans[1] = str(start)
    def findp(i, j):                                 #建立function findp尋找(i, j)之中的中轉點
        if (path[i][j] != -1):                       #中轉點不為-1 代表存在中轉點path[i][j]
            findp(i, path[i][j])                     #尋找(i, 中轉點path[i][j])之中的中轉點
            ans[1] += str(path[i][j])                #路徑加上中轉點
            findp(path[i][j], j)                     #尋找(中轉點path[i][j], j)之中的中轉點 
    findp(start, end) 
    ans[1] += str(end)
    
    return ans

if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    