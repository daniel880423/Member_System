def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    if start == end: 
        return[-1, None]
    subway = [] #matrix[i](a, b, c)
    route = []
    for i in range(0,total+1):
        subway.append([float("inf")]*(total+1)) 
        route.append([-1]*(total+1)) 
    for i in range(1,total+1):
        subway[i][i] = 0 #節點離自己的距離為0
    for i in matrix:
        subway[i[0]][i[1]] = i[2] #將matrix代入subway
    for k in range(1, total+1):
        for i in range(1, total+1):
             for j in range(1, total+1):
                if (subway[i][k] + subway[k][j] < subway[i][j]): #小於原路徑
                    subway[i][j] = subway[i][k] + subway[k][j] #替換最短路徑
                    route[i][j] = k #中轉點存入route

    final = [subway[start][end], ""] 
    if final[0] == float("inf"): 
        return[-1, None] 

    final[1] = str(start)
    def getroute(i, j): #尋找中轉點
        if (route[i][j] != -1): 
            getroute(i, route[i][j]) 
            final[1] +=str(route[i][j]) 
            getroute(route[i][j], j) 
    getroute(start, end) 
    final[1] += str(end)
    
    return final

if __name__ == '__main__':
    matrix =  [[1,2,2],[1,3,1],[1,4,5],[3,4,2],[4,5,1]]
    start = 2;end = 5; total = 5
    print(homework_5(matrix, start, end, total))