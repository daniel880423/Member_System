def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    homework_5.Path = [[-1] * total for i in range(total)] #依據節點數初始化Path矩陣儲存中轉點，前面的"homework_5."是為了方便在這個函數外也能使用這個變數

    homework_5.through = "" #初始化一個空字串儲存經過的節點，前面的"homework_5."是為了方便在這個函數外也能使用這個變數

    A = [[total * 100] * total for i in range(total)] #依據節點數初始化A矩陣儲存節點最短路徑，設total(總節點數)*100是因為題目中假設兩個單純的節點之間路徑長最大是100，total(總節點數)*100就相當於無限大(因為一定最大)

    for i in range(len(matrix)):
        A[matrix[i][0] - 1][matrix[i][1] - 1] = matrix[i][2] #讀取輸入的matrix將路徑長依據起點和終點放進A矩陣

    for k in range(total): #k是假設的中轉點
        for i in range(total): #在A矩陣中尋找是否有經過中轉點的更短路徑，並更新原來的最短路徑
            for j in range(total):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
                    homework_5.Path[i][j] = k #將中轉點存入Path矩陣中對應的那一項
    
    if homework_5.Path[start - 1][end - 1] == -1: #如果起點到終點之間沒有中轉點
        if A[start - 1][end - 1] >= total * 100: #如果起點到終點的最大路徑等於total * 100就代表沒有最短路徑(分別-1是因為主程式輸入的起點終點和python矩陣的index會差1，因為index從0開始數，輸入的節點則是從1開始數)
            return [-1, None]

    return [A[start - 1][end - 1], str(start) + getpath(start - 1, end - 1) + str(end)] #回傳一個list第0項是最短路徑，第1項是經過的節點形成的字串(起點+經過的中轉點+終點)

def getpath(i, j):
    if homework_5.Path[i][j] != -1: #如果對應項有中轉點
        getpath(i, homework_5.Path[i][j]) #呼叫自己看起點到這個中轉點之間還有沒有中轉點
        homework_5.through = homework_5.through + str(homework_5.Path[i][j] + 1) #經過的中轉點放入字串儲存
        getpath(homework_5.Path[i][j], j) #呼叫自己看這個中轉點到終點之間還有沒有中轉點
    
    return homework_5.through #回傳經過的中轉點形成的字串




if __name__ == '__main__':
    matrix = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12], [11, 12, 13], [12, 13, 14], [13, 14, 15], [14, 15, 16], [15, 16, 17]]
    start = 1;end = 15; total = 16
    print(homework_5(matrix, start, end, total))
    