def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    L = len(matrix)                             #L為矩陣長度
    
    A = tran_matrix(matrix,L,total)             #A為轉換後的矩陣

    if start == end:                            #如果起始點等於終點，進入判斷式
        return [-1,None]                        #回傳[-1,None]
    #預設path矩陣
    path = [[-1]*total for i in range(total)]   #path預設一個total*total全為-1的矩陣
    #佛洛伊德最短路徑
    for k in range(0,total):                    #中轉點 k                  
        for i in range(0,total):                #循環矩陣的 row
            for j in range(0,total):            #循環矩陣的 column
                if A[i][k]+A[k][j]<A[i][j]:     #如果加上中轉點後，其路徑比原本路徑小，進入判斷式
                    A[i][j] = A[i][k]+A[k][j]   #將原本路徑距離改為加上中轉點後的路徑距離
                    path[i][j] = k              #添加中轉點k至 path
    #路徑長為無限，直接回傳，不需要抓取中轉點
    if(A[start-1][end-1]==float("inf")):    #如果起始點與終點的路徑長為無限，進入判斷式
        return [-1,None]                    #回傳[-1,None]
    #抓取中轉點
    global ans                              #宣告全域變數ans
    ans = ""                                #其值為空字串
    def getpath(path,i,j):
        global ans                          #此function會用到全域變數ans
        if(path[i][j]!=-1):                 #如果中轉點不是-1，進入判斷式(-1代表i~j沒有更短的路徑)
            getpath(path,i,path[i][j])      #查看i~中轉點是否還有更短的路徑
            ans+=str(path[i][j]+1)          #將經過的中轉點加到ans中
            getpath(path,path[i][j],j)      #開始查看中轉點~j是否還有更短的路徑
    #回傳
    getpath(path,start-1,end-1)             #運行getpath function
    ans2 = str(start)+ans+str(end)          #將ans(經過的中轉點)加上起始點與終點
                           
    return [A[start-1][end-1] ,ans2]#回傳路徑長與經過的點

def tran_matrix(matrix,L,total):#此function用來轉換矩陣
    #第一步：預設新矩陣
    tran_matrix = [[0]*total for i in range(total)]                 #tran_matrix預設一個total*total全為0的矩陣
    #第二步：將系統給的數值(路徑長)，加入對應的矩陣位置
    for i in range(0,L):
        tran_matrix[matrix[i][0]-1][matrix[i][1]-1] = matrix[i][2]  #將給定的對應數字的路徑長度加進去
    #第三步：將矩陣位置中沒有路徑長的數值改為無限
    for i1 in range(0,total):
        for j in range(0,total):                                    
            if i1!=j and tran_matrix[i1][j]==0:                     #假如不在矩陣的對角線，其值卻是0的，進入判斷式
                    tran_matrix[i1][j]=float("inf")                 #將其值改為無限

    return tran_matrix                                              #將轉換後的矩陣回傳

if __name__ == '__main__':
    matrix = [[2, 1, 6], [2, 3, 8]]
    start = 2;end = 2; total = 3
    print(homework_5(matrix, start, end, total))
    