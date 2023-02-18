def homework_5(matrix, start, end, total): 
    def getPath(i, j):                                     #紀錄路徑
        if path[i][j] == -1:   
            ste.append(j+1)                          
            return ste                                  
        else:                                           
            getPath(i, path[i][j])                     
            getPath(path[i][j], j)                      
                                      
    inf = 99999                                            
    dis = []  
    path = []     
    ste = []                                               #紀錄路徑的list
    lst = []                                               #最後ANS                            
    for i in range(total):                                 #紀錄最短路徑的矩陣
        dis += [[]]                                        
        for j in range(total):                             
            if i == j:                                     
                dis[i].append(0)                           
            else:                                          
                dis[i].append(inf)                         

    for i in range(total):                                 #紀錄路徑的矩陣
        path += [[]]                                       
        for j in range(total):                             
            path[i].append(-1)                             
    
    for i in range(len(matrix)):                           #將輸入的矩陣套到dis
        u, v, w = matrix[i][0], matrix[i][1], matrix[i][2] 
        dis[u-1][v-1] = w                                  

    for k in range(total):                                 #計算最短路徑
        for i in range(total):                             
            for j in range(total):                         
                if dis[i][j] > (dis[i][k] + dis[k][j]):      
                    dis[i][j] = dis[i][k] + dis[k][j]
                    path[i][j] = k

    for i in range(total):                         
        for j in range(total):        
            if (start != end) and (dis[start-1][end-1] != inf): #若有最短路徑 ==> 回傳[路徑長,路徑]
                getPath(start-1, end-1)
                step = str(start)
                for k in range(len(ste)):
                    step += str(ste[k])
                lst = [dis[start-1][end-1], step]
                return lst

            elif (start == end) or (dis[start-1][end-1] == inf):#若無最短路徑 ==> 回傳[-1,None]
                lst = [-1,None]                                  
                return lst

if __name__ == '__main__':
    matrix = [[3, 6, 3], [3, 9, 1], [9, 6, 1], [12, 3, 2], [12, 9, 3]]; start = 12; end = 6; total = 12
    print(homework_5(matrix, start, end, total))
    