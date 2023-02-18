def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    inf = float('Inf')
    A = []
    path = []
    list = []
    
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

    # for i in path:
    #     print(path)

    for m in matrix:
        A[m[0]-1][m[1]-1] = m[2]

    for k in range(total):
        for i in range(total):
            for j in range(total):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
                    path[i][j] = k

    for i in A:
        for j in A:
            d = A[start-1][end-1] 

    global nodes
    if d == float("inf") or start == end:
        d = -1
        nodes = None
    else:
        nodes = str(start)
        def getpath(Start, End):
            if path[Start][End] != -1:
                global nodes
                getpath(Start, path[Start][End])
                nodes += str(path[Start][End]+1)
                getpath(path[Start][End], End)
            
        
        getpath(start-1, end-1)
        nodes += str(end)

    

    return [d, nodes]

    # for i in path:
    #     for j in path:
    #         if path[i][j] != -1:
    #             t = str(path[start-1][[path[start-1][end-1]]-1])
    #             t = t + str(end)
    #         list.append(t)




if __name__ == '__main__':
    matrix = [[1, 2, 1], [1, 3, 1], [3, 4, 1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    