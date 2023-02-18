def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    path = [[-1]*total for i in range(total)]
    A = [[float('inf')]*total for i in range(total)]

    long = len(matrix)
    for n in range(long):
        i = matrix[n][0]
        j = matrix[n][1]
        k = matrix[n][2]
        A[i-1][j-1] = k
        
    for i in range(total):
            A[i][i]=0

    for k in range(total):
        for i in range(total):
             for j in range(total):
                if (A[i-1][k-1] + A[k-1][j-1] < A[i-1][j-1]):
                    A[i-1][j-1] = min(A[i-1][j-1],A[i-1][k-1] + A[k-1][j-1])
                    path[i-1][j-1]=k

    
    if A[start-1][end-1] == float('inf'):
        return[-1, None]
    p = str(start)
    for j in range(end):
        if path[start-1][j]!=-1:
            p += str(path[start-1][j])
    p += str(end) 
    return[A[start-1][end-1], p]






    

if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    