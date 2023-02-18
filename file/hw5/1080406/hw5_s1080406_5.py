import numpy as np    
def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    path = np.zeros((total,total)).astype(int)      #製造path矩陣，類型為int
    A = np.zeros((total,total)).astype(int)     #製造A矩陣，類型為int
    inf = 9999999

    path.fill(-1)             #path矩陣的值設為全部-1
        
    A.fill(inf)
    np.fill_diagonal(A,0)      #A矩陣的對角線為0，其他先設定為inf
    

    for i in range(len(matrix)):                        #將matrix中每一個小矩陣的index[0]作為A的row項，index[1]為col項，因為python的index是從0開始，而題目的點是從1開始，所以讀到的值要減1
        A[matrix[i][0]-1][matrix[i][1]-1] = int(matrix[i][2])#將matrix中小矩陣的index[2]寫入A矩陣中

    for k in range(total):                                  #k為中轉點
        for i in range(total):
            for j in range(total):
                if A[i][k] + A[k][j] < A[i][j]:             #比較中轉點路徑有無比原本路徑短，如果有
                    A[i][j] = min(A[i][j],A[i][k]+A[k][j])  #則將矩陣中路徑改變
                    path[i][j] = k                          #該點path矩陣改成中轉點

    if A[start-1][end-1] == inf or start==end:                            #先判斷如果起點無法到終點，則回傳[-1,'None']
        return [-1,None]

    #列印經過的路徑
    i = start-1     # i為起點減一，符合python的index
    j = end-1       # j為終點減一，符合python的index
    s = [start]     #起點s
    a = []          #路徑a
    e = [end]       #終點e

    def getpath(i,j):
        if path[i][j] != -1:                                #如果path矩陣不為-1，則中間還有中轉點
            getpath(i,path[i][j])                           #將終點改為中轉點，使用遞迴判斷中轉點前還有沒有中轉點
            a.append(path[i][j]+1)                          #使用append函數將路徑紀錄至list中
            getpath(path[i,j],j)                            #使用遞迴函式判斷中轉點後到終點還有無中轉點
        return(''.join(map(str,s+a+e)))                     #將起點、路徑及終點list合併，型態改成string，最後使用join函數將list中的字元合併成一個string
            
        
    return [A[i][j] ,getpath(i,j)]


if __name__ == '__main__':
    matrix = [[2, 1, 6], [2, 3, 8]]
    start = 2;end = 2; total = 3
    print(homework_5(matrix, start, end, total))
    
    