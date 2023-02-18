from re import A


def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    
    path = list()     #先設一個矩陣
    for i in range(total):
        l = list()
        for j in range(total):
            l.append(-1)    #使矩陣內為-1
        path .append(l)


    a = list()     #再設一個矩陣為無限大
    for i in range(total):
        ls = list()
        for j in range(total):
            ls.append(float('inf'))    #inf為無限大的意思
        a.append(ls)


    length=len(matrix)     #依照題目給的兩點之間所需距離放入矩陣
    for i in range(length):
        a[matrix[i][0]-1][matrix[i][1]-1] = matrix[i][2]


    for k in range(total):        #檢查所有點的距離是否為最短的
        for i in range(total):
            for j in range(total):
                if (a[i][k] + a[k][j] < a[i][j]):
                    a[i][j] = a[i][k] + a[k][j]
                    path[i][j] = k
                    

    global string    #定義一個字串
    string = str()

    
    def count(i,j):         #把所有最短路徑中轉點合併成題目要求的答案形式
        global string
        if (path[i][j] != -1):
            count(i, path[i][j])
            string += str(path[i][j] + 1)
            count(path[i][j], j)
    count(start-1,end-1)
    if a[start-1][end-1]==float('inf'):
        answer=[-1,None]
    else:
        answer=[a[start-1][end-1], str(start) + string + str(end)]
    
    return answer
    
 

if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    