def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    n = total
    A = []
    path = []
    for i in range(total):
        row = []
        row_path = []
        for j in range(total):
            row_path.append(-1)
            if i!=j:
                row.append(float("inf"))
            else:
                row.append(0)
        A.append(row)
        path.append(row_path)

    for m in matrix:
        A[m[0]-1][m[1]-1] = m[2]
    
    for i in A:
        print(i)
    # print(path)
    for k in range(n):
        for i in range(n):
            for k in range(n):
                if A[i][k]+A[k][j] < A[i][j]:
                    A[i][j] = A[i][k]+A[k][j]
                    path[i][j] = k -1
      
    ss = start-1
    ee = end -1
    a = getpath(ss,ee,path)

    




    return a
def getpath(ss,ee,path):
    s = []
    if path[ss][ee] != -1:
        getpath(ss,path[ss][ee],path)
        a = 0
        a += path[ss][ee]
         
        getpath(path[ss][ee],ee,path)
        s.append(a)

    else:
        
        a = -1
        b = None
        s.append(a)
        s.append(b)
    return s



if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    