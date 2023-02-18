def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    path = [[-1 for _ in range(total)] for _ in range(total)]#初始化path
    #創建原圖形
    inf = float("inf")
    W = [[inf  for _ in range(total)] for _ in range(total)]
    for u,v,x in matrix:
        W[u-1][v-1] = x
    for n in range (total):
        W[n][n]=0
    A = W
    #加入中轉點，找最短路徑長度
    for k in range (total):
        for i in range (total):
            for j in range (total):
                if (A[i][k] + A[k][j] < A[i][j]):
                    A[i][j] = min(A[i][j], A[i][k] + A[k][j])
                    path[i][j] = k
    #假如 start 到達不了 end，最短距離 return -1，經過節點 return None
    if (A[start-1][end-1])==inf:
        return [-1,None]
    #取得經過路徑
    global s
    s=[]
    def getpath(i,j):
        #path[i][j] != -1表示i~j之間還有最短路徑
        if (path[i][j] != -1):
            getpath(i, path[i][j])
            s.append(str(path[i][j]+1))
            getpath(path[i][j], j)
            return s 
    s = getpath(start-1,end-1) 
    p = str(start)+"".join(s)+str(end)

    ans = [A[start-1][end-1],p]

    return ans


if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    