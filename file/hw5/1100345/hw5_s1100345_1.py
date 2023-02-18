def getpath(path,start,end): #佛洛伊德遞迴function找出最短路徑
    global ans
    if start>=0 and end>=0:
        if path[start][end]>=1 :
            getpath(path,start,path[start][end]-1)
            ans = ans + str(path[start][end])
            getpath(path,path[start][end]-1,end)

def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    path = [[-1]*total for i in range(total)]
    A = [[float('inf')]*total for i in range(total)]

    long = len(matrix)
    for n in range(long):
        i = matrix[n][0]
        j = matrix[n][1]
        k = matrix[n][2]
        A[i-1][j-1] = k
        
    for i in range(total):#節點到節點本身距離為0
            A[i][i]=0

    for k in range(total):#計算並比較原本距離和經過中節點距離的最小值
        for i in range(total):
             for j in range(total):
                if (A[i-1][k-1] + A[k-1][j-1] < A[i-1][j-1]):
                    A[i-1][j-1] = min(A[i-1][j-1],A[i-1][k-1] + A[k-1][j-1])
                    path[i-1][j-1]=k

    global ans 
    if path[start-1][end-1]!=-1: #找出最短路徑後，並按照老師要求格式給答案。
        ans = str(start)
        anss = getpath(path,start-1,end-1)
        anss = ans + str(end)
    else:
        return [-1,None]
    return [A[start-1][end-1],anss]

if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    