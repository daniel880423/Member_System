def homework_5(matrix, start, end, total):  # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    inf = float("inf")
    for i in matrix:
        if i[0] > total:
            total = i[0]
        if i[1] > total:
            total = i[1]
    total += 1
    W = [[inf]*total for row in range(total)]
    P = [[-1]*total for row in range(total)]
    i = 0
    j = 0
    k = 0
    while k < len(matrix):
        i = matrix[k][0]
        j = matrix[k][1]
        W[i][j] = matrix[k][2]
        W[k][k] = 0
        k += 1
    D = W
    i = 0
    j = 0
    k = 0
    for k in range(1, total):
        for i in range(1, total):
            for j in range(1, total):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = k


    lst = []
    s=""
    path_s = getpath(lst,start, end, P, D)
    for i in path_s:
        s = s+str(i)
    path_s = str(start)+ s + str(end)
    if D[start][end] == inf:
        D[start][end] = -1
        path_s = None
    lst=[D[start][end], path_s]


    return lst

def getpath(path_s,i, j, P, D):
    if (P[i][j] != -1):
        getpath(path_s,i, P[i][j],P,D)
        path_s.append(P[i][j])
        getpath(path_s,P[i][j], j,P,D)


    return path_s



if __name__ == '__main__':
    matrix = [[1, 2, 1], [1, 3, 3], [2, 1, 2], [3, 4, 4]]
    start = 2
    end = 4
    total = 4
    print(homework_5(matrix, start, end, total))
