def path(p,start,end): #佛洛伊德遞迴function找出最短路徑
    global ans
    if start>=0 and end>=0:
        if p[start][end]>=1 :
            path(p,start,p[start][end]-1)
            ans = ans + str(p[start][end])
            path(p,p[start][end]-1,end)


def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    if start == end:
        return [-1,None]
    p = [[-1]*total for _ in range(total)] #創p矩陣
    a = [[float("inf")]*total for _ in range(total)] #創a矩陣
    l = len(matrix)
    for m in range(l):     #將各節點路徑的距離放進a矩陣
        i = matrix[m][0]
        j = matrix[m][1]
        k = matrix[m][2]
        a[i-1][j-1] = k
    for i in range(total):  #節點到節點本身距離為0
        a[i-1][i-1] = 0
    for k in range(total):    #計算並比較原本距離和經過中節點距離的最小值為何，將最小值代入a矩陣，並改變p矩陣的中節點
        for i in range(total):
            for j in range(total):
                if (a[i][k] + a[k][j] < a[i][j]):
                    a[i][j] = a[i][k] + a[k][j]
                    p[i][j] = k+1
    
    print(p)
    global ans 
    if p[start-1][end-1]!=-1: #找出最短路徑後，並按照老師要求格式給答案。
        ans = str(start)
        anss = path(p,start-1,end-1)
        anss = ans + str(end)
    else:
        return [-1,None]
    return [a[start-1][end-1],anss]


if __name__ == '__main__':
    matrix =  [[1, 10, 1], [10, 3, 1], [1, 2, 10], [1, 4, 10], [2, 4, 5], [3, 1, 2], [1, 3, 3], [3, 4, 4]]
    start = 1;end = 4; total = 10
    print(homework_5(matrix, start, end, total))
    