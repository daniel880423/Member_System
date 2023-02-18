def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    W = [[float("inf")]*total for x in range(total)]   #預設(節點數)*(節點數)大小的矩陣
    P = [[-1]*total for y in range(total)]             #預設路徑矩陣
    for i in range(0,len(matrix)):                     #將matrix中各節點間的距離記錄在W中
        start_point = matrix[i][0]-1
        end_point = matrix[i][1]-1
        W[start_point][end_point] = matrix[i][2]
    for k in range(0,total):                           #找出各節點間最短距離
        for j in range(0,total):
            for l in range(0,total):
                if  (W[j][k]+W[k][l]<W[j][l]):         #判斷新路徑是否比原路徑短
                    W[j][l] = W[j][k]+W[k][l]          
                    P[j][l] = k                        #紀錄中轉點
    global path                                        #設定全域變數path
    path = ""                                          #path為空字串
    getpath(P,start-1,end-1)                           #找出路徑中經過的節點
    if path != "":
        path = str(start)+path+str(end)                #補上起點與終點
    else:
        path = None
    ans = []                                           #設定ans為一個空list
    distance = W[start-1][end-1]                       
    if distance == float("inf") :                      #start到不了end，無路徑
        distance = -1                                  #設定距離為-1
    ans.append(distance)                               #將start到end的距離加入ans
    ans.append(path)                                   #將start到end的路徑加入ans

    return ans


def getpath(P,start,end):
    global path
    if P[start][end] != -1 :                           #若start與end間有路徑
        getpath(P,start,P[start][end])                 #搜尋起點到中間是否還有其他節點
        path += str(P[start][end]+1)                   #將搜尋到的節點加入路徑中
        getpath(P,P[start][end],end)                   #搜尋中間到終點是否還有其他節點
      



if __name__ == '__main__':
    matrix =[[1,2,2],[1,3,1],[1,4,5],[3,4,2],[4,5,1]]
    start = 2;end = 5; total = 5
    print(homework_5(matrix, start, end, total))

