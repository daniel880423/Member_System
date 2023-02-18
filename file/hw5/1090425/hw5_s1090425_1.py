def homework_5(matrix, start, end, total):
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    inf = float("inf")
    total+=1                                      #因為python的index從0開始
    W = [[inf]*total for row in range(total)]     #建立相鄰矩陣，以無窮為初始值
    P = [[-1]*total for row in range(total)]      #建立節點矩陣
    i = 0
    j = 0
    k = 0
    for k in range (0,len(matrix)):
        i = matrix[k][0]                          #matrix[k][0]是起點
        j = matrix[k][1]                          #matrix[k][1]是起點
        W[i][j] = matrix[k][2]                    #將其距離存入W取代無窮
                                                  
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
    matrix = [[1, 2, 5], [2, 3, 1], [2, 5, 4], [3, 4, 3], [4, 6, 5], [6, 7, 2], [2, 6, 8], [5, 7, 5], [6, 8, 2], [7, 9, 4], [8, 9, 12], [9, 10, 10], [9, 11, 2], [10, 11, 2], [11, 12, 2]]
    start = 6
    end = 12
    total = 12
    print(homework_5(matrix, start, end, total))
