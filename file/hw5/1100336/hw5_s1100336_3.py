def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    if start==end:   #如果start=end直接return[-1,None]
        return[-1,None]

    global re_path

    D=[[-1 for j in range(total)] for i in range(0,total)]  #先設一個矩陣存步數
    path=[[-1 for j in range(total)] for i in range(0,total)]  #設一個矩陣暫存經過的節點

    for i in range(total):        
        for j  in range(total):
            if i==j:          #把1到1、2到2....原本的點到原本的點的都先設成部數0
                D[i][j]=0
            else:
                D[i][j]=float("inf")  #其他的先設成無限大
    

    for i in matrix: #把matrix內有的步數先放進存步數的矩陣裡
        D[i[0]-1][i[1]-1]=i[2]
    


    
    me_path=[['']*total for i in range(0,total)]#創一個存經過的節點的
    #Flotd code
    for k in range(total): 
        for i in range(total):
            for j in range(total):
                if (D[i][k]+D[k][j]<D[i][j]):
                    D[i][j] = min(D[i][j], D[i][k] + D[k][j])
                    path[i][j]=k
                        
    if D[start-1][end-1]==float("inf"):   #如果經過以上的Floyd演算法仍是無限大的步數
        D[start-1][end-1]=-1       #就把該點設成-1
        re_path=None       #要回傳經過的節點的矩陣的那格輸出None
        return [-1,None]
    
    re_path = str()      
    def getpath(i, j):      #Floyd path recursive code
        global re_path
        if path[i][j] != -1:
            getpath(i, path[i][j])
            re_path += str(path[i][j]+1)
            getpath(path[i][j], j)
    getpath(start-1, end-1)




    return [D[start-1][end-1],str(start)+re_path+str(end)] #回傳

if __name__ == '__main__':
    """
    matrix = [[1, 2, 1], [1, 3, 1], [3, 4, 1]]
    start = 1; end = 4; total = 4
    
    
    matrix = [[1,2,1],[1,3,3],[2,1,2],[3,4,4]]
    start = 2; end = 4; total = 4
    
    
    matrix = [[1,2,2],[1,3,1],[1,4,5],[3,4,2],[4,5,1]]
    start = 2; end = 4; total=5
    """"""
    matrix = [[1,2,1],        #節點 1 到節點 2 的距離是 1
              [1,3,1],        #節點 1 到節點 3 的距離是 1
              [3,4,1]]        #節點 3 到節點 4 的距離是 1
    start = 1;end = 4; total = 4 """       #  Output : [2,"134"]   //節點 1 到節點 4 為 1+1=2，經過的節點有 134
    
    matrix=[[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12], [11, 12, 13], [12, 13, 14], [13, 14, 15], [14, 15, 16], [15, 16, 17]]
    start=1;end=15;total=16	
    #[133, '123456789101112131415']
    # 
    print(homework_5(matrix, start, end, total))


    """
[[[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12], [11, 12, 13], [12, 13, 14], [13, 14, 15], [14, 15, 16], [15, 16, 17]], 1, 15, 16]	[-1, None]	[133, '123456789101112131415']


"""
    """      -1=None
         (1)   (2)   (3)   (4)
    (1)   0     1     1    -1
    (2)  -1     0    -1    -1
    (3)  -1    -1     0     1
    (4)  -1    -1    -1     0
    
    """
    """     路徑長  (-1=None)
         (1)   (2)   (3)   (4)
    (1)   0     1     1     2
    (2)  -1     0    -1    -1
    (3)  -1    -1     0     1
    (4)  -1    -1    -1     0
    
    """

    """      中間點  (-1=None)
         (1)   (2)   (3)   (4)
    (1)   0     0     0     2
    (2)  -1     0    -1    -1
    (3)  -1    -1     0     0
    (4)  -1    -1    -1     0
    
    """
"""
------------------------顯示錯誤題目-------------------------
第1題答錯了!
答錯的題目:[[[1, 2, 1], [1, 3, 1], [3, 4, 1]], 1, 4, 4]
您的答案:IndexError:list assignment index out of range
============================================
第2題答錯了!
答錯的題目:[[[1, 2, 2], [1, 3, 1], [1, 4, 5], [3, 4, 2], [4, 5, 1]], 2, 5, 5]
您的答案:IndexError:list assignment index out of range
============================================
第3題答錯了!
答錯的題目:[[[1, 2, 1], [1, 3, 3], [2, 1, 2], [3, 4, 4]], 2, 4, 4]
您的答案:IndexError:list assignment index out of range
============================================
第4題答錯了!
答錯的題目:[[[1, 2, 1], [1, 3, 3], [2, 1, 2], [3, 4, 4]], 2, 3, 4]
您的答案:IndexError:list assignment index out of range
"""