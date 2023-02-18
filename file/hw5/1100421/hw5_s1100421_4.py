def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    path = [[-1]*total for _ in range(total)]   #設計一個n*n矩陣來填入path
    A = [[0]*total for _ in range(total) ]      #設計一個n*n矩陣來填入初始數對應步數
    for i in range(len(matrix)):    #將題目給的數值及對應步數丟到矩陣A
        if i>=len(matrix):
                break
        for j in range(total):
            tmp_i = matrix[i][j]
            tmp_j = matrix[i][j+1]
            A[tmp_i-1][tmp_j-1] = matrix[i][j+2]
            break
    for i in range(total):      #將A矩陣內不是對角線且數值為零的設為無限大
        for j in range(total):
            if i != j and A[i][j] == 0:
                A[i][j] = float("inf")
    for k in range(total):      #算出最佳距離並將path更新
        for i in range(total):
            for j in range(total):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = min(A[i][k] + A[k][j], A[i][j])
                    path[i][j] = k+1
    lst = [start]   #先將起始點嘉進list
    getpath(start, end, path, lst)      #走遞迴回傳走的順序
    lst.append(end)     #再將結束點加入list
    ans_lst = ""
    for x in lst:   #將list換成str
        ans_lst += str(x)
    step = A[start-1][end-1]
    if step == float("inf") or step == 0:   #如果是0代表是起始點跟終點一樣，inf則代表沒有方法走到終點
        step = -1
        ans_lst = None
    ans_lst = [step, ans_lst]
    return ans_lst

def getpath(start, end, path, lst):
    if path[start-1][end-1] != -1:
        getpath(start, path[start-1][end-1], path, lst)
        lst.append(path[start-1][end-1])
        getpath(path[start-1][end-1], end, path, lst)

if __name__ == '__main__':
    matrix =    [[1,2,1],[1,3,3],[2,1,2],[3,4,4]]
    start = 2; end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    