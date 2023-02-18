def homework_5(matrix, start, end, total): 
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    path=[[-1]*total for c in range(total)] #中轉點
    inf = float('inf')      #無限大
    A=[[inf]*total for a in range(total)]   
    for i in range(total):
        A[i][i]=0           #自己走到自己路徑是0
    for d in range(len(matrix)):
        A[matrix[d][0] - 1][matrix[d][1] - 1] = matrix[d][2] #讀取輸入的matrix將路徑長依據起點和終點放進A矩陣
    for k in range(total):  #中轉點 k
        for i in range(total):  #循環矩陣的 row
            for j in range(total):  #循環矩陣的 column
                if (A[i][k]+A[k][j]<A[i][j]):   #中轉點路徑比原本路徑小，進入判斷式
                    A[i][j] = min(A[i][j], A[i][k] + A[k][j])   #替換矩陣路徑距離
                    path[i][j]=k+1  #添加中轉點k至 path

    out_val=A[start-1][end-1]
    ans=path[start-1][end-1]
    out_path=""
    while ans!=-1:                  #中轉點 != -1，-1代表ans沒有更短的路徑
        out_path=str(ans)+out_path
        ans=path[start-1][ans-1]    #尋找起始位置ans中間是否有中轉點，有的話代表他前面還有節點需要走訪
    out_path=str(start)+out_path           #把起始位置加進字串
    out_path+=str(end)                  #把結束位置加進字串
    if out_val==inf:                #假如start到達不了end，最短距離return-1，經過節點 return None。
        return [-1,None]

    return [out_val,out_path]

if __name__ == '__main__':
    matrix = [[30, 31, 1], [30, 32, 1], [30, 34, 2], [31, 34, 2], [32, 34, 2], [34, 35, 3], [34, 36, 3], [35, 37, 2], [36, 37, 1], [37, 38, 5]]
    start = 30;end = 37; total = 38
    print(homework_5(matrix, start, end, total))
    