def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。

    #設path為全是-1的矩陣
    path=list()
    for i in range(total):
       l=list()
       for j in range(total):
           l.append(-1) 
       path.append(l)
    
    #設A為全是無限大的矩陣
    A=list()
    for i in range(total):
        b=list()
        for j in range(total):
            b.append(float('inf'))
        A.append(b)

    #根據題目給的兩點之間所需距離放入A矩陣
    for i in range(len(matrix)):
        A[matrix[i][0]-1][matrix[i][1]-1]=matrix[i][2]

    #檢查是否為最短路徑
    for k in range (total):
        for i in range (total):
            for j in range (total):
                if (A[i][k]+A[k][j]<A[i][j]):
                    A[i][j]=A[i][k]+A[k][j]
                    path[i][j]=k
    
    #定義字串用來接收中轉點
    global change_point
    change_point=str()

    #return 最短路徑的中轉點，按照題目要求合併
    def min_path(i,j):
        global change_point
        if (path[i][j] != -1):
            min_path(i,path[i][j])
            change_point += str(path[i][j]+1)
            min_path(path[i][j],j)
    min_path(start-1,end-1)
    if A[start-1][end-1]==float('inf'):
        ans=[-1,None]
    else:
        ans=[A[start-1][end-1],str(start)+change_point+str(end)]
    
    return ans 

if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    