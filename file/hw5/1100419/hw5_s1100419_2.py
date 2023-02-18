
def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。

    #先設一個矩陣裡面全部放-1
    path=list()
    for i in range(total):
        l=list()
        for j in range(total):
            l.append(-1)
        path.append(l)

    #再設一個矩陣裡面全部放無限大
    a=list()
    for i in range(total):
        b=list()
        for j in range(total):
            b.append(float('inf'))
        a.append(b)

    #依照題目給的兩點之間所需距離放入矩陣
    lenmatrix=len(matrix)
    for i in range(lenmatrix):
        a[matrix[i][0]-1][matrix[i][1]-1]=matrix[i][2]

    #檢查是否為最短路徑
    for k in range (total):
        for i in range (total):
            for j in range (total):
                if (a[i][k] + a[k][j] < a[i][j]):
                    a[i][j] = a[i][k] + a[k][j]
                    path[i][j] = k
    print(a,path)

    #定義一個字串
    global strpath
    strpath=str()

    #將找到的最短路徑中轉點return出來並合併成題目要求的答案形式
    def pathcount(i,j):
        global strpath
        if (path[i][j] != -1):
            pathcount(i, path[i][j])
            strpath += str(path[i][j]+1)
            pathcount(path[i][j], j)
    pathcount(start-1,end-1)
    if a[start-1][end-1]==float('inf'):
        answer=[-1,None]
    else:
        answer=[a[start-1][end-1],str(start)+strpath+str(end)]
    return answer

if __name__ == '__main__':
    matrix = [[1,2,2],[1,3,1],[1,4,5],[3,4,2],[4,5,1]]
    start = 2;end = 5; total = 5
    print(homework_5(matrix, start, end, total))
    