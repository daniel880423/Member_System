def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    ##創建需要用到的變數
    path=[]
    A=[]
    name=[]
    pp=[]
    nnaa=''

    ## 1.創造矩陣 A 與 path
    ## 2.矩陣A全部設為無限
    ## 3.矩陣path全部設為-1
    for k in range(total):
        path.append([])
        A.append([])
        for j in range(total):
            path[k].append(-1)
            if k==j:
                A[k].append(0)
            else:
                A[k].append(float("inf"))

    ## 矩陣A填入輸入的特定節點距離
    for i in matrix :
        A[i[0]-1][i[1]-1]=i[2]

    ##矩陣A中的距離作比較
    ##比較後確定比較小再存進去，並利用path紀錄當前中轉點
    for k in range (total):
        for i in range (total):
            for j in range (total):
                if (A[i][k]+A[k][j])<A[i][j]:
                    A[i][j]=min(A[i][j],(A[i][k] + A[k][j]))
                    path[i][j]=k

    ##紀錄經過節點
    def getpath(i,j,path,nn):
        if (path[i][j]!=-1):
            getpath(i,path[i][j],path,nn)
            nn.append(str(path[i][j]+1))
            getpath(path[i][j],j,path,nn)
    
    getpath(start-1,end-1,path,name)
    ##設定特定的中止條件
    if A[start-1][end-1]==float("inf") or A[start-1][end-1]==0:
        return [-1,None]

    ##結合所有經過節點
    for i in name:
        nnaa=nnaa+str(i)
    ##統整到一個list中
    pp.append( A[start-1][end-1])
    pp.append(str(start)+nnaa+str(end))
    ##回傳
    return pp

if __name__ == '__main__':
    matrix = [[2, 1, 6], [2, 3, 8]]
    start = 2;end = 2; total = 3
    print(homework_5(matrix, start, end, total))
    
