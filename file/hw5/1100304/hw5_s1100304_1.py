def homework_5(matrix, start, end, total): 
    def getPath(i, j):                                     #紀錄路徑
        if path[i][j] != -1:                               #
            getPath(i, path[i][j])                         #
            getPath(path[i][j], j)                         #
        else:                                              # 
            ste.append(j+1)                                #
            return ste                                     #
                                                 
    inf = 99999                                            
    dis = []  
    path = []     
    ste = []                                               #紀錄路徑的list
    lst = []                                               #最後ANS
                                         
    for i in range(total):                                 #紀錄最短路徑的矩陣
        dis += [[]]                                        #
        for j in range(total):                             #
            if i == j:                                     #
                dis[i].append(0)                           #
            else:                                          #
                dis[i].append(inf)                         #

    for i in range(total):                                 #紀錄路徑的矩陣
        path += [[]]                                       #
        for j in range(total):                             #
            path[i].append(-1)                             #
    
    for i in range(len(matrix)):                           #將輸入的矩陣套到dis
        u, v, w = matrix[i][0], matrix[i][1], matrix[i][2] #
        dis[u-1][v-1] = w                                  #

    for i in range(total):                                 #計算最短路徑
        for j in range(total):                             #
            for k in range(total):                         #
                if dis[i][j] > dis[i][k] + dis[k][j]:      #
                    dis[i][j] = dis[i][k] + dis[k][j]      #
                    path[i][j] = k                         #

    if dis[start-1][end-1] != 99999:                       #若有最短路徑 ==> 回傳[路徑長,路徑]
        getPath(start-1, end-1)   
        step = str(start)
        for i in range(len(ste)):
            step += str(ste[i])
            
        lst = [dis[start-1][end-1], step]
        return lst
    else:
        lst = [-1,None]                                    ##若無最短路徑 ==> 回傳[-1,None]
        return lst

if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,3],[2,1,2],[3,4,4]]; start = 2; end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    