from math import inf


def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    global node #定義全域變數node
    node =''    #定義node為空字串
    A = [[float('inf') for i in range(total)] for j in range(total)] #初始化A矩陣大小為total*total，矩陣裡每個位置皆為無限大。
    path = [[-1 for i in range(total)] for j in range(total)]        #初始化path矩陣大小為total*total，矩陣裡每個位置皆為-1。
    
    for m in range(total):                                    #m代表A矩陣的列數從 0~total-1
        for n in range(total):                                #n代表A矩陣的行數從 0~total-1
            for k in matrix:                                  #k代表matrix從index 0~最後代表的list
                if k[0] == m+1 and k[1] == n+1:               #如果k裡 index 0的值和 m+1相等且k裡 index 1的值和 n+1相等
                    A[m][n] = k[2]                            #A矩陣m列n行值更改為k裡 index 2的值，代表節點m+1和n+1有路徑相連。

    for k in range(total):                                    #k代表中轉點從 0~total-1
        for i in range(total):                                #i代表起點從 0~total-1
            for j in range(total):                            #j代表終點從 0~total-1
                if (A[i][k] + A[k][j]) < A[i][j]:             #如果從i開始經過中轉點k再到j經過的路徑長小於從i開始到j經過的路徑長
                    A[i][j] = min(A[i][j], A[i][k] + A[k][j]) #A矩陣存取從i到j的路徑長更新為(從i開始經過中轉點k再到j經過的路徑長和從i開始到j經過的路徑長)兩者之最小值。
                    path[i][j] = k                            #path矩陣從i到j新增中轉點k
    ans_path = A[start-1][end-1]                              #最短路徑經由A矩陣中第start-1列和第end-1行交點之值求得(-1是因為index從0開始)


    def getpath(l, p):                                        #getpath這個函式用來把從起點至終點最短路徑經過之節點紀錄在node字串裡，利用遞迴方式求得中間節點。
        global node                                           #定義全域變數node
        if path[l][p] != -1:                                  #如果path矩陣裡的值不等於-1，代表有中轉點存在。
            getpath(l, path[l][p])                            #呼叫自己代入起點和中轉點去找中間是否還有其他中轉點
            node += str((path[l][p])+1)                       #如果沒有其他中轉點，把當前中轉點+1再存入node。
            getpath(path[l][p], p)                            #呼叫自己代入中轉點和終點去找中間是否還有其他中轉點

    getpath(start-1, end-1)                                   #在homework_5中呼叫getpath函式
    ans_str = str(start)+ str(node) + str(end)                #配合回傳值格式在前方加上起點並在後方加上終點
    if A[start-1][end-1] == float('inf'):                     #如果A矩陣中第start-1列和第end-1行交點之值等於無限大，代表起點到終點不存在任何路徑可到達。
        ans_str = None                                        #中間節點為None
        ans_path = -1                                         #最短路徑設為-1
    ans_lst = [ans_path, ans_str]                             #最終回傳的答案為一個list包含最短路徑和中間節點
    return ans_lst                                            #回傳ans_lst



if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,3],[2,1,2],[3,4,4]]
    start = 2;end = 3; total = 4
    print(homework_5(matrix, start, end, total))
    