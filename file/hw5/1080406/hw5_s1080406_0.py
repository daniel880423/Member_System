import numpy as np    
def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    path = np.zeros((total,total)).astype(int)      #製造path矩陣
    A = np.zeros((total,total)).astype(int)     #製造A矩陣，類型為int
    inf = 9999999
    for i in range(total):              #path矩陣的值設為全部-1
        for j in range(total):
            path[i][j] = -1

    for i in range(total):              #A矩陣的對角線為0，其他先設定為inf
        for j in range(total):
            if i == j:
                A[i][j] = 0
            else:
                A[i][j] = inf

    for i in range(len(matrix)):                        #將matrix中每一個小矩陣的index[0]作為A的row項，index[1]為col項，因為python的index是從0開始，而題目的點是從1開始，所以讀到的值要減1
        A[matrix[i][0]-1][matrix[i][1]-1] = int(matrix[i][2])#將matrix中小矩陣的index[2]寫入A矩陣中

    for k in range(total):                                  #k為中轉點
        for i in range(total):
            for j in range(total):
                if A[i][k] + A[k][j] < A[i][j]:             #比較中轉點路徑有無比原本路徑短，如果有
                    A[i][j] = min(A[i][j],A[i][k]+A[k][j])  #則將矩陣中路徑改變
                    path[i][j] = k                          #該點path矩陣改成中轉點
    i = start-1
    j = end-1
    a = []
    e = [end]
    a.insert(0,start)

    def getpath(i,j):
        if path[i][j] != -1:
            getpath(i,path[i][j])
            a.append(path[i][j]+1) 
        return(''.join(map(str,a+e)))
            
        
    return A[start-1][end-1] ,getpath(i,j)


if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,3],[2,1,2],[3,4,4]]
    start = 2;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    
    