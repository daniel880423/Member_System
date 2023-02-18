def homework_5(matrix, start, end, total):
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    A = [[]]
    path = [[]]
    for i in range(total):
        for j in range(total):
            if i == j:
                A[i].append(0)
            elif i != 0 and j == 0:
                A.append([float('inf')])
            else:
                A[i].append(float('inf'))
    
    for i in matrix:
        a = i[0] - 1
        b = i[1] - 1
        A[a][b] = i[2]

    for i in range(total):
        for j in range(total):
            if i != 0 and j == 0:
                path.append([-1])
            else:
                path[i].append(-1)

    for k in range(total):
        for i in range(total):
            for j in range(total):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
                    path[i][j] = k 
    
    
    if A[start-1][end-1] == float('inf'):
        distance = None
    else:
        distance = A[start-1][end-1]

    nope = str(start)
    tmp = path[start-1][end-1]
    while True:
        if tmp == -1:
            break
        else:
            nope += str(tmp+1)
            tmp = path[tmp][end-1]
    nope += str(end)

    return [distance, nope]

if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))