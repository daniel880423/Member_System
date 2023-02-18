def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    path = []
    A = []

    for i in range(total):
        path.append([-1]*total)
        A.append([float('inf')]*total)

    for i in range(total):
        A[i][i] = 0
    for i in matrix:
        A[i[0]-1][i[1]-1] = i[2]

    for k in range(total):
        for i in range(total):
            for j in range(total):
                if(A[i][k] + A[k][j] < A[i][j]):
                    A[i][j] = A[i][k] + A[k][j]
                    path[i][j] = k

    ans = [A[start-1][end-1], '']

    if ans[0] == float('inf'):
        return[-1, None]

    ans[1] = str(start)
    def getpath(i, j):
        if(path[i][j] != -1):
            getpath(i, path[i][j])
            ans[1] += str(path[i][j])
            getpath(path[i][j], j)

    getpath(start-1, end-1)
    ans[1] += str(end)

    return ans

if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    