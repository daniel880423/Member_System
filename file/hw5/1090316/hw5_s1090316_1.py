def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。

    n=total
    A=[]
    path=[]
    for i in range(total):
        row=[]
        row_path=[]
        for j in range(total):
            row_path.append(-1)
            if i!=j:
                row.append(float("inf"))
            else:
                row.append(0)
        A.append(row)
        path.append(row_path)
    for m in matrix:
        A[m[0]-1][m[1]-1]=m[2]
    for i in A:
        print(i)
    for k in range(n):
        for i in range(n):
            for k in range(n):
                if A[i][k]+A[k][j]<A[i][j]:
                    A[i][j]=A[i][k]+A[k][j]
                    path[i][j]=k-1

    return A

if __name__ == '__main__':
    matrix = [[1,2,2],[1,3,1],[1,4,5],[3,4,2],[4,5,1]]
    start = 2;end = 4; total = 5
    print(homework_5(matrix, start, end, total))