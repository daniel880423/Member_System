def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    
    A = []     #假設一個空矩陣
    path = []      #假設一個路徑

    if start == end:     #若初始位置到不了終點位置
        return[-1, None]        #回傳要求的結果:最短距離 return -1/經過節點 return None

    for i in range(0,total+1):
        A.append([float("inf")]*(total+1))     #將A矩陣全部的值設為無限大
        path.append([-1]*(total+1))      #將路徑的值設為-1

    for i in range(1,total+1):
        A[i][i] = 0     #對角線數值=0:因為自己到自己所需的距離都為0

    for i in matrix:
        A[i[0]][i[1]] = i[2]     #將matrix的值存入A

    for k in range(1, total+1):     #中轉點 k
        for i in range(1, total+1):      #循環矩陣的 row
             for j in range(1, total+1):      #循環矩陣的 column
                if (A[i][k] + A[k][j] < A[i][j]):       #判斷若過中轉點路徑比原路徑小
                    A[i][j] = A[i][k] + A[k][j]        #則替換矩陣最短路徑
                    path[i][j] = k       #添加中轉點k至path

    ans = [A[start][end], ""]      #ans[0]=start到end的最短距離/ans[1]=路徑
    if ans[0] == float("inf"):      #若ans[0]=無窮大
        return[-1, None]        #則直接回傳[-1, None]

    ans[1] = str(start)

    def getpath(i, j):     #尋找(i, j)之中的中轉點
        if (path[i][j] != -1):      #中轉點 != -1:-1代表i~j沒有更短的路徑
            getpath(i, path[i][j])       #尋找起始位置i~j中間是否有中轉點，有的話代表他前面還有節點需要走訪
            ans[1] +=str(path[i][j])         #路徑加上中轉點
            getpath(path[i][j], j)       #查看中轉點~j是否還有更短的路徑

    getpath(start, end) 
    ans[1] += str(end)
    
    return ans

if __name__ == '__main__':
    matrix =  [[2, 1, 6], [2, 3, 8]]
    start = 2;end = 2; total = 3
    print(homework_5(matrix, start, end, total))
    