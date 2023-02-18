def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    homework_5.path = [[-1] * total for i in range(total)] #存取節點中插入的中轉點"homework_5."是為了方便在這個函數外也能使用這個變數
    homework_5.ans = "" #初始化一個空字串儲存經過的節點，前面的"homework_5."是為了方便在這個函數外也能使用這個變數
    inf = float('inf')      #無限大
    A = [[inf] * total for i in range(total)]  #存取節點到節點間的路徑

    for i in range(len(matrix)):
        A[matrix[i][0] - 1][matrix[i][1] - 1] = matrix[i][2] #讀取輸入的matrix將路徑長依據起點和終點放進A矩陣

    for k in range(total): #中轉點 k
        for i in range(total): #循環矩陣的 row
            for j in range(total):  #循環矩陣的 column
                if A[i][k] + A[k][j] < A[i][j]: #中轉點路徑比原本路徑小，進入判斷式
                    A[i][j] = A[i][k] + A[k][j] #替換矩陣路徑距離
                    homework_5.path[i][j] = k #添加中轉點k至path
    
    if A[start - 1][end - 1] == inf: #假如start到達不了end，最短距離return-1，經過節點 return None。
        return [-1,None]

    return [A[start - 1][end - 1], str(start) + getpath(start - 1, end - 1) + str(end)] 
def getpath(i, j):
    if homework_5.path[i][j] != -1: #如果對應項有中轉點
        getpath(i, homework_5.path[i][j]) #呼叫自己看起點到這個中轉點之間還有沒有中轉點
        homework_5.ans = homework_5.ans + str(homework_5.path[i][j] +1) #經過的中轉點放入字串儲存
        getpath(homework_5.path[i][j], j) #呼叫自己看這個中轉點到終點之間還有沒有中轉點
    
    return homework_5.ans #回傳經過的中轉點形成的字串


if __name__ == '__main__':
    matrix=[[1, 2, 4], [1, 3, 5], [2, 6, 1], [3, 4, 4], [3, 1, 1], [4, 5, 2], [5, 6, 6], [6, 7, 10], [4, 3, 1]]
    start=4 ; end=6; total=7
    print(homework_5(matrix, start, end, total))
    