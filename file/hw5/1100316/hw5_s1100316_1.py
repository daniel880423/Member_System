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
                if (a[i-1][k-1] + a[k-1][j-1] < a[i-1][j-1]):
                    a[i-1][j-1] = min(a[i-1][j-1], a[i-1][k-1] + a[k-1][j-1])
                    p[i-1][j-1] = k
    if a[start-1][end-1] == float("inf"): #假如起點到達不了終點，回傳None
        return [-1,None]
    an = a[start-1][end-1]     #將答案從矩陣取去放進新陣列，並按照老師要求的規格印出答案
    pos = [str(start)]
    print(p)
    for i in range(end):
        if (p[start-1][i] != -1):
            pos.append(str(p[start-1][i]))
    pos.append(str(end))
    pos = ''.join(pos)
    ans = [an,pos]



    return ans

if __name__ == '__main__':
    matrix =  [[1,2,1],[1,3,3],[2,1,2],[3,4,4]]
    start = 2;end = 3; total = 4
    print(homework_5(matrix, start, end, total))
    