import numpy as np
def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    #路徑從頭開始
    path = ""
    path += str(start)
    inf = 65535
    dp = np.zeros((total+1,total+1))
    #將權重放入矩陣
    for i in matrix:
        dp[i[0]][i[1]]=i[2]
    #將沒有的路徑用無限權重來表示
    for i in range(1,len(dp)):
        for j in range(1,len(dp)):
            if i==j:
                dp[i][i]=0
            elif (dp[i][j]==0):
                dp[i][j]=inf
    #動態規劃
    for k in range(1,total+1):
        for i in range(1,total+1):
            for j in range(1,total+1):
                if(dp[i][k]+dp[k][j]<dp[i][j]):
                    if(i==start):
                        path+=str(k)
                    dp[i][j]=dp[i][k]+dp[k][j]
    #路徑結尾
    if (path[-1]!=str(end)):
        path+=str(end)
    #如果沒路徑
    if (dp[start][end]==inf):
        return [-1,None]
    



    return [int(dp[start][end]),path]

if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    