def path(p, start, end):
    global ans
    if start >= 0 and end >= 0:
        if p[start][end]>=1:
            path(p, start, p[start][end]-1)
            ans = ans + str(p[start][end])
            path(p, p[start][end]-1, end)
def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    start = start - 1
    end = end - 1
    p = [[-1]*total for i in range(total)]
    A = [[float("inf")]*total for i in range(total)]
    l = len(matrix)
    for m in range(l):
        i = matrix[m][0]
        j = matrix[m][1]
        k = matrix[m][2]
        A[i-1][j-1] = k
    for i in range(total):
        A[i-1][i-1] = 0
    for k in range(total):
        for i in range(total):
            for j in range(total):
                 if (A[i][k] + A[k][j] < A[i][j]):
                    A[i][j] = A[i][k] + A[k][j]
                    p[i][j] = k+1
    global ans
    if p[start][end] != -1:
        ans = str(start+1)
        ans_2 = path(p, start, end)
        ans_2 = ans + str(end+1)
    else:
        return [-1,None]
    return [A[start][end], ans_2]

    










if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    