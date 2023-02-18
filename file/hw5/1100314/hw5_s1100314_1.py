def path(p, start, end):
    global ans #對照第26行
    if start >= 0 and end >= 0: #矩陣最小為0
        if p[start][end]>=1:
            path(p, start, p[start][end]-1)
            ans = ans + str(p[start][end])  #遞迴呼叫，直到沒有中斷點
            path(p, p[start][end]-1, end)
def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    p = [[-1]*total for i in range(total)] #建立P矩陣
    A = [[float("inf")]*total for i in range(total)] #建立A矩陣
    l = len(matrix) #藉matrix長度來抓起點 終點 位移長，並放入A矩陣
    for m in range(l):
        i = matrix[m][0]
        j = matrix[m][1]
        k = matrix[m][2]
        A[i-1][j-1] = k
    for i in range(total): #自己到自己的位移為0
        A[i-1][i-1] = 0
    for k in range(total): #判斷加入中斷點後位移是否比原本位移小，若有則改變A矩陣內容，並於P中記錄K值
        for i in range(total):
            for j in range(total):
                 if (A[i][k] + A[k][j] < A[i][j]):
                    A[i][j] = A[i][k] + A[k][j]
                    p[i][j] = k+1 #因K一開始為0，故要+1
    global ans #讓該段程式以外還能繼續用ans變數
    start = start-1 #矩陣內是從0開始，故要-1
    end = end-1
    if p[start][end] != -1:
        ans = str(start+1)
        ans_2 = path(p, start, end) #計算所有的中斷點
        ans_2 = ans + str(end+1) #補上終點
    else:
        return [-1,None]
    return [A[start][end], ans_2]

    










if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    