def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。

    v=[[-1]*total for i in range(0,total)]  #先設一個矩陣存步數
    path=[['']*total for i in range(0,total)]  #設一個矩陣暫存經過的節點
    for i in range(total):        
        for j  in range(total):
            if i==j:          #把1到1、2到2....原本的點到原本的點的都先設成部數0
                v[i][j]=0
            else:
                v[i][j]=float("inf")  #其他的先設成無限大
    

    for i in matrix: #把matrix內有的步數先放進存步數的矩陣裡
        v[i[0]-1][i[1]-1]=i[2]
    


    D=v
    me_path=[['']*total for i in range(0,total)]#創一個存經過的節點的
    #Flotd code
    for k in range(total): 
       for i in range(total):
           for j in range(total):
               if (D[i][k]+D[k][j]<D[i][j]):
                    D[i][j] = min(D[i][j], D[i][k] + D[k][j])
                    path[i][j]=str(k+1)
                    me_path[i][j]=path[i][k]+path[k][j]+path[i][j]
    
    if D[start-1][end-1]==float("inf"):   #如果經過以上的Floyd演算法仍是無限大的步數
        D[start-1][end-1]=-1       #就把該點設成-1
        re_path=None       #要回傳經過的節點的矩陣的那格輸出None
    else:
        re_path=str(start)+me_path[start-1][end-1]+str(end)#不是無限大就回傳包刮起使和結束和經過的節點合併的字串




    return [D[start-1][end-1],re_path] #回傳

if __name__ == '__main__':
    """
    matrix = [[1, 2, 1], [1, 3, 1], [3, 4, 1]]
    start = 1; end = 4; total = 4
    
    
    matrix = [[1,2,1],[1,3,3],[2,1,2],[3,4,4]]
    start = 2; end = 4; total = 4
    """
    """
    matrix = [[1,2,2],[1,3,1],[1,4,5],[3,4,2],[4,5,1]]
    start = 2; end = 4; total=5
    """
    matrix = [[1,2,1],        #節點 1 到節點 2 的距離是 1
              [1,3,1],        #節點 1 到節點 3 的距離是 1
              [3,4,1]]        #節點 3 到節點 4 的距離是 1
    start = 1;end = 4; total = 4        #  Output : [2,"134"]   //節點 1 到節點 4 為 1+1=2，經過的節點有 134
    
    print(homework_5(matrix, start, end, total))



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