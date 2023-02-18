def homework_5(matrix, start, end, total): 
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    path=[[-1]*total for p in range(total)] #存取節點中插入的中轉點
    inf = float('inf')      #無限大
    A=[[inf]*total for a in range(total)]   #存取節點到節點間的路徑
    for i in range(total):
        A[i][i]=0           #自己走到自己路徑是0
    for i in range(len(matrix)):
        A[matrix[i][0] - 1][matrix[i][1] - 1] = matrix[i][2] #讀取輸入的matrix將路徑長依據起點和終點放進A矩陣
    for k in range(total):  #中轉點 k
        for i in range(total):  #循環矩陣的 row
            for j in range(total):  #循環矩陣的 column
                if (A[i][k]+A[k][j] < A[i][j]):   #中轉點路徑比原本路徑小，進入判斷式
                    A[i][j] =A[i][k] + A[k][j]
                    #A[i][j] = min(A[i][j], A[i][k] + A[k][j])   #替換矩陣路徑距離
                    path[i][j]=k+1  #添加中轉點k+1至path
    i=start-1
    j=end-1
    out_val=A[i][j]
    ans=path[i][j]
    out_path=""
    while ans!=-1:                  #中轉點 != -1，-1代表ans沒有更短的路徑
        out_path=str(ans)+out_path
        ans=path[i][ans-1]    #尋找起始位置ans中間是否有中轉點，有的話代表他前面還有節點需要走訪
    ans=path[i][j]
    while ans!=-1:                  #中轉點 != -1，-1代表ans沒有更短的路徑
        ans=path[ans-1][j]          #尋找ans到end中間是否有中轉點
        if ans!=-1:
            out_path+=str(ans)
    out_path=str(start)+out_path+str(end)         #把起始位置加進字串，結束位置加進字串                 
    if out_val==inf or out_val==0:                #假如start到達不了end，最短距離return-1，經過節點 return None。
        return [-1,None]

    return [out_val,out_path]

if __name__ == '__main__':
    matrix=[[1, 10, 1], [10, 3, 1], [1, 2, 10], [1, 4, 10], [2, 4, 5], [3, 1, 2], [1, 3, 3], [3, 4, 4]]
    start=1 ; end=4; total=10
    print(homework_5(matrix, start, end, total))
    