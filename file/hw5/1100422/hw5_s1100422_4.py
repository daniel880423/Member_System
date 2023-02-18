def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。


    #先設一個矩陣A裡面全部放無限大，用來記錄最短路徑
    A=list()
    for i in range(total):
        b=list()
        for j in range(total):
            b.append(float('inf'))
        A.append(b)

     #先設一個矩陣path裡面全部放-1，用來記錄中轉點
    path=list()
    for i in range(total):
        l=list()
        for j in range(total):
            l.append(-1)
        path.append(l)

    #依照題目給的兩點之間所需距離放入矩陣A中
    for i in range(len(matrix)):
        A[matrix[i][0]-1][matrix[i][1]-1]=matrix[i][2]

    #檢查矩陣A中的是否為最短路徑
    for k in range (total):
        for i in range (total):
            for j in range (total):
                if (A[i][k] + A[k][j] < A[i][j]):
                    A[i][j] = A[i][k] + A[k][j]
                    path[i][j] = k

    #定義一個字串relay_point用來接收中轉點
    global relay_point
    relay_point=str()

    #將找到的最短路徑中轉點return出來並合併成題目要求的答案
    def pathnew(i,j):
        global relay_point
        if (path[i][j] != -1):
            pathnew(i, path[i][j])
            relay_point += str(path[i][j]+1)
            pathnew(path[i][j], j)
    pathnew(start-1,end-1)
    if A[start-1][end-1]==float('inf'):
        answer=[-1,None]
    else:
        answer=[A[start-1][end-1],str(start)+relay_point+str(end)]
    return answer

if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,3],[2,1,2],[3,4,4]] 
    start = 2; end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    