def homework_5(matrix, start, end, total): 
    if start == end: 
        return[-1, None]
    W = []                                                  #建立W矩陣存放已知資訊(每個點之間的距離)
    P = []                                                  #建立P矩陣存放點到點之間經過的點
    for i in range(0,total+1):
        W.append([float("inf")]*(total+1))                  #建立一個(total+1)*(total+1)階的W初始矩陣(因為沒有點0)
        P.append([-1]*(total+1))                            #建立一個(total+1)*(total+1)階的P初始矩陣

    for i in range(1,total+1):
        W[i][i] = 0                                         #自己走到自己必為零
    for i in matrix:
        W[i[0]][i[1]] = i[2]                                #將matrix給予的點到點距離存放進W矩陣
    for k in range(1, total+1):                             #以點k作為中轉點
        for i in range(1, total+1):
             for j in range(1, total+1):
                if (W[i][k] + W[k][j] < W[i][j]):           #如果透過中轉點的距離比原路徑小
                    W[i][j] = W[i][k] + W[k][j]             #最短距離更新
                    P[i][j] = k                             #將此中轉點存入p矩陣

    final = [W[start][end], ""]                             #final[0]=start到end的最短距離 final[1]=路徑
    if final[0] == float("inf"):                            #final[0]=inf 也就是並無start到end的路徑就直接回傳[-1, None] 
        return[-1, None] 

    final[1] = str(start)                                   #建立start到end的起點start
    def getpath(i, j):                                      #尋找(i, j)之中的中轉點
        if (P[i][j] != -1):                                 #中轉點!=-1 代表存在中轉點[i][j]
            getpath(i, P[i][j])                             #尋找(i, 中轉點[i][j])之中的中轉點
            final[1] +=str(P[i][j])                         #路徑加上中轉點
            getpath(P[i][j], j)                             #尋找(中轉點[i][j], j)之中的中轉點
    getpath(start, end) 
    final[1] += str(end)
    
    return final
if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))

