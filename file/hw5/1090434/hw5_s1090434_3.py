def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    import numpy as np
    INF=999
    O=[0, ''] #output
    def sol(start, end):
        stri=''
        stri+=str(start)
        if P[start-1][end-1]!=-1:
            stri+=str(k)
            O[0]+=A[start-1][k]
            stri+=str(end)
        else:
            O[0]=-1
        O[1]=stri
        return O
    A=np.zeros(shape=(total,total))
    P=np.zeros(shape=(total,total))
    for a in range(total):
        for b in range(total):
            P[a][b]=None
    for a in range(total):
        for b in range(total):
            A[a][b]=INF
    for a in range(len(matrix)):
        A[matrix[a][0]-1][matrix[a][1]-1]=matrix[a][2]
    for k in range(total):
        for i in range(total):
            for j in range(total):
                if A[i][k]+A[k][j]<A[i][j]:
                    A[i][j]=min(A[i][j], A[i][k]+A[k][j])
                    P[i][j]=k
    return sol(start, end)

if __name__ == '__main__':
    matrix = [[1, 2, 2], [1, 3, 1], [1, 4, 5], [3, 4, 2], [4, 5, 1]]
    start = 2;end = 5; total = 5
    print(homework_5(matrix, start, end, total))
    