def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    inf = float('Inf')
    A = []
    path = []
    for i in range(total):
        row = []
        row_p = []
        for j in range(total):
            row_p.append(-1)
            if i != j:
                row.append(inf)
            else:
                row.append(0)
        A.append(row)
        path.append(row_p)

    for m in matrix:
        A[m[0]-1][m[1]-1] = m[2]

    for k in range(total):
        for i in range(total):
            for j in range(total):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]

    






    return 

if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    