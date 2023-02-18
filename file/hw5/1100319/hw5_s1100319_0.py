def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    
    path = [[-1]*(total) for i in range(total)]    #建立path矩陣
    A = [[0]*(total) for i in range(total)]        #建立A矩陣
    
    for i in range (total):
        for j in range (total):
            if i!=j:                                #若矩陣A中的i不等於j
                A[i][j] = float("inf")              #先將其設為inf
                
    n=a=0
    while n < len(matrix):                          #走訪matrix
        b = 0
        A[matrix[a][b]-1][matrix[a][b+1]-1] = matrix[a][b+2] #將裡面的路徑權重加到A矩陣對應的位置
        a+=1
        n+=1
            
    for k in range(total):
        for i in range (total):
            for j in range(total):               
                if A[i][k]+ A[k][j] < A[i][j]:       #若加入中轉點路徑比原本路徑小
                   A[i][j] = min(A[i][j], A[i][k]+ A[k][j])  #替換A矩陣路徑距離
                   path[i][j] = k                    #添加中轉點k至path矩陣
    
    s = start-1
    e = end-1
    global total_path
    total_path = str('')

    def getpath(start,end,path):
        global total_path 
        if path[start][end] != -1:                  #若中轉點不等於-1(有更短的路徑)           
            getpath(start,path[start][end],path)    #尋找起點到中轉點之間是否還有中轉點
            p = path[start][end]
            total_path = total_path + str(p+1)      #印出所有經過的中轉點     
            getpath(path[start][end],end,path)      #尋找中轉點到終點之間是否還有中轉點
            return total_path                       
            
        else:                                       #若中轉點等於-1(沒有更短的路徑)
            return None 
    
    get = getpath(s,e,path)
    if A[start-1][end-1] == float("inf"):
        A[start-1][end-1] = -1
    if get == None:
        get_path = None
    else:
        get_path = str(start)+get+str(end)          #將所有經過的中轉點前後加上起點及終點
    lst = (A[start-1][end-1],get_path)
       
    return list(lst)
    
    
    
if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,3],[2,1,2],[3,4,4]]
    start = 2;end = 4; total = 4
    print(homework_5(matrix, start, end, total)) 