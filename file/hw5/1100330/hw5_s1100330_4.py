def homework_5(matrix, start, end, total):
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
    
    distance = A[start-1][end-1]

    global node 
    if distance == float('inf') or start == end:
        distance = -1
        node = None
    else:
        node = str(start)
        
        def getpath(Start, End):
            if path[Start][End] != -1:
                global node
                getpath(Start, path[Start][End])
                node += str(path[Start][End] + 1)
                getpath(path[Start][End], End)

        getpath(start-1, end-1)
        node += str(end)

    

    return [distance, node]


    
if __name__ == '__main__':
    matrix =   [[1,2,2],[1,3,1],[1,4,5],[3,4,2],[4,5,1]]
    start = 2;end = 4; total = 5
    print(homework_5(matrix, start, end, total))