def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    inf = float('inf')
    D = [[inf] * total for row in range(total)] #建立D矩陣，inf代表無限
    P = [[-1] * total for row in range(total)]  #建立P矩陣
    homework_5.traval = ""                      #建立經過的節點字串
    pathnums = len(matrix)
    for i in range(pathnums):                   #將matrix中的路徑加入到D矩陣中
       D[matrix[i][0]-1][matrix[i][1]-1] = matrix[i][2]
       
    for k in range(total):                      
        for i in range(total):
            for j in range(total):
                if D[i][k] + D[k][j] < D[i][j]: #尋找更短的路徑
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = k                 #將中轉站加入到P矩陣
            
    if D[start-1][end-1] == inf:                #若起點到終點為inf，則沒有路徑
        return [-1,None]
   

    return [D[start-1][end-1],str(start)+Path(start-1,end-1,P)+str(end)]

def Path(start,end,P):
    if P[start][end] != -1:                     #若P上位置等於-1，則代表沒有中轉站
        Path(start,P[start][end],P)             #若有中轉站則尋找起點與中轉站之間有沒有中轉站
        homework_5.traval = homework_5.traval + str(P[start][end]+1)
        Path(P[start][end],end,P)               #若有中轉站則尋找終點與中轉站之間有沒有中轉站
    return homework_5.traval

if __name__ == '__main__':
    matrix = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12], [11, 12, 13], [12, 13, 14], [13, 14, 15], [14, 15, 16], [15, 16, 17]]
    start = 1;end = 15; total = 16
    print(homework_5(matrix, start, end, total))
    