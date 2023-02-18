def getpath(path,start,end):                               #佛洛伊德遞迴function找出最短路徑
    global ans
    if start>=0 and end>=0:
        if path[start][end]>=1 :
            getpath(path,start,path[start][end]-1)
            ans = ans + str(path[start][end])
            getpath(path,path[start][end]-1,end)

def homework_5(matrix, start, end, total):                 
    path = [[-1]*total for i in range(total)]              #一個矩陣存取節點中插入的中轉點。
    A = [[float('inf')]*total for i in range(total)]       # 一個矩陣存取節點到節點間的路徑。


    long = len(matrix)
    for m in range(long):
        i = matrix[m][0]
        j = matrix[m][1]
        k = matrix[m][2]
        A[i-1][j-1] = k
        
    for i in range(total):                                 #節點到節點本身距離為0
            A[i][i]=0

    for k in range(total):                                 #計算並比較原本距離和經過中節點距離的最小值
        for i in range(total):
             for j in range(total):
                if (A[i][k] + A[k][j] < A[i][j]):
                    A[i][j] = min(A[i][j],A[i][k] + A[k][j])
                    path[i][j]=k+1
    if start == end:                                       
        return [-1,None]
    global ans 
    if path[start-1][end-1]!=-1:                           #找出最短路徑後，並按照老師要求格式給答案。
        ans = str(start)
        path_ans = getpath(path,start-1,end-1)
        path_ans = ans + str(end)
    else:
        return [-1,None]

    return [A[start-1][end-1],path_ans]

if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))