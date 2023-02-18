def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    A = [[float("inf") if x!=y else 0 for x in range(total)] for y in range(total) ]   #設立3*3初始值為無限大的矩陣，並且對角線的值為0
    path = [[-1 for x in range(total)] for y in range(total) ]      #設立3*3初始值=-1的path矩陣
    for a,b,c in matrix:                        #矩陣A
        A[a-1][b-1] = c           
    for i in range(total):                      #path矩陣
        for j in range(total):
            for k in range(total):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = min(A[i][j],A[i][k] + A[k][j])
                    path[i][j] = k
    global s
    s = str() 
    def getpath(i, j):                  
        if path[i][j]!=-1:
            global s
            getpath(i, path[i][j])
            s += str(path[i][j]+1)
            getpath(path[i][j], j)

    
    getpath(start-1 ,end-1)
    if A[start-1][end-1] == float("inf"):       #如果沒有最短距離(也就是無限大)，那麼便回傳[-1,None]
            return[-1,None]
    
    return [A[start-1][end-1],str(start)+s+str(end)]  

if __name__ == '__main__':
    matrix = [[1, 2, 2], [1, 3, 1], [1, 4, 5], [3, 4, 2], [4, 5, 1]]
    start = 2;end = 5; total = 5
    print(homework_5(matrix, start, end, total))
    