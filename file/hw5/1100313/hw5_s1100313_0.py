def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    path=[]
    for i in range(0, total):
        path2=[]
        for j in range(0, total):
            path2.append(-1)
        path.append(path2)

    A=[]
    for i in range(0, total):
        A2=[]
        for j in range(0, total):
            A2.append(float("inf"))
        A.append(A2)

    for a in range(0, total):
        for b in range(0, total):
            for c in matrix:
                if c[0]==a+1 and c[1]==b+1:
                    A[a][b]=c[2]

    for k in range(0, total):
        for i in range(0, total):
            for j in range(0, total):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = min(A[i][j], A[i][k] + A[k][j])
                    path[i][j] = k
    ans=A[start-1][end-1]    
    if ans==float("inf"):
        return[-1, None]
    global ans2
    ans2=str()
    def getpath (i, j):
        if path[i][j] != -1:
            getpath(i, path[i][j])
            global ans2
            ans2 += (str(path[i][j]+1))
            getpath(path[i][j], j)
    getpath(start-1, end-1)
    return [ans, str(start)+ans2+str(end)]
    
        


if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    